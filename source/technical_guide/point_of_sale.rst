
.. module:: point_of_sale
    :synopsis: Point Of Sale
    :noindex:
.. 

Point Of Sale (*point_of_sale*)
===============================
:Module: point_of_sale
:Name: Point Of Sale
:Version: 5.0.1.0
:Directory: point_of_sale
:Web: 
:Is certified: yes

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

Object: Point of Sale journal configuration. (pos.config.journal)
#################################################################



:code: Code, char





:name: Description, char





:journal_id: Journal, many2one




Object: Point of Sale (pos.order)
#################################



:sale_journal: Journal, many2one, required, readonly





:date_validity: Validity Date, date, required





:account_move: Account Entry, many2one, readonly





:date_order: Date Ordered, date, readonly





:partner_id: Partner, many2one, readonly





:last_out_picking: Last output picking, many2one, readonly





:nb_print: Number of print, integer, readonly





:note: Notes, text





:user_id: Salesman, many2one, readonly





:pickings: Picking, one2many, readonly





:invoice_wanted: Create invoice, boolean





:amount_tax: Taxes, float, readonly





:state: State, selection, readonly





:pricelist_id: Pricelist, many2one, required, readonly





:amount_return: unknown, float, readonly





:account_receivable: Default Receivable, many2one, required, readonly





:amount_paid: unknown, float, readonly





:amount_total: Total, float, readonly





:name: Order Description, char, required, readonly





:invoice_id: Invoice, many2one, readonly





:lines: Order Lines, one2many, readonly





:shop_id: Shop, many2one, required, readonly





:payments: Order Payments, one2many, readonly




Object: Lines of Point of Sale (pos.order.line)
###############################################



:create_date: Creation date, datetime, readonly





:name: Line Description, char





:order_id: Order Ref, many2one





:price_unit: Unit Price, float, required





:price_subtotal: Subtotal, float, readonly





:qty: Quantity, float





:discount: Discount (%), float





:product_id: Product, many2one, required




Object: Pos Payment (pos.payment)
#################################



:payment_id: Payment Term, many2one





:payment_date: Payment date, date, required





:payment_name: Payment name, char





:name: Description, char





:order_id: Order Ref, many2one, required





:journal_id: Journal, many2one, required





:amount: Amount, float, required





:payment_nb: Piece number, char




Object: transaction for the pos (report.transaction.pos)
########################################################



:user_id: User, many2one, readonly





:no_trans: Number of transaction, float, readonly





:invoice_id: Invoice, many2one, readonly





:journal_id: Journal, many2one, readonly





:date_create: Date, char, readonly





:amount: Amount, float, readonly


