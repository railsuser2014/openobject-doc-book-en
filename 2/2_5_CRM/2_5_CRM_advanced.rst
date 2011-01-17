.. index::
   single: advanced
   single: customer
   single: report
..

Advanced Customer Relations
===========================

OpenERP also supplies several tools to improve and automate relationships with partners. They will not be described in detail here, just briefly introduced.

The Web client allows you to define specific access rules to allow your customers to access useful information, such as orders or deliveries.

.. index::
   single: module; fetchmail

Fetchmail
---------

The *Fetchmail* functionality lets you interface the CRM with incoming and outgoing e-mails.
You can install this feature when you configure the CRM or by installing the :mod:`fetchmail` module.
It also allows you to create an object in OpenERP from an e-mail you receive.
Simply define the generic mail address you want to use, such as sales@openerp.com, and link it to the crm.lead object.
Every mail that is sent to this address, will automatically created as a lead for you to qualify.

.. index::
   single: module; outlook, thunderbird

The Outlook and Thunderbird plugins let you easily create contacts from your mail client in OpenERP.
You can also link e-mails (with attachments) to OpenERP, to avoid information getting lost.
Both plugins enable you to create sales leads based on exchanges you have with the customer.

Automated Actions
-----------------

The rules for automating actions enable you to send emails automatically based on the event,
such as assigning opportunities to the most appropriate person. To access the CRM rules, use the
menu :menuselection:`Sales --> Configuration --> Automated Actions --> Automated Actions`.

.. index::
   single: module; crm_profiling

Profiling
---------

The segmentation tools let you create partner groups and act on each segment differently according to questionnaires.
For example you could create pricelists for each of the segments, or start phone marketing campaigns
by segment. To enable the management of segmentation you should install the module
:mod:`crm_profiling`, which can also be achieved from the Configuration Wizard.

.. index::
   single: module; base_report_designer

Report Designer
---------------

The :mod:`base_report_designer` module enables you to create letter templates in OpenOffice and automate
letters for different prospects. OpenERP also has e-mail templates to simplify the creation of
mass mailing.


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

