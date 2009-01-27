
Module Margins in Sale Orders (*sale_margin*)
=============================================
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

.. index::
  single: report.account.invoice.product object
.. 


:name: Month, date, readonly



.. index::
  single: name field
.. 




:margin: Margin, float, readonly



.. index::
  single: margin field
.. 




:state: State, selection, readonly



.. index::
  single: state field
.. 




:amount: Amount, float, readonly



.. index::
  single: amount field
.. 




:product_id: Product, many2one, readonly



.. index::
  single: product_id field
.. 




:cost_price: Cost Price, float, readonly



.. index::
  single: cost_price field
.. 




:type: Type, selection, readonly



.. index::
  single: type field
.. 




:quantity: Quantity, float, readonly



.. index::
  single: quantity field
.. 



Object: report.account.invoice.category
#######################################

.. index::
  single: report.account.invoice.category object
.. 


:name: Month, date, readonly



.. index::
  single: name field
.. 




:margin: Margin, float, readonly



.. index::
  single: margin field
.. 




:amount: Amount, float, readonly



.. index::
  single: amount field
.. 




:state: State, selection, readonly



.. index::
  single: state field
.. 




:type: Type, selection, readonly



.. index::
  single: type field
.. 




:quantity: Quantity, float, readonly



.. index::
  single: quantity field
.. 




:categ_id: Categories, many2one, readonly



.. index::
  single: categ_id field
.. 




:cost_price: Cost Price, float, readonly



.. index::
  single: cost_price field
.. 



Object: report.account.invoice.partner
######################################

.. index::
  single: report.account.invoice.partner object
.. 


:name: Month, date, readonly



.. index::
  single: name field
.. 




:partner_id: Partner, many2one, readonly



.. index::
  single: partner_id field
.. 




:amount: Amount, float, readonly



.. index::
  single: amount field
.. 




:state: State, selection, readonly



.. index::
  single: state field
.. 




:type: Type, selection, readonly



.. index::
  single: type field
.. 




:quantity: Quantity, float, readonly



.. index::
  single: quantity field
.. 




:margin: Margin, float, readonly



.. index::
  single: margin field
.. 




:cost_price: Cost Price, float, readonly



.. index::
  single: cost_price field
.. 



Object: report.account.invoice.partner.product
##############################################

.. index::
  single: report.account.invoice.partner.product object
.. 


:name: Month, date, readonly



.. index::
  single: name field
.. 




:quantity: Quantity, float, readonly



.. index::
  single: quantity field
.. 




:partner_id: Partner, many2one, readonly



.. index::
  single: partner_id field
.. 




:amount: Amount, float, readonly



.. index::
  single: amount field
.. 




:state: State, selection, readonly



.. index::
  single: state field
.. 




:type: Type, selection, readonly



.. index::
  single: type field
.. 




:cost_price: Cost Price, float, readonly



.. index::
  single: cost_price field
.. 




:margin: Margin, float, readonly



.. index::
  single: margin field
.. 




:product_id: Product, many2one, readonly



.. index::
  single: product_id field
.. 



Object: report.account.invoice
##############################

.. index::
  single: report.account.invoice object
.. 


:name: Month, date, readonly



.. index::
  single: name field
.. 




:margin: Margin, float, readonly



.. index::
  single: margin field
.. 




:amount: Amount, float, readonly



.. index::
  single: amount field
.. 




:state: State, selection, readonly



.. index::
  single: state field
.. 




:quantity: Quantity, float, readonly



.. index::
  single: quantity field
.. 




:type: Type, selection, readonly



.. index::
  single: type field
.. 




:cost_price: Cost Price, float, readonly



.. index::
  single: cost_price field
.. 

