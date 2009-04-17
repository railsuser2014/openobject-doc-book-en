
.. module:: product_expiry
    :synopsis: Products date of expiry 
    :noindex:
.. 

.. raw:: html

      <br />
    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. tip:: This module is part of the Open ERP software, the leading Open Source 
  enterprise management system. If you want to discover Open ERP, check our 
  `screencasts <href="http://openerp.tv>`_ or download 
  `Open ERP <href="http://openerp.com>`_ directly.

Products date of expiry (*product_expiry*)
==========================================
:Module: product_expiry
:Name: Products date of expiry
:Version: 5.0.1.0
:Author: Tiny
:Directory: product_expiry
:Web: 
:Official module: no
:Quality certified: no

Description
-----------

::

  Track different dates on products and lots. Used, for exampel, in food industries: expiry date, alert date, date of removal, eso.

Download links
--------------

You can download this module as a zip file in the following version:

  * `trunk </download/modules/trunk/product_expiry.zip>`_


Dependencies
------------

 * :mod:`base`
 * :mod:`account`
 * :mod:`product`
 * :mod:`stock`

Reports
-------

None


Menus
-------


None


Views
-----

 * \* INHERIT stock.production.lot.form (form)
 * \* INHERIT product.normal.form (form)


Objects
-------

None
