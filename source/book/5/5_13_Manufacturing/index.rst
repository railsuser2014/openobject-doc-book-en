Production Management
######################

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
.. raw:: html

    <div class="all-toctree">

.. toctree::

   5_13_Manufacturing_bom   
   5_13_Manufacturing_bom_multi   
   5_13_Manufacturing_manufacturing   
   5_13_Manufacturing_wf   
   5_13_Manufacturing_order   
   5_13_Manufacturing_scheduling   
   5_13_Manufacturing_operations   
   5_13_Manufacturing_scores   
   5_13_Manufacturing_subcontracting   
   5_13_Manufacturing_repairs   

.. raw:: html

    </div>
  
