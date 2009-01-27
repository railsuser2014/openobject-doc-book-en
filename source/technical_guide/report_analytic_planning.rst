
Module Analytic planning - Reporting (*report_analytic_planning*)
=================================================================
:Module: report_analytic_planning
:Name: Analytic planning - Reporting
:Version: 5.0.1.0
:Directory: report_analytic_planning
:Web: http://www.openerp.com

Description
-----------

::

  Planning on analytic accounts.

Dependencies
------------

 * account - installed
 * hr_timesheet_invoice - installed
 * project - installed
 * report_analytic_line - installed

Reports
-------

 * Planning

Menus
-------

 * Human Resources/Planning
 * Human Resources/Planning/Plannings
 * Human Resources/Planning/My Plannings
 * Human Resources/Planning/My Plannings/My Current Plannings
 * Human Resources/Planning/Plannings/Current Plannings
 * Human Resources/Planning/New Planning
 * Human Resources/Reporting/Planning
 * Human Resources/Reporting/Planning/Planning Statistics
 * Human Resources/Reporting/Planning/My Planning Statistics
 * Human Resources/Reporting/Planning/Planning Statistics of My Projects

Views
-----

 * report.account.analytic.planning.tree (tree)
 * report.account.analytic.planning.form (form)
 * report.account.analytic.planning.stat.form (form)
 * report.account.analytic.planning.stat.tree (tree)
 * report.account.analytic.planning.stat.graph (graph)


Objects
-------

Object: Planning
################

.. index::
  single: Planning object
.. 


:user_id: Responsible, many2one, required



.. index::
  single: user_id field
.. 




:name: Planning Name, char, required



.. index::
  single: name field
.. 




:date_from: Start Date, date, required



.. index::
  single: date_from field
.. 




:stat_account_ids: Planning by account, one2many, readonly



.. index::
  single: stat_account_ids field
.. 




:stat_ids: Planning analysis, one2many, readonly



.. index::
  single: stat_ids field
.. 




:state: Status, selection, required



.. index::
  single: state field
.. 




:date_to: End Date, date, required



.. index::
  single: date_to field
.. 




:line_ids: Planning lines, one2many



.. index::
  single: line_ids field
.. 




:stat_user_ids: Planning by user, one2many, readonly



.. index::
  single: stat_user_ids field
.. 




:delegate_ids: unknown, one2many, readonly



.. index::
  single: delegate_ids field
.. 




:stat_product_ids: Planning by Post / Product, one2many, readonly



.. index::
  single: stat_product_ids field
.. 



Object: Planning Line
#####################

.. index::
  single: Planning Line object
.. 


:user_id: User, many2one



.. index::
  single: user_id field
.. 




:account_id: Analytic account, many2one, required



.. index::
  single: account_id field
.. 




:planning_id: Planning, many2one, required



.. index::
  single: planning_id field
.. 




:amount_unit: Qty UoM, many2one, required



.. index::
  single: amount_unit field
.. 




:note: Note, text



.. index::
  single: note field
.. 




:amount: Quantity, float, required



.. index::
  single: amount field
.. 




:date_to: End date, date



.. index::
  single: date_to field
.. 




:delegate_id: Delegate To, many2one



.. index::
  single: delegate_id field
.. 




:date_from: Start date, date



.. index::
  single: date_from field
.. 




:product_id: Job / Product, many2one, required



.. index::
  single: product_id field
.. 



Object: Planning account stat
#############################

.. index::
  single: Planning account stat object
.. 


:sum_amount_real: Timesheet, float, readonly



.. index::
  single: sum_amount_real field
.. 




:account_id: Analytic Account, many2one, required



.. index::
  single: account_id field
.. 




:planning_id: Planning, many2one



.. index::
  single: planning_id field
.. 




:quantity: Planned, float, required



.. index::
  single: quantity field
.. 



Object: Planning stat
#####################

.. index::
  single: Planning stat object
.. 


:user_id: User, many2one



.. index::
  single: user_id field
.. 




:account_id: Account, many2one, required



.. index::
  single: account_id field
.. 




:planning_id: Planning, many2one



.. index::
  single: planning_id field
.. 




:sum_amount_real: Timesheet, float, readonly



.. index::
  single: sum_amount_real field
.. 




:sum_amount: Planned hours, float, required



.. index::
  single: sum_amount field
.. 




:manager_id: Manager, many2one



.. index::
  single: manager_id field
.. 




:sum_amount_tasks: Tasks, float, readonly



.. index::
  single: sum_amount_tasks field
.. 



Object: Planning user stat
##########################

.. index::
  single: Planning user stat object
.. 


:sum_amount_real: Timesheet, float, readonly



.. index::
  single: sum_amount_real field
.. 




:user_id: User, many2one



.. index::
  single: user_id field
.. 




:planning_id: Planning, many2one, required



.. index::
  single: planning_id field
.. 




:quantity: Planned, float, required



.. index::
  single: quantity field
.. 

