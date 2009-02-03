
.. module:: hr_timesheet_invoice
    :synopsis: Invoice on analytic lines (Quality Certified)
    :noindex:
.. 

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

    <style>
      div.body p#module-hr_timesheet_invoice {
        display: none;
      }
    </style>

Invoice on analytic lines (*hr_timesheet_invoice*)
==================================================
:Module: hr_timesheet_invoice
:Name: Invoice on analytic lines
:Version: 5.0.1.0
:Author: Tiny
:Directory: hr_timesheet_invoice
:Web: http://www.openerp.com
:Is certified: yes

Description
-----------

::

  Module to generate invoices based on costs (human resources, expenses, ...).
  You can define price lists in analytic account, make some theoretical revenue
  reports, eso.

Dependencies
------------

 * :mod:`account`
 * :mod:`hr_timesheet`

Reports
-------

 * Cost Ledger

 * Timesheet Profit

Menus
-------

 * Financial Management/Periodical Processing/Entries to invoice
 * Financial Management/Periodical Processing/Entries to invoice/Uninvoiced Entries
 * Financial Management/Periodical Processing/Entries to invoice/My Uninvoiced Entries
 * Financial Management/Configuration/Analytic Accounting/Analytic Accounts/Analytic Chart of Accounts/Open Analytic Accounts
 * .../Configuration/Analytic Accounting/Analytic Accounts/Analytic Chart of Accounts/Open Analytic Accounts/Unclosed Invoiceable Accounts
 * Financial Management/Configuration/Analytic Accounting/Analytic Accounts/Analytic Chart of Accounts/Draft Analytic Accounts
 * Financial Management/Configuration/Analytic Accounting/Analytic Accounts/Analytic Chart of Accounts/Pending Analytic Accounts
 * Financial Management/Configuration/Analytic Accounting/Analytic Accounts/Types of Invoicing
 * Human Resources/Reporting/Timesheet profit

Views
-----

 * \* INHERIT account.analytic.account.invoice.form (form)
 * \* INHERIT hr.analytic.timesheet.form (form)
 * \* INHERIT hr.analytic.timesheet.form2 (form)
 * \* INHERIT hr.analytic.timesheet.tree (tree)
 * \* INHERIT hr.analytic.timesheet.tree2 (tree)
 * \* INHERIT account.analytic.line.tree.to_invoice (tree)
 * \* INHERIT account.analytic.line.form.to_invoice (form)
 * hr_timesheet_invoice.factor.form (form)
 * hr_timesheet_invoice.factor.tree (tree)


Objects
-------

Object: Invoice rate (hr_timesheet_invoice.factor)
##################################################



:factor: Discount (%), float, required





:name: Internal name, char, required





:customer_name: Visible name, char


