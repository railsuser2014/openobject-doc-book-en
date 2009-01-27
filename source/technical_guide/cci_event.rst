
Module CCI EVENT (*cci_event*)
==============================
:Module: cci_event
:Name: CCI EVENT
:Version: 5.0.1.0
:Directory: cci_event
:Web: http://www.openerp.com

Description
-----------

::

  specific module for cci project which will use Event module.

Dependencies
------------

 * event_project - installed
 * account_payment - installed
 * membership - installed
 * cci_account - installed
 * cci_partner - installed

Reports
-------

None


Menus
-------

 * Events Organisation/Configuration/Groups
 * Events Organisation/Configuration/Groups/Event Group
 * Events Organisation/Event Check
 * Events Organisation/Configuration/Event Check
 * Events Organisation/Configuration/Event Check/Check Type
 * Events Organisation/Event Meeting
 * Events Organisation/Reporting/Registrations with Missing Checks

Views
-----

 * \* INHERIT event.event.form.cci (form)
 * \* INHERIT event.event.form (form)
 * \* INHERIT event.event.form (form)
 * \* INHERIT event.event.form (form)
 * \* INHERIT event.event.form (form)
 * \* INHERIT event.event.form (form)
 * \* INHERIT event.event.form (form)
 * event.event.tree (tree)
 * \* INHERIT Event type (form)
 * \* INHERIT Event type (tree)
 * event.group.form (form)
 * event.group.tree (tree)
 * event.check.form (form)
 * event.check.tree (tree)
 * event.check.type.form (form)
 * event.check.type.tree (tree)
 * \* INHERIT event.registration.form (form)
 * \* INHERIT event.registration.form (form)
 * \* INHERIT event.registration.form (form)
 * \* INHERIT event.registration.form (form)
 * \* INHERIT event.registration.form.cci (form)
 * \* INHERIT event.registration.form (form)
 * \* INHERIT event.registration.form (form)
 * \* INHERIT event.registration.form (form)
 * \* INHERIT event.registration.form (form)
 * event.meeting.table.form (form)
 * event.meeting.table.tree (tree)
 * \* INHERIT account.move.line.form (form)


Objects
-------

Object: event.meeting.table
###########################

.. index::
  single: event.meeting.table object
.. 


:service: Service, integer, required



.. index::
  single: service field
.. 




:event_id: Related Event, many2one, required



.. index::
  single: event_id field
.. 




:contact_id2: Second Contact, many2one, required



.. index::
  single: contact_id2 field
.. 




:contact_id1: First Contact, many2one, required



.. index::
  single: contact_id1 field
.. 




:partner_id1: First Partner, many2one, required



.. index::
  single: partner_id1 field
.. 




:table: Table, char, required



.. index::
  single: table field
.. 




:partner_id2: Second Partner, many2one, required



.. index::
  single: partner_id2 field
.. 



Object: event.check.type
########################

.. index::
  single: event.check.type object
.. 


:name: Name, char, required



.. index::
  single: name field
.. 



Object: event.check
###################

.. index::
  single: event.check object
.. 


:date_reception: Reception Date, date



.. index::
  single: date_reception field
.. 




:code: Code, char



.. index::
  single: code field
.. 




:name: Name, char, required



.. index::
  single: name field
.. 




:type_id: Type, many2one



.. index::
  single: type_id field
.. 




:date_submission: Submission Date, date



.. index::
  single: date_submission field
.. 




:date_limit: Limit Date, date



.. index::
  single: date_limit field
.. 




:reg_id: Inscriptions, many2one, required



.. index::
  single: reg_id field
.. 




:state: State, selection, readonly



.. index::
  single: state field
.. 




:unit_nbr: Value, float



.. index::
  single: unit_nbr field
.. 



Object: event.group
###################

.. index::
  single: event.group object
.. 


:picture: Picture, binary



.. index::
  single: picture field
.. 




:type: Type, selection, required



.. index::
  single: type field
.. 




:name: Group Name, char, required



.. index::
  single: name field
.. 




:bookmark_name: Value, char



.. index::
  single: bookmark_name field
.. 

