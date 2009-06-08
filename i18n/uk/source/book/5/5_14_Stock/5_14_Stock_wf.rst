
.. i18n: Complete workflow from supplier to customer
.. i18n: ===========================================

Complete workflow from supplier to customer
===========================================

.. i18n: Now you'll follow a practical example by adapting stock management operations. In order you'll see:

Now you'll follow a practical example by adapting stock management operations. In order you'll see:

.. i18n: * defining a new product,
.. i18n: 
.. i18n: * initial setting of inventory,
.. i18n: 
.. i18n: * receiving products from a supplier,
.. i18n: 
.. i18n: * delivering to a customer,
.. i18n: 
.. i18n: * analysis of the state of stock.

* defining a new product,

* initial setting of inventory,

* receiving products from a supplier,

* delivering to a customer,

* analysis of the state of stock.

.. i18n: Defining a new product
.. i18n: -----------------------

Defining a new product
-----------------------

.. i18n: To start, define the following product:

To start, define the following product:

.. i18n: .. table:: Product Definition
.. i18n: 
.. i18n:    ==================== ======================
.. i18n:    Field                Value
.. i18n:    ==================== ======================
.. i18n:    Name                 Central Heating Type 1
.. i18n:    Code                 CCT1
.. i18n:    Product Type         Stockable Product
.. i18n:    Supply Method        Buy
.. i18n:    ==================== ======================

.. table:: Product Definition

   ==================== ======================
   Field                Value
   ==================== ======================
   Name                 Central Heating Type 1
   Code                 CCT1
   Product Type         Stockable Product
   Supply Method        Buy
   ==================== ======================

.. i18n: Use the menu :menuselection:`Products --> Products`, then click :guilabel:`New` to define a new
.. i18n: product.

Use the menu :menuselection:`Products --> Products`, then click :guilabel:`New` to define a new
product.

.. i18n: .. figure:: images/stock_product.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Definition of a new product*

.. figure:: images/stock_product.png
   :scale: 75
   :align: center

   *Definition of a new product*

.. i18n: Three fields are important for stock management when you're configuring a new product:

Three fields are important for stock management when you're configuring a new product:

.. i18n: * :guilabel:`Product Type`,
.. i18n: 
.. i18n: * :guilabel:`Procure Method`,
.. i18n: 
.. i18n: * :guilabel:`Supply Method`.

* :guilabel:`Product Type`,

* :guilabel:`Procure Method`,

* :guilabel:`Supply Method`.

.. i18n: Product Types
.. i18n: --------------

Product Types
--------------

.. i18n: The product type indicates if the product is handled in stock management and if Open ERP manages its
.. i18n: procurement. The three distinct product types are:

The product type indicates if the product is handled in stock management and if Open ERP manages its
procurement. The three distinct product types are:

.. i18n: * :guilabel:`Stockable Product` : this product is used in stock management and its replenishment is
.. i18n:   more or less automated as defined by the rules established in the system. Examples, a bicycle, a
.. i18n:   computer or a central heating system.
.. i18n: 
.. i18n: * :guilabel:`Consumable` : handled in stock management, you can receive it, deliver it and make it.
.. i18n:   But its stock level isn't managed by the system. Open ERP assumes that you've got sufficient levels
.. i18n:   in stock at all time, so it doesn't restock it automatically. Example, nails.
.. i18n: 
.. i18n: * :guilabel:`Service` : doesn't appear in the various stock operations. Example, a consulting
.. i18n:   service.

* :guilabel:`Stockable Product` : this product is used in stock management and its replenishment is
  more or less automated as defined by the rules established in the system. Examples, a bicycle, a
  computer or a central heating system.

* :guilabel:`Consumable` : handled in stock management, you can receive it, deliver it and make it.
  But its stock level isn't managed by the system. Open ERP assumes that you've got sufficient levels
  in stock at all time, so it doesn't restock it automatically. Example, nails.

* :guilabel:`Service` : doesn't appear in the various stock operations. Example, a consulting
  service.

.. i18n: Procure Methods – Make to Stock and Make to Order
.. i18n: -------------------------------------------------

Procure Methods – Make to Stock and Make to Order
-------------------------------------------------

.. i18n: The procure method determines how the product will be replenished:

The procure method determines how the product will be replenished:

.. i18n: * :guilabel:`Make to Stock` : your customers are supplied from available stock. You procure a
.. i18n:   set quantity of each product when its stock is too low. Example, a classic distributor.
.. i18n: 
.. i18n: * :guilabel:`Make to Order` : when a customer order is confirmed, you then procure or manufacture
.. i18n:   the products for this order. A customer order 'Make to Order' won't modify stock in the medium term
.. i18n:   because you restock with the exact amount that was ordered. Example, computers from a large supplier
.. i18n:   assembled on demand.

* :guilabel:`Make to Stock` : your customers are supplied from available stock. You procure a
  set quantity of each product when its stock is too low. Example, a classic distributor.

* :guilabel:`Make to Order` : when a customer order is confirmed, you then procure or manufacture
  the products for this order. A customer order 'Make to Order' won't modify stock in the medium term
  because you restock with the exact amount that was ordered. Example, computers from a large supplier
  assembled on demand.

.. i18n: You find a mix of these two modes used for the different final and intermediate products in most
.. i18n: industries. The procurement method shown on the product form is a default value for the order,
.. i18n: enabling the salesperson to choose the best mode for fulfilling a particular order by varying the 
.. i18n: sales order parameters as needed.

You find a mix of these two modes used for the different final and intermediate products in most
industries. The procurement method shown on the product form is a default value for the order,
enabling the salesperson to choose the best mode for fulfilling a particular order by varying the 
sales order parameters as needed.

.. i18n: The figures :ref:`fig-stfrst` and :ref:`fig-stfrord` show the change of stock levels for one product 
.. i18n: managed Make to Order and another 
.. i18n: managed Make to Stock. The two figures are taken from Open ERP's :guilabel:`Future Stock Forecast` report,
.. i18n: available from the product form.

The figures :ref:`fig-stfrst` and :ref:`fig-stfrord` show the change of stock levels for one product 
managed Make to Order and another 
managed Make to Stock. The two figures are taken from Open ERP's :guilabel:`Future Stock Forecast` report,
available from the product form.

.. i18n: .. _fig-stfrst:
.. i18n: 
.. i18n: .. figure:: images/stock_from_stock.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Change in stock for a product managed as Make to Stock*

.. _fig-stfrst:

.. figure:: images/stock_from_stock.png
   :scale: 75
   :align: center

   *Change in stock for a product managed as Make to Stock*

.. i18n: .. _fig-stfrord:
.. i18n: 
.. i18n: .. figure:: images/stock_from_order.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Change in stock for a product managed as Make to Order*

.. _fig-stfrord:

.. figure:: images/stock_from_order.png
   :scale: 75
   :align: center

   *Change in stock for a product managed as Make to Order*

.. i18n: .. note:: Logistical Methods
.. i18n: 
.. i18n:    The :guilabel:`Make to Stock` logistical approach is usually used for high volumes and when the
.. i18n:    demand is seasonal or otherwise easy to forecast.
.. i18n:    The :guilabel:`Make to Order` approach is used for products that are measured, or very costly to
.. i18n:    stock or have a short re-stocking time.

.. note:: Logistical Methods

   The :guilabel:`Make to Stock` logistical approach is usually used for high volumes and when the
   demand is seasonal or otherwise easy to forecast.
   The :guilabel:`Make to Order` approach is used for products that are measured, or very costly to
   stock or have a short re-stocking time.

.. i18n: Supply Methods
.. i18n: ---------------

Supply Methods
---------------

.. i18n: Open ERP supports two supply methods:

Open ERP supports two supply methods:

.. i18n: * Produce: when the product or service is supplied from internal resources,
.. i18n: 
.. i18n: * Buy: when the product is bought from a supplier.

* Produce: when the product or service is supplied from internal resources,

* Buy: when the product is bought from a supplier.

.. i18n: These are just the default settings used by the system during automated replenishment. The same
.. i18n: product can be either manufactured internally or bought from a supplier.

These are just the default settings used by the system during automated replenishment. The same
product can be either manufactured internally or bought from a supplier.

.. i18n: These three fields (:guilabel:`Supply Method`, :guilabel:`Procurem Method`, :guilabel:`Product
.. i18n: Type`) determine the system's behaviour when a product is required. The system will generate
.. i18n: different documents depending on the configuration of these three fields when satisfying an order, a
.. i18n: price quotation to a supplier or a manufacturing order.

These three fields (:guilabel:`Supply Method`, :guilabel:`Procurem Method`, :guilabel:`Product
Type`) determine the system's behaviour when a product is required. The system will generate
different documents depending on the configuration of these three fields when satisfying an order, a
price quotation to a supplier or a manufacturing order.

.. i18n: Open ERP manages both stockable products and services. A service bought from a supplier in
.. i18n: :guilabel:`Make to Order` mode, will generate a subcontract order from the supplier in question.

Open ERP manages both stockable products and services. A service bought from a supplier in
:guilabel:`Make to Order` mode, will generate a subcontract order from the supplier in question.

.. i18n: Figure :ref:`fig-stflow` illustrates different cases for automatic procurement.

Figure :ref:`fig-stflow` illustrates different cases for automatic procurement.

.. i18n: .. _fig-stflow:
.. i18n: 
.. i18n: .. figure:: images/stock_flow.png
.. i18n:    :scale: 90
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Workflow for automatic procurement, dependent on the configuration of the product*

.. _fig-stflow:

.. figure:: images/stock_flow.png
   :scale: 90
   :align: center

   *Workflow for automatic procurement, dependent on the configuration of the product*

.. i18n: The table below shows all possible cases for the figure :ref:`fig-stflow`.

The table below shows all possible cases for the figure :ref:`fig-stflow`.

.. i18n: .. table:: Consequences of Procurement Methods Make to Stock and Make To Order
.. i18n: 
.. i18n:    ================== ===================== =====================
.. i18n:    Procurement Method Produce               Buy
.. i18n:    ================== ===================== =====================
.. i18n:    MTS                Wait for availability Wait for availability
.. i18n:    MTO                Production Order      Supplier Order
.. i18n:    ================== ===================== =====================

.. table:: Consequences of Procurement Methods Make to Stock and Make To Order

   ================== ===================== =====================
   Procurement Method Produce               Buy
   ================== ===================== =====================
   MTS                Wait for availability Wait for availability
   MTO                Production Order      Supplier Order
   ================== ===================== =====================

.. i18n: .. table:: Consequences of Procurement Methods when using Services
.. i18n: 
.. i18n:    ================== ===================== =====================
.. i18n:    Procurement Method Produce               Buy
.. i18n:    ================== ===================== =====================
.. i18n:    MTS                /                     /
.. i18n:    MTO                Create task           Subcontract
.. i18n:    ================== ===================== =====================

.. table:: Consequences of Procurement Methods when using Services

   ================== ===================== =====================
   Procurement Method Produce               Buy
   ================== ===================== =====================
   MTS                /                     /
   MTO                Create task           Subcontract
   ================== ===================== =====================

.. i18n: You'll see the automated management processes for procurement in detail further on in this chapter.

You'll see the automated management processes for procurement in detail further on in this chapter.

.. i18n: .. index::
.. i18n:    single: unit of measure
.. i18n:    single: UoM

.. index::
   single: unit of measure
   single: UoM

.. i18n: Units of Measure
.. i18n: ----------------

Units of Measure
----------------

.. i18n: Open ERP supports several units of measure. Quantities of the same product can be expressed in
.. i18n: several units of measure at once. For example you can buy grain by the tonne and resell it by kg.
.. i18n: You just have to make sure that all the units of measure used for a product are in the same units of
.. i18n: measure category.

Open ERP supports several units of measure. Quantities of the same product can be expressed in
several units of measure at once. For example you can buy grain by the tonne and resell it by kg.
You just have to make sure that all the units of measure used for a product are in the same units of
measure category.

.. i18n: .. note:: Categories of units of measure
.. i18n: 
.. i18n:    All units of measure in the same category are convertible from one unit to another.

.. note:: Categories of units of measure

   All units of measure in the same category are convertible from one unit to another.

.. i18n: The table below shows some examples of units of measure and their category. The factor is used to
.. i18n: convert from one unit of measure to another as long as they are in the same category.

The table below shows some examples of units of measure and their category. The factor is used to
convert from one unit of measure to another as long as they are in the same category.

.. i18n: .. table:: Example Units of Measure
.. i18n: 
.. i18n:    ========= ============ ======
.. i18n:    UoM       Category     Factor
.. i18n:    ========= ============ ======
.. i18n:    Kg        Weight            1
.. i18n:    Gram      Weight         1000
.. i18n:    Tonne     Weight         0.01
.. i18n:    Hour      Working time      8
.. i18n:    Day       Working time      1
.. i18n:    Half-day  Working time      2
.. i18n:    Item      Unit              1
.. i18n:    100 Items Unit           0.01
.. i18n:    ========= ============ ======

.. table:: Example Units of Measure

   ========= ============ ======
   UoM       Category     Factor
   ========= ============ ======
   Kg        Weight            1
   Gram      Weight         1000
   Tonne     Weight         0.01
   Hour      Working time      8
   Day       Working time      1
   Half-day  Working time      2
   Item      Unit              1
   100 Items Unit           0.01
   ========= ============ ======

.. i18n: Depending on the table above you have 1Kg = 1000g = 0.001 Tonnes. A product in the ``Weight``
.. i18n: category could be expressed in Kg, Tonnes or Grammes. You can't express them in hours or pieces.

Depending on the table above you have 1Kg = 1000g = 0.001 Tonnes. A product in the ``Weight``
category could be expressed in Kg, Tonnes or Grammes. You can't express them in hours or pieces.

.. i18n: Use the menu :menuselection:`Products --> Configuration --> Units of Measure --> Units of Measure`
.. i18n: to define a new unit of measure.

Use the menu :menuselection:`Products --> Configuration --> Units of Measure --> Units of Measure`
to define a new unit of measure.

.. i18n: In the definition of a Unit of Measure, you have a :guilabel:`Rounding precision` factor which shows how
.. i18n: amounts are rounded after the conversion. A value of 1 gives rounding to the level of one unit. 0.01
.. i18n: gives rounding to one hundredth.

In the definition of a Unit of Measure, you have a :guilabel:`Rounding precision` factor which shows how
amounts are rounded after the conversion. A value of 1 gives rounding to the level of one unit. 0.01
gives rounding to one hundredth.

.. i18n: .. note::  Secondary Units
.. i18n: 
.. i18n:    Open ERP supports double units of measure.
.. i18n:    When you use this, the whole of the stock management system is encoded in two units that don't
.. i18n:    have a real link between them.
.. i18n: 
.. i18n:    This is very useful in the agro-food industry, for example: you sell ham by the piece but invoice
.. i18n:    by the Kg.
.. i18n:    A weighing operation is needed before invoicing the customer.

.. note::  Secondary Units

   Open ERP supports double units of measure.
   When you use this, the whole of the stock management system is encoded in two units that don't
   have a real link between them.

   This is very useful in the agro-food industry, for example: you sell ham by the piece but invoice
   by the Kg.
   A weighing operation is needed before invoicing the customer.

.. i18n: To activate the management options for double units of measure, assign the group :guilabel:`Useability /
.. i18n: Product UoS View` to your user.

To activate the management options for double units of measure, assign the group :guilabel:`Useability /
Product UoS View` to your user.

.. i18n: In this case the same product can be expressed in two units of measure belonging to different
.. i18n: categories. You can then distinguish between the unit of stock management (the piece) and the unit
.. i18n: of invoicing or sale (kg).

In this case the same product can be expressed in two units of measure belonging to different
categories. You can then distinguish between the unit of stock management (the piece) and the unit
of invoicing or sale (kg).

.. i18n: In the product form you can then set one unit of measure for sales and stock management, and one
.. i18n: unit of measure for purchases.

In the product form you can then set one unit of measure for sales and stock management, and one
unit of measure for purchases.

.. i18n: These units are given suggested titles. For each operation on a product you can use another unit of
.. i18n: measure, as long as it can be found in the same category as the two units already defined. If you
.. i18n: use another unit of measure, Open ERP automatically handles the conversion of prices and quantities.

These units are given suggested titles. For each operation on a product you can use another unit of
measure, as long as it can be found in the same category as the two units already defined. If you
use another unit of measure, Open ERP automatically handles the conversion of prices and quantities.

.. i18n: So if you have 430 Kg of carrots at 5.30 EUR/Kg, Open ERP will automatically make the conversion if
.. i18n: you want to sell in tonnes – 0.43 tonnes at 5300 EUR / tonne. If you had set a rounding factor of
.. i18n: 0.1 for the :guilabel:`tonne` unit of measure then Open ERP will tell you that you have only 0.4 tonnes
.. i18n: available.

So if you have 430 Kg of carrots at 5.30 EUR/Kg, Open ERP will automatically make the conversion if
you want to sell in tonnes – 0.43 tonnes at 5300 EUR / tonne. If you had set a rounding factor of
0.1 for the :guilabel:`tonne` unit of measure then Open ERP will tell you that you have only 0.4 tonnes
available.

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
