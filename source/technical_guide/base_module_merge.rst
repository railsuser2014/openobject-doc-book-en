
Module Module Merger (*base_module_merge*)
==========================================
:Module: base_module_merge
:Name: Module Merger
:Version: False
:Directory: base_module_merge
:Web: http://www.openerp.com

Description
-----------

::
  
    
      * The wizard asks a many2many of modules
      * And then generate a module which is the merge of all selected modules
      * The new module is provided as a .zip file
  
      The merge will works in all situations:
      * Merging all .py files with the same name in the new module
      * merging all .xml files and take care of id's.
      

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