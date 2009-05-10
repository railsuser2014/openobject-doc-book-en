
.. module:: c2c_analytic_wizard
    :synopsis: Analytic wizard and tools for services companies 
    :noindex:
.. 

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

Analytic wizard and tools for services companies (*c2c_analytic_wizard*)
========================================================================
:Module: c2c_analytic_wizard
:Name: Analytic wizard and tools for services companies
:Version: 1.2
:Author: Camptocamp
:Directory: c2c_analytic_wizard
:Web: http://www.camptocamp.com
:Official module: no
:Quality certified: no

Description
-----------

::

  
  Add wizard to manage analytic account and invoicing :
   - Associate Analytic Lines to invoice (from an invoice or from analytic line directly)
   - Dissociate Analytic Lines from an invoice
   - Create blank invoice from Analytic Account (with all informations completed)
   - Create invoice from Analytic Lines
   - Get all invoice from Analytic Account (with recurssion in child account)
   - Get Analytic Lines from Analytic Account (with recurssion in child account)
   - Get Analytic Lines from an invoice for controlling
  Add report for on analytic account showing the indicators et open invoice.
  
  -----------------------------------------------------------------------------------------------
  
  Ce module comprend un set de wizard pour faciliter la gestion des entreprises de service travaillant avec les comptes analytiques,
  par exemple pour la gestion de projet. Il apporte une réelle plus-value en terme d'ergonomie. Ces wizards améliorent la facturation du travail
  effectué depuis un projet (compte analytique), permettent d'associer / dissocier des lignes analytiques d'une facture ou encore d'obtenir 
  la liste des factures relatives à un projet.
  Ajoute egalement un rapport affichant le détails d'un compte analytique et ses factures ouvertes
  	

Dependencies
------------

 * :mod:`base`
 * :mod:`account`
 * :mod:`product`
 * :mod:`account_analytic_analysis`
 * :mod:`c2c_reporting_tools`
 * :mod:`hr_timesheet_invoice`
 * :mod:`account_tax_include`

Reports
-------

None


Menus
-------


None


Views
-----


None



Objects
-------

None
