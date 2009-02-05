
.. module:: sale
    :synopsis: Sales Management (Official, Quality Certified)
    :noindex:
.. 

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

Sales Management (*sale*)
=========================
:Module: sale
:Name: Sales Management
:Version: 5.0.1.0
:Author: Tiny
:Directory: sale
:Web: http://www.openerp.com
:Official module: yes
:Quality certified: yes

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

 * :mod:`product`
 * :mod:`stock`
 * :mod:`mrp`
 * :mod:`process`

Reports
-------

 * Print Order

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
 * Sale lines (tree)
 * sale.order.line.form2 (form)
 * Configure Picking Policy for Sale Order  (form)
 * \* INHERIT stock.picking.form (form)


Objects
-------

Object: Sale Shop (sale.shop)
#############################



:payment_account_id: Payment accounts, many2many





:name: Shop name, char, required





:warehouse_id: Warehouse, many2one





:pricelist_id: Pricelist, many2one





:project_id: Analytic Account, many2one





:payment_default_id: Default Payment Term, many2one, required




Object: Sale Order (sale.order)
###############################



:origin: Origin, char





:topnotes: Top Notes, text





:order_line: Order Lines, one2many, readonly





:picking_policy: Packing Policy, selection, required

    *If you don't have enough stock available to deliver all at once, do you accept partial shippings or not.*



:order_policy: Shipping Policy, selection, required, readonly

    *The Shipping Policy is used to synchronise invoice and delivery operations.
    - The 'Pay before delivery' choice will first generate the invoice and then generate the packing order after the payment of this invoice.
    - The 'Shipping & Manual Invoice' will create the packing order directly and wait for the user to manually click on the 'Invoice' button to generate the draft invoice.
    - The 'Invoice on Order Ater Delivery' choice will generate the draft invoice based on sale order after all packing lists have been finished.
    - The 'Invoice from the packings' choice is used to create an invoice during the packing process.*



:carrier_id: Delivery method, many2one

    *Complete this field if you plan to invoice the shipping based on packings made.*



:invoice_ids: Invoice, many2many

    *This is the list of invoices that have been generated for this sale order. The same sale order may have been invoiced in several times (by line for example).*



:shop_id: Shop, many2one, required, readonly





:fleet_id: Default Sub Fleet, many2one





:client_order_ref: Customer Ref., char





:date_order: Date Ordered, date, required, readonly





:esale_osc_id: esale_osc Id, integer





:id: ID, integer, readonly





:invoiced: Paid, boolean, readonly





:delivery_line: Delivery Lines, one2many, readonly





:amount_tax: Taxes, float, readonly





:fiscal_position: Fiscal Position, many2one





:user_id: Salesman, many2one





:esale_osc_web: Website, many2one





:partner_id: Customer, many2one, readonly





:payment_term: Payment Term, many2one





:parent_so: Parent Sales Order, many2one





:journal_id: Journal, many2one





:note: Notes, text





:state: Order State, selection, readonly

    *Gives the state of the quotation or sale order. The exception state is automatically set when a cancel operation occurs in the invoice validation (Invoice Exception) or in the packing list process (Shipping Exception). The 'Waiting Schedule' state is set when the invoice is confirmed but waiting for the scheduler to be on the date 'Date Ordered'.*



:partner_bank: Bank Account, many2one

    *The bank account to pay to or to be paid from. It will be transferred to the invoice*



:abstract_line_ids: Order Lines, one2many, readonly





:invoiced_rate: Invoiced, float, readonly





:pricelist_id: Pricelist, many2one, required, readonly





:advertising_agency: Advertising Agency, many2one





:project_id: Analytic Account, many2one, readonly





:has_supplier_direct_delivery: Has Supplier Direct Delivery, boolean, readonly





:child_so: Child Sales Order, one2many





:incoterm: Incoterm, selection





:published_customer: Published Customer, many2one





:partner_order_id: Ordering Contact, many2one, required, readonly

    *The name and address of the contact that requested the order or quotation.*



:picked_rate: Picked, float, readonly





:partner_invoice_id: Invoice Address, many2one, required, readonly





:amount_untaxed: Untaxed Amount, float, readonly





:invoice_type_id: Invoice Type, many2one





:picking_ids: Related Packings, one2many, readonly

    *This is the list of picking list that have been generated for this invoice*



:amount_total: Total, float, readonly





:name: Order Reference, char, required





:partner_shipping_id: Shipping Address, many2one, required, readonly





:customer_pricelist_id: Customer Pricelist, many2one





:price_type: Price method, selection, required





:case_ids: Related Cases, one2many





:dept: Department, many2one





:shipped: Picked, boolean, readonly





:invoice_quantity: Invoice on, selection, required

    *The sale order will automatically create the invoice proposition (draft invoice). Ordered and delivered quantities may not be the same. You have to choose if you invoice based on ordered or shipped quantities. If the product is a service, shipped quantities means hours spent on the associated tasks.*



:payment_type: Payment type, many2one

    *The type of payment. It will be transferred to the invoice*



:discount_campaign: Discount Campaign, many2one





:margin: Margin, float, readonly




Object: Sale Order line (sale.order.line)
#########################################



:property_ids: Properties, many2many





:product_uos_qty: Quantity (UOS), float





:adv_issue: Advertising Issue, many2one





:product_uom: Product UoM, many2one, required





:sequence: Sequence Number, integer





:parent_fleet_id: Fleet, many2one





:price_unit: Unit Price, float, required





:product_uom_qty: Quantity (UoM), float, required





:price_subtotal: Subtotal w/o tax, float, readonly





:maintenance_end_date: Maintenance End Date, date





:deliveries: Planned Deliveries, float, readonly





:is_supplier_direct_delivery_advised: Is Supplier Direct Delivery Advised?, boolean, readonly





:size_x: Width, float





:size_y: Height, float





:size_z: Thickness, float





:product_uos: Product UOS, many2one





:purchase_order_line: Related Purchase Order Line, many2one





:production_lot_id: Production Lot, many2one





:number_packages: Number packages, integer, readonly





:invoiced: Invoiced, boolean, readonly





:move_ids: Inventory Moves, one2many, readonly





:analytics_id: Analytic Distribution, many2one





:from_date: Start of Validity, datetime





:page_reference: Reference of the Page, char





:delay: Delivery Delay, float, required





:price_unit_customer: Customer Unit Price, float





:state: Status, selection, required, readonly





:maintenance_product_qty: Maintenance Product Quantity, integer





:order_partner_id: Customer, many2one





:is_supplier_direct_delivery: Is Direct Delivery?, boolean





:product_packaging: Packaging, many2one





:maintenance_start_date: Maintenance Start Date, date





:type: Procure Method, selection, required





:fleet_id: Sub Fleet, many2one





:maintenance_month_qty: Maintenance Month Quantity, integer, readonly





:procurement_id: Procurement, many2one





:order_fleet_id: Default Sale Order Sub Fleet, many2one





:order_id: Order Ref, many2one, required





:layout_remark: Layout Remark, text





:price_subtotal_incl: Subtotal, float, readonly





:discount: Discount (%), float





:prodlot_id: Production lot, many2one

    *Production lot is used to put a serial number on the production*



:to_date: End of Validity, datetime





:price_net: Net Price, float, readonly





:customer_ref: Customer reference, char





:tax_id: Taxes, many2many





:is_maintenance: Is Maintenance, boolean





:name: Description, char, required





:expected_invoice_date: Expected Invoice Date, datetime





:invoice_lines: Invoice Lines, many2many, readonly





:notes: Notes, text





:purchase_order_state: Purchase Order State, char





:purchase_order: Related Purchase Order, many2one





:prodlot_ids: Lots Assignation, one2many

    *Production lot is used to put a serial number on the production*



:product_id: Product, many2one





:th_weight: Weight, float





:y: Y of Product, float





:x: X of Product, float





:layout_type: Layout Type, selection, required





:z: Z of Product, float





:margin: Margin, float, readonly





:address_allotment_id: Allotment Partner, many2one




Object: sale.config.picking_policy (sale.config.picking_policy)
###############################################################



:picking_policy: Packing Default Policy, selection, required





:order_policy: Shipping Default Policy, selection, required





:step: Steps To Deliver a Sale Order, selection, required

    *By default, Open ERP is able to manage complex routing and paths of products in your warehouse and partner locations. This will configure the most common and simple methods to deliver products to the customer in one or two operations by the worker.*



:name: Name, char


