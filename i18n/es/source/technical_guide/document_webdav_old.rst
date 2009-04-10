
.. i18n: .. module:: document_webdav_old
.. i18n:     :synopsis: Integrated Document Management System 
.. i18n:     :noindex:
.. i18n: .. 

.. module:: document_webdav_old
    :synopsis: Integrated Document Management System 
    :noindex:
.. 

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. i18n: Integrated Document Management System (*document_webdav_old*)
.. i18n: =============================================================
.. i18n: :Module: document_webdav_old
.. i18n: :Name: Integrated Document Management System
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: document_webdav_old
.. i18n: :Web: http://www.openerp.com/
.. i18n: :Official module: no
.. i18n: :Quality certified: no

Integrated Document Management System (*document_webdav_old*)
=============================================================
:Module: document_webdav_old
:Name: Integrated Document Management System
:Version: 5.0.1.0
:Author: Tiny
:Directory: document_webdav_old
:Web: http://www.openerp.com/
:Official module: no
:Quality certified: no

.. i18n: Description
.. i18n: -----------

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   This is a complete document management system:
.. i18n:   	* WebDav Interface
.. i18n:   	* User Authentification
.. i18n:   	* Document Indexation

::

  This is a complete document management system:
  	* WebDav Interface
  	* User Authentification
  	* Document Indexation

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

.. i18n:  * Document Management
.. i18n:  * Document Management/Configuration/Directories
.. i18n:  * Document Management/Directorie's Structure
.. i18n:  * Document Management/Search a File

 * Document Management
 * Document Management/Configuration/Directories
 * Document Management/Directorie's Structure
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

 * document.directory (form)
 * document.directory (tree)
 * ir.attachment (form)
 * ir.attachment (tree)
 * \* INHERIT ir.attachment.view.inherit (form)

.. i18n: Objects
.. i18n: -------

Objects
-------

.. i18n: Object: Document directory (document.directory)
.. i18n: ###############################################

Object: Document directory (document.directory)
###############################################

.. i18n: :create_uid: Creator, many2one, readonly

:create_uid: Creator, many2one, readonly

.. i18n: :domain: Domain, char

:domain: Domain, char

.. i18n:     *Use a domain if you want to apply an automatic filter on visible resources.*

    *Use a domain if you want to apply an automatic filter on visible resources.*

.. i18n: :group_ids: Groups, many2many

:group_ids: Groups, many2many

.. i18n: :create_date: Date Created, datetime, readonly

:create_date: Date Created, datetime, readonly

.. i18n: :ressource_type_id: Directories Mapped to Objects, many2one

:ressource_type_id: Directories Mapped to Objects, many2one

.. i18n:     *Select an object here and Open ERP will create a mapping for each of these objects, using the given domain, when browsing through FTP.*

    *Select an object here and Open ERP will create a mapping for each of these objects, using the given domain, when browsing through FTP.*

.. i18n: :ressource_tree: Tree Structure, boolean

:ressource_tree: Tree Structure, boolean

.. i18n:     *Check this if you want to use the same tree structure than the selected object in the system.*

    *Check this if you want to use the same tree structure than the selected object in the system.*

.. i18n: :file_type: Content Type, char

:file_type: Content Type, char

.. i18n: :version_regex: Reg. Ex., char

:version_regex: Reg. Ex., char

.. i18n: :content_ids: Virtual Files, one2many

:content_ids: Virtual Files, one2many

.. i18n: :child_ids: Childs, one2many

:child_ids: Childs, one2many

.. i18n: :file_ids: Files, one2many

:file_ids: Files, one2many

.. i18n: :write_uid: Last Modification User, many2one, readonly

:write_uid: Last Modification User, many2one, readonly

.. i18n: :parent_id: Parent Item, many2one

:parent_id: Parent Item, many2one

.. i18n: :version_replace: Replace, char

:version_replace: Replace, char

.. i18n: :ressource_parent_type_id: Parent Model, many2one

:ressource_parent_type_id: Parent Model, many2one

.. i18n:     *If you put an object here, this directory template will appear bellow all of these objects. Don't put a parent directory if you select a parent model.*

    *If you put an object here, this directory template will appear bellow all of these objects. Don't put a parent directory if you select a parent model.*

.. i18n: :write_date: Date Modified, datetime, readonly

:write_date: Date Modified, datetime, readonly

.. i18n: :user_id: Owner, many2one

:user_id: Owner, many2one

.. i18n: :ressource_id: Ressource ID, integer

:ressource_id: Ressource ID, integer

.. i18n: :type: Type, selection, required

:type: Type, selection, required

.. i18n: :versioning: Automatic Versioning, boolean

:versioning: Automatic Versioning, boolean

.. i18n: :name: Name, char, required

:name: Name, char, required

.. i18n: Object: Directory Content (document.directory.content)
.. i18n: ######################################################

Object: Directory Content (document.directory.content)
######################################################

.. i18n: :ics_object_id: Object, many2one

:ics_object_id: Object, many2one

.. i18n: :ics_field_ids: Fields Mapping, one2many

:ics_field_ids: Fields Mapping, one2many

.. i18n: :suffix: Suffix, char

:suffix: Suffix, char

.. i18n: :extension: Document Type, selection, required

:extension: Document Type, selection, required

.. i18n: :sequence: Sequence, integer

:sequence: Sequence, integer

.. i18n: :name: Content Name, char, required

:name: Content Name, char, required

.. i18n: :directory_id: Directory, many2one

:directory_id: Directory, many2one

.. i18n: :ics_domain: Domain, char

:ics_domain: Domain, char

.. i18n: :include_name: Include Record Name, boolean

:include_name: Include Record Name, boolean

.. i18n:     *Check this field if you want that the name of the file start by the record name.*

    *Check this field if you want that the name of the file start by the record name.*

.. i18n: :report_id: Report, many2one

:report_id: Report, many2one
