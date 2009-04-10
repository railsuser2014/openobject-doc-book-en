
.. i18n: .. module:: mrp_subproduct
.. i18n:     :synopsis: MRP Sub Product (Official, Quality Certified)
.. i18n:     :noindex:
.. i18n: .. 

.. module:: mrp_subproduct
    :synopsis: MRP Sub Product (Official, Quality Certified)
    :noindex:
.. 

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. i18n: MRP Sub Product (*mrp_subproduct*)
.. i18n: ==================================
.. i18n: :Module: mrp_subproduct
.. i18n: :Name: MRP Sub Product
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: mrp_subproduct
.. i18n: :Web: http://www.openerp.com
.. i18n: :Official module: yes
.. i18n: :Quality certified: yes

MRP Sub Product (*mrp_subproduct*)
==================================
:Module: mrp_subproduct
:Name: MRP Sub Product
:Version: 5.0.1.0
:Author: Tiny
:Directory: mrp_subproduct
:Web: http://www.openerp.com
:Official module: yes
:Quality certified: yes

.. i18n: Description
.. i18n: -----------

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   This module allows you to produce several products from one production order.
.. i18n:   You can configure sub-products in the bill of material.
.. i18n:   Without this module:
.. i18n:       A + B + C -> D
.. i18n:   With this module:
.. i18n:       A + B + C -> D + E

::

  This module allows you to produce several products from one production order.
  You can configure sub-products in the bill of material.
  Without this module:
      A + B + C -> D
  With this module:
      A + B + C -> D + E

.. i18n: Dependencies
.. i18n: ------------

Dependencies
------------

.. i18n:  * :mod:`base`
.. i18n:  * :mod:`mrp`

 * :mod:`base`
 * :mod:`mrp`

.. i18n: Reports
.. i18n: -------

Reports
-------

.. i18n: None

None

.. i18n: Menus
.. i18n: -------

Menus
-------

.. i18n: None

None

.. i18n: Views
.. i18n: -----

Views
-----

.. i18n:  * \* INHERIT mrp.bom.sub.product (form)

 * \* INHERIT mrp.bom.sub.product (form)

.. i18n: Objects
.. i18n: -------

Objects
-------

.. i18n: Object: Mrp Sub Product (mrp.subproduct)
.. i18n: ########################################

Object: Mrp Sub Product (mrp.subproduct)
########################################

.. i18n: :bom_id: BoM, many2one

:bom_id: BoM, many2one

.. i18n: :product_id: Product, many2one, required

:product_id: Product, many2one, required

.. i18n: :product_uom: Product UOM, many2one, required

:product_uom: Product UOM, many2one, required

.. i18n: :product_qty: Product Qty, float, required

:product_qty: Product Qty, float, required
