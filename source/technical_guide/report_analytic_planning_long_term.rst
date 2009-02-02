
.. module:: report_analytic_planning_long_term
    :synopsis: report_analytic_planning_long_term
    :noindex:
.. 

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

report_analytic_planning_long_term (*report_analytic_planning_long_term*)
=========================================================================
:Module: report_analytic_planning_long_term
:Name: report_analytic_planning_long_term
:Version: 5.0.1.0
:Directory: report_analytic_planning_long_term
:Web: http://tinyerp.com/
:Is certified: no

Description
-----------

::

  This modules is an improvement of the basic planning module and offers additional functionalities for long term planning, such as:
          - planning of the functions that will be needed
          - additional data for planned ressources: the start and end dates

Dependencies
------------

 * :mod:`report_analytic_planning`

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

Object: Planning product stat (report_account_analytic.planning.stat.product)
#############################################################################



:sum_amount_real: Timesheet, float, readonly





:product_id: Post / Product, many2one, required





:planning_id: Planning, many2one, required





:quantity: Planned, float, required


