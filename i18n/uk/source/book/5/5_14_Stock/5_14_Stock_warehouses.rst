
.. i18n: .. index:: 
.. i18n:    single: stock; warehouse

.. index:: 
   single: stock; warehouse

.. i18n: Warehouses
.. i18n: ==========

Warehouses
==========

.. i18n: Warehouses are designed for physical locations from which you can deliver to the customer and to
.. i18n: which you receive raw materials. Then when you buy products from a supplier you should take account
.. i18n: of which Warehouse you use for this purchase. This also enables the end user to not have to choose
.. i18n: from a list of locations but simply a real warehouses.

Warehouses are designed for physical locations from which you can deliver to the customer and to
which you receive raw materials. Then when you buy products from a supplier you should take account
of which Warehouse you use for this purchase. This also enables the end user to not have to choose
from a list of locations but simply a real warehouses.

.. i18n: Use the menu :menuselection:`Stock Management --> Configuration --> Warehouses` then click
.. i18n: :guilabel:`New` to configure a new warehouse.

Use the menu :menuselection:`Stock Management --> Configuration --> Warehouses` then click
:guilabel:`New` to configure a new warehouse.

.. i18n: A warehouse is defined by a link between three locations:

A warehouse is defined by a link between three locations:

.. i18n: * The :guilabel:`Location Stock` field shows the place of products available for delivery to a customer direct from
.. i18n:   this warehouse. Availability is given by all the products in that location and any child locations.
.. i18n: 
.. i18n: * The :guilabel:`Location Input` field shows where ordered products are received from a supplier to that warehouse. It
.. i18n:   can be the same as the stock location if, for example, you want to do a quality control operation on
.. i18n:   your incoming raw materials.
.. i18n: 
.. i18n: * The :guilabel:`Location Output` field (called ``Output`` in the demonstration database) is designed as a buffer zone
.. i18n:   in which you store all the items that have been picked but not yet delivered to a customer. You're
.. i18n:   strongly advised not to put this location within the stock hierarchy but instead at a level higher
.. i18n:   or the same.

* The :guilabel:`Location Stock` field shows the place of products available for delivery to a customer direct from
  this warehouse. Availability is given by all the products in that location and any child locations.

* The :guilabel:`Location Input` field shows where ordered products are received from a supplier to that warehouse. It
  can be the same as the stock location if, for example, you want to do a quality control operation on
  your incoming raw materials.

* The :guilabel:`Location Output` field (called ``Output`` in the demonstration database) is designed as a buffer zone
  in which you store all the items that have been picked but not yet delivered to a customer. You're
  strongly advised not to put this location within the stock hierarchy but instead at a level higher
  or the same.

.. i18n:     .. figure:: images/stock_warehouse.png
.. i18n:        :scale: 75
.. i18n:        :align: center
.. i18n: 
.. i18n:        *Warehouse parameters*

    .. figure:: images/stock_warehouse.png
       :scale: 75
       :align: center

       *Warehouse parameters*

.. i18n: You can also set an address for the warehouse. This address should ideally be an address for your
.. i18n: company. Once the warehouse has been defined it can be used in:

You can also set an address for the warehouse. This address should ideally be an address for your
company. Once the warehouse has been defined it can be used in:

.. i18n: * Minimum stock rules,
.. i18n: 
.. i18n: * Supplier orders,
.. i18n: 
.. i18n: * Customer orders (using the definition of a point of sale, which is linked to a warehouse).

* Minimum stock rules,

* Supplier orders,

* Customer orders (using the definition of a point of sale, which is linked to a warehouse).

.. i18n: .. index:: procurement

.. index:: procurement

.. i18n: Automatic procurement
.. i18n: ---------------------

Automatic procurement
---------------------

.. i18n: Several methods of automatically procuring products can be carried out by Open ERP:

Several methods of automatically procuring products can be carried out by Open ERP:

.. i18n: * the workflow used by products that have the procurement mode :guilabel:`Make to Order`,
.. i18n: 
.. i18n: * using minimum stock rules for :guilabel:`Make to Stock` products,
.. i18n: 
.. i18n: * using the master production schedule for :guilabel:`Make to Stock` products.

* the workflow used by products that have the procurement mode :guilabel:`Make to Order`,

* using minimum stock rules for :guilabel:`Make to Stock` products,

* using the master production schedule for :guilabel:`Make to Stock` products.

.. i18n: The two last methods are described below.

The two last methods are described below.

.. i18n: .. index:: 
.. i18n:    single: stock; orderpoint
.. i18n:    single: minimum stock rule

.. index:: 
   single: stock; orderpoint
   single: minimum stock rule

.. i18n: Minimum stock rules
.. i18n: -------------------

Minimum stock rules
-------------------

.. i18n: To automatically make stock replenishment proposals, you can use minimum stock rules. To do this use
.. i18n: the menu :menuselection:`Stock Management --> Automatic Procurements --> Minimum Stock Rules`.

To automatically make stock replenishment proposals, you can use minimum stock rules. To do this use
the menu :menuselection:`Stock Management --> Automatic Procurements --> Minimum Stock Rules`.

.. i18n: The rule is the following: if the virtual stock for the given location is lower than the minimum stock
.. i18n: indicated in the rule, the system will automatically propose a procurement to increase the level
.. i18n: of virtual stock to the maximum level given in the rule.

The rule is the following: if the virtual stock for the given location is lower than the minimum stock
indicated in the rule, the system will automatically propose a procurement to increase the level
of virtual stock to the maximum level given in the rule.

.. i18n: .. figure:: images/stock_min_rule.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *List of minimum stock rules*

.. figure:: images/stock_min_rule.png
   :scale: 75
   :align: center

   *List of minimum stock rules*

.. i18n: .. tip:: Conflict resolution
.. i18n: 
.. i18n:    You may find that draft production or procurement orders don't happen correctly.
.. i18n:    That can happen if the system is badly configured (for example if you've forgotten to set the
.. i18n:    supplier on a product).
.. i18n: 
.. i18n:    To check this, look at the list of procurements in the exception state in the menu
.. i18n:    :menuselection:`Stock Management --> Automatic Procurements --> Exceptions Procurements`. More
.. i18n:    detail on handling these exceptions is given in :ref:`ch-mnf`.

.. tip:: Conflict resolution

   You may find that draft production or procurement orders don't happen correctly.
   That can happen if the system is badly configured (for example if you've forgotten to set the
   supplier on a product).

   To check this, look at the list of procurements in the exception state in the menu
   :menuselection:`Stock Management --> Automatic Procurements --> Exceptions Procurements`. More
   detail on handling these exceptions is given in :ref:`ch-mnf`.

.. i18n: It's important to underline that the rule is based on virtual quantities and not just on real
.. i18n: quantities. It then takes account of the calculation of orders and receipts to come.

It's important to underline that the rule is based on virtual quantities and not just on real
quantities. It then takes account of the calculation of orders and receipts to come.

.. i18n: Take the following example:

Take the following example:

.. i18n: * Products in stock: 15
.. i18n: 
.. i18n: * Products ordered but not delivered: 5
.. i18n: 
.. i18n: * Products in manfacture: 2

* Products in stock: 15

* Products ordered but not delivered: 5

* Products in manfacture: 2

.. i18n: The rules defined are:

The rules defined are:

.. i18n: * Minimum stock: 13
.. i18n: 
.. i18n: * Maximum stock: 25.

* Minimum stock: 13

* Maximum stock: 25.

.. i18n: Once the rules have been properly configured the purchasing manager only needs to look at the list
.. i18n: of orders for confirmation with the supplier using the menu :menuselection:`Purchase Management -->
.. i18n: Purchase Orders --> Requests for Quotation`.

Once the rules have been properly configured the purchasing manager only needs to look at the list
of orders for confirmation with the supplier using the menu :menuselection:`Purchase Management -->
Purchase Orders --> Requests for Quotation`.

.. i18n: Note that the procurement doesn't require that you buy from a supplier. If the product has a
.. i18n: :guilabel:`Supply method` of ``Produce`` the scheduler will generate a production order and not a
.. i18n: supplier order.

Note that the procurement doesn't require that you buy from a supplier. If the product has a
:guilabel:`Supply method` of ``Produce`` the scheduler will generate a production order and not a
supplier order.

.. i18n: You can also set multiple quantities in the minimum stock rules. If you set a multiple quantity of 3
.. i18n: the system will propose procurement of 15 pieces not the 13 it really needs. In this case it
.. i18n: automatically rounds the quantity upwards.

You can also set multiple quantities in the minimum stock rules. If you set a multiple quantity of 3
the system will propose procurement of 15 pieces not the 13 it really needs. In this case it
automatically rounds the quantity upwards.

.. i18n: In a minimum stock rule, when you indicate a warehouse it suggests a stock location by default in
.. i18n: that warehouse. You can change that location by default when the scheduler completes, by location
.. i18n: and not by warehouse.

In a minimum stock rule, when you indicate a warehouse it suggests a stock location by default in
that warehouse. You can change that location by default when the scheduler completes, by location
and not by warehouse.

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
