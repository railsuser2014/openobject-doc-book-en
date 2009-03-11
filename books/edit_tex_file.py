#!/usr/bin/python
#-*- encoding: utf8 -*-

import os, sys
from glob import glob
import shutil
import re
import optparse

__version__ = '0.1'
USAGE = """%prog [options] <latex build directory>"""

documentclass_regex = re.compile(r"""^\\documentclass\[(?P<options>[\w,]+)\]\{(?P<class>\w+)\}""")
begin_doc_regex = re.compile(r"""^\\begin\{document\}""")
maketitle_regex = re.compile(r"""^\\maketitle""")
tableofcontents_regex = re.compile(r"""^\\tableofcontents""")
end_foreword_regex = re.compile(r"""SPHINXENDFOREWORDDIRECTIVE""")
printindex_regex = re.compile(r"""^\\printindex""")


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
        shutil.copy2(src, dst)

    def _get_content(self, tex_filename):
        tex_file = open(tex_filename, 'r')
        content = tex_file.readlines()
        tex_file.close()
        return content

    def transform(self):
        for tex_filename in self.tex_files:
            self._make_backup(tex_filename)

            orig_lines = self._get_content(tex_filename)
            try:
                tex_file = open(tex_filename, 'w')
                new_lines = []

                for old_line in orig_lines:

                    match_dclass = documentclass_regex.search(old_line)
                    match_begin_document = begin_doc_regex.search(old_line)
                    match_maketitle = maketitle_regex.search(old_line)
                    match_tableofcontents = tableofcontents_regex.search(old_line)
                    match_end_foreword = end_foreword_regex.search(old_line)
                    match_printindex = printindex_regex.search(old_line)

                    if match_dclass:
                        # set 'book' document class:
                        new_line = """\\documentclass[%s]{book}\n""" % (match_dclass.group('options'), )
                    elif match_begin_document:
                        new_line = '\n'.join([old_line,
                                              "\\frontmatter",
                                              "\\pagenumbering{roman}",
                                              '',
                                             ])
                    elif match_maketitle:
                        new_line = '\n'.join([old_line,
                                              "\\thispagestyle{empty}",
                                              "\\newpage",
                                              "\\pagestyle{plain}",
                                              '',
                                             ])
                    elif match_tableofcontents:
                        new_line = '\n'.join([old_line,
                                              "\\newpage",
                                              '',
                                             ])
                    elif match_end_foreword:
                        new_line = '\n'.join(["",
                                              "\\mainmatter",
                                              "\\pagenumbering{arabic}",
                                              "\\setcounter{page}{1}",
                                              "",
                                             ])
                    elif match_printindex:
                        new_line = '\n'.join(["",
                                              "\\chapter*{\indexname}",
                                              "",
                                              "\\begin{multicols}{2}",
                                              "\\printindex",
                                              "\\end{multicols}",
                                              "",
                                             ])
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
    print os.path.join(os.path.abspath('.'), args[0])

    try:
        book = LatexBook(args, opt)
    except (CommandLineException, ), e:
        sys.stderr.write("%s\n" % (e, ))
        sys.exit(parser.print_usage())

    book.transform()

if __name__ == '__main__':
    _main()

