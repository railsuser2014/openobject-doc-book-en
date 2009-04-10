
.. i18n: .. module:: report_analytic_planning_long_term
.. i18n:     :synopsis: report_analytic_planning_long_term 
.. i18n:     :noindex:
.. i18n: .. 

.. module:: report_analytic_planning_long_term
    :synopsis: report_analytic_planning_long_term 
    :noindex:
.. 

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. i18n: report_analytic_planning_long_term (*report_analytic_planning_long_term*)
.. i18n: =========================================================================
.. i18n: :Module: report_analytic_planning_long_term
.. i18n: :Name: report_analytic_planning_long_term
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: report_analytic_planning_long_term
.. i18n: :Web: http://www.openerp.com//
.. i18n: :Official module: no
.. i18n: :Quality certified: no

report_analytic_planning_long_term (*report_analytic_planning_long_term*)
=========================================================================
:Module: report_analytic_planning_long_term
:Name: report_analytic_planning_long_term
:Version: 5.0.1.0
:Author: Tiny
:Directory: report_analytic_planning_long_term
:Web: http://www.openerp.com//
:Official module: no
:Quality certified: no

.. i18n: Description
.. i18n: -----------

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   This modules is an improvement of the basic planning module and offers additional functionalities 
.. i18n:   for long term planning, such as:
.. i18n:           - planning of the functions that will be needed
.. i18n:           - additional data for planned resources: the start and end dates

::

  This modules is an improvement of the basic planning module and offers additional functionalities 
  for long term planning, such as:
          - planning of the functions that will be needed
          - additional data for planned resources: the start and end dates

.. i18n: Dependencies
.. i18n: ------------

Dependencies
------------

.. i18n:  * :mod:`report_analytic_planning`

 * :mod:`report_analytic_planning`

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

.. i18n: None

None

.. i18n: Views
.. i18n: -----

Views
-----

.. i18n:  * \* INHERIT report.account.analytic.planning.form.inherit_longterm_1 (form)
.. i18n:  * \* INHERIT report.account.analytic.planning.form.inherit_longterm_2 (form)
.. i18n:  * \* INHERIT report.account.analytic.planning.form.inherit_longterm_3 (form)
.. i18n:  * \* INHERIT report.account.analytic.planning.form.inherit_longterm_4 (form)

 * \* INHERIT report.account.analytic.planning.form.inherit_longterm_1 (form)
 * \* INHERIT report.account.analytic.planning.form.inherit_longterm_2 (form)
 * \* INHERIT report.account.analytic.planning.form.inherit_longterm_3 (form)
 * \* INHERIT report.account.analytic.planning.form.inherit_longterm_4 (form)

.. i18n: Objects
.. i18n: -------

Objects
-------

.. i18n: Object: Planning product stat (report_account_analytic.planning.stat.product)
.. i18n: #############################################################################

Object: Planning product stat (report_account_analytic.planning.stat.product)
#############################################################################

.. i18n: :sum_amount_real: Timesheet, float, readonly

:sum_amount_real: Timesheet, float, readonly

.. i18n: :product_id: Post / Product, many2one, required

:product_id: Post / Product, many2one, required

.. i18n: :planning_id: Planning, many2one, required

:planning_id: Planning, many2one, required

.. i18n: :quantity: Planned, float, required

:quantity: Planned, float, required
