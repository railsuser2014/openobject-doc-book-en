
Module Event (*event*)
======================
:Module: event
:Name: Event
:Version: 5.0.0.1
:Directory: event
:Web: 

Description
-----------

::

  Organization and management of events.
  
      This module allow you
          * to manage your events and their registrations
          * to use emails to automatically confirm and send acknowledgements for any registration to an event
          * ...
  
      Note that:
      - You can define new types of events in
                  Events \ Configuration \ Types of Events
      - You can access predefined reports about number of registration per event or per event category in :
                  Events \ Reporting

Dependencies
------------

 * crm - installed
 * base_contact - installed
 * account - installed

Reports
-------

None


Menus
-------

 * Events Organisation
 * Events Organisation/Configuration
 * Events Organisation/Configuration/Types of Events
 * Events Organisation/Events by Categories
 * Events Organisation/New event
 * Events Organisation/All Events
 * Events Organisation/All Events/Draft Events
 * Events Organisation/All Events/Confirmed Events
 * Events Organisation/All Registrations
 * Events Organisation/All Registrations/Unconfirmed Registrations
 * Events Organisation/All Registrations/Confirmed Registrations
 * Events Organisation/Reporting
 * Events Organisation/Reporting/Events On Registrations
 * Events Organisation/Reporting/Registration By Event Types

Views
-----

 * Event type (form)
 * Event type (tree)
 * Events (form)
 * event.event.tree (tree)
 * event.registration.tree (tree)
 * event.registration.form (form)
 * report.event.registration.tree (tree)
 * report.event.registration.graph (graph)
 * report.event.type.registration.tree (tree)
 * report.event.type.registration.graph (graph)


Objects
-------

Object: Event type
##################

.. index::
  single: Event type object
.. 


:name: Event type, char, required



.. index::
  single: name field
.. 




:check_type: Default Check Type, many2one



.. index::
  single: check_type field
.. 



Object: Event
#############

.. index::
  single: Event object
.. 


:code: Section Code, char



.. index::
  single: code field
.. 




:check_type: Check Type, many2one



.. index::
  single: check_type field
.. 




:sequence: Sequence, integer



.. index::
  single: sequence field
.. 




:date_end: Ending date, datetime, required



.. index::
  single: date_end field
.. 




:register_max: Maximum Registrations, integer



.. index::
  single: register_max field
.. 




:task_ids: Project tasks, one2many, readonly



.. index::
  single: task_ids field
.. 




:date_begin: Beginning date, datetime, required



.. index::
  single: date_begin field
.. 




:mail_registr: Registration Email, text

    *This email will be sent when someone subscribes to the event.*

.. index::
  single: mail_registr field
.. 




:analytic_account_id: Main Analytic Account, many2one



.. index::
  single: analytic_account_id field
.. 




:mail_auto_confirm: Mail Auto Confirm, boolean

    *Check this box if you want ot use the automatic confirmation emailing or the reminder*

.. index::
  single: mail_auto_confirm field
.. 




:user_id: Responsible, many2one



.. index::
  single: user_id field
.. 




:mail_auto_registr: Mail Auto Register, boolean

    *Check this box if you want to use the automatic mailing for new registration*

.. index::
  single: mail_auto_registr field
.. 




:register_min: Minimum Registrations, integer



.. index::
  single: register_min field
.. 




:note: Note, text



.. index::
  single: note field
.. 




:parent_id: Parent Section, many2one



.. index::
  single: parent_id field
.. 




:state: State, selection, required, readonly



.. index::
  single: state field
.. 




:mail_confirm: Confirmation Email, text

    *This email will be sent when the event gets confimed or when someone subscribes to a confirmed event. This is also the email sent to remind someone about the event.*

.. index::
  single: mail_confirm field
.. 




:project_id: Project, many2one, readonly



.. index::
  single: project_id field
.. 




:type: Type, many2one



.. index::
  single: type field
.. 




:agreement_nbr: Agreement Nbr, char



.. index::
  single: agreement_nbr field
.. 




:child_ids: Childs Sections, one2many



.. index::
  single: child_ids field
.. 




:section_id: Case section, many2one, required



.. index::
  single: section_id field
.. 




:localisation: Localisation, char



.. index::
  single: localisation field
.. 




:active: Active, boolean



.. index::
  single: active field
.. 




:signet_type: Signet type, selection



.. index::
  single: signet_type field
.. 




:fse_hours: FSE Hours, integer



.. index::
  single: fse_hours field
.. 




:register_prospect: Unconfirmed Registrations, float, readonly



.. index::
  single: register_prospect field
.. 




:name: Case Section, char, required



.. index::
  single: name field
.. 




:case_ids: Cases, many2many



.. index::
  single: case_ids field
.. 




:analytic_journal_id: Analytic Journal, many2one



.. index::
  single: analytic_journal_id field
.. 




:fse_code: FSE code, char



.. index::
  single: fse_code field
.. 




:package_product_id: Package Product, many2one



.. index::
  single: package_product_id field
.. 




:register_current: Confirmed Registrations, float, readonly



.. index::
  single: register_current field
.. 




:product_id: Product, many2one, required



.. index::
  single: product_id field
.. 




:reply_to: Reply-To, char

    *The email address wich is the 'Reply-To' of all email sent by Open ERP for cases in this section*

.. index::
  single: reply_to field
.. 



Object: Event Registration
##########################

.. index::
  single: Event Registration object
.. 


:date_closed: Closed, datetime, readonly



.. index::
  single: date_closed field
.. 




:history_line: Communication, one2many, readonly



.. index::
  single: history_line field
.. 




:code: Calendar Code, char



.. index::
  single: code field
.. 




:create_date: Created, datetime, readonly



.. index::
  single: create_date field
.. 




:probability: Probability (%), float



.. index::
  single: probability field
.. 




:canal_id: Channel, many2one



.. index::
  single: canal_id field
.. 




:parent_fleet_id: Fleet, many2one



.. index::
  single: parent_fleet_id field
.. 




:zip_id: Zip, many2one



.. index::
  single: zip_id field
.. 




:partner_address_id: Partner Contact, many2one



.. index::
  single: partner_address_id field
.. 




:som: State of Mind, many2one



.. index::
  single: som field
.. 




:contact_id: Partner Contact, many2one



.. index::
  single: contact_id field
.. 




:check_amount: Check Amount, float, readonly



.. index::
  single: check_amount field
.. 




:incoming_move_id: Incoming Move, many2one



.. index::
  single: incoming_move_id field
.. 




:invoice_label: Label Invoice, char, required



.. index::
  single: invoice_label field
.. 




:fleet_id: Fleet, many2one



.. index::
  single: fleet_id field
.. 




:category2_id: Category Name, many2one



.. index::
  single: category2_id field
.. 




:in_supplier_move_id: Return To Supplier Move, many2one



.. index::
  single: in_supplier_move_id field
.. 




:duration: Duration, float



.. index::
  single: duration field
.. 




:event_ids: Events, many2many



.. index::
  single: event_ids field
.. 




:partner_id: Partner, many2one



.. index::
  single: partner_id field
.. 




:id: ID, integer, readonly



.. index::
  single: id field
.. 




:date_action_next: Next Action, datetime, readonly



.. index::
  single: date_action_next field
.. 




:priority: Priority, selection



.. index::
  single: priority field
.. 




:timesheet_line_id: Timesheet Line, many2one



.. index::
  single: timesheet_line_id field
.. 




:user_id: Responsible, many2one



.. index::
  single: user_id field
.. 




:tobe_invoiced: To be Invoiced, boolean



.. index::
  single: tobe_invoiced field
.. 




:partner_name: Employee Name, char



.. index::
  single: partner_name field
.. 




:planned_revenue: Planned Revenue, float



.. index::
  single: planned_revenue field
.. 




:meeting_id: Meeting confidential, many2one



.. index::
  single: meeting_id field
.. 




:unit_price: Unit Price, float



.. index::
  single: unit_price field
.. 




:badge_partner: Badge Partner, char



.. index::
  single: badge_partner field
.. 




:note: Note, text



.. index::
  single: note field
.. 




:state: Status, selection, readonly



.. index::
  single: state field
.. 




:case_id: Case, many2one



.. index::
  single: case_id field
.. 




:outgoing_move_id: Outgoing Move, many2one



.. index::
  single: outgoing_move_id field
.. 




:email_cc: Watchers Emails, char



.. index::
  single: email_cc field
.. 




:training_authorization: Training Auth., char, readonly

    *Formation Checks Authorization number*

.. index::
  single: training_authorization field
.. 




:external_ref: Ticket Code, char



.. index::
  single: external_ref field
.. 




:ref: Reference, reference



.. index::
  single: ref field
.. 




:log_ids: Logs History, one2many, readonly



.. index::
  single: log_ids field
.. 




:partner_invoice_id: Partner Invoiced, many2one



.. index::
  single: partner_invoice_id field
.. 




:cavalier: Cavalier, boolean

    *Check if we should print papers with participant name*

.. index::
  single: cavalier field
.. 




:description: Your action, text



.. index::
  single: description field
.. 




:payment_ids: Payment, many2many, readonly



.. index::
  single: payment_ids field
.. 




:date_action_last: Last Action, datetime, readonly



.. index::
  single: date_action_last field
.. 




:planned_cost: Planned Costs, float



.. index::
  single: planned_cost field
.. 




:ref2: Reference 2, reference



.. index::
  single: ref2 field
.. 




:badge_title: Badge Title, char



.. index::
  single: badge_title field
.. 




:section_id: Section, many2one, required



.. index::
  single: section_id field
.. 




:check_mode: Check Mode, boolean



.. index::
  single: check_mode field
.. 




:prodlot_id: Serial Number, many2one



.. index::
  single: prodlot_id field
.. 




:partner_name2: Employee Email, char



.. index::
  single: partner_name2 field
.. 




:partner_mobile: Mobile, char



.. index::
  single: partner_mobile field
.. 




:date: Date, datetime



.. index::
  single: date field
.. 




:nb_register: Number of Registration, integer, readonly



.. index::
  single: nb_register field
.. 




:active: Active, boolean



.. index::
  single: active field
.. 




:check_ids: Check ids, one2many



.. index::
  single: check_ids field
.. 




:name: Description, char, required



.. index::
  single: name field
.. 




:invoice_id: Invoice, many2one



.. index::
  single: invoice_id field
.. 




:stage_id: Stage, many2one



.. index::
  single: stage_id field
.. 




:contact_order_id: Contact Order, many2one



.. index::
  single: contact_order_id field
.. 




:incident_ref: Incident Ref, char, required



.. index::
  single: incident_ref field
.. 




:product_id: Related Product, many2one



.. index::
  single: product_id field
.. 




:date_deadline: Deadline, datetime



.. index::
  single: date_deadline field
.. 




:out_supplier_move_id: Return From Supplier Move, many2one



.. index::
  single: out_supplier_move_id field
.. 




:email_last: Latest E-Mail, text, readonly



.. index::
  single: email_last field
.. 




:grant_id: Grant, many2one



.. index::
  single: grant_id field
.. 




:is_fleet_expired: Is Fleet Expired?, boolean



.. index::
  single: is_fleet_expired field
.. 




:categ_id: Category, many2one



.. index::
  single: categ_id field
.. 




:email_from: Partner Email, char



.. index::
  single: email_from field
.. 




:payment_mode: Payment Mode, many2one



.. index::
  single: payment_mode field
.. 




:event_id: Event Related, many2one, required



.. index::
  single: event_id field
.. 




:partner_phone: Phone, char



.. index::
  single: partner_phone field
.. 




:badge_name: Badge Name, char



.. index::
  single: badge_name field
.. 




:group_id: Event Group, many2one



.. index::
  single: group_id field
.. 




:picking_id: Repair Picking, many2one



.. index::
  single: picking_id field
.. 



Object: Events on registrations
###############################

.. index::
  single: Events on registrations object
.. 


:date_begin: Beginning date, datetime, required



.. index::
  single: date_begin field
.. 




:name: Event, char



.. index::
  single: name field
.. 




:confirm_state: Confirm Registration, integer



.. index::
  single: confirm_state field
.. 




:draft_state: Draft Registration, integer



.. index::
  single: draft_state field
.. 




:date_end: Ending date, datetime, required



.. index::
  single: date_end field
.. 




:register_max: Maximum Registrations, integer



.. index::
  single: register_max field
.. 



Object: Event type on registration
##################################

.. index::
  single: Event type on registration object
.. 


:draft_state: Draft Registrations, integer



.. index::
  single: draft_state field
.. 




:confirm_state: Confirm Registrations, integer



.. index::
  single: confirm_state field
.. 




:name: Event Type, char



.. index::
  single: name field
.. 




:nbevent: Number Of Events, integer



.. index::
  single: nbevent field
.. 

