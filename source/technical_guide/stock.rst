
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

  OpenERP Stock Management module can manage multi-warehouses, multi and structured stock locations.
  Thanks to the double entry management, the inventory controlling is powerful and flexible:
  * Moves history and planning,
  * Different inventory methods (FIFO, LIFO, ...)
  * Stock valuation (standard or average price, ...)
  * Robustness faced with Inventory differences
  * Automatic reordering rules (stock level, JIT, ...)
  * Bar code supported
  * Rapid detection of mistakes through double entry system
  * Traceability (upstream/downstream, production lots, serial number, ...)

Dependencies
------------

 * product - installed
 * account - installed

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


Objects
-------

Object: Incoterms
#################

.. index::
  single: Incoterms object
.. 


:active: Active, boolean



.. index::
  single: active field
.. 




:code: Code, char, required



.. index::
  single: code field
.. 




:name: Name, char, required



.. index::
  single: name field
.. 



Object: Location
################

.. index::
  single: Location object
.. 


:comment: Additional Information, text



.. index::
  single: comment field
.. 




:address_id: Location Address, many2one



.. index::
  single: address_id field
.. 




:stock_virtual_value: Virtual Stock Value, float, readonly



.. index::
  single: stock_virtual_value field
.. 




:expire_time: Maintenance Expire Time, date, readonly



.. index::
  single: expire_time field
.. 




:allocation_method: Allocation Method, selection, required



.. index::
  single: allocation_method field
.. 




:partner_id: Customer, many2one



.. index::
  single: partner_id field
.. 




:fleet_account_invoice_lines: Invoice Lines, one2many



.. index::
  single: fleet_account_invoice_lines field
.. 




:location_id: Parent Location, many2one



.. index::
  single: location_id field
.. 




:parent_partner_id: Customer, many2one



.. index::
  single: parent_partner_id field
.. 




:time_to_expire: Days before expiry, integer, readonly



.. index::
  single: time_to_expire field
.. 




:complete_name: Location Name, char, readonly



.. index::
  single: complete_name field
.. 




:usage: Location type, selection, required



.. index::
  single: usage field
.. 




:stock_real_value: Real Stock Value, float, readonly



.. index::
  single: stock_real_value field
.. 




:chained_location_type: Chained Location Type, selection, required



.. index::
  single: chained_location_type field
.. 




:fleet_sale_order_lines: Sale Order Lines, one2many



.. index::
  single: fleet_sale_order_lines field
.. 




:account_invoice_lines: Invoice Lines, one2many



.. index::
  single: account_invoice_lines field
.. 




:anniversary_time: Anniversary Time, date, readonly



.. index::
  single: anniversary_time field
.. 




:account_id: Inventory Account, many2one



.. index::
  single: account_id field
.. 




:child_ids: Contains, one2many



.. index::
  single: child_ids field
.. 




:chained_delay: Chained Delay (days), integer



.. index::
  single: chained_delay field
.. 




:stock_virtual: Virtual Stock, float, readonly



.. index::
  single: stock_virtual field
.. 




:sale_order_lines: Sale Order Lines, one2many



.. index::
  single: sale_order_lines field
.. 




:posz: Height (Z), integer



.. index::
  single: posz field
.. 




:posx: Corridor (X), integer



.. index::
  single: posx field
.. 




:posy: Shelves (Y), integer



.. index::
  single: posy field
.. 




:active: Active, boolean



.. index::
  single: active field
.. 




:icon: Icon, selection



.. index::
  single: icon field
.. 




:parent_right: Right Parent, integer



.. index::
  single: parent_right field
.. 




:fleet_crm_cases: Events, one2many



.. index::
  single: fleet_crm_cases field
.. 




:name: Location Name, char, required



.. index::
  single: name field
.. 




:intrinsic_anniversary_time: Intrinsic Time, date



.. index::
  single: intrinsic_anniversary_time field
.. 




:fleet_type: Fleet type, selection



.. index::
  single: fleet_type field
.. 




:chained_auto_packing: Automatic Move, selection, required

    *This is used only if you selected a chained location type.
    The 'Automatic Move' value will create a stock move after the current one that will be validated automatically. With 'Manual Operation', the stock move has to be validated by a worker. With 'Automatic No Step Added', the location is replaced in the original move.*

.. index::
  single: chained_auto_packing field
.. 




:parent_left: Left Parent, integer



.. index::
  single: parent_left field
.. 




:chained_location_id: Chained Location If Fixed, many2one



.. index::
  single: chained_location_id field
.. 




:crm_cases: Events, one2many



.. index::
  single: crm_cases field
.. 




:is_expired: Expired ?, boolean, readonly



.. index::
  single: is_expired field
.. 




:stock_real: Real Stock, float, readonly



.. index::
  single: stock_real field
.. 



Object: Stock Tracking Lots
###########################

.. index::
  single: Stock Tracking Lots object
.. 


:active: Active, boolean



.. index::
  single: active field
.. 




:move_ids: Moves tracked, one2many



.. index::
  single: move_ids field
.. 




:serial: Reference, char



.. index::
  single: serial field
.. 




:date: Date create, datetime, required



.. index::
  single: date field
.. 




:name: Tracking, char, required



.. index::
  single: name field
.. 



Object: Packing list
####################

.. index::
  single: Packing list object
.. 


:origin: Origin Reference, char



.. index::
  single: origin field
.. 




:address_id: Partner, many2one



.. index::
  single: address_id field
.. 




:sale_journal_id: Sale Journal, many2one



.. index::
  single: sale_journal_id field
.. 




:weight: Weight, float



.. index::
  single: weight field
.. 




:carrier_id: Carrier, many2one



.. index::
  single: carrier_id field
.. 




:invoice_ids: Invoices, many2many



.. index::
  single: invoice_ids field
.. 




:pos_order: Pos order, many2one



.. index::
  single: pos_order field
.. 




:purchase_journal_id: Purchase Journal, many2one



.. index::
  single: purchase_journal_id field
.. 




:location_id: Location, many2one



.. index::
  single: location_id field
.. 




:backorder_id: Back Order, many2one



.. index::
  single: backorder_id field
.. 




:purchase_id: Purchase Order, many2one, readonly



.. index::
  single: purchase_id field
.. 




:date_done: Picking date, datetime, readonly



.. index::
  single: date_done field
.. 




:auto_picking: Auto-Packing, boolean



.. index::
  single: auto_picking field
.. 




:move_type: Delivery Method, selection, required



.. index::
  single: move_type field
.. 




:sale_id: Sale Order, many2one, readonly



.. index::
  single: sale_id field
.. 




:journal_id: Journal, many2one



.. index::
  single: journal_id field
.. 




:note: Notes, text



.. index::
  single: note field
.. 




:state: Status, selection, readonly



.. index::
  single: state field
.. 




:is_supplier_direct_delivery: Is Direct Delivery?, boolean



.. index::
  single: is_supplier_direct_delivery field
.. 




:type: Shipping Type, selection, required



.. index::
  single: type field
.. 




:move_lines: Move lines, one2many



.. index::
  single: move_lines field
.. 




:min_date: Planned Date, datetime



.. index::
  single: min_date field
.. 




:volume: Volume, float



.. index::
  single: volume field
.. 




:date: Date Order, datetime



.. index::
  single: date field
.. 




:invoice_type_id: Invoice Type, many2one, readonly



.. index::
  single: invoice_type_id field
.. 




:active: Active, boolean



.. index::
  single: active field
.. 




:name: Reference, char, required



.. index::
  single: name field
.. 




:invoice_state: Invoice Status, selection, required, readonly



.. index::
  single: invoice_state field
.. 




:location_dest_id: Dest. Location, many2one



.. index::
  single: location_dest_id field
.. 




:max_date: Max. Planned Date, datetime



.. index::
  single: max_date field
.. 



Object: Production lot
######################

.. index::
  single: Production lot object
.. 


:status: Status, selection, required



.. index::
  single: status field
.. 




:heatcode_id: HeatCode, many2one, required



.. index::
  single: heatcode_id field
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




:quality: Quality Information, char



.. index::
  single: quality field
.. 




:revisions: Revisions, one2many



.. index::
  single: revisions field
.. 




:dlc: Product usetime, datetime



.. index::
  single: dlc field
.. 




:stock_available: Available, float, readonly



.. index::
  single: stock_available field
.. 




:thickness: Thickness, float



.. index::
  single: thickness field
.. 




:width: Width, float



.. index::
  single: width field
.. 




:dluo: DLUO, datetime



.. index::
  single: dluo field
.. 




:ref: Internal Ref., char



.. index::
  single: ref field
.. 




:available: Availables, text, readonly



.. index::
  single: available field
.. 




:reservation_ids: Reservations, one2many



.. index::
  single: reservation_ids field
.. 




:localisation: Localisation, char



.. index::
  single: localisation field
.. 




:date: Created Date, datetime, required



.. index::
  single: date field
.. 




:quality_info: Quality Information, text



.. index::
  single: quality_info field
.. 




:product_id: Product, many2one



.. index::
  single: product_id field
.. 




:name: Serial, char, required



.. index::
  single: name field
.. 




:type: Type, selection, required



.. index::
  single: type field
.. 




:removal_date: Removal date, datetime



.. index::
  single: removal_date field
.. 




:length: Length, float



.. index::
  single: length field
.. 




:alert_date: Alert date, datetime



.. index::
  single: alert_date field
.. 




:y: Y of Product, float



.. index::
  single: y field
.. 




:x: X of Product, float



.. index::
  single: x field
.. 




:z: Z of Product, float



.. index::
  single: z field
.. 



Object: Production lot revisions
################################

.. index::
  single: Production lot revisions object
.. 


:indice: Revision, char



.. index::
  single: indice field
.. 




:name: Revision name, char, required



.. index::
  single: name field
.. 




:date: Revision date, date



.. index::
  single: date field
.. 




:lot_id: Production lot, many2one



.. index::
  single: lot_id field
.. 




:author_id: Author, many2one



.. index::
  single: author_id field
.. 




:description: Description, text



.. index::
  single: description field
.. 



Object: Stock Move
##################

.. index::
  single: Stock Move object
.. 


:product_uos_qty: Quantity (UOS), float



.. index::
  single: product_uos_qty field
.. 




:address_id: Dest. Address, many2one



.. index::
  single: address_id field
.. 




:product_uom: Product UOM, many2one, required



.. index::
  single: product_uom field
.. 




:price_unit: Unit Price, float



.. index::
  single: price_unit field
.. 




:procurements: Procurements, one2many



.. index::
  single: procurements field
.. 




:product_qty: Quantity, float, required



.. index::
  single: product_qty field
.. 




:product_uos: Product UOS, many2one



.. index::
  single: product_uos field
.. 




:location_id: Source Location, many2one, required



.. index::
  single: location_id field
.. 




:priority: Priority, selection



.. index::
  single: priority field
.. 




:procurement_ids: Procurements, one2many



.. index::
  single: procurement_ids field
.. 




:new_prodlot_code: Production Tracking Code To Create, char



.. index::
  single: new_prodlot_code field
.. 




:sale_line_id: Sale Order Line, many2one, readonly



.. index::
  single: sale_line_id field
.. 




:auto_validate: Auto Validate, boolean



.. index::
  single: auto_validate field
.. 




:note: Notes, text



.. index::
  single: note field
.. 




:qlty_test_reject: Rejected, boolean, readonly



.. index::
  single: qlty_test_reject field
.. 




:state: Status, selection, readonly



.. index::
  single: state field
.. 




:product_packaging: Packaging, many2one



.. index::
  single: product_packaging field
.. 




:purchase_line_id: Purchase Order Line, many2one, readonly



.. index::
  single: purchase_line_id field
.. 




:move_history_ids: Move History, many2many



.. index::
  single: move_history_ids field
.. 




:production_id: Production, many2one



.. index::
  single: production_id field
.. 




:prodlot_id: Production lot, many2one

    *Production lot is used to put a serial number on the production*

.. index::
  single: prodlot_id field
.. 




:move_dest_id: Dest. Move, many2one



.. index::
  single: move_dest_id field
.. 




:date: Date Created, datetime



.. index::
  single: date field
.. 




:name: Name, char, required



.. index::
  single: name field
.. 




:move_history_ids2: Move History, many2many



.. index::
  single: move_history_ids2 field
.. 




:product_id: Product, many2one, required



.. index::
  single: product_id field
.. 




:date_planned: Scheduled date, datetime, required



.. index::
  single: date_planned field
.. 




:qlty_test_accept: Accepted, boolean, readonly



.. index::
  single: qlty_test_accept field
.. 




:location_dest_id: Dest. Location, many2one, required



.. index::
  single: location_dest_id field
.. 




:tracking_id: Tracking lot, many2one

    *Tracking lot is the code that will be put on the logistic unit/pallet*

.. index::
  single: tracking_id field
.. 




:customer_ref: Customer reference, char



.. index::
  single: customer_ref field
.. 




:picking_id: Packing list, many2one



.. index::
  single: picking_id field
.. 



Object: Inventory
#################

.. index::
  single: Inventory object
.. 


:name: Inventory, char, required, readonly



.. index::
  single: name field
.. 




:date_done: Date done, datetime



.. index::
  single: date_done field
.. 




:move_ids: Created Moves, many2many



.. index::
  single: move_ids field
.. 




:state: Status, selection, readonly



.. index::
  single: state field
.. 




:date: Date create, datetime, required, readonly



.. index::
  single: date field
.. 




:inventory_line_id: Inventories, one2many, readonly



.. index::
  single: inventory_line_id field
.. 



Object: Inventory line
######################

.. index::
  single: Inventory line object
.. 


:inventory_id: Inventory, many2one



.. index::
  single: inventory_id field
.. 




:location_id: Location, many2one, required



.. index::
  single: location_id field
.. 




:product_id: Product, many2one, required



.. index::
  single: product_id field
.. 




:product_uom: Product UOM, many2one, required



.. index::
  single: product_uom field
.. 




:product_qty: Quantity, float



.. index::
  single: product_qty field
.. 



Object: Warehouse
#################

.. index::
  single: Warehouse object
.. 


:lot_input_id: Location Input, many2one, required



.. index::
  single: lot_input_id field
.. 




:partner_address_id: Owner Address, many2one



.. index::
  single: partner_address_id field
.. 




:lot_output_id: Location Output, many2one, required



.. index::
  single: lot_output_id field
.. 




:name: Name, char, required



.. index::
  single: name field
.. 




:lot_stock_id: Location Stock, many2one, required



.. index::
  single: lot_stock_id field
.. 



Object: stock.picking.move.wizard
#################################

.. index::
  single: stock.picking.move.wizard object
.. 


:move_ids: Move lines, many2many, required



.. index::
  single: move_ids field
.. 




:address_id: Dest. Address, many2one



.. index::
  single: address_id field
.. 




:name: Name, char



.. index::
  single: name field
.. 




:picking_id: Packing list, many2one



.. index::
  single: picking_id field
.. 



Object: Dates of Inventories
############################

.. index::
  single: Dates of Inventories object
.. 


:create_date: Latest Date of Inventory, datetime



.. index::
  single: create_date field
.. 




:id: Inventory Line Id, integer, readonly



.. index::
  single: id field
.. 




:product_id: Product Id, integer, readonly



.. index::
  single: product_id field
.. 



Object: Stock report by production lots
#######################################

.. index::
  single: Stock report by production lots object
.. 


:prodlot_id: Production lot, many2one, readonly



.. index::
  single: prodlot_id field
.. 




:location_id: Location, many2one, readonly



.. index::
  single: location_id field
.. 




:name: Quantity, float, readonly



.. index::
  single: name field
.. 




:product_id: Product, many2one, readonly



.. index::
  single: product_id field
.. 

