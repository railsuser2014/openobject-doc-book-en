
Module MRP Management - Reporting (*report_mrp*)
================================================
:Module: report_mrp
:Name: MRP Management - Reporting
:Version: 5.0.1.0
:Directory: report_mrp
:Web: http://www.openerp.com

Description
-----------

::

  A module that adds new reports based on MRP cases.
      Workcenter loads, Weekly Stock value variation

Dependencies
------------

 * mrp - installed

Reports
-------

None


Menus
-------

 * Manufacturing/Reporting
 * Manufacturing/Reporting/Workcenter Loads
 * Manufacturing/Reporting/Weekly Stock Value Variation

Views
-----

 * report.workcenter.load.tree (tree)
 * report.workcenter.load.graph (graph)
 * report.workcenter.load.form (form)
 * report.mrp.inout.tree (tree)
 * report.mrp.inout.form (form)
 * report.mrp.inout.graph (graph)


Objects
-------

Object: Workcenter Load
#######################

.. index::
  single: Workcenter Load object
.. 


:workcenter_id: Workcenter, many2one, required



.. index::
  single: workcenter_id field
.. 




:name: Week, char, required



.. index::
  single: name field
.. 




:hour: Nbr of hour, float



.. index::
  single: hour field
.. 




:cycle: Nbr of cycle, float



.. index::
  single: cycle field
.. 



Object: Stock value variation
#############################

.. index::
  single: Stock value variation object
.. 


:date: Week, char, required



.. index::
  single: date field
.. 




:value: Stock value, float, required



.. index::
  single: value field
.. 

