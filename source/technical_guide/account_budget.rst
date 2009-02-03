
.. module:: account_budget
    :synopsis: Budget Management (Quality Certified)
    :noindex:
.. 

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

    <style>
      div.body p#module-account_budget {
        display: none;
      }
    </style>

Budget Management (*account_budget*)
====================================
:Module: account_budget
:Name: Budget Management
:Version: 5.0.1.0
:Author: Tiny
:Directory: account_budget
:Web: http://www.openerp.com
:Is certified: yes

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

 * :mod:`account`

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

Object: Budgetary Position (account.budget.post)
################################################



:code: Code, char, required





:dotation_ids: Spreading, one2many





:name: Name, char, required





:company_id: Company, many2one





:crossovered_budget_line: Budget Lines, one2many





:account_ids: Accounts, many2many




Object: Budget Dotation (account.budget.post.dotation)
######################################################



:post_id: Item, many2one





:amount: Amount, float





:period_id: Period, many2one





:name: Name, char





:tot_planned: Total Planned Amount, float, readonly




Object: Budget (crossovered.budget)
###################################



:crossovered_budget_line: Budget Lines, one2many





:name: Name, char, required





:date_from: Start Date, date, required





:state: Status, selection, required, readonly





:code: Code, char, required





:validating_user_id: Validate User, many2one, readonly





:date_to: End Date, date, required





:creating_user_id: Responsible User, many2one




Object: Budget Lines (crossovered.budget.lines)
###############################################



:analytic_account_id: Analytic Account, many2one, required





:general_budget_id: Budgetary Position, many2one, required





:theoritical_amount: Theoritical Amount, float, readonly





:date_from: Start Date, date, required





:planned_amount: Planned Amount, float, required





:crossovered_budget_id: Budget, many2one, required





:paid_date: Paid Date, date





:date_to: End Date, date, required





:practical_amount: Practical Amount, float, readonly





:percentage: Percentage, float, readonly


