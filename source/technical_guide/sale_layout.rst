
.. module:: sale_layout
    :synopsis: sale_layout 
    :noindex:
.. 

.. tip:: This module is part of the Open ERP software, the leading Open Source 
  enterprise management system. If you want to discover Open ERP, check our 
  `screencasts <href="http://openerp.tv>`_ or download 
  `Open ERP <href="http://openerp.com>`_ directly.

.. raw:: html

      <br />
    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

sale_layout (*sale_layout*)
===========================
:Module: sale_layout
:Name: sale_layout
:Version: 5.0.1.0
:Author: Tiny
:Directory: sale_layout
:Web: http://www.openerp.com
:Official module: no
:Quality certified: no

Description
-----------

::

  This module provides some features to improve the layout of the Sale Order.
  
      It gives you the possibility to
          * order all the lines of an sale order
          * add titles, comment lines, sub total lines
          * draw horizontal lines and put page breaks

Download links
--------------

You can download this module as a zip file in the following version:

  * `trunk </download/modules/trunk/sale_layout.zip>`_


Dependencies
------------

 * :mod:`base`
 * :mod:`sale`

Reports
-------

 * Order with Layout

Menus
-------


None


Views
-----

 * \* INHERIT sale.order.line.form2.inherit_1 (form)
 * \* INHERIT sale.order.line.tree.inherit_1 (tree)
 * \* INHERIT sale.order.form.inherit_1 (form)


Objects
-------

None
