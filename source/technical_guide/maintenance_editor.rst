
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

.. index::
  single: maintenance modules object
.. 


:version: Version, char



.. index::
  single: version field
.. 




:name: Name, char, required



.. index::
  single: name field
.. 



Object: maintenance
###################

.. index::
  single: maintenance object
.. 


:name: Contract ID, char, required



.. index::
  single: name field
.. 




:module_ids: Modules, many2many



.. index::
  single: module_ids field
.. 




:date_from: Date From, date, required



.. index::
  single: date_from field
.. 




:state: State, selection, readonly



.. index::
  single: state field
.. 




:date_to: Date To, date, required



.. index::
  single: date_to field
.. 




:partner_invoice_id: Address, many2one



.. index::
  single: partner_invoice_id field
.. 




:password: Password, char, required



.. index::
  single: password field
.. 




:partner_id: Partner, many2one, required



.. index::
  single: partner_id field
.. 

