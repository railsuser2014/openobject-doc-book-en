
.. module:: cci_mission
    :synopsis: CCI mission
    :noindex:
.. 

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

CCI mission (*cci_mission*)
===========================
:Module: cci_mission
:Name: CCI mission
:Version: 5.0.1.0
:Directory: cci_mission
:Web: http://www.openerp.com
:Is certified: no

Description
-----------

::

  specific module for cci project.

Dependencies
------------

 * :mod:`base`
 * :mod:`crm`
 * :mod:`cci_partner`
 * :mod:`product`
 * :mod:`membership`
 * :mod:`sale`
 * :mod:`cci_event`
 * :mod:`cci_account`
 * :mod:`cci_translation`
 * :mod:`cci_country`

Reports
-------

None


Menus
-------

 * Missions
 * Missions/Configuration/Dossier Types
 * Missions/Configuration/Site
 * Missions/Configuration/Search Entries/Dossier
 * Missions/Embassy Folder
 * Missions/Configuration/Search Entries/Embassy Folder Lines
 * Missions/Configuration/Custom Codes
 * Missions/Legalizations
 * Missions/Certificates
 * Missions/Configuration/ATA Usage
 * Missions/Configuration/Search Entries/Letters Log
 * Missions/ATA Carnet
 * Missions/Incompleted Certificates
 * Financial Management/Periodical Processing/Group Draft Invoices for Missions and Events

Views
-----

 * \* INHERIT res.partner.form (form)
 * cci_missions.dossier_type.form (form)
 * cci_missions.dossier_type.tree (tree)
 * cci_missions.site.form (form)
 * cci_missions.site.tree (tree)
 * cci_missions.dossier.form (form)
 * cci_missions.dossier.tree (tree)
 * cci_missions.embassy_folder.form (form)
 * cci_missions.embassy_folder.tree (tree)
 * cci_missions.embassy_folder_line.form (form)
 * cci_missions.embassy_folder_line.tree (tree)
 * cci_missions.custom_code.form (form)
 * cci_missions.custom_code.tree (tree)
 * cci_missions.legalization.form (form)
 * cci_missions.legalization.tree (tree)
 * cci_missions.certificate.form (form)
 * cci_missions.certificate.tree (tree)
 * cci_missions.ata_usage.form (form)
 * cci_missions.ata_usage.tree (tree)
 * cci_missions.letters_log.form (form)
 * cci_missions.letters_log.tree (tree)
 * cci_missions.ata_carnet.form (form)
 * cci_missions.ata_carnet.tree (tree)
 * product.lines.tree (tree)
 * product.lines.form (form)


Objects
-------

Object: cci_missions.site (cci_missions.site)
#############################################



:name: Name of the Site, char, required





:embassy_sequence_id: Sequence for Embassy Folder, many2one, required





:official_name_4: Official Name of the Site, char





:official_name_1: Official Name of the Site, char, required





:official_name_3: Official Name of the Site, char





:official_name_2: Official Name of the Site, char




Object: cci_missions.embassy_folder (cci_missions.embassy_folder)
#################################################################



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





:customer_reference: Folders Reference for the Customer, char





:member_price: Member Price Allowed, boolean





:incoming_move_id: Incoming Move, many2one





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





:partner_name: Employee Name, char





:planned_revenue: Planned Revenue, float





:embassy_folder_line_ids: Details, one2many





:meeting_id: Meeting confidential, many2one





:note: Note, text





:state: Status, selection, readonly





:case_id: Related Case, many2one





:site_id: Site, many2one, required





:outgoing_move_id: Outgoing Move, many2one





:email_cc: Watchers Emails, char





:external_ref: Ticket Code, char





:ref: Reference, reference





:log_ids: Logs History, one2many, readonly





:description: Your action, text





:date_action_last: Last Action, datetime, readonly





:planned_cost: Planned Costs, float





:ref2: Reference 2, reference





:invoice_date: Invoice Date, datetime, readonly





:section_id: Section, many2one, required





:internal_note: Internal Note, text





:prodlot_id: Serial Number, many2one





:partner_name2: Employee Email, char





:partner_mobile: Mobile, char





:destination_id: Destination Country, many2one





:date: Date, datetime





:active: Active, boolean





:name: Description, char, required





:stage_id: Stage, many2one





:link_ids: Linked Documents, one2many





:incident_ref: Incident Ref, char, required





:product_id: Related Product, many2one





:date_deadline: Deadline, datetime





:out_supplier_move_id: Return From Supplier Move, many2one





:email_last: Latest E-Mail, text, readonly





:grant_id: Grant, many2one





:is_fleet_expired: Is Fleet Expired?, boolean





:categ_id: Category, many2one





:email_from: Partner Email, char





:partner_phone: Phone, char





:invoice_id: Invoice, many2one





:invoice_note: Note to Display on the Invoice, text

    *to display as the last embassy_folder_line of this embassy_folder.*



:picking_id: Repair Picking, many2one





:crm_case_id: Case, many2one




Object: cci_missions.embassy_folder_line  (cci_missions.embassy_folder_line)
############################################################################



:awex_amount: AWEX Amount, float, readonly





:credit_line_id: Credit Line, many2one, readonly





:name: Description, char, required





:customer_amount: Invoiced Amount, float





:account_id: Account, many2one, required





:awex_eligible: AWEX Eligible, boolean





:tax_rate: Tax Rate, many2one





:folder_id: Related Embassy Folder, many2one, required





:type: Type, selection, required





:courier_cost: Couriers Costs, float




Object: cci_missions.dossier_type (cci_missions.dossier_type)
#############################################################



:code: Code, char, required





:name: Description, char, required





:copy_product_id: Reference for Copies, many2one, required

    *for the association with a pricelist*



:id_letter: ID Letter, char

    *for identify the type of certificate by the federation*



:section: Type, selection, required





:site_id: Site, many2one, required





:sequence_id: Sequence, many2one, required

    *for association with a sequence*



:warranty_product_2: Warranty product for ATA carnet if not own Risk, many2one





:warranty_product_1: Warranty product for ATA carnet if Own Risk, many2one





:original_product_id: Reference for Original Copies, many2one, required

    *for the association with a pricelist*


Object: cci_missions.dossier (cci_missions.dossier)
###################################################



:goods: Goods Description, char





:embassy_folder_id: Related Embassy Folder, many2one





:name: Reference, char, required





:quantity_original: Quantity of Originals, integer, required





:type_id: Dossier Type, many2one, required





:sender_name: Sender Name, char





:invoiced_amount: Total, float





:sub_total: Sub Total for Extra Products, float, readonly





:order_partner_id: Billed Customer, many2one, required





:to_bill: To Be Billed, boolean





:state: State, selection





:product_ids: Products, one2many





:destination_id: Destination Country, many2one





:invoice_id: Invoice, many2one





:date: Creation Date, date, required





:quantity_copies: Number of Copies, integer





:text_on_invoice: Text to Display on the Invoice, text





:id: ID, integer, readonly





:asker_name: Asker Name, char





:goods_value: Value of the Sold Goods, float




Object: cci_missions.custom_code (cci_missions.custom_code)
###########################################################



:meaning: Meaning, text, required





:official: Official Code, boolean





:name: Name, char, required




Object: cci_missions.certificate (cci_missions.certificate)
###########################################################



:embassy_folder_id: Related Embassy Folder, many2one





:legalization_ids: Related Legalizations, one2many





:type_id: Dossier Type, many2one, required





:sender_name: Sender Name, char





:invoiced_amount: Total, float





:asker_name: Asker Name, char





:sub_total: Sub Total for Extra Products, float, readonly





:asker_zip_id: Asker Zip Code, many2one





:asker_address: Asker Address, char





:origin_ids: Origin Countries, many2many





:destination_id: Destination Country, many2one





:date: Creation Date, date, required





:total: Total, float, readonly





:text_on_invoice: Text to Display on the Invoice, text





:id: ID, integer, readonly





:special_reason: For special cases, selection





:goods: Goods Description, char





:name: Reference, char, required





:quantity_original: Quantity of Originals, integer, required





:invoice_id: Invoice, many2one





:customs_ids: Custom Codes, many2many





:state: State, selection





:dossier_id: Dossier, many2one





:order_partner_id: Billed Customer, many2one, required





:sending_spf: SPF Sending Date, date

    *Date of the sending of this record to the external database*



:quantity_copies: Number of Copies, integer





:goods_value: Value of the Sold Goods, float





:to_bill: To Be Billed, boolean





:product_ids: Products, one2many




Object: cci_missions.legalization (cci_missions.legalization)
#############################################################



:embassy_folder_id: Related Embassy Folder, many2one





:type_id: Dossier Type, many2one, required





:sender_name: Sender Name, char





:invoiced_amount: Total, float





:asker_name: Asker Name, char





:sub_total: Sub Total for Extra Products, float, readonly





:partner_member_state: Member State of the Partner, selection, readonly





:member_price: Apply the Member Price, boolean





:destination_id: Destination Country, many2one





:date: Creation Date, date, required





:total: Total, float, readonly





:text_on_invoice: Text to Display on the Invoice, text





:id: ID, integer, readonly





:goods: Goods Description, char





:name: Reference, char, required





:quantity_original: Quantity of Originals, integer, required





:invoice_id: Invoice, many2one





:state: State, selection





:dossier_id: Dossier, many2one





:order_partner_id: Billed Customer, many2one, required





:certificate_id: Related Certificate, many2one





:quantity_copies: Number of Copies, integer





:goods_value: Value of the Sold Goods, float





:to_bill: To Be Billed, boolean





:product_ids: Products, one2many




Object: cci_missions.courier_log (cci_missions.courier_log)
###########################################################



:documents_certificate: List of Certificates, text





:embassy_folder_id: Related Embassy Folder, many2one, required





:qtty_to_print: Number of Sheets, integer





:copy_cba: Photocopy Before CBA, boolean





:cba: CBA, boolean





:message: Message to the Courier, text





:address_street: Street, char





:documents: Number of Documents to Legalize, integer





:address_name_1: Company Name, char





:address_name_2: Contact Name, char





:consulate_name: Consulate Name, char





:documents_invoice: List of Invoices, text





:partner_address_id: Courier, many2one





:copy_ministry: Photocopy Before Ministry, boolean





:others: Others, char





:translation: Translation, boolean





:address_city: City, char





:ministry: Ministry, boolean





:return_address: Address of Return, selection, required





:embassy_name: Embassy Name, char





:documents_others: Others, text





:copy_embassy_consulate: Photocopy Before Embassy or Consulate, boolean




Object: cci_missions.ata_usage (cci_missions.ata_usage)
#######################################################



:name: Usage, char, required




Object: cci_missions.ata_carnet (cci_missions.ata_carnet)
#########################################################



:warranty: Warranty, float, readonly





:area_id: Area, many2one, required





:type_id: Related Type of Carnet, many2one, required





:member_price: Apply the Member Price, boolean





:partner_member_state: Member State of the Partner, selection, readonly





:creation_date: Emission Date, date, required





:ok_state_date: Date of Closure, date





:partner_id: Partner, many2one, required





:id: ID, integer, readonly





:usage_id: Usage, many2one, required





:federation_sending_date: Date of Sending to the Federation, date, readonly





:representer_name: Representer Name, char





:representer_city: Representer City, char





:warranty_product_id: Related Warranty Product, many2one, required





:initial_pages: Initial Number of Pages, integer, required





:state: State, selection, required, readonly





:representer_address: Representer Address, char





:insurer_agreement: Insurer Agreement, char





:double_signature: Double Signature, boolean





:additional_pages: Additional Number of Pages, integer





:goods_value: Goods Value, float, required





:holder_name: Holder Name, char





:sub_total: Subtotal of Extra Products, float, readonly





:validity_date: Validity Date, date, required





:holder_city: Holder City, char





:product_ids: Products, one2many





:name: Name, char, required





:letter_ids: Letters, one2many





:goods: Goods, char





:holder_address: Holder Address, char





:invoice_id: Invoice, many2one





:partner_insurer_id: Insurer ID of the Partner, float, readonly





:return_date: Date of Return, date





:own_risk: Own Risks, boolean




Object: cci_missions.letters_log (cci_missions.letters_log)
###########################################################



:date: Date of Sending, date, required





:letter_type: Type of Letter, selection, required





:ata_carnet_id: Related ATA Carnet, many2one, required




Object: Product Lines (product.lines)
#####################################



:uos_id: Unit, many2one





:name: Description, char, required





:product_line_id: Product Ref, many2one





:price_unit: Unit Price, float, required





:price_subtotal: Subtotal, float, readonly





:account_id: Account, many2one, required





:dossier_product_line_id: Product Ref, many2one





:product_id: Product, many2one, required





:quantity: Quantity, float, required


