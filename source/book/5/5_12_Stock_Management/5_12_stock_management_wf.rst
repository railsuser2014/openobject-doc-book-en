Complete workflow from supplier to customer
===========================================

Now you'll follow a practical example by adapting stock management operations. In order you'll see:

* defining a product,

* initial setting of inventory,

* receiving products from a supplier,

* delivering to a customer,

* the final state of stock.

Defining a product
-------------------

To start, define the following product:

==================== ======================
Field                Value
==================== ======================
Name                 Central Heating Type 1
Code                 CCT1
Product Type         Stockable
Method of restocking Purchase
==================== ======================

Use the menu *Products > Products*, then click *New* to define a new product. 

    .. image:: images/stock_product.png
       :align: center

*Definition of a new product.*

Three fields are important for stock management when you're configuring a new product:

* Product Type,

* Procure Method,

* Supply Method.

Product Types
--------------

The product type indicates how the product behaves. The three distinct product types are:

Stockable Product: this product is used in stock management and its replenishment is more or less automated as defined by the rules established in the system. Example, a bicycle.

Consumable: handled in stock management, you can receive it, deliver it and make it. But its stock level isn't managed by the system. Open ERP assumes that you've got sufficient levels in stock at all time, so it doesn't restock it automatically. Example, nails.

Services: these aren't stockable products and don't appear in the various stock operations. Example, a consulting service.

Procurement Methods – Make to Stock and Make to Order
------------------------------------------------------

The procurement method shows how the product will be replenished:

* Make to Stock: you manage product stock and deliver to customers from stock. Periodically you restock a significant quantity of each product if its stock is too low. Example, a classic distributor.

* Make to Order: from production or customer orders, the scheduler automatically generates restocking operations linked directly to the current requirements. A customer order 'Make to Order' won't modify stock in the medium term because you restock with the exact amount that was ordered. Example, computers from large suppliers assembled on demand.

You find a mix of these two modes used for the different final and intermediate products in most industries. The procurement method shown on the product form is just a default value, enabling the salesperson to choose the most convenient mode for fulfilling a particular order.

The figures below show the change of stock levels for a product managed Make to Order and one managed Make to Stock. The two figures are taken from Open ERP's *Future Stock Moves* report, available from the product form.

    .. image:: images/stock_from_stock.png
       :align: center

*Change in stock for a product managed as Make to Stock.*

    .. image:: images/stock_from_order.png
       :align: center

*Change in stock for a product managed as Make to Order.*

.. tip::  *Information** *Logistical Methods*

    The *Make to Stock* logistical approach is best for high volumes and when the demand is seasonal or otherwise easy to forecast. The *Make to Order* approach is used for products that are measured, or very costly to stock or have a short re-stocking time.

Supply Methods
---------------

The Supply Method can be set to:

* Produce: when the product or service is supplied from internal resources,

* Buy: when the product is bought from a supplier.

These are just the default settings used by the system during automated replenishment. A product can be both manufactured internally and bought from a supplier at the same time if required.

The three fields (Supply Method, Procurement Method, Product Type) determine the system's behaviour when a product is required. The system will generate different documents depending on the configuration of the three fields when satisfying a demand.

Open ERP manages both stockable products and services. A service bought from a supplier in *Make to Order* mode, will generate a subcontract order from the supplier in question.

The following illustrates the different cases for automatic restocking.

    .. image:: images/stock_flow.png
       :align: center

*Workflow for automatic restocking, depending on the configuration of the product.*

The table below shows all possible cases for the figure.

================== ===================== =====================
Mode of restocking Produce               Purchase
================== ===================== =====================
MTS                Wait for availability Wait for availability
MTO                Production Order      Supplier Order
================== ===================== =====================

table_stock: Showing restocking for a product of type 'restockable' or 'consumable'.

================== ===================== =====================
Mode of restocking Produce               Purchase
================== ===================== =====================
MTS                /                     /
MTO                Create task           Subcontract
================== ===================== =====================

table_service: Showing restocking for a product of type 'service'.

You'll see the automated management processes for restocking in detail further on in this chapter.

Units of Measure
-----------------

Open ERP is completely multi- units of measure. A product can be expressed in several units of measure at once. For example you can buy grain by the tonne and resell it by kg.  You just have to make sure that all the units of measure used for a product are in the same units of measure category.

.. tip:: **Definition** *Categories of units of measure*

    All units of measure in a category are convertible from one unit to another, for any group of products. This conversion is only one of terminology, transferring from one to the other without any cost change or other manipulation.

The table below shows some examples of units of measure and their category. The factor is used to convert from one unit of measure to another as long as they are in the same category.

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

So you have 1Kg = 1000g = 0.001 Tonnes.

Use the menu *Products > Configuration > Units of Measure > Units of Measure* to define a new unit of measure. In the definition of a Unit of Measure, you have a *Rounding precision* factor which shows how amounts are rounded after the conversion. A value of 1 gives rounding to the level of one unit. 0.01 gives rounding to one hundredth.

.. tip::   **Advice**  *Secondary Units*

    Open ERP supports double units of measure . In this case, the whole of the stock management system is encode in two units that don't have a real link between them. This is very useful in the agro-food industry, for example: you sell ham by the piece but invoice by the Kg. A weighing operation is needed before invoicing the customer.

To activate the management options for double units of measure, assign the group *Useability / Product UoS View* to your user.

In the product form you can then see one unit of measure for sales and stock management, and one unit of measure for purchases. You have to use units that are in the same unit of measure category otherwise you won't be able to convert quantities between the two.

These units are given suggested titles. For each operation on a product you can use another unit of measure, as long as it can be found in the same category as the two units already defined. If you use another unit of measure, Open ERP automatically handles the conversion of prices and quantities.

So if you have 430 Kg of carottes at 5.30 EUR/Kg, Open ERP will automatically make the conversion if you want to sell in tonnes – 0.43 tonnes at 5300 EUR / tonne. If you had set a rounding factor of 0.1 for the *tonne* unit of measure then Open ERP will tell you that you have only 0.4 tonnes available.


