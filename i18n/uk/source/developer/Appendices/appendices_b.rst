
.. i18n: Releasing a module
.. i18n: ==================

Releasing a module
==================

.. i18n: Introduction
.. i18n: ------------

Introduction
------------

.. i18n: You can publish your work under our systems to:

You can publish your work under our systems to:

.. i18n:     * Get help from contributors or interrested partners for the development
.. i18n:     * Get feedback from testers and translators
.. i18n:     * Get your module in the next distribution/version of Open ERP (if accepted by the editor) so that you do not have to manage migrations, testing per version, ... 

    * Get help from contributors or interrested partners for the development
    * Get feedback from testers and translators
    * Get your module in the next distribution/version of Open ERP (if accepted by the editor) so that you do not have to manage migrations, testing per version, ... 

.. i18n: Open Forge
.. i18n: ----------

Open Forge
----------

.. i18n: Here is the process of publishing a module or patch:

Here is the process of publishing a module or patch:

.. i18n:    1. Create a project on http://OpenForge.com
.. i18n:    2. Upload your work on your Open Forge project
.. i18n:    3. Create an entry on the module repository of Open ERP's website 

   1. Create a project on http://OpenForge.com
   2. Upload your work on your Open Forge project
   3. Create an entry on the module repository of Open ERP's website 

.. i18n: The Open Forge has tools to help your team collaborate, like message forums, tasks tracker and mailing lists; tools to create and control access to Source Code Management repositories. It is the central repository of collaborative developments for Open ERP. 

The Open Forge has tools to help your team collaborate, like message forums, tasks tracker and mailing lists; tools to create and control access to Source Code Management repositories. It is the central repository of collaborative developments for Open ERP. 

.. i18n: Translations
.. i18n: ============

Translations
============

.. i18n: Open ERP is multilingual. You can add as many languages as you wish. Each user may work with the interface in his own language. Moreover, some resources (the text of reports, product names, etc.) may also be translated.

Open ERP is multilingual. You can add as many languages as you wish. Each user may work with the interface in his own language. Moreover, some resources (the text of reports, product names, etc.) may also be translated.

.. i18n: This section explains how to change the language of the program shown to individual users, and how to add new languages to Open ERP.

This section explains how to change the language of the program shown to individual users, and how to add new languages to Open ERP.

.. i18n: Nearly all the labels used in the interface are stored on the server. In the same way, the translations are also stored on the server. By default, the English dictionary is stored on the server, so if the users want to try Open ERP in a language other than English, then you have to store these languages definitions on the server.

Nearly all the labels used in the interface are stored on the server. In the same way, the translations are also stored on the server. By default, the English dictionary is stored on the server, so if the users want to try Open ERP in a language other than English, then you have to store these languages definitions on the server.

.. i18n: However, it is not possible to store "everything" on the server. Indeed, the user gets some menus, buttons, etc... that must contain some text *even before* being connected to the server. These few words and sentences are translated using GETTEXT. The chosen language by default for these is the language of the computer from which the user connects.

However, it is not possible to store "everything" on the server. Indeed, the user gets some menus, buttons, etc... that must contain some text *even before* being connected to the server. These few words and sentences are translated using GETTEXT. The chosen language by default for these is the language of the computer from which the user connects.

.. i18n: The translation system of Open ERP is not limited to interface texts; it also works with reports and the "content" of some database fields. Obviously, not all the database fields need to be translated. The fields where the content is multilingual are marked thus by a flag :

The translation system of Open ERP is not limited to interface texts; it also works with reports and the "content" of some database fields. Obviously, not all the database fields need to be translated. The fields where the content is multilingual are marked thus by a flag :

.. i18n: .. figure::  images/field_flag.png
.. i18n:    :scale: 120
.. i18n:    :align: left
.. i18n: 
.. i18n: 	
.. i18n: How to change the language of the user interface ?
.. i18n: --------------------------------------------------

.. figure::  images/field_flag.png
   :scale: 120
   :align: left

	
How to change the language of the user interface ?
--------------------------------------------------

.. i18n: The language is a user preference. To change the language of the current user, click on the menu: User > Preferences.

The language is a user preference. To change the language of the current user, click on the menu: User > Preferences.

.. i18n: .. figure::  images/trans_user_pref.png
.. i18n:    :scale: 120
.. i18n:    :align: left

.. figure::  images/trans_user_pref.png
   :scale: 120
   :align: left

.. i18n: An administrator may also modify the preferences of a user (including the language of the interface) in the menu: Administration > Users > Users. He merely has to choose a user and toggle on "preferences".

An administrator may also modify the preferences of a user (including the language of the interface) in the menu: Administration > Users > Users. He merely has to choose a user and toggle on "preferences".

.. i18n: .. figure::  images/menu_bar_pref.png
.. i18n:    :scale: 120
.. i18n:    :align: left

.. figure::  images/menu_bar_pref.png
   :scale: 120
   :align: left

.. i18n: Store a translation file on the server
.. i18n: --------------------------------------

Store a translation file on the server
--------------------------------------

.. i18n: To import a file having translations, use this command:

To import a file having translations, use this command:

.. i18n:     ./openerp_server.py --i18n-import=file.csv -l **LANG** 

    ./openerp_server.py --i18n-import=file.csv -l **LANG** 

.. i18n: where **LANG** is the language of the translation data in the CSV file.

where **LANG** is the language of the translation data in the CSV file.

.. i18n: Note that the translation file must be encoded in **UTF8!**

Note that the translation file must be encoded in **UTF8!**

.. i18n: Translate to a new language
.. i18n: ---------------------------

Translate to a new language
---------------------------

.. i18n: **Please keep in mind to use the same translation string for identical sources**	. Launchpad Online Translation may give helpful hints.

**Please keep in mind to use the same translation string for identical sources**	. Launchpad Online Translation may give helpful hints.

.. i18n: More information on accelerators on this website: http://translate.sourceforge.net/wiki/guide/translation/accelerators

More information on accelerators on this website: http://translate.sourceforge.net/wiki/guide/translation/accelerators

.. i18n: To translate or modify the translation of a language already translated, you have to:

To translate or modify the translation of a language already translated, you have to:

.. i18n: 1. Export all the sentences to translate in a CSV file
.. i18n: +++++++++++++++++++++++++++++++++++++++++++++++++++++++

1. Export all the sentences to translate in a CSV file
+++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. i18n: To export this file, use this command:

To export this file, use this command:

.. i18n:         ./openerp_server.py --i18n-export=file.csv -l**LANG** 

        ./openerp_server.py --i18n-export=file.csv -l**LANG** 

.. i18n: where **LANG** is the language to which you want to translate the program.

where **LANG** is the language to which you want to translate the program.

.. i18n: 2. Translate the last column of the file
.. i18n: ++++++++++++++++++++++++++++++++++++++++

2. Translate the last column of the file
++++++++++++++++++++++++++++++++++++++++

.. i18n: You can make a translation for a language, which has already been translated or for a new one. If you ask for a language already translated, the sentences already translated will be written in the last column.

You can make a translation for a language, which has already been translated or for a new one. If you ask for a language already translated, the sentences already translated will be written in the last column.

.. i18n: For example, here are the first lines of a translation file (Dutch):
.. i18n:  
.. i18n: +--------+------------------------+---------+----------------+--------------------+
.. i18n: | type   | name                   | res_id  |      src       |   value            |
.. i18n: +--------+------------------------+---------+----------------+--------------------+
.. i18n: | field  |"account.account,code"  |  0      |    Code        |    Code 		  |
.. i18n: +--------+------------------------+---------+----------------+--------------------+
.. i18n: |  field | "account.account,name" |  0      |	 Name        |   Name             | 
.. i18n: +--------+------------------------+---------+----------------+--------------------+
.. i18n: |  model | "account.account,name" |  2      |	 Assets      |   Aktiva           |
.. i18n: +--------+------------------------+---------+----------------+--------------------+
.. i18n: |  model | "account.account,name" |  25     |	 Results     |   Salden           |
.. i18n: +--------+------------------------+---------+----------------+--------------------+
.. i18n: |  model |"account.account,name"  |   61    |    Liabilities |  Verbindlichkeiten |
.. i18n: +--------+------------------------+---------+----------------+--------------------+

For example, here are the first lines of a translation file (Dutch):
 
+--------+------------------------+---------+----------------+--------------------+
| type   | name                   | res_id  |      src       |   value            |
+--------+------------------------+---------+----------------+--------------------+
| field  |"account.account,code"  |  0      |    Code        |    Code 		  |
+--------+------------------------+---------+----------------+--------------------+
|  field | "account.account,name" |  0      |	 Name        |   Name             | 
+--------+------------------------+---------+----------------+--------------------+
|  model | "account.account,name" |  2      |	 Assets      |   Aktiva           |
+--------+------------------------+---------+----------------+--------------------+
|  model | "account.account,name" |  25     |	 Results     |   Salden           |
+--------+------------------------+---------+----------------+--------------------+
|  model |"account.account,name"  |   61    |    Liabilities |  Verbindlichkeiten |
+--------+------------------------+---------+----------------+--------------------+

.. i18n: 3. Import this file into Open ERP (as explained in the preceding section)
.. i18n: +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

3. Import this file into Open ERP (as explained in the preceding section)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. i18n: **Notes**

**Notes**

.. i18n:     * You should perform all these tasks on an empty database, so as to avoid over-writing data. 

    * You should perform all these tasks on an empty database, so as to avoid over-writing data. 

.. i18n: To create a new database (named 'terp_test'), use these commands:

To create a new database (named 'terp_test'), use these commands:

.. i18n:     createdb terp_test --encoding=unicode 
.. i18n:     terp_server.py --database=terp_test --init=all 

    createdb terp_test --encoding=unicode 
    terp_server.py --database=terp_test --init=all 

.. i18n: Alternatively, you could also delete your current database with these:

Alternatively, you could also delete your current database with these:

.. i18n:     dropdb terp 
.. i18n:     createdb terp --encoding=unicode 
.. i18n:     terp_server.py --init=all 

    dropdb terp 
    createdb terp --encoding=unicode 
    terp_server.py --init=all 

.. i18n: 4. Using Launchpad / Rosetta to translate modules and applications
.. i18n: +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

4. Using Launchpad / Rosetta to translate modules and applications
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. i18n: A good starting point is here https://launchpad.net/openobject

A good starting point is here https://launchpad.net/openobject

.. i18n: **Online**

**Online**

.. i18n: Select the module translation section and enter your translation.

Select the module translation section and enter your translation.

.. i18n: **Offline**

**Offline**

.. i18n: Use this, if you want to translate some 100 terms.

Use this, if you want to translate some 100 terms.

.. i18n: It seems mandatory to follow theses steps to successfully complete a translation cycle. (tested on Linux)

It seems mandatory to follow theses steps to successfully complete a translation cycle. (tested on Linux)

.. i18n:    1. Download the <po file> from Launchpad
.. i18n:    2. Get the message template file <pot file> from bzr branches
.. i18n:          1. keep in mind that the <pot file> might not always contain all strings, the <pot files> are updated irregularly.
.. i18n:          2. msgmerge <pot file> <po file> -o <new po file> 
.. i18n:    3. translate <new po file> using poedit, kbabel (KDE)
.. i18n:          1. some programs (like kbabel) allow using dictionaries to create rough translations.
.. i18n:          2. It is especially useful to create a complete dictionary from existing translations to reuse existing terms related to the application.
.. i18n:                1. In OpenERP load most/all of the modules
.. i18n:                2. Load your language
.. i18n:                3. export all modules of your language as po file and use this one as dictionary. Depending on context of the module this creates 30-80% exact translations. 
.. i18n:    4. the <new po file> must not contain <fuzzy> comments inserted by kbabel for rough translation
.. i18n:          1. grep -v fuzzy <new po file> > <po file> 
.. i18n:    5. check for correct spelling
.. i18n:          1. msgfmt <po file> -o <mo file> 
.. i18n:    6. check your translation for correct context
.. i18n:          1. import the <po file> (for modules)
.. i18n:          2. install the <mo file> and restart the application (for applications) 
.. i18n:    7. adjust the translation Online in OpenERP
.. i18n:          1. check context
.. i18n:          2. check length of strings
.. i18n:          3. export <po file> 
.. i18n:    8. upload <po file> to Launchpad
.. i18n:          1. keep in mind that Launchpad / Rosetta uses some tags (not sure which) in the header section of the exported <po file> to recognize the imported <po file> as valid.
.. i18n:          2. after some time (hours) you will receive a confirmation E-Mail (success / error) 

   1. Download the <po file> from Launchpad
   2. Get the message template file <pot file> from bzr branches
         1. keep in mind that the <pot file> might not always contain all strings, the <pot files> are updated irregularly.
         2. msgmerge <pot file> <po file> -o <new po file> 
   3. translate <new po file> using poedit, kbabel (KDE)
         1. some programs (like kbabel) allow using dictionaries to create rough translations.
         2. It is especially useful to create a complete dictionary from existing translations to reuse existing terms related to the application.
               1. In OpenERP load most/all of the modules
               2. Load your language
               3. export all modules of your language as po file and use this one as dictionary. Depending on context of the module this creates 30-80% exact translations. 
   4. the <new po file> must not contain <fuzzy> comments inserted by kbabel for rough translation
         1. grep -v fuzzy <new po file> > <po file> 
   5. check for correct spelling
         1. msgfmt <po file> -o <mo file> 
   6. check your translation for correct context
         1. import the <po file> (for modules)
         2. install the <mo file> and restart the application (for applications) 
   7. adjust the translation Online in OpenERP
         1. check context
         2. check length of strings
         3. export <po file> 
   8. upload <po file> to Launchpad
         1. keep in mind that Launchpad / Rosetta uses some tags (not sure which) in the header section of the exported <po file> to recognize the imported <po file> as valid.
         2. after some time (hours) you will receive a confirmation E-Mail (success / error) 

.. i18n: Using context Dictionary for Translations
.. i18n: -----------------------------------------

Using context Dictionary for Translations
-----------------------------------------

.. i18n: The context dictionary is explained in details in section "The Objects - Methods - The context Dictionary". If an additional language is installed using the Administration menu, the context dictionary will contain an additional key : lang. For example, if you install the French language then select it for the current user, his or her context dictionary will contain the key lang to which will be associated the value *fr_FR*. 

The context dictionary is explained in details in section "The Objects - Methods - The context Dictionary". If an additional language is installed using the Administration menu, the context dictionary will contain an additional key : lang. For example, if you install the French language then select it for the current user, his or her context dictionary will contain the key lang to which will be associated the value *fr_FR*. 

.. i18n: 	

	
