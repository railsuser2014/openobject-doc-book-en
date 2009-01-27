
Module Network Management (*network*)
=====================================
:Module: network
:Name: Network Management
:Version: 5.0.1.0
:Directory: network
:Web: 

Description
-----------

::

  A simple module to encode your networks and materials:
      - networks and connections between networks
      - hardwares and softwares with:
          - versions, access rights, waranties
  
      You can print interventions form for technical people.

Dependencies
------------

 * base - installed

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

Object: Hardware type
#####################

.. index::
  single: Hardware type object
.. 


:name: Type of material, char, required



.. index::
  single: name field
.. 




:networkable: Networkable hardware, boolean



.. index::
  single: networkable field
.. 



Object: Network
###############

.. index::
  single: Network object
.. 


:material_ids: Members, one2many



.. index::
  single: material_ids field
.. 




:range: Address range, char



.. index::
  single: range field
.. 




:user_id: Onsite Contact person, many2one



.. index::
  single: user_id field
.. 




:name: Network name, char, required



.. index::
  single: name field
.. 




:contact_id: Partner, many2one, required



.. index::
  single: contact_id field
.. 



Object: Material
################

.. index::
  single: Material object
.. 


:warranty: Warranty deadline, date



.. index::
  single: warranty field
.. 




:ip_addr: IP Address, char



.. index::
  single: ip_addr field
.. 




:name: Device Name, char, required



.. index::
  single: name field
.. 




:network_id: Network, many2one



.. index::
  single: network_id field
.. 




:change_id: Changes on this machine, one2many



.. index::
  single: change_id field
.. 




:note: Notes, text



.. index::
  single: note field
.. 




:parent_id: Parent Material, many2one



.. index::
  single: parent_id field
.. 




:date: Installation Date, date



.. index::
  single: date field
.. 




:child_id: Childs Materials, one2many



.. index::
  single: child_id field
.. 




:supplier: Supplier, many2one



.. index::
  single: supplier field
.. 




:type: Hardware type, many2one, required



.. index::
  single: type field
.. 




:software_id: Installed Software, one2many



.. index::
  single: software_id field
.. 



Object: Network changes
#######################

.. index::
  single: Network changes object
.. 


:date: Change date, date



.. index::
  single: date field
.. 




:machine_id: Machine, many2one



.. index::
  single: machine_id field
.. 




:name: Short Description, char, required



.. index::
  single: name field
.. 




:description: Long Description, text



.. index::
  single: description field
.. 



Object: Software type
#####################

.. index::
  single: Software type object
.. 


:note: Notes, text



.. index::
  single: note field
.. 




:name: Composant Name, char, required



.. index::
  single: name field
.. 



Object: Software
################

.. index::
  single: Software object
.. 


:name: Composant Name, char, required



.. index::
  single: name field
.. 




:logpass: Login / Password, one2many



.. index::
  single: logpass field
.. 




:material_id: Material, many2one



.. index::
  single: material_id field
.. 




:note: Notes, text



.. index::
  single: note field
.. 




:version: Software version, char



.. index::
  single: version field
.. 




:date: Installation Date, date



.. index::
  single: date field
.. 




:type: Software Type, many2one, required



.. index::
  single: type field
.. 




:email: Contact Email, char



.. index::
  single: email field
.. 



Object: Software login
######################

.. index::
  single: Software login object
.. 


:login: Login, char, required



.. index::
  single: login field
.. 




:password: Password, char, required



.. index::
  single: password field
.. 




:software_id: Software, many2one, required



.. index::
  single: software_id field
.. 

