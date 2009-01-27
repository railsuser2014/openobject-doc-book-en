
Module Integrated Document Management System (*document*)
=========================================================
:Module: document
:Name: Integrated Document Management System
:Version: 5.0.1.0
:Directory: document
:Web: http://www.openerp.com

Description
-----------

::

  This is a complete document management system:
      * FTP Interface
      * User Authentication
      * Document Indexation

Dependencies
------------

 * base - installed
 * process - installed

Reports
-------

None


Menus
-------

 * Document Management
 * Document Management/Document Configuration
 * Document Management/Document Configuration/Directories
 * Document Management/Document Configuration/Directorie's Structure
 * Document Management/Browse Files Using FTP
 * Document Management/Search a File

Views
-----

 * document.directory (form)
 * document.directory (tree)
 * ir.attachment (form)
 * ir.attachment (tree)
 * \* INHERIT ir.attachment.view.inherit (form)
 * \* INHERIT process.node.form (form)
 * \* INHERIT process.process.form (form)
 * Auto Configure Directory (form)


Objects
-------

Object: Directory Content Type
##############################

.. index::
  single: Directory Content Type object
.. 


:active: Active, boolean



.. index::
  single: active field
.. 




:code: Extension, char



.. index::
  single: code field
.. 




:name: Content Type, char, required



.. index::
  single: name field
.. 



Object: document.configuration.wizard
#####################################

.. index::
  single: document.configuration.wizard object
.. 


:host: Server Address, char, required

    *Put here the server address or IP. Keep localhost if you don't know what to write.*

.. index::
  single: host field
.. 

