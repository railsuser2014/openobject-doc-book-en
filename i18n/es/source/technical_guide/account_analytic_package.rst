
.. i18n: .. module:: account_analytic_package
.. i18n:     :synopsis: account_analytic_package 
.. i18n:     :noindex:
.. i18n: .. 

.. module:: account_analytic_package
    :synopsis: account_analytic_package 
    :noindex:
.. 

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. i18n: account_analytic_package (*account_analytic_package*)
.. i18n: =====================================================
.. i18n: :Module: account_analytic_package
.. i18n: :Name: account_analytic_package
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: account_analytic_package
.. i18n: :Web: http://www.openerp.com/
.. i18n: :Official module: no
.. i18n: :Quality certified: no

account_analytic_package (*account_analytic_package*)
=====================================================
:Module: account_analytic_package
:Name: account_analytic_package
:Version: 5.0.1.0
:Author: Tiny
:Directory: account_analytic_package
:Web: http://www.openerp.com/
:Official module: no
:Quality certified: no

.. i18n: Description
.. i18n: -----------

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   The Module allows to configure analytic account for product packages.
.. i18n:       Views for total and monthly product packages weight, Amount analysis.

::

  The Module allows to configure analytic account for product packages.
      Views for total and monthly product packages weight, Amount analysis.

.. i18n: Dependencies
.. i18n: ------------

Dependencies
------------

.. i18n:  * :mod:`account`
.. i18n:  * :mod:`product`
.. i18n:  * :mod:`crm`

 * :mod:`account`
 * :mod:`product`
 * :mod:`crm`

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

.. i18n:  * Financial Management/Reporting/Packages
.. i18n:  * Financial Management/Reporting/Packages/Service & Activity Units
.. i18n:  * Financial Management/Reporting/Packages/Service & Activity Units/Service Units
.. i18n:  * Financial Management/Reporting/Packages/Service & Activity Units/Activity Units
.. i18n:  * Financial Management/Reporting/Packages/Monthly Services & Activity Units
.. i18n:  * Financial Management/Reporting/Packages/Products Units

 * Financial Management/Reporting/Packages
 * Financial Management/Reporting/Packages/Service & Activity Units
 * Financial Management/Reporting/Packages/Service & Activity Units/Service Units
 * Financial Management/Reporting/Packages/Service & Activity Units/Activity Units
 * Financial Management/Reporting/Packages/Monthly Services & Activity Units
 * Financial Management/Reporting/Packages/Products Units

.. i18n: Views
.. i18n: -----

Views
-----

.. i18n:  * \* INHERIT account.analytic.account.package.form (form)
.. i18n:  * \* INHERIT crm.case.section.package.form (form)
.. i18n:  * \* INHERIT product.normal.package.form (form)
.. i18n:  * account.analytic.line.package.simplified.tree (tree)
.. i18n:  * account.analytic.line.package.form (form)
.. i18n:  * account.analytic.line.package.tree (tree)
.. i18n:  * account.analytic.line.package.month.graph (graph)
.. i18n:  * account.analytic.line.package.month.form (form)
.. i18n:  * account.analytic.line.package.month.tree (tree)
.. i18n:  * Products List (tree)

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

.. i18n: Objects
.. i18n: -------

Objects
-------

.. i18n: Object: account.analytic.line.package (account.analytic.line.package)
.. i18n: #####################################################################

Object: account.analytic.line.package (account.analytic.line.package)
#####################################################################

.. i18n: :account_id: Account, many2one, readonly

:account_id: Account, many2one, readonly

.. i18n: :product_id: Product, many2one, readonly

:product_id: Product, many2one, readonly

.. i18n: :unit_weight: Unit Weight, float, readonly

:unit_weight: Unit Weight, float, readonly

.. i18n: :total_weight: Total Weight, float, readonly

:total_weight: Total Weight, float, readonly

.. i18n: :unit_amount: Quantity, float, readonly

:unit_amount: Quantity, float, readonly

.. i18n: :date: Date, date, readonly

:date: Date, date, readonly

.. i18n: :partner_id: Partner, many2one, readonly

:partner_id: Partner, many2one, readonly

.. i18n: :name: Name, char, readonly

:name: Name, char, readonly

.. i18n: Object: account.analytic.line.package.month (account.analytic.line.package.month)
.. i18n: #################################################################################

Object: account.analytic.line.package.month (account.analytic.line.package.month)
#################################################################################

.. i18n: :product_id: Product, many2one, readonly

:product_id: Product, many2one, readonly

.. i18n: :total_service: Total Service, float, readonly

:total_service: Total Service, float, readonly

.. i18n: :total_activity: Total Activity, float, readonly

:total_activity: Total Activity, float, readonly

.. i18n: :total_weight: Total Weight, float, readonly

:total_weight: Total Weight, float, readonly

.. i18n: :partner_id: Partner, many2one, readonly

:partner_id: Partner, many2one, readonly

.. i18n: :name: Date, date, readonly

:name: Date, date, readonly
