
Module Project Management (*project*)
=====================================
:Module: project
:Name: Project Management
:Version: 5.0.1.1
:Directory: project
:Web: http://www.openerp.com

Description
-----------

::

  Project management module that track multi-level projects, tasks,
  works done on tasks, eso. It is able to render planning, order tasks, eso.

Dependencies
------------

 * product - installed
 * account - installed
 * hr - installed
 * process - installed

Reports
-------

 * Gantt Representation

 * Gantt Representation

Menus
-------

 * Project Management/Configuration
 * Project Management/Projects/New Project
 * Project Management
 * Project Management/Tasks
 * Project Management/Projects
 * Project Management/Projects/All projects
 * Project Management/Projects/All projects/Running projects
 * Project Management/Configuration/Template of Projects
 * Project Management/Projects/My Projects
 * Project Management/Projects/My Projects/My Running Projects
 * Project Management/Projects/Projects Structure
 * Project Management/Tasks/All Tasks
 * Project Management/Tasks/My Tasks
 * Project Management/Tasks/My Tasks/My Pending Tasks
 * Project Management/Tasks/My Tasks/My Current Tasks
 * Project Management/Tasks/My Tasks/My Current Tasks/My Tasks in Progress
 * Project Management/Tasks/My Tasks/My Current Tasks/My Draft Tasks
 * Project Management/Tasks/New Task
 * Project Management/Tasks/All Tasks/Tasks in Progress
 * Project Management/Tasks/All Tasks/Unassigned Tasks
 * Project Management/Configuration/Task Types

Views
-----

 * project.project.form (form)
 * project.project.tree (tree)
 * project.task.work.form (form)
 * project.task.work.tree (tree)
 * project.project.tree (tree)
 * Compute Remaining Hours  (form)
 * project.task.form (form)
 * project.task.tree (tree)
 * project.task.calendar (calendar)
 * project.task.gantt (gantt)
 * project.task.graph (graph)
 * project.task.type.form (form)
 * project.task.type.tree (tree)
 * \* INHERIT res.company.task.config (form)


Objects
-------

Object: Project
###############

.. index::
  single: Project object
.. 


:tasks: Project tasks, one2many



.. index::
  single: tasks field
.. 




:date_end: Expected End, date



.. index::
  single: date_end field
.. 




:contact_id: Contact, many2one



.. index::
  single: contact_id field
.. 




:effective_hours: Time Spent, float, readonly

    *Sum of spent hours of all tasks related to this project.*

.. index::
  single: effective_hours field
.. 




:manager: Project Manager, many2one



.. index::
  single: manager field
.. 




:child_id: Subproject, one2many



.. index::
  single: child_id field
.. 




:planned_hours: Planned Time, float, readonly

    *Sum of planned hours of all tasks related to this project.*

.. index::
  single: planned_hours field
.. 




:partner_id: Partner, many2one



.. index::
  single: partner_id field
.. 




:warn_footer: Mail Footer, text

    *Footer added at the beginning of the email for the warning message sent to the customer when a task is closed.*

.. index::
  single: warn_footer field
.. 




:warn_manager: Warn Manager, boolean

    *If you check this field, the project manager will receive a request each time a task is completed by his team.*

.. index::
  single: warn_manager field
.. 




:warn_customer: Warn Partner, boolean

    *If you check this, the user will have a popup when closing a task that propose a message to send by email to the customer.*

.. index::
  single: warn_customer field
.. 




:date_start: Starting Date, date



.. index::
  single: date_start field
.. 




:company_id: Company, many2one



.. index::
  single: company_id field
.. 




:priority: Sequence, integer



.. index::
  single: priority field
.. 




:parent_id: Parent Project, many2one



.. index::
  single: parent_id field
.. 




:state: State, selection, required, readonly



.. index::
  single: state field
.. 




:contact_id2: Contact, many2one



.. index::
  single: contact_id2 field
.. 




:timesheet_id: Working Time, many2one

    *Timetable working hours to adjust the gantt diagram report*

.. index::
  single: timesheet_id field
.. 




:members: Project Members, many2many

    *Project's member. Not used in any computation, just for information purpose.*

.. index::
  single: members field
.. 




:active: Active, boolean



.. index::
  single: active field
.. 




:name: Project Name, char, required



.. index::
  single: name field
.. 




:notes: Notes, text

    *Internal description of the project.*

.. index::
  single: notes field
.. 




:warn_header: Mail Header, text

    *Header added at the beginning of the email for the warning message sent to the customer when a task is closed.*

.. index::
  single: warn_header field
.. 




:total_hours: Total Time, float, readonly

    *Sum of total hours of all tasks related to this project.*

.. index::
  single: total_hours field
.. 




:category_id: Analytic Account, many2one

    *Link this project to an analytic account if you need financial management on projects. It ables to connect projects with budgets, plannings, costs and revenues analysis, timesheet on projects, etc.*

.. index::
  single: category_id field
.. 




:progress_rate: Progress, float, readonly

    *Percent of tasks closed according to the total of tasks todo.*

.. index::
  single: progress_rate field
.. 



Object: Project task type
#########################

.. index::
  single: Project task type object
.. 


:name: Type, char, required



.. index::
  single: name field
.. 




:description: Description, text



.. index::
  single: description field
.. 



Object: Task
############

.. index::
  single: Task object
.. 


:sequence: Sequence, integer



.. index::
  single: sequence field
.. 




:context_id: Context, many2one



.. index::
  single: context_id field
.. 




:date_reviewed: Reviewed Date, datetime



.. index::
  single: date_reviewed field
.. 




:effective_hours: Hours Spent, float, readonly

    *Computed using the sum of the task work done.*

.. index::
  single: effective_hours field
.. 




:planned_hours: Planned Hours, float, required, readonly

    *Estimated time to do the task, usually set by the project manager when the task is in draft state.*

.. index::
  single: planned_hours field
.. 




:partner_id: Partner, many2one



.. index::
  single: partner_id field
.. 




:user_id: Assigned to, many2one



.. index::
  single: user_id field
.. 




:timebox_id: Timebox, many2one



.. index::
  single: timebox_id field
.. 




:date_start: Starting Date, datetime



.. index::
  single: date_start field
.. 




:company_id: Company, many2one



.. index::
  single: company_id field
.. 




:priority: Importance, selection



.. index::
  single: priority field
.. 




:parent_id: Parent Task, many2one



.. index::
  single: parent_id field
.. 




:state: Status, selection, required, readonly



.. index::
  single: state field
.. 




:progress: Progress (%), float, readonly

    *Computed as: Time Spent / Total Time.*

.. index::
  single: progress field
.. 




:project_id: Project, many2one



.. index::
  single: project_id field
.. 




:type: Type, many2one



.. index::
  single: type field
.. 




:procurement_id: Procurement, many2one



.. index::
  single: procurement_id field
.. 




:description: Description, text



.. index::
  single: description field
.. 




:child_ids: Delegated Tasks, one2many



.. index::
  single: child_ids field
.. 




:work_ids: Work done, one2many



.. index::
  single: work_ids field
.. 




:active: Active, boolean



.. index::
  single: active field
.. 




:delay_hours: Delay Hours, float, readonly

    *Computed as: Total Time - Estimated Time. It gives the difference of the time estimated by the project manager and the real time to close the task.*

.. index::
  single: delay_hours field
.. 




:name: Task summary, char, required



.. index::
  single: name field
.. 




:date_deadline: Deadline, datetime



.. index::
  single: date_deadline field
.. 




:date_planned: Planned Date, datetime



.. index::
  single: date_planned field
.. 




:notes: Notes, text



.. index::
  single: notes field
.. 




:date_close: Date Closed, datetime, readonly



.. index::
  single: date_close field
.. 




:total_hours: Total Hours, float, readonly

    *Computed as: Time Spent + Remaining Time.*

.. index::
  single: total_hours field
.. 




:history: Task Details, text, readonly



.. index::
  single: history field
.. 




:remaining_hours: Remaining Hours, float

    *Total remaining time, can be re-estimated periodically by the assignee of the task.*

.. index::
  single: remaining_hours field
.. 



Object: Task Work
#################

.. index::
  single: Task Work object
.. 


:timesheet_line_id: Timesheet Line, many2one



.. index::
  single: timesheet_line_id field
.. 




:user_id: Done by, many2one, required



.. index::
  single: user_id field
.. 




:name: Work summary, char



.. index::
  single: name field
.. 




:task_id: Task, many2one, required



.. index::
  single: task_id field
.. 




:zip_id: Zip, many2one



.. index::
  single: zip_id field
.. 




:grant_id: Grant, many2one



.. index::
  single: grant_id field
.. 




:contact_id: Contact, many2one



.. index::
  single: contact_id field
.. 




:hours: Time Spent, float



.. index::
  single: hours field
.. 




:date: Date, datetime



.. index::
  single: date field
.. 




:partner_id: Partner, many2one



.. index::
  single: partner_id field
.. 




:hr_analytic_timesheet_id: Related Timeline Id, integer



.. index::
  single: hr_analytic_timesheet_id field
.. 



Object: config.compute.remaining
################################

.. index::
  single: config.compute.remaining object
.. 


:remaining_hours: Remaining Hours, float

    *Total remaining time, can be re-estimated periodically by the assignee of the task.*

.. index::
  single: remaining_hours field
.. 

