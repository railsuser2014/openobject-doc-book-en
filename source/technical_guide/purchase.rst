
Purchase Management (*purchase*)
================================
:Module: purchase
:Name: Purchase Management
:Version: 5.0.1.1
:Directory: purchase
:Web: http://www.openerp.com

Description
-----------

::

  Module for purchase management
      Request for quotation, Create Supplier Invoice, Print Order...

Dependencies
------------

 * base - installed
 * account - installed
 * stock - installed
 * process - installed

Reports
-------

 * Request for Quotation

 * Purchase Order

Menus
-------

 * Purchase Management
 * Purchase Management/Purchase Orders
 * Purchase Management/Purchase Orders/Request For Quotations
 * Purchase Management/Purchase Orders/Purchase Order Waiting Approval
 * Purchase Management/Purchase Orders/Purchase Orders in Progress
 * Purchase Management/New Purchase Order

Views
-----

 * purchase.order.calendar (calendar)
 * purchase.order.graph (graph)
 * purchase.order.form (form)
 * purchase.order.tree (tree)
 * purchase.order.line.form (form)
 * purchase.order.line.tree (tree)
 * \* INHERIT Packing list (form)
 * \* INHERIT res.partner.purchase.property.form.inherit (form)


Objects
-------

Object: Purchase order
######################



:origin: Origin, char

    *Reference of the document that generated this purchase order request.*



:has_supplier_direct_delivery: Has Supplier Direct Delivery, boolean, readonly





:order_line: Order Lines, one2many





:invoiced_rate: Invoiced, float, readonly





:internal_notes: Internal Note, text





:carrier_id: Delivery method, many2one

    *Complete this field if you plan to invoice the shipping based on packings made.*



:date_order: Date Ordered, date, required





:partner_id: Supplier, many2one, required





:invoiced: Invoiced & Paid, boolean, readonly





:dest_address_id: Destination Address, many2one

    *Put an address if you want to deliver directly from the supplier to the customer.In this case, it will remove the warehouse link and set the customer location.*



:fiscal_position: Fiscal Position, many2one





:approvator: Approved by, many2one, readonly





:location_id: Destination, many2one, required





:journal_id: Journal, many2one





:amount_tax: Taxes, float, readonly





:state: Order State, selection, readonly

    *The state of the purchase order or the quotation request. A quotation is a purchase order in a 'Draft' state. Then the order has to be confirmed by the user, the state switch to 'Confirmed'. Then the supplier must confirm the order to change the state to 'Approved'. When the purchase order is paid and received, the state becomes 'Done'. If a cancel action occurs in the invoice or in the reception of goods, the state becomes in exception.*



:dm_campaign_purchase_line: DM Campaign Purchase Line, many2one





:pricelist_id: Pricelist, many2one, required

    *The pricelist sets the currency used for this purchase order. It also computes the supplier price for the selected products/quantities.*



:tender_id: Purchase Tender, many2one





:partner_address_id: Address, many2one, required





:warehouse_id: Warehouse, many2one





:amount_untaxed: Untaxed Amount, float, readonly





:shipped_rate: Received, float, readonly





:partner_ref: Partner Ref., char





:picking_ids: Picking List, one2many, readonly

    *This is the list of picking list that have been generated for this purchase*



:date_approve: Date Approved, date, readonly





:amount_total: Total, float, readonly





:name: Order Reference, char, required





:price_type: Price method, selection, required





:invoice_id: Invoice, many2one, readonly





:notes: Notes, text





:invoice_method: Invoicing Control, selection, required

    *From Order: a draft invoice will be pre-generated based on the purchase order. The accountant will just have to validate this invoice for control.
    From Picking: a draft invoice will be pre-genearted based on validated receptions.
    Manual: no invoice will be pre-generated. The accountant will have to encode manually.*



:shipped: Received, boolean, readonly





:validator: Validated by, many2one, readonly





:minimum_planned_date: Planned Date, datetime

    *This is computed as the minimum scheduled date of all purchase order lines' products.*


Object: Purchase Order lines
############################



:origin: Origin, char





:sale_order_line: Related Sale Order Line, many2one





:price_unit: Unit Price, float, required





:partner_address_id: Shipping address, many2one





:price_subtotal: Subtotal, float, readonly





:product_qty: Quantity, float, required





:production_lot_id: Production Lot, many2one





:product_uom: Product UOM, many2one, required





:analytics_id: Analytic Distribution, many2one





:move_ids: Moves, one2many





:sale_order: Related Sale Order, many2one





:is_supplier_direct_delivery: Is Direct Delivery?, boolean





:account_analytic_id: Analytic Account, many2one





:order_id: Order Ref, many2one, required





:price_subtotal_incl: Subtotal, float, readonly





:discount: Discount (%), float





:move_dest_id: Reservation Destination, many2one





:move_id: Reservation, many2one





:product_id: Product, many2one





:name: Description, char, required





:date_planned: Scheduled date, datetime, required





:notes: Notes, text





:taxes_id: Taxes, many2many





:customer_ref: Customer reference, char


