
Module Scrum, Agile Development Method (*scrum*)
================================================
:Module: scrum
:Name: Scrum, Agile Development Method
:Version: 5.0.1.0
:Directory: scrum
:Web: 

Description
-----------

::

  This modules implements all concepts defined by the scrum project
      management methodology for IT companies:
      * Project with sprints, product owner, scrum master
      * Sprints with reviews, daily meetings, feedbacks
      * Product backlog
      * Sprint backlog
  
      It adds some concepts to the project management module:
      * Mid-term, long-term road-map
      * Customers/functional requests VS technical ones
  
      It also create a new reporting:
      * Burn-down chart
  
      The scrum projects and tasks inherits from the real projects and
      tasks, so you can continue working on normal tasks that will also
      include tasks from scrum projects.
  
      More information on the methodology:
      * http://controlchaos.com

Dependencies
------------

 * project - installed
 * process - installed

Reports
-------

None


Menus
-------

 * Project Management/Scrum
 * Project Management/Scrum/Projects
 * Project Management/Scrum/Projects/Edit Projects
 * Project Management/Scrum/Backlogs
 * Project Management/Scrum/Backlogs/Draft Backlogs
 * Project Management/Scrum/Backlogs/Opened Backlogs
 * Project Management/Scrum/Sprint
 * Project Management/Scrum/Sprint/Opened Sprints
 * Project Management/Scrum/Sprint/Draft Sprints
 * Project Management/Scrum/Sprint/Sprints Done
 * Project Management/Scrum/Sprint/My Sprints (Product Owner)
 * Project Management/Scrum/Sprint/My Sprints (Scrum Master)
 * Project Management/Scrum/Sprint/My Sprints (Product Owner)/My opened sprints (Product Owner)
 * Project Management/Scrum/Sprint/My Sprints (Scrum Master)/My opened sprints (Scrum Master)
 * Project Management/Scrum/Scrum Meeting
 * Project Management/Scrum/All Tasks
 * Project Management/Scrum/All Tasks/My tasks
 * Project Management/Scrum/All Tasks/My tasks/My opened tasks
 * Project Management/Tasks/All Tasks/Opened tasks

Views
-----

 * \* INHERIT scrum.project.form (form)
 * scrum.project.tree (tree)
 * scrum.product.backlog.tree (tree)
 * scrum.product.backlog.form (form)
 * scrum.sprint.tree (tree)
 * scrum.sprint.form (form)
 * scrum.meeting.tree (tree)
 * Scrum Meeting (form)
 * \* INHERIT scrum.task.form (form)


Objects
-------

Object: Scrum Team
##################

.. index::
  single: Scrum Team object
.. 


:users_id: Users, many2many



.. index::
  single: users_id field
.. 




:name: Team Name, char



.. index::
  single: name field
.. 



Object: Scrum Project
#####################

.. index::
  single: Scrum Project object
.. 


:tasks: Scrum Tasks, one2many



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




:priority: Sequence, integer



.. index::
  single: priority field
.. 




:parent_id: Parent project, many2one



.. index::
  single: parent_id field
.. 




:state: State, selection, required, readonly



.. index::
  single: state field
.. 




:timesheet_id: Working Time, many2one

    *Timetable working hours to adjust the gantt diagram report*

.. index::
  single: timesheet_id field
.. 




:scrum: Is Scrum, integer



.. index::
  single: scrum field
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




:sprint_size: Sprint Days, integer



.. index::
  single: sprint_size field
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




:product_owner_id: Product Owner, many2one



.. index::
  single: product_owner_id field
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



Object: Scrum Sprint
####################

.. index::
  single: Scrum Sprint object
.. 


:date_stop: Ending Date, date, required



.. index::
  single: date_stop field
.. 




:planned_hours: Planned Hours, float, readonly



.. index::
  single: planned_hours field
.. 




:name: Sprint Name, char, required



.. index::
  single: name field
.. 




:retrospective: Sprint Retrospective, text



.. index::
  single: retrospective field
.. 




:meetings_id: Daily Scrum, one2many



.. index::
  single: meetings_id field
.. 




:review: Sprint Review, text



.. index::
  single: review field
.. 




:date_start: Starting Date, date, required



.. index::
  single: date_start field
.. 




:scrum_master_id: Scrum Master, many2one, required



.. index::
  single: scrum_master_id field
.. 




:state: Status, selection, required



.. index::
  single: state field
.. 




:backlog_ids: Sprint Backlog, one2many



.. index::
  single: backlog_ids field
.. 




:effective_hours: Effective hours, float, readonly



.. index::
  single: effective_hours field
.. 




:progress: Progress (0-100), float, readonly



.. index::
  single: progress field
.. 




:project_id: Project, many2one, required



.. index::
  single: project_id field
.. 




:product_owner_id: Product Owner, many2one, required



.. index::
  single: product_owner_id field
.. 



Object: Product Backlog
#######################

.. index::
  single: Product Backlog object
.. 


:priority: Priority, selection



.. index::
  single: priority field
.. 




:planned_hours: Planned Hours, float, readonly



.. index::
  single: planned_hours field
.. 




:user_id: User, many2one



.. index::
  single: user_id field
.. 




:name: Feature, char, required



.. index::
  single: name field
.. 




:tasks_id: Tasks Details, one2many



.. index::
  single: tasks_id field
.. 




:sequence: Sequence, integer



.. index::
  single: sequence field
.. 




:note: Note, text



.. index::
  single: note field
.. 




:effective_hours: Effective hours, float, readonly



.. index::
  single: effective_hours field
.. 




:state: Status, selection, required



.. index::
  single: state field
.. 




:sprint_id: Sprint, many2one



.. index::
  single: sprint_id field
.. 




:active: Active, boolean



.. index::
  single: active field
.. 




:progress: Progress (0-100), float, readonly



.. index::
  single: progress field
.. 




:project_id: Scrum Project, many2one, required



.. index::
  single: project_id field
.. 



Object: Scrum Task
##################

.. index::
  single: Scrum Task object
.. 


:sequence: Sequence, integer



.. index::
  single: sequence field
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




:date_start: Starting Date, datetime



.. index::
  single: date_start field
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




:description: Description, text



.. index::
  single: description field
.. 




:scrum: Is Scrum, integer



.. index::
  single: scrum field
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




:product_backlog_id: Product Backlog, many2one



.. index::
  single: product_backlog_id field
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



Object: Scrum Meeting
#####################

.. index::
  single: Scrum Meeting object
.. 


:question_blocks: Blocks encountered, text



.. index::
  single: question_blocks field
.. 




:question_yesterday: Tasks since yesterday, text



.. index::
  single: question_yesterday field
.. 




:name: Meeting Name, char, required



.. index::
  single: name field
.. 




:question_today: Tasks for today, text



.. index::
  single: question_today field
.. 




:question_backlog: Backlog Accurate, text



.. index::
  single: question_backlog field
.. 




:sprint_id: Sprint, many2one, required



.. index::
  single: sprint_id field
.. 




:date: Meeting Date, date, required



.. index::
  single: date field
.. 

