
.. i18n: .. module:: account_budget
.. i18n:     :synopsis: Budget Management (Official, Quality Certified)
.. i18n:     :noindex:
.. i18n: .. 

.. module:: account_budget
    :synopsis: Budget Management (Official, Quality Certified)
    :noindex:
.. 

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. i18n: Budget Management (*account_budget*)
.. i18n: ====================================
.. i18n: :Module: account_budget
.. i18n: :Name: Budget Management
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: account_budget
.. i18n: :Web: http://www.openerp.com
.. i18n: :Official module: yes
.. i18n: :Quality certified: yes

Budget Management (*account_budget*)
====================================
:Module: account_budget
:Name: Budget Management
:Version: 5.0.1.0
:Author: Tiny
:Directory: account_budget
:Web: http://www.openerp.com
:Official module: yes
:Quality certified: yes

.. i18n: Description
.. i18n: -----------

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   This module allows accountants to manage analytic and crossovered budgets.
.. i18n:   
.. i18n:   Once the Master Budgets and the Budgets defined (in Financial Management/Budgets/), 
.. i18n:   the Project Managers can set the planned amount on each Analytic Account.
.. i18n:   
.. i18n:   The accountant has the possibility to see the total of amount planned for each Budget and 
.. i18n:   Master Budget in order to ensure the total planned is not greater/lower than what he planned 
.. i18n:   for this Budget/Master Budget. Each list of record can also be switched to a graphical view 
.. i18n:   of it.
.. i18n:   
.. i18n:   Three reports are available:
.. i18n:       1. The first is available from a list of Budgets. It gives the spreading, for these Budgets, 
.. i18n:          of the Analytic Accounts per Master Budgets.
.. i18n:   
.. i18n:       2. The second is a summary of the previous one, it only gives the spreading, for the selected 
.. i18n:          Budgets, of the Analytic Accounts.
.. i18n:   
.. i18n:       3. The last one is available from the Analytic Chart of Accounts. It gives the spreading, for the 
.. i18n:          selected Analytic Accounts, of the Master Budgets per Budgets.

::

  This module allows accountants to manage analytic and crossovered budgets.
  
  Once the Master Budgets and the Budgets defined (in Financial Management/Budgets/), 
  the Project Managers can set the planned amount on each Analytic Account.
  
  The accountant has the possibility to see the total of amount planned for each Budget and 
  Master Budget in order to ensure the total planned is not greater/lower than what he planned 
  for this Budget/Master Budget. Each list of record can also be switched to a graphical view 
  of it.
  
  Three reports are available:
      1. The first is available from a list of Budgets. It gives the spreading, for these Budgets, 
         of the Analytic Accounts per Master Budgets.
  
      2. The second is a summary of the previous one, it only gives the spreading, for the selected 
         Budgets, of the Analytic Accounts.
  
      3. The last one is available from the Analytic Chart of Accounts. It gives the spreading, for the 
         selected Analytic Accounts, of the Master Budgets per Budgets.

.. i18n: Dependencies
.. i18n: ------------

Dependencies
------------

.. i18n:  * :mod:`account`

 * :mod:`account`

.. i18n: Reports
.. i18n: -------

Reports
-------

.. i18n:  * Print Budgets
.. i18n: 
.. i18n:  * Print Budgets
.. i18n: 
.. i18n:  * Print Budget

 * Print Budgets

 * Print Budgets

 * Print Budget

.. i18n: Menus
.. i18n: -------

Menus
-------

.. i18n:  * Financial Management/Reporting/Budgets
.. i18n:  * Financial Management/Budgets
.. i18n:  * Financial Management/Budgets/Budgetary Positions
.. i18n:  * Financial Management/Budgets/Budget
.. i18n:  * Financial Management/Reporting/Budgets/Budget Lines

 * Financial Management/Reporting/Budgets
 * Financial Management/Budgets
 * Financial Management/Budgets/Budgetary Positions
 * Financial Management/Budgets/Budget
 * Financial Management/Reporting/Budgets/Budget Lines

.. i18n: Views
.. i18n: -----

Views
-----

.. i18n:  * account.budget.post.tree (tree)
.. i18n:  * account.budget.post.dotation.form (form)
.. i18n:  * account.budget.post.dotation.tree (tree)
.. i18n:  * account.budget.post.form.inherit (form)
.. i18n:  * crossovered.budget.view.form (form)
.. i18n:  * crossovered.budget.view.tree (tree)
.. i18n:  * crossovered.budget.line.tree (tree)
.. i18n:  * crossovered.budget.line.form (form)
.. i18n:  * \* INHERIT account.analytic.account.form.inherot.cci (form)

 * account.budget.post.tree (tree)
 * account.budget.post.dotation.form (form)
 * account.budget.post.dotation.tree (tree)
 * account.budget.post.form.inherit (form)
 * crossovered.budget.view.form (form)
 * crossovered.budget.view.tree (tree)
 * crossovered.budget.line.tree (tree)
 * crossovered.budget.line.form (form)
 * \* INHERIT account.analytic.account.form.inherot.cci (form)

.. i18n: Objects
.. i18n: -------

Objects
-------

.. i18n: Object: Budgetary Position (account.budget.post)
.. i18n: ################################################

Object: Budgetary Position (account.budget.post)
################################################

.. i18n: :code: Code, char, required

:code: Code, char, required

.. i18n: :dotation_ids: Spreading, one2many

:dotation_ids: Spreading, one2many

.. i18n: :name: Name, char, required

:name: Name, char, required

.. i18n: :company_id: Company, many2one

:company_id: Company, many2one

.. i18n: :crossovered_budget_line: Budget Lines, one2many

:crossovered_budget_line: Budget Lines, one2many

.. i18n: :account_ids: Accounts, many2many

:account_ids: Accounts, many2many

.. i18n: Object: Budget Dotation (account.budget.post.dotation)
.. i18n: ######################################################

Object: Budget Dotation (account.budget.post.dotation)
######################################################

.. i18n: :post_id: Item, many2one

:post_id: Item, many2one

.. i18n: :amount: Amount, float

:amount: Amount, float

.. i18n: :period_id: Period, many2one

:period_id: Period, many2one

.. i18n: :name: Name, char

:name: Name, char

.. i18n: :tot_planned: Total Planned Amount, float, readonly

:tot_planned: Total Planned Amount, float, readonly

.. i18n: Object: Budget (crossovered.budget)
.. i18n: ###################################

Object: Budget (crossovered.budget)
###################################

.. i18n: :crossovered_budget_line: Budget Lines, one2many

:crossovered_budget_line: Budget Lines, one2many

.. i18n: :name: Name, char, required

:name: Name, char, required

.. i18n: :date_from: Start Date, date, required

:date_from: Start Date, date, required

.. i18n: :state: Status, selection, required, readonly

:state: Status, selection, required, readonly

.. i18n: :code: Code, char, required

:code: Code, char, required

.. i18n: :validating_user_id: Validate User, many2one, readonly

:validating_user_id: Validate User, many2one, readonly

.. i18n: :date_to: End Date, date, required

:date_to: End Date, date, required

.. i18n: :creating_user_id: Responsible User, many2one

:creating_user_id: Responsible User, many2one

.. i18n: Object: Budget Lines (crossovered.budget.lines)
.. i18n: ###############################################

Object: Budget Lines (crossovered.budget.lines)
###############################################

.. i18n: :analytic_account_id: Analytic Account, many2one, required

:analytic_account_id: Analytic Account, many2one, required

.. i18n: :general_budget_id: Budgetary Position, many2one, required

:general_budget_id: Budgetary Position, many2one, required

.. i18n: :theoritical_amount: Theoritical Amount, float, readonly

:theoritical_amount: Theoritical Amount, float, readonly

.. i18n: :date_from: Start Date, date, required

:date_from: Start Date, date, required

.. i18n: :planned_amount: Planned Amount, float, required

:planned_amount: Planned Amount, float, required

.. i18n: :crossovered_budget_id: Budget, many2one, required

:crossovered_budget_id: Budget, many2one, required

.. i18n: :paid_date: Paid Date, date

:paid_date: Paid Date, date

.. i18n: :date_to: End Date, date, required

:date_to: End Date, date, required

.. i18n: :practical_amount: Practical Amount, float, readonly

:practical_amount: Practical Amount, float, readonly

.. i18n: :percentage: Percentage, float, readonly

:percentage: Percentage, float, readonly
