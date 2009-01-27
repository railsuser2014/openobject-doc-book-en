
Module Point Of Sale (*point_of_sale*)
======================================
:Module: point_of_sale
:Name: Point Of Sale
:Version: 5.0.1.0
:Directory: point_of_sale
:Web: 

Description
-----------

::

  Main features :
   - Fast encoding of the sale.
   - Allow to choose one payment mode (the quick way) or to split the payment between several payment mode.
   - Computation of the amount of money to return.
   - Create and confirm picking list automatically.
   - Allow the user to create invoice automatically.
   - Allow to refund former sales.

Dependencies
------------

 * sale - installed
 * purchase - installed
 * account - installed
 * account_tax_include - installed

Reports
-------

 * Receipt

 * Invoice

 * Details of Sales

 * Sales (summary)

 * Pos Lines

Menus
-------

 * Point of Sale
 * Point of Sale/Point of Sale
 * Point of Sale/Configuration
 * Point of Sale/Configuration/Default journals
 * Point of Sale/Point of Sale/Orders of the day
 * Point of Sale/Point of Sale/All orders
 * Point of Sale/POS Lines
 * Point of Sale/POS Lines/POS Lines of the day
 * Point of Sale/Reporting
 * Point of Sale/Reporting/Sales of the day
 * Point of Sale/Reporting/Sales of the month
 * Point of Sale/Reporting/All the sales

Views
-----

 * pos.order (form)
 * Sales (tree)
 * Sale lines (tree)
 * Sale line (form)
 * report.trans.pos.user.form (form)
 * Sales by user (tree)


Objects
-------

Object: Point of Sale journal configuration.
############################################

.. index::
  single: Point of Sale journal configuration. object
.. 


:code: Code, char



.. index::
  single: code field
.. 




:name: Description, char



.. index::
  single: name field
.. 




:journal_id: Journal, many2one



.. index::
  single: journal_id field
.. 



Object: Point of Sale
#####################

.. index::
  single: Point of Sale object
.. 


:sale_journal: Journal, many2one, required, readonly



.. index::
  single: sale_journal field
.. 




:date_validity: Validity Date, date, required



.. index::
  single: date_validity field
.. 




:account_move: Account Entry, many2one, readonly



.. index::
  single: account_move field
.. 




:date_order: Date Ordered, date, readonly



.. index::
  single: date_order field
.. 




:partner_id: Partner, many2one, readonly



.. index::
  single: partner_id field
.. 




:last_out_picking: Last output picking, many2one, readonly



.. index::
  single: last_out_picking field
.. 




:nb_print: Number of print, integer, readonly



.. index::
  single: nb_print field
.. 




:note: Notes, text



.. index::
  single: note field
.. 




:user_id: Salesman, many2one, readonly



.. index::
  single: user_id field
.. 




:pickings: Picking, one2many, readonly



.. index::
  single: pickings field
.. 




:invoice_wanted: Create invoice, boolean



.. index::
  single: invoice_wanted field
.. 




:amount_tax: Taxes, float, readonly



.. index::
  single: amount_tax field
.. 




:state: State, selection, readonly



.. index::
  single: state field
.. 




:pricelist_id: Pricelist, many2one, required, readonly



.. index::
  single: pricelist_id field
.. 




:amount_return: unknown, float, readonly



.. index::
  single: amount_return field
.. 




:account_receivable: Default Receivable, many2one, required, readonly



.. index::
  single: account_receivable field
.. 




:amount_paid: unknown, float, readonly



.. index::
  single: amount_paid field
.. 




:amount_total: Total, float, readonly



.. index::
  single: amount_total field
.. 




:name: Order Description, char, required, readonly



.. index::
  single: name field
.. 




:invoice_id: Invoice, many2one, readonly



.. index::
  single: invoice_id field
.. 




:lines: Order Lines, one2many, readonly



.. index::
  single: lines field
.. 




:shop_id: Shop, many2one, required, readonly



.. index::
  single: shop_id field
.. 




:payments: Order Payments, one2many, readonly



.. index::
  single: payments field
.. 



Object: Lines of Point of Sale
##############################

.. index::
  single: Lines of Point of Sale object
.. 


:create_date: Creation date, datetime, readonly



.. index::
  single: create_date field
.. 




:name: Line Description, char



.. index::
  single: name field
.. 




:order_id: Order Ref, many2one



.. index::
  single: order_id field
.. 




:price_unit: Unit Price, float, required



.. index::
  single: price_unit field
.. 




:price_subtotal: Subtotal, float, readonly



.. index::
  single: price_subtotal field
.. 




:qty: Quantity, float



.. index::
  single: qty field
.. 




:discount: Discount (%), float



.. index::
  single: discount field
.. 




:product_id: Product, many2one, required



.. index::
  single: product_id field
.. 



Object: Pos Payment
###################

.. index::
  single: Pos Payment object
.. 


:payment_id: Payment Term, many2one



.. index::
  single: payment_id field
.. 




:payment_date: Payment date, date, required



.. index::
  single: payment_date field
.. 




:payment_name: Payment name, char



.. index::
  single: payment_name field
.. 




:name: Description, char



.. index::
  single: name field
.. 




:order_id: Order Ref, many2one, required



.. index::
  single: order_id field
.. 




:journal_id: Journal, many2one, required



.. index::
  single: journal_id field
.. 




:amount: Amount, float, required



.. index::
  single: amount field
.. 




:payment_nb: Piece number, char



.. index::
  single: payment_nb field
.. 



Object: transaction for the pos
###############################

.. index::
  single: transaction for the pos object
.. 


:user_id: User, many2one, readonly



.. index::
  single: user_id field
.. 




:no_trans: Number of transaction, float, readonly



.. index::
  single: no_trans field
.. 




:invoice_id: Invoice, many2one, readonly



.. index::
  single: invoice_id field
.. 




:journal_id: Journal, many2one, readonly



.. index::
  single: journal_id field
.. 




:date_create: Date, char, readonly



.. index::
  single: date_create field
.. 




:amount: Amount, float, readonly



.. index::
  single: amount field
.. 

