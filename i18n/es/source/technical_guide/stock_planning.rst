
.. i18n: .. module:: stock_planning
.. i18n:     :synopsis: Master Procurement Schedule 
.. i18n:     :noindex:
.. i18n: .. 

.. module:: stock_planning
    :synopsis: Master Procurement Schedule 
    :noindex:
.. 

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. i18n: Master Procurement Schedule (*stock_planning*)
.. i18n: ==============================================
.. i18n: :Module: stock_planning
.. i18n: :Name: Master Procurement Schedule
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: stock_planning
.. i18n: :Web: 
.. i18n: :Official module: no
.. i18n: :Quality certified: no

Master Procurement Schedule (*stock_planning*)
==============================================
:Module: stock_planning
:Name: Master Procurement Schedule
:Version: 5.0.1.0
:Author: Tiny
:Directory: stock_planning
:Web: 
:Official module: no
:Quality certified: no

.. i18n: Description
.. i18n: -----------

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   This module allows you to manage the planning of procurements based on sales forecasts, confirmed 
.. i18n:   orders (customers and suppliers), stock movements, etc.
.. i18n:   You can planify expected outputs and inputs for each warehouses. 
.. i18n:   It also worksto manage all kind of procurements like purchase orders. 
.. i18n:   That's why it is called Master Procurement Schedule instead of the classic Master Production Schedule 
.. i18n:   therminology.

::

  This module allows you to manage the planning of procurements based on sales forecasts, confirmed 
  orders (customers and suppliers), stock movements, etc.
  You can planify expected outputs and inputs for each warehouses. 
  It also worksto manage all kind of procurements like purchase orders. 
  That's why it is called Master Procurement Schedule instead of the classic Master Production Schedule 
  therminology.

.. i18n: Dependencies
.. i18n: ------------

Dependencies
------------

.. i18n:  * :mod:`stock`
.. i18n:  * :mod:`sale`

 * :mod:`stock`
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

.. i18n:  * Sales Management/Configuration/Create Sales Periods
.. i18n:  * Sales Management/Configuration/Stock and Sales Periods
.. i18n:  * Stock Management/Plannification
.. i18n:  * Sales Management/Sales Forecasts
.. i18n:  * Sales Management/Sales Forecasts/All Sales Forecasts
.. i18n:  * Sales Management/Sales Forecasts/All Sales Forecasts/Sales Previsions of Current Period
.. i18n:  * Sales Management/Sales Forecasts/My Sales Forecasts
.. i18n:  * Sales Management/Sales Forecasts/My Sales Forecasts/My Previsions of Current Period
.. i18n:  * Stock Management/Plannification/Master Procurement Schedule

 * Sales Management/Configuration/Create Sales Periods
 * Sales Management/Configuration/Stock and Sales Periods
 * Stock Management/Plannification
 * Sales Management/Sales Forecasts
 * Sales Management/Sales Forecasts/All Sales Forecasts
 * Sales Management/Sales Forecasts/All Sales Forecasts/Sales Previsions of Current Period
 * Sales Management/Sales Forecasts/My Sales Forecasts
 * Sales Management/Sales Forecasts/My Sales Forecasts/My Previsions of Current Period
 * Stock Management/Plannification/Master Procurement Schedule

.. i18n: Views
.. i18n: -----

Views
-----

.. i18n:  * stock.planning.period.form (form)
.. i18n:  * stock.period.form (form)
.. i18n:  * stock.period.tree (tree)
.. i18n:  * stock.planning.sale.prevision.form (form)
.. i18n:  * stock.planning.sale.prevision.tree (tree)
.. i18n:  * stock.planning.sale.prevision.graph (graph)
.. i18n:  * stock.planning.form (form)
.. i18n:  * stock.planning.tree (tree)

 * stock.planning.period.form (form)
 * stock.period.form (form)
 * stock.period.tree (tree)
 * stock.planning.sale.prevision.form (form)
 * stock.planning.sale.prevision.tree (tree)
 * stock.planning.sale.prevision.graph (graph)
 * stock.planning.form (form)
 * stock.planning.tree (tree)

.. i18n: Objects
.. i18n: -------

Objects
-------

.. i18n: Object: stock.planning.period (stock.planning.period)
.. i18n: #####################################################

Object: stock.planning.period (stock.planning.period)
#####################################################

.. i18n: :date_stop: End Date, date, required

:date_stop: End Date, date, required

.. i18n: :date_start: Start Date, date, required

:date_start: Start Date, date, required

.. i18n: :name: Period Name, char

:name: Period Name, char

.. i18n: :period_ids: Periods, one2many

:period_ids: Periods, one2many

.. i18n: Object: stock.period (stock.period)
.. i18n: ###################################

Object: stock.period (stock.period)
###################################

.. i18n: :date_stop: End Date, datetime, required

:date_stop: End Date, datetime, required

.. i18n: :date_start: Start Date, datetime, required

:date_start: Start Date, datetime, required

.. i18n: :name: Period Name, char

:name: Period Name, char

.. i18n: :state: State, selection

:state: State, selection

.. i18n: Object: stock.planning.sale.prevision (stock.planning.sale.prevision)
.. i18n: #####################################################################

Object: stock.planning.sale.prevision (stock.planning.sale.prevision)
#####################################################################

.. i18n: :user_id: Salesman, many2one, readonly

:user_id: Salesman, many2one, readonly

.. i18n: :name: Name, char

:name: Name, char

.. i18n: :product_uom: Product UoM, many2one, required, readonly

:product_uom: Product UoM, many2one, required, readonly

.. i18n: :state: State, selection, readonly

:state: State, selection, readonly

.. i18n: :product_id: Product, many2one, required, readonly

:product_id: Product, many2one, required, readonly

.. i18n: :period_id: Period, many2one, required

:period_id: Period, many2one, required

.. i18n: :product_qty: Product Quantity, float, required, readonly

:product_qty: Product Quantity, float, required, readonly

.. i18n: :amt_sold: Real Amount Sold, float, readonly

:amt_sold: Real Amount Sold, float, readonly

.. i18n: :product_amt: Product Amount, float, readonly

:product_amt: Product Amount, float, readonly

.. i18n: Object: stock.planning (stock.planning)
.. i18n: #######################################

Object: stock.planning (stock.planning)
#######################################

.. i18n: :outgoing: Confirmed Out, float, readonly

:outgoing: Confirmed Out, float, readonly

.. i18n: :outgoing_left: Expected Out, float, readonly

:outgoing_left: Expected Out, float, readonly

.. i18n: :incoming: Confirmed In, float, readonly

:incoming: Confirmed In, float, readonly

.. i18n: :name: Name, char

:name: Name, char

.. i18n: :product_uom: UoM, many2one, required

:product_uom: UoM, many2one, required

.. i18n: :incoming_left: Expected In, float, readonly

:incoming_left: Expected In, float, readonly

.. i18n: :warehouse_id: Warehouse, many2one

:warehouse_id: Warehouse, many2one

.. i18n: :stock_start: Stock Start, float, readonly

:stock_start: Stock Start, float, readonly

.. i18n: :state: State, selection, readonly

:state: State, selection, readonly

.. i18n: :line_time: Past/Future, char, readonly

:line_time: Past/Future, char, readonly

.. i18n: :period_id: Period, many2one, required

:period_id: Period, many2one, required

.. i18n: :planned_outgoing: Planned Out, float, required

:planned_outgoing: Planned Out, float, required

.. i18n: :to_procure: Planned In, float, required

:to_procure: Planned In, float, required

.. i18n: :planned_sale: Planned Sales, float, readonly

:planned_sale: Planned Sales, float, readonly

.. i18n: :product_id: Product, many2one, required

:product_id: Product, many2one, required
