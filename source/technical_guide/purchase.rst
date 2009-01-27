
Module Purchase Management (*purchase*)
=======================================
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

.. index::
  single: Purchase order object
.. 


:origin: Origin, char

    *Reference of the document that generated this purchase order request.*

.. index::
  single: origin field
.. 




:has_supplier_direct_delivery: Has Supplier Direct Delivery, boolean, readonly



.. index::
  single: has_supplier_direct_delivery field
.. 




:order_line: Order Lines, one2many



.. index::
  single: order_line field
.. 




:invoiced_rate: Invoiced, float, readonly



.. index::
  single: invoiced_rate field
.. 




:internal_notes: Internal Note, text



.. index::
  single: internal_notes field
.. 




:carrier_id: Delivery method, many2one

    *Complete this field if you plan to invoice the shipping based on packings made.*

.. index::
  single: carrier_id field
.. 




:date_order: Date Ordered, date, required



.. index::
  single: date_order field
.. 




:partner_id: Supplier, many2one, required



.. index::
  single: partner_id field
.. 




:invoiced: Invoiced & Paid, boolean, readonly



.. index::
  single: invoiced field
.. 




:dest_address_id: Destination Address, many2one

    *Put an address if you want to deliver directly from the supplier to the customer.In this case, it will remove the warehouse link and set the customer location.*

.. index::
  single: dest_address_id field
.. 




:fiscal_position: Fiscal Position, many2one



.. index::
  single: fiscal_position field
.. 




:approvator: Approved by, many2one, readonly



.. index::
  single: approvator field
.. 




:location_id: Destination, many2one, required



.. index::
  single: location_id field
.. 




:journal_id: Journal, many2one



.. index::
  single: journal_id field
.. 




:amount_tax: Taxes, float, readonly



.. index::
  single: amount_tax field
.. 




:state: Order State, selection, readonly

    *The state of the purchase order or the quotation request. A quotation is a purchase order in a 'Draft' state. Then the order has to be confirmed by the user, the state switch to 'Confirmed'. Then the supplier must confirm the order to change the state to 'Approved'. When the purchase order is paid and received, the state becomes 'Done'. If a cancel action occurs in the invoice or in the reception of goods, the state becomes in exception.*

.. index::
  single: state field
.. 




:dm_campaign_purchase_line: DM Campaign Purchase Line, many2one



.. index::
  single: dm_campaign_purchase_line field
.. 




:pricelist_id: Pricelist, many2one, required

    *The pricelist sets the currency used for this purchase order. It also computes the supplier price for the selected products/quantities.*

.. index::
  single: pricelist_id field
.. 




:tender_id: Purchase Tender, many2one



.. index::
  single: tender_id field
.. 




:partner_address_id: Address, many2one, required



.. index::
  single: partner_address_id field
.. 




:warehouse_id: Warehouse, many2one



.. index::
  single: warehouse_id field
.. 




:amount_untaxed: Untaxed Amount, float, readonly



.. index::
  single: amount_untaxed field
.. 




:shipped_rate: Received, float, readonly



.. index::
  single: shipped_rate field
.. 




:partner_ref: Partner Ref., char



.. index::
  single: partner_ref field
.. 




:picking_ids: Picking List, one2many, readonly

    *This is the list of picking list that have been generated for this purchase*

.. index::
  single: picking_ids field
.. 




:date_approve: Date Approved, date, readonly



.. index::
  single: date_approve field
.. 




:amount_total: Total, float, readonly



.. index::
  single: amount_total field
.. 




:name: Order Reference, char, required



.. index::
  single: name field
.. 




:price_type: Price method, selection, required



.. index::
  single: price_type field
.. 




:invoice_id: Invoice, many2one, readonly



.. index::
  single: invoice_id field
.. 




:notes: Notes, text



.. index::
  single: notes field
.. 




:invoice_method: Invoicing Control, selection, required

    *From Order: a draft invoice will be pre-generated based on the purchase order. The accountant will just have to validate this invoice for control.
    From Picking: a draft invoice will be pre-genearted based on validated receptions.
    Manual: no invoice will be pre-generated. The accountant will have to encode manually.*

.. index::
  single: invoice_method field
.. 




:shipped: Received, boolean, readonly



.. index::
  single: shipped field
.. 




:validator: Validated by, many2one, readonly



.. index::
  single: validator field
.. 




:minimum_planned_date: Planned Date, datetime

    *This is computed as the minimum scheduled date of all purchase order lines' products.*

.. index::
  single: minimum_planned_date field
.. 



Object: Purchase Order lines
############################

.. index::
  single: Purchase Order lines object
.. 


:origin: Origin, char



.. index::
  single: origin field
.. 




:sale_order_line: Related Sale Order Line, many2one



.. index::
  single: sale_order_line field
.. 




:price_unit: Unit Price, float, required



.. index::
  single: price_unit field
.. 




:partner_address_id: Shipping address, many2one



.. index::
  single: partner_address_id field
.. 




:price_subtotal: Subtotal, float, readonly



.. index::
  single: price_subtotal field
.. 




:product_qty: Quantity, float, required



.. index::
  single: product_qty field
.. 




:production_lot_id: Production Lot, many2one



.. index::
  single: production_lot_id field
.. 




:product_uom: Product UOM, many2one, required



.. index::
  single: product_uom field
.. 




:analytics_id: Analytic Distribution, many2one



.. index::
  single: analytics_id field
.. 




:move_ids: Moves, one2many



.. index::
  single: move_ids field
.. 




:sale_order: Related Sale Order, many2one



.. index::
  single: sale_order field
.. 




:is_supplier_direct_delivery: Is Direct Delivery?, boolean



.. index::
  single: is_supplier_direct_delivery field
.. 




:account_analytic_id: Analytic Account, many2one



.. index::
  single: account_analytic_id field
.. 




:order_id: Order Ref, many2one, required



.. index::
  single: order_id field
.. 




:price_subtotal_incl: Subtotal, float, readonly



.. index::
  single: price_subtotal_incl field
.. 




:discount: Discount (%), float



.. index::
  single: discount field
.. 




:move_dest_id: Reservation Destination, many2one



.. index::
  single: move_dest_id field
.. 




:move_id: Reservation, many2one



.. index::
  single: move_id field
.. 




:product_id: Product, many2one



.. index::
  single: product_id field
.. 




:name: Description, char, required



.. index::
  single: name field
.. 




:date_planned: Scheduled date, datetime, required



.. index::
  single: date_planned field
.. 




:notes: Notes, text



.. index::
  single: notes field
.. 




:taxes_id: Taxes, many2many



.. index::
  single: taxes_id field
.. 




:customer_ref: Customer reference, char



.. index::
  single: customer_ref field
.. 

