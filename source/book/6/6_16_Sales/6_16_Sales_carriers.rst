
Management of Carriers
======================

.. index::
   single: delivery grid
   single: carriers
   single: module; delivery
   single: module; profile_manfuacturing

To manage deliveries in Open ERP, install the :mod:`delivery` module. (If you have installed the
:mod:`profile_manufacturing` profile this is installed by default during configuration of the database.) 
This module enables you to manage:

* the different carriers with whom you work,

* the different possible modes of transport,

* cost calculation and invoicing of each delivery,

* the modes of transport and their tariffs.

Once the :mod:`delivery` module has been installed, the first thing to do is to configure the different
modes of delivery accepted by your company. To do that use the menu :menuselection:`Stock Management
--> Configuration --> Delivery --> Delivery Method`.

For each delivery mode, you should define the following elements:

* Name of the delivery mode,

* The partner associated with the transport (which can be yourselves),

* The associated product.

For example you can create the following modes:

.. table:: Example Delivery Modes

================    ===========   ==========================
Delivery Mode       Partner       Associated Product
================    ===========   ==========================
Express Track       Mail Office   Express Track Delivery
Priority Courier    Mail Office   Courier Express Delivery
EFG Standard        EFG Inc       Delivery EFG
EFG Express         EFG Inc       Delivery EFG Express
================    ===========   ==========================

Information about the invoicing of transport (such as accounts, applicable taxes) are entered in the
product linked to the delivery mode. Ideally the product should be configured as 
:guilabel:`Product Type` ``Service`` and :guilabel:`Procure Method` ``Make to Stock``.

You can use the same product for several delivery modes. This simplifies the
configuration but you won't be able to separate out your sales figures by delivery mode.

Tariff grids
------------

Unlike ordinary products, delivery prices aren't given by pricelists but by delivery grids,
designed specifically for this purpose. For each delivery mode, you enter one or several tariff grids.
Each grid is used for a given region/destination.

For example, for the postal tariffs for Priority Courier, you generally define the three tariff grids
for Mail Office:

* Courier National,

* Courier Europe,

* Courier Outside Europe.

To define a new delivery grid, use the menu :menuselection:`Stock Management --> Configuration -->
Deliveries --> Delivery Pricelist`. You then give a name to your delivery grid and define the
region for which the tariffs in the grid will be applicable. To do this, use the second tab
:guilabel:`Destination`. There you can set:

* A list of countries (for UK or Europe, for example),

* A list of states,

* A range of post codes (for Paris you might have 75000 – 75900).

You must then set the rules for calculating the price of transport in the first tab :guilabel:`Grid definition`.
A rule must first of all have a name. Then set the condition for which this rule is applicable, for
example ``Weight < 0.5kg``.

.. note:: Weights

   Weights are expressed in kilograms. You can define a number with a decimal point or comma, so
   that to set 500g you'd put 0.5 in the weight rule.

Then set the sale price and the cost price. The price can be expressed in different ways:

* a fixed price,

* a variable price, as a function of weight, or volume, or weight x volume or price.

For example, the rules for defining

.. table:: *Example Tariff Rules*

==========  =============  =====   =============
Rule Title  Condition      Price   Type of Price
==========  =============  =====   =============
S           Weight < 3 kg   6.9    Fixed
M           Weight < 5 kg  7.82    Fixed
L           Weight < 6 kg  8.53    Fixed
XL          Weight < 7 kg  9.87    Fixed
==========  =============  =====   =============

You can also define rules that depend on the total amount on the order. For example to offer fixed price
delivery if the order is more than 150 USD, add the following rule:

.. table:: *Additional Tariff Rule*

================= ===============  ======   =============
Rule Title        Condition        Price    Type of Price
================= ===============  ======   =============
Franked > 150 USD Price > 150 USD   10      Fixed
================= ===============  ======   =============

Using delivery modes
--------------------

Once the delivery modes and their tariffs have been defined you can use them in a Sales Order. 
There are two methods for doing that in Open ERP.

* Delivery based on order quantities,

* Delivery based on deliverd quantities.

Delivery based on order quantities
----------------------------------

To add the delivery charges on the quotation, use the action :guilabel:`Delivery Costs` available to the right
of the form. A dialog box opens, asking you to select a delivery mode from one of the preconfigured available
ones.

.. figure:: images/sale_delivery.png
   :scale: 75
   :align: center

   *Adding a delivery charge to an order*

Once the delivery mode has been selected, Open ERP automatically adds a line on the draft order with
the amount calculated by the delivery function. This technique enables you to calculate the
delivery charge based on the order and then, separately, how the products will really be delivered
to the customer.

If you want to calculate the exact delivery charges depending on the actual deliveries you must use
invoicing based on deliveries.

Delivery based on the packed items
----------------------------------

To invoice the delivery on the basis of items packed you set the delivery mode in the
:guilabel:`Delivery method` field on the second tab of the order, :guilabel:`Other data`. 
Don't add delivery lines to the Sales Order but to the Invoices after they have been
generated for the delivered items.

For this to work properly, your order must be set to the state 
:guilabel:`Invoice from the Packing`.
You can then confirm the order and validate the delivery.

When the manager has generated the invoices corresponding to the deliveries carried out,
Open ERP automatically adds a line on each invoice corresponding to the delivery charge, calculated
on the basis of the items actually sent.

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
