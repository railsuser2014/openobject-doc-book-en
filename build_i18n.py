#!/usr/bin/python
#-*- encoding: utf8 -*-

import os, sys
import re
import optparse
import pickle


__version__ = '0.1'
USAGE = """%prog [options] <command> <lang code>
eg. %prog create-templates fr source i18n
available commands are:
  - create-templates: create the necessary templates before translating
  - copy-translated: copy the translated files"""


conf = {
    'ext': 'rst',
    'build_default_dir': 'i18n',
}

I18N_PREFIX = '.. i18n:'
I18N_REGEX = r'^\.\. i18n: '
PICKLE_FILENAME = 'i18n.pickle'

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

    _slice_int = 80 # how many chars to display in repr.
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

    def merge(self, next_section):
        self.lines.append('')
        self.lines.extend(next_section.lines)
        next_section.lines = []

    def __repr__(self):
        return """<%s object, lines: %s, directive:%s list:%s "%s">""" % (
            self.__class__.__name__,
            len(self.lines),
            self.has_directive() or 'None',
            self.is_list_item() or 'None',
            self.content[:self._slice_int],
        )


class FileContent(object):
    def __init__(self, lines, lang):
        self.lines = lines
        self.lang = lang
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
        for i, line in enumerate(lines):
            line = line.replace('\n', '')
            orig_section = I18nSection(filter(None, section))
            # line is empty -> this is a paragraph separator
            if not line:
                sections.append(orig_section)
                section = []
                continue
            # (or this is the last line):
            elif i+1 == len(lines):
                section.append(line)
                orig_section = I18nSection(filter(None, section))
                sections.append(orig_section)
                section = []
                continue
            section.append(line)
        return sections

    def merge_sections(self, sections):
        """Merge contiguous sections when necessary (eg.: multiline directives for example)"""
        return sections # XXX for the moment, there are problems with this XXX
#         for i, section in enumerate(sections):
#             next_section = self._get_next_non_empty_section(sections, i)

#             if section and next_section:
#                 if section.has_directive():
#                     section.merge(next_section)
#                 elif section.is_list_item() and next_section.is_list_item():
#                     section.merge(next_section)
#         return sections

    def _get_next_non_empty_section(self, sections, index):
        for section in sections[index+1:]:
            if section:
                return section
        return None


class TemplateContent(FileContent):
    def __init__(self, lines, lang):
        super(TemplateContent, self).__init__(lines, lang)

    def add_i18n_sections(self, sections):
        new_sections = []
        for section in sections:
            i18nsection = I18nSection(section.lines, True)
            new_sections.append(i18nsection)
            new_sections.append(section)
        return new_sections

    def _get_content(self):
        sections = self.build_sections(self.lines)
        sections = self.merge_sections(sections)
        sections = self.add_i18n_sections(sections)

        # build file content:
        content = ''
        for i, section in enumerate(sections):
            if section:
                if not section.i18n:
                    translated_content = ExistingTranslationManager.remember(section.raw_content, self.lang)
                    content += '\n' + translated_content + '\n'
                else:
                    content += '\n' + section.content + '\n'
        return content


class TranslatedContent(FileContent):
    def __init__(self, lines, lang):
        super(TranslatedContent, self).__init__(lines, lang)

    def process_i18n_sections(self, sections):
        processed_sections = []
        for i, section in enumerate(sections):
            if section and not section.i18n:
                previous_section = sections[i-1]
                processed_sections.append(section)
                ExistingTranslationManager.memorize(previous_section.raw_content, section.content, self.lang)

        return processed_sections

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
    def __init__(self, cmd, lang, options=None):
        self.cmd = cmd
        self.lang = lang
        self.src_dir, self.dst_dir = self._get_src_and_dst_dir()
        self.options = options

        self._check_src_dir()
        self.source_content = self.get_structure()
        self._build_dst_structure()
        self.translation_memory = {}

    def _get_src_and_dst_dir(self):
        if self.cmd == 'create-templates':
            src_dir = os.path.join('.', 'source')
            dst_dir = os.path.join(conf['build_default_dir'], 'source', self.lang) + os.sep
        elif self.cmd == 'copy-translated':
            src_dir = os.path.join(conf['build_default_dir'], 'source', self.lang) + os.sep
            dst_dir = os.path.join(conf['build_default_dir'], 'build', self.lang) + os.sep
        return (src_dir, dst_dir)

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
            ExistingTranslationManager.create_memory()
            for k, v in self.source_content.items():
                self.create_templates(k, v)
        elif self.cmd == 'copy-translated':
            ExistingTranslationManager.create_memory()
            for k, v in self.source_content.items():
                self.copy_translated(k, v)
            ExistingTranslationManager.save_memory()

    def _check_src_dir(self):
        """Check that source directory is a valid directory."""
        if not os.path.isdir(self.src_dir):
            if self.cmd == 'copy-translated':
                msg = "Source directory '%s' does not exists."
                msg += " You should probably create the translation templates before trying to copy them."
            else:
                msg = "Source directory '%s' does not exists."
            msg = msg % (self.src_dir, )
            raise OSError(msg)

    def _build_dst_structure(self):
        for d in self.source_content.keys():
            dst_filepath = re.sub(self.src_dir, self.dst_dir, d)
            if not os.path.exists(dst_filepath):
                os.makedirs(dst_filepath)

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

    def create_template(self, src_filepath, dst_filepath):
        src_file = open(src_filepath, 'r')
        src_lines = src_file.readlines()
        src_file.close()
        dst_file = open(dst_filepath, 'w')
        tmpl_content = TemplateContent(src_lines, self.lang).content
        dst_file.write(tmpl_content)
        dst_file.close()

    def create_translated(self, src_filepath, dst_filepath):
        src_file = open(src_filepath, 'r')
        src_lines = src_file.readlines()
        src_file.close()
        dst_file = open(dst_filepath, 'w')
        tmpl_content = TranslatedContent(src_lines, self.lang).content

        dst_file.write(tmpl_content)
        dst_file.close()

    def _check_files(self, directory, files):
        def _set_dst_filepath(filepath):
            dst_filepath = re.sub(self.src_dir, self.dst_dir, filepath).replace('.'+conf['ext'], '') + '.' + conf['ext']
            return dst_filepath

        existing, new = 0, 0
        for filename in files:
            filepath = os.path.join(directory, filename)
            dst_filepath = _set_dst_filepath(filepath)
            new += 1
            if os.path.exists(dst_filepath):
                existing += 1
        return existing, new

    def create_templates(self, directory, files):
        def _set_dst_filepath(filepath):
            dst_filepath = re.sub(self.src_dir, self.dst_dir, filepath).replace('.'+conf['ext'], '') + '.' + conf['ext']
            return dst_filepath

        for filename in files:
            filepath = os.path.join(directory, filename)
            dst_filepath = _set_dst_filepath(filepath)
            self.create_template(filepath, dst_filepath)

    def copy_translated(self, directory, files):
        def _set_dst_filepath(filepath):
            dst_filepath = re.sub(self.src_dir, self.dst_dir, filepath).replace('-'+self.lang, '')
            return dst_filepath

        for filename in files:
            filepath = os.path.join(directory, filename)
            dst_filepath = _set_dst_filepath(filepath)
            self.create_translated(filepath, dst_filepath)


class ExistingTranslationManager(object):
    pickle_filename = PICKLE_FILENAME
    memory = {}

    @classmethod
    def memorize(cls, key, content, lang):
        if not cls.memory.get(lang, None):
            cls.memory[lang] = {key: content}
        else:
            cls.memory[lang][key] = content

    @classmethod
    def remember(cls, key, lang):
        if not cls.memory.get(lang, None):
            content = key
        else:
            try:
                content = cls.memory[lang][key]
            except KeyError:
                content = key
        return content

    @classmethod
    def save_memory(cls):
        try:
            pickled_file = open(cls.pickle_filename, 'w')
            pickle.dump(cls.memory, pickled_file)
        finally:
            pickled_file.close()

    @classmethod
    def create_memory(cls):
        if os.path.exists(cls.pickle_filename):
            try:
                pickled_file = open(cls.pickle_filename, 'r')
                cls.memory = pickle.load(pickled_file)
            finally:
                pickled_file.close()
        else:
            cls.memory = {}


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
        if args_len != 2:
            raise I18nBuilderArgumentException("Incorrect number of arguments. Expected 2, got %d" % (args_len, ))
        cmd = self.args[0]
        if cmd not in self.valid_commands:
            msg = "Command '%s' is not recognized. Valid commands are: %s" % (cmd, ', '.join(self.valid_commands))
            raise I18nBuilderArgumentException(msg)

    def dispatch(self):
        src_mngr = SectionManager(self.args[0], self.args[1], self.options)
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

