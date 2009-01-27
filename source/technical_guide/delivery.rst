
Module Carriers and deliveries (*delivery*)
===========================================
:Module: delivery
:Name: Carriers and deliveries
:Version: 5.0.1.0
:Directory: delivery
:Web: 

Description
-----------

::

  Allows to add delivery methods in sales order and packing. You can define your own carrier and delivery grids for prices. When creating invoices from pickings, Open ERP is able to add and compute the shipping line.

Dependencies
------------

 * sale - installed
 * purchase - installed
 * stock - installed

Reports
-------

None


Menus
-------

 * Stock Management/Configuration/Delivery
 * Stock Management/Configuration/Delivery/Delivery Method
 * Stock Management/Configuration/Delivery/Delivery Pricelist
 * Stock Management/Outgoing Products/Packings to be invoiced
 * Stock Management/Incoming Products/Generate Draft Invoices On Receptions

Views
-----

 * delivery.carrier.tree (tree)
 * delivery.carrier.form (form)
 * delivery.grid.tree (tree)
 * delivery.grid.form (form)
 * delivery.grid.line.form (form)
 * delivery.grid.line.tree (tree)
 * \* INHERIT delivery.sale.order_withcarrier.form.view (form)
 * \* INHERIT delivery.stock.picking_withcarrier.out.form.view (form)
 * \* INHERIT delivery.stock.picking_withcarrier.delivery.form.view (form)
 * \* INHERIT res.partner.carrier.property.form.inherit (form)


Objects
-------

Object: Carrier and delivery grids
##################################

.. index::
  single: Carrier and delivery grids object
.. 


:product_id: Delivery Product, many2one, required



.. index::
  single: product_id field
.. 




:price: Price, float, readonly



.. index::
  single: price field
.. 




:grids_id: Delivery Grids, one2many



.. index::
  single: grids_id field
.. 




:active: Active, boolean



.. index::
  single: active field
.. 




:partner_id: Carrier Partner, many2one, required



.. index::
  single: partner_id field
.. 




:name: Carrier, char, required



.. index::
  single: name field
.. 



Object: Delivery Grid
#####################

.. index::
  single: Delivery Grid object
.. 


:name: Grid Name, char, required



.. index::
  single: name field
.. 




:sequence: Sequence, integer, required



.. index::
  single: sequence field
.. 




:state_ids: States, many2many



.. index::
  single: state_ids field
.. 




:country_ids: Countries, many2many



.. index::
  single: country_ids field
.. 




:carrier_id: Carrier, many2one, required



.. index::
  single: carrier_id field
.. 




:active: Active, boolean



.. index::
  single: active field
.. 




:zip_from: Start Zip, char



.. index::
  single: zip_from field
.. 




:line_ids: Grid Line, one2many



.. index::
  single: line_ids field
.. 




:zip_to: To Zip, char



.. index::
  single: zip_to field
.. 



Object: Delivery line of grid
#############################

.. index::
  single: Delivery line of grid object
.. 


:list_price: Sale Price, float, required



.. index::
  single: list_price field
.. 




:name: Name, char, required



.. index::
  single: name field
.. 




:price_type: Price Type, selection, required



.. index::
  single: price_type field
.. 




:max_value: Maximum Value, float, required



.. index::
  single: max_value field
.. 




:standard_price: Cost Price, float, required



.. index::
  single: standard_price field
.. 




:grid_id: Grid, many2one, required



.. index::
  single: grid_id field
.. 




:variable_factor: Variable Factor, selection, required



.. index::
  single: variable_factor field
.. 




:operator: Operator, selection, required



.. index::
  single: operator field
.. 




:type: Variable, selection, required



.. index::
  single: type field
.. 

