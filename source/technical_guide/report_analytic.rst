
.. module:: report_analytic
    :synopsis: Analytic Account Reporting
    :noindex:
.. 

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

Analytic Account Reporting (*report_analytic*)
==============================================
:Module: report_analytic
:Name: Analytic Account Reporting
:Version: 5.0.1.0
:Directory: report_analytic
:Web: http://www.openerp.com
:Is certified: yes

Description
-----------

::

  A module that adds new reports based on analytic accounts.

Dependencies
------------

 * :mod:`account`
 * :mod:`hr_timesheet_invoice`

Reports
-------

None


Menus
-------

 * Financial Management/Reporting/Analytic/All Months/Expired analytic accounts

Views
-----

 * report.analytic.account.close.form (form)
 * report.analytic.account.close.tree (tree)
 * report.analytic.account.close.graph (graph)


Objects
-------

Object: Analytic account to close (report.analytic.account.close)
#################################################################



:name: Analytic account, many2one, readonly





:date_deadline: Deadline, date, readonly





:quantity_max: Max. Quantity, float, readonly





:state: State, char, readonly





:balance: Balance, float, readonly





:partner_id: Partner, many2one, readonly





:quantity: Quantity, float, readonly


