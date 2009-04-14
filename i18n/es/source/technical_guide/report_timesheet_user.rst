
.. i18n: .. module:: report_timesheet_user
.. i18n:     :synopsis: Report for timesheet 
.. i18n:     :noindex:
.. i18n: .. 

.. module:: report_timesheet_user
    :synopsis: Report for timesheet 
    :noindex:
.. 

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. i18n: Report for timesheet (*report_timesheet_user*)
.. i18n: ==============================================
.. i18n: :Module: report_timesheet_user
.. i18n: :Name: Report for timesheet
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: report_timesheet_user
.. i18n: :Web: 
.. i18n: :Official module: no
.. i18n: :Quality certified: no

Report for timesheet (*report_timesheet_user*)
==============================================
:Module: report_timesheet_user
:Name: Report for timesheet
:Version: 5.0.1.0
:Author: Tiny
:Directory: report_timesheet_user
:Web: 
:Official module: no
:Quality certified: no

.. i18n: Description
.. i18n: -----------

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   New report for timesheet

::

  New report for timesheet

.. i18n: Dependencies
.. i18n: ------------

Dependencies
------------

.. i18n:  * :mod:`hr_timesheet_sheet`
.. i18n:  * :mod:`multi_company`

 * :mod:`hr_timesheet_sheet`
 * :mod:`multi_company`

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

.. i18n:  * Project
.. i18n:  * Project/Reporting
.. i18n:  * Project/Reporting/This Month
.. i18n:  * Project/Reporting/This Month/Timesheets by user and company
.. i18n:  * Project/Reporting/This Month/Timesheets by user and company/My Timesheets by company
.. i18n:  * Project/Reporting/All Months
.. i18n:  * Project/Reporting/All Months/Timesheets by user and company
.. i18n:  * Project/Reporting/All Months/Timesheets by user and company/My task by company
.. i18n:  * Project/Reporting/This Month/Timesheets by company
.. i18n:  * Project/Reporting/All Months/Timesheets by company

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

.. i18n: Views
.. i18n: -----

Views
-----

.. i18n:  * view.report.timesheet.user.user.form (form)
.. i18n:  * view.report.timesheet.user.user.tree (tree)
.. i18n:  * view.report.timesheet.user.form (form)
.. i18n:  * view.report.timesheet.user.tree (tree)

 * view.report.timesheet.user.user.form (form)
 * view.report.timesheet.user.user.tree (tree)
 * view.report.timesheet.user.form (form)
 * view.report.timesheet.user.tree (tree)

.. i18n: Objects
.. i18n: -------

Objects
-------

.. i18n: Object: Tasks by user and company (report.timesheet.user.user)
.. i18n: ##############################################################

Object: Tasks by user and company (report.timesheet.user.user)
##############################################################

.. i18n: :user_id: User, many2one, readonly

:user_id: User, many2one, readonly

.. i18n: :name: Month, date, readonly

:name: Month, date, readonly

.. i18n: :total_cost: Task Cost, float, readonly

:total_cost: Task Cost, float, readonly

.. i18n: :company_id: Company Name, many2one, readonly

:company_id: Company Name, many2one, readonly

.. i18n: :total_hours: Task Hours, float, readonly

:total_hours: Task Hours, float, readonly

.. i18n: :user_company_id: User's Company, many2one, readonly

:user_company_id: User's Company, many2one, readonly

.. i18n: Object: Tasks by company (report.timesheet.user)
.. i18n: ################################################

Object: Tasks by company (report.timesheet.user)
################################################

.. i18n: :total_cost: Task Cost, float, readonly

:total_cost: Task Cost, float, readonly

.. i18n: :total_hours: Task Hours, float, readonly

:total_hours: Task Hours, float, readonly

.. i18n: :user_company_id: User's Company, many2one, readonly

:user_company_id: User's Company, many2one, readonly

.. i18n: :name: Month, date, readonly

:name: Month, date, readonly

.. i18n: :company_id: Company Name, many2one, readonly

:company_id: Company Name, many2one, readonly
