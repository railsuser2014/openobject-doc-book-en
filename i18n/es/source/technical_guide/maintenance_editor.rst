
.. i18n: .. module:: maintenance_editor
.. i18n:     :synopsis: Base 
.. i18n:     :noindex:
.. i18n: .. 

.. module:: maintenance_editor
    :synopsis: Base 
    :noindex:
.. 

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. i18n: Base (*maintenance_editor*)
.. i18n: ===========================
.. i18n: :Module: maintenance_editor
.. i18n: :Name: Base
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: maintenance_editor
.. i18n: :Web: 
.. i18n: :Official module: no
.. i18n: :Quality certified: no

Base (*maintenance_editor*)
===========================
:Module: maintenance_editor
:Name: Base
:Version: 5.0.1.0
:Author: Tiny
:Directory: maintenance_editor
:Web: 
:Official module: no
:Quality certified: no

.. i18n: Description
.. i18n: -----------

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   module to manage maintenance contracts:

::

  module to manage maintenance contracts:

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

.. i18n:  * Administration/Modules Management/Maintenance Editor
.. i18n:  * Administration/Modules Management/Maintenance Editor/Maintenance Configuration
.. i18n:  * Administration/Modules Management/Maintenance Editor/Maintenance Modules

 * Administration/Modules Management/Maintenance Editor
 * Administration/Modules Management/Maintenance Editor/Maintenance Configuration
 * Administration/Modules Management/Maintenance Editor/Maintenance Modules

.. i18n: Views
.. i18n: -----

Views
-----

.. i18n:  * maintenance.maintenance.tree (tree)
.. i18n:  * maintenance.maintenance.form (form)
.. i18n:  * maintenance.maintenance.module.tree (tree)
.. i18n:  * maintenance.maintenance.module.form (form)

 * maintenance.maintenance.tree (tree)
 * maintenance.maintenance.form (form)
 * maintenance.maintenance.module.tree (tree)
 * maintenance.maintenance.module.form (form)

.. i18n: Objects
.. i18n: -------

Objects
-------

.. i18n: Object: maintenance modules (maintenance.maintenance.module)
.. i18n: ############################################################

Object: maintenance modules (maintenance.maintenance.module)
############################################################

.. i18n: :version: Version, char

:version: Version, char

.. i18n: :name: Name, char, required

:name: Name, char, required

.. i18n: Object: maintenance (maintenance.maintenance)
.. i18n: #############################################

Object: maintenance (maintenance.maintenance)
#############################################

.. i18n: :name: Contract ID, char, required

:name: Contract ID, char, required

.. i18n: :module_ids: Modules, many2many

:module_ids: Modules, many2many

.. i18n: :date_from: Date From, date, required

:date_from: Date From, date, required

.. i18n: :state: State, selection, readonly

:state: State, selection, readonly

.. i18n: :date_to: Date To, date, required

:date_to: Date To, date, required

.. i18n: :partner_invoice_id: Address, many2one

:partner_invoice_id: Address, many2one

.. i18n: :password: Password, char, required

:password: Password, char, required

.. i18n: :partner_id: Partner, many2one, required

:partner_id: Partner, many2one, required
