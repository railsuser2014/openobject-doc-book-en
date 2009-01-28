
Analytic lines - Reporting (*report_analytic_line*)
===================================================
:Module: report_analytic_line
:Name: Analytic lines - Reporting
:Version: 5.0.1.0
:Directory: report_analytic_line
:Web: http://www.openerp.com

Description
-----------

::

  A report on analytic lines, costs by products, months and accounts.

Dependencies
------------

 * account - installed
 * hr_timesheet_invoice - installed

Reports
-------

None


Menus
-------

 * Financial Management/Reporting/Analytic/All Months/Analytic Lines to Invoice

Views
-----

 * report.account.analytic.line.to.invoice (form)
 * report.account.analytic.line.to.invoice (tree)
 * report.account.analytic.line.to.invoice.graph (graph)


Objects
-------

Object: Analytic lines to invoice report
########################################



:account_id: Analytic account, many2one, readonly





:product_uom_id: UoM, many2one, readonly





:amount: Amount, float, readonly





:product_id: Product, many2one, readonly





:unit_amount: Units, float, readonly





:sale_price: Sale price, float, readonly





:name: Month, date, readonly


