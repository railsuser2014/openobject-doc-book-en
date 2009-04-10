
.. i18n: .. module:: base_module_record
.. i18n:     :synopsis: Module Recorder (Official, Quality Certified)
.. i18n:     :noindex:
.. i18n: .. 

.. module:: base_module_record
    :synopsis: Module Recorder (Official, Quality Certified)
    :noindex:
.. 

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. i18n: Module Recorder (*base_module_record*)
.. i18n: ======================================
.. i18n: :Module: base_module_record
.. i18n: :Name: Module Recorder
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: base_module_record
.. i18n: :Web: http://www.openerp.com
.. i18n: :Official module: yes
.. i18n: :Quality certified: yes

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

.. i18n: Description
.. i18n: -----------

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   This module allows you to create a new module without any development.
.. i18n:   It records all operations on objects during the recording session and produce a .ZIP module. 
.. i18n:   So you can create your own module directly from the Open ERP client.
.. i18n:   
.. i18n:   This version works for creating and updating existing records. It recomputes
.. i18n:   dependencies and links for all types of widgets (many2one, many2many, ...).
.. i18n:   It also support workflows and demo/update data.
.. i18n:   
.. i18n:   This should help you to easily create reusable and publishable modules for custom configurations and 
.. i18n:   demo/testing data.
.. i18n:   
.. i18n:   How to use it:
.. i18n:   1. Start the recording
.. i18n:   2. Do stuff in your Open ERP client
.. i18n:   3. Stop the recording session
.. i18n:   4. Export to a reusable module

::

  This module allows you to create a new module without any development.
  It records all operations on objects during the recording session and produce a .ZIP module. 
  So you can create your own module directly from the Open ERP client.
  
  This version works for creating and updating existing records. It recomputes
  dependencies and links for all types of widgets (many2one, many2many, ...).
  It also support workflows and demo/update data.
  
  This should help you to easily create reusable and publishable modules for custom configurations and 
  demo/testing data.
  
  How to use it:
  1. Start the recording
  2. Do stuff in your Open ERP client
  3. Stop the recording session
  4. Export to a reusable module

.. i18n: Dependencies
.. i18n: ------------

Dependencies
------------

.. i18n:  * :mod:`base`

 * :mod:`base`

.. i18n: Reports
.. i18n: -------

Reports
-------

.. i18n: None

None

.. i18n: Menus
.. i18n: -------

Menus
-------

.. i18n:  * Administration/Customization/Module Creation
.. i18n:  * Administration/Customization/Module Creation/Module Recorder
.. i18n:  * Administration/Customization/Module Creation/Module Recorder/Start Recording
.. i18n:  * Administration/Customization/Module Creation/Module Recorder/Stop Recording
.. i18n:  * Administration/Customization/Module Creation/Module Recorder/Save Recorded Module
.. i18n:  * Administration/Customization/Module Creation/Export Customizations As a Module

 * Administration/Customization/Module Creation
 * Administration/Customization/Module Creation/Module Recorder
 * Administration/Customization/Module Creation/Module Recorder/Start Recording
 * Administration/Customization/Module Creation/Module Recorder/Stop Recording
 * Administration/Customization/Module Creation/Module Recorder/Save Recorded Module
 * Administration/Customization/Module Creation/Export Customizations As a Module

.. i18n: Views
.. i18n: -----

Views
-----

.. i18n: None

None

.. i18n: Objects
.. i18n: -------

Objects
-------

.. i18n: Object: ir.module.record (ir.module.record)
.. i18n: ###########################################

Object: ir.module.record (ir.module.record)
###########################################
