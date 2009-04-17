
.. module:: sale_delivery
    :synopsis: Sale Delivery Planning 
    :noindex:
.. 

.. tip:: This module is part of the Open ERP software, the leading Open Source 
  enterprise management system. If you want to discover Open ERP, check our 
  `screencasts <href="http://openerp.tv>`_ or download 
  `Open ERP <href="http://openerp.com>`_ directly.

.. raw:: html

      <br />
    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

Sale Delivery Planning (*sale_delivery*)
========================================
:Module: sale_delivery
:Name: Sale Delivery Planning
:Version: 5.0.1.0
:Author: Tiny
:Directory: sale_delivery
:Web: 
:Official module: no
:Quality certified: no

Description
-----------

::

  None

Download links
--------------

You can download this module as a zip file in the following version:

  * `4.2 </download/modules/4.2/sale_delivery.zip>`_
  * `trunk </download/modules/trunk/sale_delivery.zip>`_


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


