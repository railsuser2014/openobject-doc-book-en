
.. module:: cci_event
    :synopsis: CCI EVENT
    :noindex:
.. 

CCI EVENT (*cci_event*)
=======================
:Module: cci_event
:Name: CCI EVENT
:Version: 5.0.1.0
:Directory: cci_event
:Web: http://www.openerp.com
:Is certified: no

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

Object: event.meeting.table (event.meeting.table)
#################################################



:service: Service, integer, required





:event_id: Related Event, many2one, required





:contact_id2: Second Contact, many2one, required





:contact_id1: First Contact, many2one, required





:partner_id1: First Partner, many2one, required





:table: Table, char, required





:partner_id2: Second Partner, many2one, required




Object: event.check.type (event.check.type)
###########################################



:name: Name, char, required




Object: event.check (event.check)
#################################



:date_reception: Reception Date, date





:code: Code, char





:name: Name, char, required





:type_id: Type, many2one





:date_submission: Submission Date, date





:date_limit: Limit Date, date





:reg_id: Inscriptions, many2one, required





:state: State, selection, readonly





:unit_nbr: Value, float




Object: event.group (event.group)
#################################



:picture: Picture, binary





:type: Type, selection, required





:name: Group Name, char, required





:bookmark_name: Value, char


