
.. i18n: .. module:: report_analytic_planning
.. i18n:     :synopsis: Analytic planning - Reporting (Official, Quality Certified)
.. i18n:     :noindex:
.. i18n: .. 

.. module:: report_analytic_planning
    :synopsis: Analytic planning - Reporting (Official, Quality Certified)
    :noindex:
.. 

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. i18n: Analytic planning - Reporting (*report_analytic_planning*)
.. i18n: ==========================================================
.. i18n: :Module: report_analytic_planning
.. i18n: :Name: Analytic planning - Reporting
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: report_analytic_planning
.. i18n: :Web: http://www.openerp.com
.. i18n: :Official module: yes
.. i18n: :Quality certified: yes

Analytic planning - Reporting (*report_analytic_planning*)
==========================================================
:Module: report_analytic_planning
:Name: Analytic planning - Reporting
:Version: 5.0.1.0
:Author: Tiny
:Directory: report_analytic_planning
:Web: http://www.openerp.com
:Official module: yes
:Quality certified: yes

.. i18n: Description
.. i18n: -----------

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   Planning on analytic accounts.

::

  Planning on analytic accounts.

.. i18n: Dependencies
.. i18n: ------------

Dependencies
------------

.. i18n:  * :mod:`account`
.. i18n:  * :mod:`hr_timesheet_invoice`
.. i18n:  * :mod:`project`
.. i18n:  * :mod:`report_analytic_line`

 * :mod:`account`
 * :mod:`hr_timesheet_invoice`
 * :mod:`project`
 * :mod:`report_analytic_line`

.. i18n: Reports
.. i18n: -------

Reports
-------

.. i18n:  * Planning

 * Planning

.. i18n: Menus
.. i18n: -------

Menus
-------

.. i18n:  * Human Resources/Planning
.. i18n:  * Human Resources/Planning/Plannings
.. i18n:  * Human Resources/Planning/My Plannings
.. i18n:  * Human Resources/Planning/My Plannings/My Current Plannings
.. i18n:  * Human Resources/Planning/Plannings/Current Plannings
.. i18n:  * Human Resources/Planning/New Planning
.. i18n:  * Human Resources/Reporting/Planning
.. i18n:  * Human Resources/Reporting/Planning/Planning Statistics
.. i18n:  * Human Resources/Reporting/Planning/My Planning Statistics
.. i18n:  * Human Resources/Reporting/Planning/Planning Statistics of My Projects

 * Human Resources/Planning
 * Human Resources/Planning/Plannings
 * Human Resources/Planning/My Plannings
 * Human Resources/Planning/My Plannings/My Current Plannings
 * Human Resources/Planning/Plannings/Current Plannings
 * Human Resources/Planning/New Planning
 * Human Resources/Reporting/Planning
 * Human Resources/Reporting/Planning/Planning Statistics
 * Human Resources/Reporting/Planning/My Planning Statistics
 * Human Resources/Reporting/Planning/Planning Statistics of My Projects

.. i18n: Views
.. i18n: -----

Views
-----

.. i18n:  * report.account.analytic.planning.tree (tree)
.. i18n:  * report.account.analytic.planning.form (form)
.. i18n:  * report.account.analytic.planning.stat.form (form)
.. i18n:  * report.account.analytic.planning.stat.tree (tree)
.. i18n:  * report.account.analytic.planning.stat.graph (graph)

 * report.account.analytic.planning.tree (tree)
 * report.account.analytic.planning.form (form)
 * report.account.analytic.planning.stat.form (form)
 * report.account.analytic.planning.stat.tree (tree)
 * report.account.analytic.planning.stat.graph (graph)

.. i18n: Objects
.. i18n: -------

Objects
-------

.. i18n: Object: Planning (report_account_analytic.planning)
.. i18n: ###################################################

Object: Planning (report_account_analytic.planning)
###################################################

.. i18n: :user_id: Responsible, many2one, required

:user_id: Responsible, many2one, required

.. i18n: :name: Planning Name, char, required

:name: Planning Name, char, required

.. i18n: :date_from: Start Date, date, required

:date_from: Start Date, date, required

.. i18n: :stat_account_ids: Planning by account, one2many, readonly

:stat_account_ids: Planning by account, one2many, readonly

.. i18n: :stat_ids: Planning analysis, one2many, readonly

:stat_ids: Planning analysis, one2many, readonly

.. i18n: :state: Status, selection, required

:state: Status, selection, required

.. i18n: :date_to: End Date, date, required

:date_to: End Date, date, required

.. i18n: :line_ids: Planning lines, one2many

:line_ids: Planning lines, one2many

.. i18n: :stat_user_ids: Planning by user, one2many, readonly

:stat_user_ids: Planning by user, one2many, readonly

.. i18n: :delegate_ids: unknown, one2many, readonly

:delegate_ids: unknown, one2many, readonly

.. i18n: :stat_product_ids: Planning by Post / Product, one2many, readonly

:stat_product_ids: Planning by Post / Product, one2many, readonly

.. i18n: Object: Planning Line (report_account_analytic.planning.line)
.. i18n: #############################################################

Object: Planning Line (report_account_analytic.planning.line)
#############################################################

.. i18n: :user_id: User, many2one

:user_id: User, many2one

.. i18n: :account_id: Analytic account, many2one, required

:account_id: Analytic account, many2one, required

.. i18n: :planning_id: Planning, many2one, required

:planning_id: Planning, many2one, required

.. i18n: :amount_unit: Qty UoM, many2one, required

:amount_unit: Qty UoM, many2one, required

.. i18n: :note: Note, text

:note: Note, text

.. i18n: :amount: Quantity, float, required

:amount: Quantity, float, required

.. i18n: :date_to: End date, date

:date_to: End date, date

.. i18n: :delegate_id: Delegate To, many2one

:delegate_id: Delegate To, many2one

.. i18n: :date_from: Start date, date

:date_from: Start date, date

.. i18n: :product_id: Job / Product, many2one, required

:product_id: Job / Product, many2one, required

.. i18n: Object: Planning account stat (report_account_analytic.planning.stat.account)
.. i18n: #############################################################################

Object: Planning account stat (report_account_analytic.planning.stat.account)
#############################################################################

.. i18n: :sum_amount_real: Timesheet, float, readonly

:sum_amount_real: Timesheet, float, readonly

.. i18n: :account_id: Analytic Account, many2one, required

:account_id: Analytic Account, many2one, required

.. i18n: :planning_id: Planning, many2one

:planning_id: Planning, many2one

.. i18n: :quantity: Planned, float, required

:quantity: Planned, float, required

.. i18n: Object: Planning stat (report_account_analytic.planning.stat)
.. i18n: #############################################################

Object: Planning stat (report_account_analytic.planning.stat)
#############################################################

.. i18n: :user_id: User, many2one

:user_id: User, many2one

.. i18n: :account_id: Account, many2one, required

:account_id: Account, many2one, required

.. i18n: :planning_id: Planning, many2one

:planning_id: Planning, many2one

.. i18n: :sum_amount_real: Timesheet, float, readonly

:sum_amount_real: Timesheet, float, readonly

.. i18n: :sum_amount: Planned hours, float, required

:sum_amount: Planned hours, float, required

.. i18n: :manager_id: Manager, many2one

:manager_id: Manager, many2one

.. i18n: :sum_amount_tasks: Tasks, float, readonly

:sum_amount_tasks: Tasks, float, readonly

.. i18n: Object: Planning user stat (report_account_analytic.planning.stat.user)
.. i18n: #######################################################################

Object: Planning user stat (report_account_analytic.planning.stat.user)
#######################################################################

.. i18n: :sum_amount_real: Timesheet, float, readonly

:sum_amount_real: Timesheet, float, readonly

.. i18n: :user_id: User, many2one

:user_id: User, many2one

.. i18n: :planning_id: Planning, many2one, required

:planning_id: Planning, many2one, required

.. i18n: :quantity: Planned, float, required

:quantity: Planned, float, required
