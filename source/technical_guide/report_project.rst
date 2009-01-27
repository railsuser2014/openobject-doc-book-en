
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

.. index::
  single: Tasks by user and project object
.. 


:hours_effective: Effective Hours, float, readonly



.. index::
  single: hours_effective field
.. 




:user_id: User, many2one, readonly



.. index::
  single: user_id field
.. 




:name: Month, date, readonly



.. index::
  single: name field
.. 




:closing_days: Avg Closing Delay, char, readonly



.. index::
  single: closing_days field
.. 




:task_closed: Task Closed, integer, readonly



.. index::
  single: task_closed field
.. 




:project_id: Project, many2one, readonly



.. index::
  single: project_id field
.. 




:hours_delay: Avg. Plan.-Eff., float, readonly



.. index::
  single: hours_delay field
.. 




:hours_planned: Planned Hours, float, readonly



.. index::
  single: hours_planned field
.. 



Object: Tasks by project
########################

.. index::
  single: Tasks by project object
.. 


:hours_effective: Effective Hours, float, readonly



.. index::
  single: hours_effective field
.. 




:name: Month, date, readonly



.. index::
  single: name field
.. 




:closing_days: Avg Closing Delay, char, readonly



.. index::
  single: closing_days field
.. 




:task_closed: Task Closed, integer, readonly



.. index::
  single: task_closed field
.. 




:project_id: Project, many2one, readonly



.. index::
  single: project_id field
.. 




:hours_delay: Avg. Plan.-Eff., float, readonly



.. index::
  single: hours_delay field
.. 




:hours_planned: Planned Hours, float, readonly



.. index::
  single: hours_planned field
.. 

