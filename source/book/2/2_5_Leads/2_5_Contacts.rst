
Managing Contacts
=================

The two figures below show the UML classes with and without the ``base_contact`` module.

.. figure:: images/crm_contact_with.png
   :align: center

   *UML class diagram with base_contact.*

.. figure:: images/crm_contact_without.png
   :align: center

   *UML class diagram without base_contact.*

A concrete example will illustrate the concept of multiple relationships between contacts and
partners (companies)  The figure below shows two companies each having several addresses (places of
business) and several contacts attached to these addresses.

.. figure:: images/crm_contact_exemple.png
   :align: center

   *Example of a structure with management of partners and contacts.*

In this example you'll find the following elements:

* The ABC bank has two places of business, represented by the addresses of ABC Belgium and ABC
  Luxembourg,

* The addresses of Dexey France and Dexey Belgium belong to the Dexey company,

* At the office of ABC Luxembourg, you have the contacts of the director (D Fogerty) and the
  accountant (A. Jacket),

* Mr Jacket holds the post of accountant for ABC Luxembourg and Dexey France,

* Mr J Smith is director of Dexey France and Dexey Belgium and we also have his private address
  attached to no partner.

Depending on your needs, Open ERP provides three menus to access the same information:

* List of partners: :menuselection:`Partners --> Partners`,

* List of contacts: :menuselection:`Partners --> Contacts`,

* List of posts held by contacts at partners: :menuselection:`Partners --> Contact Posts`.

The three menus above are only three different views on the same data. If you correct a contact name
on the contact form, this will be modified on all the posts occupied in the different companies.

The screen above represents a partner form. You can see several possible address there and a list of
contacts above each address. For each contact you see a name, a function, a phone number and an
email.

.. figure:: images/crm_partner_contact.png
   :align: center

   *A partner form with the \ ``base_contact``\ module installed.*

If you click on the line you can get more detail about the function (such as start date, end date,
and fax) or enter into the contact form (such as personal phone, different posts occupied, and
personal blog).

.. figure:: images/crm_partner_poste.png
   :align: center

   *Detail of a post occupied by a contact at a partner.*

.. figure:: images/crm_partner_contacts.png
   :align: center

   *Detail of a contact form for someone occupying several posts.*

Partner management is found in the Open ERP base modules. To manager partner relations you must
install the CRM modules. Then start by installing a CRM profile and configure the system to meet
your needs.

For this chapter you should create a new database. After installing the database select
:guilabel:`Demonstration Data` and select the :guilabel:`CRM profile`. Open ERP's modularity enables you to install only
the CRM module if your requirements are limited to customer relationships.

.. figure:: images/crm_db_init.png
   :align: center

   *Creating a new database.*

Once the database is installed, Open ERP proposes that you configure it with a series of questions:

* Creating users: click :guilabel:`Skip`,

* Simplified or Extended mode: select simplified and click :guilabel:`Ok`,

* Select the CRM functionality to install.

.. figure:: images/ crm_db_select.png
   :align: center

   *Selecting the CRM functionality to install.*

.. note:: The CRM configuration module

    The pre-configuration of the management of customer relations to generate prospects,
    opportunities, and phone calls
    isn't supplied by the ``crm`` module itself but by the ``crm_configuration`` module.

If you install the modules separately don't forget to install the ``crm_configuration`` module.
The ``crm`` module just contains the generic case management system.

Open ERP proposes that you select from preconfigured functions for CRM:

* managing a prospects database,

* managing and tracking opportunities,

* managing meetings and the company calendar,

* managing pre-sales,

* managing phone calls and/or a call center,

* managing after-sales service,

* managing employment offers,

* managing technical service,

* tracking bugs and new functional requests.

You see that Open ERP's CRM module isn't limited just to Customer relationships but is designed to
generate all types of relations with a partner: such as suppliers, employees, customers, prospects.
This book will describe just customer relationships. The other CRM functions are similar in use, so
you shouldn't have problems with understanding those extra functions.

The following cases will be looked at for this chapter

* Prospect management,

* Opportunity management,

* Management of the company calendar,

* Management of phone calls.

The figure below shows the CRM module configuration screen after selecting some functions to
install.

.. figure:: images/crm_configuration_wizard.png
   :align: center

   *Selecting parameters for CRM modules for the reader of this chapter.*

Organizing Prospects
--------------------

If you have installed the management of prospects and opportunities, Open ERP implements the
following workflow for the qualification of prospects and future opportunities.

.. figure:: images/crm_flux.png
   :align: center

   *Process of converting a prospect into a customer or opportunity.*

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

