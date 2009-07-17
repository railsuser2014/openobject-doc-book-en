
.. i18n: .. index:: Outlook (Microsoft)

.. index:: Outlook (Microsoft)

.. i18n: Microsoft Outlook interface
.. i18n: ===========================

Microsoft Outlook interface
===========================

.. i18n: The Microsoft Outlook plugin enables you to carry out a series of Open ERP operations directly
.. i18n: from the Outlook email client:

The Microsoft Outlook plugin enables you to carry out a series of Open ERP operations directly
from the Outlook email client:

.. i18n: * create a contact or partner from an email,
.. i18n: 
.. i18n: * archive an email and its attachments in Open ERP,
.. i18n: 
.. i18n: * send any file attached to an Open ERP document (such as proposals, projects, and tasks).

* create a contact or partner from an email,

* archive an email and its attachments in Open ERP,

* send any file attached to an Open ERP document (such as proposals, projects, and tasks).

.. i18n: .. tip:: Outlook versions
.. i18n: 
.. i18n: 	The Microsoft Outlook plugin works with Microsoft Outlook 2003 and 2007 but not with Outlook
.. i18n: 	Express

.. tip:: Outlook versions

	The Microsoft Outlook plugin works with Microsoft Outlook 2003 and 2007 but not with Outlook
	Express

.. i18n: Installing the Outlook plugin
.. i18n: -----------------------------

Installing the Outlook plugin
-----------------------------

.. i18n: To start, you must install the :mod:`email_interface` module in Open ERP. It's the same module as
.. i18n: used by the Thunderbird extension. Don't install it again if it's already there (which it might be
.. i18n: because you can use both Outlook and Thunderbird simultaneously to get the same Open ERP
.. i18n: functionality – so some of your staff may use one and other may use the other).

To start, you must install the :mod:`email_interface` module in Open ERP. It's the same module as
used by the Thunderbird extension. Don't install it again if it's already there (which it might be
because you can use both Outlook and Thunderbird simultaneously to get the same Open ERP
functionality – so some of your staff may use one and other may use the other).

.. i18n: Once you've installed the module all you need is to run the Windows auto-installer \
.. i18n: ``tiny_outlook_plugin-X.exe``\   where X corresponds to the version number downloaded. This file can
.. i18n: be found in the list of modules on the official Open ERP site.

Once you've installed the module all you need is to run the Windows auto-installer \
``tiny_outlook_plugin-X.exe``\   where X corresponds to the version number downloaded. This file can
be found in the list of modules on the official Open ERP site.

.. i18n: Installation is then automatic.

Installation is then automatic.

.. i18n: Using the Outlook plugin
.. i18n: ------------------------

Using the Outlook plugin
------------------------

.. i18n: Using the Microsoft Outlook plugin is quite similar to using the Thunderbird extension. In Outlook
.. i18n: find the menu :menuselection:`Tools --> Open ERP Options`.

Using the Microsoft Outlook plugin is quite similar to using the Thunderbird extension. In Outlook
find the menu :menuselection:`Tools --> Open ERP Options`.

.. i18n: .. figure::  images/outlook_menu.png
.. i18n:    :scale: 50
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Configuration menu for the interface between Outlook and Open ERP*

.. figure::  images/outlook_menu.png
   :scale: 50
   :align: center

   *Configuration menu for the interface between Outlook and Open ERP*

.. i18n: In the window that you use for configuring the Outlook plugin you can enter parameters for accessing
.. i18n: the Open ERP server, with various options for:

In the window that you use for configuring the Outlook plugin you can enter parameters for accessing
the Open ERP server, with various options for:

.. i18n: * how to handle attachments,
.. i18n: 
.. i18n: * which color to give emails transferred to Open ERP.

* how to handle attachments,

* which color to give emails transferred to Open ERP.

.. i18n: Once the server data entry is completed, click :guilabel:`Test the Connection` to check that your
.. i18n: parameters make it function correctly.

Once the server data entry is completed, click :guilabel:`Test the Connection` to check that your
parameters make it function correctly.

.. i18n: .. figure::  images/outlook_config.png
.. i18n:    :scale: 50
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Configuring access to Open ERP from Word*

.. figure::  images/outlook_config.png
   :scale: 50
   :align: center

   *Configuring access to Open ERP from Word*

.. i18n: When Outlook is configured, archiving an email and its attached files in Open ERP can be done in
.. i18n: several ways:

When Outlook is configured, archiving an email and its attached files in Open ERP can be done in
several ways:

.. i18n: * directly from the toolbar,
.. i18n: 
.. i18n: * from the context menu by right-clicking on an email,
.. i18n: 
.. i18n: * from the page while looking at the email.

* directly from the toolbar,

* from the context menu by right-clicking on an email,

* from the page while looking at the email.

.. i18n: .. figure::  images/outlook_archive.png
.. i18n:    :scale: 50
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Saving an Outlook email in Open ERP*

.. figure::  images/outlook_archive.png
   :scale: 50
   :align: center

   *Saving an Outlook email in Open ERP*

.. i18n: You can select an existing contact or create a new contact on the fly in the Open ERP database.
.. i18n: Then you can send the email and its attachments and also save it in Open ERP.

You can select an existing contact or create a new contact on the fly in the Open ERP database.
Then you can send the email and its attachments and also save it in Open ERP.

.. i18n: It's possible to send attachments to all types of Open ERP objects. For example this might be
.. i18n: useful for:

It's possible to send attachments to all types of Open ERP objects. For example this might be
useful for:

.. i18n: * sending documents about a customer project into the corresponding project in Open ERP,
.. i18n: 
.. i18n: * attaching the documents about an order (such as proof of payment and order receipts),
.. i18n: 
.. i18n: * attaching documents to an employee file (such as their CV or annual appraisal).

* sending documents about a customer project into the corresponding project in Open ERP,

* attaching the documents about an order (such as proof of payment and order receipts),

* attaching documents to an employee file (such as their CV or annual appraisal).

.. i18n: Once the email is sent into Open ERP it's marked with another color in Outlook to help remind you
.. i18n: not to archive it again.

Once the email is sent into Open ERP it's marked with another color in Outlook to help remind you
not to archive it again.

.. i18n: .. note:: Testing the Outlook adapter
.. i18n: 
.. i18n: 	If you install the Outlook adapter as described,
.. i18n: 	explore its	functionality with the database as described in this section.

.. note:: Testing the Outlook adapter

	If you install the Outlook adapter as described,
	explore its	functionality with the database as described in this section.

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
