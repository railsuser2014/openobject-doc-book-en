
.. i18n: .. index::
.. i18n:    single: Partner
.. i18n: ..

.. index::
   single: Partner
..

.. i18n: Partners
.. i18n: ========

Partners
========

.. i18n: In Open ERP, a partner represents all the entities that you can do business with. Some possible
.. i18n: different types of partners are:

In Open ERP, a partner represents all the entities that you can do business with. Some possible
different types of partners are:

.. i18n: * suppliers,
.. i18n: 
.. i18n: * manufacturers,
.. i18n: 
.. i18n: * customers,
.. i18n: 
.. i18n: * clients,
.. i18n: 
.. i18n: * employees,
.. i18n: 
.. i18n: * prospects.

* suppliers,

* manufacturers,

* customers,

* clients,

* employees,

* prospects.

.. i18n: The concept of a partner here is much more flexible than in many other management applications
.. i18n: because a partner can correspond to one type or a combination of several of these types. This avoids
.. i18n: double data-entry and provides greater flexibility in the features available.

The concept of a partner here is much more flexible than in many other management applications
because a partner can correspond to one type or a combination of several of these types. This avoids
double data-entry and provides greater flexibility in the features available.

.. i18n: So a partner can be both your supplier and your customer at the same time. This feature is
.. i18n: particularly important when you have subsidiaries or franchises since transactions between the
.. i18n: parent and its subsidiaries in these cases will generally be two-way.

So a partner can be both your supplier and your customer at the same time. This feature is
particularly important when you have subsidiaries or franchises since transactions between the
parent and its subsidiaries in these cases will generally be two-way.

.. i18n: To get a list of partners using demonstration data, use the menu :menuselection:`Partners -->
.. i18n: Partners`.

To get a list of partners using demonstration data, use the menu :menuselection:`Partners -->
Partners`.

.. i18n: .. figure::  images/crm_partner.png
.. i18n:    :scale: 50
.. i18n:    :align: center
.. i18n: 
.. i18n:    *A partner form*

.. figure::  images/crm_partner.png
   :scale: 50
   :align: center

   *A partner form*

.. i18n: .. index::
.. i18n:    single: send SMS

.. index::
   single: send SMS

.. i18n: To the right of the partner form you'll find all of the actions, reports and shortcuts available to
.. i18n: the selected partner. This enables you to quickly send an SMS message, for example, or review a
.. i18n: partner's order history, or print a reminder letter.

To the right of the partner form you'll find all of the actions, reports and shortcuts available to
the selected partner. This enables you to quickly send an SMS message, for example, or review a
partner's order history, or print a reminder letter.

.. i18n: .. tip::  Send an SMS message
.. i18n: 
.. i18n: 	To send an SMS message from standard Open ERP you'll have to place an order with the bulk SMS
.. i18n: 	gateway operator Clickatell™http://clickatell.com.
.. i18n: 
.. i18n: 	You'll then receive an API number, a login and a password which you can use in Open ERP to send
.. i18n: 	SMS messages to your partners.
.. i18n: 
.. i18n: 	Or you can just develop a new module based on the inbuilt SMS functions, targeted at any of the
.. i18n: 	other SMS service suppliers, and use that instead.

.. tip::  Send an SMS message

	To send an SMS message from standard Open ERP you'll have to place an order with the bulk SMS
	gateway operator Clickatell™http://clickatell.com.

	You'll then receive an API number, a login and a password which you can use in Open ERP to send
	SMS messages to your partners.

	Or you can just develop a new module based on the inbuilt SMS functions, targeted at any of the
	other SMS service suppliers, and use that instead.

.. i18n: To send an SMS message to a partner or a selection of several partners, first select the partners
.. i18n: then click the :guilabel:`Send SMS` Action icon.

To send an SMS message to a partner or a selection of several partners, first select the partners
then click the :guilabel:`Send SMS` Action icon.

.. i18n: To create a company in Open ERP (that is – a new partner) you should at a minimum enter the
.. i18n: company's :guilabel:`Name` in the partner form.

To create a company in Open ERP (that is – a new partner) you should at a minimum enter the
company's :guilabel:`Name` in the partner form.

.. i18n: .. index:: Contact

.. index:: Contact

.. i18n: Contacts
.. i18n: --------

Contacts
--------

.. i18n: You can have several contacts for one partner. Contacts represent company employees that you're in
.. i18n: contact with, along with their address details. For each address you can indicate their type (\
.. i18n: ``Default``\  , \ ``Invoice``\  , \ ``Delivery``\  , \ ``Contact``\   or \ ``Other``\  ). Based on
.. i18n: this, Open ERP can supply an address that matches the contact's function when generating documents
.. i18n: at various stages through an Order process.

You can have several contacts for one partner. Contacts represent company employees that you're in
contact with, along with their address details. For each address you can indicate their type (\
``Default``\  , \ ``Invoice``\  , \ ``Delivery``\  , \ ``Contact``\   or \ ``Other``\  ). Based on
this, Open ERP can supply an address that matches the contact's function when generating documents
at various stages through an Order process.

.. i18n: Contacts can be entered into the first (:guilabel:`General`) tab of the :guilabel:`Partners` form,
.. i18n: or you can get direct access to the list of addresses through the :menuselection:`Partners -->
.. i18n: Partner Contacts` menu.

Contacts can be entered into the first (:guilabel:`General`) tab of the :guilabel:`Partners` form,
or you can get direct access to the list of addresses through the :menuselection:`Partners -->
Partner Contacts` menu.

.. i18n: You can search for a subset of Partners and Contacts using their company :guilabel:`Name` or
.. i18n: :guilabel:`Contact name` or part of the address, or any of the other search fields in either the
.. i18n: :guilabel:`Basic Search` or the :guilabel:`Advanced Search` tab.

You can search for a subset of Partners and Contacts using their company :guilabel:`Name` or
:guilabel:`Contact name` or part of the address, or any of the other search fields in either the
:guilabel:`Basic Search` or the :guilabel:`Advanced Search` tab.

.. i18n: .. note:: Independent partners or physical people
.. i18n: 
.. i18n: 	If you want to represent a physical person rather than a company, in Open ERP, that person's name
.. i18n: 	can be typed directly into the :guilabel:`Name` field on the Partner form. In this case don't put
.. i18n: 	in any Contact Name.

.. note:: Independent partners or physical people

	If you want to represent a physical person rather than a company, in Open ERP, that person's name
	can be typed directly into the :guilabel:`Name` field on the Partner form. In this case don't put
	in any Contact Name.

.. i18n: .. index::
.. i18n:    pair: partner; category
.. i18n: ..

.. index::
   pair: partner; category
..

.. i18n: Partner Categories
.. i18n: ------------------

Partner Categories
------------------

.. i18n: Open ERP uses hierarchical categories to organize all of its partners. To reach the list of
.. i18n: available partner categories, use the menu :menuselection:`Partners --> Partners by Category`.

Open ERP uses hierarchical categories to organize all of its partners. To reach the list of
available partner categories, use the menu :menuselection:`Partners --> Partners by Category`.

.. i18n: .. figure::  images/crm_partner_category_big.png
.. i18n:    :scale: 50
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Example Partner Category structure*

.. figure::  images/crm_partner_category_big.png
   :scale: 50
   :align: center

   *Example Partner Category structure*

.. i18n: Double-click one of the categories in the partner category structure to get a list of the partners
.. i18n: in that category. If you click on a category that has sub-categories you'll get a list of all of the
.. i18n: partners in the main category and in all of its subcategories.

Double-click one of the categories in the partner category structure to get a list of the partners
in that category. If you click on a category that has sub-categories you'll get a list of all of the
partners in the main category and in all of its subcategories.

.. i18n: Because categories are structured in a hierarchical manner, you can apply an action at any level of
.. i18n: the structure: a marketing promotion activity, for example, can be applied either to all customers,
.. i18n: or selectively only to customers in one category and its subcategories.

Because categories are structured in a hierarchical manner, you can apply an action at any level of
the structure: a marketing promotion activity, for example, can be applied either to all customers,
or selectively only to customers in one category and its subcategories.

.. i18n: The tree structure is also very useful when you're running the various statistical reports. You can
.. i18n: structure reports at any level of the hierarchy using this partner segmentation.

The tree structure is also very useful when you're running the various statistical reports. You can
structure reports at any level of the hierarchy using this partner segmentation.

.. i18n: In the following sections you'll see how to assign partners to categories manually (perhaps for a
.. i18n: newsletter subscription or as a hot prospect), or automatically using segmentation rules.

In the following sections you'll see how to assign partners to categories manually (perhaps for a
newsletter subscription or as a hot prospect), or automatically using segmentation rules.

.. i18n: Use the menu :menuselection:`Partners --> Configuration --> Categories --> Edit Categories` to
.. i18n: define a new category.

Use the menu :menuselection:`Partners --> Configuration --> Categories --> Edit Categories` to
define a new category.

.. i18n: To try Open ERP's partner capabilities described here for yourself, log into your
.. i18n: database as \ ``admin/XXXXX``\   then click :menuselection:`Partners -->
.. i18n: Configuration --> Categories --> Edit Categories` and create a new category of \ ``Small
.. i18n: Suppliers``\   whose parent is \ ``Suppliers``\  . Then create a new :guilabel:`Partner` whose :guilabel:`Name` is \
.. i18n: ``Susan Trent ``\  and category is \ ``Small Suppliers``\  .

To try Open ERP's partner capabilities described here for yourself, log into your
database as \ ``admin/XXXXX``\   then click :menuselection:`Partners -->
Configuration --> Categories --> Edit Categories` and create a new category of \ ``Small
Suppliers``\   whose parent is \ ``Suppliers``\  . Then create a new :guilabel:`Partner` whose :guilabel:`Name` is \
``Susan Trent ``\  and category is \ ``Small Suppliers``\  .

.. i18n: Click :menuselection:`Partners --> Partners by Category` and then click :menuselection:`Suppliers
.. i18n: --> Small Suppliers` to find just \ ``Susan Trent``\  . Do this again but now click the :guilabel:`Suppliers`
.. i18n: category in :guilabel:`Partners by Category` and you'll find that both \ ``Plumbing Component Suppliers``\
.. i18n: and \ ``Susan Trent``\   are in the higher-level category: \ ``Susan Trent``\  is there because
.. i18n: she's in a child category.

Click :menuselection:`Partners --> Partners by Category` and then click :menuselection:`Suppliers
--> Small Suppliers` to find just \ ``Susan Trent``\  . Do this again but now click the :guilabel:`Suppliers`
category in :guilabel:`Partners by Category` and you'll find that both \ ``Plumbing Component Suppliers``\
and \ ``Susan Trent``\   are in the higher-level category: \ ``Susan Trent``\  is there because
she's in a child category.

.. i18n: Add new contact \ ``Graham Strong``\   to \ ``Plumbing Component Suppliers``\  . Graham's
.. i18n: :guilabel:`Address Type` is \ ``Invoice``\  . Click :menuselection:`Partners --> Partner Contacts`
.. i18n: and see that both Susan and Graham appear on that list.

Add new contact \ ``Graham Strong``\   to \ ``Plumbing Component Suppliers``\  . Graham's
:guilabel:`Address Type` is \ ``Invoice``\  . Click :menuselection:`Partners --> Partner Contacts`
and see that both Susan and Graham appear on that list.

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
