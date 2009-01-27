
Module Manufacturing Resource Planning (*mrp*)
==============================================
:Module: mrp
:Name: Manufacturing Resource Planning
:Version: 5.0.1.1
:Directory: mrp
:Web: http://www.openerp.com

Description
-----------

::

  This is the base module to manage the manufacturing process in Open ERP.
  
      Features:
      * Make to Stock / Make to Order (by line)
      * Multi-level BoMs, no limit
      * Multi-level routing, no limit
      * Routing and workcenter integrated with analytic accounting
      * Scheduler computation periodically / Just In Time module
      * Multi-pos, multi-warehouse
      * Different reordering policies
      * Cost method by product: standard price, average price
      * Easy analysis of troubles or needs
      * Very flexible
      * Allows to browse Bill of Materials in complete structure
          that include child and phantom BoMs
      It supports complete integration and planification of stockable goods,
      consumable of services. Services are completely integrated with the rest
      of the software. For instance, you can set up a sub-contracting service
      in a BoM to automatically purchase on order the assembly of your production.
  
      Reports provided by this module:
      * Bill of Material structure and components
      * Load forecast on workcenters
      * Print a production order
      * Stock forecasts

Dependencies
------------

 * stock - installed
 * hr - installed
 * purchase - installed
 * product - installed
 * process - installed

Reports
-------

 * BOM Structure

 * Production Order

Menus
-------

 * Manufacturing/Compute All Schedulers
 * Manufacturing
 * Stock Management/Automatic Procurements
 * Manufacturing/Configuration
 * Manufacturing/Configuration/Properties
 * Manufacturing/Configuration/Properties/Property Categories
 * Manufacturing/Configuration/Properties/Properties
 * Manufacturing/Configuration/Workcenters
 * Manufacturing/Configuration/Routings
 * Manufacturing/Configuration/Bill of Materials
 * Manufacturing/Configuration/Bill of Materials/Bill of Material Structure
 * Manufacturing/Configuration/Bill of Materials/New Bill of Materials
 * Manufacturing/Configuration/Bill of Materials Components
 * Manufacturing/Production Orders
 * Manufacturing/Production Orders/Production Orders Planning
 * Manufacturing/Production Orders/Production Orders To Start
 * Manufacturing/Production Orders/Production Orders in Progress
 * Manufacturing/Production Orders/Production Orders Waiting Products
 * Manufacturing/Production Orders/New Production Order
 * Manufacturing/Procurement Orders
 * Manufacturing/Procurement Orders/Unscheduled procurements
 * Stock Management/Automatic Procurements/Exceptions Procurements
 * Stock Management/Automatic Procurements/Exceptions Procurements/Exceptions Procurements to Fix
 * Stock Management/Automatic Procurements/Exceptions Procurements/Temporary Procurement Exceptions
 * Manufacturing/Procurement Orders/New Procurement
 * Stock Management/Automatic Procurements/Minimum Stock Rules
 * Manufacturing/Compute All Schedulers/Compute Procurements Only
 * Manufacturing/Compute All Schedulers/Compute Stock Minimum Rules Only

Views
-----

 * mrp.property.group.form (form)
 * mrp.property.tree (tree)
 * mrp.property.form (form)
 * mrp.workcenter.tree (tree)
 * mrp.workcenter.form (form)
 * mrp.routing.workcenter.tree (tree)
 * mrp.routing.workcenter.form (form)
 * mrp.routing.form (form)
 * mrp.routing.tree (tree)
 * mrp.bom.form (form)
 * mrp.bom.tree (tree)
 * mrp.bom.revision (tree)
 * mrp.bom.revision (form)
 * mrp.production.tree (tree)
 * mrp.production.calendar (calendar)
 * mrp.production.gantt (gantt)
 * mrp.production.graph (graph)
 * mrp.production.form (form)
 * mrp.production.workcenter.line.form (form)
 * mrp.production.workcenter.line.tree (tree)
 * mrp.production.lot.line.form (form)
 * mrp.production.lot.line.tree (tree)
 * mrp.production.product.line.form (form)
 * mrp.production.product.line.tree (tree)
 * mrp.procurement.tree (tree)
 * mrp.procurement.form (form)
 * stock.warehouse.orderpoint.tree (tree)
 * stock.warehouse.orderpoint.form (form)
 * \* INHERIT res.company.mrp.config (form)


Objects
-------

Object: Workcenter
##################

.. index::
  single: Workcenter object
.. 


:costs_cycle_account_id: Cycle Account, many2one

    *Complete this only if you want automatic analytic accounting entries on production orders.*

.. index::
  single: costs_cycle_account_id field
.. 




:time_efficiency: Time Efficiency, float

    *Factor that multiplies all times expressed in the workcenter.*

.. index::
  single: time_efficiency field
.. 




:code: Code, char



.. index::
  single: code field
.. 




:time_start: Time before prod., float

    *Time in hours for the setup.*

.. index::
  single: time_start field
.. 




:name: Workcenter Name, char, required



.. index::
  single: name field
.. 




:time_stop: Time after prod., float

    *Time in hours for the cleaning.*

.. index::
  single: time_stop field
.. 




:capacity_per_cycle: Capacity per Cycle, float

    *Number of operation this workcenter can do in parallel. If this workcenter represent a team of 5 workers, the capacity per cycle is 5.*

.. index::
  single: capacity_per_cycle field
.. 




:type: Type, selection, required



.. index::
  single: type field
.. 




:costs_journal_id: Analytic Journal, many2one



.. index::
  single: costs_journal_id field
.. 




:note: Description, text

    *Description of the workcenter. Explain here what's a cycle according to this workcenter.*

.. index::
  single: note field
.. 




:costs_hour: Cost per hour, float



.. index::
  single: costs_hour field
.. 




:costs_hour_account_id: Hour Account, many2one

    *Complete this only if you want automatic analytic accounting entries on production orders.*

.. index::
  single: costs_hour_account_id field
.. 




:costs_cycle: Cost per cycle, float



.. index::
  single: costs_cycle field
.. 




:timesheet_id: Working Time, many2one

    *The normal working time of the workcenter.*

.. index::
  single: timesheet_id field
.. 




:active: Active, boolean



.. index::
  single: active field
.. 




:costs_general_account_id: General Account, many2one



.. index::
  single: costs_general_account_id field
.. 




:time_cycle: Time for 1 cycle (hour), float

    *Time in hours for doing one cycle.*

.. index::
  single: time_cycle field
.. 



Object: Property Group
######################

.. index::
  single: Property Group object
.. 


:name: Property Group, char, required



.. index::
  single: name field
.. 




:description: Description, text



.. index::
  single: description field
.. 



Object: Property
################

.. index::
  single: Property object
.. 


:group_id: Property Group, many2one, required



.. index::
  single: group_id field
.. 




:composition: Properties composition, selection, required

    *Not used in computations, for information purpose only.*

.. index::
  single: composition field
.. 




:name: Name, char, required



.. index::
  single: name field
.. 




:description: Description, text



.. index::
  single: description field
.. 



Object: Routing
###############

.. index::
  single: Routing object
.. 


:workcenter_lines: Workcenters, one2many



.. index::
  single: workcenter_lines field
.. 




:code: Code, char



.. index::
  single: code field
.. 




:name: Name, char, required



.. index::
  single: name field
.. 




:note: Description, text



.. index::
  single: note field
.. 




:active: Active, boolean



.. index::
  single: active field
.. 




:location_id: Production Location, many2one

    *Keep empty if you produce at the location where the finnished products are needed.Put a location if you produce at a fixed location. This can be a partner location if you subcontract the manufacturing operations.*

.. index::
  single: location_id field
.. 



Object: Routing workcenter usage
################################

.. index::
  single: Routing workcenter usage object
.. 


:cycle_nbr: Number of Cycle, float, required

    *A cycle is defined in the workcenter definition.*

.. index::
  single: cycle_nbr field
.. 




:name: Name, char, required



.. index::
  single: name field
.. 




:sequence: Sequence, integer



.. index::
  single: sequence field
.. 




:note: Description, text



.. index::
  single: note field
.. 




:routing_id: Parent Routing, many2one



.. index::
  single: routing_id field
.. 




:workcenter_id: Workcenter, many2one, required



.. index::
  single: workcenter_id field
.. 




:hour_nbr: Number of Hours, float, required



.. index::
  single: hour_nbr field
.. 



Object: Bill of Material
########################

.. index::
  single: Bill of Material object
.. 


:property_ids: Properties, many2many



.. index::
  single: property_ids field
.. 




:product_uos_qty: Product UOS Qty, float



.. index::
  single: product_uos_qty field
.. 




:date_stop: Valid Until, date

    *Validity of this BoM or component. Keep empty if it's always valid.*

.. index::
  single: date_stop field
.. 




:code: Code, char



.. index::
  single: code field
.. 




:product_uom: Product UOM, many2one, required



.. index::
  single: product_uom field
.. 




:sequence: Sequence, integer



.. index::
  single: sequence field
.. 




:child_complete_ids: BoM Hyerarchy, many2many, readonly



.. index::
  single: child_complete_ids field
.. 




:product_qty: Product Qty, float, required



.. index::
  single: product_qty field
.. 




:product_uos: Product UOS, many2one



.. index::
  single: product_uos field
.. 




:date_start: Valid From, date

    *Validity of this BoM or component. Keep empty if it's always valid.*

.. index::
  single: date_start field
.. 




:sub_products: sub_products, one2many



.. index::
  single: sub_products field
.. 




:routing_id: Routing, many2one

    *The list of operations (list of workcenters) to produce the finnished product. The routing is mainly used to compute workcenter costs during operations and to plan futur loads on workcenters based on production plannification.*

.. index::
  single: routing_id field
.. 




:bom_lines: BoM Lines, one2many



.. index::
  single: bom_lines field
.. 




:type: BoM Type, selection, required

    *Use a phantom bill of material in raw materials lines that have to be automatically computed in on eproduction order and not one per level.If you put "Phantom/Set" at the root level of a bill of material it is considered as a set or pack: the products are replaced by the components between the sale order to the picking without going through the production order.The normal BoM will generate one production order per BoM level.*

.. index::
  single: type field
.. 




:method: Method, selection, readonly



.. index::
  single: method field
.. 




:child_ids: BoM Hyerarchy, many2many, readonly



.. index::
  single: child_ids field
.. 




:bom_id: Parent BoM, many2one



.. index::
  single: bom_id field
.. 




:revision_type: indice type, selection



.. index::
  single: revision_type field
.. 




:active: Active, boolean



.. index::
  single: active field
.. 




:product_efficiency: Product Efficiency, float, required

    *Efficiency on the production. A factor of 0.9 means a loss of 10% in the production.*

.. index::
  single: product_efficiency field
.. 




:product_id: Product, many2one, required



.. index::
  single: product_id field
.. 




:product_rounding: Product Rounding, float

    *Rounding applied on the product quantity. For integer only values, put 1.0*

.. index::
  single: product_rounding field
.. 




:name: Name, char, required



.. index::
  single: name field
.. 




:revision_ids: BoM Revisions, one2many



.. index::
  single: revision_ids field
.. 




:position: Internal Ref., char

    *Reference to a position in an external plan.*

.. index::
  single: position field
.. 



Object: Bill of material revisions
##################################

.. index::
  single: Bill of material revisions object
.. 


:indice: Revision, char



.. index::
  single: indice field
.. 




:name: Modification name, char, required



.. index::
  single: name field
.. 




:bom_id: BoM, many2one



.. index::
  single: bom_id field
.. 




:last_indice: last indice, char



.. index::
  single: last_indice field
.. 




:date: Modification Date, date



.. index::
  single: date field
.. 




:author_id: Author, many2one



.. index::
  single: author_id field
.. 




:description: Description, text



.. index::
  single: description field
.. 



Object: Production
##################

.. index::
  single: Production object
.. 


:origin: Origin, char



.. index::
  single: origin field
.. 




:product_uos_qty: Product Qty, float



.. index::
  single: product_uos_qty field
.. 




:product_uom: Product UOM, many2one, required



.. index::
  single: product_uom field
.. 




:procure_id: Procurement, many2one, readonly



.. index::
  single: procure_id field
.. 




:sale_ref: Sale Ref, char, readonly



.. index::
  single: sale_ref field
.. 




:product_qty: Product Qty, float, required



.. index::
  single: product_qty field
.. 




:product_uos: Product UOM, many2one



.. index::
  single: product_uos field
.. 




:date_planned_date: Planned Date, date, readonly



.. index::
  single: date_planned_date field
.. 




:partner_id: Partner, many2one



.. index::
  single: partner_id field
.. 




:note: Notes, text



.. index::
  single: note field
.. 




:sale_name: Sale Name, char, readonly



.. index::
  single: sale_name field
.. 




:location_src_id: Raw Products Location, many2one, required

    *Location where the system will look for products used in raw materials.*

.. index::
  single: location_src_id field
.. 




:cycle_total: Total Cycles, float, readonly



.. index::
  single: cycle_total field
.. 




:date_start: Start Date, datetime



.. index::
  single: date_start field
.. 




:priority: Priority, selection



.. index::
  single: priority field
.. 




:state: Status, selection, readonly



.. index::
  single: state field
.. 




:product_lines: Scheduled goods, one2many



.. index::
  single: product_lines field
.. 




:bom_id: Bill of Material, many2one



.. index::
  single: bom_id field
.. 




:move_lines: Products Consummed, many2many



.. index::
  single: move_lines field
.. 




:routing_id: Routing, many2one



.. index::
  single: routing_id field
.. 




:date_finnished: End Date, datetime



.. index::
  single: date_finnished field
.. 




:move_created_ids: Moves Created, one2many



.. index::
  single: move_created_ids field
.. 




:product_id: Product, many2one, required



.. index::
  single: product_id field
.. 




:workcenter_lines: Workcenters Utilisation, one2many



.. index::
  single: workcenter_lines field
.. 




:name: Reference, char, required



.. index::
  single: name field
.. 




:move_prod_id: Move product, many2one, readonly



.. index::
  single: move_prod_id field
.. 




:date_planned: Scheduled date, datetime, required



.. index::
  single: date_planned field
.. 




:hour_total: Total Hours, float, readonly



.. index::
  single: hour_total field
.. 




:location_dest_id: Finnished Products Location, many2one, required

    *Location where the system will stock the finnished products.*

.. index::
  single: location_dest_id field
.. 




:picking_id: Packing list, many2one, readonly

    *This is the internal picking list take bring the raw materials to the production plan.*

.. index::
  single: picking_id field
.. 



Object: Production workcenters used
###################################

.. index::
  single: Production workcenters used object
.. 


:product: Product, many2one



.. index::
  single: product field
.. 




:date_start: Start Date, datetime



.. index::
  single: date_start field
.. 




:name: Name, char, required



.. index::
  single: name field
.. 




:hour: Nbr of hour, float



.. index::
  single: hour field
.. 




:sequence: Sequence, integer, required



.. index::
  single: sequence field
.. 




:qlty_test_accept: Accepted, boolean, readonly



.. index::
  single: qlty_test_accept field
.. 




:date_planned: Date Planned, datetime



.. index::
  single: date_planned field
.. 




:qty: Qty, float



.. index::
  single: qty field
.. 




:delay: Delay, char, readonly

    *This is delay between operation start and stop in this workcenter*

.. index::
  single: delay field
.. 




:qlty_test_reject: Rejected, boolean, readonly



.. index::
  single: qlty_test_reject field
.. 




:state: Status, selection, readonly



.. index::
  single: state field
.. 




:date_finnished: End Date, datetime



.. index::
  single: date_finnished field
.. 




:production_id: Production Order, many2one



.. index::
  single: production_id field
.. 




:workcenter_id: Workcenter, many2one, required



.. index::
  single: workcenter_id field
.. 




:uom: UOM, many2one



.. index::
  single: uom field
.. 




:cycle: Nbr of cycle, float



.. index::
  single: cycle field
.. 



Object: Production scheduled products
#####################################

.. index::
  single: Production scheduled products object
.. 


:product_uos_qty: Product UOS Qty, float



.. index::
  single: product_uos_qty field
.. 




:name: Name, char, required



.. index::
  single: name field
.. 




:product_uom: Product UOM, many2one, required



.. index::
  single: product_uom field
.. 




:production_id: Production Order, many2one



.. index::
  single: production_id field
.. 




:product_qty: Product Qty, float, required



.. index::
  single: product_qty field
.. 




:product_uos: Product UOS, many2one



.. index::
  single: product_uos field
.. 




:product_id: Product, many2one, required



.. index::
  single: product_id field
.. 



Object: Procurement
###################

.. index::
  single: Procurement object
.. 


:origin: Origin, char

    *Reference of the document that created this procurement.
    This is automatically completed by Open ERP.*

.. index::
  single: origin field
.. 




:product_uos_qty: UoS Quantity, float



.. index::
  single: product_uos_qty field
.. 




:product_uom: Product UoM, many2one, required



.. index::
  single: product_uom field
.. 




:product_qty: Quantity, float, required



.. index::
  single: product_qty field
.. 




:product_uos: Product UoS, many2one



.. index::
  single: product_uos field
.. 




:message: Latest error, char



.. index::
  single: message field
.. 




:partner_id: Partner, many2one



.. index::
  single: partner_id field
.. 




:production_lot_id: Production Lot, many2one



.. index::
  single: production_lot_id field
.. 




:purchase_id: Purchase Order, many2one



.. index::
  single: purchase_id field
.. 




:note: Note, text



.. index::
  single: note field
.. 




:location_id: Location, many2one, required



.. index::
  single: location_id field
.. 




:close_move: Close Move at end, boolean, required



.. index::
  single: close_move field
.. 




:priority: Priority, selection, required



.. index::
  single: priority field
.. 




:state: Status, selection



.. index::
  single: state field
.. 




:bom_id: BoM, many2one



.. index::
  single: bom_id field
.. 




:procure_method: Procurement Method, selection, required, readonly

    *If you encode manually a procurement, you probably want to use a make to order method.*

.. index::
  single: procure_method field
.. 




:move_id: Reservation, many2one



.. index::
  single: move_id field
.. 




:product_id: Product, many2one, required



.. index::
  single: product_id field
.. 




:name: Name, char, required



.. index::
  single: name field
.. 




:date_planned: Scheduled date, datetime, required



.. index::
  single: date_planned field
.. 




:related_direct_delivery_purchase_order: Related Direct Delivery Purchase Order, many2one



.. index::
  single: related_direct_delivery_purchase_order field
.. 




:property_ids: Properties, many2many



.. index::
  single: property_ids field
.. 




:date_close: Date Closed, datetime



.. index::
  single: date_close field
.. 




:customer_ref: Customer reference, char



.. index::
  single: customer_ref field
.. 



Object: Orderpoint minimum rule
###############################

.. index::
  single: Orderpoint minimum rule object
.. 


:product_max_qty: Max Quantity, float, required

    *When the virtual stock goes belong the Min Quantity, Open ERP generates a procurement to bring the virtual stock to the Max Quantity.*

.. index::
  single: product_max_qty field
.. 




:product_min_qty: Min Quantity, float, required

    *When the virtual stock goes belong the Min Quantity, Open ERP generates a procurement to bring the virtual stock to the Max Quantity.*

.. index::
  single: product_min_qty field
.. 




:qty_multiple: Qty Multiple, integer, required

    *The procurement quantity will by rounded up to this multiple.*

.. index::
  single: qty_multiple field
.. 




:procurement_id: Purchase Order, many2one



.. index::
  single: procurement_id field
.. 




:product_id: Product, many2one, required



.. index::
  single: product_id field
.. 




:product_uom: Product UOM, many2one, required



.. index::
  single: product_uom field
.. 




:warehouse_id: Warehouse, many2one, required



.. index::
  single: warehouse_id field
.. 




:logic: Reordering Mode, selection, required



.. index::
  single: logic field
.. 




:active: Active, boolean



.. index::
  single: active field
.. 




:location_id: Location, many2one, required



.. index::
  single: location_id field
.. 




:name: Name, char, required



.. index::
  single: name field
.. 

