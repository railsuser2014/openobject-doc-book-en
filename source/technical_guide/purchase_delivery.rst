
.. module:: purchase_delivery
    :synopsis: Carriers and deliveries For Purchase Order 
    :noindex:
.. 

.. raw:: html

      <br />
    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. tip:: This module is part of the Open ERP software, the leading Open Source 
  enterprise management system. If you want to discover Open ERP, check our 
  `screencasts <href="http://openerp.tv>`_ or download 
  `Open ERP <href="http://openerp.com>`_ directly.

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="purchase_delivery"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Carriers and deliveries For Purchase Order (*purchase_delivery*)
================================================================
:Module: purchase_delivery
:Name: Carriers and deliveries For Purchase Order
:Version: 5.0.1.0
:Author: Tiny
:Directory: purchase_delivery
:Web: 
:Official module: no
:Quality certified: no

Description
-----------

::

  Allows to add delivery methods in purchase order and packings. You can define your own carrier and delivery grids for prices. When creating invoices from pickings, Tiny ERP is able to add and compute the shipping line.

Download links
--------------

You can download this module as a zip file in the following version:

  * `trunk </download/modules/trunk/purchase_delivery.zip>`_


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
