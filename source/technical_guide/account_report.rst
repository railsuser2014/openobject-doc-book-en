
Module Reporting for accounting (*account_report*)
==================================================
:Module: account_report
:Name: Reporting for accounting
:Version: 5.0.1.0
:Directory: account_report
:Web: http://www.openerp.com

Description
-----------

::

  Financial and accounting reporting
      Fiscal statements
      Indicators

Dependencies
------------

 * account - installed

Reports
-------

 * Fiscal Statements

 * Indicators

 * Print Indicators in PDF

Menus
-------

 * Financial Management/Configuration/Custom reporting
 * Financial Management/Configuration/Custom reporting/New Reporting Item Formula
 * Financial Management/Reporting/Custom reporting
 * Financial Management/Reporting/Custom reporting/Fiscal Statements reporting
 * Financial Management/Reporting/Custom reporting/Indicators reporting
 * Financial Management/Reporting/Custom reporting/Others reportings
 * Financial Management/Reporting/All Indicators History
 * Financial Management/Reporting/Custom reporting/Print Indicators

Views
-----

 * account.report.report.form (form)
 * account.report.report.tree.simple (tree)
 * account.report.report.tree (tree)
 * account.report.history1 (tree)
 * account.report.history2 (form)
 * account.report.history3 (graph)


Objects
-------

Object: Account reporting
#########################

.. index::
  single: Account reporting object
.. 


:status: Status, selection, readonly



.. index::
  single: status field
.. 




:note: Note, text



.. index::
  single: note field
.. 




:disp_tree: Display Tree, boolean

    *When the indicators will be printed, if one indicator is set with this field to True, then it will display one more graph with all its children in tree*

.. index::
  single: disp_tree field
.. 




:code: Code, char, required



.. index::
  single: code field
.. 




:name: Name, char, required



.. index::
  single: name field
.. 




:sequence: Sequence, integer



.. index::
  single: sequence field
.. 




:type: Type, selection, required



.. index::
  single: type field
.. 




:child_ids: Childs, one2many



.. index::
  single: child_ids field
.. 




:badness_limit: Badness Indicator Limit, float

    *This Value depicts the limit of badness.*

.. index::
  single: badness_limit field
.. 




:goodness_limit: Goodness Indicator Limit, float

    *This Value depicts the limit of goodness.*

.. index::
  single: goodness_limit field
.. 




:parent_id: Parent, many2one



.. index::
  single: parent_id field
.. 




:amount: Value, float, readonly



.. index::
  single: amount field
.. 




:disp_graph: Display as a Graph, boolean

    *If the field is set to True,information will be printed as a Graph; as an array otherwise.*

.. index::
  single: disp_graph field
.. 




:active: Active, boolean



.. index::
  single: active field
.. 




:expression: Expression, char, required



.. index::
  single: expression field
.. 



Object: Indicator
#################

.. index::
  single: Indicator object
.. 


:tmp: temp, integer, readonly



.. index::
  single: tmp field
.. 




:fiscalyear_id: Fiscal Year, many2one, readonly



.. index::
  single: fiscalyear_id field
.. 




:period_id: Period, many2one, readonly



.. index::
  single: period_id field
.. 




:name: Indicator, many2one, readonly



.. index::
  single: name field
.. 




:val: Value, float, readonly



.. index::
  single: val field
.. 

