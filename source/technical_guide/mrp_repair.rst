
Module Products Repairs Module (*mrp_repair*)
=============================================
:Module: mrp_repair
:Name: Products Repairs Module
:Version: 5.0.1.0
:Directory: mrp_repair
:Web: 

Description
-----------

::

  The aim is to have a complete module to manage all products repairs. The following topics should be covered by this module:
             * Add/remove products in the reparation
             * Impact for stocks
             * Invoicing (products and/or services)
             * Warranty concept
             * Repair quotation report
             * Notes for the technician and for the final customer

Dependencies
------------

 * base - installed
 * sale - installed
 * account - installed

Reports
-------

 * Quotation / Order

Menus
-------

 * Manufacturing/Repairs
 * Manufacturing/Repairs/Repairs in quotation
 * Manufacturing/Repairs/Repairs in progress
 * Manufacturing/Repairs/Repairs Ready to Start
 * Manufacturing/Repairs/Repairs to be invoiced
 * Manufacturing/Repairs/New Repair

Views
-----

 * mrp.repair.form (form)
 * mrp.repair.tree (tree)


Objects
-------

Object: Repairs Order
#####################

.. index::
  single: Repairs Order object
.. 


:operations: Operation Lines, one2many, readonly



.. index::
  single: operations field
.. 




:address_id: Delivery Address, many2one



.. index::
  single: address_id field
.. 




:internal_notes: Internal Notes, text



.. index::
  single: internal_notes field
.. 




:quotation_notes: Quotation Notes, text



.. index::
  single: quotation_notes field
.. 




:partner_id: Partner, many2one

    *This field allow you to choose the parner that will be invoiced and delivered*

.. index::
  single: partner_id field
.. 




:invoiced: Invoiced, boolean, readonly



.. index::
  single: invoiced field
.. 




:amount_untaxed: Untaxed Amount, float, readonly



.. index::
  single: amount_untaxed field
.. 




:location_id: Current Location, many2one, required, readonly



.. index::
  single: location_id field
.. 




:amount_tax: Taxes, float, readonly



.. index::
  single: amount_tax field
.. 




:state: Repair State, selection, readonly

    *Gives the state of the Repair Order*

.. index::
  single: state field
.. 




:pricelist_id: Pricelist, many2one

    *The pricelist comes from the selected partner, by default.*

.. index::
  single: pricelist_id field
.. 




:amount_total: Total, float, readonly



.. index::
  single: amount_total field
.. 




:prodlot_id: Lot Number, many2one



.. index::
  single: prodlot_id field
.. 




:partner_invoice_id: Invoicing Address, many2one



.. index::
  single: partner_invoice_id field
.. 




:move_id: Move, many2one, required, readonly



.. index::
  single: move_id field
.. 




:name: Repair Ref, char, required



.. index::
  single: name field
.. 




:product_id: Product to Repair, many2one, required, readonly



.. index::
  single: product_id field
.. 




:guarantee_limit: Guarantee limit, date

    *The garantee limit is computed as: last move date + warranty defined on selected product. If the current date is below the garantee limit, each operation and fee you will add will be set as 'not to invoiced' by default. Note that you can change manually afterwards.*

.. index::
  single: guarantee_limit field
.. 




:deliver_bool: Deliver, boolean

    *Check this box if you want to manage the delivery once the product is repaired. If cheked, it will create a packing with selected product. Note that you can select the locations in the Info tab, if you have the extended view.*

.. index::
  single: deliver_bool field
.. 




:invoice_method: Invoice Method, selection, required, readonly

    *This field allow you to change the workflow of the repair order. If value selected is different from 'No Invoice', it also allow you to select the pricelist and invoicing address.*

.. index::
  single: invoice_method field
.. 




:location_dest_id: Delivery Location, many2one, readonly



.. index::
  single: location_dest_id field
.. 




:invoice_id: Invoice, many2one, readonly



.. index::
  single: invoice_id field
.. 




:fees_lines: Fees Lines, one2many, readonly



.. index::
  single: fees_lines field
.. 




:repaired: Repaired, boolean, readonly



.. index::
  single: repaired field
.. 




:picking_id: Packing, many2one, readonly



.. index::
  single: picking_id field
.. 



Object: Repair Operations Lines
###############################

.. index::
  single: Repair Operations Lines object
.. 


:product_id: Product, many2one, required



.. index::
  single: product_id field
.. 




:product_uom: Product UoM, many2one, required



.. index::
  single: product_uom field
.. 




:repair_id: Repair Order Ref, many2one



.. index::
  single: repair_id field
.. 




:type: Type, selection, required



.. index::
  single: type field
.. 




:price_unit: Unit Price, float, required



.. index::
  single: price_unit field
.. 




:product_uom_qty: Quantity (UoM), float, required



.. index::
  single: product_uom_qty field
.. 




:price_subtotal: Subtotal, float, readonly



.. index::
  single: price_subtotal field
.. 




:name: Description, char, required



.. index::
  single: name field
.. 




:to_invoice: To Invoice, boolean



.. index::
  single: to_invoice field
.. 




:state: Status, selection, required, readonly



.. index::
  single: state field
.. 




:location_dest_id: Dest. Location, many2one, required



.. index::
  single: location_dest_id field
.. 




:tax_id: Taxes, many2many



.. index::
  single: tax_id field
.. 




:location_id: Source Location, many2one, required



.. index::
  single: location_id field
.. 




:invoice_line_id: Invoice Line, many2one, readonly



.. index::
  single: invoice_line_id field
.. 




:move_id: Inventory Move, many2one, readonly



.. index::
  single: move_id field
.. 




:invoiced: Invoiced, boolean, readonly



.. index::
  single: invoiced field
.. 



Object: Repair Fees line
########################

.. index::
  single: Repair Fees line object
.. 


:name: Description, char, required



.. index::
  single: name field
.. 




:product_uom: Product UoM, many2one, required



.. index::
  single: product_uom field
.. 




:repair_id: Repair Order Ref, many2one, required



.. index::
  single: repair_id field
.. 




:price_unit: Unit Price, float, required



.. index::
  single: price_unit field
.. 




:product_uom_qty: Quantity, float, required



.. index::
  single: product_uom_qty field
.. 




:price_subtotal: Subtotal, float, readonly



.. index::
  single: price_subtotal field
.. 




:to_invoice: To Invoice, boolean



.. index::
  single: to_invoice field
.. 




:invoiced: Invoiced, boolean, readonly



.. index::
  single: invoiced field
.. 




:tax_id: Taxes, many2many



.. index::
  single: tax_id field
.. 




:invoice_line_id: Invoice Line, many2one, readonly



.. index::
  single: invoice_line_id field
.. 




:product_id: Product, many2one



.. index::
  single: product_id field
.. 

