
Stock No Auto-Picking (*stock_no_autopicking*)
==============================================
:Module: stock_no_autopicking
:Name: Stock No Auto-Picking
:Version: 5.0.1.0
:Directory: stock_no_autopicking
:Web: 

Description
-----------

::

  This module allows an intermediate picking process to provide raw materials
      to production orders.
  
      One example of usage of this module is to manage production made by your
      suppliers (sub-contracting). To achieve this, set the assembled product
      which is sub-contracted to "No Auto-Picking" and put the location of the
      supplier in the routing of the assembly operation.

Dependencies
------------

 * mrp - installed

Reports
-------

None


Menus
-------


None


Views
-----

 * \* INHERIT product.normal.auto_pick.form (form)


Objects
-------

None
