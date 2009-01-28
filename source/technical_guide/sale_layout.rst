
sale_layout (*sale_layout*)
===========================
:Module: sale_layout
:Name: sale_layout
:Version: 5.0.1.0
:Directory: sale_layout
:Web: http://www.openerp.com

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

 * base - installed
 * sale - installed

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
