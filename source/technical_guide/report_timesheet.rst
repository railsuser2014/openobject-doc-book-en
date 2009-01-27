
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



:cost: Cost, float, readonly





:user_id: User, many2one, readonly





:name: Date, date, readonly





:quantity: Quantity, float, readonly




Object: Timesheet per account
#############################



:quantity: Quantity, float, readonly





:user_id: User, many2one, readonly





:name: Month, date, readonly





:account_id: Analytic Account, many2one, readonly




Object: Daily timesheet per account
###################################



:quantity: Quantity, float, readonly





:user_id: User, many2one, readonly





:name: Date, date, readonly





:account_id: Analytic Account, many2one, readonly




Object: Costs to invoice
########################



:amount_invoice: To invoice, float, readonly





:quantity: Quantity, float, readonly





:user_id: User, many2one, readonly





:manager_id: Manager, many2one, readonly





:account_id: Project, many2one, readonly


