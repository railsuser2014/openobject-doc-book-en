
Module Customer & Supplier Relationship Management (*crm*)
==========================================================
:Module: crm
:Name: Customer & Supplier Relationship Management
:Version: 5.0.1.0
:Directory: crm
:Web: http://www.openerp.com

Description
-----------

::

  The generic Open ERP Customer Relationship Management
  system enables a group of people to intelligently and efficiently manage
  leads, opportunities, tasks, issues, requests, bugs, campaign, claims, etc.
  It manages key tasks such as communication, identification, prioritization,
  assignment, resolution and notification.
  
  Open ERP ensures that all cases are successfully tracked by users, customers and
  suppliers. It can automatically send reminders, escalate the request, trigger
  specific methods and lots of others actions based on your enterprise own rules.
  
  The greatest thing about this system is that users don't need to do anything
  special. They can just send email to the request tracker. Open ERP will take
  care of thanking them for their message, automatically routing it to the
  appropriate staff, and making sure all future correspondence gets to the right
  place.
  
  The CRM module has a email gateway for the synchronisation interface
  between mails and Open ERP.

Dependencies
------------

 * base - installed

Reports
-------

 * Business Opportunities

Menus
-------

 * CRM & SRM
 * CRM & SRM/Configuration
 * CRM & SRM/Configuration/Cases
 * CRM & SRM/Configuration/Cases/Sections
 * CRM & SRM/All Cases
 * CRM & SRM/All Cases/Cases by section
 * CRM & SRM/Configuration/Cases/Categories
 * CRM & SRM/Configuration/Cases/Rules
 * CRM & SRM/All Cases/All Cases
 * CRM & SRM/All Cases/All Cases/Open Cases
 * CRM & SRM/All Cases/My cases
 * CRM & SRM/All Cases/My cases/My Open Cases
 * CRM & SRM/All Cases/Cases Histories
 * CRM & SRM/All Cases/Cases Histories/All Histories
 * CRM & SRM/All Cases/Cases Histories/My Histories
 * CRM & SRM/Configuration/Segmentations
 * CRM & SRM/Configuration/Segmentations/Segmentations
 * CRM & SRM/Configuration/Create menus for a case section

Views
-----

 * res.partner.events.form (tree)
 * crm.case.section.form (form)
 * crm.case.section.tree (tree)
 * crm.case.categ.form (form)
 * crm.case.categ.tree (tree)
 * crm.case.rule.form (form)
 * crm.case.rule.tree (tree)
 * crm.case.log.tree (tree)
 * crm.case.history.tree (tree)
 * crm.case.calendar (calendar)
 * crm.case.tree (tree)
 * crm.case.form (form)
 * crm.case.history.form (form)
 * crm.segmentation.line.tree (tree)
 * crm.segmentation.line.form (form)
 * crm.segmentation.form (form)
 * crm.segmentation.tree (tree)


Objects
-------

Object: Case Section
####################

.. index::
  single: Case Section object
.. 


:analytic_account_id: Main Analytic Account, many2one



.. index::
  single: analytic_account_id field
.. 




:code: Section Code, char



.. index::
  single: code field
.. 




:user_id: Responsible, many2one



.. index::
  single: user_id field
.. 




:name: Case Section, char, required



.. index::
  single: name field
.. 




:sequence: Sequence, integer



.. index::
  single: sequence field
.. 




:analytic_journal_id: Analytic Journal, many2one



.. index::
  single: analytic_journal_id field
.. 




:child_ids: Childs Sections, one2many



.. index::
  single: child_ids field
.. 




:package_product_id: Package Product, many2one



.. index::
  single: package_product_id field
.. 




:parent_id: Parent Section, many2one



.. index::
  single: parent_id field
.. 




:reply_to: Reply-To, char

    *The email address wich is the 'Reply-To' of all email sent by Open ERP for cases in this section*

.. index::
  single: reply_to field
.. 




:active: Active, boolean



.. index::
  single: active field
.. 



Object: Category of case
########################

.. index::
  single: Category of case object
.. 


:name: Case Category Name, char, required



.. index::
  single: name field
.. 




:probability: Probability (%), float, required



.. index::
  single: probability field
.. 




:section_id: Case Section, many2one



.. index::
  single: section_id field
.. 



Object: Case Rule
#################

.. index::
  single: Case Rule object
.. 


:trg_categ_id: Category, many2one



.. index::
  single: trg_categ_id field
.. 




:trg_section_id: Section, many2one



.. index::
  single: trg_section_id field
.. 




:sequence: Sequence, integer



.. index::
  single: sequence field
.. 




:act_remind_partner: Remind Partner, boolean

    *Check this if you want the rule to send a reminder by email to the partner.*

.. index::
  single: act_remind_partner field
.. 




:trg_date_range_type: Delay type, selection



.. index::
  single: trg_date_range_type field
.. 




:act_section_id: Set section to, many2one



.. index::
  single: act_section_id field
.. 




:trg_date_range: Delay after trigger date, integer



.. index::
  single: trg_date_range field
.. 




:act_remind_user: Remind responsible, boolean

    *Check this if you want the rule to send a reminder by email to the user.*

.. index::
  single: act_remind_user field
.. 




:trg_priority_from: Minimum Priority, selection



.. index::
  single: trg_priority_from field
.. 




:trg_date_type: Trigger Date, selection



.. index::
  single: trg_date_type field
.. 




:act_method: Call Object Method, char



.. index::
  single: act_method field
.. 




:act_email_cc: Add watchers (Cc), char

    *These people will receive a copy of the futur communication between partner and users by email*

.. index::
  single: act_email_cc field
.. 




:act_priority: Set priority to, selection



.. index::
  single: act_priority field
.. 




:trg_state_to: Button Pressed, selection



.. index::
  single: trg_state_to field
.. 




:act_mail_to_email: Mail to these emails, char



.. index::
  single: act_mail_to_email field
.. 




:act_remind_attach: Remind with attachment, boolean

    *Check this if you want that all documents attached to the case be attached to the reminder email sent.*

.. index::
  single: act_remind_attach field
.. 




:trg_user_id: Responsible, many2one



.. index::
  single: trg_user_id field
.. 




:act_state: Set state to, selection



.. index::
  single: act_state field
.. 




:act_mail_to_partner: Mail to partner, boolean



.. index::
  single: act_mail_to_partner field
.. 




:trg_priority_to: Maximim Priority, selection



.. index::
  single: trg_priority_to field
.. 




:active: Active, boolean



.. index::
  single: active field
.. 




:act_mail_to_watchers: Mail to watchers (Cc), boolean



.. index::
  single: act_mail_to_watchers field
.. 




:name: Rule Name, char, required



.. index::
  single: name field
.. 




:trg_state_from: Case State, selection



.. index::
  single: trg_state_from field
.. 




:act_user_id: Set responsible to, many2one



.. index::
  single: act_user_id field
.. 




:act_mail_to_user: Mail to responsible, boolean



.. index::
  single: act_mail_to_user field
.. 




:trg_partner_id: Partner, many2one



.. index::
  single: trg_partner_id field
.. 




:trg_partner_categ_id: Partner Category, many2one



.. index::
  single: trg_partner_categ_id field
.. 




:act_mail_body: Mail body, text



.. index::
  single: act_mail_body field
.. 



Object: Case
############

.. index::
  single: Case object
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




:date: Date, datetime



.. index::
  single: date field
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




:note: Note, text



.. index::
  single: note field
.. 




:timesheet_line_id: Timesheet Line, many2one



.. index::
  single: timesheet_line_id field
.. 




:user_id: Responsible, many2one



.. index::
  single: user_id field
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




:priority: Priority, selection



.. index::
  single: priority field
.. 




:state: Status, selection, readonly



.. index::
  single: state field
.. 




:case_id: Related Case, many2one



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




:description: Your action, text



.. index::
  single: description field
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




:section_id: Section, many2one, required



.. index::
  single: section_id field
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




:incoming_move_id: Incoming Move, many2one



.. index::
  single: incoming_move_id field
.. 




:active: Active, boolean



.. index::
  single: active field
.. 




:product_id: Related Product, many2one



.. index::
  single: product_id field
.. 




:stage_id: Stage, many2one



.. index::
  single: stage_id field
.. 




:incident_ref: Incident Ref, char, required



.. index::
  single: incident_ref field
.. 




:name: Description, char, required



.. index::
  single: name field
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




:picking_id: Repair Picking, many2one



.. index::
  single: picking_id field
.. 




:partner_phone: Phone, char



.. index::
  single: partner_phone field
.. 




:email_from: Partner Email, char



.. index::
  single: email_from field
.. 



Object: Case Communication History
##################################

.. index::
  single: Case Communication History object
.. 


:user_id: User Responsible, many2one, readonly



.. index::
  single: user_id field
.. 




:name: Action, char



.. index::
  single: name field
.. 




:canal_id: Channel, many2one



.. index::
  single: canal_id field
.. 




:som: State of Mind, many2one



.. index::
  single: som field
.. 




:section_id: Section, many2one



.. index::
  single: section_id field
.. 




:case_id: Case, many2one, required



.. index::
  single: case_id field
.. 




:date: Date, datetime



.. index::
  single: date field
.. 



Object: Case history
####################

.. index::
  single: Case history object
.. 


:description: Description, text



.. index::
  single: description field
.. 




:canal_id: Channel, many2one



.. index::
  single: canal_id field
.. 




:som: State of Mind, many2one



.. index::
  single: som field
.. 




:section_id: Section, many2one



.. index::
  single: section_id field
.. 




:date: Date, datetime



.. index::
  single: date field
.. 




:user_id: User Responsible, many2one, readonly



.. index::
  single: user_id field
.. 




:name: Action, char



.. index::
  single: name field
.. 




:log_id: Log, many2one



.. index::
  single: log_id field
.. 




:note: Description, text, readonly



.. index::
  single: note field
.. 




:case_id: Case, many2one, required



.. index::
  single: case_id field
.. 




:email: Email, char



.. index::
  single: email field
.. 



Object: Partner Segmentation
############################

.. index::
  single: Partner Segmentation object
.. 


:som_interval: Days per Periode, integer

    *A period is the average number of days between two cycle of sale or purchase for this segmentation. It's mainly used to detect if a partner has not purchased or buy for a too long time, so we suppose that his state of mind has decreased because he probably bought goods to another supplier. Use this functionnality for recurring businesses.*

.. index::
  single: som_interval field
.. 




:partner_id: Max Partner ID processed, integer



.. index::
  single: partner_id field
.. 




:description: Description, text



.. index::
  single: description field
.. 




:som_interval_max: Max Interval, integer

    *The computation is made on all events that occured during this interval, the past X periods.*

.. index::
  single: som_interval_max field
.. 




:child_ids: Childs profile, one2many



.. index::
  single: child_ids field
.. 




:som_interval_default: Default (0=None), float

    *Default state of mind for period preceeding the 'Max Interval' computation. This is the starting state of mind by default if the partner has no event.*

.. index::
  single: som_interval_default field
.. 




:answer_yes: Inclued answers, many2many



.. index::
  single: answer_yes field
.. 




:name: Name, char, required

    *The name of the segmentation.*

.. index::
  single: name field
.. 




:segmentation_line: Criteria, one2many, required



.. index::
  single: segmentation_line field
.. 




:profiling_active: Use The Profiling Rules, boolean

    *Check if you want to use this tab as part of the segmentation rule. If not checked, the criteria beneath will be ignored*

.. index::
  single: profiling_active field
.. 




:parent_id: Parent Profile, many2one



.. index::
  single: parent_id field
.. 




:state: Execution Status, selection, readonly



.. index::
  single: state field
.. 




:sales_purchase_active: Use The Sales Purchase Rules, boolean

    *Check if you want to use this tab as part of the segmentation rule. If not checked, the criteria beneath will be ignored*

.. index::
  single: sales_purchase_active field
.. 




:exclusif: Exclusive, boolean

    *Check if the category is limited to partners that match the segmentation criterions. If checked, remove the category from partners that doesn't match segmentation criterions*

.. index::
  single: exclusif field
.. 




:categ_id: Partner Category, many2one, required

    *The partner category that will be added to partners that match the segmentation criterions after computation.*

.. index::
  single: categ_id field
.. 




:som_interval_decrease: Decrease (0>1), float

    *If the partner has not purchased (or buied) during a period, decrease the state of mind by this factor. It's a multiplication*

.. index::
  single: som_interval_decrease field
.. 




:answer_no: Excluded answers, many2many



.. index::
  single: answer_no field
.. 



Object: Segmentation line
#########################

.. index::
  single: Segmentation line object
.. 


:expr_operator: Operator, selection, required



.. index::
  single: expr_operator field
.. 




:expr_value: Value, float, required



.. index::
  single: expr_value field
.. 




:expr_name: Control Variable, selection, required



.. index::
  single: expr_name field
.. 




:segmentation_id: Segmentation, many2one



.. index::
  single: segmentation_id field
.. 




:operator: Mandatory / Optionnal, selection, required



.. index::
  single: operator field
.. 




:name: Rule Name, char, required



.. index::
  single: name field
.. 

