
Module Reporting of Balancesheet for accounting (*account_reporting*)
=====================================================================
:Module: account_reporting
:Name: Reporting of Balancesheet for accounting
:Version: 5.0.1.0
:Directory: account_reporting
:Web: 

Description
-----------

::

  Financial and accounting reporting
      Balance Sheet Report

Dependencies
------------

 * account - installed

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

Object: Rml Colors
##################

.. index::
  single: Rml Colors object
.. 


:code: code, char, required



.. index::
  single: code field
.. 




:name: Name, char, required



.. index::
  single: name field
.. 



Object: Account reporting for Balance Sheet
###########################################

.. index::
  single: Account reporting for Balance Sheet object
.. 


:font_style: Font, selection



.. index::
  single: font_style field
.. 




:name: Name, char, required



.. index::
  single: name field
.. 




:sequence: Sequence, integer



.. index::
  single: sequence field
.. 




:note: Note, text



.. index::
  single: note field
.. 




:parent_id: Parent, many2one



.. index::
  single: parent_id field
.. 




:code: Code, char, required



.. index::
  single: code field
.. 




:report_type: Report Type, selection



.. index::
  single: report_type field
.. 




:child_id: Childs, one2many



.. index::
  single: child_id field
.. 




:color_back: Back Color, many2one



.. index::
  single: color_back field
.. 




:color_font: Font Color, many2one



.. index::
  single: color_font field
.. 




:account_id: Accounts, many2many



.. index::
  single: account_id field
.. 

