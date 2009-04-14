
.. i18n: .. module:: document
.. i18n:     :synopsis: Integrated Document Management System (Official, Quality Certified)
.. i18n:     :noindex:
.. i18n: .. 

.. module:: document
    :synopsis: Integrated Document Management System (Official, Quality Certified)
    :noindex:
.. 

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. i18n: Integrated Document Management System (*document*)
.. i18n: ==================================================
.. i18n: :Module: document
.. i18n: :Name: Integrated Document Management System
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: document
.. i18n: :Web: http://www.openerp.com
.. i18n: :Official module: yes
.. i18n: :Quality certified: yes

Integrated Document Management System (*document*)
==================================================
:Module: document
:Name: Integrated Document Management System
:Version: 5.0.1.0
:Author: Tiny
:Directory: document
:Web: http://www.openerp.com
:Official module: yes
:Quality certified: yes

.. i18n: Description
.. i18n: -----------

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   This is a complete document management system:
.. i18n:       * FTP Interface
.. i18n:       * User Authentication
.. i18n:       * Document Indexation

::

  This is a complete document management system:
      * FTP Interface
      * User Authentication
      * Document Indexation

.. i18n: Dependencies
.. i18n: ------------

Dependencies
------------

.. i18n:  * :mod:`base`
.. i18n:  * :mod:`process`

 * :mod:`base`
 * :mod:`process`

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

.. i18n:  * Document Management
.. i18n:  * Document Management/Document Configuration
.. i18n:  * Document Management/Document Configuration/Directories
.. i18n:  * Document Management/Document Configuration/Directorie's Structure
.. i18n:  * Document Management/Browse Files Using FTP
.. i18n:  * Document Management/Search a File

 * Document Management
 * Document Management/Document Configuration
 * Document Management/Document Configuration/Directories
 * Document Management/Document Configuration/Directorie's Structure
 * Document Management/Browse Files Using FTP
 * Document Management/Search a File

.. i18n: Views
.. i18n: -----

Views
-----

.. i18n:  * document.directory (form)
.. i18n:  * document.directory (tree)
.. i18n:  * ir.attachment (form)
.. i18n:  * ir.attachment (tree)
.. i18n:  * \* INHERIT ir.attachment.view.inherit (form)
.. i18n:  * \* INHERIT process.node.form (form)
.. i18n:  * \* INHERIT process.process.form (form)
.. i18n:  * Auto Configure Directory (form)

 * document.directory (form)
 * document.directory (tree)
 * ir.attachment (form)
 * ir.attachment (tree)
 * \* INHERIT ir.attachment.view.inherit (form)
 * \* INHERIT process.node.form (form)
 * \* INHERIT process.process.form (form)
 * Auto Configure Directory (form)

.. i18n: Objects
.. i18n: -------

Objects
-------

.. i18n: Object: Directory Content Type (document.directory.content.type)
.. i18n: ################################################################

Object: Directory Content Type (document.directory.content.type)
################################################################

.. i18n: :active: Active, boolean

:active: Active, boolean

.. i18n: :code: Extension, char

:code: Extension, char

.. i18n: :name: Content Type, char, required

:name: Content Type, char, required

.. i18n: Object: document.configuration.wizard (document.configuration.wizard)
.. i18n: #####################################################################

Object: document.configuration.wizard (document.configuration.wizard)
#####################################################################

.. i18n: :host: Server Address, char, required

:host: Server Address, char, required

.. i18n:     *Put here the server address or IP. Keep localhost if you don't know what to write.*

    *Put here the server address or IP. Keep localhost if you don't know what to write.*
