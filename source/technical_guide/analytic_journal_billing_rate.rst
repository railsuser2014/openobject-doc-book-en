
.. module:: analytic_journal_billing_rate
    :synopsis: Analytic Journal Billing Rate
    :noindex:
.. 

Analytic Journal Billing Rate (*analytic_journal_billing_rate*)
===============================================================
:Module: analytic_journal_billing_rate
:Name: Analytic Journal Billing Rate
:Version: 5.0.1.0
:Directory: analytic_journal_billing_rate
:Web: http://www.openerp.com
:Is certified: yes

Description
-----------

::

  This module allows you to define what is the default invoicing rate for a specific journal on a given account. This is mostly used when a user encode his timesheet: the values are retrieved and the fields are auto-filled... but the possibility to change these values is still available.
  
      Obviously if no data has been recorded for the current account, the default value is given as usual by the account data so that this module is perfectly compatible with older configurations.

Dependencies
------------

 * analytic_user_function - installed
 * account - installed
 * hr_timesheet_invoice - installed

Reports
-------

None


Menus
-------


None


Views
-----

 * analytic_journal_rate_grid.tree (tree)
 * analytic_journal_rate_grid.form (form)
 * \* INHERIT account.analytic.account.form (form)
 * \* INHERIT hr.timesheet.sheet.form (form)
 * \* INHERIT hr.analytic.timesheet.form (form)
 * \* INHERIT hr.analytic.timesheet.form (form)


Objects
-------

Object: Relation table between journals and billing rates (analytic_journal_rate_grid)
######################################################################################



:rate_id: Invoicing Rate, many2one





:journal_id: Analytic Journal, many2one, required





:account_id: Analytic Account, many2one, required


