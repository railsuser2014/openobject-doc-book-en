
Module Production Report (*mrp_production_report*)
==================================================
:Module: mrp_production_report
:Name: Production Report
:Version: 5.0.1.0
:Directory: mrp_production_report
:Web: 

Description
-----------

::

  On this module,
      ** Add partner on procurement form which set when Sale order confirm.
      ** Add link between production and procument.
      ** New report for production.

Dependencies
------------

 * base - installed
 * mrp - installed
 * sale - installed

Reports
-------

 * Production Order

Menus
-------


None


Views
-----

 * \* INHERIT mrp.production.form.inherit (form)
 * \* INHERIT mrp.production.form.inherit (form)
 * \* INHERIT mrp.procurement.form.inherit (form)


Objects
-------

None
