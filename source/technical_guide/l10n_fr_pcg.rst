
.. module:: l10n_fr_pcg
    :synopsis: France - Plan Comptable Général 
    :noindex:
.. 

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

    <style>
      div.body p#module-l10n_fr_pcg {
        display: none;
      }
    </style>

France - Plan Comptable Général (*l10n_fr_pcg*)
===============================================
:Module: l10n_fr_pcg
:Name: France - Plan Comptable Général
:Version: 5.0.1.0
:Author: Simon JAILLET - CrysaLEAD
:Directory: l10n_fr_pcg
:Web: http://www.crysalead.com
:Is certified: no

Description
-----------

::

  This is the module to manage the accounting chart for France in Open ERP.
  
  Credits: Sistheo Zeekom CrysaLEAD

Dependencies
------------

 * :mod:`base`
 * :mod:`account`
 * :mod:`account_chart`
 * :mod:`base_vat`

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

Object: Report for l10n_fr (l10n.fr.report)
###########################################



:line_ids: Lines, one2many





:code: Code, char





:name: Name, char




Object: Report Lines for l10n_fr (l10n.fr.line)
###############################################



:definition: Definition, char





:code: Variable Name, char





:name: Name, char





:report_id: Report, many2one


