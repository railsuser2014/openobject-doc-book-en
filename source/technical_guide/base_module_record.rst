
Module Module Recorder (*base_module_record*)
=============================================
:Module: base_module_record
:Name: Module Recorder
:Version: False
:Directory: base_module_record
:Web: http://www.openerp.com

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
      

Reports
-------

Menus
-------

Views
-----

Dependencies
------------

 * base - installed

Objects
-------