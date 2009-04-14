
.. i18n: .. module:: purchase
.. i18n:     :synopsis: Purchase Management (Official, Quality Certified)
.. i18n:     :noindex:
.. i18n: .. 

.. module:: purchase
    :synopsis: Purchase Management (Official, Quality Certified)
    :noindex:
.. 

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. i18n: Purchase Management (*purchase*)
.. i18n: ================================
.. i18n: :Module: purchase
.. i18n: :Name: Purchase Management
.. i18n: :Version: 5.0.1.1
.. i18n: :Author: Tiny
.. i18n: :Directory: purchase
.. i18n: :Web: http://www.openerp.com
.. i18n: :Official module: yes
.. i18n: :Quality certified: yes

Purchase Management (*purchase*)
================================
:Module: purchase
:Name: Purchase Management
:Version: 5.0.1.1
:Author: Tiny
:Directory: purchase
:Web: http://www.openerp.com
:Official module: yes
:Quality certified: yes

.. i18n: Description
.. i18n: -----------

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   Module for purchase management
.. i18n:       Request for quotation, Create Supplier Invoice, Print Order...

::

  Module for purchase management
      Request for quotation, Create Supplier Invoice, Print Order...

.. i18n: Dependencies
.. i18n: ------------

Dependencies
------------

.. i18n:  * :mod:`base`
.. i18n:  * :mod:`account`
.. i18n:  * :mod:`stock`
.. i18n:  * :mod:`process`

 * :mod:`base`
 * :mod:`account`
 * :mod:`stock`
 * :mod:`process`

.. i18n: Reports
.. i18n: -------

Reports
-------

.. i18n:  * Request for Quotation
.. i18n: 
.. i18n:  * Print Order

 * Request for Quotation

 * Print Order

.. i18n: Menus
.. i18n: -------

Menus
-------

.. i18n:  * Purchase Management
.. i18n:  * Purchase Management/Purchase Orders
.. i18n:  * Purchase Management/Purchase Orders/Request For Quotations
.. i18n:  * Purchase Management/Purchase Orders/Purchase Order Waiting Approval
.. i18n:  * Purchase Management/Purchase Orders/Purchase Orders in Progress
.. i18n:  * Purchase Management/New Purchase Order

 * Purchase Management
 * Purchase Management/Purchase Orders
 * Purchase Management/Purchase Orders/Request For Quotations
 * Purchase Management/Purchase Orders/Purchase Order Waiting Approval
 * Purchase Management/Purchase Orders/Purchase Orders in Progress
 * Purchase Management/New Purchase Order

.. i18n: Views
.. i18n: -----

Views
-----

.. i18n:  * purchase.order.calendar (calendar)
.. i18n:  * purchase.order.graph (graph)
.. i18n:  * purchase.order.form (form)
.. i18n:  * purchase.order.tree (tree)
.. i18n:  * purchase.order.line.form (form)
.. i18n:  * purchase.order.line.tree (tree)
.. i18n:  * \* INHERIT Packing list (form)
.. i18n:  * \* INHERIT res.partner.purchase.property.form.inherit (form)

 * purchase.order.calendar (calendar)
 * purchase.order.graph (graph)
 * purchase.order.form (form)
 * purchase.order.tree (tree)
 * purchase.order.line.form (form)
 * purchase.order.line.tree (tree)
 * \* INHERIT Packing list (form)
 * \* INHERIT res.partner.purchase.property.form.inherit (form)

.. i18n: Objects
.. i18n: -------

Objects
-------

.. i18n: Object: Purchase order (purchase.order)
.. i18n: #######################################

Object: Purchase order (purchase.order)
#######################################

.. i18n: :origin: Origin, char

:origin: Origin, char

.. i18n:     *Reference of the document that generated this purchase order request.*

    *Reference of the document that generated this purchase order request.*

.. i18n: :has_supplier_direct_delivery: Has Supplier Direct Delivery, boolean, readonly

:has_supplier_direct_delivery: Has Supplier Direct Delivery, boolean, readonly

.. i18n: :order_line: Order Lines, one2many

:order_line: Order Lines, one2many

.. i18n: :invoiced_rate: Invoiced, float, readonly

:invoiced_rate: Invoiced, float, readonly

.. i18n: :internal_notes: Internal Note, text

:internal_notes: Internal Note, text

.. i18n: :carrier_id: Delivery method, many2one

:carrier_id: Delivery method, many2one

.. i18n:     *Complete this field if you plan to invoice the shipping based on packings made.*

    *Complete this field if you plan to invoice the shipping based on packings made.*

.. i18n: :date_order: Date Ordered, date, required

:date_order: Date Ordered, date, required

.. i18n: :partner_id: Supplier, many2one, required

:partner_id: Supplier, many2one, required

.. i18n: :invoiced: Invoiced & Paid, boolean, readonly

:invoiced: Invoiced & Paid, boolean, readonly

.. i18n: :dest_address_id: Destination Address, many2one

:dest_address_id: Destination Address, many2one

.. i18n:     *Put an address if you want to deliver directly from the supplier to the customer.In this case, it will remove the warehouse link and set the customer location.*

    *Put an address if you want to deliver directly from the supplier to the customer.In this case, it will remove the warehouse link and set the customer location.*

.. i18n: :fiscal_position: Fiscal Position, many2one

:fiscal_position: Fiscal Position, many2one

.. i18n: :approvator: Approved by, many2one, readonly

:approvator: Approved by, many2one, readonly

.. i18n: :location_id: Destination, many2one, required

:location_id: Destination, many2one, required

.. i18n: :journal_id: Journal, many2one

:journal_id: Journal, many2one

.. i18n: :amount_tax: Taxes, float, readonly

:amount_tax: Taxes, float, readonly

.. i18n: :state: Order State, selection, readonly

:state: Order State, selection, readonly

.. i18n:     *The state of the purchase order or the quotation request. A quotation is a purchase order in a 'Draft' state. Then the order has to be confirmed by the user, the state switch to 'Confirmed'. Then the supplier must confirm the order to change the state to 'Approved'. When the purchase order is paid and received, the state becomes 'Done'. If a cancel action occurs in the invoice or in the reception of goods, the state becomes in exception.*

    *The state of the purchase order or the quotation request. A quotation is a purchase order in a 'Draft' state. Then the order has to be confirmed by the user, the state switch to 'Confirmed'. Then the supplier must confirm the order to change the state to 'Approved'. When the purchase order is paid and received, the state becomes 'Done'. If a cancel action occurs in the invoice or in the reception of goods, the state becomes in exception.*

.. i18n: :dm_campaign_purchase_line: DM Campaign Purchase Line, many2one

:dm_campaign_purchase_line: DM Campaign Purchase Line, many2one

.. i18n: :pricelist_id: Pricelist, many2one, required

:pricelist_id: Pricelist, many2one, required

.. i18n:     *The pricelist sets the currency used for this purchase order. It also computes the supplier price for the selected products/quantities.*

    *The pricelist sets the currency used for this purchase order. It also computes the supplier price for the selected products/quantities.*

.. i18n: :tender_id: Purchase Tender, many2one

:tender_id: Purchase Tender, many2one

.. i18n: :partner_address_id: Address, many2one, required

:partner_address_id: Address, many2one, required

.. i18n: :warehouse_id: Warehouse, many2one

:warehouse_id: Warehouse, many2one

.. i18n: :amount_untaxed: Untaxed Amount, float, readonly

:amount_untaxed: Untaxed Amount, float, readonly

.. i18n: :shipped_rate: Received, float, readonly

:shipped_rate: Received, float, readonly

.. i18n: :partner_ref: Partner Ref., char

:partner_ref: Partner Ref., char

.. i18n: :picking_ids: Picking List, one2many, readonly

:picking_ids: Picking List, one2many, readonly

.. i18n:     *This is the list of picking list that have been generated for this purchase*

    *This is the list of picking list that have been generated for this purchase*

.. i18n: :date_approve: Date Approved, date, readonly

:date_approve: Date Approved, date, readonly

.. i18n: :amount_total: Total, float, readonly

:amount_total: Total, float, readonly

.. i18n: :name: Order Reference, char, required

:name: Order Reference, char, required

.. i18n: :price_type: Price method, selection, required

:price_type: Price method, selection, required

.. i18n: :invoice_id: Invoice, many2one, readonly

:invoice_id: Invoice, many2one, readonly

.. i18n: :notes: Notes, text

:notes: Notes, text

.. i18n: :invoice_method: Invoicing Control, selection, required

:invoice_method: Invoicing Control, selection, required

.. i18n:     *From Order: a draft invoice will be pre-generated based on the purchase order. The accountant will just have to validate this invoice for control.
.. i18n:     From Picking: a draft invoice will be pre-genearted based on validated receptions.
.. i18n:     Manual: no invoice will be pre-generated. The accountant will have to encode manually.*

    *From Order: a draft invoice will be pre-generated based on the purchase order. The accountant will just have to validate this invoice for control.
    From Picking: a draft invoice will be pre-genearted based on validated receptions.
    Manual: no invoice will be pre-generated. The accountant will have to encode manually.*

.. i18n: :shipped: Received, boolean, readonly

:shipped: Received, boolean, readonly

.. i18n: :validator: Validated by, many2one, readonly

:validator: Validated by, many2one, readonly

.. i18n: :minimum_planned_date: Planned Date, datetime

:minimum_planned_date: Planned Date, datetime

.. i18n:     *This is computed as the minimum scheduled date of all purchase order lines' products.*

    *This is computed as the minimum scheduled date of all purchase order lines' products.*

.. i18n: Object: Purchase Order lines (purchase.order.line)
.. i18n: ##################################################

Object: Purchase Order lines (purchase.order.line)
##################################################

.. i18n: :origin: Origin, char

:origin: Origin, char

.. i18n: :sale_order_line: Related Sale Order Line, many2one

:sale_order_line: Related Sale Order Line, many2one

.. i18n: :price_unit: Unit Price, float, required

:price_unit: Unit Price, float, required

.. i18n: :partner_address_id: Shipping address, many2one

:partner_address_id: Shipping address, many2one

.. i18n: :price_subtotal: Subtotal, float, readonly

:price_subtotal: Subtotal, float, readonly

.. i18n: :product_qty: Quantity, float, required

:product_qty: Quantity, float, required

.. i18n: :production_lot_id: Production Lot, many2one

:production_lot_id: Production Lot, many2one

.. i18n: :product_uom: Product UOM, many2one, required

:product_uom: Product UOM, many2one, required

.. i18n: :analytics_id: Analytic Distribution, many2one

:analytics_id: Analytic Distribution, many2one

.. i18n: :move_ids: Moves, one2many

:move_ids: Moves, one2many

.. i18n: :sale_order: Related Sale Order, many2one

:sale_order: Related Sale Order, many2one

.. i18n: :is_supplier_direct_delivery: Is Direct Delivery?, boolean

:is_supplier_direct_delivery: Is Direct Delivery?, boolean

.. i18n: :account_analytic_id: Analytic Account, many2one

:account_analytic_id: Analytic Account, many2one

.. i18n: :order_id: Order Ref, many2one, required

:order_id: Order Ref, many2one, required

.. i18n: :price_subtotal_incl: Subtotal, float, readonly

:price_subtotal_incl: Subtotal, float, readonly

.. i18n: :discount: Discount (%), float

:discount: Discount (%), float

.. i18n: :move_dest_id: Reservation Destination, many2one

:move_dest_id: Reservation Destination, many2one

.. i18n: :move_id: Reservation, many2one

:move_id: Reservation, many2one

.. i18n: :product_id: Product, many2one

:product_id: Product, many2one

.. i18n: :name: Description, char, required

:name: Description, char, required

.. i18n: :date_planned: Scheduled date, datetime, required

:date_planned: Scheduled date, datetime, required

.. i18n: :notes: Notes, text

:notes: Notes, text

.. i18n: :taxes_id: Taxes, many2many

:taxes_id: Taxes, many2many

.. i18n: :customer_ref: Customer reference, char

:customer_ref: Customer reference, char
