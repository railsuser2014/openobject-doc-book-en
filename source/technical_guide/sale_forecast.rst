
Module Sales Forecasts, goals and statistics (*sale_forecast*)
==============================================================
:Module: sale_forecast
:Name: Sales Forecasts, goals and statistics
:Version: 5.0.1.0
:Directory: sale_forecast
:Web: http://tinyerp.com

Description
-----------

::

  This module allows manager to do their sales forecast.
  Different reports are set up for forecast and sales analysis.

Dependencies
------------

 * account - installed
 * account_invoice_salesman - installed
 * crm - installed
 * sale - installed

Reports
-------

 * Sale Forecast

 * Sales Forecast By Salesman

Menus
-------

 * Sales Management/Sales Forecasts
 * Sales Management/Sales Forecasts/New Sales Forecasts
 * Sales Management/Sales Forecasts/My Managing Sales Forecast
 * Sales Management/Sales Forecasts/Current Sales Forecast
 * Sales Management/Sales Forecasts/Forecast Reports
 * Sales Management/Sales Forecasts/Forecast Reports/Number Of Invoice
 * Sales Management/Sales Forecasts/Forecast Reports/Amount Invoiced
 * Sales Management/Sales Forecasts/Forecast Reports/Cases
 * Sales Management/Sales Forecasts/Forecast Reports/Amount Sales
 * Sales Management/Sales Forecasts/Forecast Reports/Number of Sales order

Views
-----

 * sale_forecast.tree (tree)
 * sale_forecast.form (form)
 * sale.forecast.line.graph (graph)


Objects
-------

Object: Sales Forecast
######################

.. index::
  single: Sales Forecast object
.. 


:forecast_rate: Progress (%), float, readonly



.. index::
  single: forecast_rate field
.. 




:user_id: Responsible, many2one, required



.. index::
  single: user_id field
.. 




:name: Sales Forecast, char, required



.. index::
  single: name field
.. 




:date_from: Start Period, date, required



.. index::
  single: date_from field
.. 




:note: Notes, text



.. index::
  single: note field
.. 




:state: State, selection, required



.. index::
  single: state field
.. 




:date_to: End Period, date, required



.. index::
  single: date_to field
.. 




:line_ids: Forecast lines, one2many



.. index::
  single: line_ids field
.. 



Object: Forecast Line
#####################

.. index::
  single: Forecast Line object
.. 


:state_cancel: Cancel, boolean



.. index::
  single: state_cancel field
.. 




:computation_type: Computation Base On, selection, required



.. index::
  single: computation_type field
.. 




:state_draft: Draft, boolean



.. index::
  single: state_draft field
.. 




:feedback: Feedback Comment, text



.. index::
  single: feedback field
.. 




:user_id: Salesman, many2one, required



.. index::
  single: user_id field
.. 




:state_confirmed: Confirmed, boolean



.. index::
  single: state_confirmed field
.. 




:crm_case_categ: Case Category, many2many



.. index::
  single: crm_case_categ field
.. 




:note: Note, text



.. index::
  single: note field
.. 




:amount: Value Forecasted, float



.. index::
  single: amount field
.. 




:computed_amount: Real Value, float, readonly



.. index::
  single: computed_amount field
.. 




:final_evolution: Performance, selection



.. index::
  single: final_evolution field
.. 




:forecast_rate: Progress (%), float, readonly



.. index::
  single: forecast_rate field
.. 




:state_done: Done, boolean



.. index::
  single: state_done field
.. 




:product_categ: Product Category, many2many



.. index::
  single: product_categ field
.. 




:product_product: Products, many2many



.. index::
  single: product_product field
.. 




:crm_case_section: Case Section, many2many



.. index::
  single: crm_case_section field
.. 




:forecast_id: Forecast, many2one, required



.. index::
  single: forecast_id field
.. 

