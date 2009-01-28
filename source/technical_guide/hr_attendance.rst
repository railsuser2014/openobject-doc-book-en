
Attendances Of Employees (*hr_attendance*)
==========================================
:Module: hr_attendance
:Name: Attendances Of Employees
:Version: 5.0.1.1
:Directory: hr_attendance
:Web: 

Description
-----------

::

  This module aims to manage employee's attendances.

Dependencies
------------

 * base - installed
 * hr - installed

Reports
-------

 * Attendance Error Report

Menus
-------

 * Human Resources/Attendances
 * Human Resources/Attendances/Attendances
 * Human Resources/Configuration/Attendance Reasons
 * Human Resources/Attendances/Sign in / Sign out

Views
-----

 * hr.attendance.form (form)
 * hr.attendance.tree (tree)
 * hr.attendance.tree (tree)
 * hr.action.reason.form (form)
 * hr.action.reason.tree (tree)
 * \* INHERIT hr.employee.form1 (form)


Objects
-------

Object: Action reason
#####################



:name: Reason, char, required





:action_type: Action's type, selection




Object: Attendance
##################



:action: Action, selection, required





:employee_id: Employee, many2one, required





:sheet_id: Sheet, many2one, readonly





:name: Date, datetime, required





:action_desc: Action reason, many2one


