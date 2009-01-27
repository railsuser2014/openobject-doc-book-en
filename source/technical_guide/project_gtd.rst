
Module Getting Things Done - Time Management Module (*project_gtd*)
===================================================================
:Module: project_gtd
:Name: Getting Things Done - Time Management Module
:Version: 5.0.1.0
:Directory: project_gtd
:Web: 

Description
-----------

::

  This module implements all concepts defined by the Getting Things Done
  methodology. This world-wide used methodology is used for personal
  time management improvement.
  
  Getting Things Done (commonly abbreviated as GTD) is an action management
  method created by David Allen, and described in a book of the same name.
  
  GTD rests on the principle that a person needs to move tasks out of the mind by
  recording them externally. That way, the mind is freed from the job of
  remembering everything that needs to be done, and can concentrate on actually
  performing those tasks.

Dependencies
------------

 * project - installed

Reports
-------

None


Menus
-------

 * Project Management/Configuration/Time Management
 * Project Management/Configuration/Time Management/Contexts
 * Project Management/Configuration/Time Management/Contexts/My Contexts
 * Project Management/Configuration/Time Management/Timeboxes
 * Project Management/Configuration/Time Management/Timeboxes/My Timeboxes
 * Project Management/Time Management
 * Project Management/Time Management/My Inbox
 * Project Management/Time Management/All My Timeboxes
 * Project Management/Time Management/My Daily Timebox

Views
-----

 * project.gtd.context.tree (tree)
 * project.gtd.context.form (form)
 * project.gtd.timebox.tree (tree)
 * project.gtd.timebox.form (form)
 * project.task.gtd.inbox.tree (tree)
 * project.gtd.timebox.treelist (tree)
 * \* INHERIT project.task.form.timebox (form)


Objects
-------

Object: project.gtd.context
###########################

.. index::
  single: project.gtd.context object
.. 


:project_default_id: Default Project, many2one, required



.. index::
  single: project_default_id field
.. 




:name: Context, char, required



.. index::
  single: name field
.. 




:sequence: Sequence, integer



.. index::
  single: sequence field
.. 



Object: project.gtd.timebox
###########################

.. index::
  single: project.gtd.timebox object
.. 


:context6_id: Context 6, many2one



.. index::
  single: context6_id field
.. 




:task1_ids: Tasks, one2many



.. index::
  single: task1_ids field
.. 




:col_effective_hours: Effective Hours, boolean



.. index::
  single: col_effective_hours field
.. 




:task3_ids: Tasks, one2many



.. index::
  single: task3_ids field
.. 




:task6_ids: Tasks, one2many



.. index::
  single: task6_ids field
.. 




:task_ids: Tasks, one2many



.. index::
  single: task_ids field
.. 




:user_id: User, many2one, required



.. index::
  single: user_id field
.. 




:context4_id: Context 4, many2one



.. index::
  single: context4_id field
.. 




:parent_id: Parent Timebox, many2one



.. index::
  single: parent_id field
.. 




:task2_ids: Tasks, one2many



.. index::
  single: task2_ids field
.. 




:col_project: Project, boolean



.. index::
  single: col_project field
.. 




:type: Type, selection, required



.. index::
  single: type field
.. 




:col_date_start: Date Start, boolean



.. index::
  single: col_date_start field
.. 




:col_priority: Priority, boolean



.. index::
  single: col_priority field
.. 




:task4_ids: Tasks, one2many



.. index::
  single: task4_ids field
.. 




:child_ids: Childs Timebox, one2many



.. index::
  single: child_ids field
.. 




:context2_id: Context 2, many2one



.. index::
  single: context2_id field
.. 




:task5_ids: Tasks, one2many



.. index::
  single: task5_ids field
.. 




:context3_id: Context 3, many2one



.. index::
  single: context3_id field
.. 




:name: Timebox, char, required



.. index::
  single: name field
.. 




:context5_id: Context 5, many2one



.. index::
  single: context5_id field
.. 




:context1_id: Context 1, many2one, required



.. index::
  single: context1_id field
.. 




:col_planned_hours: Planned Hours, boolean



.. index::
  single: col_planned_hours field
.. 




:col_deadline: Deadline, boolean



.. index::
  single: col_deadline field
.. 

