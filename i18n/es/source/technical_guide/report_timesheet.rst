
.. i18n: .. module:: report_timesheet
.. i18n:     :synopsis: Timesheet - Reporting (Official, Quality Certified)
.. i18n:     :noindex:
.. i18n: .. 

.. module:: report_timesheet
    :synopsis: Timesheet - Reporting (Official, Quality Certified)
    :noindex:
.. 

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. i18n: Timesheet - Reporting (*report_timesheet*)
.. i18n: ==========================================
.. i18n: :Module: report_timesheet
.. i18n: :Name: Timesheet - Reporting
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: report_timesheet
.. i18n: :Web: http://www.openerp.com
.. i18n: :Official module: yes
.. i18n: :Quality certified: yes

Timesheet - Reporting (*report_timesheet*)
==========================================
:Module: report_timesheet
:Name: Timesheet - Reporting
:Version: 5.0.1.0
:Author: Tiny
:Directory: report_timesheet
:Web: http://www.openerp.com
:Official module: yes
:Quality certified: yes

.. i18n: Description
.. i18n: -----------

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   Module to add timesheet views like
.. i18n:       All Month, Timesheet By User, Timesheet Of Month, Timesheet By Account

::

  Module to add timesheet views like
      All Month, Timesheet By User, Timesheet Of Month, Timesheet By Account

.. i18n: Dependencies
.. i18n: ------------

Dependencies
------------

.. i18n:  * :mod:`hr_timesheet`
.. i18n:  * :mod:`hr_timesheet_invoice`

 * :mod:`hr_timesheet`
 * :mod:`hr_timesheet_invoice`

.. i18n: Reports
.. i18n: -------

Reports
-------

.. i18n: None

None

.. i18n: Menus
.. i18n: -------

Menus
-------

.. i18n:  * Human Resources/Reporting/This Month
.. i18n:  * Human Resources/Reporting/This Month/Timesheet by user (this month)
.. i18n:  * Human Resources/Reporting/This Month/My Timesheet of the Month
.. i18n:  * Human Resources/Reporting/All Months
.. i18n:  * Human Resources/Reporting/All Months/Timesheet by User
.. i18n:  * Human Resources/Reporting/All Months/Timesheet by Invoice
.. i18n:  * Human Resources/Reporting/This Month/My timesheets to invoice
.. i18n:  * Human Resources/Reporting/All Months/Daily Timesheet by Account
.. i18n:  * Human Resources/Reporting/This Month/My daily timesheets by account
.. i18n:  * Human Resources/Reporting/All Months/Timesheet by Account
.. i18n:  * Human Resources/Reporting/This Month/My timesheets by account

 * Human Resources/Reporting/This Month
 * Human Resources/Reporting/This Month/Timesheet by user (this month)
 * Human Resources/Reporting/This Month/My Timesheet of the Month
 * Human Resources/Reporting/All Months
 * Human Resources/Reporting/All Months/Timesheet by User
 * Human Resources/Reporting/All Months/Timesheet by Invoice
 * Human Resources/Reporting/This Month/My timesheets to invoice
 * Human Resources/Reporting/All Months/Daily Timesheet by Account
 * Human Resources/Reporting/This Month/My daily timesheets by account
 * Human Resources/Reporting/All Months/Timesheet by Account
 * Human Resources/Reporting/This Month/My timesheets by account

.. i18n: Views
.. i18n: -----

Views
-----

.. i18n:  * report_timesheet.user.graph (graph)
.. i18n:  * report_timesheet.timesheet.user.form (form)
.. i18n:  * report_timesheet.timesheet.user.tree (tree)
.. i18n:  * report_timesheet.account.date.graph (graph)
.. i18n:  * report_timesheet.invoice.graph (graph)
.. i18n:  * report_timesheet.timesheet.invoice.form (form)
.. i18n:  * report_timesheet.timesheet.invoice.tree (tree)
.. i18n:  * report_timesheet.account.date.tree (tree)
.. i18n:  * report_timesheet.account.date.graph (graph)
.. i18n:  * report_timesheet.timesheet.account.date.form (form)
.. i18n:  * report_timesheet.account.tree (tree)
.. i18n:  * report_timesheet.account.graph (graph)
.. i18n:  * report_timesheet.timesheet.account.form (form)

 * report_timesheet.user.graph (graph)
 * report_timesheet.timesheet.user.form (form)
 * report_timesheet.timesheet.user.tree (tree)
 * report_timesheet.account.date.graph (graph)
 * report_timesheet.invoice.graph (graph)
 * report_timesheet.timesheet.invoice.form (form)
 * report_timesheet.timesheet.invoice.tree (tree)
 * report_timesheet.account.date.tree (tree)
 * report_timesheet.account.date.graph (graph)
 * report_timesheet.timesheet.account.date.form (form)
 * report_timesheet.account.tree (tree)
 * report_timesheet.account.graph (graph)
 * report_timesheet.timesheet.account.form (form)

.. i18n: Objects
.. i18n: -------

Objects
-------

.. i18n: Object: Timesheet per day (report_timesheet.user)
.. i18n: #################################################

Object: Timesheet per day (report_timesheet.user)
#################################################

.. i18n: :cost: Cost, float, readonly

:cost: Cost, float, readonly

.. i18n: :user_id: User, many2one, readonly

:user_id: User, many2one, readonly

.. i18n: :name: Date, date, readonly

:name: Date, date, readonly

.. i18n: :quantity: Quantity, float, readonly

:quantity: Quantity, float, readonly

.. i18n: Object: Timesheet per account (report_timesheet.account)
.. i18n: ########################################################

Object: Timesheet per account (report_timesheet.account)
########################################################

.. i18n: :quantity: Quantity, float, readonly

:quantity: Quantity, float, readonly

.. i18n: :user_id: User, many2one, readonly

:user_id: User, many2one, readonly

.. i18n: :name: Month, date, readonly

:name: Month, date, readonly

.. i18n: :account_id: Analytic Account, many2one, readonly

:account_id: Analytic Account, many2one, readonly

.. i18n: Object: Daily timesheet per account (report_timesheet.account.date)
.. i18n: ###################################################################

Object: Daily timesheet per account (report_timesheet.account.date)
###################################################################

.. i18n: :quantity: Quantity, float, readonly

:quantity: Quantity, float, readonly

.. i18n: :user_id: User, many2one, readonly

:user_id: User, many2one, readonly

.. i18n: :name: Date, date, readonly

:name: Date, date, readonly

.. i18n: :account_id: Analytic Account, many2one, readonly

:account_id: Analytic Account, many2one, readonly

.. i18n: Object: Costs to invoice (report_timesheet.invoice)
.. i18n: ###################################################

Object: Costs to invoice (report_timesheet.invoice)
###################################################

.. i18n: :amount_invoice: To invoice, float, readonly

:amount_invoice: To invoice, float, readonly

.. i18n: :quantity: Quantity, float, readonly

:quantity: Quantity, float, readonly

.. i18n: :user_id: User, many2one, readonly

:user_id: User, many2one, readonly

.. i18n: :manager_id: Manager, many2one, readonly

:manager_id: Manager, many2one, readonly

.. i18n: :account_id: Project, many2one, readonly

:account_id: Project, many2one, readonly
