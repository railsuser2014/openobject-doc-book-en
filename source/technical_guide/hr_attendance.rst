
.. module:: hr_attendance
    :synopsis: Attendances Of Employees (Official, Quality Certified)
    :noindex:
.. 

.. raw:: html

      <br />
    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. tip:: This module is part of the Open ERP software, the leading Open Source 
  enterprise management system. If you want to discover Open ERP, check our 
  `screencasts <href="http://openerp.tv>`_ or download 
  `Open ERP <href="http://openerp.com>`_ directly.

Attendances Of Employees (*hr_attendance*)
==========================================
:Module: hr_attendance
:Name: Attendances Of Employees
:Version: 5.0.1.1
:Author: Tiny
:Directory: hr_attendance
:Web: 
:Official module: yes
:Quality certified: yes

Description
-----------

::

  This module aims to manage employee's attendances.

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 </download/modules/5.0/hr_attendance.zip>`_
  * `trunk </download/modules/trunk/hr_attendance.zip>`_


Dependencies
------------

 * :mod:`base`
 * :mod:`hr`

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

Object: Action reason (hr.action.reason)
########################################



:name: Reason, char, required





:action_type: Action's type, selection




Object: Attendance (hr.attendance)
##################################



:action: Action, selection, required





:employee_id: Employee, many2one, required





:sheet_id: Sheet, many2one, readonly





:name: Date, datetime, required





:action_desc: Action reason, many2one


