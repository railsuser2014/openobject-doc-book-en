
Module account_analytic_package (*account_analytic_package*)
============================================================
:Module: account_analytic_package
:Name: account_analytic_package
:Version: 5.0.1.0
:Directory: account_analytic_package
:Web: http://www.tinyerp.com/

Description
-----------

::

  The Module allows to configure analytic account for product packages.
      Views for total and monthly product packages weight, Amount analysis.

Dependencies
------------

 * account - installed
 * product - installed
 * crm - installed

Reports
-------

None


Menus
-------

 * Financial Management/Reporting/Packages
 * Financial Management/Reporting/Packages/Service & Activity Units
 * Financial Management/Reporting/Packages/Service & Activity Units/Service Units
 * Financial Management/Reporting/Packages/Service & Activity Units/Activity Units
 * Financial Management/Reporting/Packages/Monthly Services & Activity Units
 * Financial Management/Reporting/Packages/Products Units

Views
-----

 * \* INHERIT account.analytic.account.package.form (form)
 * \* INHERIT crm.case.section.package.form (form)
 * \* INHERIT product.normal.package.form (form)
 * account.analytic.line.package.simplified.tree (tree)
 * account.analytic.line.package.form (form)
 * account.analytic.line.package.tree (tree)
 * account.analytic.line.package.month.graph (graph)
 * account.analytic.line.package.month.form (form)
 * account.analytic.line.package.month.tree (tree)
 * Products List (tree)


Objects
-------

Object: account.analytic.line.package
#####################################

.. index::
  single: account.analytic.line.package object
.. 


:account_id: Account, many2one, readonly



.. index::
  single: account_id field
.. 




:product_id: Product, many2one, readonly



.. index::
  single: product_id field
.. 




:unit_weight: Unit Weight, float, readonly



.. index::
  single: unit_weight field
.. 




:total_weight: Total Weight, float, readonly



.. index::
  single: total_weight field
.. 




:unit_amount: Quantity, float, readonly



.. index::
  single: unit_amount field
.. 




:date: Date, date, readonly



.. index::
  single: date field
.. 




:partner_id: Partner, many2one, readonly



.. index::
  single: partner_id field
.. 




:name: Name, char, readonly



.. index::
  single: name field
.. 



Object: account.analytic.line.package.month
###########################################

.. index::
  single: account.analytic.line.package.month object
.. 


:product_id: Product, many2one, readonly



.. index::
  single: product_id field
.. 




:total_service: Total Service, float, readonly



.. index::
  single: total_service field
.. 




:total_activity: Total Activity, float, readonly



.. index::
  single: total_activity field
.. 




:total_weight: Total Weight, float, readonly



.. index::
  single: total_weight field
.. 




:partner_id: Partner, many2one, readonly



.. index::
  single: partner_id field
.. 




:name: Date, date, readonly



.. index::
  single: name field
.. 

