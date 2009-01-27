
Module Report on tasks by user for projects (*report_task*)
===========================================================
:Module: report_task
:Name: Report on tasks by user for projects
:Version: 5.0.1.0
:Directory: report_task
:Web: 

Description
-----------

::

  Gives statistics on tasks by user on projects to check the pipeline of users.

Dependencies
------------

 * base - installed
 * project - installed

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

Object: Tasks by user and project
#################################

.. index::
  single: Tasks by user and project object
.. 


:user_id: User, many2one, readonly



.. index::
  single: user_id field
.. 




:task_progress: Task Progress, float, readonly



.. index::
  single: task_progress field
.. 




:task_hrs: Task Hours, float, readonly



.. index::
  single: task_hrs field
.. 




:task_nbr: Task Number, float, readonly



.. index::
  single: task_nbr field
.. 




:company_id: Company, many2one



.. index::
  single: company_id field
.. 




:task_state: Status, selection, readonly



.. index::
  single: task_state field
.. 

