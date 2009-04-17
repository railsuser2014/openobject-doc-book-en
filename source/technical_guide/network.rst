
.. module:: network
    :synopsis: Network Management 
    :noindex:
.. 

.. raw:: html

      <br />
    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. tip:: This module is part of the Open ERP software, the leading Open Source 
  enterprise management system. If you want to discover Open ERP, check our 
  `screencasts <href="http://openerp.tv>`_ or download 
  `Open ERP <href="http://openerp.com>`_ directly.

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/network"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Network Management (*network*)
==============================
:Module: network
:Name: Network Management
:Version: 5.0.1.0
:Author: Tiny
:Directory: network
:Web: 
:Official module: no
:Quality certified: no

Description
-----------

::

  A simple module to encode your networks and materials:
      - networks and connections between networks
      - hardwares and softwares with:
          - versions, access rights, waranties
  
      You can print interventions form for technical people.

Download links
--------------

You can download this module as a zip file in the following version:

  * `4.2 </download/modules/4.2/network.zip>`_
  * `trunk </download/modules/trunk/network.zip>`_


Dependencies
------------

 * :mod:`base`

Reports
-------

None


Menus
-------

 * Tools
 * Tools/Network
 * Tools/Network/Configuration
 * Tools/Network/All Materials
 * Tools/Network/Configuration/Software
 * Tools/Network/Configuration/Software/Types
 * Tools/Network/Configuration/Hardware
 * Tools/Network/Configuration/Hardware/Types
 * Tools/Network/Network List
 * Tools/Network/Networks

Views
-----

 * network.material.form (form)
 * network.material.tree (tree)
 * network.material.tree (tree)
 * network.software.type.form (form)
 * network.hardware.type.form (form)
 * network.software.logpass.form (form)
 * network.software.logpass.tree (tree)
 * network.software.form (form)
 * network.software.tree (tree)
 * network.network.tree (tree)
 * network.network.form (form)
 * network.changes.form (form)
 * network.changes.tree (tree)


Objects
-------

Object: Hardware type (network.hardware.type)
#############################################



:name: Type of material, char, required





:networkable: Networkable hardware, boolean




Object: Network (network.network)
#################################



:material_ids: Members, one2many





:range: Address range, char





:user_id: Onsite Contact person, many2one





:name: Network name, char, required





:contact_id: Partner, many2one, required




Object: Material (network.material)
###################################



:warranty: Warranty deadline, date





:ip_addr: IP Address, char





:name: Device Name, char, required





:network_id: Network, many2one





:change_id: Changes on this machine, one2many





:note: Notes, text





:parent_id: Parent Material, many2one





:date: Installation Date, date





:child_id: Childs Materials, one2many





:supplier: Supplier, many2one





:type: Hardware type, many2one, required





:software_id: Installed Software, one2many




Object: Network changes (network.changes)
#########################################



:date: Change date, date





:machine_id: Machine, many2one





:name: Short Description, char, required





:description: Long Description, text




Object: Software type (network.software.type)
#############################################



:note: Notes, text





:name: Composant Name, char, required




Object: Software (network.software)
###################################



:name: Composant Name, char, required





:logpass: Login / Password, one2many





:material_id: Material, many2one





:note: Notes, text





:version: Software version, char





:date: Installation Date, date





:type: Software Type, many2one, required





:email: Contact Email, char




Object: Software login (network.software.logpass)
#################################################



:login: Login, char, required





:password: Password, char, required





:software_id: Software, many2one, required


