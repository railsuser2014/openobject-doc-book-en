
Module report_analytic_planning_long_term (*report_analytic_planning_long_term*)
================================================================================
:Module: report_analytic_planning_long_term
:Name: report_analytic_planning_long_term
:Version: 5.0.1.0
:Directory: report_analytic_planning_long_term
:Web: http://tinyerp.com/

Description
-----------

::

  This modules is an improvement of the basic planning module and offers additional functionalities for long term planning, such as:
          - planning of the functions that will be needed
          - additional data for planned ressources: the start and end dates

Dependencies
------------

 * report_analytic_planning - installed

Reports
-------

None


Menus
-------


None


Views
-----

 * \* INHERIT report.account.analytic.planning.form.inherit_longterm_1 (form)
 * \* INHERIT report.account.analytic.planning.form.inherit_longterm_2 (form)
 * \* INHERIT report.account.analytic.planning.form.inherit_longterm_3 (form)
 * \* INHERIT report.account.analytic.planning.form.inherit_longterm_4 (form)


Objects
-------

Object: Planning product stat
#############################

.. index::
  single: Planning product stat object
.. 


:sum_amount_real: Timesheet, float, readonly



.. index::
  single: sum_amount_real field
.. 




:product_id: Post / Product, many2one, required



.. index::
  single: product_id field
.. 




:planning_id: Planning, many2one, required



.. index::
  single: planning_id field
.. 




:quantity: Planned, float, required



.. index::
  single: quantity field
.. 

