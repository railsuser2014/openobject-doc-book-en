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

If you only want a single work order for the complete cabinet, and not one for the BoM itself, you can define the BoM line corresponding to product ETA100 in the cabinet's BoM as type *Phantom*. Then it will automatically put ETA100's BoM contents into the cabinet's work order regardless of whether it's been defined as multi-level.

This way of representing the assembly is very useful because it allows you to define reusable elements of the assembly and keep them isolated.

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

But to gain more control over the process during the sale or procurement, you can use *properties*. The menu *Production Management > Configuration > Properties* enables you to define properties, which are concept that can be defined arbitrarily to help in the selection of Bills of Materials when you have a choice of BoM.

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

By putting a Bill of Materials on its own line, you can also implement substitute products. You set the Bill of Materials to type 'Assembly' to make the substitution transparent and for Open ERP not to propose an intermediate production order.


