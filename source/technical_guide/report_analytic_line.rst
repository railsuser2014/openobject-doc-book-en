
Module Analytic lines - Reporting (*report_analytic_line*)
==========================================================
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

.. index::
  single: Analytic lines to invoice report object
.. 


:account_id: Analytic account, many2one, readonly



.. index::
  single: account_id field
.. 




:product_uom_id: UoM, many2one, readonly



.. index::
  single: product_uom_id field
.. 




:amount: Amount, float, readonly



.. index::
  single: amount field
.. 




:product_id: Product, many2one, readonly



.. index::
  single: product_id field
.. 




:unit_amount: Units, float, readonly



.. index::
  single: unit_amount field
.. 




:sale_price: Sale price, float, readonly



.. index::
  single: sale_price field
.. 




:name: Month, date, readonly



.. index::
  single: name field
.. 

