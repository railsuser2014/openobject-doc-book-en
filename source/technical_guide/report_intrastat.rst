
Module Intrastat Reporting - Reporting (*report_intrastat*)
===========================================================
:Module: report_intrastat
:Name: Intrastat Reporting - Reporting
:Version: 5.0.1.0
:Directory: report_intrastat
:Web: http://www.openerp.com

Description
-----------

::

  A module that adds intrastat reports.

Dependencies
------------

 * base - installed
 * product - installed
 * stock - installed
 * sale - installed
 * purchase - installed

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

Object: Intrastat code
######################

.. index::
  single: Intrastat code object
.. 


:name: Intrastat Code, char



.. index::
  single: name field
.. 




:description: Description, char



.. index::
  single: description field
.. 



Object: Intrastat report
########################

.. index::
  single: Intrastat report object
.. 


:code: Country code, char, readonly



.. index::
  single: code field
.. 




:name: Month, date, readonly



.. index::
  single: name field
.. 




:weight: Weight, float, readonly



.. index::
  single: weight field
.. 




:value: Value, float, readonly



.. index::
  single: value field
.. 




:currency_id: Currency, many2one, readonly



.. index::
  single: currency_id field
.. 




:intrastat_id: Intrastat code, many2one, readonly



.. index::
  single: intrastat_id field
.. 




:type: Type, selection



.. index::
  single: type field
.. 

