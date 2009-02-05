
.. module:: report_intrastat
    :synopsis: Intrastat Reporting - Reporting
    :noindex:
.. 

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

Intrastat Reporting - Reporting (*report_intrastat*)
====================================================
:Module: report_intrastat
:Name: Intrastat Reporting - Reporting
:Version: 5.0.1.0
:Directory: report_intrastat
:Web: http://www.openerp.com
:Is certified: yes

Description
-----------

::

  A module that adds intrastat reports.

Dependencies
------------

 * :mod:`base`
 * :mod:`product`
 * :mod:`stock`
 * :mod:`sale`
 * :mod:`purchase`

Reports
-------

 * Invoice Intrastat

Menus
-------

 * Books/Configuration/Intrastat Code
 * Stock Management/Reporting/This Month
 * Stock Management/Reporting/This Month/Intrastat (this month)
 * Stock Management/Reporting/All Months
 * Stock Management/Reporting/All Months/Intrastat

Views
-----

 * \* INHERIT res.country.tree (form)
 * \* INHERIT res.country.form (form)
 * \* INHERIT product.normal.form (form)
 * report.intrastat.code.tree (tree)
 * report.intrastat.code.form (form)
 * report.intrastat.view (tree)


Objects
-------

Object: Intrastat code (report.intrastat.code)
##############################################



:name: Intrastat Code, char





:description: Description, char




Object: Intrastat report (report.intrastat)
###########################################



:code: Country code, char, readonly





:name: Month, date, readonly





:weight: Weight, float, readonly





:value: Value, float, readonly





:currency_id: Currency, many2one, readonly





:intrastat_id: Intrastat code, many2one, readonly





:type: Type, selection


