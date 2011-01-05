.. index::
   single: advanced
   single: customer
   single: report
..

Advanced Customer Relations
===========================

Open ERP also supplies several tools to improve and automate relationships with partners. They won't
be described extensively here, just introduced briefly.

.. index::
   single: modules; portal_

The supplier/customer portal gives you the ability to provide your suppliers and customers with
constrained access to Open ERP. They will then be able to view or enter sets of information directly
online to Open ERP. For example they could enter their orders, reprint their invoices, or work on
communal projects. To activate the portal you should install the modules that start with the
string :mod:`portal_`.

The email gateway lets you interface the CRM with incoming and outgoing emails. The scripts used for
the email gateway are available in the :mod:`crm` module in the ``scripts`` subdirectory.

Outlook and Thunderbird plugins let you synchronize your contacts between your email
client and your ERP. They both enable you to create sales opportunities based on exchanges you have
with the customer.

The rules for automating actions enable you to send emails automatically based on the event,
such as assigning opportunities to the most appropriate person. To access the CRM rules, use the
menu :menuselection:`Sales --> Configuration --> Automated Actions --> Automated Actions`.

.. index::
   single: module; crm_profiling

The segmentation tools let you create partner groups and act on each segment differently.
For example you could create pricelists for each of the segments, or start phone marketing campaigns
by segment. To enable the management of segmentation you should install the module
:mod:`crm_profiling`.

.. index::
   single: module; base_report_designer

The :mod:`base_report_designer` module enables you to create letter templates in OpenOffice and automate
letters for different prospects. Open ERP also has plugins for MS Word to simplify the creation of
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

