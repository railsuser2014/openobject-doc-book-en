
.. i18n: Management of Carriers
.. i18n: ======================

Management of Carriers
======================

.. i18n: .. index::
.. i18n:    single: delivery grid
.. i18n:    single: carriers
.. i18n:    single: module; delivery
.. i18n:    single: module; profile_manfuacturing

.. index::
   single: delivery grid
   single: carriers
   single: module; delivery
   single: module; profile_manfuacturing

.. i18n: To manage deliveries in Open ERP, install the :mod:`delivery` module. (If you have installed the
.. i18n: :mod:`profile_manufacturing` profile this is installed by default during configuration of the database.) 
.. i18n: This module enables you to manage:

To manage deliveries in Open ERP, install the :mod:`delivery` module. (If you have installed the
:mod:`profile_manufacturing` profile this is installed by default during configuration of the database.) 
This module enables you to manage:

.. i18n: * the different carriers with whom you work,
.. i18n: 
.. i18n: * the different possible modes of transport,
.. i18n: 
.. i18n: * cost calculation and invoicing of each delivery,
.. i18n: 
.. i18n: * the modes of transport and their tariffs.

* the different carriers with whom you work,

* the different possible modes of transport,

* cost calculation and invoicing of each delivery,

* the modes of transport and their tariffs.

.. i18n: Once the :mod:`delivery` module has been installed, the first thing to do is to configure the different
.. i18n: modes of delivery accepted by your company. To do that use the menu :menuselection:`Stock Management
.. i18n: --> Configuration --> Delivery --> Delivery Method`.

Once the :mod:`delivery` module has been installed, the first thing to do is to configure the different
modes of delivery accepted by your company. To do that use the menu :menuselection:`Stock Management
--> Configuration --> Delivery --> Delivery Method`.

.. i18n: For each delivery mode, you should define the following elements:

For each delivery mode, you should define the following elements:

.. i18n: * Name of the delivery mode,
.. i18n: 
.. i18n: * The partner associated with the transport (which can be yourselves),
.. i18n: 
.. i18n: * The associated product.

* Name of the delivery mode,

* The partner associated with the transport (which can be yourselves),

* The associated product.

.. i18n: For example you can create the following modes:

For example you can create the following modes:

.. i18n: .. table:: Example Delivery Modes
.. i18n: 
.. i18n:    ================    ===========   ==========================
.. i18n:    Delivery Mode       Partner       Associated Product
.. i18n:    ================    ===========   ==========================
.. i18n:    Express Track       Mail Office   Express Track Delivery
.. i18n:    Priority Courier    Mail Office   Courier Express Delivery
.. i18n:    EFG Standard        EFG Inc       Delivery EFG
.. i18n:    EFG Express         EFG Inc       Delivery EFG Express
.. i18n:    ================    ===========   ==========================

.. table:: Example Delivery Modes

   ================    ===========   ==========================
   Delivery Mode       Partner       Associated Product
   ================    ===========   ==========================
   Express Track       Mail Office   Express Track Delivery
   Priority Courier    Mail Office   Courier Express Delivery
   EFG Standard        EFG Inc       Delivery EFG
   EFG Express         EFG Inc       Delivery EFG Express
   ================    ===========   ==========================

.. i18n: Information about the invoicing of transport (such as accounts, applicable taxes) are entered in the
.. i18n: product linked to the delivery mode. Ideally the product should be configured as 
.. i18n: :guilabel:`Product Type` ``Service`` and :guilabel:`Procure Method` ``Make to Stock``.

Information about the invoicing of transport (such as accounts, applicable taxes) are entered in the
product linked to the delivery mode. Ideally the product should be configured as 
:guilabel:`Product Type` ``Service`` and :guilabel:`Procure Method` ``Make to Stock``.

.. i18n: You can use the same product for several delivery modes. This simplifies the
.. i18n: configuration but you won't be able to separate out your sales figures by delivery mode.

You can use the same product for several delivery modes. This simplifies the
configuration but you won't be able to separate out your sales figures by delivery mode.

.. i18n: Tariff grids
.. i18n: ------------

Tariff grids
------------

.. i18n: Unlike ordinary products, delivery prices aren't given by pricelists but by delivery grids,
.. i18n: designed specifically for this purpose. For each delivery mode, you enter one or several tariff grids.
.. i18n: Each grid is used for a given region/destination.

Unlike ordinary products, delivery prices aren't given by pricelists but by delivery grids,
designed specifically for this purpose. For each delivery mode, you enter one or several tariff grids.
Each grid is used for a given region/destination.

.. i18n: For example, for the postal tariffs for Priority Courier, you generally define the three tariff grids
.. i18n: for Mail Office:

For example, for the postal tariffs for Priority Courier, you generally define the three tariff grids
for Mail Office:

.. i18n: * Courier National,
.. i18n: 
.. i18n: * Courier Europe,
.. i18n: 
.. i18n: * Courier Outside Europe.

* Courier National,

* Courier Europe,

* Courier Outside Europe.

.. i18n: To define a new delivery grid, use the menu :menuselection:`Stock Management --> Configuration -->
.. i18n: Deliveries --> Delivery Pricelist`. You then give a name to your delivery grid and define the
.. i18n: region for which the tariffs in the grid will be applicable. To do this, use the second tab
.. i18n: :guilabel:`Destination`. There you can set:

To define a new delivery grid, use the menu :menuselection:`Stock Management --> Configuration -->
Deliveries --> Delivery Pricelist`. You then give a name to your delivery grid and define the
region for which the tariffs in the grid will be applicable. To do this, use the second tab
:guilabel:`Destination`. There you can set:

.. i18n: * A list of countries (for UK or Europe, for example),
.. i18n: 
.. i18n: * A list of states,
.. i18n: 
.. i18n: * A range of post codes (for Paris you might have 75000 – 75900).

* A list of countries (for UK or Europe, for example),

* A list of states,

* A range of post codes (for Paris you might have 75000 – 75900).

.. i18n: You must then set the rules for calculating the price of transport in the first tab :guilabel:`Grid definition`.
.. i18n: A rule must first of all have a name. Then set the condition for which this rule is applicable, for
.. i18n: example ``Weight < 0.5kg``.

You must then set the rules for calculating the price of transport in the first tab :guilabel:`Grid definition`.
A rule must first of all have a name. Then set the condition for which this rule is applicable, for
example ``Weight < 0.5kg``.

.. i18n: .. note:: Weights
.. i18n: 
.. i18n:    Weights are expressed in kilograms. You can define a number with a decimal point or comma, so
.. i18n:    that to set 500g you'd put 0.5 in the weight rule.

.. note:: Weights

   Weights are expressed in kilograms. You can define a number with a decimal point or comma, so
   that to set 500g you'd put 0.5 in the weight rule.

.. i18n: Then set the sale price and the cost price. The price can be expressed in different ways:

Then set the sale price and the cost price. The price can be expressed in different ways:

.. i18n: * a fixed price,
.. i18n: 
.. i18n: * a variable price, as a function of weight, or volume, or weight x volume or price.

* a fixed price,

* a variable price, as a function of weight, or volume, or weight x volume or price.

.. i18n: For example, mailing within France using 2008 tariffs would be defined as shown in the table.

For example, mailing within France using 2008 tariffs would be defined as shown in the table.

.. i18n: .. table:: Example Tariff Rules
.. i18n: 
.. i18n:    ==========  =============  =====   =============
.. i18n:    Rule Title  Condition      Price   Type of Price
.. i18n:    ==========  =============  =====   =============
.. i18n:    S           Weight < 3 kg   6.9    Fixed
.. i18n:    M           Weight < 5 kg  7.82    Fixed
.. i18n:    L           Weight < 6 kg  8.53    Fixed
.. i18n:    XL          Weight < 7 kg  9.87    Fixed
.. i18n:    ==========  =============  =====   =============

.. table:: Example Tariff Rules

   ==========  =============  =====   =============
   Rule Title  Condition      Price   Type of Price
   ==========  =============  =====   =============
   S           Weight < 3 kg   6.9    Fixed
   M           Weight < 5 kg  7.82    Fixed
   L           Weight < 6 kg  8.53    Fixed
   XL          Weight < 7 kg  9.87    Fixed
   ==========  =============  =====   =============

.. i18n: You can also define rules that depend on the total amount on the order. For example to offer fixed price
.. i18n: delivery if the order is more than 150 USD, add the following rule:

You can also define rules that depend on the total amount on the order. For example to offer fixed price
delivery if the order is more than 150 USD, add the following rule:

.. i18n: .. table:: Additional Tariff Rule
.. i18n: 
.. i18n:    ================= ===============  ======   =============
.. i18n:    Rule Title        Condition        Price    Type of Price
.. i18n:    ================= ===============  ======   =============
.. i18n:    Franked > 150 USD Price > 150 USD   10      Fixed
.. i18n:    ================= ===============  ======   =============

.. table:: Additional Tariff Rule

   ================= ===============  ======   =============
   Rule Title        Condition        Price    Type of Price
   ================= ===============  ======   =============
   Franked > 150 USD Price > 150 USD   10      Fixed
   ================= ===============  ======   =============

.. i18n: Using delivery modes
.. i18n: --------------------

Using delivery modes
--------------------

.. i18n: Once the delivery modes and their tariffs have been defined you can use them in a Sales Order. 
.. i18n: There are two methods for doing that in Open ERP.

Once the delivery modes and their tariffs have been defined you can use them in a Sales Order. 
There are two methods for doing that in Open ERP.

.. i18n: * Delivery based on order quantities,
.. i18n: 
.. i18n: * Delivery based on deliverd quantities.

* Delivery based on order quantities,

* Delivery based on deliverd quantities.

.. i18n: Delivery based on order quantities
.. i18n: ----------------------------------

Delivery based on order quantities
----------------------------------

.. i18n: To add the delivery charges on the quotation, use the action :guilabel:`Delivery Costs` available to the right
.. i18n: of the form. A dialog box opens, asking you to select a delivery mode from one of the preconfigured available
.. i18n: ones.

To add the delivery charges on the quotation, use the action :guilabel:`Delivery Costs` available to the right
of the form. A dialog box opens, asking you to select a delivery mode from one of the preconfigured available
ones.

.. i18n: .. figure:: images/sale_delivery.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Adding a delivery charge to an order*

.. figure:: images/sale_delivery.png
   :scale: 75
   :align: center

   *Adding a delivery charge to an order*

.. i18n: Once the delivery mode has been selected, Open ERP automatically adds a line on the draft order with
.. i18n: the amount calculated by the delivery function. This technique enables you to calculate the
.. i18n: delivery charge based on the order and then, separately, how the products will really be delivered
.. i18n: to the customer.

Once the delivery mode has been selected, Open ERP automatically adds a line on the draft order with
the amount calculated by the delivery function. This technique enables you to calculate the
delivery charge based on the order and then, separately, how the products will really be delivered
to the customer.

.. i18n: If you want to calculate the exact delivery charges depending on the actual deliveries you must use
.. i18n: invoicing based on deliveries.

If you want to calculate the exact delivery charges depending on the actual deliveries you must use
invoicing based on deliveries.

.. i18n: Delivery based on the packed items
.. i18n: ----------------------------------

Delivery based on the packed items
----------------------------------

.. i18n: To invoice the delivery on the basis of items packed you set the delivery mode in the
.. i18n: :guilabel:`Delivery method` field on the second tab of the order, :guilabel:`Other data`. 
.. i18n: Don't add delivery lines to the Sales Order but to the Invoices after they have been
.. i18n: generated for the delivered items.

To invoice the delivery on the basis of items packed you set the delivery mode in the
:guilabel:`Delivery method` field on the second tab of the order, :guilabel:`Other data`. 
Don't add delivery lines to the Sales Order but to the Invoices after they have been
generated for the delivered items.

.. i18n: For this to work properly, your order must be set to the state 
.. i18n: :guilabel:`Invoice from the Packing`.
.. i18n: You can then confirm the order and validate the delivery.

For this to work properly, your order must be set to the state 
:guilabel:`Invoice from the Packing`.
You can then confirm the order and validate the delivery.

.. i18n: When the manager has generated the invoices corresponding to the deliveries carried out,
.. i18n: Open ERP automatically adds a line on each invoice corresponding to the delivery charge, calculated
.. i18n: on the basis of the items actually sent.

When the manager has generated the invoices corresponding to the deliveries carried out,
Open ERP automatically adds a line on each invoice corresponding to the delivery charge, calculated
on the basis of the items actually sent.

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
