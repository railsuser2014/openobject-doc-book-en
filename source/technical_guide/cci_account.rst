
Module CCI Account (*cci_account*)
==================================
:Module: cci_account
:Name: CCI Account
:Version: 5.0.1.0
:Directory: cci_account
:Web: http://www.openerp.com

Description
-----------

::

  specific module for cci project which will use account module (Reports).

Dependencies
------------

 * account_invoice_layout - installed
 * sale - installed
 * account_analytic_plans - installed
 * l10n_be - installed
 * base_vat - installed
 * cci_partner - installed
 * membership - installed

Reports
-------

 * Draft Invoices

 * Print VCS

Menus
-------

 * Financial Management/Periodical Processing/Use Models

Views
-----

 * \* INHERIT account.invoice.supplier.form.inherit (form)
 * \* INHERIT account.invoice.form.inherit (form)
 * \* INHERIT account.bank.statement.form (form)
 * \* INHERIT account.invoice.supplier.form (form)
 * \* INHERIT account.invoice.form (form)
 * \* INHERIT account.invoice.supplier.form (form)
 * \* INHERIT account.invoice.form (form)
 * \* INHERIT sale.order.form (form)


Objects
-------

None
