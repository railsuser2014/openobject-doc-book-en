
Module France - Plan Comptable Général (*l10n_fr_pcg*)
======================================================
:Module: l10n_fr_pcg
:Name: France - Plan Comptable Général
:Version: 5.0.1.0
:Directory: l10n_fr_pcg
:Web: http://www.crysalead.com

Description
-----------

::

  This is the module to manage the accounting chart for France in Open ERP.
  
  Credits: Sistheo Zeekom CrysaLEAD

Dependencies
------------

 * base - installed
 * account - installed
 * account_chart - installed
 * base_vat - installed

Reports
-------

 * Compte de resultat

 * Bilan

Menus
-------


None


Views
-----


None



Objects
-------

Object: Report for l10n_fr
##########################

.. index::
  single: Report for l10n_fr object
.. 


:line_ids: Lines, one2many



.. index::
  single: line_ids field
.. 




:code: Code, char



.. index::
  single: code field
.. 




:name: Name, char



.. index::
  single: name field
.. 



Object: Report Lines for l10n_fr
################################

.. index::
  single: Report Lines for l10n_fr object
.. 


:definition: Definition, char



.. index::
  single: definition field
.. 




:code: Variable Name, char



.. index::
  single: code field
.. 




:name: Name, char



.. index::
  single: name field
.. 




:report_id: Report, many2one



.. index::
  single: report_id field
.. 

