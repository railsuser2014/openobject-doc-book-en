
Portal Management - Service (*portal_service*)
==============================================
:Module: portal_service
:Name: Portal Management - Service
:Version: 5.0.0.1
:Directory: portal_service
:Web: http://tinyerp.com/

Description
-----------

::

  Potal Management - Service company specific data.

Dependencies
------------

 * base - installed
 * portal - installed
 * project - installed
 * crm - installed
 * account_analytic_analysis - installed
 * hr_timesheet_invoice - installed
 * scrum - installed

Reports
-------

None


Menus
-------

 * Portal/Customer Portal/Your Projects
 * Portal/Customer Portal/Your Projects/Your Projects
 * Portal/Customer Portal/Support
 * Portal/Customer Portal/Support/All Support Cases
 * Portal/Customer Portal/Support/All Support Cases/Opened Cases
 * Portal/Customer Portal/Support/All Support Cases/Closed Cases

Views
-----

 * crm.case.section.tree (tree)
 * \* INHERIT Available Cases List (tree)
 * \* INHERIT Available Case (form)
 * \* INHERIT scrum.project.form (form)


Objects
-------

None
