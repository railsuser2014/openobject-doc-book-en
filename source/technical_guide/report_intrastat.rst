
.. module:: report_intrastat
    :synopsis: Intrastat Reporting - Reporting (Official, Quality Certified)
    :noindex:
.. 

.. raw:: html

      <br />
    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. tip:: This module is part of the Open ERP software, the leading Open Source 
  enterprise management system. If you want to discover Open ERP, check our 
  `screencasts <href="http://openerp.tv>`_ or download 
  `Open ERP <href="http://openerp.com>`_ directly.

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/report_intrastat"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Intrastat Reporting - Reporting (*report_intrastat*)
====================================================
:Module: report_intrastat
:Name: Intrastat Reporting - Reporting
:Version: 5.0.1.0
:Author: Tiny
:Directory: report_intrastat
:Web: http://www.openerp.com
:Official module: yes
:Quality certified: yes

Description
-----------

::

  A module that adds intrastat reports.

Download links
--------------

You can download this module as a zip file in the following version:

  * `4.2 </download/modules/4.2/report_intrastat.zip>`_
  * `5.0 </download/modules/5.0/report_intrastat.zip>`_
  * `trunk </download/modules/trunk/report_intrastat.zip>`_


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

 * Products/Configuration/Intrastat Code
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


