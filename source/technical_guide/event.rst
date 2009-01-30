
.. module:: event
    :synopsis: Event
    :noindex:
.. 

Event (*event*)
===============
:Module: event
:Name: Event
:Version: 5.0.0.1
:Directory: event
:Web: 
:Is certified: yes

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

Object: Event type (event.type)
###############################



:name: Event type, char, required





:check_type: Default Check Type, many2one




Object: Event (event.event)
###########################



:code: Section Code, char





:check_type: Check Type, many2one





:sequence: Sequence, integer





:date_end: Ending date, datetime, required





:register_max: Maximum Registrations, integer





:task_ids: Project tasks, one2many, readonly





:date_begin: Beginning date, datetime, required





:mail_registr: Registration Email, text

    *This email will be sent when someone subscribes to the event.*



:analytic_account_id: Main Analytic Account, many2one





:mail_auto_confirm: Mail Auto Confirm, boolean

    *Check this box if you want ot use the automatic confirmation emailing or the reminder*



:user_id: Responsible, many2one





:mail_auto_registr: Mail Auto Register, boolean

    *Check this box if you want to use the automatic mailing for new registration*



:register_min: Minimum Registrations, integer





:note: Note, text





:parent_id: Parent Section, many2one





:state: State, selection, required, readonly





:mail_confirm: Confirmation Email, text

    *This email will be sent when the event gets confimed or when someone subscribes to a confirmed event. This is also the email sent to remind someone about the event.*



:project_id: Project, many2one, readonly





:type: Type, many2one





:agreement_nbr: Agreement Nbr, char





:child_ids: Childs Sections, one2many





:section_id: Case section, many2one, required





:localisation: Localisation, char





:active: Active, boolean





:signet_type: Signet type, selection





:fse_hours: FSE Hours, integer





:register_prospect: Unconfirmed Registrations, float, readonly





:name: Case Section, char, required





:case_ids: Cases, many2many





:analytic_journal_id: Analytic Journal, many2one





:fse_code: FSE code, char





:package_product_id: Package Product, many2one





:register_current: Confirmed Registrations, float, readonly





:product_id: Product, many2one, required





:reply_to: Reply-To, char

    *The email address wich is the 'Reply-To' of all email sent by Open ERP for cases in this section*


Object: Event Registration (event.registration)
###############################################



:date_closed: Closed, datetime, readonly





:history_line: Communication, one2many, readonly





:code: Calendar Code, char





:create_date: Created, datetime, readonly





:probability: Probability (%), float





:canal_id: Channel, many2one





:parent_fleet_id: Fleet, many2one





:zip_id: Zip, many2one





:partner_address_id: Partner Contact, many2one





:som: State of Mind, many2one





:contact_id: Partner Contact, many2one





:check_amount: Check Amount, float, readonly





:incoming_move_id: Incoming Move, many2one





:invoice_label: Label Invoice, char, required





:fleet_id: Fleet, many2one





:category2_id: Category Name, many2one





:in_supplier_move_id: Return To Supplier Move, many2one





:duration: Duration, float





:event_ids: Events, many2many





:partner_id: Partner, many2one





:id: ID, integer, readonly





:date_action_next: Next Action, datetime, readonly





:priority: Priority, selection





:timesheet_line_id: Timesheet Line, many2one





:user_id: Responsible, many2one





:tobe_invoiced: To be Invoiced, boolean





:partner_name: Employee Name, char





:planned_revenue: Planned Revenue, float





:meeting_id: Meeting confidential, many2one





:unit_price: Unit Price, float





:badge_partner: Badge Partner, char





:note: Note, text





:state: Status, selection, readonly





:case_id: Case, many2one





:outgoing_move_id: Outgoing Move, many2one





:email_cc: Watchers Emails, char





:training_authorization: Training Auth., char, readonly

    *Formation Checks Authorization number*



:external_ref: Ticket Code, char





:ref: Reference, reference





:log_ids: Logs History, one2many, readonly





:partner_invoice_id: Partner Invoiced, many2one





:cavalier: Cavalier, boolean

    *Check if we should print papers with participant name*



:description: Your action, text





:payment_ids: Payment, many2many, readonly





:date_action_last: Last Action, datetime, readonly





:planned_cost: Planned Costs, float





:ref2: Reference 2, reference





:badge_title: Badge Title, char





:section_id: Section, many2one, required





:check_mode: Check Mode, boolean





:prodlot_id: Serial Number, many2one





:partner_name2: Employee Email, char





:partner_mobile: Mobile, char





:date: Date, datetime





:nb_register: Number of Registration, integer, readonly





:active: Active, boolean





:check_ids: Check ids, one2many





:name: Description, char, required





:invoice_id: Invoice, many2one





:stage_id: Stage, many2one





:contact_order_id: Contact Order, many2one





:incident_ref: Incident Ref, char, required





:product_id: Related Product, many2one





:date_deadline: Deadline, datetime





:out_supplier_move_id: Return From Supplier Move, many2one





:email_last: Latest E-Mail, text, readonly





:grant_id: Grant, many2one





:is_fleet_expired: Is Fleet Expired?, boolean





:categ_id: Category, many2one





:email_from: Partner Email, char





:payment_mode: Payment Mode, many2one





:event_id: Event Related, many2one, required





:partner_phone: Phone, char





:badge_name: Badge Name, char





:group_id: Event Group, many2one





:picking_id: Repair Picking, many2one




Object: Events on registrations (report.event.registration)
###########################################################



:date_begin: Beginning date, datetime, required





:name: Event, char





:confirm_state: Confirm Registration, integer





:draft_state: Draft Registration, integer





:date_end: Ending date, datetime, required





:register_max: Maximum Registrations, integer




Object: Event type on registration (report.event.type.registration)
###################################################################



:draft_state: Draft Registrations, integer





:confirm_state: Confirm Registrations, integer





:name: Event Type, char





:nbevent: Number Of Events, integer


