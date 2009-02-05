
.. module:: product_lot_foundry
    :synopsis: Products Lot Foundry
    :noindex:
.. 

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

Products Lot Foundry (*product_lot_foundry*)
============================================
:Module: product_lot_foundry
:Name: Products Lot Foundry
:Version: 5.0.1.0
:Directory: product_lot_foundry
:Web: 
:Is certified: no

Description
-----------

::

  Lots management for a metal company: cutting, heatcode, sizes

Dependencies
------------

 * :mod:`base`
 * :mod:`account`
 * :mod:`product`
 * :mod:`stock`
 * :mod:`sale`

Reports
-------

None


Menus
-------

 * Inventory Control
 * Inventory Control/Heat Codes
 * Inventory Control/Heat Codes/Draft Heat Codes

Views
-----

 * \* INHERIT stock.production.lot.foundry.tree (tree)
 * \* INHERIT stock.production.lot.form (form)
 * product.lot.foundry.heatcode.tree (tree)
 * product.lot.foundry.heatcode.form (form)
 * \* INHERIT product.normal.form (form)
 * sale.order.form (form)


Objects
-------

Object: Heat Code (product.lot.foundry.heatcode)
################################################



:name: Heat Code, char, required





:lot_ids: Lots, one2many





:mecanical_ids: Mecanical Properties, one2many





:state: State, selection, required





:date: Date, date, required





:chemical_ids: Chemical Properties, one2many




Object: Mecanical Properties (product.lot.foundry.heatcode.mecanical)
#####################################################################



:heatcode_id: Heatcode, many2one





:name: Property, char, required





:value: Value, char, required




Object: Chemical Properties (product.lot.foundry.heatcode.chemical)
###################################################################



:heatcode_id: Heatcode, many2one





:name: Property, char, required





:value: Value, char, required




Object: stock.production.lot.reservation (stock.production.lot.reservation)
###########################################################################



:name: Reservation, char





:size_x: Width, float





:size_y: Length, float





:size_z: Thickness, float





:date: Date, date





:lot_id: Lot, many2one, required




Object: stock.production.lot.all (stock.production.lot.all)
###########################################################



:lot_id: Lot, many2one





:name: Quantity, float


