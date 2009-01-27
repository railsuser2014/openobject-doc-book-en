
Module MRP Sub Product (*mrp_subproduct*)
=========================================
:Module: mrp_subproduct
:Name: MRP Sub Product
:Version: 5.0.1.0
:Directory: mrp_subproduct
:Web: http://www.openerp.com

Description
-----------

::

  This module allows you to produce several products from one production order.
  You can configure sub-products in the bill of material.
  Without this module:
      A + B + C -> D
  With this module:
      A + B + C -> D + E

Dependencies
------------

 * base - installed
 * mrp - installed

Reports
-------

None


Menus
-------


None


Views
-----

 * \* INHERIT mrp.bom.sub.product (form)


Objects
-------

Object: Mrp Sub Product
#######################

.. index::
  single: Mrp Sub Product object
.. 


:bom_id: BoM, many2one



.. index::
  single: bom_id field
.. 




:product_id: Product, many2one, required



.. index::
  single: product_id field
.. 




:product_uom: Product UOM, many2one, required



.. index::
  single: product_uom field
.. 




:product_qty: Product Qty, float, required



.. index::
  single: product_qty field
.. 

