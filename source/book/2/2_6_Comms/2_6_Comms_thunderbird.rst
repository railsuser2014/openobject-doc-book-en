.. index::
   single: Thunderbird (Mozilla)

.. todo:: Tiny -> Open ERP

Mozilla Thunderbird interface
=============================

Everything that you can do with the Outlook plugin you can also do with the Mozilla Thunderbird
plugin – enabling you to carry out a series of Open ERP operations directly from Thunderbird, such
as:

* create a contact or partner from an email,

* save an email and its attachments in Open ERP,

* send any file attached to an Open ERP document (such as proposals, projects, and tasks).

Installing the Thunderbird extension
------------------------------------

To be able to use the Thunderbird plugin you first have to install the Open ERP module \
``email_interface``\  . It may not be loaded in the core of the Open ERP Server so you might have
to load it using one of the methods described at the end of :ref:`ch-inst`. Once you've got it into your
server's filesystem it's installed the same way as all of the other modules you've handled so far.

You'll then have to install the Thunderbird extension. To do that, use the file \
``tiny_plugin_2.0.xpi``\   which is found in the plugins directory of the :mod:`email_interface`
module. Don't install it again if it's already there (which it might be
because you can use both Outlook and Thunderbird simultaneously to get the same Open ERP
functionality – so some of your staff may use one and other may use the other). 

Then take the following steps:

	#. From Thunderbird, open the menu :menuselection:`Tools --> Complementary Modules`.

	#. Click the :guilabel:`Install` button.

	#. Select the file \ ``tiny_plugin-2.0.xpi``\.

	#. Click :guilabel:`Install Now` then restart Thunderbird.

Once the extension has been installed, you have only to create a shortcut in your Thunderbird
toolbar for the function :guilabel:`Archive to Open ERP`. Do it like this:

	#. Click the right mouse button on the toolbar and select :guilabel:`Personalize`,

	#. Place the icon :guilabel:`Archive to Open ERP` in your toolbar in the place of your choice.

.. tip::  Thunderbird version

	The Open ERP plugin for Thunderbird only works with Thunderbird version 2.0 and above.

	So check your Thunderbird version before installing, and download the latest version that you need
	from the following address: http://www.mozilla.org/products/thunderbird/

Thunderbird user interface
--------------------------

When you've installed the module the first thing to do is connect it to Open ERP from Thunderbird.
To do this use the menu :menuselection:`Tools --> Open ERP Plugin`.

A configuration window appears enabling you to enter configuration data about your Open ERP server.

.. figure::  images/thunderbird_config.png
   :scale: 50
   :align: center

   *Configuration for accessing Open ERP from Thunderbird*

To archive an email in Open ERP from Thunderbird select the email and click on the icon
:guilabel:`Archive in Open ERP`. Alternatively you could right-click the mouse: either opens a search
dialog box.

This allows you to select an object that you'd like to add to your email and its attachments. You
can select a partner, a task, a project, an analytical account, or any other object.

.. figure::  images/thunderbird_selection.png
   :scale: 50
   :align: center

   *Selecting Open ERP objects from Thunderbird*

.. tip:: Document Management

	The Thunderbird plugin is compatible with Open ERP's document management. So if you install the
	module document you could:

	* search through the content of your company's documents (those that have the type .doc, .pdf, .sxw
	  and .odt) and also in archived emails,

	* have a shared filesystem that's connected to various Open ERP documents to share information and
	  access it with your favorite browser,

	* organize and structure your documents (such as projects, partners and users) in Open ERP's
	  system.

If you can't find a partner or contact to correspond with your email in Open ERP it's possible to
create one on the fly simply by using the information contained in the email and clicking the
:guilabel:`Create` button.

.. figure::  images/thunderbird_creation.png
   :scale: 50
   :align: center

   *Creating a contact on the fly from Thunderbird*

To access archived data from different documents in Open ERP you can use the :guilabel:`Email
Thunderbird` interface that appears over Open ERP documents.

.. note:: Testing the Thunderbird adapter

	If you install the Thunderbird adapter as described,
	use the openerp_ch05X database to explore its functionality as described in this section

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

