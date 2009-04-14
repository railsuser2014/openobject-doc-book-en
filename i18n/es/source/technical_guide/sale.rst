
.. i18n: .. module:: sale
.. i18n:     :synopsis: Sales Management (Official, Quality Certified)
.. i18n:     :noindex:
.. i18n: .. 

.. module:: sale
    :synopsis: Sales Management (Official, Quality Certified)
    :noindex:
.. 

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. i18n: Sales Management (*sale*)
.. i18n: =========================
.. i18n: :Module: sale
.. i18n: :Name: Sales Management
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: sale
.. i18n: :Web: http://www.openerp.com
.. i18n: :Official module: yes
.. i18n: :Quality certified: yes

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

.. i18n: Description
.. i18n: -----------

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   The base module to manage quotations and sales orders.
.. i18n:   
.. i18n:       * Workflow with validation steps:
.. i18n:           - Quotation -> Sale order -> Invoice
.. i18n:       * Invoicing methods:
.. i18n:           - Invoice on order (before or after shipping)
.. i18n:           - Invoice on delivery
.. i18n:           - Invoice on timesheets
.. i18n:           - Advance invoice
.. i18n:       * Partners preferences (shipping, invoicing, incoterm, ...)
.. i18n:       * Products stocks and prices
.. i18n:       * Delivery methods:
.. i18n:           - all at once, multi-parcel
.. i18n:           - delivery costs

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

.. i18n: Dependencies
.. i18n: ------------

Dependencies
------------

.. i18n:  * :mod:`product`
.. i18n:  * :mod:`stock`
.. i18n:  * :mod:`mrp`
.. i18n:  * :mod:`process`

 * :mod:`product`
 * :mod:`stock`
 * :mod:`mrp`
 * :mod:`process`

.. i18n: Reports
.. i18n: -------

Reports
-------

.. i18n:  * Print Order

 * Print Order

.. i18n: Menus
.. i18n: -------

Menus
-------

.. i18n:  * Sales Management/Configuration
.. i18n:  * Sales Management
.. i18n:  * Sales Management/Configuration/Shop
.. i18n:  * Sales Management/Sales Orders
.. i18n:  * Sales Management/Sales Orders/My Sales Order
.. i18n:  * Sales Management/Sales Orders/All Sales Order
.. i18n:  * Sales Management/Sales Orders/New Quotation
.. i18n:  * Sales Management/Sales Orders/All Sales Order/Sales in Exception
.. i18n:  * Sales Management/Sales Orders/All Sales Order/Sales Order To Be Invoiced
.. i18n:  * Sales Management/Sales Orders/All Sales Order/Sales Order in Progress
.. i18n:  * Sales Management/Sales Orders/All Sales Order/All Quotations
.. i18n:  * Sales Management/Sales Orders/My Sales Order/My sales in shipping exception
.. i18n:  * Sales Management/Sales Orders/My Sales Order/My sales order waiting Invoice
.. i18n:  * Sales Management/Sales Orders/My Sales Order/My sales order in progress
.. i18n:  * Sales Management/Sales Orders/My Sales Order/My Quotations
.. i18n:  * Sales Management/Sales Order Lines
.. i18n:  * Sales Management/Sales Order Lines/Uninvoiced Lines
.. i18n:  * Sales Management/Sales Order Lines/Uninvoiced Lines/Uninvoiced and Delivered Lines

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

.. i18n: Views
.. i18n: -----

Views
-----

.. i18n:  * sale.shop (form)
.. i18n:  * sale.shop (tree)
.. i18n:  * sale.order.calendar (calendar)
.. i18n:  * sale.order.graph (graph)
.. i18n:  * sale.order.tree (tree)
.. i18n:  * sale.order.form (form)
.. i18n:  * sale.order.line.graph (graph)
.. i18n:  * Sale lines (tree)
.. i18n:  * sale.order.line.form2 (form)
.. i18n:  * Configure Picking Policy for Sale Order  (form)
.. i18n:  * \* INHERIT stock.picking.form (form)

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

.. i18n: Objects
.. i18n: -------

Objects
-------

.. i18n: Object: Sale Shop (sale.shop)
.. i18n: #############################

Object: Sale Shop (sale.shop)
#############################

.. i18n: :payment_account_id: Payment accounts, many2many

:payment_account_id: Payment accounts, many2many

.. i18n: :name: Shop name, char, required

:name: Shop name, char, required

.. i18n: :warehouse_id: Warehouse, many2one

:warehouse_id: Warehouse, many2one

.. i18n: :pricelist_id: Pricelist, many2one

:pricelist_id: Pricelist, many2one

.. i18n: :project_id: Analytic Account, many2one

:project_id: Analytic Account, many2one

.. i18n: :payment_default_id: Default Payment Term, many2one, required

:payment_default_id: Default Payment Term, many2one, required

.. i18n: Object: Sale Order (sale.order)
.. i18n: ###############################

Object: Sale Order (sale.order)
###############################

.. i18n: :origin: Origin, char

:origin: Origin, char

.. i18n: :topnotes: Top Notes, text

:topnotes: Top Notes, text

.. i18n: :order_line: Order Lines, one2many, readonly

:order_line: Order Lines, one2many, readonly

.. i18n: :picking_policy: Packing Policy, selection, required

:picking_policy: Packing Policy, selection, required

.. i18n:     *If you don't have enough stock available to deliver all at once, do you accept partial shippings or not.*

    *If you don't have enough stock available to deliver all at once, do you accept partial shippings or not.*

.. i18n: :order_policy: Shipping Policy, selection, required, readonly

:order_policy: Shipping Policy, selection, required, readonly

.. i18n:     *The Shipping Policy is used to synchronise invoice and delivery operations.
.. i18n:     - The 'Pay before delivery' choice will first generate the invoice and then generate the packing order after the payment of this invoice.
.. i18n:     - The 'Shipping & Manual Invoice' will create the packing order directly and wait for the user to manually click on the 'Invoice' button to generate the draft invoice.
.. i18n:     - The 'Invoice on Order Ater Delivery' choice will generate the draft invoice based on sale order after all packing lists have been finished.
.. i18n:     - The 'Invoice from the packings' choice is used to create an invoice during the packing process.*

    *The Shipping Policy is used to synchronise invoice and delivery operations.
    - The 'Pay before delivery' choice will first generate the invoice and then generate the packing order after the payment of this invoice.
    - The 'Shipping & Manual Invoice' will create the packing order directly and wait for the user to manually click on the 'Invoice' button to generate the draft invoice.
    - The 'Invoice on Order Ater Delivery' choice will generate the draft invoice based on sale order after all packing lists have been finished.
    - The 'Invoice from the packings' choice is used to create an invoice during the packing process.*

.. i18n: :carrier_id: Delivery method, many2one

:carrier_id: Delivery method, many2one

.. i18n:     *Complete this field if you plan to invoice the shipping based on packings made.*

    *Complete this field if you plan to invoice the shipping based on packings made.*

.. i18n: :invoice_ids: Invoice, many2many

:invoice_ids: Invoice, many2many

.. i18n:     *This is the list of invoices that have been generated for this sale order. The same sale order may have been invoiced in several times (by line for example).*

    *This is the list of invoices that have been generated for this sale order. The same sale order may have been invoiced in several times (by line for example).*

.. i18n: :shop_id: Shop, many2one, required, readonly

:shop_id: Shop, many2one, required, readonly

.. i18n: :fleet_id: Default Sub Fleet, many2one

:fleet_id: Default Sub Fleet, many2one

.. i18n: :client_order_ref: Customer Ref., char

:client_order_ref: Customer Ref., char

.. i18n: :date_order: Date Ordered, date, required, readonly

:date_order: Date Ordered, date, required, readonly

.. i18n: :esale_osc_id: esale_osc Id, integer

:esale_osc_id: esale_osc Id, integer

.. i18n: :id: ID, integer, readonly

:id: ID, integer, readonly

.. i18n: :invoiced: Paid, boolean, readonly

:invoiced: Paid, boolean, readonly

.. i18n: :delivery_line: Delivery Lines, one2many, readonly

:delivery_line: Delivery Lines, one2many, readonly

.. i18n: :amount_tax: Taxes, float, readonly

:amount_tax: Taxes, float, readonly

.. i18n: :fiscal_position: Fiscal Position, many2one

:fiscal_position: Fiscal Position, many2one

.. i18n: :user_id: Salesman, many2one

:user_id: Salesman, many2one

.. i18n: :esale_osc_web: Website, many2one

:esale_osc_web: Website, many2one

.. i18n: :partner_id: Customer, many2one, readonly

:partner_id: Customer, many2one, readonly

.. i18n: :payment_term: Payment Term, many2one

:payment_term: Payment Term, many2one

.. i18n: :parent_so: Parent Sales Order, many2one

:parent_so: Parent Sales Order, many2one

.. i18n: :journal_id: Journal, many2one

:journal_id: Journal, many2one

.. i18n: :note: Notes, text

:note: Notes, text

.. i18n: :state: Order State, selection, readonly

:state: Order State, selection, readonly

.. i18n:     *Gives the state of the quotation or sale order. The exception state is automatically set when a cancel operation occurs in the invoice validation (Invoice Exception) or in the packing list process (Shipping Exception). The 'Waiting Schedule' state is set when the invoice is confirmed but waiting for the scheduler to be on the date 'Date Ordered'.*

    *Gives the state of the quotation or sale order. The exception state is automatically set when a cancel operation occurs in the invoice validation (Invoice Exception) or in the packing list process (Shipping Exception). The 'Waiting Schedule' state is set when the invoice is confirmed but waiting for the scheduler to be on the date 'Date Ordered'.*

.. i18n: :partner_bank: Bank Account, many2one

:partner_bank: Bank Account, many2one

.. i18n:     *The bank account to pay to or to be paid from. It will be transferred to the invoice*

    *The bank account to pay to or to be paid from. It will be transferred to the invoice*

.. i18n: :abstract_line_ids: Order Lines, one2many, readonly

:abstract_line_ids: Order Lines, one2many, readonly

.. i18n: :invoiced_rate: Invoiced, float, readonly

:invoiced_rate: Invoiced, float, readonly

.. i18n: :pricelist_id: Pricelist, many2one, required, readonly

:pricelist_id: Pricelist, many2one, required, readonly

.. i18n: :advertising_agency: Advertising Agency, many2one

:advertising_agency: Advertising Agency, many2one

.. i18n: :project_id: Analytic Account, many2one, readonly

:project_id: Analytic Account, many2one, readonly

.. i18n: :has_supplier_direct_delivery: Has Supplier Direct Delivery, boolean, readonly

:has_supplier_direct_delivery: Has Supplier Direct Delivery, boolean, readonly

.. i18n: :child_so: Child Sales Order, one2many

:child_so: Child Sales Order, one2many

.. i18n: :incoterm: Incoterm, selection

:incoterm: Incoterm, selection

.. i18n: :published_customer: Published Customer, many2one

:published_customer: Published Customer, many2one

.. i18n: :partner_order_id: Ordering Contact, many2one, required, readonly

:partner_order_id: Ordering Contact, many2one, required, readonly

.. i18n:     *The name and address of the contact that requested the order or quotation.*

    *The name and address of the contact that requested the order or quotation.*

.. i18n: :picked_rate: Picked, float, readonly

:picked_rate: Picked, float, readonly

.. i18n: :partner_invoice_id: Invoice Address, many2one, required, readonly

:partner_invoice_id: Invoice Address, many2one, required, readonly

.. i18n: :amount_untaxed: Untaxed Amount, float, readonly

:amount_untaxed: Untaxed Amount, float, readonly

.. i18n: :invoice_type_id: Invoice Type, many2one

:invoice_type_id: Invoice Type, many2one

.. i18n: :picking_ids: Related Packings, one2many, readonly

:picking_ids: Related Packings, one2many, readonly

.. i18n:     *This is the list of picking list that have been generated for this invoice*

    *This is the list of picking list that have been generated for this invoice*

.. i18n: :amount_total: Total, float, readonly

:amount_total: Total, float, readonly

.. i18n: :name: Order Reference, char, required

:name: Order Reference, char, required

.. i18n: :partner_shipping_id: Shipping Address, many2one, required, readonly

:partner_shipping_id: Shipping Address, many2one, required, readonly

.. i18n: :customer_pricelist_id: Customer Pricelist, many2one

:customer_pricelist_id: Customer Pricelist, many2one

.. i18n: :price_type: Price method, selection, required

:price_type: Price method, selection, required

.. i18n: :case_ids: Related Cases, one2many

:case_ids: Related Cases, one2many

.. i18n: :dept: Department, many2one

:dept: Department, many2one

.. i18n: :shipped: Picked, boolean, readonly

:shipped: Picked, boolean, readonly

.. i18n: :invoice_quantity: Invoice on, selection, required

:invoice_quantity: Invoice on, selection, required

.. i18n:     *The sale order will automatically create the invoice proposition (draft invoice). Ordered and delivered quantities may not be the same. You have to choose if you invoice based on ordered or shipped quantities. If the product is a service, shipped quantities means hours spent on the associated tasks.*

    *The sale order will automatically create the invoice proposition (draft invoice). Ordered and delivered quantities may not be the same. You have to choose if you invoice based on ordered or shipped quantities. If the product is a service, shipped quantities means hours spent on the associated tasks.*

.. i18n: :payment_type: Payment type, many2one

:payment_type: Payment type, many2one

.. i18n:     *The type of payment. It will be transferred to the invoice*

    *The type of payment. It will be transferred to the invoice*

.. i18n: :discount_campaign: Discount Campaign, many2one

:discount_campaign: Discount Campaign, many2one

.. i18n: :margin: Margin, float, readonly

:margin: Margin, float, readonly

.. i18n: Object: Sale Order line (sale.order.line)
.. i18n: #########################################

Object: Sale Order line (sale.order.line)
#########################################

.. i18n: :property_ids: Properties, many2many

:property_ids: Properties, many2many

.. i18n: :product_uos_qty: Quantity (UOS), float

:product_uos_qty: Quantity (UOS), float

.. i18n: :adv_issue: Advertising Issue, many2one

:adv_issue: Advertising Issue, many2one

.. i18n: :product_uom: Product UoM, many2one, required

:product_uom: Product UoM, many2one, required

.. i18n: :sequence: Sequence Number, integer

:sequence: Sequence Number, integer

.. i18n: :parent_fleet_id: Fleet, many2one

:parent_fleet_id: Fleet, many2one

.. i18n: :price_unit: Unit Price, float, required

:price_unit: Unit Price, float, required

.. i18n: :product_uom_qty: Quantity (UoM), float, required

:product_uom_qty: Quantity (UoM), float, required

.. i18n: :price_subtotal: Subtotal w/o tax, float, readonly

:price_subtotal: Subtotal w/o tax, float, readonly

.. i18n: :maintenance_end_date: Maintenance End Date, date

:maintenance_end_date: Maintenance End Date, date

.. i18n: :deliveries: Planned Deliveries, float, readonly

:deliveries: Planned Deliveries, float, readonly

.. i18n: :is_supplier_direct_delivery_advised: Is Supplier Direct Delivery Advised?, boolean, readonly

:is_supplier_direct_delivery_advised: Is Supplier Direct Delivery Advised?, boolean, readonly

.. i18n: :size_x: Width, float

:size_x: Width, float

.. i18n: :size_y: Height, float

:size_y: Height, float

.. i18n: :size_z: Thickness, float

:size_z: Thickness, float

.. i18n: :product_uos: Product UOS, many2one

:product_uos: Product UOS, many2one

.. i18n: :purchase_order_line: Related Purchase Order Line, many2one

:purchase_order_line: Related Purchase Order Line, many2one

.. i18n: :production_lot_id: Production Lot, many2one

:production_lot_id: Production Lot, many2one

.. i18n: :number_packages: Number packages, integer, readonly

:number_packages: Number packages, integer, readonly

.. i18n: :invoiced: Invoiced, boolean, readonly

:invoiced: Invoiced, boolean, readonly

.. i18n: :move_ids: Inventory Moves, one2many, readonly

:move_ids: Inventory Moves, one2many, readonly

.. i18n: :analytics_id: Analytic Distribution, many2one

:analytics_id: Analytic Distribution, many2one

.. i18n: :from_date: Start of Validity, datetime

:from_date: Start of Validity, datetime

.. i18n: :page_reference: Reference of the Page, char

:page_reference: Reference of the Page, char

.. i18n: :delay: Delivery Delay, float, required

:delay: Delivery Delay, float, required

.. i18n: :price_unit_customer: Customer Unit Price, float

:price_unit_customer: Customer Unit Price, float

.. i18n: :state: Status, selection, required, readonly

:state: Status, selection, required, readonly

.. i18n: :maintenance_product_qty: Maintenance Product Quantity, integer

:maintenance_product_qty: Maintenance Product Quantity, integer

.. i18n: :order_partner_id: Customer, many2one

:order_partner_id: Customer, many2one

.. i18n: :is_supplier_direct_delivery: Is Direct Delivery?, boolean

:is_supplier_direct_delivery: Is Direct Delivery?, boolean

.. i18n: :product_packaging: Packaging, many2one

:product_packaging: Packaging, many2one

.. i18n: :maintenance_start_date: Maintenance Start Date, date

:maintenance_start_date: Maintenance Start Date, date

.. i18n: :type: Procure Method, selection, required

:type: Procure Method, selection, required

.. i18n: :fleet_id: Sub Fleet, many2one

:fleet_id: Sub Fleet, many2one

.. i18n: :maintenance_month_qty: Maintenance Month Quantity, integer, readonly

:maintenance_month_qty: Maintenance Month Quantity, integer, readonly

.. i18n: :procurement_id: Procurement, many2one

:procurement_id: Procurement, many2one

.. i18n: :order_fleet_id: Default Sale Order Sub Fleet, many2one

:order_fleet_id: Default Sale Order Sub Fleet, many2one

.. i18n: :order_id: Order Ref, many2one, required

:order_id: Order Ref, many2one, required

.. i18n: :layout_remark: Layout Remark, text

:layout_remark: Layout Remark, text

.. i18n: :price_subtotal_incl: Subtotal, float, readonly

:price_subtotal_incl: Subtotal, float, readonly

.. i18n: :discount: Discount (%), float

:discount: Discount (%), float

.. i18n: :prodlot_id: Production lot, many2one

:prodlot_id: Production lot, many2one

.. i18n:     *Production lot is used to put a serial number on the production*

    *Production lot is used to put a serial number on the production*

.. i18n: :to_date: End of Validity, datetime

:to_date: End of Validity, datetime

.. i18n: :price_net: Net Price, float, readonly

:price_net: Net Price, float, readonly

.. i18n: :customer_ref: Customer reference, char

:customer_ref: Customer reference, char

.. i18n: :tax_id: Taxes, many2many

:tax_id: Taxes, many2many

.. i18n: :is_maintenance: Is Maintenance, boolean

:is_maintenance: Is Maintenance, boolean

.. i18n: :name: Description, char, required

:name: Description, char, required

.. i18n: :expected_invoice_date: Expected Invoice Date, datetime

:expected_invoice_date: Expected Invoice Date, datetime

.. i18n: :invoice_lines: Invoice Lines, many2many, readonly

:invoice_lines: Invoice Lines, many2many, readonly

.. i18n: :notes: Notes, text

:notes: Notes, text

.. i18n: :purchase_order_state: Purchase Order State, char

:purchase_order_state: Purchase Order State, char

.. i18n: :purchase_order: Related Purchase Order, many2one

:purchase_order: Related Purchase Order, many2one

.. i18n: :prodlot_ids: Lots Assignation, one2many

:prodlot_ids: Lots Assignation, one2many

.. i18n:     *Production lot is used to put a serial number on the production*

    *Production lot is used to put a serial number on the production*

.. i18n: :product_id: Product, many2one

:product_id: Product, many2one

.. i18n: :th_weight: Weight, float

:th_weight: Weight, float

.. i18n: :y: Y of Product, float

:y: Y of Product, float

.. i18n: :x: X of Product, float

:x: X of Product, float

.. i18n: :layout_type: Layout Type, selection, required

:layout_type: Layout Type, selection, required

.. i18n: :z: Z of Product, float

:z: Z of Product, float

.. i18n: :margin: Margin, float, readonly

:margin: Margin, float, readonly

.. i18n: :address_allotment_id: Allotment Partner, many2one

:address_allotment_id: Allotment Partner, many2one

.. i18n: Object: sale.config.picking_policy (sale.config.picking_policy)
.. i18n: ###############################################################

Object: sale.config.picking_policy (sale.config.picking_policy)
###############################################################

.. i18n: :picking_policy: Packing Default Policy, selection, required

:picking_policy: Packing Default Policy, selection, required

.. i18n: :order_policy: Shipping Default Policy, selection, required

:order_policy: Shipping Default Policy, selection, required

.. i18n: :step: Steps To Deliver a Sale Order, selection, required

:step: Steps To Deliver a Sale Order, selection, required

.. i18n:     *By default, Open ERP is able to manage complex routing and paths of products in your warehouse and partner locations. This will configure the most common and simple methods to deliver products to the customer in one or two operations by the worker.*

    *By default, Open ERP is able to manage complex routing and paths of products in your warehouse and partner locations. This will configure the most common and simple methods to deliver products to the customer in one or two operations by the worker.*

.. i18n: :name: Name, char

:name: Name, char
