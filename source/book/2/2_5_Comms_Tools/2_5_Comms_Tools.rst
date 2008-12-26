

Communication Tools
#####################

Summary

* Thunderbird interface

* Microsoft Outlook interface

* Microsoft Word interface

Keywords

* SRM, CRM

* productivity

* communication

* email

* Office

 *Open ERP provides all the information you need to pursue your company's business opportunities efficiently. But to stay productive with all the information you have to handle it's essential that you can keep using your normal communication tools by interfacing them with Open ERP, and not be restricted just to Open ERP's interface.* 



Open ERP can do most things you need to pursue your business opportunities effectively. But there can be quite a quite a bit to learn, which reduces your efficiency while you're learning. And if that's true for a heavy user of the system, it's doubly true for an occasional user or someone who already makes heavy use of standard Office applications and can't easily change.

So for those who need to continue using their traditional Office applications to maintain their efficiency, Open ERP can be fitted out with interface adapters to some of the most common. Your users can participate in many Open ERP-maintained processes without ever leaving their familiar Office-based environment, and can avoid double data-entry yet link into Open ERP's database automatically.

The three following modules are described:

* Mozilla Thunderbird interface,

* Microsoft Outlook interface,

* Microsoft Word interface.

These three modules were developed by the Axelor company (, located in Paris) and are available through the official Open ERP site in the modules section.

The chapter is a mix of installation and configuration instructions, and basic interaction exercises.

Open ERP preparation
=====================

You'll need only one database for this chapter:

* \ ``openerp_ch05X``\  , which should be a restored copy of\ `` openerp_ch04X``\   the database you created at the start of Chapter 4 and then extended – you'll refer to it from time to time because it contains demonstration data that you can use to exercise some of the functions you encounter in the chapter,

To be able to backup and restore the database you'll need to know your super-administrator password.

You'll probably also need your system's \ ``addons``\   directory to be writable, since some of the modules you'll need may have to be added separately – they weren't available as part of core the 4.2.2 release of Open ERP.

You will need to have administrator access to your Windows PC to install the Outlook and Word interface adapters described in the chapter.

Mozilla Thunderbird interface
===============================

The Mozilla Thunderbird plugin enables you to carry out a series of Open ERP operations directly from the Thunderbird email client:

* create a contact or partner from an email,

* save an email and its attachments in Open ERP,

* send any file attached to an Open ERP document (such as proposals, projects, and tasks).

Installing the Thunderbird extension
-------------------------------------

To be able to use the Thunderbird plugin you first have to install the Open ERP module \ ``email_interface``\  . It's not loaded in the core of Open ERP Server 4.2.2 (so you'll have to load it using one of the methods described at the end of Chapter 1) but may be in a future version. Once you've got it into your server's filesystem it's installed the same way as all of the other modules you've handled so far.

You'll then have to install the Thunderbird extension. To do that, use the file \ ``tiny_plugin_2.0.xpi``\   which is found in the plugins directory of the \ ``email_interface``\   module. Then take the following steps:

	#. From Thunderbird, open the menu  *Tools > Complementary Modules* 

	#. Click the  *Install* button.

	#. Select the file \ ``tiny_plugin-2.0.xpi``\  

	#. Click  *Install Now* then restart Thunderbird.

Once the extension has been installed, you have only to create a shortcut in your Thunderbird toolbar for the function  *Archive to Tiny* . Do it like this:

	#. Click the right mouse button on the toolbar and select  *Personalize* 

	#. Place the icon  *Archive to Tiny* in your toolbar in the place of your choice.

.. tip::   **Attention**  *Thunderbird version* 

	The Tiny plugin for Thunderbird only works with Thunderbird version 2.0 and above.

	So check your Thunderbird version before installing, and download the latest version that you need from the following address: http://www.mozilla.org/products/thunderbird/

Thunderbird user interface
---------------------------

When you've installed the module the first thing to do is connect it to Open ERP from Thunderbird. To do this use the menu  *Tools > Tiny Plugin* .

A configuration window appears enabling you to enter configuration data about your Open ERP server.


	.. image::  images/thunderbird_config.png
	   :align: center

*Configuration for accessing Open ERP from Thunderbird*


To archive an email in Open ERP from Thunderbird select the email and click on the icon  *Archive in Tiny* . Alternatively you could right-click the mouse: either opens a search dialog box.

This allows you to select an object that you'd like to add to your email and its attachments. You can select a partner, a task, a project, an analytical account, or any other object.


	.. image::  images/thunderbird_selection.png
	   :align: center

*Selecting Open ERP objects from Thunderbird*


.. tip::   **A step further**  *Document Management* 

	The Thunderbird plugin is compatible with Open ERP's document management. So if you install the module document you could:

	* search through the content of your company's documents (those that have the type .doc, .pdf, .sxw and .odt) and also in archived emails,

	* have a shared filesystem that's connected to various Open ERP documents to share information and access it with your favorite browser,

	* organize and structure your documents (such as projects, partners and users) in Open ERP's system.

If you can't find a partner or contact to correspond with your email in Open ERP it's possible to create one on the fly simply by using the information contained in the email and clicking the  *Create*  button.


	.. image::  images/thunderbird_creation.png
	   :align: center

*Creating a contact on the fly from Thunderbird*


To access archived data from different documents in Open ERP you can use the  *Email Thunderbird*  interface that appears over Open ERP documents.

.. tip::   **Note**  *Testing the Thunderbird adapter* 

	If you install the Thunderbird adapter as described, use the openerp_ch05X database to explore its functionality as described in this section

Microsoft Outlook interface
=============================

Everything that you can do with the Thunderbird plugin you can also do with the Microsoft Outlook plugin – enabling you to carry out a series of Open ERP operations directly from Outlook, such as:

* create a contact or partner from an email,

* archive an email and its attachments in Open ERP,

* send any file attached to an Open ERP document (such as proposals, projects, and tasks).

.. tip::   **Attention**  *Outlook versions* 

	The Microsoft Outlook plugin works with Microsoft Outlook 2003 and 2007 but not with Outlook Express

Installing the Outlook plugin
-------------------------------

To start, you must install the \ ``email_interface``\   module in Open ERP. It's the same module as used by the Thunderbird extension. Don't install it again if it's already there (which it might be because you can use both Outlook and Thunderbird simultaneously to get the same Open ERP functionality – so some of your staff may use one and other may use the other).

Once you've installed the module all you need is to run the Windows auto-installer \ ``tiny_outlook_plugin-X.exe``\   where X corresponds to the version number downloaded. This file can be found in the list of modules on the official Open ERP site.

Installation is then automatic.

Using the Outlook plugin
-------------------------

Using the Microsoft Outlook plugin is quite similar to using the Thunderbird extension. In Outlook find the menu  *Tools > Tiny ERP Options* .


	.. image::  images/outlook_menu.png
	   :align: center

*Configuration menu for the interface between Outlook and Open ERP*


In the window that you use for configuring the Outlook plugin you can enter parameters for accessing the Tiny server, with various options for: 

* how to handle attachments,

* which color to give emails transferred to Open ERP.

Once the server data entry is completed, click  *Test the Connection*  to check that your parameters make it function correctly.


	.. image::  images/outlook_config.png
	   :align: center

*Configuring access to Open ERP from Word*


When Outlook is configured, archiving an email and its attached files in Open ERP can be done in several ways:

* directly from the toolbar,

* from the context menu by right-clicking on an email,

* from the page while looking at the email.


	.. image::  images/outlook_archive.png
	   :align: center

*Saving an Outlook email in Open ERP*


You can select an existing contact or create a new contact on the fly in the Open ERP database. Then you can send the email and its attachments and also save it in Open ERP.

It's possible to send attachments to all types of Open ERP objects. For example this might be useful for:

* sending documents about a customer project into the corresponding project in Open ERP,

* attaching the documents about an order (such as proof of payment and order receipts),

* attaching documents to an employee file (such as their CV or annual appraisal).

Once the email is sent into Open ERP it's marked with another color in Outlook to help remind you not to archive it again.

.. tip::   **Note**  *Testing the Outlook adapter* 

	If you install the Outlook adapter as described, use the openerp_ch05X database to explore its functionality as described in this section

Microsoft Word interface
=========================

Open ERP supplies a Microsoft Word plugin that enables you to create your own document templates. What's more you can use the merge tool  *Tools > Merge documents*  to insert data from Open ERP while you generate different business documents.

So it's possible to create templates for a number of needs, such as proposals, business letters of agreement, or price requests. Each user can create his or her own document and use the plugin to obtain data from Open ERP. The plugin is very helpful for easily automating business actions.

Installing the Word plugin
---------------------------

The module for connecting Microsoft Word is also found in the list of Open ERP modules at . Once it's been downloaded install the file \ ``tiny_word_plugin-X.exe``\  .

When the program is installed, you must run Microsoft Word and configure the parameters that will enable you to access the Open ERP server from Word. Click the menu  *Tools > Tiny ERP options* .


	.. image::  images/word_menu.png
	   :align: center

*Menu for accessing the configuration of the plugin*

------------------

	.. image::  images/word_config.png
	   :align: center

*Configuration of the Word plugin for accessing Open ERP*


Using the Word interface
-------------------------

Start by selecting the module from which you want to make a report, for example a Sales Order. From Word you can access all the fields in an Open ERP Order, and all of the fields linked to that order such as from Order Lines, and from Products in those Order Lines.


	.. image::  images/word_module.png
	   :align: center

*Select the module that will generate the report*


Complete your document and insert Open ERP fields into the appropriate places.


	.. image::  images/word_fields.png
	   :align: center
	   :scale: 90

*Add Open ERP fields into a Word document*


.. tip::   **Attention**  *Fields in red* 

	When you've selected some fields and added them into your Word document, some of them appear in red. This color indicates that you can't use that particular field because it has a complex data relationships that can only be discovered when you start to use the field.

Select the merge tool from by clicking  *Perform Mail Merge*  from the toolbar. This connects Microsoft Word to Open ERP, at which point it searches for data to insert into the document. This tool enables you to select which documents must be included in the report. Make your selection and click  *Start Merge*  to run the tool that produces your different documents.


	.. image::  images/word_select.png
	   :align: center

*Selecting the Open ERP documents to use in the merge*


Word then generates the documents by inserting the Open ERP data. You get one page for each selected document.


	.. image::  images/word_finnish.png
	   :align: center

*Result of merging a Word document with data from Open ERP*


.. tip::   **Note**  *Testing the Word adapter* 

	If you install the Word adapter as described, use the openerp_ch05X database to explore its functionality as described in this section.

In Chapter 13 you'll see another, more powerful, module that enables you to create complete reports in OpenOffice.org through an interface added directly in Open ERP. So you can create your own templates, such as fax and invoice templates.

These reports can then be exported in PDF by leaving Open ERP, or can be edited before sending to a customer. So you can also personalize the details of your faxes and invoices as needed, even though they are based on your templates.



.. Copyright © Open Object Press. All rights reserved.

.. You may take electronic copy of this publication and distribute it if you don't
.. change the content. You can also print a copy to be read by yourself only.

.. We have contracts with different publishers in different countries to sell and
.. distribute paper or electronic based versions of this book (translated or not)
.. in bookstores. This helps to distribute and promote the Open ERP product. It
.. also helps us to create incentives to pay contributors and authors using author
.. rights of these sales.

.. Due to this, grants to translate, modify or sell this book are strictly
.. forbidden, unless Tiny SPRL (representing Open Object Presses) gives you a
.. written authorisation for this.

.. Many of the designations used by manufacturers and suppliers to distinguish their
.. products are claimed as trademarks. Where those designations appear in this book,
.. and Open ERP Press was aware of a trademark claim, the designations have been
.. printed in initial capitals.

.. While every precaution has been taken in the preparation of this book, the publisher
.. and the authors assume no responsibility for errors or omissions, or for damages
.. resulting from the use of the information contained herein.

.. Published by Open ERP Press, Grand Rosière, Belgium

