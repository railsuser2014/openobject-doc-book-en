
.. module:: stock_planning
    :synopsis: Master Procurement Schedule 
    :noindex:
.. 

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

    <style>
      div.body p#module-stock_planning {
        display: none;
      }
    </style>

Master Procurement Schedule (*stock_planning*)
==============================================
:Module: stock_planning
:Name: Master Procurement Schedule
:Version: 5.0.1.0
:Author: Tiny
:Directory: stock_planning
:Web: 
:Is certified: no

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

 * :mod:`stock`
 * :mod:`sale`

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

Object: stock.planning.period (stock.planning.period)
#####################################################



:date_stop: End Date, date, required





:date_start: Start Date, date, required





:name: Period Name, char





:period_ids: Periods, one2many




Object: stock.period (stock.period)
###################################



:date_stop: End Date, datetime, required





:date_start: Start Date, datetime, required





:name: Period Name, char





:state: State, selection




Object: stock.planning.sale.prevision (stock.planning.sale.prevision)
#####################################################################



:user_id: Salesman, many2one, readonly





:name: Name, char





:product_uom: Product UoM, many2one, required, readonly





:state: State, selection, readonly





:product_id: Product, many2one, required, readonly





:period_id: Period, many2one, required





:product_qty: Product Quantity, float, required, readonly





:amt_sold: Real Amount Sold, float, readonly





:product_amt: Product Amount, float, readonly




Object: stock.planning (stock.planning)
#######################################



:outgoing: Confirmed Out, float, readonly





:outgoing_left: Expected Out, float, readonly





:incoming: Confirmed In, float, readonly





:name: Name, char





:product_uom: UoM, many2one, required





:incoming_left: Expected In, float, readonly





:warehouse_id: Warehouse, many2one





:stock_start: Stock Start, float, readonly





:state: State, selection, readonly





:line_time: Past/Future, char, readonly





:period_id: Period, many2one, required





:planned_outgoing: Planned Out, float, required





:to_procure: Planned In, float, required





:planned_sale: Planned Sales, float, readonly





:product_id: Product, many2one, required


