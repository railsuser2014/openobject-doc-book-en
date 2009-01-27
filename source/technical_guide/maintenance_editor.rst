
Module Base (*maintenance_editor*)
==================================
:Module: maintenance_editor
:Name: Base
:Version: 5.0.1.0
:Directory: maintenance_editor
:Web: 

Description
-----------

::

  module to manage maintenance contracts:

Dependencies
------------

 * base - installed

Reports
-------

None


Menus
-------

 * Administration/Modules Management/Maintenance Editor
 * Administration/Modules Management/Maintenance Editor/Maintenance Configuration
 * Administration/Modules Management/Maintenance Editor/Maintenance Modules

Views
-----

 * maintenance.maintenance.tree (tree)
 * maintenance.maintenance.form (form)
 * maintenance.maintenance.module.tree (tree)
 * maintenance.maintenance.module.form (form)


Objects
-------

Object: maintenance modules
###########################



:version: Version, char





:name: Name, char, required




Object: maintenance
###################



:name: Contract ID, char, required





:module_ids: Modules, many2many





:date_from: Date From, date, required





:state: State, selection, readonly





:date_to: Date To, date, required





:partner_invoice_id: Address, many2one





:password: Password, char, required





:partner_id: Partner, many2one, required


