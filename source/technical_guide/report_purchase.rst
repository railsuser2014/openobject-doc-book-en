
Module Purchase Management - Reporting (*report_purchase*)
==========================================================
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

Object: Purchases Orders by Products
####################################

.. index::
  single: Purchases Orders by Products object
.. 


:count: # of Lines, integer, readonly



.. index::
  single: count field
.. 




:price_total: Total Price, float, readonly



.. index::
  single: price_total field
.. 




:name: Month, date, readonly



.. index::
  single: name field
.. 




:price_average: Average Price, float, readonly



.. index::
  single: price_average field
.. 




:state: Order State, selection, readonly



.. index::
  single: state field
.. 




:product_id: Product, many2one, readonly



.. index::
  single: product_id field
.. 




:quantity: # of Products, float, readonly



.. index::
  single: quantity field
.. 



Object: Purchases Orders by Categories
######################################

.. index::
  single: Purchases Orders by Categories object
.. 


:count: # of Lines, integer, readonly



.. index::
  single: count field
.. 




:price_total: Total Price, float, readonly



.. index::
  single: price_total field
.. 




:name: Month, date, readonly



.. index::
  single: name field
.. 




:price_average: Average Price, float, readonly



.. index::
  single: price_average field
.. 




:state: Order State, selection, readonly



.. index::
  single: state field
.. 




:category_id: Categories, many2one, readonly



.. index::
  single: category_id field
.. 




:quantity: # of Products, float, readonly



.. index::
  single: quantity field
.. 

