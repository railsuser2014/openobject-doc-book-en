
.. i18n: .. module:: sale_delivery
.. i18n:     :synopsis: Sale Delivery Planning 
.. i18n:     :noindex:
.. i18n: .. 

.. module:: sale_delivery
    :synopsis: Sale Delivery Planning 
    :noindex:
.. 

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. i18n: Sale Delivery Planning (*sale_delivery*)
.. i18n: ========================================
.. i18n: :Module: sale_delivery
.. i18n: :Name: Sale Delivery Planning
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: sale_delivery
.. i18n: :Web: 
.. i18n: :Official module: no
.. i18n: :Quality certified: no

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

.. i18n: Description
.. i18n: -----------

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   None

::

  None

.. i18n: Dependencies
.. i18n: ------------

Dependencies
------------

.. i18n:  * :mod:`sale`

 * :mod:`sale`

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

.. i18n:  * \* INHERIT sale.delivery.form.inherit (form)
.. i18n:  * \* INHERIT sale.delivery.form.inherit (form)
.. i18n:  * \* INHERIT sale.order.line.form1 (tree)

 * \* INHERIT sale.delivery.form.inherit (form)
 * \* INHERIT sale.delivery.form.inherit (form)
 * \* INHERIT sale.order.line.form1 (tree)

.. i18n: Objects
.. i18n: -------

Objects
-------

.. i18n: Object: sale.delivery.line (sale.delivery.line)
.. i18n: ###############################################

Object: sale.delivery.line (sale.delivery.line)
###############################################

.. i18n: :note: Note, text

:note: Note, text

.. i18n: :product_id: Product, many2one, required

:product_id: Product, many2one, required

.. i18n: :product_uom: Product UoM, many2one, required

:product_uom: Product UoM, many2one, required

.. i18n: :date_planned: Date Planned, datetime, required

:date_planned: Date Planned, datetime, required

.. i18n: :order_id: Order Ref, many2one, required

:order_id: Order Ref, many2one, required

.. i18n: :product_qty: Product Quantity, float, required

:product_qty: Product Quantity, float, required

.. i18n: :priority: Priority, integer

:priority: Priority, integer

.. i18n: :packaging_id: Packaging, many2one

:packaging_id: Packaging, many2one

.. i18n: :margin: Margin, float, readonly

:margin: Margin, float, readonly
