
Carriers and deliveries (*delivery*)
====================================
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



:product_id: Delivery Product, many2one, required





:price: Price, float, readonly





:grids_id: Delivery Grids, one2many





:active: Active, boolean





:partner_id: Carrier Partner, many2one, required





:name: Carrier, char, required




Object: Delivery Grid
#####################



:name: Grid Name, char, required





:sequence: Sequence, integer, required





:state_ids: States, many2many





:country_ids: Countries, many2many





:carrier_id: Carrier, many2one, required





:active: Active, boolean





:zip_from: Start Zip, char





:line_ids: Grid Line, one2many





:zip_to: To Zip, char




Object: Delivery line of grid
#############################



:list_price: Sale Price, float, required





:name: Name, char, required





:price_type: Price Type, selection, required





:max_value: Maximum Value, float, required





:standard_price: Cost Price, float, required





:grid_id: Grid, many2one, required





:variable_factor: Variable Factor, selection, required





:operator: Operator, selection, required





:type: Variable, selection, required


