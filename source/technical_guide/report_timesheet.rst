
Module Timesheet - Reporting (*report_timesheet*)
=================================================
:Module: report_timesheet
:Name: Timesheet - Reporting
:Version: 5.0.1.0
:Directory: report_timesheet
:Web: http://www.openerp.com

Description
-----------

::

  Module to add timesheet views like
      All Month, Timesheet By User, Timesheet Of Month, Timesheet By Account

Dependencies
------------

 * hr_timesheet - installed
 * hr_timesheet_invoice - installed

Reports
-------

None


Menus
-------

 * Human Resources/Reporting/This Month
 * Human Resources/Reporting/This Month/Timesheet by user (this month)
 * Human Resources/Reporting/This Month/My Timesheet of the Month
 * Human Resources/Reporting/All Months
 * Human Resources/Reporting/All Months/Timesheet by User
 * Human Resources/Reporting/All Months/Timesheet by Invoice
 * Human Resources/Reporting/This Month/My timesheets to invoice
 * Human Resources/Reporting/All Months/Daily Timesheet by Account
 * Human Resources/Reporting/This Month/My daily timesheets by account
 * Human Resources/Reporting/All Months/Timesheet by Account
 * Human Resources/Reporting/This Month/My timesheets by account

Views
-----

 * report_timesheet.user.graph (graph)
 * report_timesheet.timesheet.user.form (form)
 * report_timesheet.timesheet.user.tree (tree)
 * report_timesheet.account.date.graph (graph)
 * report_timesheet.invoice.graph (graph)
 * report_timesheet.timesheet.invoice.form (form)
 * report_timesheet.timesheet.invoice.tree (tree)
 * report_timesheet.account.date.tree (tree)
 * report_timesheet.account.date.graph (graph)
 * report_timesheet.timesheet.account.date.form (form)
 * report_timesheet.account.tree (tree)
 * report_timesheet.account.graph (graph)
 * report_timesheet.timesheet.account.form (form)


Objects
-------

Object: Timesheet per day
#########################

.. index::
  single: Timesheet per day object
.. 


:cost: Cost, float, readonly



.. index::
  single: cost field
.. 




:user_id: User, many2one, readonly



.. index::
  single: user_id field
.. 




:name: Date, date, readonly



.. index::
  single: name field
.. 




:quantity: Quantity, float, readonly



.. index::
  single: quantity field
.. 



Object: Timesheet per account
#############################

.. index::
  single: Timesheet per account object
.. 


:quantity: Quantity, float, readonly



.. index::
  single: quantity field
.. 




:user_id: User, many2one, readonly



.. index::
  single: user_id field
.. 




:name: Month, date, readonly



.. index::
  single: name field
.. 




:account_id: Analytic Account, many2one, readonly



.. index::
  single: account_id field
.. 



Object: Daily timesheet per account
###################################

.. index::
  single: Daily timesheet per account object
.. 


:quantity: Quantity, float, readonly



.. index::
  single: quantity field
.. 




:user_id: User, many2one, readonly



.. index::
  single: user_id field
.. 




:name: Date, date, readonly



.. index::
  single: name field
.. 




:account_id: Analytic Account, many2one, readonly



.. index::
  single: account_id field
.. 



Object: Costs to invoice
########################

.. index::
  single: Costs to invoice object
.. 


:amount_invoice: To invoice, float, readonly



.. index::
  single: amount_invoice field
.. 




:quantity: Quantity, float, readonly



.. index::
  single: quantity field
.. 




:user_id: User, many2one, readonly



.. index::
  single: user_id field
.. 




:manager_id: Manager, many2one, readonly



.. index::
  single: manager_id field
.. 




:account_id: Project, many2one, readonly



.. index::
  single: account_id field
.. 

