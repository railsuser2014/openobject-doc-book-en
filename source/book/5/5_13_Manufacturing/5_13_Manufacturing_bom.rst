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


