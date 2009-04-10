
.. i18n: .. module:: product_lot_foundry
.. i18n:     :synopsis: Products Lot Foundry 
.. i18n:     :noindex:
.. i18n: .. 

.. module:: product_lot_foundry
    :synopsis: Products Lot Foundry 
    :noindex:
.. 

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. i18n: Products Lot Foundry (*product_lot_foundry*)
.. i18n: ============================================
.. i18n: :Module: product_lot_foundry
.. i18n: :Name: Products Lot Foundry
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: product_lot_foundry
.. i18n: :Web: 
.. i18n: :Official module: no
.. i18n: :Quality certified: no

Products Lot Foundry (*product_lot_foundry*)
============================================
:Module: product_lot_foundry
:Name: Products Lot Foundry
:Version: 5.0.1.0
:Author: Tiny
:Directory: product_lot_foundry
:Web: 
:Official module: no
:Quality certified: no

.. i18n: Description
.. i18n: -----------

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   Lots management for a metal company: cutting, heatcode, sizes

::

  Lots management for a metal company: cutting, heatcode, sizes

.. i18n: Dependencies
.. i18n: ------------

Dependencies
------------

.. i18n:  * :mod:`base`
.. i18n:  * :mod:`account`
.. i18n:  * :mod:`product`
.. i18n:  * :mod:`stock`
.. i18n:  * :mod:`sale`

 * :mod:`base`
 * :mod:`account`
 * :mod:`product`
 * :mod:`stock`
 * :mod:`sale`

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

.. i18n:  * Inventory Control
.. i18n:  * Inventory Control/Heat Codes
.. i18n:  * Inventory Control/Heat Codes/Draft Heat Codes

 * Inventory Control
 * Inventory Control/Heat Codes
 * Inventory Control/Heat Codes/Draft Heat Codes

.. i18n: Views
.. i18n: -----

Views
-----

.. i18n:  * \* INHERIT stock.production.lot.foundry.tree (tree)
.. i18n:  * \* INHERIT stock.production.lot.form (form)
.. i18n:  * product.lot.foundry.heatcode.tree (tree)
.. i18n:  * product.lot.foundry.heatcode.form (form)
.. i18n:  * \* INHERIT product.normal.form (form)
.. i18n:  * sale.order.form (form)

 * \* INHERIT stock.production.lot.foundry.tree (tree)
 * \* INHERIT stock.production.lot.form (form)
 * product.lot.foundry.heatcode.tree (tree)
 * product.lot.foundry.heatcode.form (form)
 * \* INHERIT product.normal.form (form)
 * sale.order.form (form)

.. i18n: Objects
.. i18n: -------

Objects
-------

.. i18n: Object: Heat Code (product.lot.foundry.heatcode)
.. i18n: ################################################

Object: Heat Code (product.lot.foundry.heatcode)
################################################

.. i18n: :name: Heat Code, char, required

:name: Heat Code, char, required

.. i18n: :lot_ids: Lots, one2many

:lot_ids: Lots, one2many

.. i18n: :mecanical_ids: Mecanical Properties, one2many

:mecanical_ids: Mecanical Properties, one2many

.. i18n: :state: State, selection, required

:state: State, selection, required

.. i18n: :date: Date, date, required

:date: Date, date, required

.. i18n: :chemical_ids: Chemical Properties, one2many

:chemical_ids: Chemical Properties, one2many

.. i18n: Object: Mecanical Properties (product.lot.foundry.heatcode.mecanical)
.. i18n: #####################################################################

Object: Mecanical Properties (product.lot.foundry.heatcode.mecanical)
#####################################################################

.. i18n: :heatcode_id: Heatcode, many2one

:heatcode_id: Heatcode, many2one

.. i18n: :name: Property, char, required

:name: Property, char, required

.. i18n: :value: Value, char, required

:value: Value, char, required

.. i18n: Object: Chemical Properties (product.lot.foundry.heatcode.chemical)
.. i18n: ###################################################################

Object: Chemical Properties (product.lot.foundry.heatcode.chemical)
###################################################################

.. i18n: :heatcode_id: Heatcode, many2one

:heatcode_id: Heatcode, many2one

.. i18n: :name: Property, char, required

:name: Property, char, required

.. i18n: :value: Value, char, required

:value: Value, char, required

.. i18n: Object: stock.production.lot.reservation (stock.production.lot.reservation)
.. i18n: ###########################################################################

Object: stock.production.lot.reservation (stock.production.lot.reservation)
###########################################################################

.. i18n: :name: Reservation, char

:name: Reservation, char

.. i18n: :size_x: Width, float

:size_x: Width, float

.. i18n: :size_y: Length, float

:size_y: Length, float

.. i18n: :size_z: Thickness, float

:size_z: Thickness, float

.. i18n: :date: Date, date

:date: Date, date

.. i18n: :lot_id: Lot, many2one, required

:lot_id: Lot, many2one, required

.. i18n: Object: stock.production.lot.all (stock.production.lot.all)
.. i18n: ###########################################################

Object: stock.production.lot.all (stock.production.lot.all)
###########################################################

.. i18n: :lot_id: Lot, many2one

:lot_id: Lot, many2one

.. i18n: :name: Quantity, float

:name: Quantity, float
