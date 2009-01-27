
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



:workcenter_id: Workcenter, many2one, required





:name: Week, char, required





:hour: Nbr of hour, float





:cycle: Nbr of cycle, float




Object: Stock value variation
#############################



:date: Week, char, required





:value: Stock value, float, required


