
.. i18n: .. module:: sale_margin
.. i18n:     :synopsis: Margins in Sale Orders 
.. i18n:     :noindex:
.. i18n: .. 

.. module:: sale_margin
    :synopsis: Margins in Sale Orders 
    :noindex:
.. 

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. i18n: Margins in Sale Orders (*sale_margin*)
.. i18n: ======================================
.. i18n: :Module: sale_margin
.. i18n: :Name: Margins in Sale Orders
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: sale_margin
.. i18n: :Web: 
.. i18n: :Official module: no
.. i18n: :Quality certified: no

Margins in Sale Orders (*sale_margin*)
======================================
:Module: sale_margin
:Name: Margins in Sale Orders
:Version: 5.0.1.0
:Author: Tiny
:Directory: sale_margin
:Web: 
:Official module: no
:Quality certified: no

.. i18n: Description
.. i18n: -----------

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   None

::

  None

.. i18n: Dependencies
.. i18n: ------------

Dependencies
------------

.. i18n:  * :mod:`sale`
.. i18n:  * :mod:`account`

 * :mod:`sale`
 * :mod:`account`

.. i18n: Reports
.. i18n: -------

Reports
-------

.. i18n: None

None

.. i18n: Menus
.. i18n: -------

Menus
-------

.. i18n:  * Financial Management/Reporting/Invoice
.. i18n:  * Financial Management/Reporting/Invoice/This Month
.. i18n:  * Financial Management/Reporting/Invoice/This Month/Invoices by Product
.. i18n:  * Financial Management/Reporting/Invoice/All Months
.. i18n:  * Financial Management/Reporting/Invoice/All Months/Invoices by Product
.. i18n:  * Financial Management/Reporting/Invoice/This Month/Invoices by Category
.. i18n:  * Financial Management/Reporting/Invoice/All Months/Invoices by Category
.. i18n:  * Financial Management/Reporting/Invoice/This Month/Invoices by Partner
.. i18n:  * Financial Management/Reporting/Invoice/All Months/Invoices by Partner
.. i18n:  * Financial Management/Reporting/Invoice/This Month/Invoices by Partner and Product
.. i18n:  * Financial Management/Reporting/Invoice/All Months/Invoices by Partner and Product
.. i18n:  * Financial Management/Reporting/Invoice/This Month/Invoices
.. i18n:  * Financial Management/Reporting/Invoice/All Months/Invoices

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

.. i18n: Views
.. i18n: -----

Views
-----

.. i18n:  * \* INHERIT sale.order.margin.view.form (form)
.. i18n:  * \* INHERIT sale.order.margin.view.tree (tree)
.. i18n:  * \* INHERIT sale.order.margin.line.view.tree (tree)
.. i18n:  * \* INHERIT picking.margin.view.form (form)
.. i18n:  * report.account.invoice.product.tree (tree)
.. i18n:  * report.account.invoice.category.tree (tree)
.. i18n:  * report.account.invoice.partner.tree (tree)
.. i18n:  * report.account.invoice.partner.product.tree (tree)
.. i18n:  * report.account.invoice (tree)

 * \* INHERIT sale.order.margin.view.form (form)
 * \* INHERIT sale.order.margin.view.tree (tree)
 * \* INHERIT sale.order.margin.line.view.tree (tree)
 * \* INHERIT picking.margin.view.form (form)
 * report.account.invoice.product.tree (tree)
 * report.account.invoice.category.tree (tree)
 * report.account.invoice.partner.tree (tree)
 * report.account.invoice.partner.product.tree (tree)
 * report.account.invoice (tree)

.. i18n: Objects
.. i18n: -------

Objects
-------

.. i18n: Object: report.account.invoice.product (report.account.invoice.product)
.. i18n: #######################################################################

Object: report.account.invoice.product (report.account.invoice.product)
#######################################################################

.. i18n: :name: Month, date, readonly

:name: Month, date, readonly

.. i18n: :margin: Margin, float, readonly

:margin: Margin, float, readonly

.. i18n: :state: State, selection, readonly

:state: State, selection, readonly

.. i18n: :amount: Amount, float, readonly

:amount: Amount, float, readonly

.. i18n: :product_id: Product, many2one, readonly

:product_id: Product, many2one, readonly

.. i18n: :cost_price: Cost Price, float, readonly

:cost_price: Cost Price, float, readonly

.. i18n: :type: Type, selection, readonly

:type: Type, selection, readonly

.. i18n: :quantity: Quantity, float, readonly

:quantity: Quantity, float, readonly

.. i18n: Object: report.account.invoice.category (report.account.invoice.category)
.. i18n: #########################################################################

Object: report.account.invoice.category (report.account.invoice.category)
#########################################################################

.. i18n: :name: Month, date, readonly

:name: Month, date, readonly

.. i18n: :margin: Margin, float, readonly

:margin: Margin, float, readonly

.. i18n: :amount: Amount, float, readonly

:amount: Amount, float, readonly

.. i18n: :state: State, selection, readonly

:state: State, selection, readonly

.. i18n: :type: Type, selection, readonly

:type: Type, selection, readonly

.. i18n: :quantity: Quantity, float, readonly

:quantity: Quantity, float, readonly

.. i18n: :categ_id: Categories, many2one, readonly

:categ_id: Categories, many2one, readonly

.. i18n: :cost_price: Cost Price, float, readonly

:cost_price: Cost Price, float, readonly

.. i18n: Object: report.account.invoice.partner (report.account.invoice.partner)
.. i18n: #######################################################################

Object: report.account.invoice.partner (report.account.invoice.partner)
#######################################################################

.. i18n: :name: Month, date, readonly

:name: Month, date, readonly

.. i18n: :partner_id: Partner, many2one, readonly

:partner_id: Partner, many2one, readonly

.. i18n: :amount: Amount, float, readonly

:amount: Amount, float, readonly

.. i18n: :state: State, selection, readonly

:state: State, selection, readonly

.. i18n: :type: Type, selection, readonly

:type: Type, selection, readonly

.. i18n: :quantity: Quantity, float, readonly

:quantity: Quantity, float, readonly

.. i18n: :margin: Margin, float, readonly

:margin: Margin, float, readonly

.. i18n: :cost_price: Cost Price, float, readonly

:cost_price: Cost Price, float, readonly

.. i18n: Object: report.account.invoice.partner.product (report.account.invoice.partner.product)
.. i18n: #######################################################################################

Object: report.account.invoice.partner.product (report.account.invoice.partner.product)
#######################################################################################

.. i18n: :name: Month, date, readonly

:name: Month, date, readonly

.. i18n: :quantity: Quantity, float, readonly

:quantity: Quantity, float, readonly

.. i18n: :partner_id: Partner, many2one, readonly

:partner_id: Partner, many2one, readonly

.. i18n: :amount: Amount, float, readonly

:amount: Amount, float, readonly

.. i18n: :state: State, selection, readonly

:state: State, selection, readonly

.. i18n: :type: Type, selection, readonly

:type: Type, selection, readonly

.. i18n: :cost_price: Cost Price, float, readonly

:cost_price: Cost Price, float, readonly

.. i18n: :margin: Margin, float, readonly

:margin: Margin, float, readonly

.. i18n: :product_id: Product, many2one, readonly

:product_id: Product, many2one, readonly

.. i18n: Object: report.account.invoice (report.account.invoice)
.. i18n: #######################################################

Object: report.account.invoice (report.account.invoice)
#######################################################

.. i18n: :name: Month, date, readonly

:name: Month, date, readonly

.. i18n: :margin: Margin, float, readonly

:margin: Margin, float, readonly

.. i18n: :amount: Amount, float, readonly

:amount: Amount, float, readonly

.. i18n: :state: State, selection, readonly

:state: State, selection, readonly

.. i18n: :quantity: Quantity, float, readonly

:quantity: Quantity, float, readonly

.. i18n: :type: Type, selection, readonly

:type: Type, selection, readonly

.. i18n: :cost_price: Cost Price, float, readonly

:cost_price: Cost Price, float, readonly
