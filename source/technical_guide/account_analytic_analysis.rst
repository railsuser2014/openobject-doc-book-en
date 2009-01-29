
report_account_analytic (*account_analytic_analysis*)
=====================================================
:Module: account_analytic_analysis
:Name: report_account_analytic
:Version: 5.0.1.1
:Directory: account_analytic_analysis
:Web: http://www.camptocamp.com/

Description
-----------

::

  Modify account analytic view to show
  important data for project manager of services companies.
  Add menu to show relevant information for each manager.

Dependencies
------------

 * account - installed
 * hr_timesheet - installed
 * hr_timesheet_invoice - installed
 * project - installed

Reports
-------

None


Menus
-------

 * Project Management/Financial Project Management
 * Project Management/Financial Project Management/Analytic Accounts
 * Project Management/Financial Project Management/Invoicing
 * Project Management/Financial Project Management/Analytic Accounts/My Accounts
 * Project Management/Financial Project Management/Invoicing/All Uninvoiced Entries
 * Project Management/Financial Project Management/Invoicing/My Uninvoiced Entries
 * Project Management/Financial Project Management/Analytic Accounts/My Accounts/My Current Accounts
 * Project Management/Financial Project Management/Analytic Accounts/My Accounts/My Pending Accounts
 * Project Management/Financial Project Management/Analytic Accounts/New Analytic Account
 * Project Management/Financial Project Management/Analytic Accounts/All Analytic Accounts
 * Project Management/Financial Project Management/Invoicing/Overpassed Accounts
 * Project Management/Financial Project Management/Analytic Accounts/All Analytic Accounts/Current Analytic Accounts
 * Project Management/Financial Project Management/Analytic Accounts/All Analytic Accounts/Pending Analytic Accounts

Views
-----

 * \* INHERIT account.analytic.account.tree (tree)
 * \* INHERIT account.analytic.account.tree (tree)
 * account.analytic.account.simplified.tree (tree)


Objects
-------

Object: Hours summary by user
#############################



:account_id: Analytic Account, many2one, readonly





:unit_amount: Total Time, float, readonly





:user: User, many2one




Object: Hours summary by month
##############################



:account_id: Analytic Account, many2one, readonly





:unit_amount: Total Time, float, readonly





:month: Month, char, readonly


