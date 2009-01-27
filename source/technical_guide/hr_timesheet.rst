
Module Human Resources (Timesheet encoding) (*hr_timesheet*)
============================================================
:Module: hr_timesheet
:Name: Human Resources (Timesheet encoding)
:Version: 5.0.1.0
:Directory: hr_timesheet
:Web: http://www.openerp.com

Description
-----------

::

  This module implement a timesheet system. Each employee can encode and
  track their time spent on the different projects. A project is an
  analytic account and the time spent on a project generate costs on
  the analytic account.
  
  Lots of reporting on time and employee tracking are provided.
  
  It is completely integrated with the cost accounting module. It allows you
  to set up a management by affair.

Dependencies
------------

 * account - installed
 * hr - installed
 * base - installed
 * hr_attendance - installed
 * process - installed

Reports
-------

 * Employee timesheet

 * Employees timesheet

Menus
-------

 * Human Resources/Working Hours
 * Human Resources/Working Hours/My Working Hours
 * Human Resources/Working Hours/My Working Hours/My Working Hours of The Day
 * Human Resources/Working Hours/Working Hours
 * Human Resources/Working Hours/Working Hours/Working Hours of The Day
 * Human Resources/Reporting/Timesheet
 * Human Resources/Reporting/Timesheet/Employee timesheet
 * Human Resources/Reporting/Timesheet/Print my timesheet
 * Human Resources/Reporting/Timesheet/Employees timesheet
 * Human Resources/Attendances/Sign in / Sign out by project

Views
-----

 * hr.analytic.timesheet.tree (tree)
 * hr.analytic.timesheet.form (form)
 * \* INHERIT hr.timesheet.employee.extd_form (form)
 * \* INHERIT account.analytic.account.invoice.form.inherit (form)


Objects
-------

Object: Timesheet line
######################

.. index::
  single: Timesheet line object
.. 


:code: Code, char



.. index::
  single: code field
.. 




:account_id: Analytic Account, many2one, required



.. index::
  single: account_id field
.. 




:general_account_id: General Account, many2one, required



.. index::
  single: general_account_id field
.. 




:line_id: Analytic line, many2one



.. index::
  single: line_id field
.. 




:date: Date, date, required



.. index::
  single: date field
.. 




:move_id: Move Line, many2one



.. index::
  single: move_id field
.. 




:name: Description, char, required



.. index::
  single: name field
.. 




:user_id: User, many2one



.. index::
  single: user_id field
.. 




:product_id: Product, many2one



.. index::
  single: product_id field
.. 




:product_uom_id: UoM, many2one



.. index::
  single: product_uom_id field
.. 




:journal_id: Analytic Journal, many2one, required



.. index::
  single: journal_id field
.. 




:to_invoice: Invoicing, many2one



.. index::
  single: to_invoice field
.. 




:amount: Amount, float, required



.. index::
  single: amount field
.. 




:unit_amount: Quantity, float



.. index::
  single: unit_amount field
.. 




:invoice_id: Invoice, many2one



.. index::
  single: invoice_id field
.. 




:sheet_id: Sheet, many2one, readonly



.. index::
  single: sheet_id field
.. 




:ref: Ref., char



.. index::
  single: ref field
.. 




:invoice_line_id: Invoice Line, many2one



.. index::
  single: invoice_line_id field
.. 

