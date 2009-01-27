
Module Budget Management (*account_budget*)
===========================================
:Module: account_budget
:Name: Budget Management
:Version: 5.0.1.0
:Directory: account_budget
:Web: http://www.openerp.com

Description
-----------

::

  This module allows accountants to manage analytic and crossovered budgets.
  
  Once the Master Budgets and the Budgets defined (in Financial
  Management/Budgets/), the Project Managers can set the planned amount on each
  Analytic Account.
  
  The accountant has the possibility to see the total of amount planned for each
  Budget and Master Budget in order to ensure the total planned is not
  greater/lower than what he planned for this Budget/Master Budget. Each list of
  record can also be switched to a graphical view of it.
  
  Three reports are available:
      1. The first is available from a list of Budgets. It gives the spreading, for these Budgets, of the Analytic Accounts per Master Budgets.
  
      2. The second is a summary of the previous one, it only gives the spreading, for the selected Budgets, of the Analytic Accounts.
  
      3. The last one is available from the Analytic Chart of Accounts. It gives the spreading, for the selected Analytic Accounts, of the Master Budgets per Budgets.

Dependencies
------------

 * account - installed

Reports
-------

 * Print Budgets

 * Print Budgets

 * Print Budget

Menus
-------

 * Financial Management/Reporting/Budgets
 * Financial Management/Budgets
 * Financial Management/Budgets/Budgetary Positions
 * Financial Management/Budgets/Budget
 * Financial Management/Reporting/Budgets/Budget Lines

Views
-----

 * account.budget.post.tree (tree)
 * account.budget.post.dotation.form (form)
 * account.budget.post.dotation.tree (tree)
 * account.budget.post.form.inherit (form)
 * crossovered.budget.view.form (form)
 * crossovered.budget.view.tree (tree)
 * crossovered.budget.line.tree (tree)
 * crossovered.budget.line.form (form)
 * \* INHERIT account.analytic.account.form.inherot.cci (form)


Objects
-------

Object: Budgetary Position
##########################

.. index::
  single: Budgetary Position object
.. 


:code: Code, char, required



.. index::
  single: code field
.. 




:dotation_ids: Spreading, one2many



.. index::
  single: dotation_ids field
.. 




:name: Name, char, required



.. index::
  single: name field
.. 




:company_id: Company, many2one



.. index::
  single: company_id field
.. 




:crossovered_budget_line: Budget Lines, one2many



.. index::
  single: crossovered_budget_line field
.. 




:account_ids: Accounts, many2many



.. index::
  single: account_ids field
.. 



Object: Budget Dotation
#######################

.. index::
  single: Budget Dotation object
.. 


:post_id: Item, many2one



.. index::
  single: post_id field
.. 




:amount: Amount, float



.. index::
  single: amount field
.. 




:period_id: Period, many2one



.. index::
  single: period_id field
.. 




:name: Name, char



.. index::
  single: name field
.. 




:tot_planned: Total Planned Amount, float, readonly



.. index::
  single: tot_planned field
.. 



Object: Budget
##############

.. index::
  single: Budget object
.. 


:crossovered_budget_line: Budget Lines, one2many



.. index::
  single: crossovered_budget_line field
.. 




:name: Name, char, required



.. index::
  single: name field
.. 




:date_from: Start Date, date, required



.. index::
  single: date_from field
.. 




:state: Status, selection, required, readonly



.. index::
  single: state field
.. 




:code: Code, char, required



.. index::
  single: code field
.. 




:validating_user_id: Validate User, many2one, readonly



.. index::
  single: validating_user_id field
.. 




:date_to: End Date, date, required



.. index::
  single: date_to field
.. 




:creating_user_id: Responsible User, many2one



.. index::
  single: creating_user_id field
.. 



Object: Budget Lines
####################

.. index::
  single: Budget Lines object
.. 


:analytic_account_id: Analytic Account, many2one, required



.. index::
  single: analytic_account_id field
.. 




:general_budget_id: Budgetary Position, many2one, required



.. index::
  single: general_budget_id field
.. 




:theoritical_amount: Theoritical Amount, float, readonly



.. index::
  single: theoritical_amount field
.. 




:date_from: Start Date, date, required



.. index::
  single: date_from field
.. 




:planned_amount: Planned Amount, float, required



.. index::
  single: planned_amount field
.. 




:crossovered_budget_id: Budget, many2one, required



.. index::
  single: crossovered_budget_id field
.. 




:paid_date: Paid Date, date



.. index::
  single: paid_date field
.. 




:date_to: End Date, date, required



.. index::
  single: date_to field
.. 




:practical_amount: Practical Amount, float, readonly



.. index::
  single: practical_amount field
.. 




:percentage: Percentage, float, readonly



.. index::
  single: percentage field
.. 

