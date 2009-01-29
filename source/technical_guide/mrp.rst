
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



:costs_cycle_account_id: Cycle Account, many2one

    *Complete this only if you want automatic analytic accounting entries on production orders.*



:time_efficiency: Time Efficiency, float

    *Factor that multiplies all times expressed in the workcenter.*



:code: Code, char





:time_start: Time before prod., float

    *Time in hours for the setup.*



:name: Workcenter Name, char, required





:time_stop: Time after prod., float

    *Time in hours for the cleaning.*



:capacity_per_cycle: Capacity per Cycle, float

    *Number of operation this workcenter can do in parallel. If this workcenter represent a team of 5 workers, the capacity per cycle is 5.*



:type: Type, selection, required





:costs_journal_id: Analytic Journal, many2one





:note: Description, text

    *Description of the workcenter. Explain here what's a cycle according to this workcenter.*



:costs_hour: Cost per hour, float





:costs_hour_account_id: Hour Account, many2one

    *Complete this only if you want automatic analytic accounting entries on production orders.*



:costs_cycle: Cost per cycle, float





:timesheet_id: Working Time, many2one

    *The normal working time of the workcenter.*



:active: Active, boolean





:costs_general_account_id: General Account, many2one





:time_cycle: Time for 1 cycle (hour), float

    *Time in hours for doing one cycle.*


Object: Property Group
######################



:name: Property Group, char, required





:description: Description, text




Object: Property
################



:group_id: Property Group, many2one, required





:composition: Properties composition, selection, required

    *Not used in computations, for information purpose only.*



:name: Name, char, required





:description: Description, text




Object: Routing
###############



:workcenter_lines: Workcenters, one2many





:code: Code, char





:name: Name, char, required





:note: Description, text





:active: Active, boolean





:location_id: Production Location, many2one

    *Keep empty if you produce at the location where the finnished products are needed.Put a location if you produce at a fixed location. This can be a partner location if you subcontract the manufacturing operations.*


Object: Routing workcenter usage
################################



:cycle_nbr: Number of Cycle, float, required

    *A cycle is defined in the workcenter definition.*



:name: Name, char, required





:sequence: Sequence, integer





:note: Description, text





:routing_id: Parent Routing, many2one





:workcenter_id: Workcenter, many2one, required





:hour_nbr: Number of Hours, float, required




Object: Bill of Material
########################



:property_ids: Properties, many2many





:product_uos_qty: Product UOS Qty, float





:date_stop: Valid Until, date

    *Validity of this BoM or component. Keep empty if it's always valid.*



:code: Code, char





:product_uom: Product UOM, many2one, required





:sequence: Sequence, integer





:child_complete_ids: BoM Hyerarchy, many2many, readonly





:product_qty: Product Qty, float, required





:product_uos: Product UOS, many2one





:date_start: Valid From, date

    *Validity of this BoM or component. Keep empty if it's always valid.*



:sub_products: sub_products, one2many





:routing_id: Routing, many2one

    *The list of operations (list of workcenters) to produce the finnished product. The routing is mainly used to compute workcenter costs during operations and to plan futur loads on workcenters based on production plannification.*



:bom_lines: BoM Lines, one2many





:type: BoM Type, selection, required

    *Use a phantom bill of material in raw materials lines that have to be automatically computed in on eproduction order and not one per level.If you put "Phantom/Set" at the root level of a bill of material it is considered as a set or pack: the products are replaced by the components between the sale order to the picking without going through the production order.The normal BoM will generate one production order per BoM level.*



:method: Method, selection, readonly





:child_ids: BoM Hyerarchy, many2many, readonly





:bom_id: Parent BoM, many2one





:revision_type: indice type, selection





:active: Active, boolean





:product_efficiency: Product Efficiency, float, required

    *Efficiency on the production. A factor of 0.9 means a loss of 10% in the production.*



:product_id: Product, many2one, required





:product_rounding: Product Rounding, float

    *Rounding applied on the product quantity. For integer only values, put 1.0*



:name: Name, char, required





:revision_ids: BoM Revisions, one2many





:position: Internal Ref., char

    *Reference to a position in an external plan.*


Object: Bill of material revisions
##################################



:indice: Revision, char





:name: Modification name, char, required





:bom_id: BoM, many2one





:last_indice: last indice, char





:date: Modification Date, date





:author_id: Author, many2one





:description: Description, text




Object: Production
##################



:origin: Origin, char





:product_uos_qty: Product Qty, float





:product_uom: Product UOM, many2one, required





:procure_id: Procurement, many2one, readonly





:sale_ref: Sale Ref, char, readonly





:product_qty: Product Qty, float, required





:product_uos: Product UOM, many2one





:date_planned_date: Planned Date, date, readonly





:partner_id: Partner, many2one





:note: Notes, text





:sale_name: Sale Name, char, readonly





:location_src_id: Raw Products Location, many2one, required

    *Location where the system will look for products used in raw materials.*



:cycle_total: Total Cycles, float, readonly





:date_start: Start Date, datetime





:priority: Priority, selection





:state: Status, selection, readonly





:product_lines: Scheduled goods, one2many





:bom_id: Bill of Material, many2one





:move_lines: Products Consummed, many2many





:routing_id: Routing, many2one





:date_finnished: End Date, datetime





:move_created_ids: Moves Created, one2many





:product_id: Product, many2one, required





:workcenter_lines: Workcenters Utilisation, one2many





:name: Reference, char, required





:move_prod_id: Move product, many2one, readonly





:date_planned: Scheduled date, datetime, required





:hour_total: Total Hours, float, readonly





:location_dest_id: Finnished Products Location, many2one, required

    *Location where the system will stock the finnished products.*



:picking_id: Packing list, many2one, readonly

    *This is the internal picking list take bring the raw materials to the production plan.*


Object: Production workcenters used
###################################



:product: Product, many2one





:date_start: Start Date, datetime





:name: Name, char, required





:hour: Nbr of hour, float





:sequence: Sequence, integer, required





:qlty_test_accept: Accepted, boolean, readonly





:date_planned: Date Planned, datetime





:qty: Qty, float





:delay: Delay, char, readonly

    *This is delay between operation start and stop in this workcenter*



:qlty_test_reject: Rejected, boolean, readonly





:state: Status, selection, readonly





:date_finnished: End Date, datetime





:production_id: Production Order, many2one





:workcenter_id: Workcenter, many2one, required





:uom: UOM, many2one





:cycle: Nbr of cycle, float




Object: Production scheduled products
#####################################



:product_uos_qty: Product UOS Qty, float





:name: Name, char, required





:product_uom: Product UOM, many2one, required





:production_id: Production Order, many2one





:product_qty: Product Qty, float, required





:product_uos: Product UOS, many2one





:product_id: Product, many2one, required




Object: Procurement
###################



:origin: Origin, char

    *Reference of the document that created this procurement.
    This is automatically completed by Open ERP.*



:product_uos_qty: UoS Quantity, float





:product_uom: Product UoM, many2one, required





:product_qty: Quantity, float, required





:product_uos: Product UoS, many2one





:message: Latest error, char





:partner_id: Partner, many2one





:production_lot_id: Production Lot, many2one





:purchase_id: Purchase Order, many2one





:note: Note, text





:location_id: Location, many2one, required





:close_move: Close Move at end, boolean, required





:priority: Priority, selection, required





:state: Status, selection





:bom_id: BoM, many2one





:procure_method: Procurement Method, selection, required, readonly

    *If you encode manually a procurement, you probably want to use a make to order method.*



:move_id: Reservation, many2one





:product_id: Product, many2one, required





:name: Name, char, required





:date_planned: Scheduled date, datetime, required





:related_direct_delivery_purchase_order: Related Direct Delivery Purchase Order, many2one





:property_ids: Properties, many2many





:date_close: Date Closed, datetime





:customer_ref: Customer reference, char




Object: Orderpoint minimum rule
###############################



:product_max_qty: Max Quantity, float, required

    *When the virtual stock goes belong the Min Quantity, Open ERP generates a procurement to bring the virtual stock to the Max Quantity.*



:product_min_qty: Min Quantity, float, required

    *When the virtual stock goes belong the Min Quantity, Open ERP generates a procurement to bring the virtual stock to the Max Quantity.*



:qty_multiple: Qty Multiple, integer, required

    *The procurement quantity will by rounded up to this multiple.*



:procurement_id: Purchase Order, many2one





:product_id: Product, many2one, required





:product_uom: Product UOM, many2one, required





:warehouse_id: Warehouse, many2one, required





:logic: Reordering Mode, selection, required





:active: Active, boolean





:location_id: Location, many2one, required





:name: Name, char, required


