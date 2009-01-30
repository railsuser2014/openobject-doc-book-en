
.. module:: base_report_creator
    :synopsis: Report Creator
    :noindex:
.. 

Report Creator (*base_report_creator*)
======================================
:Module: base_report_creator
:Name: Report Creator
:Version: 5.0.1.0
:Directory: base_report_creator
:Web: 

Description
-----------

::

  This modules allows you to create any statistic
  report on several object. It's a SQL query builder and browser
  for and users.
  
  After installing the module, it adds a menu to define custom report in
  the "Dashboard" menu.

Dependencies
------------

 * base - installed
 * board - installed

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


