
Module Master Procurement Schedule (*stock_planning*)
=====================================================
:Module: stock_planning
:Name: Master Procurement Schedule
:Version: 5.0.1.0
:Directory: stock_planning
:Web: 

Description
-----------

::

  This module allows you to manage the planning of procurements based on sales
  forecasts, confirmed orders (customers and suppliers), stock movements, etc.
  You can planify expected outputs and inputs for each warehouses. It also works
  to manage all kind of procurements like purchase orders. That's why it is
  called Master Procurement Schedule instead of the classic Master Production
  Schedule therminology.

Dependencies
------------

 * stock - installed
 * sale - installed

Reports
-------

None


Menus
-------

 * Sales Management/Configuration/Create Sales Periods
 * Sales Management/Configuration/Stock and Sales Periods
 * Stock Management/Plannification
 * Sales Management/Sales Forecasts
 * Sales Management/Sales Forecasts/All Sales Forecasts
 * Sales Management/Sales Forecasts/All Sales Forecasts/Sales Previsions of Current Period
 * Sales Management/Sales Forecasts/My Sales Forecasts
 * Sales Management/Sales Forecasts/My Sales Forecasts/My Previsions of Current Period
 * Stock Management/Plannification/Master Procurement Schedule

Views
-----

 * stock.planning.period.form (form)
 * stock.period.form (form)
 * stock.period.tree (tree)
 * stock.planning.sale.prevision.form (form)
 * stock.planning.sale.prevision.tree (tree)
 * stock.planning.sale.prevision.graph (graph)
 * stock.planning.form (form)
 * stock.planning.tree (tree)


Objects
-------

Object: stock.planning.period
#############################

.. index::
  single: stock.planning.period object
.. 


:date_stop: End Date, date, required



.. index::
  single: date_stop field
.. 




:date_start: Start Date, date, required



.. index::
  single: date_start field
.. 




:name: Period Name, char



.. index::
  single: name field
.. 




:period_ids: Periods, one2many



.. index::
  single: period_ids field
.. 



Object: stock.period
####################

.. index::
  single: stock.period object
.. 


:date_stop: End Date, datetime, required



.. index::
  single: date_stop field
.. 




:date_start: Start Date, datetime, required



.. index::
  single: date_start field
.. 




:name: Period Name, char



.. index::
  single: name field
.. 




:state: State, selection



.. index::
  single: state field
.. 



Object: stock.planning.sale.prevision
#####################################

.. index::
  single: stock.planning.sale.prevision object
.. 


:user_id: Salesman, many2one, readonly



.. index::
  single: user_id field
.. 




:name: Name, char



.. index::
  single: name field
.. 




:product_uom: Product UoM, many2one, required, readonly



.. index::
  single: product_uom field
.. 




:state: State, selection, readonly



.. index::
  single: state field
.. 




:product_id: Product, many2one, required, readonly



.. index::
  single: product_id field
.. 




:period_id: Period, many2one, required



.. index::
  single: period_id field
.. 




:product_qty: Product Quantity, float, required, readonly



.. index::
  single: product_qty field
.. 




:amt_sold: Real Amount Sold, float, readonly



.. index::
  single: amt_sold field
.. 




:product_amt: Product Amount, float, readonly



.. index::
  single: product_amt field
.. 



Object: stock.planning
######################

.. index::
  single: stock.planning object
.. 


:outgoing: Confirmed Out, float, readonly



.. index::
  single: outgoing field
.. 




:outgoing_left: Expected Out, float, readonly



.. index::
  single: outgoing_left field
.. 




:incoming: Confirmed In, float, readonly



.. index::
  single: incoming field
.. 




:name: Name, char



.. index::
  single: name field
.. 




:product_uom: UoM, many2one, required



.. index::
  single: product_uom field
.. 




:incoming_left: Expected In, float, readonly



.. index::
  single: incoming_left field
.. 




:warehouse_id: Warehouse, many2one



.. index::
  single: warehouse_id field
.. 




:stock_start: Stock Start, float, readonly



.. index::
  single: stock_start field
.. 




:state: State, selection, readonly



.. index::
  single: state field
.. 




:line_time: Past/Future, char, readonly



.. index::
  single: line_time field
.. 




:period_id: Period, many2one, required



.. index::
  single: period_id field
.. 




:planned_outgoing: Planned Out, float, required



.. index::
  single: planned_outgoing field
.. 




:to_procure: Planned In, float, required



.. index::
  single: to_procure field
.. 




:planned_sale: Planned Sales, float, readonly



.. index::
  single: planned_sale field
.. 




:product_id: Product, many2one, required



.. index::
  single: product_id field
.. 

