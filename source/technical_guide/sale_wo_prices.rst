
.. module:: sale_wo_prices
    :synopsis: Sales without prices 
    :noindex:
.. 

.. tip:: This module is part of the Open ERP software, the leading Open Source 
  enterprise management system. If you want to discover Open ERP, check our 
  `screencasts <href="http://openerp.tv>`_ or download 
  `Open ERP <href="http://openerp.com>`_ directly.

.. raw:: html

      <br />
    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

Sales without prices (*sale_wo_prices*)
=======================================
:Module: sale_wo_prices
:Name: Sales without prices
:Version: 5.0.1.0
:Author: Zikzakmedia SL
:Directory: sale_wo_prices
:Web: www.zikzakmedia.com
:Official module: no
:Quality certified: no

Description
-----------

::

  Hides prices in sales and product forms. Only sale manager can see them. Normal salesmen can do sales without seeing the product prices.

Download links
--------------

You can download this module as a zip file in the following version:

  * `trunk </download/modules/trunk/sale_wo_prices.zip>`_


Dependencies
------------

 * :mod:`sale`
 * :mod:`product`

Reports
-------

None


Menus
-------


None


Views
-----

 * \* INHERIT product.normal.form.wop1 (form)
 * \* INHERIT product.product.tree.wop1 (tree)
 * \* INHERIT product.product.tree.wop2 (tree)
 * \* INHERIT product.product.tree.wop3 (tree)
 * \* INHERIT sale.order.form.wop1 (form)
 * \* INHERIT sale.order.form.wop2 (form)
 * \* INHERIT sale.order.form.wop3 (form)
 * \* INHERIT sale.order.form.wop4 (form)
 * \* INHERIT sale.order.form.wop5 (form)
 * \* INHERIT sale.order.form.wop6 (form)
 * \* INHERIT sale.order.tree.wop1 (tree)


Objects
-------

None
