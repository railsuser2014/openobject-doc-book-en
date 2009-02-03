
.. module:: portal_service
    :synopsis: Portal Management - Service 
    :noindex:
.. 

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

    <style>
      div.body p#module-portal_service {
        display: none;
      }
    </style>

Portal Management - Service (*portal_service*)
==============================================
:Module: portal_service
:Name: Portal Management - Service
:Version: 5.0.0.1
:Author: Tiny
:Directory: portal_service
:Web: http://tinyerp.com/
:Is certified: no

Description
-----------

::

  Potal Management - Service company specific data.

Dependencies
------------

 * :mod:`base`
 * :mod:`portal`
 * :mod:`project`
 * :mod:`crm`
 * :mod:`account_analytic_analysis`
 * :mod:`hr_timesheet_invoice`
 * :mod:`scrum`

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
