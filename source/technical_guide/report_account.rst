
Account Reporting - Reporting (*report_account*)
================================================
:Module: report_account
:Name: Account Reporting - Reporting
:Version: 5.0.1.0
:Directory: report_account
:Web: http://www.openerp.com

Description
-----------

::

  A module that adds new reports based on the account module.

Dependencies
------------

 * account - installed

Reports
-------

None


Menus
-------

 * Financial Management/Reporting/Balance by Type of Account

Views
-----

 * report.account.receivable.graph (graph)
 * report.account.receivable.tree (tree)
 * report.account.receivable.form (form)


Objects
-------

Object: Receivable accounts
###########################



:credit: Credit, float, readonly





:balance: Balance, float, readonly





:type: Account Type, selection, required





:name: Week of Year, char, readonly





:debit: Debit, float, readonly


