
.. module:: document_webdav_old
    :synopsis: Integrated Document Management System
    :noindex:
.. 

Integrated Document Management System (*document_webdav_old*)
=============================================================
:Module: document_webdav_old
:Name: Integrated Document Management System
:Version: 5.0.1.0
:Directory: document_webdav_old
:Web: http://www.tinyerp.com
:Is certified: no

Description
-----------

::

  This is a complete document management system:
  	* WebDav Interface
  	* User Authentification
  	* Document Indexation

Dependencies
------------

 * base - installed

Reports
-------

None


Menus
-------

 * Document Management
 * Document Management/Configuration/Directories
 * Document Management/Directorie's Structure
 * Document Management/Search a File

Views
-----

 * document.directory (form)
 * document.directory (tree)
 * ir.attachment (form)
 * ir.attachment (tree)
 * \* INHERIT ir.attachment.view.inherit (form)


Objects
-------

Object: Document directory (document.directory)
###############################################



:create_uid: Creator, many2one, readonly





:domain: Domain, char

    *Use a domain if you want to apply an automatic filter on visible ressources.*



:group_ids: Groups, many2many





:create_date: Date Created, datetime, readonly





:ressource_type_id: Directories Mapped to Objects, many2one

    *Select an object here and Open ERP will create a mapping for each of these objects, using the given domain, when browsing through FTP.*



:ressource_tree: Tree Structure, boolean

    *Check this if you want to use the same tree structure than the selected object in the system.*



:file_type: Content Type, char





:version_regex: Reg. Ex., char





:content_ids: Virtual Files, one2many





:child_ids: Childs, one2many





:file_ids: Files, one2many





:write_uid: Last Modification User, many2one, readonly





:parent_id: Parent Item, many2one





:version_replace: Replace, char





:ressource_parent_type_id: Parent Model, many2one

    *If you put an object here, this directory template will appear bellow all of these objects. Don't put a parent directory if you select a parent model.*



:write_date: Date Modified, datetime, readonly





:user_id: Owner, many2one





:ressource_id: Ressource ID, integer





:type: Type, selection, required





:versioning: Automatic Versioning, boolean





:name: Name, char, required




Object: Directory Content (document.directory.content)
######################################################



:ics_object_id: Object, many2one





:ics_field_ids: Fields Mapping, one2many





:suffix: Suffix, char





:extension: Document Type, selection, required





:sequence: Sequence, integer





:name: Content Name, char, required





:directory_id: Directory, many2one





:ics_domain: Domain, char





:include_name: Include Record Name, boolean

    *Check this field if you want that the name of the file start by the record name.*



:report_id: Report, many2one


