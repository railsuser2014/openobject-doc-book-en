#!/usr/bin/python
#-*- encoding: utf8 -*-

import os, sys
from glob import glob
from shutil import copy2 as filecopy
import re
import optparse

__version__ = '0.1'
USAGE = """%prog [options] <latex build directory>"""

rgxs = {
    'begin_conclusion': r"""(?P<directive>SPHINXBEGINCONCLUSIONDIRECTIVE)(?P<after>.*)""",
    'begin_document': r"""^\\begin\{document\}""",
    'begin_figure': r"""(?P<envname>\\begin\{figure\})(?P<opt>.*)""",
    'begin_notice': r"""\\begin\{notice\}""",
    'begin_tabular': r"""(?P<envname>\\begin\{tabular.*?\})(?P<opt>\{.*?\})(?P<coldef>\{.*?\})""",
    'begin_threeparttable': r"""(?P<envname>\\begin\{threeparttable.*?\})""",
    'documentclass': r"""^\\documentclass\[(?P<opt>[\w,]+)\]\{(?P<class>\w+)\}""",
    'end_document': r"""^\\end\{document\}""",
    'end_figure': r"""(?P<before>.*)(?P<envname>\\end\{figure\})(?P<after>)""",
    'end_foreword': r"""(?P<directive>SPHINXENDFOREWORDDIRECTIVE)(?P<after>.*)""",
    'end_notice': r"""\\end\{notice\}""",
    'end_tabular': r"""(?P<envname>\\end\{tabular.*?\})""",
    'end_threeparttable': r"""(?P<envname>\\end\{threeparttable.*?\})""",
    'fancychapter': r"""^\\usepackage\[Bjarne\]\{fncychap\}""",
    'maketitle': r"""^\\maketitle""",
    'printindex': r"""^\\printindex""",
    'tableofcontents': r"""^\\tableofcontents""",
}


class LatexRgx(object):
    def __init__(self, regexes):
        self.regexes = regexes
        self.compiled = {}
        self.compile_regexes()

    def compile_regexes(self):
        for k, v in self.regexes.items():
            self.compiled[k] = re.compile(v)

    def match(self, s):
        for rgxname, rgxobj in self.compiled.items():
            matchobj = rgxobj.search(s)
            if matchobj:
                return (rgxname, matchobj)
        return (None, None)


class LatexState(object):
    def __init__(self):
        self.in_threeparttable = False
        self.in_begin_document = False
        self.in_begin_notice = False


class LatexBook(object):
    def __init__(self, args, options):
        self._check_args(args, options)
        self.build_dir = args[0]
        self.tex_files = self._get_tex_files()
        self.tex_rgx = LatexRgx(rgxs)
        self.state = LatexState()

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
                for i, old_line in enumerate(orig_lines):
                    rgxname, matchobj = self.tex_rgx.match(old_line)

                    if rgxname:
                        if rgxname == 'documentclass':
                            # set 'book' document class:
                            new_line = """\\documentclass[%s]{book}\n""" % (matchobj.group('opt'), )
                        elif rgxname == 'begin_document':
                            self.state.in_begin_document = True
                            new_line = '\n'.join([old_line,
                                                  "",
                                                  r"\frontmatter",
                                                  r"\pagenumbering{roman}",
                                                  "",
                                                 ])
                        elif rgxname == 'end_document':
                            self.state.in_begin_document = False
                            new_line = old_line
                        elif rgxname == 'fancychapter':
                            new_line = '\n'.join([
                                                  r"\usepackage[Tiny]{fncychap}",
                                                  "",
                                                 ])
                        elif rgxname == 'maketitle':
                            new_line = '\n'.join([old_line,
                                                  r"\thispagestyle{empty}",
                                                  r"\newpage",
                                                  "",
                                                 ])
                        elif rgxname == 'tableofcontents':
                            new_line = '\n'.join([old_line,
                                                  r"\newpage",
                                                  "",
                                                 ])
                        elif rgxname == 'end_foreword':
                            new_line = '\n'.join(["",
                                                  r"\mainmatter",
                                                  r"\pagestyle{fancy}",
                                                  r"\pagenumbering{arabic}",
                                                  r"\setcounter{page}{1}",
                                                  "",
                                                 ])
                        elif rgxname == 'begin_conclusion':
                            part = matchobj.group('after')
                            new_line = '\n'.join(["",
                                                  r"\backmatter",
                                                  r"\pagestyle{plain}",
                                                  part
                                                 ])
                        elif rgxname == 'printindex':
                            new_line = '\n'.join(["",
                                                  r"\chapter*{\indexname}",
                                                  "",
                                                  r"\begin{multicols}{2}",
                                                  r"\printindex",
                                                  r"\end{multicols}",
                                                  "",
                                                 ])
                        elif rgxname == 'begin_figure':
                            if self.state.in_begin_notice:
                                new_line = '\n'.join([r"\begin{staticfigure}",
                                                      ""
                                                     ])
                            else:
                                new_line = '\n'.join([old_line.strip('\n\r'),
                                                      r"\begin{minipage}[htbp]{\linewidth}",
                                                      "",
                                                     ])
                        elif rgxname == 'end_figure':
                            if self.state.in_begin_notice:
                                # in a notice env, figure -> staticfigure
                                new_line = '\n'.join([matchobj.group('before'),
                                                      r"\end{staticfigure}",
                                                      matchobj.group('after'),
                                                      ""
                                                     ])
                            else:
                                new_line = '\n'.join([matchobj.group('before'),
                                                      r"\end{minipage}",
                                                      matchobj.group('envname'),
                                                      matchobj.group('after'),
                                                      ""
                                                     ])
                        elif rgxname == 'begin_tabular':
                            if self.state.in_begin_document:
                                coldef = matchobj.group('coldef').replace('|', '')
                                table_line = "%s%s%s\n" % (matchobj.group('envname'),
                                                           matchobj.group('opt'),
                                                           coldef,
                                                          )
                                if self.state.in_threeparttable:
                                    new_line = table_line
                                else:
                                    new_line = '\n'.join([r"\begin{center}",
                                                          table_line,
                                                          "",
                                                         ])
                        elif rgxname == 'end_tabular':
                            if self.state.in_begin_document and not self.state.in_threeparttable:
                                new_line = '\n'.join([old_line.strip('\n\r'),
                                                      r"\end{center}",
                                                      "",
                                                     ])
                            else:
                                new_line = old_line
                        elif rgxname == 'begin_threeparttable':
                            self.state.in_threeparttable = True
                            new_line = '\n'.join([r"\begin{center}",
                                                  old_line,
                                                  "",
                                                 ])
                        elif rgxname == 'end_threeparttable':
                            self.state.in_threeparttable = False
                            old_line = old_line.strip('\n\r')
                            new_line = '\n'.join([old_line,
                                                  r"\end{center}",
                                                  "",
                                                 ])
                        elif rgxname == 'begin_notice':
                            self.state.in_begin_notice = True
                            i_next_non_blank = self._get_next_non_blank_line_index(i, orig_lines)
                            new_line = old_line
                        elif rgxname == 'end_notice':
                            self.state.in_begin_notice = False
                            new_line = old_line
                        else:
                            raise UnhandledMatchException("Matching object '%s' was not handled (matching line: %s)." % (rgxname, i))

                    elif i == i_next_non_blank:
                        new_line = '\n'.join([self.add_tex_command('strong', old_line),
                                              "",
                                             ])
                        i_next_non_blank = None # job done -> reset i_next_non_blank
                    else:
                        new_line = old_line
                    new_lines.append(new_line)

                new_lines.append("\n".join(["%% ", "%% vi: fdm=manual", "%% "]))
                tex_file.writelines(new_lines)
            finally:
                tex_file.close()


class CommandLineException(Exception):
    pass


class UnhandledMatchException(Exception):
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

