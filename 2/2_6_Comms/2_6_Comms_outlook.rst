.. index:: Outlook (Microsoft)

Microsoft Outlook interface
===========================

The Microsoft Outlook plugin enables you to carry out a series of OpenERP operations directly
from the Outlook e-mail client:

* create a contact or partner from an e-mail,

* save an e-mail and its attachments in OpenERP,

* send any attachment to an OpenERP document (such as proposals, projects, and tasks).

This might be useful for sending documents about a customer project to the corresponding project in OpenERP, attaching documents to an order (such as proof of payment and order receipts), attaching documents to an employee file (such as a CV or annual appraisal).

.. tip:: Outlook versions

	The Microsoft Outlook plugin works with Microsoft Outlook 2003 and 2007 but not with Outlook
	Express

Installing the Outlook plugin
-----------------------------

* Step 1: install the Outlook plugin in OpenERP

Use the OpenERP Configuration Wizard and install the ``Customer Relationship Management`` application. In the *CRM Application Configuration* dialog under Plug-In, select MS-Outlook.
Then the *Outlook Plug-In* wizard appears. Next to the ``Outlook Plug-in`` field, click the ``Save As`` button to save the plugin to your desktop (or any other location on your computer).

You can also download the installation manual by clicking the green arrow next to ``Installation Manual``.  

Another way to use the Outlook plugin, is by installing the OpenERP module \
``outlook``\. When you install this module, the same Configuration Wizard as explained before will be displayed. Follow the same instructions.


* Step 2: Prerequisites

|  1. Install Python 2.6+
|  Download from http://www.python.org/ftp/python/2.6.6/python-2.6.6.msi
|  or for 64bit system http://www.python.org/ftp/python/2.6.6/python-2.6.6.amd64.msi. Run the .exe file to install the software.
|
|   2. Python for Windows extensions - PyWin32, this module for python must be installed for the appropriate version of Python.
|   http://sourceforge.net/projects/pywin32/files/pywin32/Build%20214/pywin32-214.win32-py2.6.exe/download or for 64bit system
|   http://sourceforge.net/projects/pywin32/files/pywin32/Build%20214/pywin32-214.win-amd64-py2.6.exe/download
|
|   3. Specify the python folder in the system path (typically with this installer C:\Python26)
|
|   *How to set the path in Windows XP*
|   For Windows XP: http://www.computerhope.com/issues/ch000549.htm
|    
|   *How to set the path in Windows 7*
|   To change the system environment variables, follow the steps below. 
|
|   - From the Windows button, select ``Control Panel``, then click ``System``. 
|   - Click ``Remote Settings`` to open the System Properties window.
|   - In the System Properties window, click the Advanced tab. 
|   - In the Advanced section, click the ``Environment Variables`` button. 
|   - Finally, in the Environment Variables window (as shown below) under System Variables, highlight the Path directory,
|     click Edit and add ;C:\Python26.
|     See also http://geekswithblogs.net/renso/archive/2009/10/21/how-to-set-the-windows-path-in-windows-7.aspx
|
|   4. If you are using MS Outlook 2007 than you are required to install "Microsoft Exchange Server MAPI Client and Collaboration
|   Data Objects 1.2.1 (CDO 1.21)" from
|   http://www.microsoft.com/downloads/en/details.aspx?FamilyId=2714320D-C997-4DE1-986F-24F081725D36&displaylang=en.
|   Double-click Exchange Cdo to install it.
|
|   5. If you are using MS Outlook 2003, be sure to install the builtin Cdo component.


* Step 3: install the OpenERP extension in Outlook.

	#. Double-click the file \``OpenERP-Outlook-addin.exe``\ that you saved on your desktop. Confirm the default settings.

	#. Double-click the file \``Register plugin``\ in the OpenERP Outlook Addin folder (typically in C:\Program Files).

	#. Start Outlook.

Configuring the Outlook plugin
------------------------------

When you have executed Installation Step 1, Step 2 and Step 3, the first thing to do is connect Outlook to OpenERP.
A little configuration needs to be done.

.. tip:: If you want the OpenERP connection to be shown as a separate toolbar, go to the menu :menuselection:`View --> Toolbars`. Select ``OpenERP``.

* Go to the menu :menuselection:`Tools` and select `Configuration`. If this raises an error, make sure to check the rights to that particular folder.

A configuration window appears enabling you to enter configuration data about your OpenERP server.

.. figure::  images/outlook_menu2.png
   :scale: 50
   :align: center

   *How to Connect to the Server*

	#. On the ``Configuration Settings`` tab, under *Connection Parameters* click the `Change` button
	   and type your server settings and xml-rpc port, e.g. ``http://127.0.0.1:8069``,

	#. Select the database you want to connect to, and type the user and the password required to log in to the database,

	#. Click the `Connect` button,

	#. On the ``Configuration Settings`` tab, under *Webserver Parameters* click the `Change` button
	   and type your web server settings, e.g. ``http://localhost:8080``,

	#. Click the `Open` button to test the connection.

When your connection has succeeded, you would typically want to configure Outlook to fit your needs.

To define extra document types, go to the `Document Settings` tab. This is the place where you can add objects from OpenERP that you wish to link mails to. The default installation comes with a number of predefined documents, such as Partners, Leads and Sales Orders.

Here is an example of how to configure extra document types. Suppose you would like to link mails to a meeting.

	#. In the `Title`, type Meeting,

	#. In the `Document`, type the object from OpenERP, in this example ``crm.meeting``,

	#. In the `Image`, select an icon you would like to use,

	#. Click the `Add` button to actually create the document type.

.. note:: To find the object you need in OpenERP, go to the menu :menuselection:`Administration --> Customization --> Database Structure --> Objects`. OpenERP will only show objects for which the corresponding Business Applications / Modules have been installed. You can only add objects to Outlook that are available in the selected database.

Using the Outlook plugin
------------------------

You can use the menu :menuselection:`Tools` for several things.

The `Push` option allows you to archive e-mails to OpenERP, either to new document types or to existing ones. It also allows you to create a new contact.

The `Partner` allows you to open the Partner in OpenERP according to the e-mail (i.e. contact e-mail address) selected. 

With `Document`, you can open the document concerned in OpenERP. Make sure you are logged in to the web version to use this functionality. 

* Link a mail to an existing document in OpenERP

.. figure::  images/outlook_config2.png
   :scale: 50
   :align: center

   *How to Access OpenERP from Outlook?*

To archive an e-mail in OpenERP from Outlook, select the e-mail and click the `Push` button. Alternatively you can open the menu :menuselection:`Tools --> Push`: the ``Push to OpenERP`` screen will open.

In the ``Link to an Existing Document`` section, select an object to which you like to add to your email and its attachments. You
can select any object you defined in the ``Document Settings`` section and attach the selected mail to the selected record.
The plugin also allows you to select several documents at once, simply by selecting a document and pressing the ``ctrl`` button when selecting the next document.

Do not forget to click the ``Search`` button to refresh the Documents list when you have selected a different document type.    

* Create a New Document

This feature can be used to create any of the configured document types in the ``Document Settings`` tab.
Suppose you would like to create a new lead from an e-mail. In the ``Create a New Document`` section, select ``CRM Lead``, then click the ``Create`` button. A new lead will be created in OpenERP from the selected e-mail.

* Create a New Contact / Partner

If you cannot find a partner or contact for your e-mail in OpenERP, the Outlook plugin allows you to
create one on the fly simply by using the information contained in the e-mail.

Select the e-mail from which you want to create a new contact, then click the ``Push`` button.
In the ``Create a New Contact`` section, click the ``New Contact`` button. This option offers two possibilities:
either you just create a contact (address), or you create a partner with the contact linked to it.

	- When you just want to create a new contact, complete the address data in the dialog box and click the ``Save`` button.
	  The contact will then be created in OpenERP.

	- When you also want to create a new partner, complete the contact data.
	  Then click the ``Create Partner`` button, add the partner's name and click the ``Save`` button.

	- You can also add a new contact to an existing partner. Click the ``Search`` button next to the Partner field
	  and select the corresponding partner from the list. Then complete the contact data and click the ``Save`` button.

.. figure::  images/outlook_creation.png
   :scale: 50
   :align: center

   *Creating a contact on the fly from Outlook*

* Open the Document created in OpenERP

To access archived data from different documents in OpenERP you can use the menu :menuselection:`Tools --> Document` which allows you to access the document in OpenERP directly from your e-mail.

.. tip:: Knowledge Management

	The Outlook plugin is compatible with OpenERP's Knowledge (i.e. Document) Management. If you install the
	Knowledge application you will be able to:

	* search through the content of your company's documents (those that have the type .doc, .pdf, .sxw
	  and .odt) and also in archived emails,

	* have a shared file system that is connected to various OpenERP documents to share information and
	  access it with your favorite browser,

	* organize and structure your documents (such as projects, partners and users) in OpenERP's
	  system.

.. note:: Testing the Outlook adapter

	If you have installed the Outlook adapter as described,
	explore its functionality with the database as described in this section.

.. Copyright © Open Object Press. All rights reserved.

.. You may take electronic copy of this publication and distribute it if you don't
.. change the content. You can also print a copy to be read by yourself only.

.. We have contracts with different publishers in different countries to sell and
.. distribute paper or electronic based versions of this book (translated or not)
.. in bookstores. This helps to distribute and promote the Open ERP product. It
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

