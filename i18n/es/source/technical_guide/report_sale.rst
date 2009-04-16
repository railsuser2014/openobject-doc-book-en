
.. i18n: .. module:: report_sale
.. i18n:     :synopsis: Sales Management - Reporting (Official, Quality Certified)
.. i18n:     :noindex:
.. i18n: .. 

.. module:: report_sale
    :synopsis: Sales Management - Reporting (Official, Quality Certified)
    :noindex:
.. 

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. i18n: Sales Management - Reporting (*report_sale*)
.. i18n: ============================================
.. i18n: :Module: report_sale
.. i18n: :Name: Sales Management - Reporting
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: report_sale
.. i18n: :Web: http://www.openerp.com
.. i18n: :Official module: yes
.. i18n: :Quality certified: yes

Sales Management - Reporting (*report_sale*)
============================================
:Module: report_sale
:Name: Sales Management - Reporting
:Version: 5.0.1.0
:Author: Tiny
:Directory: report_sale
:Web: http://www.openerp.com
:Official module: yes
:Quality certified: yes

.. i18n: Description
.. i18n: -----------

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   Reporting for the sale module:
.. i18n:       * Sales order by product (my/this month/all)
.. i18n:       * Sales order by category of product (my/this month/all)
.. i18n:   
.. i18n:       Some predefined lists:
.. i18n:       * Sales of the month
.. i18n:       * Open quotations
.. i18n:       * Uninvoiced Sales
.. i18n:       * Uninvoiced but shipped Sales

::

  Reporting for the sale module:
      * Sales order by product (my/this month/all)
      * Sales order by category of product (my/this month/all)
  
      Some predefined lists:
      * Sales of the month
      * Open quotations
      * Uninvoiced Sales
      * Uninvoiced but shipped Sales

.. i18n: Dependencies
.. i18n: ------------

Dependencies
------------

.. i18n:  * :mod:`sale`

 * :mod:`sale`

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

.. i18n:  * Sales Management/Reporting
.. i18n:  * Sales Management/Reporting/This Month
.. i18n:  * Sales Management/Reporting/This Month/Sales by Product (this month)
.. i18n:  * Sales Management/Reporting/All Months
.. i18n:  * Sales Management/Reporting/All Months/Sales by Product
.. i18n:  * Sales Management/Reporting/This Month/Sales by Category of Product (this month)
.. i18n:  * Sales Management/Reporting/All Months/Sales by Category of Products
.. i18n:  * Sales Management/Reporting/This Month/Sales of the Month
.. i18n:  * Sales Management/Reporting/All Months/Graphs
.. i18n:  * Sales Management/Reporting/All Months/Graphs/Monthly Sales Turnover Over One Year
.. i18n:  * Sales Management/Reporting/All Months/Graphs/Daily Sales Turnover Over One Year
.. i18n:  * Sales Management/Reporting/All Months/Graphs/Monthly Cumulated Sales Turnover Over One Year

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

.. i18n: Views
.. i18n: -----

Views
-----

.. i18n:  * report.sale.order.product.form (form)
.. i18n:  * report.sale.order.product.tree (tree)
.. i18n:  * report.sale.order.product.graph (graph)
.. i18n:  * report.sale.order.category.form (form)
.. i18n:  * report.sale.order.category.tree (tree)
.. i18n:  * report.sale.order.category.graph (graph)
.. i18n:  * sale.order.graph (graph)

 * report.sale.order.product.form (form)
 * report.sale.order.product.tree (tree)
 * report.sale.order.product.graph (graph)
 * report.sale.order.category.form (form)
 * report.sale.order.category.tree (tree)
 * report.sale.order.category.graph (graph)
 * sale.order.graph (graph)

.. i18n: Objects
.. i18n: -------

Objects
-------

.. i18n: Object: Sales Orders by Products (report.sale.order.product)
.. i18n: ############################################################

Object: Sales Orders by Products (report.sale.order.product)
############################################################

.. i18n: :count: # of Lines, integer, readonly

:count: # of Lines, integer, readonly

.. i18n: :price_total: Total Price, float, readonly

:price_total: Total Price, float, readonly

.. i18n: :name: Month, date, readonly

:name: Month, date, readonly

.. i18n: :price_average: Average Price, float, readonly

:price_average: Average Price, float, readonly

.. i18n: :state: Order State, selection, readonly

:state: Order State, selection, readonly

.. i18n: :product_id: Product, many2one, readonly

:product_id: Product, many2one, readonly

.. i18n: :quantity: # of Products, float, readonly

:quantity: # of Products, float, readonly

.. i18n: Object: Sales Orders by Categories (report.sale.order.category)
.. i18n: ###############################################################

Object: Sales Orders by Categories (report.sale.order.category)
###############################################################

.. i18n: :count: # of Lines, integer, readonly

:count: # of Lines, integer, readonly

.. i18n: :price_total: Total Price, float, readonly

:price_total: Total Price, float, readonly

.. i18n: :name: Month, date, readonly

:name: Month, date, readonly

.. i18n: :price_average: Average Price, float, readonly

:price_average: Average Price, float, readonly

.. i18n: :state: Order State, selection, readonly

:state: Order State, selection, readonly

.. i18n: :category_id: Categories, many2one, readonly

:category_id: Categories, many2one, readonly

.. i18n: :quantity: # of Products, float, readonly

:quantity: # of Products, float, readonly
