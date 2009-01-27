
Module Sales Management (*sale*)
================================
:Module: sale
:Name: Sales Management
:Version: 5.0.1.0
:Directory: sale
:Web: http://www.openerp.com

Description
-----------

::

  The base module to manage quotations and sales orders.
  
      * Workflow with validation steps:
          - Quotation -> Sale order -> Invoice
      * Invoicing methods:
          - Invoice on order (before or after shipping)
          - Invoice on delivery
          - Invoice on timesheets
          - Advance invoice
      * Partners preferences (shipping, invoicing, incoterm, ...)
      * Products stocks and prices
      * Delivery methods:
          - all at once, multi-parcel
          - delivery costs

Dependencies
------------

 * product - installed
 * stock - installed
 * mrp - installed
 * process - installed

Reports
-------

 * Quotation / Order

Menus
-------

 * Sales Management/Configuration
 * Sales Management
 * Sales Management/Configuration/Shop
 * Sales Management/Sales Orders
 * Sales Management/Sales Orders/My Sales Order
 * Sales Management/Sales Orders/All Sales Order
 * Sales Management/Sales Orders/New Quotation
 * Sales Management/Sales Orders/All Sales Order/Sales in Exception
 * Sales Management/Sales Orders/All Sales Order/Sales Order To Be Invoiced
 * Sales Management/Sales Orders/All Sales Order/Sales Order in Progress
 * Sales Management/Sales Orders/All Sales Order/All Quotations
 * Sales Management/Sales Orders/My Sales Order/My sales in shipping exception
 * Sales Management/Sales Orders/My Sales Order/My sales order waiting Invoice
 * Sales Management/Sales Orders/My Sales Order/My sales order in progress
 * Sales Management/Sales Orders/My Sales Order/My Quotations
 * Sales Management/Sales Order Lines
 * Sales Management/Sales Order Lines/Uninvoiced Lines
 * Sales Management/Sales Order Lines/Uninvoiced Lines/Uninvoiced and Delivered Lines

Views
-----

 * sale.shop (form)
 * sale.shop (tree)
 * sale.order.calendar (calendar)
 * sale.order.graph (graph)
 * sale.order.tree (tree)
 * sale.order.form (form)
 * sale.order.line.graph (graph)
 * sale.order.line.tree (tree)
 * sale.order.line.form2 (form)
 * Configure Picking Policy for Sale Order  (form)
 * \* INHERIT stock.picking.form (form)


Objects
-------

Object: Sale Shop
#################

.. index::
  single: Sale Shop object
.. 


:payment_account_id: Payment accounts, many2many



.. index::
  single: payment_account_id field
.. 




:name: Shop name, char, required



.. index::
  single: name field
.. 




:warehouse_id: Warehouse, many2one



.. index::
  single: warehouse_id field
.. 




:pricelist_id: Pricelist, many2one



.. index::
  single: pricelist_id field
.. 




:project_id: Analytic Account, many2one



.. index::
  single: project_id field
.. 




:payment_default_id: Default Payment Term, many2one, required



.. index::
  single: payment_default_id field
.. 



Object: Sale Order
##################

.. index::
  single: Sale Order object
.. 


:origin: Origin, char



.. index::
  single: origin field
.. 




:has_supplier_direct_delivery: Has Supplier Direct Delivery, boolean, readonly



.. index::
  single: has_supplier_direct_delivery field
.. 




:order_line: Order Lines, one2many, readonly



.. index::
  single: order_line field
.. 




:picking_policy: Packing Policy, selection, required

    *If you don't have enough stock available to deliver all at once, do you accept partial shippings or not.*

.. index::
  single: picking_policy field
.. 




:order_policy: Shipping Policy, selection, required, readonly

    *The Shipping Policy is used to synchronise invoice and delivery operations.
    - The 'Pay before delivery' choice will first generate the invoice and then generate the packing order after the payment of this invoice.
    - The 'Shipping & Manual Invoice' will create the packing order directly and wait for the user to manually click on the 'Invoice' button to generate the draft invoice.
    - The 'Invoice on Order Ater Delivery' choice will generate the draft invoice based on sale order after all packing lists have been finished.
    - The 'Invoice from the packings' choice is used to create an invoice during the packing process.*

.. index::
  single: order_policy field
.. 




:carrier_id: Delivery method, many2one

    *Complete this field if you plan to invoice the shipping based on packings made.*

.. index::
  single: carrier_id field
.. 




:invoice_ids: Invoice, many2many

    *This is the list of invoices that have been generated for this sale order. The same sale order may have been invoiced in several times (by line for example).*

.. index::
  single: invoice_ids field
.. 




:shop_id: Shop, many2one, required, readonly



.. index::
  single: shop_id field
.. 




:fleet_id: Default Sub Fleet, many2one



.. index::
  single: fleet_id field
.. 




:client_order_ref: Customer Ref., char



.. index::
  single: client_order_ref field
.. 




:date_order: Date Ordered, date, required, readonly



.. index::
  single: date_order field
.. 




:esale_osc_id: esale_osc Id, integer



.. index::
  single: esale_osc_id field
.. 




:id: ID, integer, readonly



.. index::
  single: id field
.. 




:invoiced: Paid, boolean, readonly



.. index::
  single: invoiced field
.. 




:delivery_line: Delivery Lines, one2many, readonly



.. index::
  single: delivery_line field
.. 




:amount_tax: Taxes, float, readonly



.. index::
  single: amount_tax field
.. 




:fiscal_position: Fiscal Position, many2one



.. index::
  single: fiscal_position field
.. 




:user_id: Salesman, many2one



.. index::
  single: user_id field
.. 




:esale_osc_web: Website, many2one



.. index::
  single: esale_osc_web field
.. 




:partner_id: Customer, many2one, readonly



.. index::
  single: partner_id field
.. 




:payment_term: Payment Term, many2one



.. index::
  single: payment_term field
.. 




:parent_so: Parent Sales Order, many2one



.. index::
  single: parent_so field
.. 




:journal_id: Journal, many2one



.. index::
  single: journal_id field
.. 




:note: Notes, text



.. index::
  single: note field
.. 




:state: Order State, selection, readonly

    *Gives the state of the quotation or sale order. The exception state is automatically set when a cancel operation occurs in the invoice validation (Invoice Exception) or in the packing list process (Shipping Exception). The 'Waiting Schedule' state is set when the invoice is confirmed but waiting for the scheduler to be on the date 'Date Ordered'.*

.. index::
  single: state field
.. 




:partner_bank: Bank Account, many2one

    *The bank account to pay to or to be paid from. It will be transferred to the invoice*

.. index::
  single: partner_bank field
.. 




:abstract_line_ids: Order Lines, one2many, readonly



.. index::
  single: abstract_line_ids field
.. 




:invoiced_rate: Invoiced, float, readonly



.. index::
  single: invoiced_rate field
.. 




:pricelist_id: Pricelist, many2one, required, readonly



.. index::
  single: pricelist_id field
.. 




:advertising_agency: Advertising Agency, many2one



.. index::
  single: advertising_agency field
.. 




:project_id: Analytic Account, many2one, readonly



.. index::
  single: project_id field
.. 




:child_so: Child Sales Order, one2many



.. index::
  single: child_so field
.. 




:incoterm: Incoterm, selection



.. index::
  single: incoterm field
.. 




:published_customer: Published Customer, many2one



.. index::
  single: published_customer field
.. 




:partner_order_id: Ordering Contact, many2one, required, readonly

    *The name and address of the contact that requested the order or quotation.*

.. index::
  single: partner_order_id field
.. 




:picked_rate: Picked, float, readonly



.. index::
  single: picked_rate field
.. 




:partner_invoice_id: Invoice Address, many2one, required, readonly



.. index::
  single: partner_invoice_id field
.. 




:amount_untaxed: Untaxed Amount, float, readonly



.. index::
  single: amount_untaxed field
.. 




:invoice_type_id: Invoice Type, many2one



.. index::
  single: invoice_type_id field
.. 




:picking_ids: Related Packings, one2many, readonly

    *This is the list of picking list that have been generated for this invoice*

.. index::
  single: picking_ids field
.. 




:amount_total: Total, float, readonly



.. index::
  single: amount_total field
.. 




:name: Order Reference, char, required



.. index::
  single: name field
.. 




:partner_shipping_id: Shipping Address, many2one, required, readonly



.. index::
  single: partner_shipping_id field
.. 




:customer_pricelist_id: Customer Pricelist, many2one



.. index::
  single: customer_pricelist_id field
.. 




:price_type: Price method, selection, required



.. index::
  single: price_type field
.. 




:case_ids: Related Cases, one2many



.. index::
  single: case_ids field
.. 




:dept: Department, many2one



.. index::
  single: dept field
.. 




:shipped: Picked, boolean, readonly



.. index::
  single: shipped field
.. 




:invoice_quantity: Invoice on, selection, required

    *The sale order will automatically create the invoice proposition (draft invoice). Ordered and delivered quantities may not be the same. You have to choose if you invoice based on ordered or shipped quantities. If the product is a service, shipped quantities means hours spent on the associated tasks.*

.. index::
  single: invoice_quantity field
.. 




:payment_type: Payment type, many2one

    *The type of payment. It will be transferred to the invoice*

.. index::
  single: payment_type field
.. 




:topnotes: Top Notes, text



.. index::
  single: topnotes field
.. 




:discount_campaign: Discount Campaign, many2one



.. index::
  single: discount_campaign field
.. 




:margin: Margin, float, readonly



.. index::
  single: margin field
.. 



Object: Sale Order line
#######################

.. index::
  single: Sale Order line object
.. 


:property_ids: Properties, many2many



.. index::
  single: property_ids field
.. 




:product_uos_qty: Quantity (UOS), float



.. index::
  single: product_uos_qty field
.. 




:adv_issue: Advertising Issue, many2one



.. index::
  single: adv_issue field
.. 




:product_uom: Product UoM, many2one, required



.. index::
  single: product_uom field
.. 




:sequence: Sequence Number, integer



.. index::
  single: sequence field
.. 




:parent_fleet_id: Fleet, many2one



.. index::
  single: parent_fleet_id field
.. 




:price_unit: Unit Price, float, required



.. index::
  single: price_unit field
.. 




:product_uom_qty: Quantity (UoM), float, required



.. index::
  single: product_uom_qty field
.. 




:price_subtotal: Subtotal w/o tax, float, readonly



.. index::
  single: price_subtotal field
.. 




:maintenance_end_date: Maintenance End Date, date



.. index::
  single: maintenance_end_date field
.. 




:deliveries: Planned Deliveries, float, readonly



.. index::
  single: deliveries field
.. 




:is_supplier_direct_delivery_advised: Is Supplier Direct Delivery Advised?, boolean, readonly



.. index::
  single: is_supplier_direct_delivery_advised field
.. 




:size_x: Width, float



.. index::
  single: size_x field
.. 




:size_y: Height, float



.. index::
  single: size_y field
.. 




:size_z: Thickness, float



.. index::
  single: size_z field
.. 




:product_uos: Product UOS, many2one



.. index::
  single: product_uos field
.. 




:purchase_order_line: Related Purchase Order Line, many2one



.. index::
  single: purchase_order_line field
.. 




:production_lot_id: Production Lot, many2one



.. index::
  single: production_lot_id field
.. 




:number_packages: Number packages, integer, readonly



.. index::
  single: number_packages field
.. 




:invoiced: Invoiced, boolean, readonly



.. index::
  single: invoiced field
.. 




:move_ids: Inventory Moves, one2many, readonly



.. index::
  single: move_ids field
.. 




:analytics_id: Analytic Distribution, many2one



.. index::
  single: analytics_id field
.. 




:from_date: Start of Validity, datetime



.. index::
  single: from_date field
.. 




:page_reference: Reference of the Page, char



.. index::
  single: page_reference field
.. 




:delay: Delivery Delay, float, required



.. index::
  single: delay field
.. 




:price_unit_customer: Customer Unit Price, float



.. index::
  single: price_unit_customer field
.. 




:state: Status, selection, required, readonly



.. index::
  single: state field
.. 




:maintenance_product_qty: Maintenance Product Quantity, integer



.. index::
  single: maintenance_product_qty field
.. 




:order_partner_id: Customer, many2one



.. index::
  single: order_partner_id field
.. 




:is_supplier_direct_delivery: Is Direct Delivery?, boolean



.. index::
  single: is_supplier_direct_delivery field
.. 




:product_packaging: Packaging, many2one



.. index::
  single: product_packaging field
.. 




:maintenance_start_date: Maintenance Start Date, date



.. index::
  single: maintenance_start_date field
.. 




:type: Procure Method, selection, required



.. index::
  single: type field
.. 




:fleet_id: Sub Fleet, many2one



.. index::
  single: fleet_id field
.. 




:maintenance_month_qty: Maintenance Month Quantity, integer, readonly



.. index::
  single: maintenance_month_qty field
.. 




:procurement_id: Procurement, many2one



.. index::
  single: procurement_id field
.. 




:order_fleet_id: Default Sale Order Sub Fleet, many2one



.. index::
  single: order_fleet_id field
.. 




:order_id: Order Ref, many2one, required



.. index::
  single: order_id field
.. 




:layout_remark: Layout Remark, text



.. index::
  single: layout_remark field
.. 




:price_subtotal_incl: Subtotal, float, readonly



.. index::
  single: price_subtotal_incl field
.. 




:discount: Discount (%), float



.. index::
  single: discount field
.. 




:prodlot_id: Production lot, many2one

    *Production lot is used to put a serial number on the production*

.. index::
  single: prodlot_id field
.. 




:to_date: End of Validity, datetime



.. index::
  single: to_date field
.. 




:price_net: Net Price, float, readonly



.. index::
  single: price_net field
.. 




:customer_ref: Customer reference, char



.. index::
  single: customer_ref field
.. 




:tax_id: Taxes, many2many



.. index::
  single: tax_id field
.. 




:is_maintenance: Is Maintenance, boolean



.. index::
  single: is_maintenance field
.. 




:name: Description, char, required



.. index::
  single: name field
.. 




:expected_invoice_date: Expected Invoice Date, datetime



.. index::
  single: expected_invoice_date field
.. 




:invoice_lines: Invoice Lines, many2many, readonly



.. index::
  single: invoice_lines field
.. 




:notes: Notes, text



.. index::
  single: notes field
.. 




:purchase_order_state: Purchase Order State, char



.. index::
  single: purchase_order_state field
.. 




:purchase_order: Related Purchase Order, many2one



.. index::
  single: purchase_order field
.. 




:prodlot_ids: Lots Assignation, one2many

    *Production lot is used to put a serial number on the production*

.. index::
  single: prodlot_ids field
.. 




:product_id: Product, many2one



.. index::
  single: product_id field
.. 




:th_weight: Weight, float



.. index::
  single: th_weight field
.. 




:y: Y of Product, float



.. index::
  single: y field
.. 




:x: X of Product, float



.. index::
  single: x field
.. 




:layout_type: Layout Type, selection, required



.. index::
  single: layout_type field
.. 




:z: Z of Product, float



.. index::
  single: z field
.. 




:margin: Margin, float, readonly



.. index::
  single: margin field
.. 




:address_allotment_id: Allotment Partner, many2one



.. index::
  single: address_allotment_id field
.. 



Object: sale.config.picking_policy
##################################

.. index::
  single: sale.config.picking_policy object
.. 


:picking_policy: Packing Default Policy, selection, required



.. index::
  single: picking_policy field
.. 




:order_policy: Shipping Default Policy, selection, required



.. index::
  single: order_policy field
.. 




:step: Steps To Deliver a Sale Order, selection, required

    *By default, Open ERP is able to manage complex routing and paths of products in your warehouse and partner locations. This will configure the most common and simple methods to deliver products to the customer in one or two operations by the worker.*

.. index::
  single: step field
.. 




:name: Name, char



.. index::
  single: name field
.. 

