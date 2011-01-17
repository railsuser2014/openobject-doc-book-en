*********************
What's new in OpenERP
*********************

.. index::
   single: new
   single: features

General Features
================

* OpenERP has been structured as Business Applications and its menu has been changed to match this,

* Great Improvements as to Useability, not in the least in the Web version,

* When you click a Business Application in the Web version, the related Dashboard will be opened.

* Menutips & Tooltips will be displayed to explain more about the active screen,

* Dynamic Filters which allow you to easily create and save your own filters, with Group by options, Extended filters, and much more,

* User Roles are no longer used, they have been integrated in the User Groups,

* The Administrator will now only have the rights according to the user groups that have been assigned to him,

* Multicompany has been integrated in the core of OpenERP and does not require the installation of modules. You just have to add the User Group Useability / Multi-Company,

* Perform actions, such as update status, confirm, delete, ... directly from List View,

* Use communication tools such as Fetchmail, Outlook & Thunderbird integration and CalDAV / WebDAV (also available on Android & Iphone),

* Create your own e-mail templates for use throughout OpenERP,

* Use the Scheduler for other objects than Manufacturing.

Business Application-related Features
=====================================

*Sales Management*

* CRM has been integrated in the Sales Management Business Application,

* Geolocalization module, also allowing you to send qualified opportunities directly to external partners,

* Manage your Marketing Campaigns and send automated e-mails based on your own templates,

* For Leads, OpenERP will check the email address of the contact and when found for an existing partner, it will propose to merge the new contact with the corresponding partner,  

* Create your company wiki for Sales FAQ,

* History tab in the Customer form to keep track of all events,
 
*Warehouse Management*

* Push & Pull rules for stock locations have been extended and integrated with multicompany,

*Accounting & Financial Management*

* By default, only one Entry Sequence available for a journal. If you want to have two sequences to be used for your journal numbering, please install the :mod:`account_sequence` module,

* Separate numbering now also available for Bank Journals,

* Quickly enter Journal Entries from List View from the Journal Items menu. Configure your journal with default debit & credit accounts, select the journal in the Journal Items List View, click New and start creating new entries, 

* Chart of Accounts and Chart of Taxes can be displayed for a selected period,

* OpenERP added a flexible, easy Invoicing module allowing you to keep track of your accounting, even when you are not an accountant. If you install the Invoicing module, in Simplified view, you will only have the Invoicing items. You shouldn't use both Invoicing and Accounting,

* Use the Financial Management Configuration Wizard to easily select features you want to use.

* On installation of a predefined Chart of Accounts, the wizard also proposes default bank and cash accounts, and default Sales and Purchase taxes,

* On a journal you can set whether OpenERP should perform a check whether the invoice date is in the current period. This used to be a separate module,

* Different journal types for Refunds and Invoices,

* When creating a new journal, parameters are preset according to the journal type. The Entry Sequence for the journal is automatically created on Save,

* Cash Box, possible to keep a real cash register.

*Project Management*

* Improved Gantt chart in the Web version,

* Long Term Planning that can be calculated according to the working time of each employee involved in the project with the new Scheduler feature,

*Manufacturing Management* 

* Scrap consumed or finished goods and have the related stock moves automatically,

* Consume products partially or completely.

*Human Resources Management*

* Manage your evaluation process,

* Keep track of your recruitments and receive applicant mails directly in OpenERP, including attachments.


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

