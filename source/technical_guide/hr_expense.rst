
Module Human Resources Expenses Tracking (*hr_expense*)
=======================================================
:Module: hr_expense
:Name: Human Resources Expenses Tracking
:Version: 5.0.1.0
:Directory: hr_expense
:Web: http://www.openerp.com

Description
-----------

::

  This module aims to manage employee's expenses.
  
      The whole workflow is implemented:
      * Draft expense
      * Confirmation of the sheet by the employee
      * Validation by his manager
      * Validation by the accountant and invoice creation
      * Payment of the invoice to the employee
  
      This module also use the analytic accounting and is compatible with
      the invoice on timesheet module so that you will be able to automatically
      re-invoice your customer's expenses if your work by project.

Dependencies
------------

 * hr - installed
 * account - installed
 * account_tax_include - installed

Reports
-------

 * Print HR expenses

Menus
-------

 * Human Resources/Expenses
 * Human Resources/Expenses/All expenses
 * Human Resources/Expenses/All expenses/Draft expenses
 * Human Resources/Expenses/All expenses/Expenses waiting validation
 * Human Resources/Expenses/All expenses/Expenses waiting invoice
 * Human Resources/Expenses/All expenses/Expenses waiting payment
 * Human Resources/Expenses/My Expenses
 * Human Resources/Expenses/New Expenses Sheet
 * Human Resources/Expenses/My Expenses/My Draft expenses
 * Human Resources/Expenses/My Expenses/My expenses waiting validation

Views
-----

 * hr.expense.line.tree (tree)
 * hr.expense.expense.tree (tree)
 * hr.expense.form (form)


Objects
-------

Object: Expense
###############

.. index::
  single: Expense object
.. 


:note: Note, text



.. index::
  single: note field
.. 




:employee_id: Employee, many2one, required



.. index::
  single: employee_id field
.. 




:user_id: User, many2one, required



.. index::
  single: user_id field
.. 




:name: Expense Sheet, char, required



.. index::
  single: name field
.. 




:account_move_id: Account Move, many2one



.. index::
  single: account_move_id field
.. 




:invoice_id: Invoice, many2one



.. index::
  single: invoice_id field
.. 




:journal_id: Force Journal, many2one



.. index::
  single: journal_id field
.. 




:id: Sheet ID, integer, readonly



.. index::
  single: id field
.. 




:currency_id: Currency, many2one, required



.. index::
  single: currency_id field
.. 




:user_valid: Validation User, many2one



.. index::
  single: user_valid field
.. 




:state: State, selection, readonly



.. index::
  single: state field
.. 




:date_valid: Date Valided, date



.. index::
  single: date_valid field
.. 




:date: Date, date



.. index::
  single: date field
.. 




:line_ids: Expense Lines, one2many



.. index::
  single: line_ids field
.. 




:amount: Total Amount, float, readonly



.. index::
  single: amount field
.. 




:ref: Reference, char



.. index::
  single: ref field
.. 




:date_confirm: Date Confirmed, date



.. index::
  single: date_confirm field
.. 



Object: Expense Line
####################

.. index::
  single: Expense Line object
.. 


:total_amount: Total, float, readonly



.. index::
  single: total_amount field
.. 




:analytic_account: Analytic account, many2one



.. index::
  single: analytic_account field
.. 




:description: Description, text



.. index::
  single: description field
.. 




:sequence: Sequence, integer



.. index::
  single: sequence field
.. 




:date_value: Date, date, required



.. index::
  single: date_value field
.. 




:uom_id: UoM, many2one, readonly



.. index::
  single: uom_id field
.. 




:product_id: Product, many2one, readonly



.. index::
  single: product_id field
.. 




:expense_id: Expense, many2one



.. index::
  single: expense_id field
.. 




:unit_amount: Unit Price, float, readonly



.. index::
  single: unit_amount field
.. 




:unit_quantity: Quantities, float, readonly



.. index::
  single: unit_quantity field
.. 




:ref: Reference, char



.. index::
  single: ref field
.. 




:name: Short Description, char, required



.. index::
  single: name field
.. 

