
.. module:: base_report_creator
    :synopsis: Report Creator (Official, Quality Certified)
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="base_report_creator"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Report Creator (*base_report_creator*)
======================================
:Module: base_report_creator
:Name: Report Creator
:Version: 5.0.1.0
:Author: Tiny & Axelor
:Directory: base_report_creator
:Web: 
:Official module: yes
:Quality certified: yes

Description
-----------

::

  This modules allows you to create any statistic
  report on several object. It's a SQL query builder and browser
  for and users.
  
  After installing the module, it adds a menu to define custom report in
  the "Dashboard" menu.

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 </download/modules/5.0/base_report_creator.zip>`_
  * `trunk </download/modules/trunk/base_report_creator.zip>`_


Dependencies
------------

 * :mod:`base`
 * :mod:`board`

Reports
-------

None


Menus
-------

 * Dashboards/Configuration/Custom Reports
 * Dashboards/Custom Reports

Views
-----

 * base_report_creator.report.tree (tree)
 * base_report_creator.report.form (form)
 * base_report_creator.report.simple.tree (tree)


Objects
-------

Object: Report (base_report_creator.report)
###########################################



:model_ids: Reported Objects, many2many





:filter_ids: Filters, one2many





:name: Report Name, char, required





:sql_query: SQL Query, text, readonly





:view_graph_type: Graph Type, selection, required





:state: Status, selection, required





:view_type1: First View, selection, required





:view_type2: Second View, selection





:view_type3: Third View, selection





:field_ids: Fields to Display, one2many





:active: Active, boolean





:group_ids: Authorized Groups, many2many





:type: Report Type, selection, required





:view_graph_orientation: Graph Orientation, selection, required




Object: Display Fields (base_report_creator.report.fields)
##########################################################



:calendar_mode: Calendar Mode, selection





:group_method: Grouping Method, selection, required





:sequence: Sequence, integer





:field_id: Field, many2one





:graph_mode: Graph Mode, selection





:report_id: Report, many2one




Object: Report Filters (base_report_creator.report.filter)
##########################################################



:expression: Value, text, required





:name: Filter Name, char, required





:condition: Condition, selection





:report_id: Report, many2one


