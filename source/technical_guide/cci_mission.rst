
Module CCI mission (*cci_mission*)
==================================
:Module: cci_mission
:Name: CCI mission
:Version: 5.0.1.0
:Directory: cci_mission
:Web: http://www.openerp.com

Description
-----------

::

  specific module for cci project.

Dependencies
------------

 * base - installed
 * crm - installed
 * cci_partner - installed
 * product - installed
 * membership - installed
 * sale - installed
 * cci_event - installed
 * cci_account - installed
 * cci_translation - installed
 * cci_country - installed

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

Object: cci_missions.site
#########################

.. index::
  single: cci_missions.site object
.. 


:name: Name of the Site, char, required



.. index::
  single: name field
.. 




:embassy_sequence_id: Sequence for Embassy Folder, many2one, required



.. index::
  single: embassy_sequence_id field
.. 




:official_name_4: Official Name of the Site, char



.. index::
  single: official_name_4 field
.. 




:official_name_1: Official Name of the Site, char, required



.. index::
  single: official_name_1 field
.. 




:official_name_3: Official Name of the Site, char



.. index::
  single: official_name_3 field
.. 




:official_name_2: Official Name of the Site, char



.. index::
  single: official_name_2 field
.. 



Object: cci_missions.embassy_folder
###################################

.. index::
  single: cci_missions.embassy_folder object
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




:customer_reference: Folders Reference for the Customer, char



.. index::
  single: customer_reference field
.. 




:member_price: Member Price Allowed, boolean



.. index::
  single: member_price field
.. 




:incoming_move_id: Incoming Move, many2one



.. index::
  single: incoming_move_id field
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




:partner_name: Employee Name, char



.. index::
  single: partner_name field
.. 




:planned_revenue: Planned Revenue, float



.. index::
  single: planned_revenue field
.. 




:embassy_folder_line_ids: Details, one2many



.. index::
  single: embassy_folder_line_ids field
.. 




:meeting_id: Meeting confidential, many2one



.. index::
  single: meeting_id field
.. 




:note: Note, text



.. index::
  single: note field
.. 




:state: Status, selection, readonly



.. index::
  single: state field
.. 




:case_id: Related Case, many2one



.. index::
  single: case_id field
.. 




:site_id: Site, many2one, required



.. index::
  single: site_id field
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




:invoice_date: Invoice Date, datetime, readonly



.. index::
  single: invoice_date field
.. 




:section_id: Section, many2one, required



.. index::
  single: section_id field
.. 




:internal_note: Internal Note, text



.. index::
  single: internal_note field
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




:destination_id: Destination Country, many2one



.. index::
  single: destination_id field
.. 




:date: Date, datetime



.. index::
  single: date field
.. 




:active: Active, boolean



.. index::
  single: active field
.. 




:name: Description, char, required



.. index::
  single: name field
.. 




:stage_id: Stage, many2one



.. index::
  single: stage_id field
.. 




:link_ids: Linked Documents, one2many



.. index::
  single: link_ids field
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




:partner_phone: Phone, char



.. index::
  single: partner_phone field
.. 




:invoice_id: Invoice, many2one



.. index::
  single: invoice_id field
.. 




:invoice_note: Note to Display on the Invoice, text

    *to display as the last embassy_folder_line of this embassy_folder.*

.. index::
  single: invoice_note field
.. 




:picking_id: Repair Picking, many2one



.. index::
  single: picking_id field
.. 




:crm_case_id: Case, many2one



.. index::
  single: crm_case_id field
.. 



Object: cci_missions.embassy_folder_line 
#########################################

.. index::
  single: cci_missions.embassy_folder_line  object
.. 


:awex_amount: AWEX Amount, float, readonly



.. index::
  single: awex_amount field
.. 




:credit_line_id: Credit Line, many2one, readonly



.. index::
  single: credit_line_id field
.. 




:name: Description, char, required



.. index::
  single: name field
.. 




:customer_amount: Invoiced Amount, float



.. index::
  single: customer_amount field
.. 




:account_id: Account, many2one, required



.. index::
  single: account_id field
.. 




:awex_eligible: AWEX Eligible, boolean



.. index::
  single: awex_eligible field
.. 




:tax_rate: Tax Rate, many2one



.. index::
  single: tax_rate field
.. 




:folder_id: Related Embassy Folder, many2one, required



.. index::
  single: folder_id field
.. 




:type: Type, selection, required



.. index::
  single: type field
.. 




:courier_cost: Couriers Costs, float



.. index::
  single: courier_cost field
.. 



Object: cci_missions.dossier_type
#################################

.. index::
  single: cci_missions.dossier_type object
.. 


:code: Code, char, required



.. index::
  single: code field
.. 




:name: Description, char, required



.. index::
  single: name field
.. 




:copy_product_id: Reference for Copies, many2one, required

    *for the association with a pricelist*

.. index::
  single: copy_product_id field
.. 




:id_letter: ID Letter, char

    *for identify the type of certificate by the federation*

.. index::
  single: id_letter field
.. 




:section: Type, selection, required



.. index::
  single: section field
.. 




:site_id: Site, many2one, required



.. index::
  single: site_id field
.. 




:sequence_id: Sequence, many2one, required

    *for association with a sequence*

.. index::
  single: sequence_id field
.. 




:warranty_product_2: Warranty product for ATA carnet if not own Risk, many2one



.. index::
  single: warranty_product_2 field
.. 




:warranty_product_1: Warranty product for ATA carnet if Own Risk, many2one



.. index::
  single: warranty_product_1 field
.. 




:original_product_id: Reference for Original Copies, many2one, required

    *for the association with a pricelist*

.. index::
  single: original_product_id field
.. 



Object: cci_missions.dossier
############################

.. index::
  single: cci_missions.dossier object
.. 


:goods: Goods Description, char



.. index::
  single: goods field
.. 




:embassy_folder_id: Related Embassy Folder, many2one



.. index::
  single: embassy_folder_id field
.. 




:name: Reference, char, required



.. index::
  single: name field
.. 




:quantity_original: Quantity of Originals, integer, required



.. index::
  single: quantity_original field
.. 




:type_id: Dossier Type, many2one, required



.. index::
  single: type_id field
.. 




:sender_name: Sender Name, char



.. index::
  single: sender_name field
.. 




:invoiced_amount: Total, float



.. index::
  single: invoiced_amount field
.. 




:sub_total: Sub Total for Extra Products, float, readonly



.. index::
  single: sub_total field
.. 




:order_partner_id: Billed Customer, many2one, required



.. index::
  single: order_partner_id field
.. 




:to_bill: To Be Billed, boolean



.. index::
  single: to_bill field
.. 




:state: State, selection



.. index::
  single: state field
.. 




:product_ids: Products, one2many



.. index::
  single: product_ids field
.. 




:destination_id: Destination Country, many2one



.. index::
  single: destination_id field
.. 




:invoice_id: Invoice, many2one



.. index::
  single: invoice_id field
.. 




:date: Creation Date, date, required



.. index::
  single: date field
.. 




:quantity_copies: Number of Copies, integer



.. index::
  single: quantity_copies field
.. 




:text_on_invoice: Text to Display on the Invoice, text



.. index::
  single: text_on_invoice field
.. 




:id: ID, integer, readonly



.. index::
  single: id field
.. 




:asker_name: Asker Name, char



.. index::
  single: asker_name field
.. 




:goods_value: Value of the Sold Goods, float



.. index::
  single: goods_value field
.. 



Object: cci_missions.custom_code
################################

.. index::
  single: cci_missions.custom_code object
.. 


:meaning: Meaning, text, required



.. index::
  single: meaning field
.. 




:official: Official Code, boolean



.. index::
  single: official field
.. 




:name: Name, char, required



.. index::
  single: name field
.. 



Object: cci_missions.certificate
################################

.. index::
  single: cci_missions.certificate object
.. 


:embassy_folder_id: Related Embassy Folder, many2one



.. index::
  single: embassy_folder_id field
.. 




:legalization_ids: Related Legalizations, one2many



.. index::
  single: legalization_ids field
.. 




:type_id: Dossier Type, many2one, required



.. index::
  single: type_id field
.. 




:sender_name: Sender Name, char



.. index::
  single: sender_name field
.. 




:invoiced_amount: Total, float



.. index::
  single: invoiced_amount field
.. 




:asker_name: Asker Name, char



.. index::
  single: asker_name field
.. 




:sub_total: Sub Total for Extra Products, float, readonly



.. index::
  single: sub_total field
.. 




:asker_zip_id: Asker Zip Code, many2one



.. index::
  single: asker_zip_id field
.. 




:asker_address: Asker Address, char



.. index::
  single: asker_address field
.. 




:origin_ids: Origin Countries, many2many



.. index::
  single: origin_ids field
.. 




:destination_id: Destination Country, many2one



.. index::
  single: destination_id field
.. 




:date: Creation Date, date, required



.. index::
  single: date field
.. 




:total: Total, float, readonly



.. index::
  single: total field
.. 




:text_on_invoice: Text to Display on the Invoice, text



.. index::
  single: text_on_invoice field
.. 




:id: ID, integer, readonly



.. index::
  single: id field
.. 




:special_reason: For special cases, selection



.. index::
  single: special_reason field
.. 




:goods: Goods Description, char



.. index::
  single: goods field
.. 




:name: Reference, char, required



.. index::
  single: name field
.. 




:quantity_original: Quantity of Originals, integer, required



.. index::
  single: quantity_original field
.. 




:invoice_id: Invoice, many2one



.. index::
  single: invoice_id field
.. 




:customs_ids: Custom Codes, many2many



.. index::
  single: customs_ids field
.. 




:state: State, selection



.. index::
  single: state field
.. 




:dossier_id: Dossier, many2one



.. index::
  single: dossier_id field
.. 




:order_partner_id: Billed Customer, many2one, required



.. index::
  single: order_partner_id field
.. 




:sending_spf: SPF Sending Date, date

    *Date of the sending of this record to the external database*

.. index::
  single: sending_spf field
.. 




:quantity_copies: Number of Copies, integer



.. index::
  single: quantity_copies field
.. 




:goods_value: Value of the Sold Goods, float



.. index::
  single: goods_value field
.. 




:to_bill: To Be Billed, boolean



.. index::
  single: to_bill field
.. 




:product_ids: Products, one2many



.. index::
  single: product_ids field
.. 



Object: cci_missions.legalization
#################################

.. index::
  single: cci_missions.legalization object
.. 


:embassy_folder_id: Related Embassy Folder, many2one



.. index::
  single: embassy_folder_id field
.. 




:type_id: Dossier Type, many2one, required



.. index::
  single: type_id field
.. 




:sender_name: Sender Name, char



.. index::
  single: sender_name field
.. 




:invoiced_amount: Total, float



.. index::
  single: invoiced_amount field
.. 




:asker_name: Asker Name, char



.. index::
  single: asker_name field
.. 




:sub_total: Sub Total for Extra Products, float, readonly



.. index::
  single: sub_total field
.. 




:partner_member_state: Member State of the Partner, selection, readonly



.. index::
  single: partner_member_state field
.. 




:member_price: Apply the Member Price, boolean



.. index::
  single: member_price field
.. 




:destination_id: Destination Country, many2one



.. index::
  single: destination_id field
.. 




:date: Creation Date, date, required



.. index::
  single: date field
.. 




:total: Total, float, readonly



.. index::
  single: total field
.. 




:text_on_invoice: Text to Display on the Invoice, text



.. index::
  single: text_on_invoice field
.. 




:id: ID, integer, readonly



.. index::
  single: id field
.. 




:goods: Goods Description, char



.. index::
  single: goods field
.. 




:name: Reference, char, required



.. index::
  single: name field
.. 




:quantity_original: Quantity of Originals, integer, required



.. index::
  single: quantity_original field
.. 




:invoice_id: Invoice, many2one



.. index::
  single: invoice_id field
.. 




:state: State, selection



.. index::
  single: state field
.. 




:dossier_id: Dossier, many2one



.. index::
  single: dossier_id field
.. 




:order_partner_id: Billed Customer, many2one, required



.. index::
  single: order_partner_id field
.. 




:certificate_id: Related Certificate, many2one



.. index::
  single: certificate_id field
.. 




:quantity_copies: Number of Copies, integer



.. index::
  single: quantity_copies field
.. 




:goods_value: Value of the Sold Goods, float



.. index::
  single: goods_value field
.. 




:to_bill: To Be Billed, boolean



.. index::
  single: to_bill field
.. 




:product_ids: Products, one2many



.. index::
  single: product_ids field
.. 



Object: cci_missions.courier_log
################################

.. index::
  single: cci_missions.courier_log object
.. 


:documents_certificate: List of Certificates, text



.. index::
  single: documents_certificate field
.. 




:embassy_folder_id: Related Embassy Folder, many2one, required



.. index::
  single: embassy_folder_id field
.. 




:qtty_to_print: Number of Sheets, integer



.. index::
  single: qtty_to_print field
.. 




:copy_cba: Photocopy Before CBA, boolean



.. index::
  single: copy_cba field
.. 




:cba: CBA, boolean



.. index::
  single: cba field
.. 




:message: Message to the Courier, text



.. index::
  single: message field
.. 




:address_street: Street, char



.. index::
  single: address_street field
.. 




:documents: Number of Documents to Legalize, integer



.. index::
  single: documents field
.. 




:address_name_1: Company Name, char



.. index::
  single: address_name_1 field
.. 




:address_name_2: Contact Name, char



.. index::
  single: address_name_2 field
.. 




:consulate_name: Consulate Name, char



.. index::
  single: consulate_name field
.. 




:documents_invoice: List of Invoices, text



.. index::
  single: documents_invoice field
.. 




:partner_address_id: Courier, many2one



.. index::
  single: partner_address_id field
.. 




:copy_ministry: Photocopy Before Ministry, boolean



.. index::
  single: copy_ministry field
.. 




:others: Others, char



.. index::
  single: others field
.. 




:translation: Translation, boolean



.. index::
  single: translation field
.. 




:address_city: City, char



.. index::
  single: address_city field
.. 




:ministry: Ministry, boolean



.. index::
  single: ministry field
.. 




:return_address: Address of Return, selection, required



.. index::
  single: return_address field
.. 




:embassy_name: Embassy Name, char



.. index::
  single: embassy_name field
.. 




:documents_others: Others, text



.. index::
  single: documents_others field
.. 




:copy_embassy_consulate: Photocopy Before Embassy or Consulate, boolean



.. index::
  single: copy_embassy_consulate field
.. 



Object: cci_missions.ata_usage
##############################

.. index::
  single: cci_missions.ata_usage object
.. 


:name: Usage, char, required



.. index::
  single: name field
.. 



Object: cci_missions.ata_carnet
###############################

.. index::
  single: cci_missions.ata_carnet object
.. 


:warranty: Warranty, float, readonly



.. index::
  single: warranty field
.. 




:area_id: Area, many2one, required



.. index::
  single: area_id field
.. 




:type_id: Related Type of Carnet, many2one, required



.. index::
  single: type_id field
.. 




:member_price: Apply the Member Price, boolean



.. index::
  single: member_price field
.. 




:partner_member_state: Member State of the Partner, selection, readonly



.. index::
  single: partner_member_state field
.. 




:creation_date: Emission Date, date, required



.. index::
  single: creation_date field
.. 




:ok_state_date: Date of Closure, date



.. index::
  single: ok_state_date field
.. 




:partner_id: Partner, many2one, required



.. index::
  single: partner_id field
.. 




:id: ID, integer, readonly



.. index::
  single: id field
.. 




:usage_id: Usage, many2one, required



.. index::
  single: usage_id field
.. 




:federation_sending_date: Date of Sending to the Federation, date, readonly



.. index::
  single: federation_sending_date field
.. 




:representer_name: Representer Name, char



.. index::
  single: representer_name field
.. 




:representer_city: Representer City, char



.. index::
  single: representer_city field
.. 




:warranty_product_id: Related Warranty Product, many2one, required



.. index::
  single: warranty_product_id field
.. 




:initial_pages: Initial Number of Pages, integer, required



.. index::
  single: initial_pages field
.. 




:state: State, selection, required, readonly



.. index::
  single: state field
.. 




:representer_address: Representer Address, char



.. index::
  single: representer_address field
.. 




:insurer_agreement: Insurer Agreement, char



.. index::
  single: insurer_agreement field
.. 




:double_signature: Double Signature, boolean



.. index::
  single: double_signature field
.. 




:additional_pages: Additional Number of Pages, integer



.. index::
  single: additional_pages field
.. 




:goods_value: Goods Value, float, required



.. index::
  single: goods_value field
.. 




:holder_name: Holder Name, char



.. index::
  single: holder_name field
.. 




:sub_total: Subtotal of Extra Products, float, readonly



.. index::
  single: sub_total field
.. 




:validity_date: Validity Date, date, required



.. index::
  single: validity_date field
.. 




:holder_city: Holder City, char



.. index::
  single: holder_city field
.. 




:product_ids: Products, one2many



.. index::
  single: product_ids field
.. 




:name: Name, char, required



.. index::
  single: name field
.. 




:letter_ids: Letters, one2many



.. index::
  single: letter_ids field
.. 




:goods: Goods, char



.. index::
  single: goods field
.. 




:holder_address: Holder Address, char



.. index::
  single: holder_address field
.. 




:invoice_id: Invoice, many2one



.. index::
  single: invoice_id field
.. 




:partner_insurer_id: Insurer ID of the Partner, float, readonly



.. index::
  single: partner_insurer_id field
.. 




:return_date: Date of Return, date



.. index::
  single: return_date field
.. 




:own_risk: Own Risks, boolean



.. index::
  single: own_risk field
.. 



Object: cci_missions.letters_log
################################

.. index::
  single: cci_missions.letters_log object
.. 


:date: Date of Sending, date, required



.. index::
  single: date field
.. 




:letter_type: Type of Letter, selection, required



.. index::
  single: letter_type field
.. 




:ata_carnet_id: Related ATA Carnet, many2one, required



.. index::
  single: ata_carnet_id field
.. 



Object: Product Lines
#####################

.. index::
  single: Product Lines object
.. 


:uos_id: Unit, many2one



.. index::
  single: uos_id field
.. 




:name: Description, char, required



.. index::
  single: name field
.. 




:product_line_id: Product Ref, many2one



.. index::
  single: product_line_id field
.. 




:price_unit: Unit Price, float, required



.. index::
  single: price_unit field
.. 




:price_subtotal: Subtotal, float, readonly



.. index::
  single: price_subtotal field
.. 




:account_id: Account, many2one, required



.. index::
  single: account_id field
.. 




:dossier_product_line_id: Product Ref, many2one



.. index::
  single: dossier_product_line_id field
.. 




:product_id: Product, many2one, required



.. index::
  single: product_id field
.. 




:quantity: Quantity, float, required



.. index::
  single: quantity field
.. 

