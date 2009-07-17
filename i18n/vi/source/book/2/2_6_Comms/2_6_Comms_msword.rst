
.. i18n: .. index::
.. i18n:    single: Word (Microsoft)

.. index::
   single: Word (Microsoft)

.. i18n: Microsoft Word interface
.. i18n: ========================

Microsoft Word interface
========================

.. i18n: Open ERP supplies a Microsoft Word plugin that enables you to create your own document templates.
.. i18n: What's more you can use the merge tool :menuselection:`Tools --> Merge documents` to insert data
.. i18n: from Open ERP while you generate different business documents.

Open ERP supplies a Microsoft Word plugin that enables you to create your own document templates.
What's more you can use the merge tool :menuselection:`Tools --> Merge documents` to insert data
from Open ERP while you generate different business documents.

.. i18n: So you can create templates for a number of needs, such as proposals, business letters of
.. i18n: agreement, or price requests. Each user can create his or her own document and use the plugin to
.. i18n: obtain data from Open ERP. The plugin is very helpful for easily automating business actions.

So you can create templates for a number of needs, such as proposals, business letters of
agreement, or price requests. Each user can create his or her own document and use the plugin to
obtain data from Open ERP. The plugin is very helpful for easily automating business actions.

.. i18n: Installing the Word plugin
.. i18n: --------------------------

Installing the Word plugin
--------------------------

.. i18n: The module for connecting Microsoft Word is also found in the list of Open ERP modules at
.. i18n: http://openerp.com. Once it's been downloaded install the file \ ``tiny_word_plugin-X.exe``\  .

The module for connecting Microsoft Word is also found in the list of Open ERP modules at
http://openerp.com. Once it's been downloaded install the file \ ``tiny_word_plugin-X.exe``\  .

.. i18n: When the program is installed, you must run Microsoft Word and configure the parameters that
.. i18n: enable you to access the Open ERP server from Word. Click the menu :menuselection:`Tools --> Open
.. i18n: ERP options`.

When the program is installed, you must run Microsoft Word and configure the parameters that
enable you to access the Open ERP server from Word. Click the menu :menuselection:`Tools --> Open
ERP options`.

.. i18n: .. figure::  images/word_menu.png
.. i18n:    :scale: 50
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Menu for accessing the configuration of the plugin*

.. figure::  images/word_menu.png
   :scale: 50
   :align: center

   *Menu for accessing the configuration of the plugin*

.. i18n: .. figure::  images/word_config.png
.. i18n:    :scale: 50
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Configuration of the Word plugin for accessing Open ERP*

.. figure::  images/word_config.png
   :scale: 50
   :align: center

   *Configuration of the Word plugin for accessing Open ERP*

.. i18n: Using the Word interface
.. i18n: ------------------------

Using the Word interface
------------------------

.. i18n: Start by selecting the module from which you want to make a report, for example a Sales Order. From
.. i18n: Word you can access all the fields in an Open ERP Order, and all of the fields linked to that order
.. i18n: such as from Order Lines, and from Products in those Order Lines.

Start by selecting the module from which you want to make a report, for example a Sales Order. From
Word you can access all the fields in an Open ERP Order, and all of the fields linked to that order
such as from Order Lines, and from Products in those Order Lines.

.. i18n: .. figure::  images/word_module.png
.. i18n:    :scale: 50
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Select the module that will generate the report*

.. figure::  images/word_module.png
   :scale: 50
   :align: center

   *Select the module that will generate the report*

.. i18n: Complete your document and insert Open ERP fields into the appropriate places.

Complete your document and insert Open ERP fields into the appropriate places.

.. i18n: .. figure::  images/word_fields.png
.. i18n:    :align: center
.. i18n:    :scale: 90
.. i18n: 
.. i18n:    *Add Open ERP fields into a Word document*

.. figure::  images/word_fields.png
   :align: center
   :scale: 90

   *Add Open ERP fields into a Word document*

.. i18n: .. note::  Fields in red
.. i18n: 
.. i18n: 	When you've selected some fields and added them into your Word document, some of them appear in
.. i18n: 	red.
.. i18n: 	This color indicates that you can't use that particular field because it has a complex data
.. i18n: 	relationships that can only be discovered when you start to use the field.

.. note::  Fields in red

	When you've selected some fields and added them into your Word document, some of them appear in
	red.
	This color indicates that you can't use that particular field because it has a complex data
	relationships that can only be discovered when you start to use the field.

.. i18n: Select the merge tool from by clicking :guilabel:`Perform Mail Merge` from the toolbar. This
.. i18n: connects Microsoft Word to Open ERP, at which point it searches for data to insert into the
.. i18n: document. This tool enables you to select which documents must be included in the report. Make your
.. i18n: selection and click :guilabel:`Start Merge` to run the tool that produces your different documents.

Select the merge tool from by clicking :guilabel:`Perform Mail Merge` from the toolbar. This
connects Microsoft Word to Open ERP, at which point it searches for data to insert into the
document. This tool enables you to select which documents must be included in the report. Make your
selection and click :guilabel:`Start Merge` to run the tool that produces your different documents.

.. i18n: .. figure::  images/word_select.png
.. i18n:    :scale: 50
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Selecting the Open ERP documents to use in the merge*

.. figure::  images/word_select.png
   :scale: 50
   :align: center

   *Selecting the Open ERP documents to use in the merge*

.. i18n: Word then generates the documents by inserting the Open ERP data. You get one page for each
.. i18n: selected document.

Word then generates the documents by inserting the Open ERP data. You get one page for each
selected document.

.. i18n: .. figure::  images/word_finnish.png
.. i18n:    :scale: 50
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Result of merging a Word document with data from Open ERP*

.. figure::  images/word_finnish.png
   :scale: 50
   :align: center

   *Result of merging a Word document with data from Open ERP*

.. i18n: .. index::
.. i18n:    single: Word adapter

.. index::
   single: Word adapter

.. i18n: .. note:: Testing the Word adapter
.. i18n: 
.. i18n:    If you install the Word adapter as described, explore its functionality 
.. i18n:    using the database as described in this section.

.. note:: Testing the Word adapter

   If you install the Word adapter as described, explore its functionality 
   using the database as described in this section.

.. i18n: In :ref:`ch-config` you'll see another, more powerful, module that enables you to create complete reports
.. i18n: in OpenOffice.org through an interface added directly in Open ERP. So you can create your own
.. i18n: templates, such as fax and invoice templates.

In :ref:`ch-config` you'll see another, more powerful, module that enables you to create complete reports
in OpenOffice.org through an interface added directly in Open ERP. So you can create your own
templates, such as fax and invoice templates.

.. i18n: These reports can then be exported in PDF by leaving Open ERP, or can be edited before sending to a
.. i18n: customer. So you can also personalize the details of your faxes and invoices as needed, even though
.. i18n: they are based on your templates.

These reports can then be exported in PDF by leaving Open ERP, or can be edited before sending to a
customer. So you can also personalize the details of your faxes and invoices as needed, even though
they are based on your templates.

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
