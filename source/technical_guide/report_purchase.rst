
.. module:: report_purchase
    :synopsis: Purchase Management - Reporting
    :noindex:
.. 

Purchase Management - Reporting (*report_purchase*)
===================================================
:Module: report_purchase
:Name: Purchase Management - Reporting
:Version: 5.0.1.0
:Directory: report_purchase
:Web: http://www.openerp.com

Description
-----------

::

  Module to add views like
      Purchase By Product, Purchase By Category of Product, All Months, Current Month.

Dependencies
------------

 * purchase - installed

Reports
-------

None


Menus
-------

 * Purchase Management/Reporting
 * Purchase Management/Reporting/This Month
 * Purchase Management/Reporting/This Month/Purchases by Products (this month)
 * Purchase Management/Reporting/All Months
 * Purchase Management/Reporting/All Months/Purchases by Products
 * Purchase Management/Reporting/This Month/Purchases by Category of Product (this month)
 * Purchase Management/Reporting/All Months/Purchases by Category of Products

Views
-----

 * report.purchase.order.product.form (form)
 * product.month.graph (graph)
 * report.purchase.order.product.tree (tree)
 * report.purchase.order.category.form (form)
 * product.category.graph (graph)
 * report.purchase.order.category.tree (tree)


Objects
-------

Object: Purchases Orders by Products (report.purchase.order.product)
####################################################################



:count: # of Lines, integer, readonly





:price_total: Total Price, float, readonly





:name: Month, date, readonly





:price_average: Average Price, float, readonly





:state: Order State, selection, readonly





:product_id: Product, many2one, readonly





:quantity: # of Products, float, readonly




Object: Purchases Orders by Categories (report.purchase.order.category)
#######################################################################



:count: # of Lines, integer, readonly





:price_total: Total Price, float, readonly





:name: Month, date, readonly





:price_average: Average Price, float, readonly





:state: Order State, selection, readonly





:category_id: Categories, many2one, readonly





:quantity: # of Products, float, readonly


