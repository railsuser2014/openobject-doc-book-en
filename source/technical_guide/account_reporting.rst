
.. module:: account_reporting
    :synopsis: Reporting of Balancesheet for accounting (Official, Quality Certified)
    :noindex:
.. 

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

Reporting of Balancesheet for accounting (*account_reporting*)
==============================================================
:Module: account_reporting
:Name: Reporting of Balancesheet for accounting
:Version: 5.0.1.0
:Author: Tiny
:Directory: account_reporting
:Web: 
:Official module: yes
:Quality certified: yes

Description
-----------

::

  Financial and accounting reporting
      Balance Sheet Report

Dependencies
------------

 * :mod:`account`

Reports
-------

None


Menus
-------

 * Financial Management/Configuration/Balance Sheet Report
 * Financial Management/Configuration/Balance Sheet Report/Balance Sheet Report
 * Financial Management/Configuration/Balance Sheet Report/Balance Sheet Report Form

Views
-----

 * account.report.bs.form (form)
 * account.report.report.tree.bs (tree)


Objects
-------

Object: Rml Colors (color.rml)
##############################



:code: code, char, required





:name: Name, char, required




Object: Account reporting for Balance Sheet (account.report.bs)
###############################################################



:font_style: Font, selection





:name: Name, char, required





:sequence: Sequence, integer





:note: Note, text





:parent_id: Parent, many2one





:code: Code, char, required





:report_type: Report Type, selection





:child_id: Childs, one2many





:color_back: Back Color, many2one





:color_font: Font Color, many2one





:account_id: Accounts, many2many


