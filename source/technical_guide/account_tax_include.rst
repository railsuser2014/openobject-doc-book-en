
.. module:: account_tax_include
    :synopsis: Invoices and prices with taxes included
    :noindex:
.. 

Invoices and prices with taxes included (*account_tax_include*)
===============================================================
:Module: account_tax_include
:Name: Invoices and prices with taxes included
:Version: 5.0.1.0
:Directory: account_tax_include
:Web: http://www.openerp.com

Description
-----------

::

  Allow the user to work tax included prices.
  Especially useful for b2c businesses.
      
  This module implement the modification on the invoice form.

Dependencies
------------

 * account - installed

Reports
-------

None


Menus
-------


None


Views
-----

 * \* INHERIT account.tax.exlcuded.view.form (form)
 * \* INHERIT account.invoice.vat.exlcuded.view.form (form)
 * \* INHERIT account.invoice.supplier.tax_include (form)
 * \* INHERIT account.invoice.supplier.tax_include2 (form)
 * \* INHERIT account.invoice.supplier.tax_include3 (form)
 * \* INHERIT account.invoice.line.tree (tree)


Objects
-------

None
