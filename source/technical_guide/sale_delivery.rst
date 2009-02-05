
.. module:: sale_delivery
    :synopsis: Sale Delivery Planning
    :noindex:
.. 

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

Sale Delivery Planning (*sale_delivery*)
========================================
:Module: sale_delivery
:Name: Sale Delivery Planning
:Version: 5.0.1.0
:Directory: sale_delivery
:Web: 
:Is certified: no

Description
-----------

::

  None

Dependencies
------------

 * :mod:`sale`

Reports
-------

None


Menus
-------


None


Views
-----

 * \* INHERIT sale.delivery.form.inherit (form)
 * \* INHERIT sale.delivery.form.inherit (form)
 * \* INHERIT sale.order.line.form1 (tree)


Objects
-------

Object: sale.delivery.line (sale.delivery.line)
###############################################



:note: Note, text





:product_id: Product, many2one, required





:product_uom: Product UoM, many2one, required





:date_planned: Date Planned, datetime, required





:order_id: Order Ref, many2one, required





:product_qty: Product Quantity, float, required





:priority: Priority, integer





:packaging_id: Packaging, many2one





:margin: Margin, float, readonly


