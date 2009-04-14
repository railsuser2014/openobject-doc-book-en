
.. i18n: .. module:: report_analytic_line
.. i18n:     :synopsis: Analytic lines - Reporting (Official, Quality Certified)
.. i18n:     :noindex:
.. i18n: .. 

.. module:: report_analytic_line
    :synopsis: Analytic lines - Reporting (Official, Quality Certified)
    :noindex:
.. 

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. i18n: Analytic lines - Reporting (*report_analytic_line*)
.. i18n: ===================================================
.. i18n: :Module: report_analytic_line
.. i18n: :Name: Analytic lines - Reporting
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: report_analytic_line
.. i18n: :Web: http://www.openerp.com
.. i18n: :Official module: yes
.. i18n: :Quality certified: yes

Analytic lines - Reporting (*report_analytic_line*)
===================================================
:Module: report_analytic_line
:Name: Analytic lines - Reporting
:Version: 5.0.1.0
:Author: Tiny
:Directory: report_analytic_line
:Web: http://www.openerp.com
:Official module: yes
:Quality certified: yes

.. i18n: Description
.. i18n: -----------

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   A report on analytic lines, costs by products, months and accounts.

::

  A report on analytic lines, costs by products, months and accounts.

.. i18n: Dependencies
.. i18n: ------------

Dependencies
------------

.. i18n:  * :mod:`account`
.. i18n:  * :mod:`hr_timesheet_invoice`

 * :mod:`account`
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

.. i18n:  * Financial Management/Reporting/Analytic/All Months/Analytic Lines to Invoice

 * Financial Management/Reporting/Analytic/All Months/Analytic Lines to Invoice

.. i18n: Views
.. i18n: -----

Views
-----

.. i18n:  * report.account.analytic.line.to.invoice (form)
.. i18n:  * report.account.analytic.line.to.invoice (tree)
.. i18n:  * report.account.analytic.line.to.invoice.graph (graph)

 * report.account.analytic.line.to.invoice (form)
 * report.account.analytic.line.to.invoice (tree)
 * report.account.analytic.line.to.invoice.graph (graph)

.. i18n: Objects
.. i18n: -------

Objects
-------

.. i18n: Object: Analytic lines to invoice report (report.account.analytic.line.to.invoice)
.. i18n: ##################################################################################

Object: Analytic lines to invoice report (report.account.analytic.line.to.invoice)
##################################################################################

.. i18n: :account_id: Analytic account, many2one, readonly

:account_id: Analytic account, many2one, readonly

.. i18n: :product_uom_id: UoM, many2one, readonly

:product_uom_id: UoM, many2one, readonly

.. i18n: :amount: Amount, float, readonly

:amount: Amount, float, readonly

.. i18n: :product_id: Product, many2one, readonly

:product_id: Product, many2one, readonly

.. i18n: :unit_amount: Units, float, readonly

:unit_amount: Units, float, readonly

.. i18n: :sale_price: Sale price, float, readonly

:sale_price: Sale price, float, readonly

.. i18n: :name: Month, date, readonly

:name: Month, date, readonly
