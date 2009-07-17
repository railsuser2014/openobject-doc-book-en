
.. i18n: .. index::
.. i18n:    single: Thunderbird (Mozilla)

.. index::
   single: Thunderbird (Mozilla)

.. i18n: Mozilla Thunderbird interface
.. i18n: =============================

Mozilla Thunderbird interface
=============================

.. i18n: Everything that you can do with the Outlook plugin you can also do with the Mozilla Thunderbird
.. i18n: plugin – enabling you to carry out a series of Open ERP operations directly from Thunderbird, such
.. i18n: as:

Everything that you can do with the Outlook plugin you can also do with the Mozilla Thunderbird
plugin – enabling you to carry out a series of Open ERP operations directly from Thunderbird, such
as:

.. i18n: * create a contact or partner from an email,
.. i18n: 
.. i18n: * save an email and its attachments in Open ERP,
.. i18n: 
.. i18n: * send any file attached to an Open ERP document (such as proposals, projects, and tasks).

* create a contact or partner from an email,

* save an email and its attachments in Open ERP,

* send any file attached to an Open ERP document (such as proposals, projects, and tasks).

.. i18n: Installing the Thunderbird extension
.. i18n: ------------------------------------

Installing the Thunderbird extension
------------------------------------

.. i18n: To be able to use the Thunderbird plugin you first have to install the Open ERP module \
.. i18n: ``thunderbird``\  . It may not be loaded in the core of the Open ERP Server so you might have
.. i18n: to load it using one of the methods described at the end of :ref:`ch-inst`. Once you've got it into your
.. i18n: server's filesystem it's installed the same way as all of the other modules you've handled so far.

To be able to use the Thunderbird plugin you first have to install the Open ERP module \
``thunderbird``\  . It may not be loaded in the core of the Open ERP Server so you might have
to load it using one of the methods described at the end of :ref:`ch-inst`. Once you've got it into your
server's filesystem it's installed the same way as all of the other modules you've handled so far.

.. i18n: You'll then have to install the Thunderbird extension. To do that, use the file \
.. i18n: ``tiny_plugin_2.0.xpi``\   which is found in the plugins directory of the :mod:`thunderbird`
.. i18n: module. Don't install it again if it's already there (which it might be
.. i18n: because you can use both Outlook and Thunderbird simultaneously to get the same Open ERP
.. i18n: functionality – so some of your staff may use one and other may use the other). 

You'll then have to install the Thunderbird extension. To do that, use the file \
``tiny_plugin_2.0.xpi``\   which is found in the plugins directory of the :mod:`thunderbird`
module. Don't install it again if it's already there (which it might be
because you can use both Outlook and Thunderbird simultaneously to get the same Open ERP
functionality – so some of your staff may use one and other may use the other). 

.. i18n: Then take the following steps:

Then take the following steps:

.. i18n: 	#. From Thunderbird, open the menu :menuselection:`Tools --> Complementary Modules`.
.. i18n: 
.. i18n: 	#. Click the :guilabel:`Install` button.
.. i18n: 
.. i18n: 	#. Select the file \ ``tiny_plugin-2.0.xpi``\.
.. i18n: 
.. i18n: 	#. Click :guilabel:`Install Now` then restart Thunderbird.

	#. From Thunderbird, open the menu :menuselection:`Tools --> Complementary Modules`.

	#. Click the :guilabel:`Install` button.

	#. Select the file \ ``tiny_plugin-2.0.xpi``\.

	#. Click :guilabel:`Install Now` then restart Thunderbird.

.. i18n: Once the extension has been installed, you have only to create a shortcut in your Thunderbird
.. i18n: toolbar for the function :guilabel:`Archive to Open ERP`. Do it like this:

Once the extension has been installed, you have only to create a shortcut in your Thunderbird
toolbar for the function :guilabel:`Archive to Open ERP`. Do it like this:

.. i18n: 	#. Click the right mouse button on the toolbar and select :guilabel:`Personalize`,
.. i18n: 
.. i18n: 	#. Place the icon :guilabel:`Archive to Open ERP` in your toolbar in the place of your choice.

	#. Click the right mouse button on the toolbar and select :guilabel:`Personalize`,

	#. Place the icon :guilabel:`Archive to Open ERP` in your toolbar in the place of your choice.

.. i18n: .. tip::  Thunderbird version
.. i18n: 
.. i18n: 	The Open ERP plugin for Thunderbird only works with Thunderbird version 2.0 and above.
.. i18n: 
.. i18n: 	So check your Thunderbird version before installing, and download the latest version that you need
.. i18n: 	from the following address: http://www.mozilla.org/products/thunderbird/

.. tip::  Thunderbird version

	The Open ERP plugin for Thunderbird only works with Thunderbird version 2.0 and above.

	So check your Thunderbird version before installing, and download the latest version that you need
	from the following address: http://www.mozilla.org/products/thunderbird/

.. i18n: Thunderbird user interface
.. i18n: --------------------------

Thunderbird user interface
--------------------------

.. i18n: When you've installed the module the first thing to do is connect it to Open ERP from Thunderbird.
.. i18n: To do this use the menu :menuselection:`Tools --> Open ERP Plugin`.

When you've installed the module the first thing to do is connect it to Open ERP from Thunderbird.
To do this use the menu :menuselection:`Tools --> Open ERP Plugin`.

.. i18n: A configuration window appears enabling you to enter configuration data about your Open ERP server.

A configuration window appears enabling you to enter configuration data about your Open ERP server.

.. i18n: .. figure::  images/thunderbird_config.png
.. i18n:    :scale: 50
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Configuration for accessing Open ERP from Thunderbird*

.. figure::  images/thunderbird_config.png
   :scale: 50
   :align: center

   *Configuration for accessing Open ERP from Thunderbird*

.. i18n: To archive an email in Open ERP from Thunderbird select the email and click on the icon
.. i18n: :guilabel:`Archive in Open ERP`. Alternatively you could right-click the mouse: either opens a search
.. i18n: dialog box.

To archive an email in Open ERP from Thunderbird select the email and click on the icon
:guilabel:`Archive in Open ERP`. Alternatively you could right-click the mouse: either opens a search
dialog box.

.. i18n: This allows you to select an object that you'd like to add to your email and its attachments. You
.. i18n: can select a partner, a task, a project, an analytical account, or any other object and attach 
.. i18n: selected mail as .eml file in attachment of selected record.

This allows you to select an object that you'd like to add to your email and its attachments. You
can select a partner, a task, a project, an analytical account, or any other object and attach 
selected mail as .eml file in attachment of selected record.

.. i18n: You can create new case in crm using Create Case button.Select a section for which you want to
.. i18n: create case.

You can create new case in crm using Create Case button.Select a section for which you want to
create case.

.. i18n: .. figure::  images/thunderbird_selection.png
.. i18n:    :scale: 50
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Selecting Open ERP objects from Thunderbird*

.. figure::  images/thunderbird_selection.png
   :scale: 50
   :align: center

   *Selecting Open ERP objects from Thunderbird*

.. i18n: .. tip:: Document Management
.. i18n: 
.. i18n: 	The Thunderbird plugin is compatible with Open ERP's document management. So if you install the
.. i18n: 	module document you could:
.. i18n: 
.. i18n: 	* search through the content of your company's documents (those that have the type .doc, .pdf, .sxw
.. i18n: 	  and .odt) and also in archived emails,
.. i18n: 
.. i18n: 	* have a shared filesystem that's connected to various Open ERP documents to share information and
.. i18n: 	  access it with your favorite browser,
.. i18n: 
.. i18n: 	* organize and structure your documents (such as projects, partners and users) in Open ERP's
.. i18n: 	  system.

.. tip:: Document Management

	The Thunderbird plugin is compatible with Open ERP's document management. So if you install the
	module document you could:

	* search through the content of your company's documents (those that have the type .doc, .pdf, .sxw
	  and .odt) and also in archived emails,

	* have a shared filesystem that's connected to various Open ERP documents to share information and
	  access it with your favorite browser,

	* organize and structure your documents (such as projects, partners and users) in Open ERP's
	  system.

.. i18n: If you can't find a partner or contact to correspond with your email in Open ERP it's possible to
.. i18n: create one on the fly simply by using the information contained in the email and clicking the
.. i18n: :guilabel:`Create` button.

If you can't find a partner or contact to correspond with your email in Open ERP it's possible to
create one on the fly simply by using the information contained in the email and clicking the
:guilabel:`Create` button.

.. i18n: .. figure::  images/thunderbird_creation.png
.. i18n:    :scale: 50
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Creating a contact on the fly from Thunderbird*

.. figure::  images/thunderbird_creation.png
   :scale: 50
   :align: center

   *Creating a contact on the fly from Thunderbird*

.. i18n: To access archived data from different documents in Open ERP you can use the :guilabel:`Email
.. i18n: Thunderbird` interface that appears over Open ERP documents.

To access archived data from different documents in Open ERP you can use the :guilabel:`Email
Thunderbird` interface that appears over Open ERP documents.

.. i18n: .. note:: Testing the Thunderbird adapter
.. i18n: 
.. i18n: 	If you install the Thunderbird adapter as described,
.. i18n: 	explore its functionality as described in this section using the database you 
.. i18n: 	installed.

.. note:: Testing the Thunderbird adapter

	If you install the Thunderbird adapter as described,
	explore its functionality as described in this section using the database you 
	installed.

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
