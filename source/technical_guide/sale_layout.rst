
.. module:: sale_layout
    :synopsis: sale_layout 
    :noindex:
.. 

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

    <style>
      div.body p#module-sale_layout {
        display: none;
      }
    </style>

sale_layout (*sale_layout*)
===========================
:Module: sale_layout
:Name: sale_layout
:Version: 5.0.1.0
:Author: Tiny
:Directory: sale_layout
:Web: http://www.openerp.com
:Is certified: no

Description
-----------

::

  This module provides some features to improve the layout of the Sale Order.
  
      It gives you the possibility to
          * order all the lines of an sale order
          * add titles, comment lines, sub total lines
          * draw horizontal lines and put page breaks

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
