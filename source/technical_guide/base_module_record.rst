
.. module:: base_module_record
    :synopsis: Module Recorder (Official, Quality Certified)
    :noindex:
.. 

.. tip:: This module is part of the Open ERP software, the leading Open Source 
  enterprise management system. If you want to discover Open ERP, check our 
  `screencasts <href="http://openerp.tv>`_ or download 
  `Open ERP <href="http://openerp.com>`_ directly.

.. raw:: html

      <br />
    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

Module Recorder (*base_module_record*)
======================================
:Module: base_module_record
:Name: Module Recorder
:Version: 5.0.1.0
:Author: Tiny
:Directory: base_module_record
:Web: http://www.openerp.com
:Official module: yes
:Quality certified: yes

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

Download links
--------------

You can download this module as a zip file in the following version:

  * `4.2 </download/modules/4.2/base_module_record.zip>`_
  * `5.0 </download/modules/5.0/base_module_record.zip>`_
  * `trunk </download/modules/trunk/base_module_record.zip>`_


Dependencies
------------

 * :mod:`base`

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
