#!/usr/bin/python
#-*- encoding: utf8 -*-

import os, sys
import re
import optparse
import pickle

from pprint import pprint as pp

__version__ = '0.1'
USAGE = """%prog [options] <command> <lang code> <source directory> <destination directory>
eg. %prog create-templates fr source i18n
available commands are:
  - create-templates: create the necessary templates before translating
  - copy-translated: copy the translated files"""


conf = {
    'ext': 'rst',
    'build_default_dir': 'i18n',
}


IGNORED_RST_DIRECTIVES = [ # XXX not used for the moment
    'toctree',
]
I18N_PREFIX = '.. i18n:'
I18N_REGEX = r'^\.\. i18n: '
PICKLE_FILE = 'i18n.pickle'

has_directive_regex = re.compile(r"""\.\.\s+(?P<directive>\w+)::(?P<content>.*)""")
is_list_item_regex = re.compile(r"""^\s*(?P<list_item_char>#\.|\*|-|\d+\.){1,1}\s+(?P<content>.*)""")


def propertx(fct):
    """Decorator to simplify the use of property.
       Like @property for attrs who need more than a getter.
       For getter only property use @property."""
    arg = [None, None, None, None]
    for i, f in enumerate(fct()):
        arg[i] = f
    if not arg[3]:
        arg[3] = fct.__doc__

    return property(*arg)


class I18nSection(object):
    def __init__(self, lines, i18n=False):
        self.lines = lines
        self._raw_content = ''
        self._content = ''
        self._i18n = i18n

    def __len__(self):
        return len(self.lines)

    @propertx
    def content():
        def get(self):
            if self._i18n:
                lines = ["%s %s" % (I18N_PREFIX, line,) for line in self.lines]
            else:
                lines = self.lines
            return '\n'.join(lines)
        return (get, None)

    @propertx
    def raw_content():
        def get(self):
            return '\n'.join([re.sub(I18N_REGEX, '', line) for line in self.lines])
        return (get, None)

    @propertx
    def i18n():
        """is this an i18n section or an original section ?"""
        def get(self):
            return self._i18n or self.content.startswith(I18N_PREFIX)
        return (get, None)

    def has_directive(self):
        match_obj = has_directive_regex.search(self.content)
        if match_obj:
            return match_obj.group('directive')
        else:
            return False

    def is_list_item(self):
        match_obj = is_list_item_regex.search(self.content)
        if match_obj:
            return match_obj.group('list_item_char')
        else:
            return False

    def merge(self, i18nsection):
        self.lines.append('')
        self.lines.extend(i18nsection.lines)
        i18nsection.lines = []

    def __repr__(self):
        return """<%s object, lines: %s, directive:%s list:%s "%s">""" % (
            self.__class__.__name__,
            len(self.lines),
            self.has_directive(),
            self.is_list_item(),
            self.content[:12],
        )


class FileContent(object):
    def __init__(self, lines):
        self.lines = lines
        self._content = ''

    def _get_content(self):
        raise NotImplementedError("Please implement this method in a subclass")

    @propertx
    def content():
        def get(self):
            return self._get_content()
        return (get, None)

    def build_sections(self, lines):
        # separate file sections:
        section = []
        sections = []
        for line in lines:
            line = line.replace('\n', '')
            orig_section = I18nSection(filter(None, section))
            if not line: # line is empty -> this is a paragraph separator
                sections.append(orig_section)
                section = []
                continue
            section.append(line)
        return sections

    def merge_sections(self, sections):
        """Merge contiguous sections when necessary (eg.: multiline directives for example)"""
        #pp(sections)
        for i, section in enumerate(sections):
            next_section = self._get_next_non_empty_section(sections, i)

            if section and next_section:
                #print section
                #print next_section
                #print
                if section.has_directive():
                    section.merge(next_section)
                elif section.is_list_item() and next_section.is_list_item():
                    section.merge(next_section)
        #pp(sections)
        return sections

    def _get_next_non_empty_section(self, sections, index):
        for section in sections[index+1:]:
            if section:
                return section
        return None


class TemplateContent(FileContent):
    def __init__(self, lines):
        super(TemplateContent, self).__init__(lines)

    def add_i18n_sections(self, sections):
        new_sections = []
        for section in sections:
            i18nsection = I18nSection(section.lines, True)
            new_sections.append(i18nsection)
            new_sections.append(section)
        return new_sections

    def _get_content(self):
        sections = self.build_sections(self.lines)
        print len(sections)
        sections = self.merge_sections(sections)
        sections = self.add_i18n_sections(sections)

        # build file content:
        content = ''
        for section in sections:
            if section:
                content += '\n' + section.content + '\n'
        return content


class TranslatedContent(FileContent):
    def __init__(self, lines):
        super(TranslatedContent, self).__init__(lines)

    def _save_pickled_dict(self, dico):
        print dico

    def _get_pickled_dict(self):
        dico = {}
        return dico

    def process_i18n_sections(self, sections):
        new_sections = []
        dico = {}
        for i, section in enumerate(sections):
            if section and section.i18n:
                next_section = self._get_next_non_empty_section(sections, i)
                if next_section is not None:
                    new_sections.append(next_section)
                    dico[section.raw_content] = next_section.content

        self._save_pickled_dict(dico)
        return new_sections

    def _get_content(self):
        sections = self.build_sections(self.lines)
        sections = self.process_i18n_sections(sections)

        # build file content:
        content = ''
        for section in sections:
            if section:
                content += '\n' + section.content + '\n'
        return content


class SectionManager(object):
    def __init__(self, cmd, lang, src_dir, dest_dir, options=None):
        self.cmd = cmd
        self.lang = lang
        self.src_dir = src_dir + os.sep
        self.dest_dir = os.path.join(conf['build_default_dir'], dest_dir, self.lang, 'source') + os.sep
        self.options = options

        self._check_src_dir()
        self.source_content = self.get_structure()
        self._build_dest_structure()

    def run(self):
        # checking that files are new to avoid overwriting a big work:
        allexisting, allnew = 0, 0
        for k, v in self.source_content.items():
            existing, new = self._check_files(k, v)
            allexisting += existing
            allnew += new

        if not self.options.force:
            if float(allexisting) / float(allnew) > 0.001:
                question = raw_input("Some files are already existing. Are you sure you want to overwrite them ? [y/n]\n")
                if question not in ('y', 'n'):
                    sys.stderr.write("Please answer with 'y' or 'n'.\n")
                if question == 'n':
                    sys.exit("Doing nothing.")

        if self.cmd == 'create-templates':
            for k, v in self.source_content.items():
                self.create_templates(k, v)
        elif self.cmd == 'copy-translated':
            for k, v in self.source_content.items():
                self.copy_translated(k, v)

    def _check_src_dir(self):
        """Check that source directory is a valid directory."""
        if not os.path.isdir(self.src_dir):
            raise OSError("Source directory does not exists")

    def _build_dest_structure(self):
        for d in self.source_content.keys():
            dest_filepath = re.sub(self.src_dir, self.dest_dir, d)
            if not os.path.exists(dest_filepath):
                os.makedirs(dest_filepath)

    def get_structure(self):
        """Get the source directory structure"""
        def _visit_func(arg, dirname, names):
            content[dirname] = [name for name in names if name.endswith('.'+conf['ext'])]
        content = {}
        os.path.walk(self.src_dir, _visit_func, None)
        for directory in os.listdir(self.src_dir):
            directory = os.path.join(self.src_dir, directory)
            os.path.walk(directory, _visit_func, None)
        return content

    def create_template(self, src_filepath, dest_filepath):
        src_file = open(src_filepath, 'r')
        src_lines = src_file.readlines()
        src_file.close()
        dest_file = open(dest_filepath, 'w')
        tmpl_content = TemplateContent(src_lines).content
        dest_file.write(tmpl_content)
        dest_file.close()

    def create_translated(self, src_filepath, dest_filepath):
        src_file = open(src_filepath, 'r')
        src_lines = src_file.readlines()
        src_file.close()
        dest_file = open(dest_filepath, 'w')
        tmpl_content = TranslatedContent(src_lines).content
        dest_file.write(tmpl_content)
        dest_file.close()

    def _check_files(self, d, files):
        def _set_dest_filepath(filepath):
            dest_filepath = re.sub(self.src_dir, self.dest_dir, filepath).replace('.'+conf['ext'], '') + '.' + conf['ext']
            return dest_filepath

        existing, new = 0, 0
        for filename in files:
            filepath = os.path.join(d, filename)
            dest_filepath = _set_dest_filepath(filepath)
            new += 1
            if os.path.exists(dest_filepath):
                existing += 1
        return existing, new

    def create_templates(self, d, files):
        def _set_dest_filepath(filepath):
            dest_filepath = re.sub(self.src_dir, self.dest_dir, filepath).replace('.'+conf['ext'], '') + '.' + conf['ext']
            return dest_filepath

        for filename in files:
            filepath = os.path.join(d, filename)
            dest_filepath = _set_dest_filepath(filepath)
            self.create_template(filepath, dest_filepath)

    def copy_translated(self, d, files):
        def _set_dest_filepath(filepath):
            dest_filepath = re.sub(self.src_dir, self.dest_dir, filepath).replace('-'+self.lang, '')
            return dest_filepath

        for filename in files:
            filepath = os.path.join(d, filename)
            dest_filepath = _set_dest_filepath(filepath)
            self.create_translated(filepath, dest_filepath)


class I18nBuilderArgumentException(Exception):
    pass


class ArgDispatcher(object):
    def __init__(self, args, opts):
        self.valid_commands = ('create-templates', 'copy-translated')
        self.args = args
        self.options = opts
        self._check_args()

    def _check_args(self):
        args_len = len(self.args)
        if args_len != 4:
            raise I18nBuilderArgumentException("Incorrect number of arguments. Expected 4, got %d" % (args_len, ))
        cmd = self.args[0]
        if cmd not in self.valid_commands:
            msg = "Command '%s' is not recognized. Valid commands are: %s" % (cmd, ', '.join(self.valid_commands))
            raise I18nBuilderArgumentException(msg)

    def dispatch(self):
        src_mngr = SectionManager(self.args[0], self.args[1], self.args[2], self.args[3], self.options)
        src_mngr.run()


def _main():
    parser = optparse.OptionParser(usage=USAGE, version=__version__)
    parser.add_option('', '--force', dest='force', default=False, action="store_true", help="Force the copy without prompting for confirmation")
    (opt, args) = parser.parse_args()

    try:
        argdispatcher = ArgDispatcher(args, opt)
    except (I18nBuilderArgumentException, ), e:
        sys.stderr.write("%s\n" % (e, ))
        sys.exit(parser.print_usage())
    try:
        argdispatcher.dispatch()
    except (OSError, ), e:
        sys.exit("Error: %s" % (e, ))

if __name__ == '__main__':
    _main()

