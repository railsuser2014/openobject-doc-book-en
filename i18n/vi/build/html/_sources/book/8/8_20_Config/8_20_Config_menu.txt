
.. i18n: .. index:: 
.. i18n:    single: menu; configuring

.. index:: 
   single: menu; configuring

.. i18n: Configuring the menu
.. i18n: ====================

Configuring the menu
====================

.. i18n: Open ERP's menu organization isn't subject to any restriction, so you can modify the whole
.. i18n: structure, the terminology and all access rights to it to meet your specific needs in the best
.. i18n: possible way. However, before you do all that and just as you would for any other customizable
.. i18n: software, you should balance both the benefits you see in such changes and the costs, such as the
.. i18n: need to train users, to maintain new documentation and to continue the alterations through
.. i18n: subsequent versions of the software.

Open ERP's menu organization isn't subject to any restriction, so you can modify the whole
structure, the terminology and all access rights to it to meet your specific needs in the best
possible way. However, before you do all that and just as you would for any other customizable
software, you should balance both the benefits you see in such changes and the costs, such as the
need to train users, to maintain new documentation and to continue the alterations through
subsequent versions of the software.

.. i18n: This section describes how to proceed to change the structure of the menu and the welcome page, to
.. i18n: configure the terminology of the menus and forms in the user interface and for managing users'
.. i18n: access rights to the menus and the various underlying business objects.

This section describes how to proceed to change the structure of the menu and the welcome page, to
configure the terminology of the menus and forms in the user interface and for managing users'
access rights to the menus and the various underlying business objects.

.. i18n: .. index::
.. i18n:    single: menu; duplicating

.. index::
   single: menu; duplicating

.. i18n: Changing the menu
.. i18n: -----------------

Changing the menu
-----------------

.. i18n: As administrator, and using the web client, select a menu item (but don't click it).
.. i18n: Click on the line containing
.. i18n: :menuselection:`Administration --> Translations --> Import/Export --> Export a Translation File`
.. i18n: (but not on the string \ ``Export a Translation File``\   itself) and click the 
.. i18n: :guilabel:`Switch` button to bring up the menu item as an
.. i18n: editable form (you can do the same using the GTK client – there you select the line and click the
.. i18n: :guilabel:`View` button instead).

As administrator, and using the web client, select a menu item (but don't click it).
Click on the line containing
:menuselection:`Administration --> Translations --> Import/Export --> Export a Translation File`
(but not on the string \ ``Export a Translation File``\   itself) and click the 
:guilabel:`Switch` button to bring up the menu item as an
editable form (you can do the same using the GTK client – there you select the line and click the
:guilabel:`View` button instead).

.. i18n: You could now edit this form (**but don't do that, read the next paragraph first!**) – change 
.. i18n: its :guilabel:`Parent Menu`, which moves the entry to a
.. i18n: different part of the menu system; edit its :guilabel:`Menu` name to change how it appears in the
.. i18n: menu tree, or give it a new :guilabel:`Icon`. Or you could give it a new :guilabel:`Action` entirely
.. i18n: (but this would lose the point of this particular exercise).

You could now edit this form (**but don't do that, read the next paragraph first!**) – change 
its :guilabel:`Parent Menu`, which moves the entry to a
different part of the menu system; edit its :guilabel:`Menu` name to change how it appears in the
menu tree, or give it a new :guilabel:`Icon`. Or you could give it a new :guilabel:`Action` entirely
(but this would lose the point of this particular exercise).

.. i18n: Instead of editing this form, which is the original menu entry, duplicate it. With the web
.. i18n: client you must first make the form read-only by clicking the :guilabel:`Cancel` button, then you
.. i18n: click the :guilabel:`Duplicate` button that appears (in the GTK client, click :menuselection:`Form
.. i18n: --> Duplicate`  from the top menu). The form that remains is now the duplicate entry, not the
.. i18n: original.

Instead of editing this form, which is the original menu entry, duplicate it. With the web
client you must first make the form read-only by clicking the :guilabel:`Cancel` button, then you
click the :guilabel:`Duplicate` button that appears (in the GTK client, click :menuselection:`Form
--> Duplicate`  from the top menu). The form that remains is now the duplicate entry, not the
original.

.. i18n: To move this duplicate entry, change the :guilabel:`Parent Menu` field by deleting what's there and
.. i18n: replacing it with another menu that everyone can see, such as :guilabel:`Tools` or :guilabel:`Human
.. i18n: Resources`, and make sure that the entry moves to the end of the menu list by replacing the
.. i18n: :guilabel:`Sequence` with \ ``99``\  . You can experiment with icons if you like. Save the form and
.. i18n: then click :guilabel:`Main Menu` to see the results.

To move this duplicate entry, change the :guilabel:`Parent Menu` field by deleting what's there and
replacing it with another menu that everyone can see, such as :guilabel:`Tools` or :guilabel:`Human
Resources`, and make sure that the entry moves to the end of the menu list by replacing the
:guilabel:`Sequence` with \ ``99``\  . You can experiment with icons if you like. Save the form and
then click :guilabel:`Main Menu` to see the results.

.. i18n: .. tip:: Duplicating the menu
.. i18n: 
.. i18n:    If you're planning to modify a menu you should duplicate it first.
.. i18n:    In this way you'll always keep a link to the original menu that works if you need it to.

.. tip:: Duplicating the menu

   If you're planning to modify a menu you should duplicate it first.
   In this way you'll always keep a link to the original menu that works if you need it to.

.. i18n: .. index:: 
.. i18n:    single: welcome page
.. i18n:    
.. i18n: Personalizing the welcome page for each user
.. i18n: --------------------------------------------

.. index:: 
   single: welcome page
   
Personalizing the welcome page for each user
--------------------------------------------

.. i18n: When you sign into Open ERP for the first time, a welcome page appears. In a minimal system, such
.. i18n: as that created in the original \ ``openerp_ch02``\  database before it was expanded in 
.. i18n: :ref:`ch-guided`, and in the  \ ``openerp_ch03``\  database, you only get the main menu – the same as you
.. i18n: get by default when you click the :menuselection:`Main Menu` button. As you add functionality to
.. i18n: your database you get more choices for the welcome page, with different dashboards automatically
.. i18n: assigned to various company roles as they're created in the demonstration data.

When you sign into Open ERP for the first time, a welcome page appears. In a minimal system, such
as that created in the original \ ``openerp_ch02``\  database before it was expanded in 
:ref:`ch-guided`, and in the  \ ``openerp_ch03``\  database, you only get the main menu – the same as you
get by default when you click the :menuselection:`Main Menu` button. As you add functionality to
your database you get more choices for the welcome page, with different dashboards automatically
assigned to various company roles as they're created in the demonstration data.

.. i18n: The administrator can change both the welcome page and the main menu page individually for each user
.. i18n: of the system, and can adapt Open ERP to each role in the company to best fit the needs of everyone.

The administrator can change both the welcome page and the main menu page individually for each user
of the system, and can adapt Open ERP to each role in the company to best fit the needs of everyone.

.. i18n: To make modifications for a particular user, edit the user configuration again in
.. i18n: :menuselection:`Administration --> Users --> Users`. Open the form for a particular user, and select
.. i18n: different menu entries for the two fields :guilabel:`Home Action` and :guilabel:`Menu Action`.

To make modifications for a particular user, edit the user configuration again in
:menuselection:`Administration --> Users --> Users`. Open the form for a particular user, and select
different menu entries for the two fields :guilabel:`Home Action` and :guilabel:`Menu Action`.

.. i18n: .. figure::  images/new_home.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Selecting a new welcome page*

.. figure::  images/new_home.png
   :scale: 75
   :align: center

   *Selecting a new welcome page*

.. i18n: The :guilabel:`Home Action` is the menu item that is automatically opened when you first sign on,
.. i18n: and is also reached when you click the :guilabel:`Home` link in the top right toolbar of the web
.. i18n: client. There you can choose any page that you'd reach through any menu – one of the dashboards
.. i18n: could be most useful. The :guilabel:`Menu Action` is the one you reach through the :guilabel:`Main
.. i18n: Menu` button in the web client (the :guilabel:`Menu` button in the GTK client). You can choose the
.. i18n: main menu and the dashboards there.

The :guilabel:`Home Action` is the menu item that is automatically opened when you first sign on,
and is also reached when you click the :guilabel:`Home` link in the top right toolbar of the web
client. There you can choose any page that you'd reach through any menu – one of the dashboards
could be most useful. The :guilabel:`Menu Action` is the one you reach through the :guilabel:`Main
Menu` button in the web client (the :guilabel:`Menu` button in the GTK client). You can choose the
main menu and the dashboards there.

.. i18n: .. tip:: Actions on the administrator's menu
.. i18n: 
.. i18n: 	It's very easy to change the welcome page and the menu of the different users.
.. i18n: 	However, you shouldn't change the main administrator's menu because you could make certain menus
.. i18n: 	completely inaccessible by mistake.

.. tip:: Actions on the administrator's menu

	It's very easy to change the welcome page and the menu of the different users.
	However, you shouldn't change the main administrator's menu because you could make certain menus
	completely inaccessible by mistake.

.. i18n: .. index:: 
.. i18n:    single: field; default value
.. i18n:    
.. i18n: Assigning default values to fields
.. i18n: ----------------------------------

.. index:: 
   single: field; default value
   
Assigning default values to fields
----------------------------------

.. i18n: You can quite easily configure the system to put default values in various fields as you open new
.. i18n: forms. This enables you to pre-complete the fields with default data to simplify your users' work in
.. i18n: entering new documents.

You can quite easily configure the system to put default values in various fields as you open new
forms. This enables you to pre-complete the fields with default data to simplify your users' work in
entering new documents.

.. i18n: * If you're using the web client hold :kbd:`Ctrl` down and Right-Click at the same time (that's a mouse right-click while the mouse
.. i18n:   pointer is in the field and the Control key is held down on the keyboard).
.. i18n: 
.. i18n: * If you're using the GTK client, you just need to right-click the mouse while the pointer is in the
.. i18n:   field.
.. i18n:   
.. i18n: An administrator has the choice of making the default work just for that user, or for all users of the database.

* If you're using the web client hold :kbd:`Ctrl` down and Right-Click at the same time (that's a mouse right-click while the mouse
  pointer is in the field and the Control key is held down on the keyboard).

* If you're using the GTK client, you just need to right-click the mouse while the pointer is in the
  field.
  
An administrator has the choice of making the default work just for that user, or for all users of the database.

.. i18n: .. figure::  images/set_default.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Inserting a new default value*

.. figure::  images/set_default.png
   :scale: 75
   :align: center

   *Inserting a new default value*

.. i18n: To check this new configuration, open a new partner form: the field :guilabel:`Country` should now
.. i18n: contain the entry \ ``New Zealand``\  .

To check this new configuration, open a new partner form: the field :guilabel:`Country` should now
contain the entry \ ``New Zealand``\  .

.. i18n: This is a very powerful feature! An administrator can use this functionality to redefine the
.. i18n: behavior of your whole system. You can test that in database \ ``openerp_ch13``\   by opening up a
.. i18n: new :guilabel:`Purchase Order` form, clicking the second tab :guilabel:`Purchase Shippings`,
.. i18n: selecting \ ``From Picking``\   in the :guilabel:`Invoicing Control` field and then making that the
.. i18n: default.

This is a very powerful feature! An administrator can use this functionality to redefine the
behavior of your whole system. You can test that in database \ ``openerp_ch13``\   by opening up a
new :guilabel:`Purchase Order` form, clicking the second tab :guilabel:`Purchase Shippings`,
selecting \ ``From Picking``\   in the :guilabel:`Invoicing Control` field and then making that the
default.

.. i18n: From that moment on, you'd automatically create draft purchase invoices only when goods are
.. i18n: received, so you could very easily restrict your accountants from paying any invoices that turn up
.. i18n: until you were sure you had received the goods. It wouldn't stop anyone from selecting another
.. i18n: method of invoice control, but they'd start with the default definition.

From that moment on, you'd automatically create draft purchase invoices only when goods are
received, so you could very easily restrict your accountants from paying any invoices that turn up
until you were sure you had received the goods. It wouldn't stop anyone from selecting another
method of invoice control, but they'd start with the default definition.

.. i18n: Changing the terminology
.. i18n: ------------------------

Changing the terminology
------------------------

.. i18n: You can use Open ERP's language translation functionality to substitute its standard terminology
.. i18n: with terminology that fits your company better. It's quite straightforward to adapt the software
.. i18n: with different terms specific to your industry. Moreover, this can strengthen acceptance of your new
.. i18n: Open ERP system, because everybody will be able to retain their usual vocabulary.

You can use Open ERP's language translation functionality to substitute its standard terminology
with terminology that fits your company better. It's quite straightforward to adapt the software
with different terms specific to your industry. Moreover, this can strengthen acceptance of your new
Open ERP system, because everybody will be able to retain their usual vocabulary.

.. i18n: You can do this one of two ways:

You can do this one of two ways:

.. i18n: * translate them in a CSV file, which gives you a global overview of all of the system terms so that
.. i18n:   you can search and replace specific occurrences everywhere,
.. i18n: 
.. i18n: * translate the phrases directly in the client, which means that you can change them in their
.. i18n:   context, and that can be helpful to you while you're translating.

* translate them in a CSV file, which gives you a global overview of all of the system terms so that
  you can search and replace specific occurrences everywhere,

* translate the phrases directly in the client, which means that you can change them in their
  context, and that can be helpful to you while you're translating.

.. i18n: The same approach is used to translate terms that haven't been created yet. This can be useful, for
.. i18n: example, with modules that haven't yet been translated into English or any other language that you
.. i18n: want.

The same approach is used to translate terms that haven't been created yet. This can be useful, for
example, with modules that haven't yet been translated into English or any other language that you
want.

.. i18n: .. index::
.. i18n:    single: translation

.. index::
   single: translation

.. i18n: Translation through a CSV file
.. i18n: ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Translation through a CSV file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. i18n: To translate or modify all of the system's phrases you first have to export a translation file in
.. i18n: CSV form. And to do that, you have to install a language into Open ERP. To load a translation
.. i18n: that already exists in Open ERP use
.. i18n: :menuselection:`Administration --> Translations --> Load an Official Translation`
.. i18n: choose a language and then click :guilabel:`Start Installation`.

To translate or modify all of the system's phrases you first have to export a translation file in
CSV form. And to do that, you have to install a language into Open ERP. To load a translation
that already exists in Open ERP use
:menuselection:`Administration --> Translations --> Load an Official Translation`
choose a language and then click :guilabel:`Start Installation`.

.. i18n: Then export it using 
.. i18n: :menuselection:`Administration --> Translations --> Import/Export --> Export a Translation file. 
.. i18n: Select the language, then the :guilabel:`CSV File` format, then one or more (or all) modules.
.. i18n: Click :guilabel:`Get File` to start the download process, then click the small 
.. i18n: :guilabel:`Save` icon to save the file somewhere. A French translation would be
.. i18n: named :file:`fr_FR.csv` by default, but you can name it whatever you like. 

Then export it using 
:menuselection:`Administration --> Translations --> Import/Export --> Export a Translation file. 
Select the language, then the :guilabel:`CSV File` format, then one or more (or all) modules.
Click :guilabel:`Get File` to start the download process, then click the small 
:guilabel:`Save` icon to save the file somewhere. A French translation would be
named :file:`fr_FR.csv` by default, but you can name it whatever you like. 

.. i18n: .. note:: UTF-8 format
.. i18n: 
.. i18n: 	The CSV file is encoded in the UTF-8 format.
.. i18n: 	Make sure that you retain this format when you open the file in a spreadsheet program because
.. i18n: 	if you **don't** retain it you risk seeing strange character strings in place of accented
.. i18n: 	characters.

.. note:: UTF-8 format

	The CSV file is encoded in the UTF-8 format.
	Make sure that you retain this format when you open the file in a spreadsheet program because
	if you **don't** retain it you risk seeing strange character strings in place of accented
	characters.

.. i18n: .. figure::  images/csv_transl.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *CSV translation file with a translation in view*

.. figure::  images/csv_transl.png
   :scale: 75
   :align: center

   *CSV translation file with a translation in view*

.. i18n: The file contains six columns: :guilabel:`module` , 
.. i18n: :guilabel:`type` , :guilabel:`name`, :guilabel:`res_id`,
.. i18n: :guilabel:`src`, and :guilabel:`value`. You have to ensure that the first line, which specifies
.. i18n: these column names, remains untouched. 

The file contains six columns: :guilabel:`module` , 
:guilabel:`type` , :guilabel:`name`, :guilabel:`res_id`,
:guilabel:`src`, and :guilabel:`value`. You have to ensure that the first line, which specifies
these column names, remains untouched. 

.. i18n: The :guilabel:`src`  field contains the base text in English,
.. i18n: and the :guilabel:`value` field contains a translation into another conventional language or into a
.. i18n: specialist technical phrase. If there's nothing at all in the :guilabel:`value` field then the
.. i18n: English translation will automatically be used on the the form you see.

The :guilabel:`src`  field contains the base text in English,
and the :guilabel:`value` field contains a translation into another conventional language or into a
specialist technical phrase. If there's nothing at all in the :guilabel:`value` field then the
English translation will automatically be used on the the form you see.

.. i18n: .. tip:: Where should you modify the text?
.. i18n: 
.. i18n:    Most of the time, you will find the text that you want to modify in several lines of the CSV
.. i18n:    file.
.. i18n:    Which line should you modify?
.. i18n:    Refer to the two columns :guilabel:`type` (in column B) and :guilabel:`name` (in column C).
.. i18n:    Some lines have the name :guilabel:`ir.ui.menu` in the :guilabel:`name` column which shows that this is a menu entry.
.. i18n:    Others have :guilabel:`selection` in the :guilabel:`type` column, which indicates that you'd see this entry in a drop-down
.. i18n:    menu.

.. tip:: Where should you modify the text?

   Most of the time, you will find the text that you want to modify in several lines of the CSV
   file.
   Which line should you modify?
   Refer to the two columns :guilabel:`type` (in column B) and :guilabel:`name` (in column C).
   Some lines have the name :guilabel:`ir.ui.menu` in the :guilabel:`name` column which shows that this is a menu entry.
   Others have :guilabel:`selection` in the :guilabel:`type` column, which indicates that you'd see this entry in a drop-down
   menu.

.. i18n: You should then load the new file into your Open ERP system using the menu
.. i18n: :menuselection:`Administration --> Translations --> Import/Export --> Import a Translation file`. 
.. i18n: You've then got two ways forward:

You should then load the new file into your Open ERP system using the menu
:menuselection:`Administration --> Translations --> Import/Export --> Import a Translation file`. 
You've then got two ways forward:

.. i18n: * you can overwrite the previous translation by using the same name as before (so you could have a
.. i18n:   special 'standard French' translation by reusing the :guilabel:`Name` \ ``Français``\   and
.. i18n:   :guilabel:`Code` \ ``fr_FR``\  ),
.. i18n: 
.. i18n: * you could create a new translation file which users can select in their :guilabel:`Preferences`.

* you can overwrite the previous translation by using the same name as before (so you could have a
  special 'standard French' translation by reusing the :guilabel:`Name` \ ``Français``\   and
  :guilabel:`Code` \ ``fr_FR``\  ),

* you could create a new translation file which users can select in their :guilabel:`Preferences`.

.. i18n: If you're not connected to the translated language, click :guilabel:`Preferences`, select the
.. i18n: language in :guilabel:`Language` and finally click :guilabel:`OK` to load the new language with its
.. i18n: new terminology.

If you're not connected to the translated language, click :guilabel:`Preferences`, select the
language in :guilabel:`Language` and finally click :guilabel:`OK` to load the new language with its
new terminology.

.. i18n: .. tip:: Partial translations
.. i18n: 
.. i18n:    You can load a selection of the lines in a translation file by deleting most of the lines in the
.. i18n:    file and then loading back only the changed ones. Open ERP then changes only the uploaded lines
.. i18n:    and leaves the original ones alone.

.. tip:: Partial translations

   You can load a selection of the lines in a translation file by deleting most of the lines in the
   file and then loading back only the changed ones. Open ERP then changes only the uploaded lines
   and leaves the original ones alone.

.. i18n: Changes through the client interface
.. i18n: ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Changes through the client interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. i18n: You can also change labels and other screen items on screen in the web client. 
.. i18n: To do that, open the form that you want to translate, then click the 
.. i18n: :guilabel:`Translate this resource.` icon to its top right. 
.. i18n: You then have the choice of translating:

You can also change labels and other screen items on screen in the web client. 
To do that, open the form that you want to translate, then click the 
:guilabel:`Translate this resource.` icon to its top right. 
You then have the choice of translating:

.. i18n: * the data in the system (contained in the :guilabel:`Fields`),
.. i18n: 
.. i18n: * the field titles (the :guilabel:`Labels`),
.. i18n: 
.. i18n: * all of the :guilabel:`Action` buttons to the right of the form (the :guilabel:`Relates` option),
.. i18n: 
.. i18n: * the terms used in the form :guilabel:`View`.

* the data in the system (contained in the :guilabel:`Fields`),

* the field titles (the :guilabel:`Labels`),

* all of the :guilabel:`Action` buttons to the right of the form (the :guilabel:`Relates` option),

* the terms used in the form :guilabel:`View`.

.. i18n: You can modify any of these.

You can modify any of these.

.. i18n: The procedure is slightly different using the GTK client. In this you just right-click on a label or button
.. i18n: with the mouse. You can choose to translate the item itself or the whole view.

The procedure is slightly different using the GTK client. In this you just right-click on a label or button
with the mouse. You can choose to translate the item itself or the whole view.

.. i18n: This method is simple and quick when you only have a few entries to modify, but it can become
.. i18n: tiresome and you can lose a lot of time if you've got to change some terms across the whole system.

This method is simple and quick when you only have a few entries to modify, but it can become
tiresome and you can lose a lot of time if you've got to change some terms across the whole system.

.. i18n: In that case it would be better to use the translation method that employs a CSV file.

In that case it would be better to use the translation method that employs a CSV file.

.. i18n: .. tip:: Tacking account of translations
.. i18n: 
.. i18n:    In the GTK client the modified terms aren't updated immediately.
.. i18n:    To see the effects of the modifications you must close the current window and then reopen the
.. i18n:    form.

.. tip:: Tacking account of translations

   In the GTK client the modified terms aren't updated immediately.
   To see the effects of the modifications you must close the current window and then reopen the
   form.

.. i18n: .. Copyright © Open Object Press. All rights reserved.

.. Copyright © Open Object Press. All rights reserved.

.. i18n: .. You may take electronic copy of this publication and distribute it if you don't
.. i18n: .. change the content. You can also print a copy to be read by yourself only.

.. You may take electronic copy of this publication and distribute it if you don't
.. change the content. You can also print a copy to be read by yourself only.

.. i18n: .. We have contracts with different publishers in different countries to sell and
.. i18n: .. distribute paper or electronic based versions of this book (translated or not)
.. i18n: .. in bookstores. This helps to distribute and promote the Open ERP product. It
.. i18n: .. also helps us to create incentives to pay contributors and authors using author
.. i18n: .. rights of these sales.

.. We have contracts with different publishers in different countries to sell and
.. distribute paper or electronic based versions of this book (translated or not)
.. in bookstores. This helps to distribute and promote the Open ERP product. It
.. also helps us to create incentives to pay contributors and authors using author
.. rights of these sales.

.. i18n: .. Due to this, grants to translate, modify or sell this book are strictly
.. i18n: .. forbidden, unless Tiny SPRL (representing Open Object Press) gives you a
.. i18n: .. written authorisation for this.

.. Due to this, grants to translate, modify or sell this book are strictly
.. forbidden, unless Tiny SPRL (representing Open Object Press) gives you a
.. written authorisation for this.

.. i18n: .. Many of the designations used by manufacturers and suppliers to distinguish their
.. i18n: .. products are claimed as trademarks. Where those designations appear in this book,
.. i18n: .. and Open Object Press was aware of a trademark claim, the designations have been
.. i18n: .. printed in initial capitals.

.. Many of the designations used by manufacturers and suppliers to distinguish their
.. products are claimed as trademarks. Where those designations appear in this book,
.. and Open Object Press was aware of a trademark claim, the designations have been
.. printed in initial capitals.

.. i18n: .. While every precaution has been taken in the preparation of this book, the publisher
.. i18n: .. and the authors assume no responsibility for errors or omissions, or for damages
.. i18n: .. resulting from the use of the information contained herein.

.. While every precaution has been taken in the preparation of this book, the publisher
.. and the authors assume no responsibility for errors or omissions, or for damages
.. resulting from the use of the information contained herein.

.. i18n: .. Published by Open Object Press, Grand Rosière, Belgium

.. Published by Open Object Press, Grand Rosière, Belgium
