
France - Plan Comptable Général (*l10n_fr_pcg*)
===============================================
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



:line_ids: Lines, one2many





:code: Code, char





:name: Name, char




Object: Report Lines for l10n_fr
################################



:definition: Definition, char





:code: Variable Name, char





:name: Name, char





:report_id: Report, many2one


