
.. i18n: .. module:: report_task
.. i18n:     :synopsis: Report on tasks by user for projects (Official, Quality Certified)
.. i18n:     :noindex:
.. i18n: .. 

.. module:: report_task
    :synopsis: Report on tasks by user for projects (Official, Quality Certified)
    :noindex:
.. 

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. i18n: Report on tasks by user for projects (*report_task*)
.. i18n: ====================================================
.. i18n: :Module: report_task
.. i18n: :Name: Report on tasks by user for projects
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: report_task
.. i18n: :Web: 
.. i18n: :Official module: yes
.. i18n: :Quality certified: yes

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

.. i18n: Description
.. i18n: -----------

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   Gives statistics on tasks by user on projects to check the pipeline of users.

::

  Gives statistics on tasks by user on projects to check the pipeline of users.

.. i18n: Dependencies
.. i18n: ------------

Dependencies
------------

.. i18n:  * :mod:`base`
.. i18n:  * :mod:`project`

 * :mod:`base`
 * :mod:`project`

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

.. i18n:  * Project Management/Reporting
.. i18n:  * Project Management/Reporting/All Months
.. i18n:  * Project Management/Reporting/All Months/Tasks by User

 * Project Management/Reporting
 * Project Management/Reporting/All Months
 * Project Management/Reporting/All Months/Tasks by User

.. i18n: Views
.. i18n: -----

Views
-----

.. i18n:  * report.project.task.form (form)
.. i18n:  * report.project.task.graph (graph)
.. i18n:  * report.project.task.tree (tree)

 * report.project.task.form (form)
 * report.project.task.graph (graph)
 * report.project.task.tree (tree)

.. i18n: Objects
.. i18n: -------

Objects
-------

.. i18n: Object: Tasks by user and project (report.task.user.pipeline.open)
.. i18n: ##################################################################

Object: Tasks by user and project (report.task.user.pipeline.open)
##################################################################

.. i18n: :user_id: User, many2one, readonly

:user_id: User, many2one, readonly

.. i18n: :task_progress: Task Progress, float, readonly

:task_progress: Task Progress, float, readonly

.. i18n: :task_hrs: Task Hours, float, readonly

:task_hrs: Task Hours, float, readonly

.. i18n: :task_nbr: Task Number, float, readonly

:task_nbr: Task Number, float, readonly

.. i18n: :company_id: Company, many2one

:company_id: Company, many2one

.. i18n: :task_state: Status, selection, readonly

:task_state: Status, selection, readonly
