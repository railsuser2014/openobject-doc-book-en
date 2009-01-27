
Module Report Creator (*base_report_creator*)
=============================================
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

Object: Report
##############

.. index::
  single: Report object
.. 


:model_ids: Reported Objects, many2many



.. index::
  single: model_ids field
.. 




:filter_ids: Filters, one2many



.. index::
  single: filter_ids field
.. 




:name: Report Name, char, required



.. index::
  single: name field
.. 




:sql_query: SQL Query, text, readonly



.. index::
  single: sql_query field
.. 




:view_graph_type: Graph Type, selection, required



.. index::
  single: view_graph_type field
.. 




:state: Status, selection, required



.. index::
  single: state field
.. 




:view_type1: First View, selection, required



.. index::
  single: view_type1 field
.. 




:view_type2: Second View, selection



.. index::
  single: view_type2 field
.. 




:view_type3: Third View, selection



.. index::
  single: view_type3 field
.. 




:field_ids: Fields to Display, one2many



.. index::
  single: field_ids field
.. 




:active: Active, boolean



.. index::
  single: active field
.. 




:group_ids: Authorized Groups, many2many



.. index::
  single: group_ids field
.. 




:type: Report Type, selection, required



.. index::
  single: type field
.. 




:view_graph_orientation: Graph Orientation, selection, required



.. index::
  single: view_graph_orientation field
.. 



Object: Display Fields
######################

.. index::
  single: Display Fields object
.. 


:calendar_mode: Calendar Mode, selection



.. index::
  single: calendar_mode field
.. 




:group_method: Grouping Method, selection, required



.. index::
  single: group_method field
.. 




:sequence: Sequence, integer



.. index::
  single: sequence field
.. 




:field_id: Field, many2one



.. index::
  single: field_id field
.. 




:graph_mode: Graph Mode, selection



.. index::
  single: graph_mode field
.. 




:report_id: Report, many2one



.. index::
  single: report_id field
.. 



Object: Report Filters
######################

.. index::
  single: Report Filters object
.. 


:expression: Value, text, required



.. index::
  single: expression field
.. 




:name: Filter Name, char, required



.. index::
  single: name field
.. 




:condition: Condition, selection



.. index::
  single: condition field
.. 




:report_id: Report, many2one



.. index::
  single: report_id field
.. 

