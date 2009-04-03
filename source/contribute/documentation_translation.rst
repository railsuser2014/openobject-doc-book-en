
How to translate the Open Object Documentation in your language
===============================================================

Prerequisite
------------

You should be able to build the untranslated documentation. So `Sphinx
<http://sphinx.pocoo.org>`_ should be installed on your system and you should
know how to use it.

If this is not the case, please read the `Community Guide
<http://doc.openerp.com/contribute/documentation_process.html#building-the-documentation>`_.

Understanding the directory structure
-------------------------------------

We are supposing that **<openobject-doc>** is the root of the Open Object
documentation baazar branch.

The *untranslated sources* are located in **<openobject-doc>/source**.

The translated documentation is located in **<openobject-doc>>/i18n/<lang>/source**.

For example, the documentation in french will be
located in **<openobject-doc>/i18n/fr/source** and it will be built
in **<openobject-doc>/i18n/fr/build/html** for example.

Summary
+++++++

.. csv-table::
    :header: "Directory", "Description"
    :widths: 5,5

    <openobject-doc>/source,untranslated sources
    <openobject-doc>/i18n/<lang>/source,translated sources
    <openobject-doc>/i18n/<lang>/build/html,translated documentation in html

Creating the translation directory structure
--------------------------------------------

Use the **make** command (with target **i18n**) to create the translation
templates. You'll need to pass the language as an additional parameter to the *make* command.

For example, supposing you want to translate the documentation in french: ::

  make i18n LANG=fr

This command will do several things:

* create these directories, if they does not exist yet:

  * i18n
  * i18n/fr
  * i18n/fr/source
  * i18n/fr/build

* copy files in *i18n/fr/* required for the html build:

  * MakeFile
  * conf.py

* create the *translation templates* based on the untranslated restructured text files. They will be created in *i18n/fr/source*

* copy all the other necessary files (images for example)


Translation templates
---------------------

The template structure for a given file is very simple. Each text section is
prepended by the original context. Here is a title, for example: ::

  .. i18n: %%%%%%%%%%%%%%%%%%%%%%%%%
  .. i18n: Open Object Documentation
  .. i18n: %%%%%%%%%%%%%%%%%%%%%%%%%

  %%%%%%%%%%%%%%%%%%%%%%%%%
  Open Object Documentation
  %%%%%%%%%%%%%%%%%%%%%%%%%

The context is a commented section starting with **.. i18n:**. It helps you
understand the section in its context. It also helps you remember the original
section.

And here is the translated section: ::

  .. i18n: %%%%%%%%%%%%%%%%%%%%%%%%%
  .. i18n: Open Object Documentation
  .. i18n: %%%%%%%%%%%%%%%%%%%%%%%%%

  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%
  Documentation sur Open Object
  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Managing source changes
-----------------------

If someone adds or changes something in the documentation, that section will
have to be retranslated but all the other sections will hopefully keep their
translation.

When you will get the documentation changes with bzr pull (for example), the
new sections and some changed sections will be reset to the untranslated text
when you will rebuild the translation with *make i18n LANG=fr*.

------

At the moment, this script is in alpha status and has not been thoroughly
tested. It should work but expects some bugs to pop up at unexpected times.


