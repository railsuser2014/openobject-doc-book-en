
.. i18n: .. module:: account_analytic_analysis
.. i18n:     :synopsis: report_account_analytic (Official, Quality Certified)
.. i18n:     :noindex:
.. i18n: .. 

.. module:: account_analytic_analysis
    :synopsis: report_account_analytic (Official, Quality Certified)
    :noindex:
.. 

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. i18n: report_account_analytic (*account_analytic_analysis*)
.. i18n: =====================================================
.. i18n: :Module: account_analytic_analysis
.. i18n: :Name: report_account_analytic
.. i18n: :Version: 5.0.1.1
.. i18n: :Author: Camptocamp
.. i18n: :Directory: account_analytic_analysis
.. i18n: :Web: http://www.camptocamp.com/
.. i18n: :Official module: yes
.. i18n: :Quality certified: yes

report_account_analytic (*account_analytic_analysis*)
=====================================================
:Module: account_analytic_analysis
:Name: report_account_analytic
:Version: 5.0.1.1
:Author: Camptocamp
:Directory: account_analytic_analysis
:Web: http://www.camptocamp.com/
:Official module: yes
:Quality certified: yes

.. i18n: Description
.. i18n: -----------

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   Modify account analytic view to show important data for project manager of services companies.
.. i18n:   Add menu to show relevant information for each manager.

::

  Modify account analytic view to show important data for project manager of services companies.
  Add menu to show relevant information for each manager.

.. i18n: Dependencies
.. i18n: ------------

Dependencies
------------

.. i18n:  * :mod:`account`
.. i18n:  * :mod:`hr_timesheet`
.. i18n:  * :mod:`hr_timesheet_invoice`
.. i18n:  * :mod:`project`

 * :mod:`account`
 * :mod:`hr_timesheet`
 * :mod:`hr_timesheet_invoice`
 * :mod:`project`

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

.. i18n:  * Project Management/Financial Project Management
.. i18n:  * Project Management/Financial Project Management/Analytic Accounts
.. i18n:  * Project Management/Financial Project Management/Invoicing
.. i18n:  * Project Management/Financial Project Management/Analytic Accounts/My Accounts
.. i18n:  * Project Management/Financial Project Management/Invoicing/All Uninvoiced Entries
.. i18n:  * Project Management/Financial Project Management/Invoicing/My Uninvoiced Entries
.. i18n:  * Project Management/Financial Project Management/Analytic Accounts/My Accounts/My Current Accounts
.. i18n:  * Project Management/Financial Project Management/Analytic Accounts/My Accounts/My Pending Accounts
.. i18n:  * Project Management/Financial Project Management/Analytic Accounts/New Analytic Account
.. i18n:  * Project Management/Financial Project Management/Analytic Accounts/All Analytic Accounts
.. i18n:  * Project Management/Financial Project Management/Invoicing/Overpassed Accounts
.. i18n:  * Project Management/Financial Project Management/Analytic Accounts/All Analytic Accounts/Current Analytic Accounts
.. i18n:  * Project Management/Financial Project Management/Analytic Accounts/All Analytic Accounts/Pending Analytic Accounts

 * Project Management/Financial Project Management
 * Project Management/Financial Project Management/Analytic Accounts
 * Project Management/Financial Project Management/Invoicing
 * Project Management/Financial Project Management/Analytic Accounts/My Accounts
 * Project Management/Financial Project Management/Invoicing/All Uninvoiced Entries
 * Project Management/Financial Project Management/Invoicing/My Uninvoiced Entries
 * Project Management/Financial Project Management/Analytic Accounts/My Accounts/My Current Accounts
 * Project Management/Financial Project Management/Analytic Accounts/My Accounts/My Pending Accounts
 * Project Management/Financial Project Management/Analytic Accounts/New Analytic Account
 * Project Management/Financial Project Management/Analytic Accounts/All Analytic Accounts
 * Project Management/Financial Project Management/Invoicing/Overpassed Accounts
 * Project Management/Financial Project Management/Analytic Accounts/All Analytic Accounts/Current Analytic Accounts
 * Project Management/Financial Project Management/Analytic Accounts/All Analytic Accounts/Pending Analytic Accounts

.. i18n: Views
.. i18n: -----

Views
-----

.. i18n:  * \* INHERIT account.analytic.account.tree (tree)
.. i18n:  * \* INHERIT account.analytic.account.tree (tree)
.. i18n:  * account.analytic.account.simplified.tree (tree)

 * \* INHERIT account.analytic.account.tree (tree)
 * \* INHERIT account.analytic.account.tree (tree)
 * account.analytic.account.simplified.tree (tree)

.. i18n: Objects
.. i18n: -------

Objects
-------

.. i18n: Object: Hours summary by user (account_analytic_analysis.summary.user)
.. i18n: ######################################################################

Object: Hours summary by user (account_analytic_analysis.summary.user)
######################################################################

.. i18n: :account_id: Analytic Account, many2one, readonly

:account_id: Analytic Account, many2one, readonly

.. i18n: :unit_amount: Total Time, float, readonly

:unit_amount: Total Time, float, readonly

.. i18n: :user: User, many2one

:user: User, many2one

.. i18n: Object: Hours summary by month (account_analytic_analysis.summary.month)
.. i18n: ########################################################################

Object: Hours summary by month (account_analytic_analysis.summary.month)
########################################################################

.. i18n: :account_id: Analytic Account, many2one, readonly

:account_id: Analytic Account, many2one, readonly

.. i18n: :unit_amount: Total Time, float, readonly

:unit_amount: Total Time, float, readonly

.. i18n: :month: Month, char, readonly

:month: Month, char, readonly
