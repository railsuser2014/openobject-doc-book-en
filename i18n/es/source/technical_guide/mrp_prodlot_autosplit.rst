
.. i18n: .. module:: mrp_prodlot_autosplit
.. i18n:     :synopsis: Stock Management 
.. i18n:     :noindex:
.. i18n: .. 

.. module:: mrp_prodlot_autosplit
    :synopsis: Stock Management 
    :noindex:
.. 

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. i18n: Stock Management (*mrp_prodlot_autosplit*)
.. i18n: ==========================================
.. i18n: :Module: mrp_prodlot_autosplit
.. i18n: :Name: Stock Management
.. i18n: :Version: 5.0.0.9.0
.. i18n: :Author: Raphaël Valyi
.. i18n: :Directory: mrp_prodlot_autosplit
.. i18n: :Web: http://rvalyi.blogspot.com
.. i18n: :Official module: no
.. i18n: :Quality certified: no

Stock Management (*mrp_prodlot_autosplit*)
==========================================
:Module: mrp_prodlot_autosplit
:Name: Stock Management
:Version: 5.0.0.9.0
:Author: Raphaël Valyi
:Directory: mrp_prodlot_autosplit
:Web: http://rvalyi.blogspot.com
:Official module: no
:Quality certified: no

.. i18n: Description
.. i18n: -----------

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   Turn production lot tracking into unique per product instance code. Moreover, it
.. i18n:       1) adds a new checkbox on the product form to enable or disable this behavior
.. i18n:       2) then forbids to perform a move if a move involves more than one product instance
.. i18n:       3) automagically splits up picking list movements into one movement per product instance
.. i18n:       4) turns incoming pickings into an editable grid where you can directly type the code
.. i18n:       of a new production number/code to create and associate to the move (it also checks it
.. i18n:       doesn't exist yet)
.. i18n:       
.. i18n:       Notice: this module doesn't split product nomemclatures in MRP since 
.. i18n:               they don't use pickings
.. i18n:       A good workaround is too define several lines of individual products in nomemclatures
.. i18n:       and produce 1 by 1 (if possible) to make it easier to encore unique prodlot in 
.. i18n:       production orders too.

::

  Turn production lot tracking into unique per product instance code. Moreover, it
      1) adds a new checkbox on the product form to enable or disable this behavior
      2) then forbids to perform a move if a move involves more than one product instance
      3) automagically splits up picking list movements into one movement per product instance
      4) turns incoming pickings into an editable grid where you can directly type the code
      of a new production number/code to create and associate to the move (it also checks it
      doesn't exist yet)
      
      Notice: this module doesn't split product nomemclatures in MRP since 
              they don't use pickings
      A good workaround is too define several lines of individual products in nomemclatures
      and produce 1 by 1 (if possible) to make it easier to encore unique prodlot in 
      production orders too.

.. i18n: Dependencies
.. i18n: ------------

Dependencies
------------

.. i18n:  * :mod:`product`
.. i18n:  * :mod:`stock`

 * :mod:`product`
 * :mod:`stock`

.. i18n: Reports
.. i18n: -------

Reports
-------

.. i18n: None

None

.. i18n: Menus
.. i18n: -------

Menus
-------

.. i18n: None

None

.. i18n: Views
.. i18n: -----

Views
-----

.. i18n:  * \* INHERIT product.normal.stock.form.unique_production_number.inherit (form)
.. i18n:  * \* INHERIT view.picking.in.form.unique_production_number (form)
.. i18n:  * \* INHERIT view.picking.out.form.unique_production_number
.. i18n:  * 			 (form)

 * \* INHERIT product.normal.stock.form.unique_production_number.inherit (form)
 * \* INHERIT view.picking.in.form.unique_production_number (form)
 * \* INHERIT view.picking.out.form.unique_production_number
 * 			 (form)

.. i18n: Objects
.. i18n: -------

Objects
-------

.. i18n: None

None
