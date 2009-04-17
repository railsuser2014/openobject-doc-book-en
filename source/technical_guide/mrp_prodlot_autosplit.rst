
.. module:: mrp_prodlot_autosplit
    :synopsis: Unique serial number management management:  
    :noindex:
.. 

.. tip:: This module is part of the Open ERP software, the leading Open Source 
  enterprise management system. If you want to discover Open ERP, check our 
  `screencasts <href="http://openerp.tv>`_ or download 
  `Open ERP <href="http://openerp.com>`_ directly.

.. raw:: html

      <br />
    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

Unique serial number management management:  (*mrp_prodlot_autosplit*)
======================================================================
:Module: mrp_prodlot_autosplit
:Name: Unique serial number management management: 
:Version: 5.0.0.9.0
:Author: Raphaël Valyi
:Directory: mrp_prodlot_autosplit
:Web: http://rvalyi.blogspot.com
:Official module: no
:Quality certified: no

Description
-----------

::

  Turn production lot tracking into unique per product instance code. Moreover, it
      1) adds a new checkbox on the product form to enable or disable this behavior
      2) then forbids to perform a move if a move involves more than one product instance
      3) automagically splits up picking list movements into one movement per product instance
      4) turns incoming pickings into an editable grid where you can directly type the code
      of a new production number/code to create and associate to the move (it also checks it
      doesn't exist yet)
      
      Notice: this module doesn't split product nomemclatures in MRP since they don't use pickings
      A good workaround is too define several lines of individual products in nomemclatures
      and produce 1 by 1 (if possible) to make it easier to encore unique prodlot in production orders too.

Download links
--------------

You can download this module as a zip file in the following version:

  * `trunk </download/modules/trunk/mrp_prodlot_autosplit.zip>`_


Dependencies
------------

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

 * \* INHERIT product.normal.stock.form.unique_production_number.inherit (form)
 * \* INHERIT view.picking.in.form.unique_production_number (form)
 * \* INHERIT view_production_lot_form_unique_production_number (form)


Objects
-------

None
