
.. i18n: .. module:: event
.. i18n:     :synopsis: Event (Official, Quality Certified)
.. i18n:     :noindex:
.. i18n: .. 

.. module:: event
    :synopsis: Event (Official, Quality Certified)
    :noindex:
.. 

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. i18n: Event (*event*)
.. i18n: ===============
.. i18n: :Module: event
.. i18n: :Name: Event
.. i18n: :Version: 5.0.0.1
.. i18n: :Author: Tiny
.. i18n: :Directory: event
.. i18n: :Web: 
.. i18n: :Official module: yes
.. i18n: :Quality certified: yes

Event (*event*)
===============
:Module: event
:Name: Event
:Version: 5.0.0.1
:Author: Tiny
:Directory: event
:Web: 
:Official module: yes
:Quality certified: yes

.. i18n: Description
.. i18n: -----------

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   Organization and management of events.
.. i18n:   
.. i18n:       This module allow you
.. i18n:           * to manage your events and their registrations
.. i18n:           * to use emails to automatically confirm and send acknowledgements for 
.. i18n:             any registration to an event
.. i18n:           * ...
.. i18n:   
.. i18n:       Note that:
.. i18n:       - You can define new types of events in
.. i18n:                   Events \ Configuration \ Types of Events
.. i18n:       - You can access predefined reports about number of registration per event 
.. i18n:         or per event category in :
.. i18n:                   Events \ Reporting

::

  Organization and management of events.
  
      This module allow you
          * to manage your events and their registrations
          * to use emails to automatically confirm and send acknowledgements for 
            any registration to an event
          * ...
  
      Note that:
      - You can define new types of events in
                  Events \ Configuration \ Types of Events
      - You can access predefined reports about number of registration per event 
        or per event category in :
                  Events \ Reporting

.. i18n: Dependencies
.. i18n: ------------

Dependencies
------------

.. i18n:  * :mod:`crm`
.. i18n:  * :mod:`base_contact`
.. i18n:  * :mod:`account`

 * :mod:`crm`
 * :mod:`base_contact`
 * :mod:`account`

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

.. i18n:  * Events Organisation
.. i18n:  * Events Organisation/Configuration
.. i18n:  * Events Organisation/Configuration/Types of Events
.. i18n:  * Events Organisation/Events by Categories
.. i18n:  * Events Organisation/New event
.. i18n:  * Events Organisation/All Events
.. i18n:  * Events Organisation/All Events/Draft Events
.. i18n:  * Events Organisation/All Events/Confirmed Events
.. i18n:  * Events Organisation/All Registrations
.. i18n:  * Events Organisation/All Registrations/Unconfirmed Registrations
.. i18n:  * Events Organisation/All Registrations/Confirmed Registrations
.. i18n:  * Events Organisation/Reporting
.. i18n:  * Events Organisation/Reporting/Events On Registrations
.. i18n:  * Events Organisation/Reporting/Registration By Event Types

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

.. i18n: Views
.. i18n: -----

Views
-----

.. i18n:  * Event type (form)
.. i18n:  * Event type (tree)
.. i18n:  * Events (form)
.. i18n:  * event.event.tree (tree)
.. i18n:  * event.registration.tree (tree)
.. i18n:  * event.registration.form (form)
.. i18n:  * report.event.registration.tree (tree)
.. i18n:  * report.event.registration.graph (graph)
.. i18n:  * report.event.type.registration.tree (tree)
.. i18n:  * report.event.type.registration.graph (graph)

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

.. i18n: Objects
.. i18n: -------

Objects
-------

.. i18n: Object: Event type (event.type)
.. i18n: ###############################

Object: Event type (event.type)
###############################

.. i18n: :name: Event type, char, required

:name: Event type, char, required

.. i18n: :check_type: Default Check Type, many2one

:check_type: Default Check Type, many2one

.. i18n: Object: Event (event.event)
.. i18n: ###########################

Object: Event (event.event)
###########################

.. i18n: :code: Section Code, char

:code: Section Code, char

.. i18n: :check_type: Check Type, many2one

:check_type: Check Type, many2one

.. i18n: :sequence: Sequence, integer

:sequence: Sequence, integer

.. i18n: :date_end: Ending date, datetime, required

:date_end: Ending date, datetime, required

.. i18n: :register_max: Maximum Registrations, integer

:register_max: Maximum Registrations, integer

.. i18n: :task_ids: Project tasks, one2many, readonly

:task_ids: Project tasks, one2many, readonly

.. i18n: :date_begin: Beginning date, datetime, required

:date_begin: Beginning date, datetime, required

.. i18n: :mail_registr: Registration Email, text

:mail_registr: Registration Email, text

.. i18n:     *This email will be sent when someone subscribes to the event.*

    *This email will be sent when someone subscribes to the event.*

.. i18n: :analytic_account_id: Main Analytic Account, many2one

:analytic_account_id: Main Analytic Account, many2one

.. i18n: :mail_auto_confirm: Mail Auto Confirm, boolean

:mail_auto_confirm: Mail Auto Confirm, boolean

.. i18n:     *Check this box if you want ot use the automatic confirmation emailing or the reminder*

    *Check this box if you want ot use the automatic confirmation emailing or the reminder*

.. i18n: :user_id: Responsible, many2one

:user_id: Responsible, many2one

.. i18n: :mail_auto_registr: Mail Auto Register, boolean

:mail_auto_registr: Mail Auto Register, boolean

.. i18n:     *Check this box if you want to use the automatic mailing for new registration*

    *Check this box if you want to use the automatic mailing for new registration*

.. i18n: :register_min: Minimum Registrations, integer

:register_min: Minimum Registrations, integer

.. i18n: :note: Note, text

:note: Note, text

.. i18n: :parent_id: Parent Section, many2one

:parent_id: Parent Section, many2one

.. i18n: :state: State, selection, required, readonly

:state: State, selection, required, readonly

.. i18n: :mail_confirm: Confirmation Email, text

:mail_confirm: Confirmation Email, text

.. i18n:     *This email will be sent when the event gets confimed or when someone subscribes to a confirmed event. This is also the email sent to remind someone about the event.*

    *This email will be sent when the event gets confimed or when someone subscribes to a confirmed event. This is also the email sent to remind someone about the event.*

.. i18n: :project_id: Project, many2one, readonly

:project_id: Project, many2one, readonly

.. i18n: :type: Type, many2one

:type: Type, many2one

.. i18n: :agreement_nbr: Agreement Nbr, char

:agreement_nbr: Agreement Nbr, char

.. i18n: :child_ids: Childs Sections, one2many

:child_ids: Childs Sections, one2many

.. i18n: :section_id: Case section, many2one, required

:section_id: Case section, many2one, required

.. i18n: :localisation: Localisation, char

:localisation: Localisation, char

.. i18n: :active: Active, boolean

:active: Active, boolean

.. i18n: :signet_type: Signet type, selection

:signet_type: Signet type, selection

.. i18n: :fse_hours: FSE Hours, integer

:fse_hours: FSE Hours, integer

.. i18n: :register_prospect: Unconfirmed Registrations, float, readonly

:register_prospect: Unconfirmed Registrations, float, readonly

.. i18n: :name: Case Section, char, required

:name: Case Section, char, required

.. i18n: :case_ids: Cases, many2many

:case_ids: Cases, many2many

.. i18n: :analytic_journal_id: Analytic Journal, many2one

:analytic_journal_id: Analytic Journal, many2one

.. i18n: :fse_code: FSE code, char

:fse_code: FSE code, char

.. i18n: :package_product_id: Package Product, many2one

:package_product_id: Package Product, many2one

.. i18n: :register_current: Confirmed Registrations, float, readonly

:register_current: Confirmed Registrations, float, readonly

.. i18n: :product_id: Product, many2one, required

:product_id: Product, many2one, required

.. i18n: :reply_to: Reply-To, char

:reply_to: Reply-To, char

.. i18n:     *The email address wich is the 'Reply-To' of all email sent by Open ERP for cases in this section*

    *The email address wich is the 'Reply-To' of all email sent by Open ERP for cases in this section*

.. i18n: Object: Event Registration (event.registration)
.. i18n: ###############################################

Object: Event Registration (event.registration)
###############################################

.. i18n: :date_closed: Closed, datetime, readonly

:date_closed: Closed, datetime, readonly

.. i18n: :history_line: Communication, one2many, readonly

:history_line: Communication, one2many, readonly

.. i18n: :code: Calendar Code, char

:code: Calendar Code, char

.. i18n: :create_date: Created, datetime, readonly

:create_date: Created, datetime, readonly

.. i18n: :probability: Probability (%), float

:probability: Probability (%), float

.. i18n: :canal_id: Channel, many2one

:canal_id: Channel, many2one

.. i18n: :parent_fleet_id: Fleet, many2one

:parent_fleet_id: Fleet, many2one

.. i18n: :zip_id: Zip, many2one

:zip_id: Zip, many2one

.. i18n: :partner_address_id: Partner Contact, many2one

:partner_address_id: Partner Contact, many2one

.. i18n: :som: State of Mind, many2one

:som: State of Mind, many2one

.. i18n: :contact_id: Partner Contact, many2one

:contact_id: Partner Contact, many2one

.. i18n: :check_amount: Check Amount, float, readonly

:check_amount: Check Amount, float, readonly

.. i18n: :incoming_move_id: Incoming Move, many2one

:incoming_move_id: Incoming Move, many2one

.. i18n: :invoice_label: Label Invoice, char, required

:invoice_label: Label Invoice, char, required

.. i18n: :fleet_id: Fleet, many2one

:fleet_id: Fleet, many2one

.. i18n: :category2_id: Category Name, many2one

:category2_id: Category Name, many2one

.. i18n: :in_supplier_move_id: Return To Supplier Move, many2one

:in_supplier_move_id: Return To Supplier Move, many2one

.. i18n: :duration: Duration, float

:duration: Duration, float

.. i18n: :event_ids: Events, many2many

:event_ids: Events, many2many

.. i18n: :partner_id: Partner, many2one

:partner_id: Partner, many2one

.. i18n: :id: ID, integer, readonly

:id: ID, integer, readonly

.. i18n: :date_action_next: Next Action, datetime, readonly

:date_action_next: Next Action, datetime, readonly

.. i18n: :priority: Priority, selection

:priority: Priority, selection

.. i18n: :timesheet_line_id: Timesheet Line, many2one

:timesheet_line_id: Timesheet Line, many2one

.. i18n: :user_id: Responsible, many2one

:user_id: Responsible, many2one

.. i18n: :tobe_invoiced: To be Invoiced, boolean

:tobe_invoiced: To be Invoiced, boolean

.. i18n: :partner_name: Employee Name, char

:partner_name: Employee Name, char

.. i18n: :planned_revenue: Planned Revenue, float

:planned_revenue: Planned Revenue, float

.. i18n: :meeting_id: Meeting confidential, many2one

:meeting_id: Meeting confidential, many2one

.. i18n: :unit_price: Unit Price, float

:unit_price: Unit Price, float

.. i18n: :badge_partner: Badge Partner, char

:badge_partner: Badge Partner, char

.. i18n: :note: Note, text

:note: Note, text

.. i18n: :state: Status, selection, readonly

:state: Status, selection, readonly

.. i18n: :case_id: Case, many2one

:case_id: Case, many2one

.. i18n: :outgoing_move_id: Outgoing Move, many2one

:outgoing_move_id: Outgoing Move, many2one

.. i18n: :email_cc: Watchers Emails, char

:email_cc: Watchers Emails, char

.. i18n: :training_authorization: Training Auth., char, readonly

:training_authorization: Training Auth., char, readonly

.. i18n:     *Formation Checks Authorization number*

    *Formation Checks Authorization number*

.. i18n: :external_ref: Ticket Code, char

:external_ref: Ticket Code, char

.. i18n: :ref: Reference, reference

:ref: Reference, reference

.. i18n: :log_ids: Logs History, one2many, readonly

:log_ids: Logs History, one2many, readonly

.. i18n: :partner_invoice_id: Partner Invoiced, many2one

:partner_invoice_id: Partner Invoiced, many2one

.. i18n: :cavalier: Cavalier, boolean

:cavalier: Cavalier, boolean

.. i18n:     *Check if we should print papers with participant name*

    *Check if we should print papers with participant name*

.. i18n: :description: Your action, text

:description: Your action, text

.. i18n: :payment_ids: Payment, many2many, readonly

:payment_ids: Payment, many2many, readonly

.. i18n: :date_action_last: Last Action, datetime, readonly

:date_action_last: Last Action, datetime, readonly

.. i18n: :planned_cost: Planned Costs, float

:planned_cost: Planned Costs, float

.. i18n: :ref2: Reference 2, reference

:ref2: Reference 2, reference

.. i18n: :badge_title: Badge Title, char

:badge_title: Badge Title, char

.. i18n: :section_id: Section, many2one, required

:section_id: Section, many2one, required

.. i18n: :check_mode: Check Mode, boolean

:check_mode: Check Mode, boolean

.. i18n: :prodlot_id: Serial Number, many2one

:prodlot_id: Serial Number, many2one

.. i18n: :partner_name2: Employee Email, char

:partner_name2: Employee Email, char

.. i18n: :partner_mobile: Mobile, char

:partner_mobile: Mobile, char

.. i18n: :date: Date, datetime

:date: Date, datetime

.. i18n: :nb_register: Number of Registration, integer, readonly

:nb_register: Number of Registration, integer, readonly

.. i18n: :active: Active, boolean

:active: Active, boolean

.. i18n: :check_ids: Check ids, one2many

:check_ids: Check ids, one2many

.. i18n: :name: Description, char, required

:name: Description, char, required

.. i18n: :invoice_id: Invoice, many2one

:invoice_id: Invoice, many2one

.. i18n: :stage_id: Stage, many2one

:stage_id: Stage, many2one

.. i18n: :contact_order_id: Contact Order, many2one

:contact_order_id: Contact Order, many2one

.. i18n: :incident_ref: Incident Ref, char, required

:incident_ref: Incident Ref, char, required

.. i18n: :product_id: Related Product, many2one

:product_id: Related Product, many2one

.. i18n: :date_deadline: Deadline, datetime

:date_deadline: Deadline, datetime

.. i18n: :out_supplier_move_id: Return From Supplier Move, many2one

:out_supplier_move_id: Return From Supplier Move, many2one

.. i18n: :email_last: Latest E-Mail, text, readonly

:email_last: Latest E-Mail, text, readonly

.. i18n: :grant_id: Grant, many2one

:grant_id: Grant, many2one

.. i18n: :is_fleet_expired: Is Fleet Expired?, boolean

:is_fleet_expired: Is Fleet Expired?, boolean

.. i18n: :categ_id: Category, many2one

:categ_id: Category, many2one

.. i18n: :email_from: Partner Email, char

:email_from: Partner Email, char

.. i18n: :payment_mode: Payment Mode, many2one

:payment_mode: Payment Mode, many2one

.. i18n: :event_id: Event Related, many2one, required

:event_id: Event Related, many2one, required

.. i18n: :partner_phone: Phone, char

:partner_phone: Phone, char

.. i18n: :badge_name: Badge Name, char

:badge_name: Badge Name, char

.. i18n: :group_id: Event Group, many2one

:group_id: Event Group, many2one

.. i18n: :picking_id: Repair Picking, many2one

:picking_id: Repair Picking, many2one

.. i18n: Object: Events on registrations (report.event.registration)
.. i18n: ###########################################################

Object: Events on registrations (report.event.registration)
###########################################################

.. i18n: :date_begin: Beginning date, datetime, required

:date_begin: Beginning date, datetime, required

.. i18n: :name: Event, char

:name: Event, char

.. i18n: :confirm_state: Confirm Registration, integer

:confirm_state: Confirm Registration, integer

.. i18n: :draft_state: Draft Registration, integer

:draft_state: Draft Registration, integer

.. i18n: :date_end: Ending date, datetime, required

:date_end: Ending date, datetime, required

.. i18n: :register_max: Maximum Registrations, integer

:register_max: Maximum Registrations, integer

.. i18n: Object: Event type on registration (report.event.type.registration)
.. i18n: ###################################################################

Object: Event type on registration (report.event.type.registration)
###################################################################

.. i18n: :draft_state: Draft Registrations, integer

:draft_state: Draft Registrations, integer

.. i18n: :confirm_state: Confirm Registrations, integer

:confirm_state: Confirm Registrations, integer

.. i18n: :name: Event Type, char

:name: Event Type, char

.. i18n: :nbevent: Number Of Events, integer

:nbevent: Number Of Events, integer
