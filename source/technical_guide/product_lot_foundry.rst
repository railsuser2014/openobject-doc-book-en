
Module Products Lot Foundry (*product_lot_foundry*)
===================================================
:Module: product_lot_foundry
:Name: Products Lot Foundry
:Version: 5.0.1.0
:Directory: product_lot_foundry
:Web: 

Description
-----------

::

  Lots management for a metal company: cutting, heatcode, sizes

Dependencies
------------

 * base - installed
 * account - installed
 * product - installed
 * stock - installed
 * sale - installed

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

Object: Heat Code
#################

.. index::
  single: Heat Code object
.. 


:name: Heat Code, char, required



.. index::
  single: name field
.. 




:lot_ids: Lots, one2many



.. index::
  single: lot_ids field
.. 




:mecanical_ids: Mecanical Properties, one2many



.. index::
  single: mecanical_ids field
.. 




:state: State, selection, required



.. index::
  single: state field
.. 




:date: Date, date, required



.. index::
  single: date field
.. 




:chemical_ids: Chemical Properties, one2many



.. index::
  single: chemical_ids field
.. 



Object: Mecanical Properties
############################

.. index::
  single: Mecanical Properties object
.. 


:heatcode_id: Heatcode, many2one



.. index::
  single: heatcode_id field
.. 




:name: Property, char, required



.. index::
  single: name field
.. 




:value: Value, char, required



.. index::
  single: value field
.. 



Object: Chemical Properties
###########################

.. index::
  single: Chemical Properties object
.. 


:heatcode_id: Heatcode, many2one



.. index::
  single: heatcode_id field
.. 




:name: Property, char, required



.. index::
  single: name field
.. 




:value: Value, char, required



.. index::
  single: value field
.. 



Object: stock.production.lot.reservation
########################################

.. index::
  single: stock.production.lot.reservation object
.. 


:name: Reservation, char



.. index::
  single: name field
.. 




:size_x: Width, float



.. index::
  single: size_x field
.. 




:size_y: Length, float



.. index::
  single: size_y field
.. 




:size_z: Thickness, float



.. index::
  single: size_z field
.. 




:date: Date, date



.. index::
  single: date field
.. 




:lot_id: Lot, many2one, required



.. index::
  single: lot_id field
.. 



Object: stock.production.lot.all
################################

.. index::
  single: stock.production.lot.all object
.. 


:lot_id: Lot, many2one



.. index::
  single: lot_id field
.. 




:name: Quantity, float



.. index::
  single: name field
.. 

