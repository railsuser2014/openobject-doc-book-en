
.. i18n: Management of production
.. i18n: ========================

Management of production
========================

.. i18n: Production Orders describe the operations that need to be carried out and the raw materials usage
.. i18n: for each stage of production, You use specifications (bills of materials) 
.. i18n: to work out the raw material requirements
.. i18n: and the manufacturing orders needed for the finished products.

Production Orders describe the operations that need to be carried out and the raw materials usage
for each stage of production, You use specifications (bills of materials) 
to work out the raw material requirements
and the manufacturing orders needed for the finished products.

.. i18n: Manufacturing has the following results:

Manufacturing has the following results:

.. i18n: * Stock reduction: consumption of raw materials,
.. i18n: 
.. i18n: * Stock increase: production of finished goods,
.. i18n: 
.. i18n: * Analytic costs: manufacturing operations,
.. i18n: 
.. i18n: * Added accounting value of stock: by the creation of value following the transformation of
.. i18n:   products.

* Stock reduction: consumption of raw materials,

* Stock increase: production of finished goods,

* Analytic costs: manufacturing operations,

* Added accounting value of stock: by the creation of value following the transformation of
  products.

.. i18n: .. index:: BoM
.. i18n: .. index:: bill of materials

.. index:: BoM
.. index:: bill of materials

.. i18n: Bills of Materials
.. i18n: ===================

Bills of Materials
===================

.. i18n: Use of Bills of Materials
.. i18n: ---------------------------

Use of Bills of Materials
---------------------------

.. i18n: Bills of Materials are documents that describe the list of raw materials used to make a finished
.. i18n: product. To illustrate the concept of specification you're going to work on a cabinet where the
.. i18n: manufacturing plan is given by the figure :ref:`fig-mrparm`.

Bills of Materials are documents that describe the list of raw materials used to make a finished
product. To illustrate the concept of specification you're going to work on a cabinet where the
manufacturing plan is given by the figure :ref:`fig-mrparm`.

.. i18n: .. _fig-mrparm:
.. i18n: 
.. i18n: .. figure:: images/mrp_armoire.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Plan of construction of a cabinet*

.. _fig-mrparm:

.. figure:: images/mrp_armoire.png
   :scale: 75
   :align: center

   *Plan of construction of a cabinet*

.. i18n: The cabinet is assembled from raw materials and intermediate assemblies:

The cabinet is assembled from raw materials and intermediate assemblies:

.. i18n: .. table:: Product Definitions before defining Bills of Materials
.. i18n: 
.. i18n:    ================ =========================
.. i18n:    Product Code     Description
.. i18n:    ================ =========================
.. i18n:    ARM100           Cabinet
.. i18n:    PANLAT           Wooden Side Panel
.. i18n:    PANA100          Rear Panel
.. i18n:    PROFIL           Metal Strut
.. i18n:    ETA100           Shelf
.. i18n:    PLET100          Shelf Panel
.. i18n:    BOIS002          Wood Panel
.. i18n:    BOIS010          Wood Panel
.. i18n:    TAQ000           Panel Pins
.. i18n:    LIN040           Lintel
.. i18n:    ================ =========================

.. table:: Product Definitions before defining Bills of Materials

   ================ =========================
   Product Code     Description
   ================ =========================
   ARM100           Cabinet
   PANLAT           Wooden Side Panel
   PANA100          Rear Panel
   PROFIL           Metal Strut
   ETA100           Shelf
   PLET100          Shelf Panel
   BOIS002          Wood Panel
   BOIS010          Wood Panel
   TAQ000           Panel Pins
   LIN040           Lintel
   ================ =========================

.. i18n: To describe how to assemble this cabinet, you define a bill of materials for each intermediate
.. i18n: product and for the final cabinet assembly. These are given by the table below.

To describe how to assemble this cabinet, you define a bill of materials for each intermediate
product and for the final cabinet assembly. These are given by the table below.

.. i18n: .. table:: Bill of Materials for 1 ARM100 Unit
.. i18n: 
.. i18n:    ============  ========  ===============
.. i18n:    Product Code  Quantity  Unit of Measure
.. i18n:    ============  ========  ===============
.. i18n:    PANLAT        2         Unit
.. i18n:    PANA100       1         Unit
.. i18n:    PROFIL        4         Unit
.. i18n:    ETA100        3         Unit
.. i18n:    ============  ========  ===============

.. table:: Bill of Materials for 1 ARM100 Unit

   ============  ========  ===============
   Product Code  Quantity  Unit of Measure
   ============  ========  ===============
   PANLAT        2         Unit
   PANA100       1         Unit
   PROFIL        4         Unit
   ETA100        3         Unit
   ============  ========  ===============

.. i18n: .. table:: Bill of Materials for 1 ETA100 Unit
.. i18n: 
.. i18n:    ============  ========  ===============
.. i18n:    Product Code  Quantity  Unit of Measure
.. i18n:    ============  ========  ===============
.. i18n:    PLET100       1         Unit
.. i18n:    TAQ000        4         Unit
.. i18n:    ============  ========  ===============

.. table:: Bill of Materials for 1 ETA100 Unit

   ============  ========  ===============
   Product Code  Quantity  Unit of Measure
   ============  ========  ===============
   PLET100       1         Unit
   TAQ000        4         Unit
   ============  ========  ===============

.. i18n: .. table:: Bill of Materials for 1 PLET100 Unit
.. i18n: 
.. i18n:    ============  ========  ===============
.. i18n:    Product Code  Quantity  Unit of Measure
.. i18n:    ============  ========  ===============
.. i18n:    BOIS010       0.083     m2
.. i18n:    ============  ========  ===============

.. table:: Bill of Materials for 1 PLET100 Unit

   ============  ========  ===============
   Product Code  Quantity  Unit of Measure
   ============  ========  ===============
   BOIS010       0.083     m2
   ============  ========  ===============

.. i18n: .. table:: Bill of Materials for 1 PROFIL Unit
.. i18n: 
.. i18n:    ============  ========  ===============
.. i18n:    Product Code  Quantity  Unit of Measure
.. i18n:    ============  ========  ===============
.. i18n:    LIN40         0.25      m
.. i18n:    ============  ========  ===============

.. table:: Bill of Materials for 1 PROFIL Unit

   ============  ========  ===============
   Product Code  Quantity  Unit of Measure
   ============  ========  ===============
   LIN40         0.25      m
   ============  ========  ===============

.. i18n: .. table:: Bill of Materials for 1 PANA100 Unit
.. i18n: 
.. i18n:    ============  ========  ===============
.. i18n:    Product Code  Quantity  Unit of Measure
.. i18n:    ============  ========  ===============
.. i18n:    BOIS002       0.25      m2
.. i18n:    ============  ========  ===============

.. table:: Bill of Materials for 1 PANA100 Unit

   ============  ========  ===============
   Product Code  Quantity  Unit of Measure
   ============  ========  ===============
   BOIS002       0.25      m2
   ============  ========  ===============

.. i18n: .. table:: Bill of Materials for 1 PANLAT Unit
.. i18n: 
.. i18n:    ============  ========  ===============
.. i18n:    Product Code  Quantity  Unit of Measure
.. i18n:    ============  ========  ===============
.. i18n:    BOIS002       0.083     m2
.. i18n:    ============  ========  ===============

.. table:: Bill of Materials for 1 PANLAT Unit

   ============  ========  ===============
   Product Code  Quantity  Unit of Measure
   ============  ========  ===============
   BOIS002       0.083     m2
   ============  ========  ===============

.. i18n: The bills of materials are then used by the software to calculate the raw material needs based on the
.. i18n: requirements of the finished products. Then if you want to manufacture 10 cabinets, the system can
.. i18n: calculate what will be consumed:

The bills of materials are then used by the software to calculate the raw material needs based on the
requirements of the finished products. Then if you want to manufacture 10 cabinets, the system can
calculate what will be consumed:

.. i18n: .. table:: Total Quantities
.. i18n: 
.. i18n:    ============  =================  ===============
.. i18n:    Product Code  Quantity           Unit of Measure
.. i18n:    ============  =================  ===============
.. i18n:    BOIS002       2 * 0.083 + 0.25   m2
.. i18n:    LIN040        1                  m
.. i18n:    BOIS002       0.083 * 3          m2
.. i18n:    TAQ000        12                 Unit
.. i18n:    ============  =================  ===============

.. table:: Total Quantities

   ============  =================  ===============
   Product Code  Quantity           Unit of Measure
   ============  =================  ===============
   BOIS002       2 * 0.083 + 0.25   m2
   LIN040        1                  m
   BOIS002       0.083 * 3          m2
   TAQ000        12                 Unit
   ============  =================  ===============

.. i18n: .. tip:: Bill of Materials
.. i18n: 
.. i18n:    To see the bill of materials in tree view, use the menu :menuselection:`Manufacturing -->
.. i18n:    Configuration --> Bill of Materials --> Bill of Materials Structure`.

.. tip:: Bill of Materials

   To see the bill of materials in tree view, use the menu :menuselection:`Manufacturing -->
   Configuration --> Bill of Materials --> Bill of Materials Structure`.

.. i18n: .. figure:: images/mrp_bom_tree.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Bill of Materials structure*

.. figure:: images/mrp_bom_tree.png
   :scale: 75
   :align: center

   *Bill of Materials structure*

.. i18n: Use the menu :menuselection:`Manufacturing --> Configuration --> Bill of Materials --> New Bill of
.. i18n: Materials` to define a new bill of materials.

Use the menu :menuselection:`Manufacturing --> Configuration --> Bill of Materials --> New Bill of
Materials` to define a new bill of materials.

.. i18n: .. tip::The different views
.. i18n: 
.. i18n:     To change the view in the bill of materials you can:
.. i18n: 
.. i18n:     * From the list, select a bill of materials name and then click :guilabel:`Other View`,
.. i18n: 
.. i18n:     * From a product form use the menu :guilabel:`Structure of Bill of Materials` to the right.

.. tip::The different views

    To change the view in the bill of materials you can:

    * From the list, select a bill of materials name and then click :guilabel:`Other View`,

    * From a product form use the menu :guilabel:`Structure of Bill of Materials` to the right.

.. i18n: .. figure:: images/mrp_bom.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Screen defining a Bill of Materials*

.. figure:: images/mrp_bom.png
   :scale: 75
   :align: center

   *Screen defining a Bill of Materials*

.. i18n: In the area below the bill of materials you should set the finished product, which will be
.. i18n: manufactured or assembled. Once the product has been selected, Open ERP automatically completes the
.. i18n: name of the bill of materials and the default Unit of Measure for this product.

In the area below the bill of materials you should set the finished product, which will be
manufactured or assembled. Once the product has been selected, Open ERP automatically completes the
name of the bill of materials and the default Unit of Measure for this product.

.. i18n: The type of BoM (:guilabel:`BoM Type` : Phantom or Normal) and 
.. i18n: the :guilabel:`Routing` field will be described in
.. i18n: more detail later in the chapter.

The type of BoM (:guilabel:`BoM Type` : Phantom or Normal) and 
the :guilabel:`Routing` field will be described in
more detail later in the chapter.

.. i18n: After this you can select the raw materials that are used in the manufacture of the finished
.. i18n: product. The quantities are set out in a report based on the quantities of finished product and
.. i18n: the quantities needed to produce them from the bill of materials.

After this you can select the raw materials that are used in the manufacture of the finished
product. The quantities are set out in a report based on the quantities of finished product and
the quantities needed to produce them from the bill of materials.

.. i18n: .. index::
.. i18n:    single: BoM; revisions

.. index::
   single: BoM; revisions

.. i18n: The second tab, :guilabel:`Revisions`, is used to set down all the changes made to the 
.. i18n: bill of materials. After each
.. i18n: change you can specify a revision number and some notes on the modifications you carried out.

The second tab, :guilabel:`Revisions`, is used to set down all the changes made to the 
bill of materials. After each
change you can specify a revision number and some notes on the modifications you carried out.

.. i18n: .. note:: Simplified View
.. i18n: 
.. i18n:    The Revisions tab is only visible if the user works in the Extended View mode
.. i18n:    (which means that the user must belong to the group ``Usability / Extended View`` .

.. note:: Simplified View

   The Revisions tab is only visible if the user works in the Extended View mode
   (which means that the user must belong to the group ``Usability / Extended View`` .

.. i18n: .. figure:: images/mrp_bom_revision.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Revisions of a Bill of Materials*

.. figure:: images/mrp_bom_revision.png
   :scale: 75
   :align: center

   *Revisions of a Bill of Materials*

.. i18n: In the third tab, :guilabel:`Properties`, you can put a free text reference to a plan, 
.. i18n: a sequence number that is
.. i18n: used to determine the priorities between bills of materials, dates between which a bill of materials
.. i18n: is valid, and values for rounding and product efficiency.

In the third tab, :guilabel:`Properties`, you can put a free text reference to a plan, 
a sequence number that is
used to determine the priorities between bills of materials, dates between which a bill of materials
is valid, and values for rounding and product efficiency.

.. i18n: :guilabel:`Rounding` is used to set the smallest :guilabel:`Unit of Measure` 
.. i18n: for expressing the quantities of the selected
.. i18n: product. So if you set the rounding to 1.00 you'll not be able to manufacture half a piece. The
.. i18n: :guilabel:`Efficiency` of the product lets you indicate the percentage you lose during manufacture. This loss
.. i18n: can be set for the finished product or for each raw materials line. The impact of this efficiency
.. i18n: figure is to reserve more raw materials for manufacture than you'd otherwise use just from the Bill
.. i18n: of Materials calculations.

:guilabel:`Rounding` is used to set the smallest :guilabel:`Unit of Measure` 
for expressing the quantities of the selected
product. So if you set the rounding to 1.00 you'll not be able to manufacture half a piece. The
:guilabel:`Efficiency` of the product lets you indicate the percentage you lose during manufacture. This loss
can be set for the finished product or for each raw materials line. The impact of this efficiency
figure is to reserve more raw materials for manufacture than you'd otherwise use just from the Bill
of Materials calculations.

.. i18n: The final part of the third tab lets you set some properties for the product's manufacturing
.. i18n: processes. These will be detailed further on in the chapter in the section on configurable products.

The final part of the third tab lets you set some properties for the product's manufacturing
processes. These will be detailed further on in the chapter in the section on configurable products.

.. i18n: .. index::
.. i18n:    single: BoM; multi-level
.. i18n:    single: multi-level BoM

.. index::
   single: BoM; multi-level
   single: multi-level BoM

.. i18n: Multi-level Bills of Materials
.. i18n: ===============================

Multi-level Bills of Materials
===============================

.. i18n: In Open ERP each line of a bill of materials may itself be a bill of materials. So you can
.. i18n: define BoMs with several levels. Instead of defining several BoMs for the cabinet in the figure
.. i18n: :ref:`fig-mrparm` you could define the single bill of materials below:

In Open ERP each line of a bill of materials may itself be a bill of materials. So you can
define BoMs with several levels. Instead of defining several BoMs for the cabinet in the figure
:ref:`fig-mrparm` you could define the single bill of materials below:

.. i18n: .. table:: Single Bill of Materials for 1 ARM100 Unit
.. i18n: 
.. i18n:    ============  ========  ===============
.. i18n:    Product Code  Quantity  Unit of Measure
.. i18n:    ============  ========  ===============
.. i18n:    ARM100        1         Unit
.. i18n:    PANLAT        2         Unit
.. i18n:    BOIS002       0.166     m2
.. i18n:    PANA100       1         Unit
.. i18n:    BOIS002       0.25      m2
.. i18n:    PROFIL        4         Unit
.. i18n:    LIN040        1         m
.. i18n:    ETA100        3         Unit
.. i18n:    PLET100       3         Unit
.. i18n:    BOIS010       0.249     m2
.. i18n:    TAQ000        12        Unit
.. i18n:    ============  ========  ===============

.. table:: Single Bill of Materials for 1 ARM100 Unit

   ============  ========  ===============
   Product Code  Quantity  Unit of Measure
   ============  ========  ===============
   ARM100        1         Unit
   PANLAT        2         Unit
   BOIS002       0.166     m2
   PANA100       1         Unit
   BOIS002       0.25      m2
   PROFIL        4         Unit
   LIN040        1         m
   ETA100        3         Unit
   PLET100       3         Unit
   BOIS010       0.249     m2
   TAQ000        12        Unit
   ============  ========  ===============

.. i18n: Open ERP behaves differently depending on whether the bill of materials is defined in several small
.. i18n: BoMs each on a single level or in one BoM tree-structured on several levels.

Open ERP behaves differently depending on whether the bill of materials is defined in several small
BoMs each on a single level or in one BoM tree-structured on several levels.

.. i18n: So if you select a BoM using intermediate products that automatically generates production orders
.. i18n: based on calculated requirements, Open ERP will propose manufacturing an intermediate product. To
.. i18n: manufacture a cabinet, you'd create 6 production orders:

So if you select a BoM using intermediate products that automatically generates production orders
based on calculated requirements, Open ERP will propose manufacturing an intermediate product. To
manufacture a cabinet, you'd create 6 production orders:

.. i18n: .. table:: Production Order
.. i18n: 
.. i18n:    ============  ========  ===============
.. i18n:    Product Code  Quantity  Unit of Measure
.. i18n:    ============  ========  ===============
.. i18n:    PLET100       3         Unit
.. i18n:    BOIS010       0.25      m2
.. i18n:    ============  ========  ===============

.. table:: Production Order

   ============  ========  ===============
   Product Code  Quantity  Unit of Measure
   ============  ========  ===============
   PLET100       3         Unit
   BOIS010       0.25      m2
   ============  ========  ===============

.. i18n: .. table:: Production Order
.. i18n: 
.. i18n:    ============  ========  ===============
.. i18n:    Product Code  Quantity  Unit of Measure
.. i18n:    ============  ========  ===============
.. i18n:    ETA100        3         Unit
.. i18n:    PLET100       3         Unit
.. i18n:    TAQ000        12        Unit
.. i18n:    ============  ========  ===============

.. table:: Production Order

   ============  ========  ===============
   Product Code  Quantity  Unit of Measure
   ============  ========  ===============
   ETA100        3         Unit
   PLET100       3         Unit
   TAQ000        12        Unit
   ============  ========  ===============

.. i18n: .. table:: Production Order
.. i18n: 
.. i18n:    ============  ========  ===============
.. i18n:    Product Code  Quantity  Unit of Measure
.. i18n:    ============  ========  ===============
.. i18n:    PROFIL        4         Unit
.. i18n:    LIN040        1         m
.. i18n:    ============  ========  ===============

.. table:: Production Order

   ============  ========  ===============
   Product Code  Quantity  Unit of Measure
   ============  ========  ===============
   PROFIL        4         Unit
   LIN040        1         m
   ============  ========  ===============

.. i18n: .. table:: Production Order
.. i18n: 
.. i18n:    ============  ========  ===============
.. i18n:    Product Code  Quantity  Unit of Measure
.. i18n:    ============  ========  ===============
.. i18n:    PANA100       1         Unit
.. i18n:    BOIS002       0.25      m2
.. i18n:    ============  ========  ===============

.. table:: Production Order

   ============  ========  ===============
   Product Code  Quantity  Unit of Measure
   ============  ========  ===============
   PANA100       1         Unit
   BOIS002       0.25      m2
   ============  ========  ===============

.. i18n: .. table:: Production Order
.. i18n: 
.. i18n:    ============  ========  ===============
.. i18n:    Product Code  Quantity  Unit of Measure
.. i18n:    ============  ========  ===============
.. i18n:    PANA100       2         Unit
.. i18n:    BOIS002       0.17      m2
.. i18n:    ============  ========  ===============

.. table:: Production Order

   ============  ========  ===============
   Product Code  Quantity  Unit of Measure
   ============  ========  ===============
   PANA100       2         Unit
   BOIS002       0.17      m2
   ============  ========  ===============

.. i18n: .. table:: Production Order
.. i18n: 
.. i18n:    ============  ========  ===============
.. i18n:    Product Code  Quantity  Unit of Measure
.. i18n:    ============  ========  ===============
.. i18n:    ARM100        1         Unit
.. i18n:    PANLAT        2         Unit
.. i18n:    PANA100       1         Unit
.. i18n:    PROFIL        4         Unit
.. i18n:    ETA100        3         Unit
.. i18n:    ============  ========  ===============

.. table:: Production Order

   ============  ========  ===============
   Product Code  Quantity  Unit of Measure
   ============  ========  ===============
   ARM100        1         Unit
   PANLAT        2         Unit
   PANA100       1         Unit
   PROFIL        4         Unit
   ETA100        3         Unit
   ============  ========  ===============

.. i18n: In the case where a single bill of materials is defined in multiple levels, a single manufacturing
.. i18n: order will be generated for each cabinet, including all of the sub-BoMs. You'd then get the
.. i18n: following production order:

In the case where a single bill of materials is defined in multiple levels, a single manufacturing
order will be generated for each cabinet, including all of the sub-BoMs. You'd then get the
following production order:

.. i18n: .. table:: Single manufacture from a tree-structured BoM
.. i18n: 
.. i18n:    ============  ========  ===============
.. i18n:    Product Code  Quantity  Unit of Measure
.. i18n:    ============  ========  ===============
.. i18n:    ARM100        1         Unit
.. i18n:    BOIS002       0.17      m2
.. i18n:    BOIS002       0.25      m2
.. i18n:    LIN040        1         m
.. i18n:    BOIS010       0.25      m2
.. i18n:    TAQ000        12        Unit
.. i18n:    ============  ========  ===============

.. table:: Single manufacture from a tree-structured BoM

   ============  ========  ===============
   Product Code  Quantity  Unit of Measure
   ============  ========  ===============
   ARM100        1         Unit
   BOIS002       0.17      m2
   BOIS002       0.25      m2
   LIN040        1         m
   BOIS010       0.25      m2
   TAQ000        12        Unit
   ============  ========  ===============

.. i18n: .. index::
.. i18n:    pair: phantom; bill of materials

.. index::
   pair: phantom; bill of materials

.. i18n: Phantom Bills of Materials
.. i18n: ----------------------------

Phantom Bills of Materials
----------------------------

.. i18n: If a finished product is defined using intermediate products that are themselves defined using other
.. i18n: BoMs, Open ERP will then propose the manufacture of each intermediate product. This will give
.. i18n: several production orders. If you only want a single production order you can define a single BoM with
.. i18n: several levels.

If a finished product is defined using intermediate products that are themselves defined using other
BoMs, Open ERP will then propose the manufacture of each intermediate product. This will give
several production orders. If you only want a single production order you can define a single BoM with
several levels.

.. i18n: Sometimes, however, it is useful to define the intermediate product separately and not as part of a
.. i18n: multi-level assembly even if you don't want separate production orders for intermediate
.. i18n: products.

Sometimes, however, it is useful to define the intermediate product separately and not as part of a
multi-level assembly even if you don't want separate production orders for intermediate
products.

.. i18n: In the example, the intermediate product ETA100 is used in the manufacture of several different
.. i18n: cabinets. So you'd want to define a unique BoM for it even if you didn't want any
.. i18n: instances of this product to be built, nor wanted to re-write these elements in a series of
.. i18n: different multi-level BoMs.

In the example, the intermediate product ETA100 is used in the manufacture of several different
cabinets. So you'd want to define a unique BoM for it even if you didn't want any
instances of this product to be built, nor wanted to re-write these elements in a series of
different multi-level BoMs.

.. i18n: If you only want a single production order for the complete cabinet, and not one for the BoM itself, you
.. i18n: can define the BoM line corresponding to product ETA100 in the cabinet's BoM as type :guilabel:`Phantom`. Then
.. i18n: it will automatically put ETA100's BoM contents into the cabinet's production order even though
.. i18n: it's been defined as multi-level.

If you only want a single production order for the complete cabinet, and not one for the BoM itself, you
can define the BoM line corresponding to product ETA100 in the cabinet's BoM as type :guilabel:`Phantom`. Then
it will automatically put ETA100's BoM contents into the cabinet's production order even though
it's been defined as multi-level.

.. i18n: This way of representing the assembly is very useful because it allows you to define reusable
.. i18n: elements of the assembly and keep them isolated.

This way of representing the assembly is very useful because it allows you to define reusable
elements of the assembly and keep them isolated.

.. i18n: If you define the BoM for the ARM100 cabinet in the way shown by the table below,
.. i18n: you'll get two production orders when the order is confirmed, as shown in the tables below that.

If you define the BoM for the ARM100 cabinet in the way shown by the table below,
you'll get two production orders when the order is confirmed, as shown in the tables below that.

.. i18n: .. table:: Definition and use of phantom BoMs
.. i18n: 
.. i18n:    ============  ========  ===============  ===========
.. i18n:    Product Code  Quantity  Unit of Measure  Type of BoM
.. i18n:    ============  ========  ===============  ===========
.. i18n:    ARM100        1         Unit             normal
.. i18n:    PANLAT        2         Unit             normal
.. i18n:    PANA100       1         Unit             phantom
.. i18n:    PROFIL        4         Unit             phantom
.. i18n:    ETA100        3         Unit             phantom
.. i18n:    ============  ========  ===============  ===========

.. table:: Definition and use of phantom BoMs

   ============  ========  ===============  ===========
   Product Code  Quantity  Unit of Measure  Type of BoM
   ============  ========  ===============  ===========
   ARM100        1         Unit             normal
   PANLAT        2         Unit             normal
   PANA100       1         Unit             phantom
   PROFIL        4         Unit             phantom
   ETA100        3         Unit             phantom
   ============  ========  ===============  ===========

.. i18n: .. table:: Production Order from phantom BoMs
.. i18n: 
.. i18n:    ============  ========  ===============
.. i18n:    Product Code  Quantity  Unit of Measure
.. i18n:    ============  ========  ===============
.. i18n:    ARM100        1         Unit
.. i18n:    PANLAT        2         Unit
.. i18n:    BOIS002       0.25      m2
.. i18n:    LIN040        1         m
.. i18n:    BOIS010       0.25      m2
.. i18n:    TAQ000        12        Unit
.. i18n:    ============  ========  ===============

.. table:: Production Order from phantom BoMs

   ============  ========  ===============
   Product Code  Quantity  Unit of Measure
   ============  ========  ===============
   ARM100        1         Unit
   PANLAT        2         Unit
   BOIS002       0.25      m2
   LIN040        1         m
   BOIS010       0.25      m2
   TAQ000        12        Unit
   ============  ========  ===============

.. i18n: .. table:: Production Order from normal BoM
.. i18n: 
.. i18n:    ============  ========  ===============
.. i18n:    Product Code  Quantity  Unit of Measure
.. i18n:    ============  ========  ===============
.. i18n:    PANLAT        2         Unit
.. i18n:    BOIS002       0.17      m2
.. i18n:    ============  ========  ===============

.. table:: Production Order from normal BoM

   ============  ========  ===============
   Product Code  Quantity  Unit of Measure
   ============  ========  ===============
   PANLAT        2         Unit
   BOIS002       0.17      m2
   ============  ========  ===============

.. i18n: Assembly Bills of Materials
.. i18n: -----------------------------

Assembly Bills of Materials
-----------------------------

.. i18n: .. note:: Sales Bills of Materials
.. i18n: 
.. i18n:     In some software this is named a Sales Bill of Materials.
.. i18n:     In Open ERP the term assembly is used because the effect of the bill of materials is visible not
.. i18n:     only in sales but also elsewhere, for example in the intermediate manufactured products.

.. note:: Sales Bills of Materials

    In some software this is named a Sales Bill of Materials.
    In Open ERP the term assembly is used because the effect of the bill of materials is visible not
    only in sales but also elsewhere, for example in the intermediate manufactured products.

.. i18n: Assembly bills of materials enable you to define assemblies that will be sold directly. These
.. i18n: could also be used in deliveries and stock management rather than just sold in isolation.
.. i18n: For example if you deliver the cabinet in pieces for self-assembly, set the ARM100 BoM to type
.. i18n: ``Assembly`` .

Assembly bills of materials enable you to define assemblies that will be sold directly. These
could also be used in deliveries and stock management rather than just sold in isolation.
For example if you deliver the cabinet in pieces for self-assembly, set the ARM100 BoM to type
``Assembly`` .

.. i18n: When a salesperson creates an order for an ARM100 product, Open ERP automatically changes the ARM100
.. i18n: from a set of components into an identifiable package for sending to a customer. 
.. i18n: Then it asks the storesperson to pack 2 PANLAT, 1 PANA100, 4 PROFIL, 3 ETA100. 
.. i18n: This is described as an ARM100 not just the individual delivered products.

When a salesperson creates an order for an ARM100 product, Open ERP automatically changes the ARM100
from a set of components into an identifiable package for sending to a customer. 
Then it asks the storesperson to pack 2 PANLAT, 1 PANA100, 4 PROFIL, 3 ETA100. 
This is described as an ARM100 not just the individual delivered products.

.. i18n: Example: Large distributor
.. i18n: ^^^^^^^^^^^^^^^^^^^^^^^^^^

Example: Large distributor
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. i18n: As an example of using these assemblies, take the case of a supermarket. In a supermarket, you can
.. i18n: buy bottles of cola individually or in a pack of 6 bottles. The pack and the bottles are two
.. i18n: different products and the barcodes used are also different.

As an example of using these assemblies, take the case of a supermarket. In a supermarket, you can
buy bottles of cola individually or in a pack of 6 bottles. The pack and the bottles are two
different products and the barcodes used are also different.

.. i18n: But customers have the right to open a pack and extract some bottles to take them
.. i18n: individually to the checkout. The supermarket can't track its stock in packs and bottles any more, but
.. i18n: only individually in bottles.

But customers have the right to open a pack and extract some bottles to take them
individually to the checkout. The supermarket can't track its stock in packs and bottles any more, but
only individually in bottles.

.. i18n: So you can define a bill of materials for sale which defines a pack as an assembly of 6 bottles.
.. i18n: Then when you've sold a pack, you can find a pack on the invoice or bill of sale but the associated
.. i18n: stock operation will still be 6 bottles.

So you can define a bill of materials for sale which defines a pack as an assembly of 6 bottles.
Then when you've sold a pack, you can find a pack on the invoice or bill of sale but the associated
stock operation will still be 6 bottles.

.. i18n: In the case of this assembly, this isn't a production order to transform the product. The
.. i18n: transformation is done directly between the order and the set.

In the case of this assembly, this isn't a production order to transform the product. The
transformation is done directly between the order and the set.

.. i18n: .. note:: Assemblies and Purchases
.. i18n: 
.. i18n:    The use of assemblies for selling to customers has been described here, but this functionality
.. i18n:    works just as well for purchases from suppliers.
.. i18n: 
.. i18n:    So in the example of a supermarket, you can buy cola in packs and the storesperson will see a
.. i18n:    number of bottles at goods in reception.

.. note:: Assemblies and Purchases

   The use of assemblies for selling to customers has been described here, but this functionality
   works just as well for purchases from suppliers.

   So in the example of a supermarket, you can buy cola in packs and the storesperson will see a
   number of bottles at goods in reception.

.. i18n: Configurable Bills of Materials
.. i18n: --------------------------------

Configurable Bills of Materials
--------------------------------

.. i18n: In Open ERP you can define several bills of materials for the same product. In fact you can have
.. i18n: several manufacturing methods or several approved raw materials for a given product. You'll see in
.. i18n: the following section that the manufacturing procedure (the routing) is attached to the Bill of
.. i18n: Materials, so the choice of bill of materials implicitly includes the operations to make it.

In Open ERP you can define several bills of materials for the same product. In fact you can have
several manufacturing methods or several approved raw materials for a given product. You'll see in
the following section that the manufacturing procedure (the routing) is attached to the Bill of
Materials, so the choice of bill of materials implicitly includes the operations to make it.

.. i18n: Once several bills of materials have been defined for a particular product you need to have a
.. i18n: system to enable Open ERP to select one of them for use. By default the bill of materials with the
.. i18n: lowest sequence number is selected by the system.

Once several bills of materials have been defined for a particular product you need to have a
system to enable Open ERP to select one of them for use. By default the bill of materials with the
lowest sequence number is selected by the system.

.. i18n: To gain more control over the process during the sale or procurement, you can use **properties**.
.. i18n: The menu :menuselection:`Production Management --> Configuration --> Properties` enables you to
.. i18n: define properties, which can be defined arbitrarily to help you select a 
.. i18n: bill of materials when you have a choice of BoMs.

To gain more control over the process during the sale or procurement, you can use **properties**.
The menu :menuselection:`Production Management --> Configuration --> Properties` enables you to
define properties, which can be defined arbitrarily to help you select a 
bill of materials when you have a choice of BoMs.

.. i18n: .. note:: Properties
.. i18n: 
.. i18n:    Properties is a concept that enables the selection of a method for manufacturing a product.
.. i18n:    Properties define a common language between salespeople and technical people,
.. i18n:    letting the salespeople to have an influence on the manufacture of the products using
.. i18n:    non-technical language and the choices decided on by the technicians who define Bills
.. i18n:    of Materials.

.. note:: Properties

   Properties is a concept that enables the selection of a method for manufacturing a product.
   Properties define a common language between salespeople and technical people,
   letting the salespeople to have an influence on the manufacture of the products using
   non-technical language and the choices decided on by the technicians who define Bills
   of Materials.

.. i18n: For example you can define the properties and the following groups:

For example you can define the properties and the following groups:

.. i18n: .. table:: Properties
.. i18n: 
.. i18n:    =====================  ============
.. i18n:    Property Group         Property
.. i18n:    =====================  ============
.. i18n:    Warranty               3 years
.. i18n:    Warranty               1 year
.. i18n:    Method of Manufacture  Serial
.. i18n:    Method of Manufacture  Batch
.. i18n:    =====================  ============

.. table:: Properties

   =====================  ============
   Property Group         Property
   =====================  ============
   Warranty               3 years
   Warranty               1 year
   Method of Manufacture  Serial
   Method of Manufacture  Batch
   =====================  ============

.. i18n: Once the bills of materials have been defined you could associate the corresponding properties to them. Then
.. i18n: when the salesperson goes to encode a product line he can attach the properties there. If the
.. i18n: product must be manufactured, Open ERP will automatically choose the bill of materials that matches
.. i18n: the defined properties in the order most closely.

Once the bills of materials have been defined you could associate the corresponding properties to them. Then
when the salesperson goes to encode a product line he can attach the properties there. If the
product must be manufactured, Open ERP will automatically choose the bill of materials that matches
the defined properties in the order most closely.

.. i18n: Note the properties are only visible in the Bills of Materials and Sales Management if you're
.. i18n: working in the Extended View mode. If you can't see it on your screen add the group ``Useability /
.. i18n: Extended View`` to your user.

Note the properties are only visible in the Bills of Materials and Sales Management if you're
working in the Extended View mode. If you can't see it on your screen add the group ``Useability /
Extended View`` to your user.

.. i18n: .. figure:: images/sale_line_property.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Properties on a customer order line*

.. figure:: images/sale_line_property.png
   :scale: 75
   :align: center

   *Properties on a customer order line*

.. i18n: Example: Manufacturing in a batch or on a production line

Example: Manufacturing in a batch or on a production line

.. i18n: As an example, take the manufacture of the cabinet presented above. You can imagine that the company
.. i18n: has two methods of manufacturing this cabinet:

As an example, take the manufacture of the cabinet presented above. You can imagine that the company
has two methods of manufacturing this cabinet:

.. i18n: * Manually: staff assemble the cabinets one by one and cut the wood plank by plank. This approach is
.. i18n:   usually used to assembly prototypes. It gets you very rapid production, but at a high cost and
.. i18n:   only in small quantities.
.. i18n: 
.. i18n: * On a production line: staff use machines that are capable of cutting wood by bandsaw. This method
.. i18n:   is used for production runs of at least 50 items because the lead times using this method are quite
.. i18n:   lengthy. The delay to the start of production is much longer, yet the cost per unit is much lower
.. i18n:   in this volume.

* Manually: staff assemble the cabinets one by one and cut the wood plank by plank. This approach is
  usually used to assembly prototypes. It gets you very rapid production, but at a high cost and
  only in small quantities.

* On a production line: staff use machines that are capable of cutting wood by bandsaw. This method
  is used for production runs of at least 50 items because the lead times using this method are quite
  lengthy. The delay to the start of production is much longer, yet the cost per unit is much lower
  in this volume.

.. i18n: You define two bills of materials for the same cabinet. To distinguish between them, you will define
.. i18n: to properties in the same group: ``manual assembly`` and ``production line assembly`` . On the quotation, the
.. i18n: salesperson can set the method of manufacture he wants on each order line, 
.. i18n: depending on the quantities and the lead time requested by the customer.

You define two bills of materials for the same cabinet. To distinguish between them, you will define
to properties in the same group: ``manual assembly`` and ``production line assembly`` . On the quotation, the
salesperson can set the method of manufacture he wants on each order line, 
depending on the quantities and the lead time requested by the customer.

.. i18n: .. index::
.. i18n:    single: BoM, substitute products
.. i18n:    
.. i18n: .. note:: bills of materials and substitute products
.. i18n: 
.. i18n:     In some software, you use the term ``substitute`` for this principle of configurable properties in
.. i18n:     a bill of materials.

.. index::
   single: BoM, substitute products
   
.. note:: bills of materials and substitute products

    In some software, you use the term ``substitute`` for this principle of configurable properties in
    a bill of materials.

.. i18n: By putting a bill of materials on its own line, you can also implement substitute products. You set
.. i18n: the bill of materials to type ``Assembly`` to make the substitution transparent and to prevent Open ERP 
.. i18n: from proposing an intermediate production order.

By putting a bill of materials on its own line, you can also implement substitute products. You set
the bill of materials to type ``Assembly`` to make the substitution transparent and to prevent Open ERP 
from proposing an intermediate production order.

.. i18n: Manufacturing
.. i18n: =============

Manufacturing
=============

.. i18n: Once the bills of materials have been defined, Open ERP becomes capable of automatically deciding on
.. i18n: the manufacturing route depending on the needs of the company.

Once the bills of materials have been defined, Open ERP becomes capable of automatically deciding on
the manufacturing route depending on the needs of the company.

.. i18n: Production orders can be proposed automatically by the system depending on several criteria
.. i18n: described in the preceding chapter:

Production orders can be proposed automatically by the system depending on several criteria
described in the preceding chapter:

.. i18n: * Using the ``Make to Order`` rules,
.. i18n: 
.. i18n: * Using the ``Order Point`` rules,
.. i18n: 
.. i18n: * Using the Production plan.

* Using the ``Make to Order`` rules,

* Using the ``Order Point`` rules,

* Using the Production plan.

.. i18n: .. figure:: images/mrp_auto.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Automatically proposing production orders*

.. figure:: images/mrp_auto.png
   :scale: 75
   :align: center

   *Automatically proposing production orders*

.. i18n: Clearly it's also possible to start production manually. To do this you can use the menu
.. i18n: :menuselection:`Manufacturing --> Production Orders --> New Production Order`.

Clearly it's also possible to start production manually. To do this you can use the menu
:menuselection:`Manufacturing --> Production Orders --> New Production Order`.

.. i18n: .. index::
.. i18n:    single: module; mrp_jit

.. index::
   single: module; mrp_jit

.. i18n: If you haven't installed the Just-In-Time planning module :mod:`mrp_jit`, you should start
.. i18n: using Open ERP to schedule the Production Orders automatically using the
.. i18n: various system rules. To do this use the menu :menuselection:`Manufacturing --> Compute All Schedulers`.

If you haven't installed the Just-In-Time planning module :mod:`mrp_jit`, you should start
using Open ERP to schedule the Production Orders automatically using the
various system rules. To do this use the menu :menuselection:`Manufacturing --> Compute All Schedulers`.

.. i18n: Workflow for complete production
.. i18n: =================================

Workflow for complete production
=================================

.. i18n: To understand the usefulness and the functioning of the system you should test a complete workflow
.. i18n: on the new database installed with the demonstration data. In the order you can see:

To understand the usefulness and the functioning of the system you should test a complete workflow
on the new database installed with the demonstration data. In the order you can see:

.. i18n: * The creation of a customer order,
.. i18n: 
.. i18n: * The manufacturing workflow for an intermediate product,
.. i18n: 
.. i18n: * The manufacture of an ordered product,
.. i18n: 
.. i18n: * The delivery of products to a customer,
.. i18n: 
.. i18n: * Invoicing at the end of the month,
.. i18n: 
.. i18n: * Traceability for after-sales service.

* The creation of a customer order,

* The manufacturing workflow for an intermediate product,

* The manufacture of an ordered product,

* The delivery of products to a customer,

* Invoicing at the end of the month,

* Traceability for after-sales service.

.. i18n: .. tip:: Demonstration data
.. i18n: 
.. i18n:     To follow the workflow shown below exactly, you should keep the same quantities as in the
.. i18n:     example and start from a new database. Then you won't run into exceptions that would result
.. i18n:     from a lack of stock.

.. tip:: Demonstration data

    To follow the workflow shown below exactly, you should keep the same quantities as in the
    example and start from a new database. Then you won't run into exceptions that would result
    from a lack of stock.

.. i18n: This more advanced case of handling problems in procurement, will be sorted out later in the
.. i18n: chapter.

This more advanced case of handling problems in procurement, will be sorted out later in the
chapter.

.. i18n: The customer order
.. i18n: ------------------

The customer order
------------------

.. i18n: .. index:: quotation

.. index:: quotation

.. i18n: Begin by encoding a customer order. To do this, use the menu :menuselection:`Sales Management -->
.. i18n: Sales Orders -> New Quotation`. Enter the following information:

Begin by encoding a customer order. To do this, use the menu :menuselection:`Sales Management -->
Sales Orders -> New Quotation`. Enter the following information:

.. i18n: * :guilabel:`Customer` : Agrolait,
.. i18n: 
.. i18n: * :guilabel:`Shipping Policy` : Invoice from picklist (second tab),
.. i18n: 
.. i18n: * :guilabel:`Order Line` :
.. i18n: 
.. i18n:   * :guilabel:`Product` : PC2 – Basic PC (assemble on demand),
.. i18n: 
.. i18n:   * :guilabel:`Quantity (UoM)` : 1,
.. i18n: 
.. i18n:   * :guilabel:`Product UoM` : PCE,
.. i18n: 
.. i18n:   * :guilabel:`Procure method` : Make To Order.

* :guilabel:`Customer` : Agrolait,

* :guilabel:`Shipping Policy` : Invoice from picklist (second tab),

* :guilabel:`Order Line` :

  * :guilabel:`Product` : PC2 – Basic PC (assemble on demand),

  * :guilabel:`Quantity (UoM)` : 1,

  * :guilabel:`Product UoM` : PCE,

  * :guilabel:`Procure method` : Make To Order.

.. i18n: Once the quotation has been entered you can confirm it immediately by clicking the button
.. i18n: :guilabel:`Confirm Order` at the bottom to the right. Keep note of the order reference because this
.. i18n: follows all through the process. Usually, in a new database, this will be ``SO007`` . At this stage
.. i18n: you can look at the process linked to your order using the :guilabel:`Process` button above and to the right
.. i18n: of the form.

Once the quotation has been entered you can confirm it immediately by clicking the button
:guilabel:`Confirm Order` at the bottom to the right. Keep note of the order reference because this
follows all through the process. Usually, in a new database, this will be ``SO007`` . At this stage
you can look at the process linked to your order using the :guilabel:`Process` button above and to the right
of the form.

.. i18n: .. figure:: images/mrp_sale_process.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Process for handling Sales Order SO007*

.. figure:: images/mrp_sale_process.png
   :scale: 75
   :align: center

   *Process for handling Sales Order SO007*

.. i18n: Start the requirements calculation using the menu :menuselection:`Manufacturing --> Compute All
.. i18n: Schedulers`.

Start the requirements calculation using the menu :menuselection:`Manufacturing --> Compute All
Schedulers`.

.. i18n: .. index::
.. i18n:    single: semi-finished product

.. index::
   single: semi-finished product

.. i18n: Producing an Intermediate Product
.. i18n: -----------------------------------

Producing an Intermediate Product
-----------------------------------

.. i18n: To understand the implications of requirements calculation, you must know the configuration of the
.. i18n: sold product. To do this, go to the form for product PC2 and click on the link :guilabel:`Bill of
.. i18n: Materials` to the right. You get the scheme shown in :ref:`fig-mrpbomtree` which is the composition 
.. i18n: of the selected product.

To understand the implications of requirements calculation, you must know the configuration of the
sold product. To do this, go to the form for product PC2 and click on the link :guilabel:`Bill of
Materials` to the right. You get the scheme shown in :ref:`fig-mrpbomtree` which is the composition 
of the selected product.

.. i18n: .. _fig-mrpbomtree:
.. i18n: 
.. i18n: .. figure:: images/mrp_product_bom_tree.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Composition of product PC2 in the demonstration data*

.. _fig-mrpbomtree:

.. figure:: images/mrp_product_bom_tree.png
   :scale: 75
   :align: center

   *Composition of product PC2 in the demonstration data*

.. i18n: Manufacturing the PC2 computer must be done in two steps:

Manufacturing the PC2 computer must be done in two steps:

.. i18n: 1: Manufacture of the intermediate product: CPU_GEN

1: Manufacture of the intermediate product: CPU_GEN

.. i18n: 2: Manufacture of the finished product using that intermediate product: PC2

2: Manufacture of the finished product using that intermediate product: PC2

.. i18n: The manufacturing supervisor can then consult the product orders using the menu
.. i18n: :menuselection:`Manufacturing --> Production Orders --> Production Orders To Start`. You then get a
.. i18n: list of orders to start and the estimated start date to meet the ordered customer delivery date.

The manufacturing supervisor can then consult the product orders using the menu
:menuselection:`Manufacturing --> Production Orders --> Production Orders To Start`. You then get a
list of orders to start and the estimated start date to meet the ordered customer delivery date.

.. i18n: .. figure:: images/mrp_production_list.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *List of production orders*

.. figure:: images/mrp_production_list.png
   :scale: 75
   :align: center

   *List of production orders*

.. i18n: You'll see the production order for CPU_GEN but not that for PC2 because that one depends on an
.. i18n: intermediate product. Return to the production order for CPU_GEN and click below it. If there are
.. i18n: several of them, select the one corresponding to your order using the reference that contains your
.. i18n: order number (in this example ``SO007`` ).

You'll see the production order for CPU_GEN but not that for PC2 because that one depends on an
intermediate product. Return to the production order for CPU_GEN and click below it. If there are
several of them, select the one corresponding to your order using the reference that contains your
order number (in this example ``SO007`` ).

.. i18n: .. figure:: images/mrp_production_form.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *The detail of a production order*

.. figure:: images/mrp_production_form.png
   :scale: 75
   :align: center

   *The detail of a production order*

.. i18n: The system shows you that you must manufacture product CPU_GEN using the components: MB1, CPU1, FAN,
.. i18n: RAM. You can then confirm the production twice:

The system shows you that you must manufacture product CPU_GEN using the components: MB1, CPU1, FAN,
RAM. You can then confirm the production twice:

.. i18n: Start of production: consumption of raw materials,

Start of production: consumption of raw materials,

.. i18n: End of production: manufacture of finished product.

End of production: manufacture of finished product.

.. i18n: At this stage, you should click to edit the line for the product MB1 to enter a lot number for it.
.. i18n: The lot number is usually shown the parent chart, so you should just copy that over. To do that put
.. i18n: the cursor in the field :guilabel:`Production Lot` and press :kbd:`<F1>` to create a new lot. Set a lot
.. i18n: reference, for example: ``MB1345678`` . The system may then show you a warning because this lot is not in
.. i18n: stock, but you can ignore this message.

At this stage, you should click to edit the line for the product MB1 to enter a lot number for it.
The lot number is usually shown the parent chart, so you should just copy that over. To do that put
the cursor in the field :guilabel:`Production Lot` and press :kbd:`<F1>` to create a new lot. Set a lot
reference, for example: ``MB1345678`` . The system may then show you a warning because this lot is not in
stock, but you can ignore this message.

.. i18n: The production order must be in the closed state as shown in the figure :ref:`fig-mrpprdfrm`.

The production order must be in the closed state as shown in the figure :ref:`fig-mrpprdfrm`.

.. i18n: .. _fig-mrpprdfrm:
.. i18n: 
.. i18n: .. figure:: images/mrp_production_form_end.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Production order after the different stages*

.. _fig-mrpprdfrm:

.. figure:: images/mrp_production_form_end.png
   :scale: 75
   :align: center

   *Production order after the different stages*

.. i18n: Manufacture of finished product
.. i18n: --------------------------------

Manufacture of finished product
--------------------------------

.. i18n: Having manufactured the intermediate product CPU_GEN, Open ERP then automatically proposes the
.. i18n: manufacture of the computer PC2 using the order created earlier. So return to the menu for
.. i18n: production orders to start :menuselection:`Manufacturing --> Production Orders --> Production Orders
.. i18n: to start`.

Having manufactured the intermediate product CPU_GEN, Open ERP then automatically proposes the
manufacture of the computer PC2 using the order created earlier. So return to the menu for
production orders to start :menuselection:`Manufacturing --> Production Orders --> Production Orders
to start`.

.. i18n: You'll find computer PC2 which has been sold to the customer, 
.. i18n: as shown in the figure :ref:`fig-mrpprdlis`.

You'll find computer PC2 which has been sold to the customer, 
as shown in the figure :ref:`fig-mrpprdlis`.

.. i18n: .. _fig-mrpprdlis:
.. i18n: 
.. i18n: .. figure:: images/mrp_production_list_end.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *List of production orders*

.. _fig-mrpprdlis:

.. figure:: images/mrp_production_list_end.png
   :scale: 75
   :align: center

   *List of production orders*

.. i18n: Just as for product CPU_GEN, confirm the production order between two dates: start of production and end
.. i18n: of production. 

Just as for product CPU_GEN, confirm the production order between two dates: start of production and end
of production. 

.. i18n: .. todo:: Between two dates? What does that mean?

.. todo:: Between two dates? What does that mean?

.. i18n: The product sold to the customer has now been manufactured and the raw materials have been
.. i18n: consumed and taken out of stock.

The product sold to the customer has now been manufactured and the raw materials have been
consumed and taken out of stock.

.. i18n: .. tip:: Automatic Actions
.. i18n: 
.. i18n:     As well as managing the use of materials and the production of stocks,
.. i18n:     manufacturing can have the following automatic effects which are detailed further on in the
.. i18n:     chapter:
.. i18n: 
.. i18n:     * adding value to stock,
.. i18n: 
.. i18n:     * generating operations for assembly staff,
.. i18n: 
.. i18n:     * automatically creating analytical accounting entries.

.. tip:: Automatic Actions

    As well as managing the use of materials and the production of stocks,
    manufacturing can have the following automatic effects which are detailed further on in the
    chapter:

    * adding value to stock,

    * generating operations for assembly staff,

    * automatically creating analytical accounting entries.

.. i18n: Delivery of product to the customer
.. i18n: --------------------------------------

Delivery of product to the customer
--------------------------------------

.. i18n: .. index::
.. i18n:    single: picking
.. i18n:    single: packing

.. index::
   single: picking
   single: packing

.. i18n: When the products have been manufactured, the storesperson automatically finds the order in his
.. i18n: list of items to do. To see the items waiting for delivery, use the menu :menuselection:`Stock
.. i18n: Management --> Outgoing Products --> Available Packing`. You'll find lists of packing to
.. i18n: be done, there, as shown in the figure :ref:`fig-mrppacko`.

When the products have been manufactured, the storesperson automatically finds the order in his
list of items to do. To see the items waiting for delivery, use the menu :menuselection:`Stock
Management --> Outgoing Products --> Available Packing`. You'll find lists of packing to
be done, there, as shown in the figure :ref:`fig-mrppacko`.

.. i18n: .. _fig-mrppacko:
.. i18n: 
.. i18n: .. figure:: images/mrp_packing_out.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *List of packing operations to be done*

.. _fig-mrppacko:

.. figure:: images/mrp_packing_out.png
   :scale: 75
   :align: center

   *List of packing operations to be done*

.. i18n: The packing orders are presented in priority order of despatch 
.. i18n: so the storesperson must begin with the orders
.. i18n: at the top of the list. Confirm that your packing list has been created by looking for the customer
.. i18n: name ( ``Agrolait`` ) or by its reference ( ``SO007`` ). Click on it and then click the button
.. i18n: :guilabel:`Approve`.

The packing orders are presented in priority order of despatch 
so the storesperson must begin with the orders
at the top of the list. Confirm that your packing list has been created by looking for the customer
name ( ``Agrolait`` ) or by its reference ( ``SO007`` ). Click on it and then click the button
:guilabel:`Approve`.

.. i18n: .. tip:: Packing and Delivery
.. i18n: 
.. i18n:     Depending on whether you work in the simplified or extended mode you may need a further
.. i18n:     step to make a delivery to your customer, so you'd have to carry out the two steps:
.. i18n: 
.. i18n:     * picking list,
.. i18n: 
.. i18n:     * delivery order.

.. tip:: Packing and Delivery

    Depending on whether you work in the simplified or extended mode you may need a further
    step to make a delivery to your customer, so you'd have to carry out the two steps:

    * picking list,

    * delivery order.

.. i18n: .. index::
.. i18n:    single: invoicing; at delivery

.. index::
   single: invoicing; at delivery

.. i18n: Invoicing at delivery
.. i18n: ----------------------

Invoicing at delivery
----------------------

.. i18n: Periodically the administrator or an accountant can send invoices based on the deliveries that have
.. i18n: been carried out. To do that, you can use the menu :menuselection:`Stock Management --> Outgoing
.. i18n: Products --> Packing to Invoice --> Packing by Invoice Method`. 
.. i18n: You then get a list of all the deliveries that have been made but
.. i18n: haven't yet been invoiced.

Periodically the administrator or an accountant can send invoices based on the deliveries that have
been carried out. To do that, you can use the menu :menuselection:`Stock Management --> Outgoing
Products --> Packing to Invoice --> Packing by Invoice Method`. 
You then get a list of all the deliveries that have been made but
haven't yet been invoiced.

.. i18n: So select some or all of the deliveries. Click on the action :guilabel:`Create Invoice`. Open ERP asks
.. i18n: if you want to group the deliveries from the same partner into a single invoice or if you'd prefer to
.. i18n: invoice for each delivery individually.

So select some or all of the deliveries. Click on the action :guilabel:`Create Invoice`. Open ERP asks
if you want to group the deliveries from the same partner into a single invoice or if you'd prefer to
invoice for each delivery individually.

.. i18n: .. figure:: images/mrp_picking_invoice_form.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Invoicing of deliveries*

.. figure:: images/mrp_picking_invoice_form.png
   :scale: 75
   :align: center

   *Invoicing of deliveries*

.. i18n: Invoices are generated automatically in the ``Draft`` state by Open ERP. 
.. i18n: You can modify invoices before approving them finally.

Invoices are generated automatically in the ``Draft`` state by Open ERP. 
You can modify invoices before approving them finally.

.. i18n: .. figure:: images/mrp_invoice_list.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *List of invoices generated by the system based on deliveries*

.. figure:: images/mrp_invoice_list.png
   :scale: 75
   :align: center

   *List of invoices generated by the system based on deliveries*

.. i18n: Once you have reviewed the different invoices that were generated, you can confirm them one by one
.. i18n: or all at once by using the available actions. Then print the invoices using the multiple print
.. i18n: option and send them to your customers by post.

Once you have reviewed the different invoices that were generated, you can confirm them one by one
or all at once by using the available actions. Then print the invoices using the multiple print
option and send them to your customers by post.

.. i18n: Traceability
.. i18n: -------------

Traceability
-------------

.. i18n: Now suppose that the customer phones you to tell you about a production fault in a delivered
.. i18n: product. You can consult the traceability through the whole manufacturing chain using the
.. i18n: serial number indicated on the product MB1. To look through the detailed history, use the menu
.. i18n: :menuselection:`Stock Management --> Traceability --> Production Lots`.

Now suppose that the customer phones you to tell you about a production fault in a delivered
product. You can consult the traceability through the whole manufacturing chain using the
serial number indicated on the product MB1. To look through the detailed history, use the menu
:menuselection:`Stock Management --> Traceability --> Production Lots`.

.. i18n: Find the product corresponding to the product or lot number. Once it's been found you can use
.. i18n: traceability as described in the section :ref:`sect-lotmgt` in the :ref:`ch-stocks` chapter.

Find the product corresponding to the product or lot number. Once it's been found you can use
traceability as described in the section :ref:`sect-lotmgt` in the :ref:`ch-stocks` chapter.

.. i18n: .. index:: 
.. i18n:    single: manufacturing order
.. i18n:    single: production order
.. i18n:    single: order; manufacturing
.. i18n:    single: order; production

.. index:: 
   single: manufacturing order
   single: production order
   single: order; manufacturing
   single: order; production

.. i18n: Production order in detail
.. i18n: ===========================

Production order in detail
===========================

.. i18n: To open a Production Order, use the menu
.. i18n: :menuselection:`Manufacturing --> Production Orders --> New Production Order`. You get a blank form for
.. i18n: entering a new production order as shown in the figure :ref:`fig-mrpprdnew`.

To open a Production Order, use the menu
:menuselection:`Manufacturing --> Production Orders --> New Production Order`. You get a blank form for
entering a new production order as shown in the figure :ref:`fig-mrpprdnew`.

.. i18n: .. _fig-mrpprdnew:
.. i18n: 
.. i18n: .. figure:: images/mrp_production_new.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *New production order*

.. _fig-mrpprdnew:

.. figure:: images/mrp_production_new.png
   :scale: 75
   :align: center

   *New production order*

.. i18n: The production order follows the process given by the figure :ref:`fig-mrpprdproc`.

The production order follows the process given by the figure :ref:`fig-mrpprdproc`.

.. i18n: .. _fig-mrpprdproc:
.. i18n: 
.. i18n: .. figure:: images/mrp_production_processus.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Process for handling a production order*

.. _fig-mrpprdproc:

.. figure:: images/mrp_production_processus.png
   :scale: 75
   :align: center

   *Process for handling a production order*

.. i18n: The date fields, priority and reference, are automatically completed when the form is first opened.
.. i18n: Enter the product that you want to produce, and the quantity required. The :guilabel:`Product UOM` by
.. i18n: default is completed automatically by Open ERP when the product is first created.

The date fields, priority and reference, are automatically completed when the form is first opened.
Enter the product that you want to produce, and the quantity required. The :guilabel:`Product UOM` by
default is completed automatically by Open ERP when the product is first created.

.. i18n: You then have to set two locations:

You then have to set two locations:

.. i18n: The location from which the required raw materials should be found, and

The location from which the required raw materials should be found, and

.. i18n: The location for depositing the finished products.

The location for depositing the finished products.

.. i18n: For simplicity, put the ``Stock`` location in both places. The field :guilabel:`Bill of Materials` will
.. i18n: automatically be completed by Open ERP when you click the button :guilabel:`Compute Data`. You
.. i18n: can then overwrite it with another BoM to specify something else to use for this specific
.. i18n: manufacture.

For simplicity, put the ``Stock`` location in both places. The field :guilabel:`Bill of Materials` will
automatically be completed by Open ERP when you click the button :guilabel:`Compute Data`. You
can then overwrite it with another BoM to specify something else to use for this specific
manufacture.

.. i18n: The tabs :guilabel:`Planned Products` and :guilabel:`Work Orders` are also completed automatically when you click
.. i18n: :guilabel:`Compute Data`. You'll find the raw materials there that are required for
.. i18n: the production and the operations needed by the assembly staff.

The tabs :guilabel:`Planned Products` and :guilabel:`Work Orders` are also completed automatically when you click
:guilabel:`Compute Data`. You'll find the raw materials there that are required for
the production and the operations needed by the assembly staff.

.. i18n: If you want to start production, click the button :guilabel:`Confirm Production`, and Open ERP then
.. i18n: automatically completes the :guilabel:`Moves` fields in the :guilabel:`Consumed Products` and
.. i18n: :guilabel:`Finished Products` fields. 
.. i18n: The information in the :guilabel:`Consumed Products` tab can be changed if:

If you want to start production, click the button :guilabel:`Confirm Production`, and Open ERP then
automatically completes the :guilabel:`Moves` fields in the :guilabel:`Consumed Products` and
:guilabel:`Finished Products` fields. 
The information in the :guilabel:`Consumed Products` tab can be changed if:

.. i18n: * you want to enter a serial number for raw materials,
.. i18n: 
.. i18n: * you want to change the quantities consumed (lost during production).

* you want to enter a serial number for raw materials,

* you want to change the quantities consumed (lost during production).

.. i18n: For traceability you can set lot numbers on the raw materials used, or on the finished
.. i18n: products. To do this click on one of the lines of the first or the third tab. 
.. i18n: Note the :guilabel:`Production lot` and :guilabel:`Tracking lot` numbers.

For traceability you can set lot numbers on the raw materials used, or on the finished
products. To do this click on one of the lines of the first or the third tab. 
Note the :guilabel:`Production lot` and :guilabel:`Tracking lot` numbers.

.. i18n: Once the order is confirmed, you should force the reservation of materials
.. i18n: using the :guilabel:`Force Reservation` button. This means that you don't have
.. i18n: to wait for the scheduler to assign and reserve the raw materials from your stock for this
.. i18n: production run. This shortcuts the procurement process. 

Once the order is confirmed, you should force the reservation of materials
using the :guilabel:`Force Reservation` button. This means that you don't have
to wait for the scheduler to assign and reserve the raw materials from your stock for this
production run. This shortcuts the procurement process. 

.. i18n: If you don't want to change the priorities, just
.. i18n: leave the production order in this state and the scheduler will create a plan based on the priority
.. i18n: and your planned date.

If you don't want to change the priorities, just
leave the production order in this state and the scheduler will create a plan based on the priority
and your planned date.

.. i18n: .. todo:: Report that State is not shown on a Production Order

.. todo:: Report that State is not shown on a Production Order

.. i18n: To start the production of products, click :guilabel:`Start Production`. The raw materials are then
.. i18n: consumed automatically from stock, which means that the draft ( ``Waiting`` ) movements become ``Done`` .

To start the production of products, click :guilabel:`Start Production`. The raw materials are then
consumed automatically from stock, which means that the draft ( ``Waiting`` ) movements become ``Done`` .

.. i18n: Once the production is complete, click :guilabel:`Production Finished`. The finished products are
.. i18n: then moved into stock.

Once the production is complete, click :guilabel:`Production Finished`. The finished products are
then moved into stock.

.. i18n: .. index:: 
.. i18n:    single: scheduler
.. i18n:    single: requirements planning

.. index:: 
   single: scheduler
   single: requirements planning

.. i18n: Scheduling
.. i18n: ===========

Scheduling
===========

.. i18n: The requirements scheduler is the calculation engine which plans and prioritises production
.. i18n: and purchasing automatically from the rules defined on these products. It's started once
.. i18n: per day. You can also start it manually using the menu :menuselection:`Manufacturing --> Compute All
.. i18n: Schedulers`. This uses all the relevant parameters defined in the products, the suppliers and the company
.. i18n: to determine the priorities between the different production orders, deliveries and supplier
.. i18n: purchases.

The requirements scheduler is the calculation engine which plans and prioritises production
and purchasing automatically from the rules defined on these products. It's started once
per day. You can also start it manually using the menu :menuselection:`Manufacturing --> Compute All
Schedulers`. This uses all the relevant parameters defined in the products, the suppliers and the company
to determine the priorities between the different production orders, deliveries and supplier
purchases.

.. i18n: You can set the starting time by modifying the corresponding action in the menu
.. i18n: :menuselection:`Administration --> Configuration --> Scheduler --> Scheduled Actions`. Modify the
.. i18n: ``Run MRP Scheduler`` configuration document.

You can set the starting time by modifying the corresponding action in the menu
:menuselection:`Administration --> Configuration --> Scheduler --> Scheduled Actions`. Modify the
``Run MRP Scheduler`` configuration document.

.. i18n: .. figure:: images/stock_cron.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Configuring the start time for calculating requirements*

.. figure:: images/stock_cron.png
   :scale: 75
   :align: center

   *Configuring the start time for calculating requirements*

.. i18n: .. tip::  Calculating requirements / scheduling
.. i18n: 
.. i18n:     Scheduling only validates procurement confirmed but not started. These procurement reservations
.. i18n:     will themselves start production, tasks or purchases depending on the configuration of the
.. i18n:     requested product.

.. tip::  Calculating requirements / scheduling

    Scheduling only validates procurement confirmed but not started. These procurement reservations
    will themselves start production, tasks or purchases depending on the configuration of the
    requested product.

.. i18n: You take account of the priority of operations in starting reservations and procurement.
.. i18n: The urgent requests, or those with a date in the past, or those with a date earlier than the others will be
.. i18n: started first so that if there are not enough products in stock to satisfy all the requests, the
.. i18n: most urgent will be produced first.

You take account of the priority of operations in starting reservations and procurement.
The urgent requests, or those with a date in the past, or those with a date earlier than the others will be
started first so that if there are not enough products in stock to satisfy all the requests, the
most urgent will be produced first.

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
