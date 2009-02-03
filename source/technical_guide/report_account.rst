
.. module:: report_account
    :synopsis: Account Reporting - Reporting (Quality Certified)
    :noindex:
.. 

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

    <style>
      div.body p#module-report_account {
        display: none;
      }
    </style>

Account Reporting - Reporting (*report_account*)
================================================
:Module: report_account
:Name: Account Reporting - Reporting
:Version: 5.0.1.0
:Author: Tiny
:Directory: report_account
:Web: http://www.openerp.com
:Is certified: yes

Description
-----------

::

  A module that adds new reports based on the account module.

Dependencies
------------

 * :mod:`account`

Reports
-------

None


Menus
-------

 * Financial Management/Reporting/Balance by Type of Account

Views
-----

 * report.account.receivable.graph (graph)
 * report.account.receivable.tree (tree)
 * report.account.receivable.form (form)


Objects
-------

Object: Receivable accounts (report.account.receivable)
#######################################################



:credit: Credit, float, readonly





:balance: Balance, float, readonly





:type: Account Type, selection, required





:name: Week of Year, char, readonly





:debit: Debit, float, readonly


