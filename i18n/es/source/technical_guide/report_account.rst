
.. i18n: .. module:: report_account
.. i18n:     :synopsis: Account Reporting - Reporting (Official, Quality Certified)
.. i18n:     :noindex:
.. i18n: .. 

.. module:: report_account
    :synopsis: Account Reporting - Reporting (Official, Quality Certified)
    :noindex:
.. 

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. i18n: Account Reporting - Reporting (*report_account*)
.. i18n: ================================================
.. i18n: :Module: report_account
.. i18n: :Name: Account Reporting - Reporting
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: report_account
.. i18n: :Web: http://www.openerp.com
.. i18n: :Official module: yes
.. i18n: :Quality certified: yes

Account Reporting - Reporting (*report_account*)
================================================
:Module: report_account
:Name: Account Reporting - Reporting
:Version: 5.0.1.0
:Author: Tiny
:Directory: report_account
:Web: http://www.openerp.com
:Official module: yes
:Quality certified: yes

.. i18n: Description
.. i18n: -----------

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   A module that adds new reports based on the account module.

::

  A module that adds new reports based on the account module.

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

.. i18n: None

None

.. i18n: Menus
.. i18n: -------

Menus
-------

.. i18n:  * Financial Management/Reporting/Balance by Type of Account

 * Financial Management/Reporting/Balance by Type of Account

.. i18n: Views
.. i18n: -----

Views
-----

.. i18n:  * report.account.receivable.graph (graph)
.. i18n:  * report.account.receivable.tree (tree)
.. i18n:  * report.account.receivable.form (form)

 * report.account.receivable.graph (graph)
 * report.account.receivable.tree (tree)
 * report.account.receivable.form (form)

.. i18n: Objects
.. i18n: -------

Objects
-------

.. i18n: Object: Receivable accounts (report.account.receivable)
.. i18n: #######################################################

Object: Receivable accounts (report.account.receivable)
#######################################################

.. i18n: :credit: Credit, float, readonly

:credit: Credit, float, readonly

.. i18n: :balance: Balance, float, readonly

:balance: Balance, float, readonly

.. i18n: :type: Account Type, selection, required

:type: Account Type, selection, required

.. i18n: :name: Week of Year, char, readonly

:name: Week of Year, char, readonly

.. i18n: :debit: Debit, float, readonly

:debit: Debit, float, readonly
