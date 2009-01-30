
.. module:: base_module_record
    :synopsis: Module Recorder
    :noindex:
.. 

Module Recorder (*base_module_record*)
======================================
:Module: base_module_record
:Name: Module Recorder
:Version: 5.0.1.0
:Directory: base_module_record
:Web: http://www.openerp.com
:Is certified: yes

Description
-----------

::

  This module allows you to create a new module without any development.
  It records all operations on objects during the recording session and
  produce a .ZIP module. So you can create your own module directly from
  the Open ERP client.
  
  This version works for creating and updating existing records. It recomputes
  dependencies and links for all types of widgets (many2one, many2many, ...).
  It also support workflows and demo/update data.
  
  This should help you to easily create reusable and publishable modules
  for custom configurations and demo/testing data.
  
  How to use it:
  1. Start the recording
  2. Do stuff in your Open ERP client
  3. Stop the recording session
  4. Export to a reusable module

Dependencies
------------

 * base - installed

Reports
-------

None


Menus
-------

 * Administration/Customization/Module Creation
 * Administration/Customization/Module Creation/Module Recorder
 * Administration/Customization/Module Creation/Module Recorder/Start Recording
 * Administration/Customization/Module Creation/Module Recorder/Stop Recording
 * Administration/Customization/Module Creation/Module Recorder/Save Recorded Module
 * Administration/Customization/Module Creation/Export Customizations As a Module

Views
-----


None



Objects
-------

Object: ir.module.record (ir.module.record)
###########################################
