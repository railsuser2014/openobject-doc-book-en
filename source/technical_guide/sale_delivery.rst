
Module Sale Delivery Planning (*sale_delivery*)
===============================================
:Module: sale_delivery
:Name: Sale Delivery Planning
:Version: 5.0.1.0
:Directory: sale_delivery
:Web: 

Description
-----------

::

  None

Dependencies
------------

 * sale - installed

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

Object: sale.delivery.line
##########################

.. index::
  single: sale.delivery.line object
.. 


:note: Note, text



.. index::
  single: note field
.. 




:product_id: Product, many2one, required



.. index::
  single: product_id field
.. 




:product_uom: Product UoM, many2one, required



.. index::
  single: product_uom field
.. 




:date_planned: Date Planned, datetime, required



.. index::
  single: date_planned field
.. 




:order_id: Order Ref, many2one, required



.. index::
  single: order_id field
.. 




:product_qty: Product Quantity, float, required



.. index::
  single: product_qty field
.. 




:priority: Priority, integer



.. index::
  single: priority field
.. 




:packaging_id: Packaging, many2one



.. index::
  single: packaging_id field
.. 




:margin: Margin, float, readonly



.. index::
  single: margin field
.. 

