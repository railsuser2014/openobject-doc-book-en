#!/usr/bin/python
#-*- encoding: utf8 -*-

import os, sys
from glob import glob
from shutil import copy2 as filecopy
import re
import optparse

__version__ = '0.1'
USAGE = """%prog [options] <latex build directory>"""

documentclass_regex = re.compile(r"""^\\documentclass\[(?P<options>[\w,]+)\]\{(?P<class>\w+)\}""")
begin_doc_regex = re.compile(r"""^\\begin\{document\}""")
end_doc_regex = re.compile(r"""^\\end\{document\}""")
maketitle_regex = re.compile(r"""^\\maketitle""")
tableofcontents_regex = re.compile(r"""^\\tableofcontents""")
end_foreword_regex = re.compile(r"""(?P<directive>SPHINXENDFOREWORDDIRECTIVE)(?P<after>.*)""")
begin_conclusion_regex = re.compile(r"""(?P<directive>SPHINXBEGINCONCLUSIONDIRECTIVE)(?P<after>.*)""")
printindex_regex = re.compile(r"""^\\printindex""")
fancychapter_regex = re.compile(r"""^\\usepackage\[Bjarne\]\{fncychap\}""")
begin_figure_regex = re.compile(r"""\\begin\{figure\}""")
end_figure_regex = re.compile(r"""\\end\{figure\}""")
begin_tabular_regex = re.compile(r"""(?P<envname>\\begin\{tabular.*?\})(?P<opt>\{.*?\})(?P<coldef>\{.*?\})""")
end_tabular_regex = re.compile(r"""(?P<envname>\\end\{tabular.*?\})""")
begin_threeparttable_regex = re.compile(r"""(?P<envname>\\begin\{threeparttable.*?\})""")
end_threeparttable_regex = re.compile(r"""(?P<envname>\\end\{threeparttable.*?\})""")
begin_notice_regex = re.compile(r"""\\begin\{notice\}""")
conclusion_regex = re.compile(r"""\\begin\{notice\}""")


class LatexBook(object):
    def __init__(self, args, options):
        self._check_args(args, options)
        self.build_dir = args[0]
        self.tex_files = self._get_tex_files()

    def _check_args(self, args, options):
        if len(args) != 1:
            raise CommandLineException("Wrong number of arguments: expected 1, got %s" % (len(args), ))

    def _get_tex_files(self):
        return glob('%s/*.tex' % (self.build_dir, ))

    def _make_backup(self, src):
        dst = "%s.orig" % (src, )
        if os.path.exists(dst):
            os.unlink(dst)
        filecopy(src, dst)

    def _get_content(self, tex_filename):
        tex_file = open(tex_filename, 'r')
        content = tex_file.readlines()
        tex_file.close()
        return content

    def _get_next_non_blank_line_index(self, where, lines):
        i = where + 1
        while True:
            next_line = lines[i]
            if next_line.strip():
                return i
        return None

    def add_tex_command(self, cmd, s):
        def are_curly_brackets_matching(s):
            return s.count('{') == s.count('}')
        s = s.strip('\r\n')
        if are_curly_brackets_matching(s):
            return r"\%s{%s}" % (cmd, s)
        else:
            raise Exception("Non matching curly brackets in string: %s" % s)

    def transform(self):
        for tex_filename in self.tex_files:
            self._make_backup(tex_filename)

            orig_lines = self._get_content(tex_filename)
            try:
                tex_file = open(tex_filename, 'w')
                new_lines = []

                i_next_non_blank = None
                in_threeparttable = False
                in_begin_document = False
                for i, old_line in enumerate(orig_lines):

                    match_dclass = documentclass_regex.search(old_line)
                    match_begin_document = begin_doc_regex.search(old_line)
                    match_end_document = end_doc_regex.search(old_line)
                    match_maketitle = maketitle_regex.search(old_line)
                    match_tableofcontents = tableofcontents_regex.search(old_line)
                    match_end_foreword = end_foreword_regex.search(old_line)
                    match_begin_conclusion = begin_conclusion_regex.search(old_line)
                    match_printindex = printindex_regex.search(old_line)
                    match_fancychapter = fancychapter_regex.search(old_line)
                    match_begin_figure = begin_figure_regex.search(old_line)
                    match_end_figure = end_figure_regex.search(old_line)
                    match_begin_tabular = begin_tabular_regex.search(old_line)
                    match_end_tabular = end_tabular_regex.search(old_line)
                    match_begin_threeparttable = begin_threeparttable_regex.search(old_line)
                    match_end_threeparttable = end_threeparttable_regex.search(old_line)
                    match_begin_notice = begin_notice_regex.search(old_line)

                    if match_dclass:
                        # set 'book' document class:
                        new_line = """\\documentclass[%s]{book}\n""" % (match_dclass.group('options'), )
                    elif match_begin_document:
                        in_begin_document = True
                        new_line = '\n'.join([old_line,
                                              "",
                                              r"\frontmatter",
                                              r"\pagenumbering{roman}",
                                              "",
                                             ])
                    elif match_end_document:
                        in_begin_document = False
                        new_line = old_line
                    elif match_fancychapter:
                        new_line = '\n'.join([
                                              r"\usepackage[Tiny]{fncychap}",
                                              "",
                                             ])
                    elif match_maketitle:
                        new_line = '\n'.join([old_line,
                                              r"\thispagestyle{empty}",
                                              r"\newpage",
                                              #r"\pagestyle{plain}",
                                              "",
                                             ])
                    elif match_tableofcontents:
                        new_line = '\n'.join([old_line,
                                              r"\newpage",
                                              "",
                                             ])
                    elif match_end_foreword:
                        new_line = '\n'.join(["",
                                              r"\mainmatter",
                                              r"\pagestyle{fancy}",
                                              r"\pagenumbering{arabic}",
                                              r"\setcounter{page}{1}",
                                              "",
                                             ])
                    elif match_begin_conclusion:
                        # BEFORE:
                        # \resetcurrentobjects
                        # \part*{Conclusion}
                        # \addcontentsline{toc}{part}{Conclusion}

                        # AFTER
                        # \backmatter
                        # \resetcurrentobjects
                        # \part*{Conclusion}
                        # \addcontentsline{toc}{part}{Conclusion}
                        # \pagestyle{plain}
                        part = match_begin_conclusion.group('after')
                        new_line = '\n'.join(["",
                                              r"\backmatter",
                                              r"\pagestyle{plain}",
                                              part
                                             ])
                    elif match_printindex:
                        new_line = '\n'.join(["",
                                              r"\chapter*{\indexname}",
                                              "",
                                              r"\begin{multicols}{2}",
                                              r"\printindex",
                                              r"\end{multicols}",
                                              "",
                                             ])
                    elif match_begin_figure:
                        new_line = '\n'.join(["",
                                              r"\begin{minipage}[b]{\linewidth}",
                                              old_line,
                                             ])
                    elif match_end_figure:
                        new_line = '\n'.join([old_line,
                                              r"\end{minipage}",
                                              "",
                                             ])
                    elif match_begin_tabular:
                        if in_begin_document:
                            coldef = match_begin_tabular.group('coldef').replace('|', '')
                            table_line = "%s%s%s\n" % (match_begin_tabular.group('envname'),
                                                       match_begin_tabular.group('opt'),
                                                       coldef,
                                                      )
                            if in_threeparttable:
                                new_line = table_line
                            else:
                                new_line = '\n'.join([r"\begin{center}",
                                                      table_line,
                                                      "",
                                                     ])
                    elif match_end_tabular:
                        if in_begin_document and not in_threeparttable:
                            new_line = '\n'.join([old_line.strip('\n\r'),
                                                  r"\end{center}",
                                                  "",
                                                 ])
                        else:
                            new_line = old_line
                    elif match_begin_threeparttable:
                        in_threeparttable = True
                        new_line = '\n'.join([r"\begin{center}",
                                              old_line,
                                              "",
                                             ])
                    elif match_end_threeparttable:
                        in_threeparttable = False
                        old_line = old_line.strip('\n\r')
                        new_line = '\n'.join([old_line,
                                              r"\end{center}",
                                              "",
                                             ])
                    elif match_begin_notice:
                        i_next_non_blank = self._get_next_non_blank_line_index(i, orig_lines)
                        new_line = old_line
                    elif i == i_next_non_blank:
                        new_line = '\n'.join([self.add_tex_command('strong', old_line),
                                              ""])
                        i_next_non_blank = None # job done -> reset i_next_non_blank
                    else:
                        new_line = old_line
                    new_lines.append(new_line)

                tex_file.writelines(new_lines)
            finally:
                tex_file.close()


class CommandLineException(Exception):
    pass


def _main():
    parser = optparse.OptionParser(usage=USAGE, version=__version__)
    (opt, args) = parser.parse_args()

    try:
        book = LatexBook(args, opt)
    except (CommandLineException, ), e:
        sys.stderr.write("%s\n" % (e, ))
        sys.exit(parser.print_usage())

    book.transform()

if __name__ == '__main__':
    _main()

