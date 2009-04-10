
.. i18n: Price management policies
.. i18n: =========================

Price management policies
=========================

.. i18n: Some companies are notorious for their complicated pricelists. Many forms of price variation are
.. i18n: used, such as end-of-year refunds, discounts, changes of terms and conditions with time, various
.. i18n: prepayments, cascaded rebates, seasonal promotions, and progressive price reductions.

Some companies are notorious for their complicated pricelists. Many forms of price variation are
used, such as end-of-year refunds, discounts, changes of terms and conditions with time, various
prepayments, cascaded rebates, seasonal promotions, and progressive price reductions.

.. i18n: .. note:: Rebate, Refund, Reduction
.. i18n: 
.. i18n:    In some accounting jurisdictions you have to differentiate between the three following terms:
.. i18n: 
.. i18n:    * Rebate: reimbursement to the client, usually at the end of the year, that depends on the
.. i18n:      quantity of goods purchased over a period.
.. i18n: 
.. i18n:    * Refund: reduction on the order line or invoice line if a certain quantity of goods is purchased
.. i18n:      at one time or is sold in a framework of a promotional activity.
.. i18n: 
.. i18n:    * Reduction: A one-off reduction resulting from a quality defect or a variation in a product's
.. i18n:      conformance to a specification.

.. note:: Rebate, Refund, Reduction

   In some accounting jurisdictions you have to differentiate between the three following terms:

   * Rebate: reimbursement to the client, usually at the end of the year, that depends on the
     quantity of goods purchased over a period.

   * Refund: reduction on the order line or invoice line if a certain quantity of goods is purchased
     at one time or is sold in a framework of a promotional activity.

   * Reduction: A one-off reduction resulting from a quality defect or a variation in a product's
     conformance to a specification.

.. i18n: Intelligent price management is difficult, because it requires you to integrate several conditions
.. i18n: from clients and suppliers to create estimates quickly or to invoice automatically. But if you have
.. i18n: an efficient price management mechanism you can often keep margins raised and respond quickly to
.. i18n: changes in market conditions. A good price management system gives you scope for varying any and all
.. i18n: of the relevant factors when you're negotiating a contract.

Intelligent price management is difficult, because it requires you to integrate several conditions
from clients and suppliers to create estimates quickly or to invoice automatically. But if you have
an efficient price management mechanism you can often keep margins raised and respond quickly to
changes in market conditions. A good price management system gives you scope for varying any and all
of the relevant factors when you're negotiating a contract.

.. i18n: To help you work most effectively, Open ERP's pricelist principles are extremely powerful yet are
.. i18n: based on simple and generic rules. You can develop both sales pricelists and purchase pricelists for
.. i18n: products capable of accommodating conditions such as the date period, the quantity requested and the
.. i18n: type of product.

To help you work most effectively, Open ERP's pricelist principles are extremely powerful yet are
based on simple and generic rules. You can develop both sales pricelists and purchase pricelists for
products capable of accommodating conditions such as the date period, the quantity requested and the
type of product.

.. i18n: .. tip:: Don't confuse the different price specifications
.. i18n: 
.. i18n:    Don't confuse the sale price with the base price of the product.
.. i18n:    In Open ERP's basic configuration the sale price is the list price set on the product form
.. i18n:    but a customer can be given a different sale price depending on the conditions.

.. tip:: Don't confuse the different price specifications

   Don't confuse the sale price with the base price of the product.
   In Open ERP's basic configuration the sale price is the list price set on the product form
   but a customer can be given a different sale price depending on the conditions.

.. i18n: It's the same for purchase price and standard cost. Purchase price is your suppliers' selling price,
.. i18n: which changes in response to different criteria such as quantities, dates, and supplier. This is
.. i18n: automatically set by the accounting system. You'll find that the two prices have been set by default to the
.. i18n: same for all products with the demonstration data, which can be a source of confusion.
.. i18n: You're free to set the standard cost to something different.

It's the same for purchase price and standard cost. Purchase price is your suppliers' selling price,
which changes in response to different criteria such as quantities, dates, and supplier. This is
automatically set by the accounting system. You'll find that the two prices have been set by default to the
same for all products with the demonstration data, which can be a source of confusion.
You're free to set the standard cost to something different.

.. i18n: Each pricelist is calculated from defined policies, so you'll have as many sales pricelists as
.. i18n: active sales policies in the company. For example a company that sells products through three sales
.. i18n: channels could create the following price lists:

Each pricelist is calculated from defined policies, so you'll have as many sales pricelists as
active sales policies in the company. For example a company that sells products through three sales
channels could create the following price lists:

.. i18n:  #. Main distribution:
.. i18n: 
.. i18n: 	- pricelist for Walbury,
.. i18n: 
.. i18n: 	- pricelist for TesMart,
.. i18n: 
.. i18n:  #. Postal Sales.
.. i18n: 
.. i18n:  #. Walk-in customers.

 #. Main distribution:

	- pricelist for Walbury,

	- pricelist for TesMart,

 #. Postal Sales.

 #. Walk-in customers.

.. i18n: A single pricelist can exist in several versions, only one of which is permitted to be active at a
.. i18n: given time. These versions let you set different prices at different points in time. So the
.. i18n: pricelist for walk-in customers could have five different versions, for example: \ ``Autumn``\,  \
.. i18n: ``Summer``\, \ ``Summer Sales``\, \ ``Winter``\, \ ``Spring``\. Direct customers will see prices
.. i18n: that change with the seasons.

A single pricelist can exist in several versions, only one of which is permitted to be active at a
given time. These versions let you set different prices at different points in time. So the
pricelist for walk-in customers could have five different versions, for example: \ ``Autumn``\,  \
``Summer``\, \ ``Summer Sales``\, \ ``Winter``\, \ ``Spring``\. Direct customers will see prices
that change with the seasons.

.. i18n: Each pricelist is expressed in a single currency. If your company sells products in several
.. i18n: currencies you'll have to create as many pricelists as you have currencies.

Each pricelist is expressed in a single currency. If your company sells products in several
currencies you'll have to create as many pricelists as you have currencies.

.. i18n: The prices on a pricelist can depend on another list, which means that you don't have to repeat the
.. i18n: definition of all conditions for each product. So a pricelist in USD can be based on a pricelist in
.. i18n: EUR. If the currency conversion rates between EUR and USD change, or the EUR prices change, the USD
.. i18n: rates can be **automatically** adjusted.

The prices on a pricelist can depend on another list, which means that you don't have to repeat the
definition of all conditions for each product. So a pricelist in USD can be based on a pricelist in
EUR. If the currency conversion rates between EUR and USD change, or the EUR prices change, the USD
rates can be **automatically** adjusted.

.. i18n: .. index::
.. i18n:    single: pricelist; create

.. index::
   single: pricelist; create

.. i18n: Creating pricelists
.. i18n: -------------------

Creating pricelists
-------------------

.. i18n: To define a pricelist use the menu :menuselection:`Products --> Pricelists --> Pricelists` .

To define a pricelist use the menu :menuselection:`Products --> Pricelists --> Pricelists` .

.. i18n: For each list you should define:

For each list you should define:

.. i18n: * a :guilabel:`Name` for the list,
.. i18n: 
.. i18n: * a :guilabel:`Type` of list: \ ``Sale``\   for customers or \ ``Purchase``\   for suppliers,
.. i18n: 
.. i18n: * the :guilabel:`Currency` in which the prices are expressed.

* a :guilabel:`Name` for the list,

* a :guilabel:`Type` of list: \ ``Sale``\   for customers or \ ``Purchase``\   for suppliers,

* the :guilabel:`Currency` in which the prices are expressed.

.. i18n: .. index::
.. i18n:    single: module; edi

.. index::
   single: module; edi

.. i18n: .. tip:: Customer Price
.. i18n: 
.. i18n:    If you install the module :mod:`edi` (in ``addons-extra`` at the time of writing)
.. i18n:    a third type of list appears – the :guilabel:`Customer Price` - which
.. i18n:    defines the price displayed for the end user.
.. i18n:    This doesn't have to be the same as your selling price to an intermediary or distributor.

.. tip:: Customer Price

   If you install the module :mod:`edi` (in ``addons-extra`` at the time of writing)
   a third type of list appears – the :guilabel:`Customer Price` - which
   defines the price displayed for the end user.
   This doesn't have to be the same as your selling price to an intermediary or distributor.

.. i18n: .. index::
.. i18n:    single: pricelists; version

.. index::
   single: pricelists; version

.. i18n: Pricelist versions
.. i18n: ^^^^^^^^^^^^^^^^^^

Pricelist versions
^^^^^^^^^^^^^^^^^^

.. i18n: Once the list is defined you must provide it with at least one version. To do that use the menu
.. i18n: :menuselection:`Products --> Pricelists --> Pricelist Versions`. The version contains all of the
.. i18n: rules that enable you to calculate a price for a product and a given quantity.

Once the list is defined you must provide it with at least one version. To do that use the menu
:menuselection:`Products --> Pricelists --> Pricelist Versions`. The version contains all of the
rules that enable you to calculate a price for a product and a given quantity.

.. i18n: So set the :guilabel:`Name` of this associated version. If the list only has a single version you
.. i18n: can use the same name for the pricelist and the version. In the :guilabel:`Pricelist` field select
.. i18n: the pricelist you created.

So set the :guilabel:`Name` of this associated version. If the list only has a single version you
can use the same name for the pricelist and the version. In the :guilabel:`Pricelist` field select
the pricelist you created.

.. i18n: Then set the :guilabel:`Start date` and :guilabel:`End date` of this version. The fields are both
.. i18n: optional: if you don't set any dates the version will be permanently active. Only one version
.. i18n: may be active at any one point, so bear this in mind when creating them.
.. i18n: Use the :guilabel:`Active` field in the versions to activate or disable a pricelist version.

Then set the :guilabel:`Start date` and :guilabel:`End date` of this version. The fields are both
optional: if you don't set any dates the version will be permanently active. Only one version
may be active at any one point, so bear this in mind when creating them.
Use the :guilabel:`Active` field in the versions to activate or disable a pricelist version.

.. i18n: .. note:: Automatically updating the sale pricelist
.. i18n: 
.. i18n:    You can make any sale pricelist depend on one of the other pricelists.
.. i18n:    So you could make your sale pricelist depend on your supplier's purchase pricelist, to
.. i18n:    which you add a margin.
.. i18n:    The prices are automatically calculated as a function of the purchase price and need no further
.. i18n:    manual adjustment.

.. note:: Automatically updating the sale pricelist

   You can make any sale pricelist depend on one of the other pricelists.
   So you could make your sale pricelist depend on your supplier's purchase pricelist, to
   which you add a margin.
   The prices are automatically calculated as a function of the purchase price and need no further
   manual adjustment.

.. i18n: .. index:: price

.. index:: price

.. i18n: Rules for calculating price
.. i18n: ^^^^^^^^^^^^^^^^^^^^^^^^^^^

Rules for calculating price
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. i18n: A pricelist version is made up of a set of rules that apply to the product base prices.

A pricelist version is made up of a set of rules that apply to the product base prices.

.. i18n: .. figure:: images/service_pricelist_line.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Detail of a rule in a pricelist version*

.. figure:: images/service_pricelist_line.png
   :scale: 75
   :align: center

   *Detail of a rule in a pricelist version*

.. i18n: You define the conditions for a rule in the first part of the definition screen labeled :guilabel:`Rules Test
.. i18n: Match`. The rule applies to the :guilabel:`Product` or :guilabel:`Product Template` and/or the named :guilabel:`Product
.. i18n: Category`. If a rule is applied to a category then it is automatically applied to all of its
.. i18n: subcategories too (using the tree structure for product categories).

You define the conditions for a rule in the first part of the definition screen labeled :guilabel:`Rules Test
Match`. The rule applies to the :guilabel:`Product` or :guilabel:`Product Template` and/or the named :guilabel:`Product
Category`. If a rule is applied to a category then it is automatically applied to all of its
subcategories too (using the tree structure for product categories).

.. i18n: If you set a minimum quantity in :guilabel:`Min. Quantity` the rule will only apply to a quantity the same
.. i18n: as or larger than that set. This lets you set reduced rates in steps that depend on the quantities ordered.

If you set a minimum quantity in :guilabel:`Min. Quantity` the rule will only apply to a quantity the same
as or larger than that set. This lets you set reduced rates in steps that depend on the quantities ordered.

.. i18n: Several rules can be applied to an order. Open ERP evaluates these rules in sequence to select
.. i18n: which to apply to the specified price calculation. If several rules are valid only the first in
.. i18n: sequence is used for the calculation. The :guilabel:`Sequence` field determines the order, starting with the
.. i18n: lowest number and working up.

Several rules can be applied to an order. Open ERP evaluates these rules in sequence to select
which to apply to the specified price calculation. If several rules are valid only the first in
sequence is used for the calculation. The :guilabel:`Sequence` field determines the order, starting with the
lowest number and working up.

.. i18n: Once a rule has been selected, the system has to determine how to calculate the price from the rule.
.. i18n: This operation is based on the criteria set out in the lower part of the form, labeled :guilabel:`Price
.. i18n: Computation`.

Once a rule has been selected, the system has to determine how to calculate the price from the rule.
This operation is based on the criteria set out in the lower part of the form, labeled :guilabel:`Price
Computation`.

.. i18n: The first field you have to complete is labeled :guilabel:`Based on`. Set the mode for
.. i18n: partner price calculation, choosing between:

The first field you have to complete is labeled :guilabel:`Based on`. Set the mode for
partner price calculation, choosing between:

.. i18n: * the :guilabel:`List Price` set in the product file,
.. i18n: 
.. i18n: * the :guilabel:`Standard Cost` set in the product file,
.. i18n: 
.. i18n: * an :guilabel:`Other Pricelist` given in the field :guilabel:`If Other Pricelist`,
.. i18n: 
.. i18n: * the price that varies as a function of a supplier defined in the :guilabel:`Partner section of the
.. i18n:   product form`.

* the :guilabel:`List Price` set in the product file,

* the :guilabel:`Standard Cost` set in the product file,

* an :guilabel:`Other Pricelist` given in the field :guilabel:`If Other Pricelist`,

* the price that varies as a function of a supplier defined in the :guilabel:`Partner section of the
  product form`.

.. i18n: Several other criteria can be considered and added to the list, as you'll see in the following
.. i18n: section.

Several other criteria can be considered and added to the list, as you'll see in the following
section.

.. i18n: Next, various operations can be applied to the base price to calculate the sales or purchase price
.. i18n: for the partner at the specified quantities. To calculate it you apply the formula shown on the
.. i18n: form: ``Price = Base Price x (1 – Field1) + Field2`` .

Next, various operations can be applied to the base price to calculate the sales or purchase price
for the partner at the specified quantities. To calculate it you apply the formula shown on the
form: ``Price = Base Price x (1 – Field1) + Field2`` .

.. i18n: The first field, :guilabel:`Field1`, defines a discount. Set it to 0.20 for a discount of 20% from
.. i18n: the base price. If your price is based on standard cost, you can set -0.15 to get a 15% price uplift
.. i18n: compared with the standard costs.

The first field, :guilabel:`Field1`, defines a discount. Set it to 0.20 for a discount of 20% from
the base price. If your price is based on standard cost, you can set -0.15 to get a 15% price uplift
compared with the standard costs.

.. i18n: :guilabel:`Field2` sets a fixed supplement to the price, expressed in the currency of the pricelist.
.. i18n: This amount is just added (or subtracted, if negative) to the amount calculated with the
.. i18n: :guilabel:`Field1` discount.

:guilabel:`Field2` sets a fixed supplement to the price, expressed in the currency of the pricelist.
This amount is just added (or subtracted, if negative) to the amount calculated with the
:guilabel:`Field1` discount.

.. i18n: Then you can specify a rounding method. The rounding calculation is carried out to the nearest
.. i18n: number. For example if you set 0.05 in this example, a price of 45.66 will be rounded to 45.65, and
.. i18n: 14,567 rounded to 100 will give a price of 14,600.

Then you can specify a rounding method. The rounding calculation is carried out to the nearest
number. For example if you set 0.05 in this example, a price of 45.66 will be rounded to 45.65, and
14,567 rounded to 100 will give a price of 14,600.

.. i18n: .. note:: Swiss special situation
.. i18n: 
.. i18n:    In Switzerland, the smallest monetary unit is 5 cents.
.. i18n:    There aren't any 1 or 2 cent coins.
.. i18n:    So you set Open ERP's rounding to 0.05 to round everything in a Swiss franc pricelist.

.. note:: Swiss special situation

   In Switzerland, the smallest monetary unit is 5 cents.
   There aren't any 1 or 2 cent coins.
   So you set Open ERP's rounding to 0.05 to round everything in a Swiss franc pricelist.

.. i18n: The supplement from :guilabel:`Field2` is applied before the rounding calculation, which enables
.. i18n: some interesting effects. For example if you want all your prices to end in 9.99, set your rounding
.. i18n: to 10 and your supplement to -0.01 in :guilabel:`Field2`.

The supplement from :guilabel:`Field2` is applied before the rounding calculation, which enables
some interesting effects. For example if you want all your prices to end in 9.99, set your rounding
to 10 and your supplement to -0.01 in :guilabel:`Field2`.

.. i18n: Minimum and Maximum margins enable you to guarantee a given margin over the base price. A margin of
.. i18n: 10 USD enables you to stop the discount from returning less than that margin. If you put 0 into this
.. i18n: field, no effect is taken into account.

Minimum and Maximum margins enable you to guarantee a given margin over the base price. A margin of
10 USD enables you to stop the discount from returning less than that margin. If you put 0 into this
field, no effect is taken into account.

.. i18n: Once the pricelist is defined you can assign it to a partner. To do this, find a Partner and select
.. i18n: its :guilabel:`Properties` tab. You can then change the :guilabel:`Purchase Pricelist` and the
.. i18n: :guilabel:`Sale Pricelist` that's loaded by default for the partner.

Once the pricelist is defined you can assign it to a partner. To do this, find a Partner and select
its :guilabel:`Properties` tab. You can then change the :guilabel:`Purchase Pricelist` and the
:guilabel:`Sale Pricelist` that's loaded by default for the partner.

.. i18n: Case of using pricelists
.. i18n: ------------------------

Case of using pricelists
------------------------

.. i18n: Take the case of an IT systems trading company, for which the following product categories have
.. i18n: been configured:

Take the case of an IT systems trading company, for which the following product categories have
been configured:

.. i18n: All products

All products

.. i18n:  #. Accessories
.. i18n: 
.. i18n:                 * Printers
.. i18n: 
.. i18n:                 * Scanners
.. i18n: 
.. i18n:                 * Keyboards and Mice
.. i18n: 
.. i18n:  #. Computers
.. i18n: 
.. i18n:                 * Portables
.. i18n: 
.. i18n:                  - Large-screen portables
.. i18n: 
.. i18n:                 * Computers
.. i18n: 
.. i18n:                  - Office Computers
.. i18n: 
.. i18n:                  - Professional Computers

 #. Accessories

                * Printers

                * Scanners

                * Keyboards and Mice

 #. Computers

                * Portables

                 - Large-screen portables

                * Computers

                 - Office Computers

                 - Professional Computers

.. i18n: In addition, the products presented in the table below are defined in the currency of the installed
.. i18n: chart of accounts.

In addition, the products presented in the table below are defined in the currency of the installed
chart of accounts.

.. i18n: TABLE

TABLE

.. i18n: .. csv-table:: Examples of products with their different prices
.. i18n: 
.. i18n:    "Product ","List Price","Standard Price","Default supplier price",
.. i18n:    "Acclo Portable","1,200 ","887 ","893 ",
.. i18n:    "Toshibishi Portable","1,340 ","920 ","920 ",
.. i18n:    "Berrel Keyboard","100 ","50 ","50 ",
.. i18n:    "Office Computer","1,400 ","1,000 ","1,000 ",

.. csv-table:: Examples of products with their different prices

   "Product ","List Price","Standard Price","Default supplier price",
   "Acclo Portable","1,200 ","887 ","893 ",
   "Toshibishi Portable","1,340 ","920 ","920 ",
   "Berrel Keyboard","100 ","50 ","50 ",
   "Office Computer","1,400 ","1,000 ","1,000 ",

.. i18n: .. index::
.. i18n:    single: pricelist; default pricelist

.. index::
   single: pricelist; default pricelist

.. i18n: Default pricelists
.. i18n: ^^^^^^^^^^^^^^^^^^

Default pricelists
^^^^^^^^^^^^^^^^^^

.. i18n: .. figure:: images/product_pricelist_default.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Default pricelist after installing Open ERP*

.. figure:: images/product_pricelist_default.png
   :scale: 75
   :align: center

   *Default pricelist after installing Open ERP*

.. i18n: When you install the software two pricelists are created by default: one for sales and one for
.. i18n: purchases. These each contain only one pricelist version and only one line in that version.

When you install the software two pricelists are created by default: one for sales and one for
purchases. These each contain only one pricelist version and only one line in that version.

.. i18n: The price for sales defined in the Default Public Pricelist is set by default to
.. i18n: the Public Price of the product in the product file, which is the Sale Price in the Product file.

The price for sales defined in the Default Public Pricelist is set by default to
the Public Price of the product in the product file, which is the Sale Price in the Product file.

.. i18n: The price for purchases defined in the Default Purchase Pricelist is set by default in the same way to
.. i18n: the Standard Cost of the product in the product file.

The price for purchases defined in the Default Purchase Pricelist is set by default in the same way to
the Standard Cost of the product in the product file.

.. i18n: .. index::
.. i18n:    single: trading company

.. index::
   single: trading company

.. i18n: Example of a trading company
.. i18n: ^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Example of a trading company
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. i18n: Take the case of a trading company, where the sale price for resellers can be defined like this:

Take the case of a trading company, where the sale price for resellers can be defined like this:

.. i18n: * For portable computers, the sale price is calculated from the list price of the supplier Acclo,
.. i18n:   with a supplement of 23% on the cost of purchase.
.. i18n: 
.. i18n: * For all other products the sale price is given by the standard cost in the product file, on which
.. i18n:   31% is added. The price must end in ``.99`` .
.. i18n: 
.. i18n: * The sale price of Berrel keyboards is fixed at 60 for a minimum quantity of 5 keyboards purchased.
.. i18n:   Otherwise it uses the rule above.
.. i18n: 
.. i18n: * Assume that the Acclo pricelist is defined in Open ERP. The pricelist for resellers and the
.. i18n:   pricelist version then contains three lines:
.. i18n: 
.. i18n:        #. \ ``Acclo``\  line:
.. i18n: 
.. i18n:                 *  :guilabel:`Product Category` : \ ``Portables``\  ,
.. i18n: 
.. i18n:                 *  :guilabel:`Based on` : \ ``Other pricelist``\  ,
.. i18n: 
.. i18n:                 *  :guilabel:`Pricelist if other` : \ ``Acclo pricelist``\  ,
.. i18n: 
.. i18n:                 *  :guilabel:`Field1` : \ ``-0.23``\  ,
.. i18n: 
.. i18n:                 *  :guilabel:`Priority` : \ ``1``\  .
.. i18n: 
.. i18n:        #. \ ``Berrel Keyboard``\  line:
.. i18n: 
.. i18n:                 *  :guilabel:`Product Template` : \ ``Berrel Keyboard``\  ,
.. i18n: 
.. i18n:                 *  :guilabel:`Min. Quantity` : \ ``5``\  ,
.. i18n: 
.. i18n:                 *  :guilabel:`Field1` : \ ``1.0``\  ,
.. i18n: 
.. i18n:                 *  :guilabel:`Field2` : \ ``60``\  ,
.. i18n: 
.. i18n:                 *  :guilabel:`Priority` : \ ``2``\  .
.. i18n: 
.. i18n:        #. \ ``Other products``\  line:
.. i18n: 
.. i18n:                 *  :guilabel:`Based on:` \ ``Standard Price``\  ,
.. i18n: 
.. i18n:                 *  :guilabel:`Field1` : \ ``-0.31``\  ,
.. i18n: 
.. i18n:                 *  :guilabel:`Field2` : \ ``-0.01``\  ,
.. i18n: 
.. i18n:                 *  :guilabel:`Rounding` : \ ``1.0``\  .
.. i18n: 
.. i18n:                 *  :guilabel:`Priority` :  \ ``3``\ .

* For portable computers, the sale price is calculated from the list price of the supplier Acclo,
  with a supplement of 23% on the cost of purchase.

* For all other products the sale price is given by the standard cost in the product file, on which
  31% is added. The price must end in ``.99`` .

* The sale price of Berrel keyboards is fixed at 60 for a minimum quantity of 5 keyboards purchased.
  Otherwise it uses the rule above.

* Assume that the Acclo pricelist is defined in Open ERP. The pricelist for resellers and the
  pricelist version then contains three lines:

       #. \ ``Acclo``\  line:

                *  :guilabel:`Product Category` : \ ``Portables``\  ,

                *  :guilabel:`Based on` : \ ``Other pricelist``\  ,

                *  :guilabel:`Pricelist if other` : \ ``Acclo pricelist``\  ,

                *  :guilabel:`Field1` : \ ``-0.23``\  ,

                *  :guilabel:`Priority` : \ ``1``\  .

       #. \ ``Berrel Keyboard``\  line:

                *  :guilabel:`Product Template` : \ ``Berrel Keyboard``\  ,

                *  :guilabel:`Min. Quantity` : \ ``5``\  ,

                *  :guilabel:`Field1` : \ ``1.0``\  ,

                *  :guilabel:`Field2` : \ ``60``\  ,

                *  :guilabel:`Priority` : \ ``2``\  .

       #. \ ``Other products``\  line:

                *  :guilabel:`Based on:` \ ``Standard Price``\  ,

                *  :guilabel:`Field1` : \ ``-0.31``\  ,

                *  :guilabel:`Field2` : \ ``-0.01``\  ,

                *  :guilabel:`Rounding` : \ ``1.0``\  .

                *  :guilabel:`Priority` :  \ ``3``\ .

.. i18n: It's important that the priority of the second rule is set below the priority of the third in this
.. i18n: example. If it were the other way round the third rule would always be applied because a quantity of
.. i18n: 5 is always greater than a quantity of 1 for all products.

It's important that the priority of the second rule is set below the priority of the third in this
example. If it were the other way round the third rule would always be applied because a quantity of
5 is always greater than a quantity of 1 for all products.

.. i18n: Also note that to fix a price of 60 for the 5 Berrel Keyboards, the formula \ ``Price = Base Price x
.. i18n: (1 – 1.0) + 60``\   has been used.

Also note that to fix a price of 60 for the 5 Berrel Keyboards, the formula \ ``Price = Base Price x
(1 – 1.0) + 60``\   has been used.

.. i18n: Establishing customer contract conditions
.. i18n: ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Establishing customer contract conditions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. i18n: The trading company can now set specific conditions to a customer, such as the company TinAtwo, who
.. i18n: might have signed a valid contract with the following conditions:

The trading company can now set specific conditions to a customer, such as the company TinAtwo, who
might have signed a valid contract with the following conditions:

.. i18n: * For Toshibishi portables, TinAtwo benefits from a discount of 5% of resale price.
.. i18n: 
.. i18n: * For all other products, the resale conditions are unchanged.

* For Toshibishi portables, TinAtwo benefits from a discount of 5% of resale price.

* For all other products, the resale conditions are unchanged.

.. i18n: The list price for TinAtwo, called ``TinAtwo contract`` , contains two rules:

The list price for TinAtwo, called ``TinAtwo contract`` , contains two rules:

.. i18n:        #. \ ``Toshibishi portable``\  :
.. i18n: 
.. i18n:                 *  :guilabel:`Product` : \ ``Toshibishi Portable``\  ,
.. i18n: 
.. i18n:                 *  :guilabel:`Based on` : \ ``Other pricelist``\  ,
.. i18n: 
.. i18n:                 *  :guilabel:`Pricelist if other` : \ ``Reseller pricelist``\  ,
.. i18n: 
.. i18n:                 *  :guilabel:`Field1` : \ ``0.05``\  ,
.. i18n: 
.. i18n:                 *  :guilabel:`Priority` : \ ``1``\  .
.. i18n: 
.. i18n:        #. \ ``Other Products``\ :
.. i18n: 
.. i18n:                 *  :guilabel:`Product` :
.. i18n: 
.. i18n:                 *  :guilabel:`Based on` : \ ``Other pricelist``\  ,
.. i18n: 
.. i18n:                 *  :guilabel:`Pricelist if other` : \ ``Reseller pricelist``\  ,
.. i18n: 
.. i18n:                 *  :guilabel:`Priority` : \ ``2``\  .

       #. \ ``Toshibishi portable``\  :

                *  :guilabel:`Product` : \ ``Toshibishi Portable``\  ,

                *  :guilabel:`Based on` : \ ``Other pricelist``\  ,

                *  :guilabel:`Pricelist if other` : \ ``Reseller pricelist``\  ,

                *  :guilabel:`Field1` : \ ``0.05``\  ,

                *  :guilabel:`Priority` : \ ``1``\  .

       #. \ ``Other Products``\ :

                *  :guilabel:`Product` :

                *  :guilabel:`Based on` : \ ``Other pricelist``\  ,

                *  :guilabel:`Pricelist if other` : \ ``Reseller pricelist``\  ,

                *  :guilabel:`Priority` : \ ``2``\  .

.. i18n: Once this list has been entered you should look for the partner form for TinAtwo again. Click the
.. i18n: :guilabel:`Properties` tab to set the :guilabel:`Sale List Price` field to *TinAtwo Contract*. If
.. i18n: the contract is only valid for one year, don't forget to set the :guilabel:`Start Date` and
.. i18n: :guilabel:`End Date` fields in the :guilabel:`Price List Version`.

Once this list has been entered you should look for the partner form for TinAtwo again. Click the
:guilabel:`Properties` tab to set the :guilabel:`Sale List Price` field to *TinAtwo Contract*. If
the contract is only valid for one year, don't forget to set the :guilabel:`Start Date` and
:guilabel:`End Date` fields in the :guilabel:`Price List Version`.

.. i18n: Then when salespeople prepare an estimate for TinAtwo the prices proposed will automatically be
.. i18n: calculated from the contract conditions.

Then when salespeople prepare an estimate for TinAtwo the prices proposed will automatically be
calculated from the contract conditions.

.. i18n: Different bases for price calculation
.. i18n: -------------------------------------

Different bases for price calculation
-------------------------------------

.. i18n: Open ERP's flexibility enables you to make prices that depend not only on prices on the product
.. i18n: form, but in addition to the two predefined ones – Cost Price and Public Price.

Open ERP's flexibility enables you to make prices that depend not only on prices on the product
form, but in addition to the two predefined ones – Cost Price and Public Price.

.. i18n: To do this use the menu :menuselection:`Products --> Definitions --> Price Types`. Create a new
.. i18n: entry for the new price type. Enter the field name, the field on the product form that this type of
.. i18n: price corresponds to and the currency that will be expressed in this field. The operation works just
.. i18n: as well on new fields added to the product form to meet specific developments.

To do this use the menu :menuselection:`Products --> Definitions --> Price Types`. Create a new
entry for the new price type. Enter the field name, the field on the product form that this type of
price corresponds to and the currency that will be expressed in this field. The operation works just
as well on new fields added to the product form to meet specific developments.

.. i18n: Once this operation has been carried out you can make pricelists depend on this new price type.

Once this operation has been carried out you can make pricelists depend on this new price type.

.. i18n: Then, adding the weight and/or volume field, the price of a product by piece can vary by its weight
.. i18n: and/or volume. This is different from defining a price by weight – in that case the default unit
.. i18n: of measure is weight and not piece.

Then, adding the weight and/or volume field, the price of a product by piece can vary by its weight
and/or volume. This is different from defining a price by weight – in that case the default unit
of measure is weight and not piece.

.. i18n: Pricelists and managing currencies
.. i18n: ----------------------------------

Pricelists and managing currencies
----------------------------------

.. i18n: If your trading company wants to start a product catalog in a new currency you can handle this
.. i18n: several ways:

If your trading company wants to start a product catalog in a new currency you can handle this
several ways:

.. i18n: * Enter the prices in a new independent pricelist and maintain the lists in the two currencies
.. i18n:   separately,
.. i18n: 
.. i18n: * Create a field in the product form for this new currency and make the new pricelist depend on this
.. i18n:   field: prices are then maintained separately but in the product file,
.. i18n: 
.. i18n: * Create a new pricelist for the second currency and make it depend on another pricelist or on the
.. i18n:   product price: the conversion between the currencies will then be done automatically at the
.. i18n:   prevailing currency conversion rate.

* Enter the prices in a new independent pricelist and maintain the lists in the two currencies
  separately,

* Create a field in the product form for this new currency and make the new pricelist depend on this
  field: prices are then maintained separately but in the product file,

* Create a new pricelist for the second currency and make it depend on another pricelist or on the
  product price: the conversion between the currencies will then be done automatically at the
  prevailing currency conversion rate.

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
