
.. module:: report_task
    :synopsis: Report on tasks by user for projects (Official, Quality Certified)
    :noindex:
.. 

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

Report on tasks by user for projects (*report_task*)
====================================================
:Module: report_task
:Name: Report on tasks by user for projects
:Version: 5.0.1.0
:Author: Tiny
:Directory: report_task
:Web: 
:Official module: yes
:Quality certified: yes

Description
-----------

::

  Gives statistics on tasks by user on projects to check the pipeline of users.

Dependencies
------------

 * :mod:`base`
 * :mod:`project`

Reports
-------

None


Menus
-------

 * Project Management/Reporting
 * Project Management/Reporting/All Months
 * Project Management/Reporting/All Months/Tasks by User

Views
-----

 * report.project.task.form (form)
 * report.project.task.graph (graph)
 * report.project.task.tree (tree)


Objects
-------

Object: Tasks by user and project (report.task.user.pipeline.open)
##################################################################



:user_id: User, many2one, readonly





:task_progress: Task Progress, float, readonly





:task_hrs: Task Hours, float, readonly





:task_nbr: Task Number, float, readonly





:company_id: Company, many2one





:task_state: Status, selection, readonly


