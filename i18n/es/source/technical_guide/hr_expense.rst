
.. i18n: .. module:: hr_expense
.. i18n:     :synopsis: Human Resources Expenses Tracking (Official, Quality Certified)
.. i18n:     :noindex:
.. i18n: .. 

.. module:: hr_expense
    :synopsis: Human Resources Expenses Tracking (Official, Quality Certified)
    :noindex:
.. 

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. i18n: Human Resources Expenses Tracking (*hr_expense*)
.. i18n: ================================================
.. i18n: :Module: hr_expense
.. i18n: :Name: Human Resources Expenses Tracking
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: hr_expense
.. i18n: :Web: http://www.openerp.com
.. i18n: :Official module: yes
.. i18n: :Quality certified: yes

Human Resources Expenses Tracking (*hr_expense*)
================================================
:Module: hr_expense
:Name: Human Resources Expenses Tracking
:Version: 5.0.1.0
:Author: Tiny
:Directory: hr_expense
:Web: http://www.openerp.com
:Official module: yes
:Quality certified: yes

.. i18n: Description
.. i18n: -----------

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   This module aims to manage employee's expenses.
.. i18n:   
.. i18n:       The whole workflow is implemented:
.. i18n:       * Draft expense
.. i18n:       * Confirmation of the sheet by the employee
.. i18n:       * Validation by his manager
.. i18n:       * Validation by the accountant and invoice creation
.. i18n:       * Payment of the invoice to the employee
.. i18n:   
.. i18n:       This module also use the analytic accounting and is compatible with
.. i18n:       the invoice on timesheet module so that you will be able to automatically
.. i18n:       re-invoice your customer's expenses if your work by project.

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

.. i18n: Dependencies
.. i18n: ------------

Dependencies
------------

.. i18n:  * :mod:`hr`
.. i18n:  * :mod:`account`
.. i18n:  * :mod:`account_tax_include`

 * :mod:`hr`
 * :mod:`account`
 * :mod:`account_tax_include`

.. i18n: Reports
.. i18n: -------

Reports
-------

.. i18n:  * Print HR expenses

 * Print HR expenses

.. i18n: Menus
.. i18n: -------

Menus
-------

.. i18n:  * Human Resources/Expenses
.. i18n:  * Human Resources/Expenses/All expenses
.. i18n:  * Human Resources/Expenses/All expenses/Draft expenses
.. i18n:  * Human Resources/Expenses/All expenses/Expenses waiting validation
.. i18n:  * Human Resources/Expenses/All expenses/Expenses waiting invoice
.. i18n:  * Human Resources/Expenses/All expenses/Expenses waiting payment
.. i18n:  * Human Resources/Expenses/My Expenses
.. i18n:  * Human Resources/Expenses/New Expenses Sheet
.. i18n:  * Human Resources/Expenses/My Expenses/My Draft expenses
.. i18n:  * Human Resources/Expenses/My Expenses/My expenses waiting validation

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

.. i18n: Views
.. i18n: -----

Views
-----

.. i18n:  * hr.expense.line.tree (tree)
.. i18n:  * hr.expense.expense.tree (tree)
.. i18n:  * hr.expense.form (form)

 * hr.expense.line.tree (tree)
 * hr.expense.expense.tree (tree)
 * hr.expense.form (form)

.. i18n: Objects
.. i18n: -------

Objects
-------

.. i18n: Object: Expense (hr.expense.expense)
.. i18n: ####################################

Object: Expense (hr.expense.expense)
####################################

.. i18n: :note: Note, text

:note: Note, text

.. i18n: :employee_id: Employee, many2one, required

:employee_id: Employee, many2one, required

.. i18n: :user_id: User, many2one, required

:user_id: User, many2one, required

.. i18n: :name: Expense Sheet, char, required

:name: Expense Sheet, char, required

.. i18n: :account_move_id: Account Move, many2one

:account_move_id: Account Move, many2one

.. i18n: :invoice_id: Invoice, many2one

:invoice_id: Invoice, many2one

.. i18n: :journal_id: Force Journal, many2one

:journal_id: Force Journal, many2one

.. i18n: :id: Sheet ID, integer, readonly

:id: Sheet ID, integer, readonly

.. i18n: :currency_id: Currency, many2one, required

:currency_id: Currency, many2one, required

.. i18n: :user_valid: Validation User, many2one

:user_valid: Validation User, many2one

.. i18n: :state: State, selection, readonly

:state: State, selection, readonly

.. i18n: :date_valid: Date Valided, date

:date_valid: Date Valided, date

.. i18n: :date: Date, date

:date: Date, date

.. i18n: :line_ids: Expense Lines, one2many

:line_ids: Expense Lines, one2many

.. i18n: :amount: Total Amount, float, readonly

:amount: Total Amount, float, readonly

.. i18n: :ref: Reference, char

:ref: Reference, char

.. i18n: :date_confirm: Date Confirmed, date

:date_confirm: Date Confirmed, date

.. i18n: Object: Expense Line (hr.expense.line)
.. i18n: ######################################

Object: Expense Line (hr.expense.line)
######################################

.. i18n: :total_amount: Total, float, readonly

:total_amount: Total, float, readonly

.. i18n: :analytic_account: Analytic account, many2one

:analytic_account: Analytic account, many2one

.. i18n: :description: Description, text

:description: Description, text

.. i18n: :sequence: Sequence, integer

:sequence: Sequence, integer

.. i18n: :date_value: Date, date, required

:date_value: Date, date, required

.. i18n: :uom_id: UoM, many2one, readonly

:uom_id: UoM, many2one, readonly

.. i18n: :product_id: Product, many2one, readonly

:product_id: Product, many2one, readonly

.. i18n: :expense_id: Expense, many2one

:expense_id: Expense, many2one

.. i18n: :unit_amount: Unit Price, float, readonly

:unit_amount: Unit Price, float, readonly

.. i18n: :unit_quantity: Quantities, float, readonly

:unit_quantity: Quantities, float, readonly

.. i18n: :ref: Reference, char

:ref: Reference, char

.. i18n: :name: Short Description, char, required

:name: Short Description, char, required
