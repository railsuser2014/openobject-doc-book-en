
Module Sales Management - Reporting (*report_project*)
======================================================
:Module: report_project
:Name: Sales Management - Reporting
:Version: 5.0.1.0
:Directory: report_project
:Web: http://www.openerp.com

Description
-----------

::

  A module that adds some reports on projects.
      Closed Tasks (By User and By Project), Finished Task (By User and By Project)

Dependencies
------------

 * project - installed
 * report_task - installed

Reports
-------

None


Menus
-------

 * Project Management/Reporting/This Month
 * Project Management/Reporting/This Month/Tasks finished by project and user (this month)
 * Project Management/Reporting/All Months/Tasks Closed by Project and User
 * Project Management/Reporting/This Month/Tasks finished by project (this month)
 * Project Management/Reporting/All Months/Tasks Closed by Project

Views
-----

 * report.project.task.user.form (form)
 * report.project.task.user.tree (tree)
 * report.project.task.form (form)
 * report.project.task.tree (tree)


Objects
-------

Object: Tasks by user and project
#################################



:hours_effective: Effective Hours, float, readonly





:user_id: User, many2one, readonly





:name: Month, date, readonly





:closing_days: Avg Closing Delay, char, readonly





:task_closed: Task Closed, integer, readonly





:project_id: Project, many2one, readonly





:hours_delay: Avg. Plan.-Eff., float, readonly





:hours_planned: Planned Hours, float, readonly




Object: Tasks by project
########################



:hours_effective: Effective Hours, float, readonly





:name: Month, date, readonly





:closing_days: Avg Closing Delay, char, readonly





:task_closed: Task Closed, integer, readonly





:project_id: Project, many2one, readonly





:hours_delay: Avg. Plan.-Eff., float, readonly





:hours_planned: Planned Hours, float, readonly


