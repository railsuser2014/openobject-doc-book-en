Scheduling
===========

Calculation requirements is the calculation engine which makes planning, prioritising and ?? automatically procurement as a function of the rules defined on these products. It's started once per day. You can also start it manually using the menu Manufacturing > Calculate requirements. This then uses the parameters defined in the products, the suppliers and the company to determine the priorities between the different production orders, deliveries and supplier purchases.

You can decide the starting time by modifying the corresponding action in the menu Administration > Configuration > Planning > Planned Actions. Modify the resource called 'Run MRP Scheduler'.

    .. image:: images/stock_cron.png
       :align: center

*Configuring the start time for calculating requirements.*

.. tip::   **Technique** *Calculating requirements*

    Scheduling only validates procurement confirmed but not started. These procurement reservations will themselves start production, tasks or purchases depending on the configuration of the requested product.

You take account of the priority of operations in the start of the reservations and procurement. Then the urgent requests or those having a past date or a date sooner than the others will be started first so that if there are not enough products in stock to satisfy all the requests, the most urgent will be produced first.

Calculation of lead times
--------------------------

Each request for products will then 

All the operations are automatically calculated by the requirements calculator. But more than creating each production order and procurements, Open ERP plans each action, You will find on each document a plan date calculated by the system.

To organize a whole chain of manufacturing and restocking, Open ERP bases everythin on the delivery date promised to the customer. This is given by the date of the confirmation in the order and the lead times shown in each product line of the order. This lead time is itself suggested automatically in the field 'Customer Lead Time' shown in the product form. It shows the time promised to the customer between the order and that of the delivery.

To show the calculation of the lead times, take the example of the cabinet above. Suppose that the cabinet is assembled in two time, use the two following Bills of Materials.

============  ========  ===============
Product Code  Quantity  Unit of Measure
============  ========  ===============
ARM100        1         Unit
PANLAT        2         Unit
BOIS002       0.25      Unit
LIN040        1         Unit
BOIS010       0.25      m2
TAQ000        12        Unit
============  ========  ===============

============  ========  ===============
Product Code  Quantity  Unit of Measure
============  ========  ===============
PANLAT        2         Unit
BOIS002       0.17      Unit
============  ========  ===============

The PANLAT is made from an order using the workflow shown. The BOIS02 is purchased on order and the other products are all found in stock. An order for the product ARM100 will then generate two production orders (ARM100 et PANLAT) then produce two purchase orders for the product BOIS02. Product BOIS02 is used in the production of both ARM100 and PANLAT. Set the lead times on the product forms to the following:

============ ================== ==================== ==================
Product Code Customer Lead Time Production Lead Time Supplier Lead Time 
============ ================== ==================== ==================
ARM100       30 days            5 days            
PANLAT                          10 days
BOIS02                                               5 days
============ ================== ==================== ==================

Then a customer order placed on the 1st January will set uup the following operations and delays:

* Delivery ARM100: 31 January (=1st January + 30 days),

* Manufacture ARM100: 26 January (=31 January – 5 days),

* Manufacture PANLAT: 16 January (=26 January – 10 days),

* Purchase BOIS02 (for ARM100): 21 January (=26 January – 5 days),

* Purchase BOIS02 (for PANLAT): 11 January (=16 January – 5 days).

In this example, Open ERP will propose making two orders to the supplier of product BOIS02. Each of these orders can be for a different planned data. Clearly before confirming these orders, the purchasing manager can group these orders into single one.

Security days
--------------

The scheduler will plan all operations as a function of the time configured on the products. But it is also possible to configure these factors in the company. These factors are then global to the company, whatever the product concerned. In the description of the company, on the Configuration tab, you find the following parameters:

* Security days: number of days to deduct from a system order to cope with the problems of restocking,

* Purchase lead time: additional days to include for all purchase orders with this supplier,

* Production lead time: number of additional days needed for manufacturing.

Period for calculating requirements: all the requests which are for procuring for a later date to the number of days which aren't calculated in the scheduler.

.. tip::  **Point** *Purchasing lead time*

    The security delay for purchases is the average time between the order generated by Open ERP and the real purchase time from the supplier by your purchasing department. This delay takes account of the order process in your company, including negotation time.

Take for example the following configuration:

* Security days: 2,

* Purchase Lead time: 3,

* Production Lead Time: 1.

The example above will then be given the following lead times:

* Delivery ARM100: 29 January (=1st January + 30 days – 2 days),

* Manufacture ARM100: 23 January (=29 January – 5 days – 1 day),

* Manufacture PANLAT: 12 January (=26 January – 10 days – 1 day),

* Purchase BOIS02 (for ARM100): 15 January (=26 January – 5 days – 3 days),

* Purchase BOIS02 (for PANLAT): 4 January (=12 January – 5 days – 3 days).


