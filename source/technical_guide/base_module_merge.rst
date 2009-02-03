
.. module:: base_module_merge
    :synopsis: Module Merger 
    :noindex:
.. 

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

    <style>
      div.body p#module-base_module_merge {
        display: none;
      }
    </style>

Module Merger (*base_module_merge*)
===================================
:Module: base_module_merge
:Name: Module Merger
:Version: 5.0.1.0
:Author: Tiny
:Directory: base_module_merge
:Web: http://tinyerp.com
:Is certified: no

Description
-----------

::

  * The wizard asks a many2many of modules
      * And then generate a module which is the merge of all selected modules
      * The new module is provided as a .zip file
  
      The merge will works in all situations:
      * Merging all .py files with the same name in the new module
      * merging all .xml files and take care of id's.

Dependencies
------------

 * :mod:`base`

Reports
-------

None


Menus
-------

 * Administration/Modules Management/Merge module

Views
-----


None



Objects
-------

None
