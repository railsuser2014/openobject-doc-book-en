
Margins in Sale Orders (*sale_margin*)
======================================
:Module: sale_margin
:Name: Margins in Sale Orders
:Version: 5.0.1.0
:Directory: sale_margin
:Web: 

Description
-----------

::

  None

Dependencies
------------

 * sale - installed
 * account - installed

Reports
-------

None


Menus
-------

 * Financial Management/Reporting/Invoice
 * Financial Management/Reporting/Invoice/This Month
 * Financial Management/Reporting/Invoice/This Month/Invoices by Product
 * Financial Management/Reporting/Invoice/All Months
 * Financial Management/Reporting/Invoice/All Months/Invoices by Product
 * Financial Management/Reporting/Invoice/This Month/Invoices by Category
 * Financial Management/Reporting/Invoice/All Months/Invoices by Category
 * Financial Management/Reporting/Invoice/This Month/Invoices by Partner
 * Financial Management/Reporting/Invoice/All Months/Invoices by Partner
 * Financial Management/Reporting/Invoice/This Month/Invoices by Partner and Product
 * Financial Management/Reporting/Invoice/All Months/Invoices by Partner and Product
 * Financial Management/Reporting/Invoice/This Month/Invoices
 * Financial Management/Reporting/Invoice/All Months/Invoices

Views
-----

 * \* INHERIT sale.order.margin.view.form (form)
 * \* INHERIT sale.order.margin.view.tree (tree)
 * \* INHERIT sale.order.margin.line.view.tree (tree)
 * \* INHERIT picking.margin.view.form (form)
 * report.account.invoice.product.tree (tree)
 * report.account.invoice.category.tree (tree)
 * report.account.invoice.partner.tree (tree)
 * report.account.invoice.partner.product.tree (tree)
 * report.account.invoice (tree)


Objects
-------

Object: report.account.invoice.product
######################################



:name: Month, date, readonly





:margin: Margin, float, readonly





:state: State, selection, readonly





:amount: Amount, float, readonly





:product_id: Product, many2one, readonly





:cost_price: Cost Price, float, readonly





:type: Type, selection, readonly





:quantity: Quantity, float, readonly




Object: report.account.invoice.category
#######################################



:name: Month, date, readonly





:margin: Margin, float, readonly





:amount: Amount, float, readonly





:state: State, selection, readonly





:type: Type, selection, readonly





:quantity: Quantity, float, readonly





:categ_id: Categories, many2one, readonly





:cost_price: Cost Price, float, readonly




Object: report.account.invoice.partner
######################################



:name: Month, date, readonly





:partner_id: Partner, many2one, readonly





:amount: Amount, float, readonly





:state: State, selection, readonly





:type: Type, selection, readonly





:quantity: Quantity, float, readonly





:margin: Margin, float, readonly





:cost_price: Cost Price, float, readonly




Object: report.account.invoice.partner.product
##############################################



:name: Month, date, readonly





:quantity: Quantity, float, readonly





:partner_id: Partner, many2one, readonly





:amount: Amount, float, readonly





:state: State, selection, readonly





:type: Type, selection, readonly





:cost_price: Cost Price, float, readonly





:margin: Margin, float, readonly





:product_id: Product, many2one, readonly




Object: report.account.invoice
##############################



:name: Month, date, readonly





:margin: Margin, float, readonly





:amount: Amount, float, readonly





:state: State, selection, readonly





:quantity: Quantity, float, readonly





:type: Type, selection, readonly





:cost_price: Cost Price, float, readonly


