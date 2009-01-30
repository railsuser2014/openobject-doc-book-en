
.. module:: l10n_be
    :synopsis: Belgium - Plan Comptable Minimum Normalise
    :noindex:
.. 

Belgium - Plan Comptable Minimum Normalise (*l10n_be*)
======================================================
:Module: l10n_be
:Name: Belgium - Plan Comptable Minimum Normalise
:Version: 5.0.1.1
:Directory: l10n_be
:Web: 

Description
-----------

::

  This is the base module to manage the accounting chart for Belgium in Open ERP.
  
      After Installing this module,The Configuration wizard for accounting is launched.
      * We have the account templates which can be helpful to generate Charts of Accounts.
      * On that particular wizard,You will be asked to pass the name of the company,the chart template to follow,the no. of digits to generate the code for your account and Bank account,currency  to create Journals.
          Thus,the pure copy of Chart Template is generated.
      * This is the same wizard that runs from Financial Management/Configuration/Financial Accounting/Financial Accounts/Generate Chart of Accounts from a Chart Template.
  
      Wizards provided by this module:
      * Enlist the partners with their related VAT  and invoiced amounts.Prepares an XML file format.Path to access : Financial Management/Reporting/Listing of VAT Customers.
      * Prepares an XML file for Vat Declaration of the Main company of the User currently Logged in.Path to access : Financial Management/Reporting/Listing of VAT Customers.

Dependencies
------------

 * account - installed
 * account_report - installed
 * base_vat - installed
 * base_iban - installed
 * account_chart - installed

Reports
-------

None


Menus
-------

 * Financial Management/Legal Statements/Listing of VAT Customers
 * Financial Management/Legal Statements/Taxes Statement

Views
-----


None



Objects
-------

None
