
.. module:: account_report
    :synopsis: Reporting for accounting
    :noindex:
.. 

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

Reporting for accounting (*account_report*)
===========================================
:Module: account_report
:Name: Reporting for accounting
:Version: 5.0.1.0
:Directory: account_report
:Web: http://www.openerp.com
:Is certified: yes

Description
-----------

::

  Financial and accounting reporting
      Fiscal statements
      Indicators

Dependencies
------------

 * :mod:`account`

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

Object: Account reporting (account.report.report)
#################################################



:status: Status, selection, readonly





:note: Note, text





:disp_tree: Display Tree, boolean

    *When the indicators will be printed, if one indicator is set with this field to True, then it will display one more graph with all its children in tree*



:code: Code, char, required





:name: Name, char, required





:sequence: Sequence, integer





:type: Type, selection, required





:child_ids: Childs, one2many





:badness_limit: Badness Indicator Limit, float

    *This Value depicts the limit of badness.*



:goodness_limit: Goodness Indicator Limit, float

    *This Value depicts the limit of goodness.*



:parent_id: Parent, many2one





:amount: Value, float, readonly





:disp_graph: Display as a Graph, boolean

    *If the field is set to True,information will be printed as a Graph; as an array otherwise.*



:active: Active, boolean





:expression: Expression, char, required




Object: Indicator (account.report.history)
##########################################



:tmp: temp, integer, readonly





:fiscalyear_id: Fiscal Year, many2one, readonly





:period_id: Period, many2one, readonly





:name: Indicator, many2one, readonly





:val: Value, float, readonly


