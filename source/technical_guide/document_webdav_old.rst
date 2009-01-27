
Module Integrated Document Management System (*document_webdav_old*)
====================================================================
:Module: document_webdav_old
:Name: Integrated Document Management System
:Version: 5.0.1.0
:Directory: document_webdav_old
:Web: http://www.tinyerp.com

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

Object: Document directory
##########################

.. index::
  single: Document directory object
.. 


:create_uid: Creator, many2one, readonly



.. index::
  single: create_uid field
.. 




:domain: Domain, char

    *Use a domain if you want to apply an automatic filter on visible ressources.*

.. index::
  single: domain field
.. 




:group_ids: Groups, many2many



.. index::
  single: group_ids field
.. 




:create_date: Date Created, datetime, readonly



.. index::
  single: create_date field
.. 




:ressource_type_id: Directories Mapped to Objects, many2one

    *Select an object here and Open ERP will create a mapping for each of these objects, using the given domain, when browsing through FTP.*

.. index::
  single: ressource_type_id field
.. 




:ressource_tree: Tree Structure, boolean

    *Check this if you want to use the same tree structure than the selected object in the system.*

.. index::
  single: ressource_tree field
.. 




:file_type: Content Type, char



.. index::
  single: file_type field
.. 




:version_regex: Reg. Ex., char



.. index::
  single: version_regex field
.. 




:content_ids: Virtual Files, one2many



.. index::
  single: content_ids field
.. 




:child_ids: Childs, one2many



.. index::
  single: child_ids field
.. 




:file_ids: Files, one2many



.. index::
  single: file_ids field
.. 




:write_uid: Last Modification User, many2one, readonly



.. index::
  single: write_uid field
.. 




:parent_id: Parent Item, many2one



.. index::
  single: parent_id field
.. 




:version_replace: Replace, char



.. index::
  single: version_replace field
.. 




:ressource_parent_type_id: Parent Model, many2one

    *If you put an object here, this directory template will appear bellow all of these objects. Don't put a parent directory if you select a parent model.*

.. index::
  single: ressource_parent_type_id field
.. 




:write_date: Date Modified, datetime, readonly



.. index::
  single: write_date field
.. 




:user_id: Owner, many2one



.. index::
  single: user_id field
.. 




:ressource_id: Ressource ID, integer



.. index::
  single: ressource_id field
.. 




:type: Type, selection, required



.. index::
  single: type field
.. 




:versioning: Automatic Versioning, boolean



.. index::
  single: versioning field
.. 




:name: Name, char, required



.. index::
  single: name field
.. 



Object: Directory Content
#########################

.. index::
  single: Directory Content object
.. 


:ics_object_id: Object, many2one



.. index::
  single: ics_object_id field
.. 




:ics_field_ids: Fields Mapping, one2many



.. index::
  single: ics_field_ids field
.. 




:suffix: Suffix, char



.. index::
  single: suffix field
.. 




:extension: Document Type, selection, required



.. index::
  single: extension field
.. 




:sequence: Sequence, integer



.. index::
  single: sequence field
.. 




:name: Content Name, char, required



.. index::
  single: name field
.. 




:directory_id: Directory, many2one



.. index::
  single: directory_id field
.. 




:ics_domain: Domain, char



.. index::
  single: ics_domain field
.. 




:include_name: Include Record Name, boolean

    *Check this field if you want that the name of the file start by the record name.*

.. index::
  single: include_name field
.. 




:report_id: Report, many2one



.. index::
  single: report_id field
.. 

