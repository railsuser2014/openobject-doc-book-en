
.. module:: report_project
    :synopsis: Sales Management - Reporting (Quality Certified)
    :noindex:
.. 

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

    <style>
      div.body p#module-report_project {
        display: none;
      }
    </style>

Sales Management - Reporting (*report_project*)
===============================================
:Module: report_project
:Name: Sales Management - Reporting
:Version: 5.0.1.0
:Author: Tiny
:Directory: report_project
:Web: http://www.openerp.com
:Is certified: yes

Description
-----------

::

  A module that adds some reports on projects.
      Closed Tasks (By User and By Project), Finished Task (By User and By Project)

Dependencies
------------

 * :mod:`project`
 * :mod:`report_task`

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

Object: Tasks by user and project (report.project.task.user)
############################################################



:hours_effective: Effective Hours, float, readonly





:user_id: User, many2one, readonly





:name: Month, date, readonly





:closing_days: Avg Closing Delay, char, readonly





:task_closed: Task Closed, integer, readonly





:project_id: Project, many2one, readonly





:hours_delay: Avg. Plan.-Eff., float, readonly





:hours_planned: Planned Hours, float, readonly




Object: Tasks by project (report.project.task)
##############################################



:hours_effective: Effective Hours, float, readonly





:name: Month, date, readonly





:closing_days: Avg Closing Delay, char, readonly





:task_closed: Task Closed, integer, readonly





:project_id: Project, many2one, readonly





:hours_delay: Avg. Plan.-Eff., float, readonly





:hours_planned: Planned Hours, float, readonly


