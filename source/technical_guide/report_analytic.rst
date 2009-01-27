
Module Analytic Account Reporting (*report_analytic*)
=====================================================
:Module: report_analytic
:Name: Analytic Account Reporting
:Version: 5.0.1.0
:Directory: report_analytic
:Web: http://www.openerp.com

Description
-----------

::

  A module that adds new reports based on analytic accounts.

Dependencies
------------

 * account - installed
 * hr_timesheet_invoice - installed

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

Object: Analytic account to close
#################################

.. index::
  single: Analytic account to close object
.. 


:name: Analytic account, many2one, readonly



.. index::
  single: name field
.. 




:date_deadline: Deadline, date, readonly



.. index::
  single: date_deadline field
.. 




:quantity_max: Max. Quantity, float, readonly



.. index::
  single: quantity_max field
.. 




:state: State, char, readonly



.. index::
  single: state field
.. 




:balance: Balance, float, readonly



.. index::
  single: balance field
.. 




:partner_id: Partner, many2one, readonly



.. index::
  single: partner_id field
.. 




:quantity: Quantity, float, readonly



.. index::
  single: quantity field
.. 

