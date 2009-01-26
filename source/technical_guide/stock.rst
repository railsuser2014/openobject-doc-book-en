
Module Stock Management (*stock*)
=================================
:Module: stock
:Name: Stock Management
:Version: 5.0.1.1
:Directory: stock
:Web: http://www.openerp.com

Description
-----------

::
  
    None

Reports
-------

 * Future Stock Forecast

 * Packing list

 * Print Item Labels

 * Location Overview

 * Lots by location

 * Location Content (With childs)

Menus
-------

 * Stock Management

 * Stock Management/Configuration

 * Stock Management/Periodical Inventory

 * Stock Management/Periodical Inventory/Draft Periodical Inventories

 * Stock Management/Periodical Inventory/New Periodical Inventory

 * Stock Management/Traceability

 * Stock Management/Traceability/Tracking Lots

 * Stock Management/Traceability/Production Lots

 * Stock Management/Configuration/Locations

 * Stock Management/Stock Locations Structure

 * Stock Management/Configuration/Warehouses

 * Stock Management/Delivery Orders

 * Stock Management/Delivery Orders/Delivery Orders to Process

 * Stock Management/Delivery Orders/Futur Delivery Orders

 * Stock Management/Delivery Orders/Calendar of Deliveries

 * Stock Management/Outgoing Products

 * Stock Management/Outgoing Products/Available Packings

 * Stock Management/Outgoing Products/Confirmed Packings Waiting Availability

 * Stock Management/Incoming Products

 * Stock Management/Incoming Products/Packings to Process

 * Stock Management/Incoming Products/New Reception Packing

 * Stock Management/Internal Moves

 * Stock Management/Internal Moves/Available Packings

 * Stock Management/Internal Moves/Confirmed Packings Waiting Availability

 * Stock Management/Internal Moves/New Internal Packings

 * Stock Management/Traceability/Low Level

 * Stock Management/Traceability/Low Level/Stock Moves

 * Stock Management/Traceability/Low Level/Stock Moves/Draft Moves

 * Stock Management/Traceability/Low Level/Stock Moves/Available Moves

 * Stock Management/Traceability/Low Level/Packings

 * Stock Management/Configuration/Incoterms

 * Stock Management/Reporting

 * Stock Management/Reporting/Traceability

 * Stock Management/Reporting/Traceability/Stock by Lots

 * Stock Management/Reporting/Dates of Inventories

 * Stock Management/Reporting/Locations' Values

Views
-----

 * stock.inventory.line.tree (tree)

 * stock.inventory.line.form (form)

 * stock.inventory.tree (tree)

 * stock.inventory.form (form)

 * stock.tracking.form (form)

 * stock.tracking.tree (tree)

 * stock.tracking.tree (tree)

 * stock.production.lot.revision.form (form)

 * stock.production.lot.revision.tree (tree)

 * stock.production.lot.form (form)

 * stock.production.lot.tree (tree)

 * stock.move.tree2 (tree)

 * stock.move.tree2 (tree)

 * stock.location.form (form)

 * stock.location.tree (tree)

 * stock.location.tree (tree)

 * stock.warehouse (form)

 * stock.warehouse.tree (tree)

 * stock.picking.move.wizard.form (form)

 * stock.picking.calendar (calendar)

 * stock.picking.tree (tree)

 * stock.picking.form (form)

 * stock.picking.delivery.tree (tree)

 * stock.picking.delivery.form (form)

 * stock.picking.out.tree (tree)

 * stock.picking.out.form (form)

 * stock.picking.in.tree (tree)

 * stock.picking.in.form (form)

 * stock.move.tree (tree)

 * stock.move.form (form)

 * stock.incoterms.tree (tree)

 * stock.incoterms.form (form)

 * \* INHERIT product.category.stock.property.form.inherit (form)

 * \* INHERIT product.template.stock.property.form.inherit (form)

 * \* INHERIT product.normal.stock.acc.property.form.inherit (form)

 * \* INHERIT product.normal.stock.form.inherit (form)

 * \* INHERIT product.normal.stock.property.form.inherit (form)

 * \* INHERIT res.partner.stock.property.form.inherit (form)

 * stock.report.prodlots.view (tree)

 * report.stock.lines.date.tree (tree)

 * report.stock.lines.date.form (form)

 * stock.location.tree (tree)

Dependencies
------------

 * product - installed

 * account - installed

Objects
-------

Incoterms
#########


:active: Active, boolean




:code: Code, char, required




:name: Name, char, required




Location
########


:comment: Additional Information, text




:address_id: Location Address, many2one




:stock_virtual_value: Virtual Stock Value, float, readonly




:allocation_method: Allocation Method, selection, required




:location_id: Parent Location, many2one




:chained_location_id: Chained Location If Fixed, many2one




:complete_name: Location Name, char, readonly




:usage: Location type, selection, required




:stock_real_value: Real Stock Value, float, readonly




:chained_location_type: Chained Location Type, selection, required




:account_id: Inventory Account, many2one




:child_ids: Contains, one2many




:chained_delay: Chained Delay (days), integer




:stock_virtual: Virtual Stock, float, readonly




:posz: Height (Z), integer




:posx: Corridor (X), integer




:posy: Shelves (Y), integer




:active: Active, boolean




:icon: Icon, selection




:parent_right: Right Parent, integer




:name: Location Name, char, required




:chained_auto_packing: Automatic Move, selection, required

    *This is used only if you selected a chained location type.
    The 'Automatic Move' value will create a stock move after the current one that will be validated automatically. With 'Manual Operation', the stock move has to be validated by a worker. With 'Automatic No Step Added', the location is replaced in the original move.*


:parent_left: Left Parent, integer




:stock_real: Real Stock, float, readonly




Stock Tracking Lots
###################


:active: Active, boolean




:move_ids: Moves tracked, one2many




:serial: Reference, char




:date: Date create, datetime, required




:name: Tracking, char, required




Packing list
############


:origin: Origin Reference, char




:address_id: Partner, many2one




:type: Shipping Type, selection, required




:move_lines: Move lines, one2many




:date_done: Date Done, datetime




:name: Reference, char, required




:move_type: Delivery Method, selection, required




:invoice_state: Invoice Status, selection, required, readonly




:min_date: Planned Date, datetime




:note: Notes, text




:date: Date Order, datetime




:state: Status, selection, readonly




:location_dest_id: Dest. Location, many2one




:max_date: Max. Planned Date, datetime




:auto_picking: Auto-Packing, boolean




:active: Active, boolean




:location_id: Location, many2one




:backorder_id: Back Order, many2one




Production lot
##############


:stock_available: Available, float, readonly




:product_id: Product, many2one, required




:date: Created Date, datetime, required




:revisions: Revisions, one2many




:ref: Internal Ref., char




:name: Serial, char, required




Production lot revisions
########################


:indice: Revision, char




:name: Revision name, char, required




:date: Revision date, date




:lot_id: Production lot, many2one




:author_id: Author, many2one




:description: Description, text




Stock Move
##########


:product_uos_qty: Quantity (UOS), float




:address_id: Dest. Address, many2one




:product_uom: Product UOM, many2one, required




:price_unit: Unit Price, float




:product_qty: Quantity, float, required




:product_uos: Product UOS, many2one




:location_id: Source Location, many2one, required




:priority: Priority, selection




:auto_validate: Auto Validate, boolean




:note: Notes, text




:state: Status, selection, readonly




:product_packaging: Packaging, many2one




:move_history_ids: Move History, many2many




:prodlot_id: Production lot, many2one

    *Production lot is used to put a serial number on the production*


:move_dest_id: Dest. Move, many2one




:date: Date Created, datetime




:name: Name, char, required




:move_history_ids2: Move History, many2many




:product_id: Product, many2one, required




:date_planned: Scheduled date, datetime, required




:location_dest_id: Dest. Location, many2one, required




:tracking_id: Tracking lot, many2one

    *Tracking lot is the code that will be put on the logistic unit/pallet*


:picking_id: Packing list, many2one




Inventory
#########


:name: Inventory, char, required, readonly




:date_done: Date done, datetime




:move_ids: Created Moves, many2many




:state: Status, selection, readonly




:date: Date create, datetime, required, readonly




:inventory_line_id: Inventories, one2many, readonly




Inventory line
##############


:inventory_id: Inventory, many2one




:location_id: Location, many2one, required




:product_id: Product, many2one, required




:product_uom: Product UOM, many2one, required




:product_qty: Quantity, float




Warehouse
#########


:lot_input_id: Location Input, many2one, required




:partner_address_id: Owner Address, many2one




:lot_output_id: Location Output, many2one, required




:name: Name, char, required




:lot_stock_id: Location Stock, many2one, required




stock.picking.move.wizard
#########################


:move_ids: Move lines, many2many, required




:address_id: Dest. Address, many2one




:name: Name, char




:picking_id: Packing list, many2one




Dates of Inventories
####################


:create_date: Latest Date of Inventory, datetime




:id: Inventory Line Id, integer, readonly




:product_id: Product Id, integer, readonly




Stock report by production lots
###############################


:prodlot_id: Production lot, many2one, readonly




:location_id: Location, many2one, readonly




:name: Quantity, float, readonly




:product_id: Product, many2one, readonly


