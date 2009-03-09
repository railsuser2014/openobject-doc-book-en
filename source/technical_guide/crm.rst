
.. module:: crm
    :synopsis: Customer & Supplier Relationship Management (Official, Quality Certified)
    :noindex:
.. 

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

Customer & Supplier Relationship Management (*crm*)
===================================================
:Module: crm
:Name: Customer & Supplier Relationship Management
:Version: 5.0.1.0
:Author: Tiny
:Directory: crm
:Web: http://www.openerp.com
:Official module: yes
:Quality certified: yes

Description
-----------

::

  The generic Open ERP Customer Relationship Management system enables a group of people to 
  intelligently and efficiently manage leads, opportunities, tasks, issues, requests, bugs, campaign, 
  claims, etc.
  It manages key tasks such as communication, identification, prioritization, assignment, 
  resolution and notification.
  
  Open ERP ensures that all cases are successfully tracked by users, customers and suppliers. 
  It can automatically send reminders, escalate the request, trigger specific methods and lots of others 
  actions based on your enterprise own rules.
  
  The greatest thing about this system is that users don't need to do anything special. 
  They can just send email to the request tracker. 
  Open ERP will take care of thanking them for their message, automatically routing it to the appropriate 
  staff, and making sure all future correspondence gets to the right place.
  
  The CRM module has a email gateway for the synchronisation interface
  between mails and Open ERP.

Dependencies
------------

 * :mod:`base`

Reports
-------

 * Business Opportunities

Menus
-------

 * CRM & SRM
 * CRM & SRM/Configuration
 * CRM & SRM/Configuration/Cases
 * CRM & SRM/Configuration/Cases/Sections
 * CRM & SRM/Reporting/All Cases
 * CRM & SRM/Reporting/All Cases/Cases by section
 * CRM & SRM/Configuration/Cases/Categories
 * CRM & SRM/Configuration/Cases/Rules
 * CRM & SRM/Reporting/All Cases/All Cases
 * CRM & SRM/Reporting/All Cases/All Cases/Open Cases
 * CRM & SRM/Reporting/All Cases/My cases
 * CRM & SRM/Reporting/All Cases/My cases/My Open Cases
 * CRM & SRM/Reporting/All Cases/Cases Histories
 * CRM & SRM/Reporting/All Cases/Cases Histories/All Histories
 * CRM & SRM/Reporting/All Cases/Cases Histories/My Histories
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

Object: Case Section (crm.case.section)
#######################################



:analytic_account_id: Main Analytic Account, many2one





:code: Section Code, char





:user_id: Responsible, many2one





:name: Case Section, char, required





:sequence: Sequence, integer





:analytic_journal_id: Analytic Journal, many2one





:child_ids: Childs Sections, one2many





:package_product_id: Package Product, many2one





:parent_id: Parent Section, many2one





:reply_to: Reply-To, char

    *The email address wich is the 'Reply-To' of all email sent by Open ERP for cases in this section*



:active: Active, boolean




Object: Category of case (crm.case.categ)
#########################################



:name: Case Category Name, char, required





:probability: Probability (%), float, required





:section_id: Case Section, many2one




Object: Case Rule (crm.case.rule)
#################################



:trg_categ_id: Category, many2one





:trg_section_id: Section, many2one





:sequence: Sequence, integer





:act_remind_partner: Remind Partner, boolean

    *Check this if you want the rule to send a reminder by email to the partner.*



:trg_date_range_type: Delay type, selection





:act_section_id: Set section to, many2one





:trg_date_range: Delay after trigger date, integer





:act_remind_user: Remind responsible, boolean

    *Check this if you want the rule to send a reminder by email to the user.*



:trg_priority_from: Minimum Priority, selection





:trg_date_type: Trigger Date, selection





:act_method: Call Object Method, char





:act_email_cc: Add watchers (Cc), char

    *These people will receive a copy of the futur communication between partner and users by email*



:act_priority: Set priority to, selection





:trg_state_to: Button Pressed, selection





:act_mail_to_email: Mail to these emails, char





:act_remind_attach: Remind with attachment, boolean

    *Check this if you want that all documents attached to the case be attached to the reminder email sent.*



:trg_user_id: Responsible, many2one





:act_state: Set state to, selection





:act_mail_to_partner: Mail to partner, boolean





:trg_priority_to: Maximim Priority, selection





:active: Active, boolean





:act_mail_to_watchers: Mail to watchers (Cc), boolean





:name: Rule Name, char, required





:trg_state_from: Case State, selection





:act_user_id: Set responsible to, many2one





:act_mail_to_user: Mail to responsible, boolean





:trg_partner_id: Partner, many2one





:trg_partner_categ_id: Partner Category, many2one





:act_mail_body: Mail body, text




Object: Case (crm.case)
#######################



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





:date: Date, datetime





:fleet_id: Fleet, many2one





:category2_id: Category Name, many2one





:in_supplier_move_id: Return To Supplier Move, many2one





:duration: Duration, float





:event_ids: Events, many2many





:partner_id: Partner, many2one





:id: ID, integer, readonly





:date_action_next: Next Action, datetime, readonly





:note: Note, text





:timesheet_line_id: Timesheet Line, many2one





:user_id: Responsible, many2one





:partner_name: Employee Name, char





:planned_revenue: Planned Revenue, float





:meeting_id: Meeting confidential, many2one





:priority: Priority, selection





:state: Status, selection, readonly





:case_id: Related Case, many2one





:outgoing_move_id: Outgoing Move, many2one





:email_cc: Watchers Emails, char





:external_ref: Ticket Code, char





:ref: Reference, reference





:log_ids: Logs History, one2many, readonly





:description: Your action, text





:date_action_last: Last Action, datetime, readonly





:planned_cost: Planned Costs, float





:ref2: Reference 2, reference





:section_id: Section, many2one, required





:prodlot_id: Serial Number, many2one





:partner_name2: Employee Email, char





:partner_mobile: Mobile, char





:incoming_move_id: Incoming Move, many2one





:active: Active, boolean





:product_id: Related Product, many2one





:stage_id: Stage, many2one





:incident_ref: Incident Ref, char, required





:name: Description, char, required





:date_deadline: Deadline, datetime





:out_supplier_move_id: Return From Supplier Move, many2one





:email_last: Latest E-Mail, text, readonly





:grant_id: Grant, many2one





:is_fleet_expired: Is Fleet Expired?, boolean





:categ_id: Category, many2one





:picking_id: Repair Picking, many2one





:partner_phone: Phone, char





:email_from: Partner Email, char




Object: Case Communication History (crm.case.log)
#################################################



:user_id: User Responsible, many2one, readonly





:name: Action, char





:canal_id: Channel, many2one





:som: State of Mind, many2one





:section_id: Section, many2one





:case_id: Case, many2one, required





:date: Date, datetime




Object: Case history (crm.case.history)
#######################################



:description: Description, text





:canal_id: Channel, many2one





:som: State of Mind, many2one





:section_id: Section, many2one





:date: Date, datetime





:user_id: User Responsible, many2one, readonly





:name: Action, char





:log_id: Log, many2one





:note: Description, text, readonly





:case_id: Case, many2one, required





:email: Email, char




Object: Partner Segmentation (crm.segmentation)
###############################################



:som_interval: Days per Periode, integer

    *A period is the average number of days between two cycle of sale or purchase for this segmentation. It's mainly used to detect if a partner has not purchased or buy for a too long time, so we suppose that his state of mind has decreased because he probably bought goods to another supplier. Use this functionnality for recurring businesses.*



:partner_id: Max Partner ID processed, integer





:description: Description, text





:som_interval_max: Max Interval, integer

    *The computation is made on all events that occured during this interval, the past X periods.*



:child_ids: Childs profile, one2many





:som_interval_default: Default (0=None), float

    *Default state of mind for period preceeding the 'Max Interval' computation. This is the starting state of mind by default if the partner has no event.*



:answer_yes: Inclued answers, many2many





:name: Name, char, required

    *The name of the segmentation.*



:segmentation_line: Criteria, one2many, required





:profiling_active: Use The Profiling Rules, boolean

    *Check if you want to use this tab as part of the segmentation rule. If not checked, the criteria beneath will be ignored*



:parent_id: Parent Profile, many2one





:state: Execution Status, selection, readonly





:sales_purchase_active: Use The Sales Purchase Rules, boolean

    *Check if you want to use this tab as part of the segmentation rule. If not checked, the criteria beneath will be ignored*



:exclusif: Exclusive, boolean

    *Check if the category is limited to partners that match the segmentation criterions. If checked, remove the category from partners that doesn't match segmentation criterions*



:categ_id: Partner Category, many2one, required

    *The partner category that will be added to partners that match the segmentation criterions after computation.*



:som_interval_decrease: Decrease (0>1), float

    *If the partner has not purchased (or buied) during a period, decrease the state of mind by this factor. It's a multiplication*



:answer_no: Excluded answers, many2many




Object: Segmentation line (crm.segmentation.line)
#################################################



:expr_operator: Operator, selection, required





:expr_value: Value, float, required





:expr_name: Control Variable, selection, required





:segmentation_id: Segmentation, many2one





:operator: Mandatory / Optionnal, selection, required





:name: Rule Name, char, required


