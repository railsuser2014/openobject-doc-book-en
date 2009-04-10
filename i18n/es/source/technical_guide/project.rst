
.. i18n: .. module:: project
.. i18n:     :synopsis: Project Management (Official, Quality Certified)
.. i18n:     :noindex:
.. i18n: .. 

.. module:: project
    :synopsis: Project Management (Official, Quality Certified)
    :noindex:
.. 

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. i18n: Project Management (*project*)
.. i18n: ==============================
.. i18n: :Module: project
.. i18n: :Name: Project Management
.. i18n: :Version: 5.0.1.1
.. i18n: :Author: Tiny
.. i18n: :Directory: project
.. i18n: :Web: http://www.openerp.com
.. i18n: :Official module: yes
.. i18n: :Quality certified: yes

Project Management (*project*)
==============================
:Module: project
:Name: Project Management
:Version: 5.0.1.1
:Author: Tiny
:Directory: project
:Web: http://www.openerp.com
:Official module: yes
:Quality certified: yes

.. i18n: Description
.. i18n: -----------

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   Project management module that track multi-level projects, tasks, works done on tasks, eso. 
.. i18n:   It is able to render planning, order tasks, eso.

::

  Project management module that track multi-level projects, tasks, works done on tasks, eso. 
  It is able to render planning, order tasks, eso.

.. i18n: Dependencies
.. i18n: ------------

Dependencies
------------

.. i18n:  * :mod:`product`
.. i18n:  * :mod:`account`
.. i18n:  * :mod:`hr`
.. i18n:  * :mod:`process`

 * :mod:`product`
 * :mod:`account`
 * :mod:`hr`
 * :mod:`process`

.. i18n: Reports
.. i18n: -------

Reports
-------

.. i18n:  * Gantt Representation
.. i18n: 
.. i18n:  * Gantt Representation

 * Gantt Representation

 * Gantt Representation

.. i18n: Menus
.. i18n: -------

Menus
-------

.. i18n:  * Project Management/Configuration
.. i18n:  * Project Management/Projects/New Project
.. i18n:  * Project Management
.. i18n:  * Project Management/Tasks
.. i18n:  * Project Management/Projects
.. i18n:  * Project Management/Projects/All projects
.. i18n:  * Project Management/Projects/All projects/Running projects
.. i18n:  * Project Management/Configuration/Template of Projects
.. i18n:  * Project Management/Projects/My Projects
.. i18n:  * Project Management/Projects/My Projects/My Running Projects
.. i18n:  * Project Management/Projects/Projects Structure
.. i18n:  * Project Management/Tasks/All Tasks
.. i18n:  * Project Management/Tasks/My Tasks
.. i18n:  * Project Management/Tasks/My Tasks/My Pending Tasks
.. i18n:  * Project Management/Tasks/My Tasks/My Current Tasks
.. i18n:  * Project Management/Tasks/My Tasks/My Current Tasks/My Tasks in Progress
.. i18n:  * Project Management/Tasks/My Tasks/My Current Tasks/My Draft Tasks
.. i18n:  * Project Management/Tasks/New Task
.. i18n:  * Project Management/Tasks/All Tasks/Tasks in Progress
.. i18n:  * Project Management/Tasks/All Tasks/Unassigned Tasks
.. i18n:  * Project Management/Configuration/Task Types

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

.. i18n: Views
.. i18n: -----

Views
-----

.. i18n:  * project.project.form (form)
.. i18n:  * project.project.tree (tree)
.. i18n:  * project.task.work.form (form)
.. i18n:  * project.task.work.tree (tree)
.. i18n:  * project.project.tree (tree)
.. i18n:  * Compute Remaining Hours  (form)
.. i18n:  * project.task.form (form)
.. i18n:  * project.task.tree (tree)
.. i18n:  * project.task.calendar (calendar)
.. i18n:  * project.task.gantt (gantt)
.. i18n:  * project.task.graph (graph)
.. i18n:  * project.task.type.form (form)
.. i18n:  * project.task.type.tree (tree)
.. i18n:  * \* INHERIT res.company.task.config (form)

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

.. i18n: Objects
.. i18n: -------

Objects
-------

.. i18n: Object: Project (project.project)
.. i18n: #################################

Object: Project (project.project)
#################################

.. i18n: :tasks: Project tasks, one2many

:tasks: Project tasks, one2many

.. i18n: :date_end: Expected End, date

:date_end: Expected End, date

.. i18n: :contact_id: Contact, many2one

:contact_id: Contact, many2one

.. i18n: :effective_hours: Time Spent, float, readonly

:effective_hours: Time Spent, float, readonly

.. i18n:     *Sum of spent hours of all tasks related to this project.*

    *Sum of spent hours of all tasks related to this project.*

.. i18n: :manager: Project Manager, many2one

:manager: Project Manager, many2one

.. i18n: :child_id: Subproject, one2many

:child_id: Subproject, one2many

.. i18n: :planned_hours: Planned Time, float, readonly

:planned_hours: Planned Time, float, readonly

.. i18n:     *Sum of planned hours of all tasks related to this project.*

    *Sum of planned hours of all tasks related to this project.*

.. i18n: :partner_id: Partner, many2one

:partner_id: Partner, many2one

.. i18n: :warn_footer: Mail Footer, text

:warn_footer: Mail Footer, text

.. i18n:     *Footer added at the beginning of the email for the warning message sent to the customer when a task is closed.*

    *Footer added at the beginning of the email for the warning message sent to the customer when a task is closed.*

.. i18n: :warn_manager: Warn Manager, boolean

:warn_manager: Warn Manager, boolean

.. i18n:     *If you check this field, the project manager will receive a request each time a task is completed by his team.*

    *If you check this field, the project manager will receive a request each time a task is completed by his team.*

.. i18n: :warn_customer: Warn Partner, boolean

:warn_customer: Warn Partner, boolean

.. i18n:     *If you check this, the user will have a popup when closing a task that propose a message to send by email to the customer.*

    *If you check this, the user will have a popup when closing a task that propose a message to send by email to the customer.*

.. i18n: :date_start: Starting Date, date

:date_start: Starting Date, date

.. i18n: :company_id: Company, many2one

:company_id: Company, many2one

.. i18n: :priority: Sequence, integer

:priority: Sequence, integer

.. i18n: :parent_id: Parent Project, many2one

:parent_id: Parent Project, many2one

.. i18n: :state: State, selection, required, readonly

:state: State, selection, required, readonly

.. i18n: :contact_id2: Contact, many2one

:contact_id2: Contact, many2one

.. i18n: :timesheet_id: Working Time, many2one

:timesheet_id: Working Time, many2one

.. i18n:     *Timetable working hours to adjust the gantt diagram report*

    *Timetable working hours to adjust the gantt diagram report*

.. i18n: :members: Project Members, many2many

:members: Project Members, many2many

.. i18n:     *Project's member. Not used in any computation, just for information purpose.*

    *Project's member. Not used in any computation, just for information purpose.*

.. i18n: :active: Active, boolean

:active: Active, boolean

.. i18n: :name: Project Name, char, required

:name: Project Name, char, required

.. i18n: :notes: Notes, text

:notes: Notes, text

.. i18n:     *Internal description of the project.*

    *Internal description of the project.*

.. i18n: :warn_header: Mail Header, text

:warn_header: Mail Header, text

.. i18n:     *Header added at the beginning of the email for the warning message sent to the customer when a task is closed.*

    *Header added at the beginning of the email for the warning message sent to the customer when a task is closed.*

.. i18n: :total_hours: Total Time, float, readonly

:total_hours: Total Time, float, readonly

.. i18n:     *Sum of total hours of all tasks related to this project.*

    *Sum of total hours of all tasks related to this project.*

.. i18n: :category_id: Analytic Account, many2one

:category_id: Analytic Account, many2one

.. i18n:     *Link this project to an analytic account if you need financial management on projects. It ables to connect projects with budgets, plannings, costs and revenues analysis, timesheet on projects, etc.*

    *Link this project to an analytic account if you need financial management on projects. It ables to connect projects with budgets, plannings, costs and revenues analysis, timesheet on projects, etc.*

.. i18n: :progress_rate: Progress, float, readonly

:progress_rate: Progress, float, readonly

.. i18n:     *Percent of tasks closed according to the total of tasks todo.*

    *Percent of tasks closed according to the total of tasks todo.*

.. i18n: Object: Project task type (project.task.type)
.. i18n: #############################################

Object: Project task type (project.task.type)
#############################################

.. i18n: :name: Type, char, required

:name: Type, char, required

.. i18n: :description: Description, text

:description: Description, text

.. i18n: Object: Task (project.task)
.. i18n: ###########################

Object: Task (project.task)
###########################

.. i18n: :sequence: Sequence, integer

:sequence: Sequence, integer

.. i18n: :context_id: Context, many2one

:context_id: Context, many2one

.. i18n: :date_reviewed: Reviewed Date, datetime

:date_reviewed: Reviewed Date, datetime

.. i18n: :effective_hours: Hours Spent, float, readonly

:effective_hours: Hours Spent, float, readonly

.. i18n:     *Computed using the sum of the task work done.*

    *Computed using the sum of the task work done.*

.. i18n: :planned_hours: Planned Hours, float, required, readonly

:planned_hours: Planned Hours, float, required, readonly

.. i18n:     *Estimated time to do the task, usually set by the project manager when the task is in draft state.*

    *Estimated time to do the task, usually set by the project manager when the task is in draft state.*

.. i18n: :partner_id: Partner, many2one

:partner_id: Partner, many2one

.. i18n: :user_id: Assigned to, many2one

:user_id: Assigned to, many2one

.. i18n: :timebox_id: Timebox, many2one

:timebox_id: Timebox, many2one

.. i18n: :date_start: Starting Date, datetime

:date_start: Starting Date, datetime

.. i18n: :company_id: Company, many2one

:company_id: Company, many2one

.. i18n: :priority: Importance, selection

:priority: Importance, selection

.. i18n: :parent_id: Parent Task, many2one

:parent_id: Parent Task, many2one

.. i18n: :state: Status, selection, required, readonly

:state: Status, selection, required, readonly

.. i18n: :progress: Progress (%), float, readonly

:progress: Progress (%), float, readonly

.. i18n:     *Computed as: Time Spent / Total Time.*

    *Computed as: Time Spent / Total Time.*

.. i18n: :project_id: Project, many2one

:project_id: Project, many2one

.. i18n: :type: Type, many2one

:type: Type, many2one

.. i18n: :procurement_id: Procurement, many2one

:procurement_id: Procurement, many2one

.. i18n: :description: Description, text

:description: Description, text

.. i18n: :child_ids: Delegated Tasks, one2many

:child_ids: Delegated Tasks, one2many

.. i18n: :work_ids: Work done, one2many

:work_ids: Work done, one2many

.. i18n: :active: Active, boolean

:active: Active, boolean

.. i18n: :delay_hours: Delay Hours, float, readonly

:delay_hours: Delay Hours, float, readonly

.. i18n:     *Computed as: Total Time - Estimated Time. It gives the difference of the time estimated by the project manager and the real time to close the task.*

    *Computed as: Total Time - Estimated Time. It gives the difference of the time estimated by the project manager and the real time to close the task.*

.. i18n: :name: Task summary, char, required

:name: Task summary, char, required

.. i18n: :date_deadline: Deadline, datetime

:date_deadline: Deadline, datetime

.. i18n: :date_planned: Planned Date, datetime

:date_planned: Planned Date, datetime

.. i18n: :notes: Notes, text

:notes: Notes, text

.. i18n: :date_close: Date Closed, datetime, readonly

:date_close: Date Closed, datetime, readonly

.. i18n: :total_hours: Total Hours, float, readonly

:total_hours: Total Hours, float, readonly

.. i18n:     *Computed as: Time Spent + Remaining Time.*

    *Computed as: Time Spent + Remaining Time.*

.. i18n: :history: Task Details, text, readonly

:history: Task Details, text, readonly

.. i18n: :remaining_hours: Remaining Hours, float

:remaining_hours: Remaining Hours, float

.. i18n:     *Total remaining time, can be re-estimated periodically by the assignee of the task.*

    *Total remaining time, can be re-estimated periodically by the assignee of the task.*

.. i18n: Object: Task Work (project.task.work)
.. i18n: #####################################

Object: Task Work (project.task.work)
#####################################

.. i18n: :timesheet_line_id: Timesheet Line, many2one

:timesheet_line_id: Timesheet Line, many2one

.. i18n: :user_id: Done by, many2one, required

:user_id: Done by, many2one, required

.. i18n: :name: Work summary, char

:name: Work summary, char

.. i18n: :task_id: Task, many2one, required

:task_id: Task, many2one, required

.. i18n: :zip_id: Zip, many2one

:zip_id: Zip, many2one

.. i18n: :grant_id: Grant, many2one

:grant_id: Grant, many2one

.. i18n: :contact_id: Contact, many2one

:contact_id: Contact, many2one

.. i18n: :hours: Time Spent, float

:hours: Time Spent, float

.. i18n: :date: Date, datetime

:date: Date, datetime

.. i18n: :partner_id: Partner, many2one

:partner_id: Partner, many2one

.. i18n: :hr_analytic_timesheet_id: Related Timeline Id, integer

:hr_analytic_timesheet_id: Related Timeline Id, integer

.. i18n: Object: config.compute.remaining (config.compute.remaining)
.. i18n: ###########################################################

Object: config.compute.remaining (config.compute.remaining)
###########################################################

.. i18n: :remaining_hours: Remaining Hours, float

:remaining_hours: Remaining Hours, float

.. i18n:     *Total remaining time, can be re-estimated periodically by the assignee of the task.*

    *Total remaining time, can be re-estimated periodically by the assignee of the task.*
