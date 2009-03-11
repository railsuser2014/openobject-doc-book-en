
.. module:: stock_no_autopicking
    :synopsis: Stock No Auto-Picking (Official, Quality Certified)
    :noindex:
.. 

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

Stock No Auto-Picking (*stock_no_autopicking*)
==============================================
:Module: stock_no_autopicking
:Name: Stock No Auto-Picking
:Version: 5.0.1.0
:Author: Tiny
:Directory: stock_no_autopicking
:Web: 
:Official module: yes
:Quality certified: yes

Description
-----------

::

  This module allows an intermediate picking process to provide raw materials to production orders.
  
  One example of usage of this module is to manage production made by your suppliers (sub-contracting). 
  To achieve this, set the assembled productwhich is sub-contracted to "No Auto-Picking" and put the 
  location of the supplier in the routing of the assembly operation.

Dependencies
------------

 * :mod:`mrp`

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
