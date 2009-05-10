
.. module:: product_size
    :synopsis: Sizes of lots (width, length, thickness) 
    :noindex:
.. 

.. raw:: html

      <br />
    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. tip:: This module is part of the Open ERP software, the leading Open Source 
  enterprise management system. If you want to discover Open ERP, check our 
  `screencasts <http://openerp.tv>`_ or download 
  `Open ERP <http://openerp.com>`_ directly.

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/product_size"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Sizes of lots (width, length, thickness) (*product_size*)
=========================================================
:Module: product_size
:Name: Sizes of lots (width, length, thickness)
:Version: 5.0.1.0
:Author: Tiny
:Directory: product_size
:Web: 
:Official module: no
:Quality certified: no

Description
-----------

::

  Manage 3 dimensions size on lots.
  Implements demo data for a complex workflow on steel.

Download links
--------------

You can download this module as a zip file in the following version:

  * `trunk <http://www.openerp.com/download/modules/trunk/product_size.zip>`_


Dependencies
------------

 * :mod:`base`
 * :mod:`account`
 * :mod:`product`
 * :mod:`stock`
 * :mod:`mrp`
 * :mod:`sale`

Reports
-------

None


Menus
-------


None


Views
-----

 * \* INHERIT stock.production.lot.form (form)
 * \* INHERIT stock.production.lot.tree (tree)
 * \* INHERIT product.normal.form (form)


Objects
-------

None
