
.. module:: purchase_delivery
    :synopsis: Carriers and deliveries For Purchase Order
    :noindex:
.. 

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

Carriers and deliveries For Purchase Order (*purchase_delivery*)
================================================================
:Module: purchase_delivery
:Name: Carriers and deliveries For Purchase Order
:Version: 5.0.1.0
:Directory: purchase_delivery
:Web: 
:Is certified: no

Description
-----------

::

  Allows to add delivery methods in purchase order and packings. You can define your own carrier and delivery grids for prices. When creating invoices from pickings, Tiny ERP is able to add and compute the shipping line.

Dependencies
------------

 * :mod:`sale`
 * :mod:`purchase`
 * :mod:`stock`
 * :mod:`delivery`

Reports
-------

None


Menus
-------


None


Views
-----

 * \* INHERIT delivery.purcahse.order_withcarrier.form.view (form)


Objects
-------

None
