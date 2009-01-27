
Module Report for timesheet (*report_timesheet_user*)
=====================================================
:Module: report_timesheet_user
:Name: Report for timesheet
:Version: 5.0.1.0
:Directory: report_timesheet_user
:Web: 

Description
-----------

::

  New report for timesheet

Dependencies
------------

 * hr_timesheet_sheet - installed
 * multi_company - installed

Reports
-------

None


Menus
-------

 * Project
 * Project/Reporting
 * Project/Reporting/This Month
 * Project/Reporting/This Month/Timesheets by user and company
 * Project/Reporting/This Month/Timesheets by user and company/My Timesheets by company
 * Project/Reporting/All Months
 * Project/Reporting/All Months/Timesheets by user and company
 * Project/Reporting/All Months/Timesheets by user and company/My task by company
 * Project/Reporting/This Month/Timesheets by company
 * Project/Reporting/All Months/Timesheets by company

Views
-----

 * view.report.timesheet.user.user.form (form)
 * view.report.timesheet.user.user.tree (tree)
 * view.report.timesheet.user.form (form)
 * view.report.timesheet.user.tree (tree)


Objects
-------

Object: Tasks by user and company
#################################

.. index::
  single: Tasks by user and company object
.. 


:user_id: User, many2one, readonly



.. index::
  single: user_id field
.. 




:name: Month, date, readonly



.. index::
  single: name field
.. 




:total_cost: Task Cost, float, readonly



.. index::
  single: total_cost field
.. 




:company_id: Company Name, many2one, readonly



.. index::
  single: company_id field
.. 




:total_hours: Task Hours, float, readonly



.. index::
  single: total_hours field
.. 




:user_company_id: User's Company, many2one, readonly



.. index::
  single: user_company_id field
.. 



Object: Tasks by company
########################

.. index::
  single: Tasks by company object
.. 


:total_cost: Task Cost, float, readonly



.. index::
  single: total_cost field
.. 




:total_hours: Task Hours, float, readonly



.. index::
  single: total_hours field
.. 




:user_company_id: User's Company, many2one, readonly



.. index::
  single: user_company_id field
.. 




:name: Month, date, readonly



.. index::
  single: name field
.. 




:company_id: Company Name, many2one, readonly



.. index::
  single: company_id field
.. 

