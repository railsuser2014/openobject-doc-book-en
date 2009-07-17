
.. i18n: .. module:: mrp_prodlot_autosplit
.. i18n:     :synopsis: Unique serial number management management:  
.. i18n:     :noindex:
.. i18n: .. 

.. module:: mrp_prodlot_autosplit
    :synopsis: Unique serial number management management:  
    :noindex:
.. 

.. i18n: .. raw:: html
.. i18n: 
.. i18n:       <br />
.. i18n:     <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. raw:: html

      <br />
    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. i18n: .. tip:: This module is part of the Open ERP software, the leading Open Source 
.. i18n:   enterprise management system. If you want to discover Open ERP, check our 
.. i18n:   `screencasts <http://openerp.tv>`_ or download 
.. i18n:   `Open ERP <http://openerp.com>`_ directly.

.. tip:: This module is part of the Open ERP software, the leading Open Source 
  enterprise management system. If you want to discover Open ERP, check our 
  `screencasts <http://openerp.tv>`_ or download 
  `Open ERP <http://openerp.com>`_ directly.

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/mrp_prodlot_autosplit"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/mrp_prodlot_autosplit"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Unique serial number management management:  (*mrp_prodlot_autosplit*)
.. i18n: ======================================================================
.. i18n: :Module: mrp_prodlot_autosplit
.. i18n: :Name: Unique serial number management management: 
.. i18n: :Version: 5.0.0.9.0
.. i18n: :Author: Raphaël Valyi
.. i18n: :Directory: mrp_prodlot_autosplit
.. i18n: :Web: http://rvalyi.blogspot.com
.. i18n: :Official module: no
.. i18n: :Quality certified: no

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
.. i18n:       Notice: this module doesn't split product nomemclatures in MRP since they don't use pickings
.. i18n:       A good workaround is too define several lines of individual products in nomemclatures
.. i18n:       and produce 1 by 1 (if possible) to make it easier to encore unique prodlot in production orders too.

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

.. i18n: Download links
.. i18n: --------------

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:

You can download this module as a zip file in the following version:

.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/mrp_prodlot_autosplit.zip>`_

  * `trunk <http://www.openerp.com/download/modules/trunk/mrp_prodlot_autosplit.zip>`_

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
.. i18n:  * \* INHERIT view_production_lot_form_unique_production_number (form)

 * \* INHERIT product.normal.stock.form.unique_production_number.inherit (form)
 * \* INHERIT view.picking.in.form.unique_production_number (form)
 * \* INHERIT view_production_lot_form_unique_production_number (form)

.. i18n: Objects
.. i18n: -------

Objects
-------

.. i18n: None

None
