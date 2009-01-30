
.. module:: mrp_subproduct
    :synopsis: MRP Sub Product
    :noindex:
.. 

MRP Sub Product (*mrp_subproduct*)
==================================
:Module: mrp_subproduct
:Name: MRP Sub Product
:Version: 5.0.1.0
:Directory: mrp_subproduct
:Web: http://www.openerp.com
:Is certified: yes

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

Object: Mrp Sub Product (mrp.subproduct)
########################################



:bom_id: BoM, many2one





:product_id: Product, many2one, required





:product_uom: Product UOM, many2one, required





:product_qty: Product Qty, float, required


