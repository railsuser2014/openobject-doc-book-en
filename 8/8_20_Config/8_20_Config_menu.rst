
.. index:: 
   single: menu; configuring

Configuring the Menu
====================

OpenERP's menu organization is not subject to any restriction, so you can modify the whole
structure, the terminology and all access rights to it to meet your specific needs in the best
possible way. However, before you do all that and just as you would for any other customizable
software, you should balance both the benefits you see in such changes and the costs, such as the
need to train users, to maintain new documentation and to continue the alterations through
subsequent versions of the software.

This section describes how to proceed to change the structure of the menu and the welcome page, to
configure the terminology of the menus and forms in the user interface, and for managing users'
access rights to the menus and the various underlying business objects.

.. index::
   single: menu; duplicating

Changing the Menu
-----------------

You can change the way menu items appear and the actions they trigger by using the menu
:menuselection:`Settings --> Technical --> User Interface --> Menu Items`. This
opens a search view where you may locate the menu item to be edited by entering its entire
name (specified as menu hierarchy) in the :guilabel:`Menu` field or specifying its immediate
parent menu name in :guilabel:`Parent Menu`.

As an example, locate the menu item \ ``Settings/Translations/Import / Export/Export Translation`` \
and click on this entry to open its corresponding form.
You could now edit this form (**but do not do that, read the next paragraph first!**) – change 
its :guilabel:`Parent Menu`, which moves the entry to a
different part of the menu system; edit its :guilabel:`Menu` name to change how it appears in the
menu tree, or give it a new :guilabel:`Icon`. Or you could give it a new :guilabel:`Action` entirely
(but this would lose the point of this particular exercise).

Instead of editing this form, which is the original menu entry, duplicate it. With the help of :guilabel:`Duplicate` button that appears in More button. The form should be non editable for finding the More button.

To move this duplicate entry, change the :guilabel:`Parent Menu` field by deleting what is there and
replacing it with another menu that everyone can see, such as :guilabel:`Tools` or :guilabel:`Human
Resources`, and make sure that the entry moves to the end of the menu list by replacing the
:guilabel:`Sequence` with \ ``99``\  . You can experiment with icons if you like. Save the form and
then reload the page to see the results.

.. tip:: Duplicating the Menu

   If you are planning to modify a menu, you should duplicate it first.
   In this way you will always keep a link to the original menu that works if you need it to.

.. index:: 
   single: welcome page
   

.. index:: 
   single: field; default value
   
Assigning Default Values to Fields
----------------------------------

You can quite easily configure the system to put default values in various fields as you open new
forms. This enables you to pre-complete the fields with default data to simplify your users' work in
entering new documents. Let us use the Customer form to demonstrate this feature. Create a new customer
with :guilabel:`Country` set as :guilabel:`New Zealand`

* First you have to active the developer mode, In that select \ ``Set Defaults`` \.
An administrator has the choice of making the default work just for that user, or for all users of the database.

.. figure::  images/set_default.png
   :scale: 55
   :align: center

   *Inserting a new default value*

To check this new configuration, open a new partner form: the field :guilabel:`Country` should now
contain the entry \ ``New Zealand``\  .

This is a very powerful feature! An administrator can use this functionality to redefine the
behavior of your whole system.

Changing the Terminology
------------------------

You can use OpenERP's language translation functionality to substitute its standard terminology
with terminology that fits your company better. It is quite straightforward to adapt the software
with different terms specific to your industry. Moreover, this can strengthen acceptance of your new
OpenERP system, because everybody will be able to retain their usual vocabulary.

You can do this one of two ways:

* translate them in a CSV file, which gives you a global overview of all of the system terms so that
  you can search and replace specific occurrences everywhere,

* translate the phrases directly in the client, which means that you can change them in their
  context, and that can be helpful to you while you are translating.

The same approach is used to translate terms that have not been created yet. This can be useful, for
example, with modules that have not yet been translated into English or any other language that you
want.

.. index::
   single: translation

Translation through a CSV File
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To translate or modify all of the system's phrases, you first have to export a translation file in
CSV form. And to do that, you have to install a language into OpenERP. To load a translation
that already exists in OpenERP, use
:menuselection:`Settings --> Translations --> Load an Official Translation`,
choose a language and then click :guilabel:`Load`.

Then export it using 
:menuselection:`Settings --> Translations --> Import/Export --> Export Translation`. 
Select the language, then the :guilabel:`CSV File` format, then one or more (or all) modules.
Click :guilabel:`Export` to start the export process, then click the small 
:guilabel:`Save As` icon to save the file somewhere.

.. note:: UTF-8 Format

	The CSV file is encoded in the UTF-8 format.
	Make sure that you retain this format when you open the file in a spreadsheet program, because
	if you **do not** retain it, you risk seeing strange character strings in place of accented
	characters.

.. figure::  images/csv_transl.png
   :scale: 75
   :align: center

   *CSV translation file with a translation in view*

The file contains six columns: :guilabel:`module` , 
:guilabel:`type` , :guilabel:`name`, :guilabel:`res_id`,
:guilabel:`src`, and :guilabel:`value`. You have to ensure that the first line, which specifies
these column names, remains untouched. 

The :guilabel:`src` field contains the base text in English,
and the :guilabel:`value` field contains a translation into another conventional language or into a
specialist technical phrase. If there is nothing at all in the :guilabel:`value` field then the
English translation will automatically be used on the form you see.

.. tip:: Where Should you Modify the Text?

   Most of the time, you will find the text that you want to modify in several lines of the CSV
   file.
   Which line should you modify?
   Refer to the two columns :guilabel:`type` (in column B) and :guilabel:`name` (in column C).
   Some lines have the name :guilabel:`ir.ui.menu` in the :guilabel:`name` column, which shows that this is a menu entry.
   Others have :guilabel:`selection` in the :guilabel:`type` column, which indicates that you would
   see this entry in a drop-down menu.

You should then load the new file into your OpenERP system using the menu
:menuselection:`Settings --> Translations --> Import/Export --> Import Translation`. 
You have then got two ways forward:

* You can overwrite the previous translation by using the same name as before (so you could have a
  special 'standard French' translation by reusing the :guilabel:`Name` \ ``Français``\   and
  :guilabel:`Code` \ ``fr_FR``\  ),

* You could create a new translation file which users can select in their :guilabel:`Preferences`.

If you are not connected to the translated language, click :guilabel:`Preferences`, select the
language in :guilabel:`Language` from the :guilabel:`Preferences` tab, and finally click :guilabel:`Save`
to load the new language with its new terminology.

.. tip:: Partial Translations

   You can load a selection of the lines in a translation file by deleting most of the lines in the
   file and then loading back only the changed ones. OpenERP then changes only the uploaded lines
   and leaves the original ones alone.


.. Copyright © Open Object Press. All rights reserved.

.. You may take electronic copy of this publication and distribute it if you don't
.. change the content. You can also print a copy to be read by yourself only.

.. We have contracts with different publishers in different countries to sell and
.. distribute paper or electronic based versions of this book (translated or not)
.. in bookstores. This helps to distribute and promote the OpenERP product. It
.. also helps us to create incentives to pay contributors and authors using author
.. rights of these sales.

.. Due to this, grants to translate, modify or sell this book are strictly
.. forbidden, unless Tiny SPRL (representing Open Object Press) gives you a
.. written authorisation for this.

.. Many of the designations used by manufacturers and suppliers to distinguish their
.. products are claimed as trademarks. Where those designations appear in this book,
.. and Open Object Press was aware of a trademark claim, the designations have been
.. printed in initial capitals.

.. While every precaution has been taken in the preparation of this book, the publisher
.. and the authors assume no responsibility for errors or omissions, or for damages
.. resulting from the use of the information contained herein.

.. Published by Open Object Press, Grand Rosière, Belgium

