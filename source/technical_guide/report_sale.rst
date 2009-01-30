
.. module:: report_sale
    :synopsis: Sales Management - Reporting
    :noindex:
.. 

Sales Management - Reporting (*report_sale*)
============================================
:Module: report_sale
:Name: Sales Management - Reporting
:Version: 5.0.1.0
:Directory: report_sale
:Web: http://www.openerp.com

Description
-----------

::

  Reporting for the sale module:
      * Sales order by product (my/this month/all)
      * Sales order by category of product (my/this month/all)
  
      Some predefined lists:
      * Sales of the month
      * Open quotations
      * Uninvoiced Sales
      * Uninvoiced but shipped Sales

Dependencies
------------

 * sale - installed

Reports
-------

None


Menus
-------

 * Sales Management/Reporting
 * Sales Management/Reporting/This Month
 * Sales Management/Reporting/This Month/Sales by Product (this month)
 * Sales Management/Reporting/All Months
 * Sales Management/Reporting/All Months/Sales by Product
 * Sales Management/Reporting/This Month/Sales by Category of Product (this month)
 * Sales Management/Reporting/All Months/Sales by Category of Products
 * Sales Management/Reporting/This Month/Sales of the Month
 * Sales Management/Reporting/All Months/Graphs
 * Sales Management/Reporting/All Months/Graphs/Monthly Sales Turnover Over One Year
 * Sales Management/Reporting/All Months/Graphs/Daily Sales Turnover Over One Year
 * Sales Management/Reporting/All Months/Graphs/Monthly Cumulated Sales Turnover Over One Year

Views
-----

 * report.sale.order.product.form (form)
 * report.sale.order.product.tree (tree)
 * report.sale.order.product.graph (graph)
 * report.sale.order.category.form (form)
 * report.sale.order.category.tree (tree)
 * report.sale.order.category.graph (graph)
 * sale.order.graph (graph)


Objects
-------

Object: Sales Orders by Products (report.sale.order.product)
############################################################



:count: # of Lines, integer, readonly





:price_total: Total Price, float, readonly





:name: Month, date, readonly





:price_average: Average Price, float, readonly





:state: Order State, selection, readonly





:product_id: Product, many2one, readonly





:quantity: # of Products, float, readonly




Object: Sales Orders by Categories (report.sale.order.category)
###############################################################



:count: # of Lines, integer, readonly





:price_total: Total Price, float, readonly





:name: Month, date, readonly





:price_average: Average Price, float, readonly





:state: Order State, selection, readonly





:category_id: Categories, many2one, readonly





:quantity: # of Products, float, readonly


