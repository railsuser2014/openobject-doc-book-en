Production Management
######################

Summary

* Production Management

* Production and Terminology

* Routings and workcenters

* Repairs

Keywords

* Bills of Materials

* Routing

* Production Orders

* Scheduling

* Repairs

*The management of manufacturing described in this chapter will cover planning, ordering, inventory and the manufacturing or assembly of products from raw materials and components. It also covers consumption and production of products as well as the necessary operations on machinery, tools or human resources.*

The management of manufacturing in Open ERP is based on its stock management and, like it, is very flexible in both its operations and its financial control. It particularly benefits from the use of double-entry inventory management for manufacturing orders.

Manufacturing management is implemented by the *mrp* module. It is useful for transforming all types of products:

* Assemblies of parts: composite products, soldered or welded products, assemblies, packs,

* Machined parts: machining, cutting, planing,

* Foundries: clamping, heating,

* Mixtures: mixing, chemical processes, distillation.

You'll work in two areas: on products in the first part of this chapter, and on operations in the second part. The management of products depends on the concept of classiciations while the management of operations depends on routing and workcenters.

.. tip::   **Terminology**  *Bills of Materials*

    Bills of Materials, or manufacturing specifications, are named differently depending on their application area, for example:

    * Restoration: Recipe,

    * Chemicals: Equation,

    * Building: Plan.

Management of production
------------------------

Production Orders describe the operations that need to be carried out and the raw materials usage for each stage of production, You use the specifications to work out the raw material requirements and the manufacturing orders needed for the finished products.

Manufacturing will have the following consequences:

* Stock reduction: consumption of raw materials,

* Stock increase: production of finished goods,

* Analytic costs: manufacturing operations,

* Added accounting value of stock: by the creation of value following the transformation of products.

Bills of Materials
===================

Use of Bills of Materials
---------------------------

Bills of Materials are documents that describe the list of raw materials used to make a finished product. To illustrate the concept of specification you're going to work on a cabinet where the manufacturing plan is given by the figure below.

    .. image:: images/mrp_armoire.png
       :align: center

*Plan of construction of a cabinet.*

The cabinet is assembled from raw materials and intermediate assemblies:

================ =========================
Product Code     Description
================ =========================
ARM100           Cabinet
PANLAT           Wooden Side Panel
PANA100          Rear Panel
PROFIL           Metal Strut
ETA100           Shelf
PLET100          Shelf Panel
BOIS 002         Wood Panel
TAQ000           Panel Pins
LIN040           Lintel
================ =========================

To describe how to assemble this cabinet, you then define a specification for each intermediate product and for the final cabinet assembly. These are given by the table below.

============  ========  ===============
Product Code  Quantity  Unit of Measure
============  ========  ===============
ARM100        1         Unit
PANLAT        2         m2
PANA100       1         m2
PROFIL        4         m
ETA100        3         Unit
============  ========  ===============

============  ========  ===============
Product Code  Quantity  Unit of Measure
============  ========  ===============
ETA100        1         Unit
PLET100       1         Unit
TAQ0 00       4         Unit
============  ========  ===============

============  ========  ===============
Product Code  Quantity  Unit of Measure
============  ========  ===============
PROFIL        1         Unit
LIN40         0.25      m
============  ========  ===============

============  ========  ===============
Product Code  Quantity  Unit of Measure
============  ========  ===============
PANA100       1         Unit
BOIS002       0.25      m2
============  ========  ===============

============  ========  ===============
Product Code  Quantity  Unit of Measure
============  ========  ===============
PANLAT        2         Unit
BOIS002       0.083     m2
============  ========  ===============

============  ========  ===============
Product Code  Quantity  Unit of Measure
============  ========  ===============
ARM100        1         Unit
PANLAT        2         m2
PANA100       1         m2
PROFIL        4         m
ETA100        3         Unit
============  ========  ===============

The specifications are then used by the software to calculate the raw material needs based on the requirements of the finished products. Then if you want to manufacture 10 cabinets, the system can easily calculate what will be consumed:

============  =================  ===============
Product Code  Quantity           Unit of Measure
============  =================  ===============
BOIS002       2 * 0.083 + 0.25   Unit
LIN040        1                  Unit
BOIS002       0.083 * 3          m2
TAQ000        12                 Unit
============  =================  ===============

.. tip:: **Definition**  *Bill of Materials*

    To see the Bill of Materials in tree view, use the menu *Manufacturing > Configuration > Bill of Materials > Bill of Materials Structure*.

    .. image:: images/mrp_bom_tree.png
       :align: center

*Bill of Materials structure.*

Use the menu Manufacturing > Configuration > Bill of Materials > New Bill of Materials to define a new Bill of Materials.

.. tip::  **Point**   *The different views*

    To change the view in the Bill of Materials you can:

    * From the list, select a Bill of Materials name and then click *Other View*,

    * From a product form use the menu to the right *Structure of Bill of Materials*. 

    .. image:: images/mrp_bom.png
       :align: center

*Screen defining a Bill of Materials.*

In the area below the Bill of Materials you should set the finished product, which will be manufactured or assembled. Once the product has been selected, Open ERP automatically completes the name of the Bill of Materials and the default Unit of Measure for this product.

The type of specification (BoM Type: Phantom or Normal) and the range field will be described in more detail later in the chapter.

After this you can select the raw materials that are used in the manufacture of the finished product. The quantities are expressed in a report based on the quantities of finished product and the quantities needed to produce them from the Bill of Materials.

The second tab, Revisions, is used to indicate all the changes made to the specification. After each change you can specify a revision number and some notes on the modifications you carried out.

.. tip::  **More information**  *Simplified View*

The Revisions tab is only visible if the user works in the Extended View mode (which means that the user must belong to the group “Usability / Extended View“.

    .. image:: images/mrp_bom_revision.png
       :align: center

*Revisions of a Bill of Materials.*

In the third tab, Properties, you can put a free text reference to a plan, a sequence number that is used to determine the priorities between specifications, dates between which the bill of materials is valid, and values for rounding and product efficiency.

Rounding is used to set the smallest Unit of Measure for expressing the quantities of the selected product. So if you set the rounding to 1.00 you're not able to manfuacture half a piece. The efficiency of the product lets you indicate the percentage you lose during manufacture. This loss can be set for the finished product or for each raw materials line. The impact of this efficiency figure is to reserve more raw materials for manufacture than you'd otherwise use just from the Bill of Materials calculations.

The final part of the third tab enables you to set some properties for the product's manufacturing processes. These will be detailed further on in the chapter in a section on configurable products.

Multi-level Bills of Materials
===============================

In Open ERP each line of a Bill of Materials may itself be a Bill of Materials. So it's possible to define BoMs with several levels. Instead of defining several BoMs for the cabinet in the figure mrp_chest.png you could define the single Bill of Materials below:

ARM100 ; 1 ; Unit
PANLAT ; 2 ; m2
BOIS002 ; 0.166 ; m2
PANA100 ; 1 ; m2
BOIS002 ; 0.25 ; m2
PROFIL ; 4 ; m
LIN040 ; 1 ; m
ETA100 ; 3 ; Unit
PLET100 ; 3 ; Unit
BOIS010 ; 0.249 ; m2
TAQ000 ; 12 ; Unit

Open ERP behaves differently depending on whether the Bill of Materials is defined in several small BoMs each on a single level or in one BoM tree-structured on several levels.

So if you select a BoM using intermediate products that automatically generates production orders based on calculated requirements, Open ERP will propose manufacturing an intermediate product. To manufacture a cabinet, you'd create 6 production orders:

============  ========  ===============
Product Code  Quantity  Unit of Measure
============  ========  ===============
PLET100       3         Unit
BOIS002       0.25      m2
============  ========  ===============

============  ========  ===============
Product Code  Quantity  Unit of Measure
============  ========  ===============
ETA100        3         Unit
PLET100       3         Unit
TAQ000        12        Unit
============  ========  ===============

============  ========  ===============
Product Code  Quantity  Unit of Measure
============  ========  ===============
PROFIL        4         Unit
LIN040        1         Unit
============  ========  ===============

============  ========  ===============
Product Code  Quantity  Unit of Measure
============  ========  ===============
PANA100       1         Unit
BOIS002       0.25      m2
============  ========  ===============

============  ========  ===============
Product Code  Quantity  Unit of Measure
============  ========  ===============
PANA100       2         Unit
BOIS002       0.17      m2
============  ========  ===============

============  ========  ===============
Product Code  Quantity  Unit of Measure
============  ========  ===============
ARM100        1         Unit
PANLAT        2         m2
PANA100       1         m2
PROFIL        4         m
ETA100        3         Unit
============  ========  ===============

In the case where a single Bill of Materials is defined in multiple levels, a single manufacturing order will be generated for each cabinet, including all of the sub-BoMs. You'd then get the following production order:

============  ========  ===============
Product Code  Quantity  Unit of Measure
============  ========  ===============
ARM100        1         Unit
BOIS002       0.17      Unit
BOIS002       0.25      Unit
LIN040        1         Unit
BOIS010       0.25      m2
TAQ000        12        Unit
============  ========  ===============

Table: Single manufacture from a tree-structured BoM

Phantom Bills of Materials
----------------------------

If a finished product is defined using intermediate products that are themselves defined using other BoMs, Open ERP will then propose the manufacture of each intermediate product. This will give several production orders. If you only want a single production order you can define the BoM on several levels.

Sometimes, however, it is useful to define the intermediate product separately and not as part of a multi-level assembly even if you don't want the separate production orders for intermediate products.

In the example, the intermediate product ETA100 is used in the manufacture of several different cabinets. In this case you'd want to define a unique BoM for it even if you didn't want any instances of this product to be built, nor wanted to re-write these elements in a series of different multi-level BoMs.

If you    <TODO>

This representation is very useful because it allows you to define reusable elements of the assembly and keep them isolated.

If you define the BoM for the ARM100 cabinet in the way shown by the table arm100_phantom below, you'll get production orders of the 

============  ========  ===============  ===========
Product Code  Quantity  Unit of Measure  Type of BoM
============  ========  ===============  ===========
ARM100        1         Unit             normal
PANLAT        2         m2               normal
PANA100       1         m2               phantom
PROFIL        4         m                phantom
ETA100        3         Unit             phantom
============  ========  ===============  ===========

Table: arm100_phantom: definition and use of phantom BoMs

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
BOIS002       0.17      m2
============  ========  ===============

Table: arm100_phantom_of: generated production orders

Assembly Bills of Materials
-----------------------------

.. tip::  **Point**   *Sales Bills of Materials*

    In some software this is all named Sales Bills of Materials. In Open ERP the term assembly is used because the effect of the Bill of Material is visible not only in sales but also, for example, in the intermediate manufactured products.

Sales Bills of Materials enable you to define assemblies that will be sold immediately but these products could also be used in deliveries and stock management rather than just sold in isolation. For example if you deliver the cabinet in piecesfor self-assembly, set the ARM100 BoM to type 'Assembly'.

When a salesperson creates an order for an ARM100 product, Open ERP automatically changes the ARM100 from components into a packaged for sending to a customer. Then it will ask the storesperson to deliver: 2 PANLAT, 1 PANA100, 4 PROFIL, 3 ETA100. This assembly fully represent an ARM100 not the delivered products.

Example: Large distributor

As an example of using these assemblies, take the case of a supermarket. In a supermarket, you can buy bottles of cola individually or in a pack of 6 bottles. The pack and the bottles are two different products and the barcodes used are also different.

Only the customers have the right to open a pack and take out some bottles for taking them individually to the checkout. The supermarket can't then hold its stock in packs and bottles, but only individually in bottles.

You can then define a Bill of Materials for sale which defines a pack as an assembly of 6 bottles. Then when you've sold a pack, you can find a pack on the invoice or bill of sale but the associated stock operation will still be 6 bottles.

In this case of an assembly, this isn't a production order to transform the product. The transformation is done directly between the order and the set.

.. tip::   **Point** *Assemblies and Purchases*

    The use of assemblies for selling to customers has been presented here, but this functionality works just as well for purchases from suppliers.

    So in the example of a supermarket, you can buy cola in packs and the storesperson will see a number of bottles at goods in reception.

Configurable Bills of Materials
--------------------------------

In Open ERP you can define several Bills of Materials for the same product. In fact you can have several manufacturing methods or several approved raw materials for a given product. You'll see in the following section that the manufacturing procedure (the range) is attached to the Bill of Materials, so the choice of Bill of Materials implicitly includes the operations to carry out. 

Once several Bill of Materials have been defined for a particular product it's necessary to have a system to enable Open ERP to select one of them for use. By default the Bill of Materials with the lowest sequence number is selected by the system.

But to have more control over the procedure  <TODO>

.. tip::  **Definition** *Properties*

    Properties are a concept that enables the selection of a method for manufacturing a product. They are a common language between the salespeople and the technical people, to enable the salespeople to have an impact on the manufacture of the products using non-technical language and the possibilities decided on by the technicians who define the Bills of Materials.

For example you can define the properties and the following groups:

=====================  ============
Property Group         Property
=====================  ============
Warranty               3 years
Warranty               1 year
Method of Manufacture  Serial
Method of Manufacture  Batch
=====================  ============

Once the Bills of Materials have been defined you could associate the corresponding properties. Then when the salesperson goes to encode a product line he can attach the properties there. If the product must be manufactured, Open ERP will automatically choose the Bill of Materials that matches the defined properties most closely in the order.

Note the properties are only visible in the Bills of Materials and the Sales Management if you're working in the Extended View mode. If you can't see it on your screen add the group Useability / Extended View to your user.

    .. image:: images/sale_line_property.png
       :align: center

*Properties on a customer order line.*

Example: Manufacturing in a batch or on a production line

As an example, take the manufacture of the cabinet presented above. You can imagine that the company has two methods of manufacturing this cabinet:

* Manually: staff assemble the cabinets one by one and cut the wood plank by plank. This approach is usually used to assembly prototypes. It enables you to have very rapid production but only in small quantities.

* On a production line: staff use machines that are capable of cutting wood by chainsaw. This method is used for production runs of at least 50 items because the lead times using this method are quite lengthy. The start of production is much slower.

You define two Bills of Materials for the same cabinet. To distinguish between them, you will define to properties in the same group: manual assembly and production line assembly. On the quotation, the salesperson will have the possibility of indicating the method of manufacture he wants on each order line, depending on the quantities and the lead time requested by the customer.

.. tip:: **Definition** *Bills of Materials and substitute products*

    In some software, you use the term 'substitute' for this principle of configurable properties in a Bill of Materials.

By putting a Bill of Materials on its own line, it is also possible to implement substitute products. You then put the Bill of Materials of type 'Assembly' for the substitution to be transparent and that Open ERP not to propose an intermediate production order.  <TODO>

Manufacturing
=============

Once the Bills of Materials have been defined, Open ERP becomes capable of automatically deciding on the manufacturing route depending on the needs of the company.

Production orders can be suggested automatically by the system depending on several criteria described in the preceding chapter:

* Using the 'Make to Order' rules,

* Using the order point rules,

* Using the production plan.

    .. image:: images/mrp_auto.png
       :align: center

*Automatically suggesting the production orders.*

Clearly it's also possible to start production manually. To do this you can use the menu *Manufacturing > Production Orders > New Production Order*.

If you haven't installed the 'Just-In-Time' planning module *mrp_jit*, you should start the calculation of requirements for Open ERP managed automatically the production order using the different system rules. To do this use the menu *Manufacturing > Calculate all requirements*.

Workflow for complete production
=================================

To understand the usefulness and the functioning of the system you should test a complete workflow on the new database installed with the demonstration data. In the order you can see:

* The creation of a customer order,

* The manufacturing workflow for an intermediate product,

* The manufacture of an ordered product,

* The delivery of products to a customer,

* Invoicing at the end of the month,

* Traceability for after-sales service.

.. tip:: **Attention**  *Demonstration data*

    To follow the workflow shown below well, it's important to keep the same quantities as in the example and start from a new database so that you don't run into exceptions from a lack of stock.

This case, more advanced, of handling problems of procurement, will be sorted out later in the chapter.

The customer order
-------------------

Begin by encoding a customer order. To do this, use the menu *Sales Management > Orders > New Quotation*. Enter the following information:

* Customer: Agrolait,

* Shipping Policy: Invoice from picklist (second tab),

* Order Line:

  * Product: PC2 – Basic PC (assemble on demand),

  * Quantity (UoM): 1,

  * Product UoM: PCE,

  * Procure method: Make To Order.

Once the quotation has been entered you can confirm it immediately by clicking the button at the bottom to the right *Confirm Order*. Keep note of the order reference because this follows all through the process. Usually, in a new database, this will be “SO007”. At this stage you can look at the process linked to your order using the 'Process' button above and to the right of the form.

    .. image:: images/mrp_sale_process.png
       :align: center

*Process for handling Sales Order SO007.*

Start the requirements calculation using the menu *Manufacturing > Compute All Schedulers*.

Producing an Intermediate Product
-----------------------------------

To understand the implications of requirements calculation, you must know the configuration of the sold product. To do this, go to the form for product PC2 and click on the link to the right: Bill of Materials. You get the scheme show below which is the composition of the selected product.

    .. image:: images/mrp_product_bom_tree.png
       :align: center

*Composition of product PC2 in the demonstration data.*

You can see that manufacturing the PC2 computer must be done in two steps:

1: Manufacture of the intermediate product: CPU_GEN

2: Manufacture of the finished product using that intermediate product: PC2

The manufacturing supervisor can then consult the product orders using the menu Manufacturing > Production Orders > Production Orders to start. You then get a list of orders to start and the estimated start date if the customer order date is not to be missed.

    .. image:: images/mrp_production_list.png
       :align: center

*List of production orders.*

You'll see the production order for CPU_GEN but not that for PC2 because that one depends on an intermediate product. Return to the production order for CPU_GEN and click below it. If there are several of them, select the one corresponding to your order using the reference that contains your order number (in this example SO007).

    .. image:: images/mrp_production_form.png
       :align: center

*The detail of a production order.*

The system shows you that you must manufacture product CPU_GEN using the components: MB1, CPU1, FAN, RAM. You can then confirm the production's two times:

Start of production: consumption of raw materials,

End of production: manufacture of finished product.

At this stage, you should click to edit the line for the product MB1 to encode a lot number for it. The lot number is usually shown on its card, so you should just copy that over. To do that put the cursor in the field Production Lot and press <F1> to create a new lot. Indicate a lot reference, for example: MB1345678. The system may then show you a warning because this lot is not in stock, but you can ignore this message. <TODO carte mer>

The production order must be in the closed state as shown in the figure below.

    .. image:: images/mrp_production_form_end.png
       :align: center

*Production order at the end of the different steps.*

Manufacture of finished product
--------------------------------

Having manufactured the intermediate product CPU_GEN, Open ERP then automatically suggests the manufacture of the computer PC2 using the order created earlier. So return to the menu for production orders to start *Manufacturing > Production Orders > Production Orders to start*.

You'll now find the computer PC2 which has been sold to the customer, as shown in the figure below.

    .. image:: images/mrp_production_list_end.png
       :align: center

*List of production orders.*

Just as for product CPU_GEN, confirm the production order on two dates: start of production and end of production.

At this stage the product sold to the customer has been manufactured and the raw materials have been consumed and taken out of stock.

.. tip:: **Point**  *Automatic Actions*

    As well as managing the use of materials and the production of stocks, manufacturing can have the following effects which are detailed further on in the chapter:

    * adding value to stock,

    * managing operations for assembly staff,

    * automatically creating analytical accounting entries.

Delivery of product to the customer
--------------------------------------

When the products have been manufactured, the storesperson automaticallys finds the order in his list of items to do. To see the items waiting for delivery, use the menu Stock Management > Outgoing Products > Available Packings. You'll find there the lists of packing to do, as shown in the figure below.

    .. image:: images/mrp_packing_out.png
       :align: center

*List of packings to do.*

The packing orders are treated by priority of leaving so the storesperson must begin with the orders at the top of the list. Confirm that your packing list has been create by looking for the customer name (Agrolait) or by its reference (SO007). Click on it and then click the button “Approve”.

.. tip::   **Point** *Packings and Delivery*

    Depending on whether you work in the simplified or extended mode <TODO>

    * pick lists,

    * delivery order.

Invoicing at delivery
----------------------

Periodically the admininstrator or an accountant can send invoices based on the deliveries that have been carried out. To do that, you can use the menu Stock Management > Outgoing Products > Lists to Invoice. You then get a list of all the deliveries that have been carried out but which have not yet been invoiced. <TODO>

So select some or all of the deliveries. Click on the action “Invoice pickings”. Open ERP asks if you want to group the deliveries from the same partner into a single invoice or if you prefer to invoice for each delivery individually.

    .. image:: images/mrp_picking_invoice_form.png
       :align: center

*Invoicing of deliveries.*

Invoices are then produced automatically in the draft state by Open ERP and the orders of deliveries are eventually added if they were configured on the order. You can also modify the invoice before approving them finally.

    .. image:: images/mrp_invoice_list.png
       :align: center

*List of invoices generated by the system based on deliveries.*

Once you have reviewed the different invoices that were generated, you can confirm them one by one or all at once from the actions available to you. Then print the invoices using the multiple print option and send them to your customers by post.

Traceability
-------------

Now suppose that the customer phones you to tell you about a production fault in a delivered product. You can then consult the traceability through the whole manufacturing chain using the serial number indicate on the product MB1. To consult the detailed history, use the menu *Stock Management > Traceability > Production Lots*.

So find the product corresponding to the product or lot number. Once it's been found you can use the following actions:
* Upstream traceability: go back through the entire production chain to various suppliers of the final customer.

* Downstream traceability: follow the production chain to find the final customer of specified components.

Examples of the two traceability types <TODO>

    .. image:: images/mrp_tracability_upstream.png
       :align: center

*Upstream traceability from customer to suppliers.*

    .. image:: images/mrp_tracability_downstream.png
       :align: center

*Downstream traceability from supplier to customers.*

Production order in detail
===========================

In this section production orders are detailed. To open a production order, use the menu Manufacturing > Production Orders > New Product Order. You get a blank for for encoding a new production order as shown in the figure below.

    .. image:: images/mrp_production_new.png
       :align: center

*New production order.*

The production order follows the process given by the figure below.

    .. image:: images/mrp_production_processus.png
       :align: center

*Process for handling a production order.*

The date fields, priority and reference, are automatically completed when the form is first opened. Enter the product that you want to produce, and the quantity required. The Unit of Measure by default is completed automatically by Open ERP when the product is first created.

You then have to set two locations:

The location where the required raw materials should be looked for, and

The location for depositing the finished products.

You can put the Stock location in both places for simplicilty. The field Bill of Materials will automatically be completed by Open ERP when you click the button 'Calculate the Requirements'. You can then overwrite it with another BoM to specify something else to use for this specific manufacture.

The tabs 'Planned Products' and 'Works Orders' are also completed automatically when you click 'Calculate the requirements'. You'll find the raw materials there that are required for the production and the operations needed by the assembly staff.

If you want to start production, click the button 'Confirm production', and Open ERP then automatically completes the field 'Products planned'. The information in the first tab can be changed for example if:

* you want to encode a serial number for raw materials,

* you want to change the quantities consumed (lost during production).

For traceability you can take the lot numbers from the raw materials used or from the finished products. To do this click on one of the lines of the first or the third tab. Note the Lot Number.

Once the order is confirmed, you should reserve the materials. This means that you're not reliant on the hope that your requirements will be in reserve and assigns the raw materials for your stock for this production. This guides the processes of restocking. If you don't want to change the priorities just let the production order in this state and c ...  <TODO>

To start the production of products, click 'Start Production'. The raw materials are then consumed automatically from stock, which means that the draft movements become 'Done'.

Once the production is complete, click 'Production Finished'. The finished product are then put into stock.

Scheduling
===========

Calculation requirements is the calculation engine which makes planning, prioritising and ?? automatically procurement as a function of the rules defined on these products. It's started once per day. You can also start it manually using the menu Manufacturing > Calculate requirements. This then uses the parameters defined in the products, the suppliers and the company to determine the priorities between the different production orders, deliveries and supplier purchases.

You can decide the starting time by modifying the corresponding action in the menu Administration > Configuration > Planning > Planned Actions. Modify the resource called 'Run MRP Scheduler'.

    .. image:: images/stock_cron.png
       :align: center

*Configuring the start time for calculating requirements.*

.. tip::   **Technique** *Calculating requirements*

    Scheduling only confirms procurement confirmed but not started. These procurement reservations will themselves start production, tasks or purchase depending on the configuration of the requested product. <TODO>

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

Operations
===========

In the first part of this chapter, manufacturing management was handled in terms of products and materials. This section focuses on manufacturing operations. To manufacture or assemble products, as well as using raw materials and finished product you should handle operations such as assembly, drilling wood, and cutting timber.

The different operation will have impacts on the costs of manufacture and the planning as function of the available workload.

Definition of concepts
-----------------------

To manage operations you should understand the following concepts

* Workcenters,

* Routing,

* Operations.

Workcenters
-----------

Workcenters represent units of product, capable of doing material transformation operations. You can distinguish three types of workcenter: machines, tools and human resources.

.. tip::   **Definition** *Workcenter*

    Workcenters are units of manufacture, consisting of one or several people and/or machines, which can be considered as a unit for the purposes of forecasting capacity and planning.

Use the menu *Manufacturing > Configuration > Workcenters* to define a new workcenter. You get a form as shown in the figure below.

    .. image:: images/mrp_workcenter.png
       :align: center

*Definition of a workcenter.*

A workcenter must have a name and a code. It's necessary to assign a type: machine, human resource, tool, and a description of operating hours or functionality. The figure below represents the hours from Monday to Friday, from 09:00 to 17:00 with a break from 01:00 to 12:00. <TODO>

    .. image:: images/mrp_workcenter_working_hour.png
       :align: center

*Working hours for a workcenter.*

You should show a description of the workcenter and its operations.

Once the database is encoded you should enter data about the production capacity of the workcenter. Depending on whether you have a machine or a person, a workcenter will be defined in cycles or hours. If it represents a set of machines and people you can use both cycles and hours at the same time.

.. tip::   **Definition**  *A Cycle*

    A cycle corresponds to the time required to carry out an assembly operation. The user is free to determine which is the reference operation for a given workcenter. It must be represented by the cost and time of manufacture.

    For example, for a printing workcenter, a cycle will be the printing of 1 page. Or the printing of 1000 pages depending on the printer.

To define the capacity well it is necessary know for each workcenter what will be the reference operation which will serve to determine the cycle. You can then define the data relative to the capacity.

Capacity per cycle (CA): determine the number of operations that can be done in parallel during a cycle. Generally the number defines the number of identical machines or people defined by the workcenter.

Time for a cycle (TC): give the duration in hour for that or the operations defined by a cycle.

Time before production (TS): give the wait in hours to initialise production operations. Generally this represents the machine setup time.

Time after production (TN): give the delay in hours after the end of a production operation. Generally this represents the cleaning time necessary after an operation.

Effective time (ET): is a factor that is applied to the three times above to determine the real production time. This factor enables you to readjust the different times progressively and as a measure of machine utilization. You can't readjust the other times because generally they're taken from the machine's data sheet.

The total time for carrying out X operations is then given by the following formula: ((C / CA) * TC + TS + TN_ * ET. In this formula the result of the division is rounded upwards. Then if the capacity per cycle is 6 it takes 3 cycles to realize 15 operations.

.. tip::   **Point** *Multi-level routing*

It is possible to define routing on several levels to support multi-level Bills of Materials

Then on each level of a Bill of Materials you can indicate the range. The levels are then linked to hierarchies of Bills of Materials.

The second tab of the production order lets you define the links to analytical account to report the costs of the workcenter operations. If you leave the different fields empty Open ERP won't have any effect on the analytic accounts.

    .. image:: images/mrp_workcenter_tab.png
       :align: center

*Data about analytic accounts for a workcenter.*

Routing
--------

Routings define the assembly operations to be done in workcenters for manufacturing a certain product. They are usually attached to Bills of Materials which will define the assembly of products required for manufacture or for finished products.

A routing can be defined directly in a Bill of Materials or through the menu Manufacturing > Configuration > Routings. A routing has a name, a code and a description. Later in this chapter you'll see that a routing can also be associated with a stock location. That enable you to indicate where assembly takes place.

    .. image:: images/mrp_routing.png
       :align: center

*Definition of a routing with three operations.*

.. tip::  **Point**  *Subcontracting assembly*

    You'll see further on in this chapter that it is possible to link a routing and a stock location for the customer or the supplier. It's the case, for examply. After you've subcontracted the assembly of a product to a supplier.

In the routing you must show the list of operations that must be done. Each operation must be done at a workcenter and possess a number of hours and/or cycles be done.

Impact of the production order
-------------------------------

The routings are then attached to the Bills of Materials which are then also used to generate product order. On a production order one the finds the assembly operations for making on the tab called 'Operations'.

mrp_production_workorder.png


Operations on a production order.

The times and the cycles shown in the production order are in the same way as the materials, theoretical data. The user can change the values to reflect reality for manufacture. 

So if you use routings, Open ERP automatically calculates the operations required for the production order. If the workcenters are linked to analytic accounts, at the end of production, Open Erp will generate the analytic accounts representing the costs of manufacture. This will allow you to work out profitability per workcenter or manufacturing unit through analytic accounting.

But the routings also enable you to manage your production capacity. You will be able to ....  <TODO>

To see a chart of  <TODO>

    .. image:: images/mrp_workcenter_load.png
       :align: center

*Charge by workcenter.*

.. tip::  **Point** *Theoretical times*

Once the routings have been clearly defined, that enables you to determine the effective  working time per assembly worker. The time corresponds to the time for each operation actually taken by the assembly worker. That enables you to compare the real working time in your company and work out the productivity per persons.

Work operations
----------------

A production order is for several products defined in the Bills of Materials, and several operations, defined in the routing. You've seen how to handle manufacturing production by production, Some companies like to have finer-grained control of operations where instead of encoding the production they enter data on each constituent operation of production.

Management of operations
-------------------------

.. tip::   **Definition**  *Operations*

    Operations are often called work orders.

To work using work orders you must install the optional module mrp_operations. Once the module is installed you'll find a new menu called Manufacturing > Operations > Operations to be carried out. The assembly workers must then encode each step operation by operation and, for each step, the real working time for it.

    .. image:: images/mrp_operations_tree.png
       :align: center

*List of operations to be carried out.*

Operations must then be carried out one by one. On each operation the operator can click on 'Start operation' and then 'Close Operation'. The time is then worked out automatically on the operation between the two changes of status. The operator can also put the operation on hold and start again later.

The following process is attached to each operation.

    .. image:: images/mrp_operations_workflow,png
       :align: center

*Process for handling an operation.*

Thanks to this use by operation, the real working time is recorded on the production order.

The production order is automatically put into the state 'Running' once the first operation has been started. That consumes some raw materials. Similarly the production order is closed automatically once the last operation is completed. The finished products are then made.

Scores, events and barcodes
============================

If the company wants to work with barcodes in manufacturing you can work on each operation using events. Here are some examples of events for an operations:

* Starting an operation,

* Pausing an operation,

* Restarting an operation,

* Closing an operation,

* Cancelling an operation.

You place barcodes on the production orders on the machines or operators and a form of barcodes representing the events. To print barcodes select the events using the menu *Manufacturing > Configuration > Codes from start to finish*. Then click for printing the barcodes for the selected events. You can do the same for printing barcodes for the workcenters using the menu *Manufacturing > Configuration > Workcenters*.

Using the system these operations don't need data to be entered on the keyboard. To use these barcodes, open the menu Manufacturing > Barcode events. You must then scan, in order:

#. The barcode of the production order,

#. The workcenter used,

#. The event code.

    .. image:: images/mrp_operation.png
       :align: center

*Capturing events for work orders.*


Open ERP then applies the events to the relevant operation.

Subcontracting manufacture
===========================

In Open ERP it is possible to subcontract production operations (for example painting and item assembly) at a supplier's. To do this you must indicate on the relevant routing document a supplier location for stock management.

You must then configure a location dedicated to this supplier with the following data:

* Type of location: Supplier,

* Address of Location: Select an address of the subcontractor partner,

* Type of linkage: Fixed,

* Location of linkage: your Stock,

* Lead time for linkage: number of days before receipt of the finished product.

Then once the manufacture has been planned for the product in question, Open ERP will generate the following steps:

Delivery of raw materials to the stores for the supplier,

Production order for the products at the suppliers and receipt of the finished products in the stores.

Once the production order has been confirmed, Open ERP automatically generates a delivery order to send to the raw materials supplier. The storesperson can access this delivery order using the menu *Stock Management > Incoming Products*. The raw materials will then be placed in stock at the supplier's stores.

Once the delivery of raw materials has been confirmed, Open ERP activates the production order. The supplier uses the raw materials sent to produce the finished goods which will automatically be put in your own stores. The confirmation of this manufacture is made when you receive the products from your supplier. It's then that you indicate the quantities consumed by your supplier

.. tip::  **Point**  *Subcontract without routing*

    If you don't use routing you can always subcontract work orders by creating an empty routing in the subcontract bill of materials.

Production orders are found in the menu *Manufacture > Production Orders > Production Orders to start*. A production order is always carried out in two stages:

#. Consumption of raw materials

#. Production of finished products.

Depending on the company's needs, you can specify that the first step is confirmed at the acknowledgment of manufacturing supplier and the second at the receipt of finished goods in the warehouse.

Treatment of exceptions
------------------------

The set of stock requirements is generated by procurement orders. Then for each customer order line or raw materials in a manufacturing order, you will find a restocking form. To review all the procurement orders use the menu *Manufacturing > Procurement orders*.

In normal system use, you don't need to worry about procurement orders because they're automatically generated by Open ERP and the user will usually work on the results of a procurement: a production order, a task or a supplier order.

But if there are configuration problems, the system can remain blocked by a procurement without generating a corresponding document. For example, suppose that you configure a product “to produce” 'on order' but you haven't defined the bill of materials. In that case procurement of the product will stay blocked in an exception state 'No Bill of Materials defined for this product'. You must then create a bill of materials to unblock the problem.

Possible problems include:

* No bill of materials defined for production: in this case you've got to create one or indicate that the product can be purchased instead.

* No supplier available for a purchase: it's then necessary to define a supplier in the second tab of the product form.

* No address defined on the supplier partner: you must complete an address for the supplier by default for the product in consideration.

* No quantity available in stock: you must create a rule for automatically procuring (for example a minimum stock rule) and put it in the order, or manually procure it.

Some problems are just those of timing and can be automatically corrected by the system. That's why Open ERP has the two following menus:

* *Manufacturing > Automatic Procurement > Procurement Exceptions > Exceptions to correct*,

* *Manufacturing > Automatic Procurement > Procurement Exceptions > Temporary exceptions*.

If a product must be 'in stock' but is not available in your stores, Open ERP will make the exception in 'temporary' or 'to be corrected'. The exception is temporary if the system can procure it automatically, for example if a procurement rule is defined for minimum stock.

    .. image:: images/mrp_exception.png
       :align: center

*Example of a procurement in exception.*

If no procurement rule is defined the exception must be corrected manually by the user. Once the exception is corrected you can restart by clicking on 'Retry'. If you don't do that then Open ERP will automatically recalcualte on the next automated requirements calculation.

Manual procurement
-------------------

To procure internally, you can create a procurement order manually. Use the menu *Manufacturing > Procurement Orders > New Procurement* to do this.

    .. image:: images/mrp_procurement.png
       :align: center

*Encoding for a new procurement order.*

The procurement order will then be responsible for calculating a  proposal for automatic procurement for the product concerned. This procurement wll start a task, a purchase order form the supplier or a production depending on the product configuration.

    .. image:: images/mrp_procurement_flow.png
       :align: center

*Workflow for handling a procurement, a function of the product configuration.*

It is better to encode a procurement order rather than direct purchasing or production, That method has the following advantages:

The form is simpler because Open ERP calculates the different values from other values and defined rules: purchase date calculated from order date, default supplier, raw materials needs, selection of the most suitable bill of materials, etc

The calculation of requirements prioritises the procurements. If you encode a purchase directly you short-circuit the planning of different procurements.

.. tip::   **Point**  *Shortcuts*

    On the product form you have a shortcut to the left that lets you quickly create a new procurement order.

Management of waste products and secondary products
----------------------------------------------------

For the management of waste you must install the module *mrp_subproduct*. The normal behaviour of manufacture in Open ERP enables you to manufacture several units of the same finished product from raw materials (A + B > C). With waste management, the result of a manufacture can be to have both finished products and secondary products (A + B > C + D).

.. tip::   **Definition** *Waste material*

    In Open ERP waste material corresponds to secondary products that are a by-product of the main manufacturing process. For example, cutting planks of timber will produce other planks but these bits of timber are too small (or the offcuts may have value for the company if they can be used elsewhere).

If the module mrp_subproduct has been installed you get a new field in the Bill of Material that lets you set secondary products resulting from the manufacture of the finished product.

    .. image:: images/mrp_bom_subproduct.png
       :align: center

*Definition of waste products in a Bill of Materials.*

When Open ERP generates a production order based on a Bill of Materials that uses secondary product you pick up the list of all products in the the third tab of the production order 'Finished Products'.

    .. image:: images/mrp_production.png
       :align: center

*A production order producing several finished products.*

Secondary products enable you to generate several types of products from the same raw materials and manufacturing methods – only these aren't used in the calculation of requirements. Then if you need the secondary products Open ERP won't ask you to manufacture another product to use the waste products and secondary products of this manufacture. In this case you should enter another production order for the secondary product.

.. tip::   **Point** *Services in Manufacturing*

    Unlike most software for production management, Open ERP manages services as well as stockable products. So it's possible to put products of type *Service* in a Bill of Materials. These don't appear in the production order but their requirements will be taken into account.

    If they're defined as *Make to Order*. Open ERP will generate a task for the manufacture or a subcontract order for the operations. The behaviour will depend on the supply method configured on the product form *Buy* or *Produce*.

Management of repairs
======================

The management of repairs is carried out using the module *mrp_repair*. Once it's installed this module adds new menus to the Manufacturing menu:

* *Manufacturing > Repairs*

* *Manufacturing > Repairs > Repairs in quotation*

* *Manufacturing > Repairs > Repairs in progress*

* *Manufacturing > Repairs > Repairs Ready to Start*

* *Manufacturing > Repairs > Repairs to be invoiced*

* *Manufacturing > Repairs > New Repair*

In Open ERP a repair will have the following effects:

* Use of materials: items for replacement,

* Production of products: items replaced from reserved stock,

* Quality control: tracking the reasons for repair,

* Accounting entries: following stock moves,

* Receipt and delivery of product from and to the end user,

* Adding operations in the product traceability,

* Invoicing items used and/or free for repairs.

Entering data for a new repair
-------------------------------

Use the menu *Manufacturing > Repairs > New Repair* to enter a new repair into the system. You'll see a blank form for the repair data, as shown in the figure below.

    .. image:: images/mrp_repair_new.png
       :align: center

*Entering data for a new repair.*

Start by identifying the product that will be repaired using the product lot number. Open ERP then automatically completes fields from the selected lot – the partner fields, address, delivery location, and stock move.

If a warranty period has been defined in the product description, in months, Open ERP then completes the field 'Warranty limit' with the correct warranty date.

You must then specify the components that you'll be adding, replacing or removing in the operations part. On each line you must specify the following:

Add or remove a component of the finished product:

* Product Component,

* Quantity,

* Unit of Measure

* Price of Component,

* Possible lot number,

* Location where the component was found,

* To invoice or not.

Once the component has been selected, Open ERP automatically completes most of the fields:

* Quantity: 1,

* Unit of Measure: unit for managing stock defined in the product form,

* Component Price: calculated from the customer list price,

* Source location: given by the stock management,

* To invoice or not: depends on the actual date and the quarantee period.

This information is automatically proposed by the system but you can modify it all yourself.

You can also encode additional charges in the second tab of the repair: applicable list price, address and type of invoice, as well as additional line items that need to be added to the repair bill.

    .. image:: images/mrp_repair_tab2.png
       :align: center

*Second tab.*

The third tab, Quality, is for encoding information about the quality: internal notes, notes for the quotation, corrective actions and preventative actions for example.

Repair workflow
----------------

A defined process handles a repair order – both the repair itself and invoicing the client. The figure below shows this repair process.

    .. image:: images/mrp_repair_workflow.png
       :align: center

*Process for handling a repair.*

Once a repair has been entered onto the system, it is in the 'draft' state. In this state it has no impact on the rest of the system. You can print a quotation from it using the action 'Print Quotation'. The repair quotation can then be sent to the customer.

Once the customer approves the repair, use the menu *Manufacturing > Repairs > Repairs in quotation* to find the draft repair. Click to confirm the draft repair and put it into the running state. You can specify the invoicing mode in the second tab:

* no invoicing,

* invoicing before repair,

* invoicing after repair.

You can confirm the repair operation or create an invoice for the customer depending on this state.

Invoicing the repair
---------------------

When the repair is to be invoiced, an invoice is generated in the draft state by the system. This invoice contains the raw materials used (replaced components) and any other costs such as the time used for the repair. These other costs are entered on the second tab of the repair form.

If the product to be repaired is still under guarantee, Open ERP automatically suggests that the components themselves are not invoiced, but will still use any other defined costs. You can override any of these default values when you're entering the data.

The link to the generated invoice is shown on the second tab of the repair document.

Stock movements and repair
---------------------------

When the repair has been carried out, Open ERP automatically carries out stock movements for components that have been removed, added or replaced on the finished product.

The move operations are carried out using the locations shown on the first tab of the repair document. If a destination location has been specified, Open ERP automatically handles the final customer delivery order when the repair has been completed. This also lets you manage the delivery of the repaired products.

For example, take the case of the cabinet that was produced at the start of this chapter. If you have to replace the shelf PANLAT, you must enter data for the repair as in the figure below.

    .. image:: images/mrp_repair_panlat.png
       :align: center

*Repair of a shelf in a cabinet.*

In this example, you'd carry out the following operations:

* Removal of a PANLAT shelf in the cabinet and put the faulty shelf in the location: *Defective Products*,

* Placement of a new PANLAT shelf that has been taken from stock.

When the repair is ready to be confirmed, Open ERP will generate the following stock moves:

* Put faulty PANLAT into suitable stock location: *Default Production > Defective Products*,

* Consume PANLAT:*Stock > Default production*.

If you analyze the traceability of this lot number you'll see all the repair operations in the upstream and downstream traceability lists of the products concerned.

