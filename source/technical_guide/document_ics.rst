
Module Support for iCal based on Document Management System (*document_ics*)
============================================================================
:Module: document_ics
:Name: Support for iCal based on Document Management System
:Version: 5.0.1.0
:Directory: document_ics
:Web: http://www.openerp.com

Description
-----------

::

  Allows to synchronise calendars with others applications.

Dependencies
------------

 * document - installed
 * crm_configuration - installed

Reports
-------

None


Menus
-------


None


Views
-----

 * \* INHERIT document.directory (form)


Objects
-------

Object: document.directory.ics.fields
#####################################

.. index::
  single: document.directory.ics.fields object
.. 


:content_id: Content, many2one, required



.. index::
  single: content_id field
.. 




:field_id: Open ERP Field, many2one, required



.. index::
  single: field_id field
.. 




:name: ICS Value, selection, required



.. index::
  single: name field
.. 

