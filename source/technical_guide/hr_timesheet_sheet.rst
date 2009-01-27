
Module Timesheets (*hr_timesheet_sheet*)
========================================
:Module: hr_timesheet_sheet
:Name: Timesheets
:Version: 5.0.1.0
:Directory: hr_timesheet_sheet
:Web: http://www.openerp.com

Description
-----------

::

  This module help you easily encode and validate timesheet and attendances
  within the same view. The upper part of the view is for attendances and
  track (sign in/sign out) events. The lower part is for timesheet.
  
  Others tabs contains statistics views to help you analyse your
  time or the time of your team:
  * Time spent by day (with attendances)
  * Time spent by project
  
  This module also implement a complete timesheet validation process:
  * Draft sheet
  * Confirmation at the end of the period by the employee
  * Validation by the project manager
  
  The validation can be configured in te company:
  * Period size (day, week, month, year)
  * Maximal difference between timesheet and attendances

Dependencies
------------

 * hr_timesheet - installed
 * hr_timesheet_invoice - installed
 * process - installed

Reports
-------

None


Menus
-------

 * Human Resources/Timesheets
 * Human Resources/Timesheets/Timesheets
 * Human Resources/Timesheets/My timesheets
 * Human Resources/Timesheets/My timesheets/My timesheets to confirm
 * Human Resources/Timesheets/My Department's Timesheet
 * Human Resources/Timesheets/My Department's Timesheet/My Department's Timesheet to Validate
 * Human Resources/Timesheets/My Department's Timesheet/My Department's Timesheet to Confirm
 * Human Resources/Timesheets/My timesheets/My Current Timesheet
 * Human Resources/Timesheets/Timesheets/Timesheets To Confirm
 * Human Resources/Timesheets/Timesheets/Timesheets To Validate
 * Human Resources/Timesheets/Timesheets/Unvalidated Timesheets

Views
-----

 * hr.timesheet.sheet.tree (tree)
 * hr.timesheet.account.form (form)
 * hr.timesheet.account.tree (tree)
 * hr.timesheet.day.form (form)
 * hr.timesheet.day.tree (tree)
 * hr.timesheet.sheet.form (form)
 * \* INHERIT res.company.sheet (form)
 * \* INHERIT hr.analytic.timesheet.form (form)
 * \* INHERIT hr.attendance.form (form)
 * \* INHERIT hr.attendance.tree (tree)
 * hr.timesheet.sheet.tree.simplified (tree)


Objects
-------

Object: hr_timesheet_sheet.sheet
################################

.. index::
  single: hr_timesheet_sheet.sheet object
.. 


:total_attendance: Total Attendance, float, readonly



.. index::
  single: total_attendance field
.. 




:timesheet_ids: Timesheet lines, one2many, readonly



.. index::
  single: timesheet_ids field
.. 




:user_id: User, many2one, required



.. index::
  single: user_id field
.. 




:name: Description, char



.. index::
  single: name field
.. 




:total_timesheet: Total Timesheet, float, readonly



.. index::
  single: total_timesheet field
.. 




:date_from: Date from, date, required, readonly



.. index::
  single: date_from field
.. 




:date_to: Date to, date, required, readonly



.. index::
  single: date_to field
.. 




:attendances_ids: Attendances, one2many, readonly



.. index::
  single: attendances_ids field
.. 




:company_id: Company, many2one



.. index::
  single: company_id field
.. 




:period_ids: Period, one2many, readonly



.. index::
  single: period_ids field
.. 




:total_difference: Difference, float, readonly



.. index::
  single: total_difference field
.. 




:state: Status, selection, required, readonly



.. index::
  single: state field
.. 




:total_timesheet_day: Total Timesheet, float, readonly



.. index::
  single: total_timesheet_day field
.. 




:account_ids: Analytic accounts, one2many, readonly



.. index::
  single: account_ids field
.. 




:date_current: Current date, date, required



.. index::
  single: date_current field
.. 




:state_attendance: Current Status, selection, readonly



.. index::
  single: state_attendance field
.. 




:total_difference_day: Difference, float, readonly



.. index::
  single: total_difference_day field
.. 




:total_attendance_day: Total Attendance, float, readonly



.. index::
  single: total_attendance_day field
.. 



Object: Timesheets by period
############################

.. index::
  single: Timesheets by period object
.. 


:total_attendance: Attendance, float, readonly



.. index::
  single: total_attendance field
.. 




:total_difference: Difference, float, readonly



.. index::
  single: total_difference field
.. 




:sheet_id: Sheet, many2one, readonly



.. index::
  single: sheet_id field
.. 




:total_timesheet: Project Timesheet, float, readonly



.. index::
  single: total_timesheet field
.. 




:name: Date, date, readonly



.. index::
  single: name field
.. 



Object: Timesheets by period
############################

.. index::
  single: Timesheets by period object
.. 


:total: Total Time, float, readonly



.. index::
  single: total field
.. 




:sheet_id: Sheet, many2one, readonly



.. index::
  single: sheet_id field
.. 




:name: Analytic Account, many2one, readonly



.. index::
  single: name field
.. 




:invoice_rate: Invoice rate, many2one, readonly



.. index::
  single: invoice_rate field
.. 

