
.. module:: account_analytic_package
    :synopsis: account_analytic_package 
    :noindex:
.. 

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

account_analytic_package (*account_analytic_package*)
=====================================================
:Module: account_analytic_package
:Name: account_analytic_package
:Version: 5.0.1.0
:Author: Tiny
:Directory: account_analytic_package
:Web: http://www.tinyerp.com/
:Official module: no
:Quality certified: no

Description
-----------

::

  The Module allows to configure analytic account for product packages.
      Views for total and monthly product packages weight, Amount analysis.

Dependencies
------------

 * :mod:`account`
 * :mod:`product`
 * :mod:`crm`

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

Object: account.analytic.line.package (account.analytic.line.package)
#####################################################################



:account_id: Account, many2one, readonly





:product_id: Product, many2one, readonly





:unit_weight: Unit Weight, float, readonly





:total_weight: Total Weight, float, readonly





:unit_amount: Quantity, float, readonly





:date: Date, date, readonly





:partner_id: Partner, many2one, readonly





:name: Name, char, readonly




Object: account.analytic.line.package.month (account.analytic.line.package.month)
#################################################################################



:product_id: Product, many2one, readonly





:total_service: Total Service, float, readonly





:total_activity: Total Activity, float, readonly





:total_weight: Total Weight, float, readonly





:partner_id: Partner, many2one, readonly





:name: Date, date, readonly


