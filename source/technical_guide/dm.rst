
Module Direct Marketing (*dm*)
==============================
:Module: dm
:Name: Direct Marketing
:Version: 5.0.1.0
:Directory: dm
:Web: http://tinyerp.com

Description
-----------

::

  Marketing Campaign Management Module
  
          This module allows to :
  
          * Commercial Offers :
              - Create  Multimedia Commercial Offers
              - View a Graphicalreprsesentation of the offer steps
              - Create offers from offer models and offer ideas
  
          * Marketing Campaign
              - Plan your Marketing Campaign and Commercial Propositions
              - Generate the Retro planning (automaticaly creates all the tasks necessary to launch your campaign)
              - Assign automatic prices to the items of your commercial propositions
              - Auto generate the purchase orders for all the items of the campaign
              - Manage Customers Fils, segments and segmentation criteria
              - Create campaigns from campaign models
              - Manage copywriters, brokers, dealers, addresses deduplicators and cleaners

Dependencies
------------

 * project_retro_planning - installed
 * purchase - installed
 * purchase_tender - installed
 * base_language - installed
 * document - installed

Reports
-------

 * Offer

 * Offer Model

 * PreOffer

 * Offer Graph

 * Campaign

Menus
-------

 * Direct Marketing
 * Direct Marketing/Configuration
 * Direct Marketing/Offers
 * Direct Marketing/Configuration/Offers
 * Direct Marketing/Offers/All Offers
 * Direct Marketing/Offers/All Offers/Open Offers
 * Direct Marketing/Offers/All Offers/Draft Offers
 * Direct Marketing/Offers/All Offers/Closed Offers
 * Direct Marketing/Offers/My Offers
 * Direct Marketing/Offers/My Offers/My Open Offers
 * Direct Marketing/Offers/My Offers/My Draft Offers
 * Direct Marketing/Offers/My Offers/My Closed Offers
 * Direct Marketing/Configuration/Offers/All Offer Models
 * Direct Marketing/Configuration/Offers/All Copywriters
 * Direct Marketing/Offers/All Offer Ideas
 * Direct Marketing/Offers/My Offer Ideas
 * Direct Marketing/Configuration/Offers/Edit Categories
 * Direct Marketing/Offers/Offer Categories
 * Direct Marketing/Configuration/Offer Steps
 * Direct Marketing/Configuration/Offer Steps/Documents
 * Direct Marketing/Configuration/Offer Steps/Documents/Edit document categories
 * Direct Marketing/Configuration/Offer Steps/Documents/All Documents
 * Direct Marketing/Configuration/Offer Steps/All Offer Step Types
 * Direct Marketing/Configuration/Offer Steps/All Offer Steps
 * Direct Marketing/Configuration/Offer Steps/Transition Trigger
 * Direct Marketing/Configuration/Offer Steps/All Items
 * Direct Marketing/Configuration/Offer Steps/All Manufacturing Constraints
 * Direct Marketing/Configuration/Offer Steps/All Offer Medias
 * Direct Marketing/Configuration/Campaigns
 * Direct Marketing/Configuration/Campaigns/Customers Lists
 * Direct Marketing/Campaigns
 * Direct Marketing/Campaigns/All Campaigns
 * Direct Marketing/Campaigns/All Campaigns/Open Campaigns
 * Direct Marketing/Campaigns/All Campaigns/Draft Campaigns
 * Direct Marketing/Campaigns/All Campaigns/Closed Campaigns
 * Direct Marketing/Campaigns/My Campaigns
 * Direct Marketing/Campaigns/My Campaigns/My Open Campaigns
 * Direct Marketing/Campaigns/My Campaigns/My Draft Campaigns
 * Direct Marketing/Campaigns/My Campaigns/My Closed Campaigns
 * Direct Marketing/Configuration/Campaigns/All Campaign Models
 * Direct Marketing/Campaigns/All Campaign Propositions
 * Direct Marketing/Campaigns/My Campaign Propositions
 * Direct Marketing/Configuration/Campaigns/All Segments
 * Direct Marketing/Campaigns/All Campaign Groups
 * Direct Marketing/Campaigns/My Campaign Groups
 * Direct Marketing/Configuration/Campaigns/All Campaign Types
 * Direct Marketing/Configuration/Campaigns/All Overlays
 * Direct Marketing/Configuration/Campaigns/All Dealers
 * Direct Marketing/Configuration/Campaigns/Customers Lists/All Customers Lists Brokers
 * Direct Marketing/Configuration/Campaigns/Customers Lists/All Deduplicator
 * Direct Marketing/Configuration/Campaigns/All Campaign Prices Progression
 * Direct Marketing/Configuration/Campaigns/All Purchase Lines
 * Direct Marketing/Configuration/Campaigns/Customers Lists/All Customers Lists
 * Direct Marketing/Configuration/Campaigns/Customers Lists/All Customers List Type
 * Direct Marketing/Configuration/Campaigns/Customers Lists/All Customers List Recruiting Origin
 * Direct Marketing/Configuration/Campaigns/Customers Lists/All Customers Files
 * Direct Marketing/Configuration/Customers
 * Direct Marketing/Configuration/Customers/All Customers
 * Direct Marketing/Configuration/Customers/All Customer Orders
 * Direct Marketing/Configuration/Customers/All Orders
 * Direct Marketing/Configuration/Customers/All Segmentations
 * Direct Marketing/Configuration/Campaigns/All Trademarks
 * Direct Marketing/Configuration/Offer Steps/Documents/All Document Dynamic Fields Templates
 * Direct Marketing/Configuration/Offer Steps/Documents/All Plugins
 * Direct Marketing/Configuration/Customers/All Customers' Plugins

Views
-----

 * dm.offer.list (tree)
 * dm.offer.tree (tree)
 * dm.offer.form (form)
 * dm.offer.model.tree (tree)
 * dm.offer.model.form (form)
 * dm.preoffer.form (form)
 * dm.offer.category.form (form)
 * dm.offer.category.list (tree)
 * dm.offer.category.tree (tree)
 * dm.offer.history.form (form)
 * dm.offer.history.tree (tree)
 * dm.offer.document.category.form (form)
 * dm.offer.document.category.tree (tree)
 * dm.offer.document.form (form)
 * dm.offer.document.tree (tree)
 * dm.offer.step.type.form (form)
 * dm.offer.step.type.tree (tree)
 * dm.offer.step.tree (tree)
 * dm.offer.step.form (form)
 * dm.offer.step.transition.trigger.form (form)
 * dm.offer.step.transition.trigger.tree (tree)
 * dm.offer.step.history.form (form)
 * dm.offer.step.history.tree (tree)
 * dm.offer.step.item.tree (tree)
 * dm.offer.step.item.form (form)
 * dm.offer.step.manufacturing_constraint.form (form)
 * dm.offer.step.manufacturing_constraint.tree (tree)
 * dm.media.form (form)
 * dm.meida.tree (tree)
 * dm.campaign.calendar (calendar)
 * dm.campaign.tree (tree)
 * dm.campaign.form (form)
 * dm.campaign.model.tree (tree)
 * dm.campaign.model.form (form)
 * dm.campaign.proposition.form (form)
 * dm.campaign.proposition.tree (tree)
 * dm.campaign.proposition.calendar (calendar)
 * dm.campaign.proposition.segment.form (form)
 * dm.campaign.proposition.segment.tree (tree)
 * dm.campaign.group.form (form)
 * dm.campaign.group.tree (tree)
 * dm.campaign.type.form (form)
 * dm.campaign.type.tree (tree)
 * dm.overlay.form (form)
 * dm.overlay.tree (tree)
 * dm.campaign.proposition.prices_progression.form (form)
 * dm.campaign.proposition.prices_progression.tree (tree)
 * dm.campaign.purchase_line_tree (tree)
 * dm.campaign.purchase_line_form (form)
 * dm.customers_list.form (form)
 * dm.customers_list.tree (tree)
 * dm.customers_list.type.form (form)
 * dm.customers_list.type.tree (tree)
 * dm.customers_list.recruit_origin.form (form)
 * dm.customers_list.recruit_origin.tree (tree)
 * dm.customers_file.form (form)
 * dm.customers_file.tree (tree)
 * \* INHERIT res.country.form.inherit (form)
 * \* INHERIT res.partner.form.inherit (form)
 * dm.customer.form (form)
 * dm.customer.tree (tree)
 * dm.customer.order.form (form)
 * dm.customer.order.tree (tree)
 * dm.order.form (form)
 * dm.order.tree (tree)
 * dm.customer.segmentation.form (form)
 * dm.customer.segmentation.tree (tree)
 * dm.trademark.tree (tree)
 * dm.trademark.form (form)
 * dm.document.template.form (form)
 * dm.document.template.tree (tree)
 * dm.ddf.plugin.form (form)
 * dm.ddf.plugin.tree (tree)
 * dm.customer.plugin.form (form)
 * dm.customer.plugin.tree (tree)


Objects
-------

Object: dm.trademark
####################



:code: Code, char, required





:name: Name, char, required





:header: Header (.odt), binary





:signature: Signature, binary





:logo: Logo, binary





:partner_id: Partner, many2one




Object: dm.media
################



:name: Media, char, required




Object: dm.offer.category
#########################



:child_ids: Childs Category, one2many





:parent_id: Parent, many2one





:complete_name: Category, char, readonly





:name: Name, char, required




Object: dm.offer.production.cost
################################



:name: Name, char, required




Object: dm.offer
################



:code: Code, char, required





:purchase_note: Purchase Notes, text





:production_category_ids: Production Categories, many2many





:last_modification_date: Last Modification Date, char, readonly





:keywords: Keywords, text





:preoffer_type: Type, selection





:offer_origin_id: Original Offer, many2one





:copywriter_id: Copywriter, many2one





:forbidden_state_ids: Forbidden States, many2many





:category_ids: Categories, many2many





:preoffer_original_id: Original Offer Idea, many2one





:state: Status, selection, readonly





:version: Version, float





:production_cost: Production Cost, many2one





:history_ids: History, one2many, readonly





:type: Type, selection





:purchase_category_ids: Purchase Categories, many2many





:name: Name, char, required





:child_ids: Childs Category, one2many





:preoffer_offer_id: Offer, many2one





:recommended_trademark: Recommended Trademark, many2one





:translation_ids: Translations, one2many, readonly





:active: Active, boolean





:order_date: Order Date, date





:lang_orig: Original Language, many2one





:legal_state: Legal State, selection





:quotation: Quotation, char





:step_ids: Offer Steps, one2many





:offer_responsible_id: Responsible, many2one





:notes: General Notes, text





:fixed_date: Fixed Date, date





:planned_delivery_date: Planned Delivery Date, date





:forbidden_country_ids: Forbidden Countries, many2many





:delivery_date: Delivery Date, date




Object: dm.offer.translation
############################



:date: Date, date





:language_id: Language, many2one





:offer_id: Offer, many2one, required





:notes: Notes, text





:translator_id: Translator, many2one




Object: dm.offer.step.type
##########################



:name: Name, char, required





:code: Code, char, required





:description: Description, text





:flow_stop: Flow Stop, boolean





:flow_start: Flow Start, boolean




Object: dm.offer.step
#####################



:incoming_transition_ids: Incoming Transition, one2many, readonly





:code: Code, char, readonly





:purchase_note: Purchase Notes, text





:origin_id: Origin, many2one





:floating date: Floating date, boolean





:quotation: Quotation, char





:manufacturing_constraint_ids: Manufacturing Constraints, one2many





:desc: Description, text





:media_ids: Medias, many2many





:item_ids: Items, many2many





:parent_id: Parent, many2one





:state: Status, selection, readonly





:outgoing_transition_ids: Outgoing Transition, one2many





:flow_start: Flow Start, boolean





:type: Type, many2one, required





:offer_id: Offer, many2one, required





:document_ids: DTP Documents, one2many





:trademark_note: Trademark Notes, text





:dtp_note: DTP Notes, text





:doc_number: Number of documents of the mailing, integer





:history_ids: History, one2many





:split_mode: Split mode, selection





:mailing_at_dates: Mailing at dates, boolean





:legal_state: Legal State, char





:trademark_category_ids: Trademark Categories, many2many





:dtp_category_ids: DTP Categories, many2many





:name: Name, char, required





:notes: Notes, text





:production_note: Production Notes, text





:interactive: Interactive, boolean





:planning_note: Planning Notes, text




Object: dm.offer.step.transition.trigger
########################################



:code: Code, char, required





:name: Trigger Name, char, required




Object: dm.offer.step.transition
################################



:delay: Offer Delay, integer, required





:step_from: From Offer Step, many2one, required





:media_id: Media, many2one, required





:condition: Trigger Condition, many2one, required





:step_to: To Offer Step, many2one, required




Object: dm.offer.step.history
#############################



:date: Date, date





:step_id: Offer, many2one





:state: Status, selection





:user_id: User, many2one




Object: dm.offer.step.item
##########################



:name: Description, char, required





:offer_step_id: Offer Step, many2one





:offer_step_type: Offer Step Type, char, readonly





:price: Price, float





:item_type: Item Type, selection





:product_ids: Products, many2many





:purchase_constraints: Purchase Constraints, text





:notes: Notes, text




Object: dm.offer.step.manufacturing_constraint
##############################################



:offer_step_id: Offer Step, many2one





:country_ids: Country, many2many





:name: Description, char, required





:constraint: Manufacturing Description, text




Object: dm.campaign.group
#########################



:code: Code, char, readonly





:name: Campaign group name, char, required





:quantity_wanted_total: Total Wanted Quantity, char, readonly





:campaign_ids: Campaigns, one2many, readonly





:quantity_usable_total: Total Usable Quantity, char, readonly





:quantity_planned_total: Total planned Quantity, char, readonly





:project_id: Project, many2one, readonly





:purchase_line_ids: Purchase Lines, one2many





:quantity_delivered_total: Total Delivered Quantity, char, readonly




Object: dm.campaign.type
########################



:code: Code, char, required





:name: Description, char, required





:description: Description, text




Object: dm.overlay
##################



:trademark_id: Trademark, many2one, required





:country_ids: Country, many2many, required





:code: Code, char, readonly





:dealer_id: Dealer, many2one, required





:bank_account_id: Account, many2one




Object: dm.campaign
###################



:code: Account code, char





:cleaner_id: Cleaner, many2one

    *The cleaner is a partner responsible to remove bad addresses from the customers list*



:contact_id: Contact, many2one





:address_ids: Partners Contacts, many2many





:crossovered_budget_line: Budget Lines, one2many





:quantity_usable_total: Total Usable Quantity, char, readonly





:proposition_ids: Proposition, one2many





:last_worked_date: Date of Last Cost/Work, date, readonly

    *Date of the latest work done on this account.*



:dealer_id: Dealer, many2one

    *The dealer is the partner the campaign is planned for*



:manufacturing_cost_ids: Manufacturing Costs, one2many





:company_id: Company, many2one, required





:parent_id: Parent analytic account, many2one





:pricelist_id: Sale Pricelist, many2one





:project_id: Project, many2one, readonly

    *Generating the Retro Planning will create and assign the different tasks used to plan and manage the campaign*



:ca_to_invoice: Uninvoiced Amount, float, readonly

    *If invoice from analytic account, the remaining amount you can invoice to the customer based on the total costs.*



:cust_file_task_ids: Customer Files tasks, one2many





:child_ids: Childs Accounts, one2many





:quantity_wanted_total: Total Wanted Quantity, char, readonly





:user_ids: User, many2many, readonly





:campaign_group_id: Campaign group, many2one





:item_task_ids: Items Procurement tasks, one2many





:theorical_margin: Theorical Margin, float, readonly

    *Computed using the formula: Theorial Revenue - Total Costs*



:dtp_task_ids: DTP tasks, one2many





:name: Account name, char, required





:notes: Notes, text





:translation_state: Translation Status, selection, readonly





:quantity_planned_total: Total planned Quantity, char, readonly





:remaining_hours: Remaining Hours, float, readonly

    *Computed using the formula: Maximum Quantity - Hours Tot.*



:last_worked_invoiced_date: Date of Last Invoiced Cost, date, readonly

    *If invoice from the costs, this is the date of the latest work or cost that have been invoiced.*



:customer_file_state: Customers Files Status, selection, readonly





:last_invoice_date: Last Invoice Date, date, readonly

    *Date of the last invoice created for this analytic account.*



:dtp_purchase_line_ids: DTP Purchase Lines, one2many





:package_ok: Used in Package, boolean





:partner_id: Associated partner, many2one





:analytic_account_id: Analytic Account, many2one





:revenue_per_hour: Revenue per Hours (real), float, readonly

    *Computed using the formula: Invoiced Amount / Hours Tot.*



:total_cost: Total Costs, float, readonly

    *Total of costs for this account. It includes real costs (from invoices) and indirect costs, like time spent on timesheets.*



:country_id: Country, many2one, required

    *The language and currency will be automaticaly assigned if they are defined for the country*



:state: State, selection, required





:debit: Debit, float, readonly





:amount_invoiced: Invoiced Amount, float, readonly

    *Total invoiced*



:planning_state: Planning Status, selection, readonly





:user_product_ids: Users/Products Rel., one2many





:manufacturing_responsible_id: Responsible, many2one





:overlay_id: Overlay, many2one





:active: Active, boolean





:real_margin_rate: Real Margin Rate (%), float, readonly

    *Computes using the formula: (Real Margin / Total Costs) * 100.*



:credit: Credit, float, readonly





:month_ids: Month, many2many, readonly





:line_ids: Analytic entries, one2many





:items_state: Items Status, selection, readonly





:trademark_id: Trademark, many2one





:amount_max: Max. Invoice Price, float





:campaign_type: Type, many2one





:dtp_state: DTP Status, selection, readonly





:user_id: Account Manager, many2one





:dtp_responsible_id: Responsible, many2one





:manufacturing_purchase_line_ids: Manufacturing Purchase Lines, one2many





:type: Account type, selection





:manufacturing_product: Manufacturing Product, many2one





:offer_id: Offer, many2one, required

    *Choose the commercial offer to use with this campaign, only offers in open state can be assigned*



:ca_invoiced: Invoiced Amount, float, readonly

    *Total customer invoiced amount for this account.*



:hours_quantity: Hours Tot, float, readonly

    *Number of hours you spent on the analytic account (from timesheet). It computes on all journal of type 'general'.*



:manufacturing_state: Manufacturing Status, selection, readonly





:ca_theorical: Theorical Revenue, float, readonly

    *Based on the costs you had on the project, what would have been the revenue if all these costs have been invoiced at the normal sale price provided by the pricelist.*



:currency_id: Currency, many2one





:dtp_making_time: Making Time, float, readonly





:to_invoice: Reinvoice Costs, many2one

    *Check this field if you plan to automatically generate invoices based on the costs in this analytic account: timesheets, expenses, ...You can configure an automatic invoice rate on analytic accounts.*



:balance: Balance, float, readonly





:quantity_delivered_total: Total Delivered Quantity, char, readonly





:item_responsible_id: Responsible, many2one





:quantity_max: Maximal quantity, float





:deduplicator_id: Deduplicator, many2one

    *The deduplicator is a partner responsible to remove identical addresses from the customers list*



:company_currency_id: Currency, many2one, readonly





:hours_qtt_non_invoiced: Uninvoiced Hours, float, readonly

    *Number of hours (from journal of type 'general') that can be invoiced if you invoice based on analytic account.*



:files_responsible_id: Responsible, many2one





:date_start: Date Start, date





:forwarding_charge: Forwarding Charge, float





:lang_id: Language, many2one





:complete_name: Account Name, char, readonly





:real_margin: Real Margin, float, readonly

    *Computed using the formula: Invoiced Amount - Total Costs.*



:hours_qtt_invoiced: Invoiced Hours, float, readonly

    *Number of hours that can be invoiced plus those that already have been invoiced.*



:router_id: Router, many2one

    *The router is the partner who will send the mailing to the final customer*



:description: Description, text





:manufacturing_task_ids: Manufacturing tasks, one2many





:remaining_ca: Remaining Revenue, float, readonly

    *Computed using the formula: Max Invoice Price - Invoiced Amount.*



:responsible_id: Responsible, many2one





:date: Date End, date





:item_purchase_line_ids: Items Purchase Lines, one2many





:code1: Code, char, readonly





:payment_methods: Payment Methods, many2many





:cust_file_purchase_line_ids: Customer Files Purchase Lines, one2many





:journal_rate_ids: Invoicing Rate per Journal, one2many





:quantity: Quantity, float, readonly




Object: dm.campaign.proposition
###############################



:initial_proposition_id: Initial proposition, many2one, readonly





:code: Account code, char





:last_worked_invoiced_date: Date of Last Invoiced Cost, date, readonly

    *If invoice from the costs, this is the date of the latest work or cost that have been invoiced.*



:ca_to_invoice: Uninvoiced Amount, float, readonly

    *If invoice from analytic account, the remaining amount you can invoice to the customer based on the total costs.*



:quantity_max: Maximal quantity, float





:quantity_usable: Usable Quantity, char, readonly

    *The usable quantity is the number of addresses you have after delivery, deduplication and cleaning.*



:contact_id: Contact, many2one





:company_currency_id: Currency, many2one, readonly





:date: Date End, date





:last_invoice_date: Last Invoice Date, date, readonly

    *Date of the last invoice created for this analytic account.*



:crossovered_budget_line: Budget Lines, one2many





:amount_max: Max. Invoice Price, float





:package_ok: Used in Package, boolean





:hours_qtt_non_invoiced: Uninvoiced Hours, float, readonly

    *Number of hours (from journal of type 'general') that can be invoiced if you invoice based on analytic account.*



:keep_prices: Keep Prices At Duplication, boolean





:partner_id: Associated partner, many2one





:proposition_type: Type, selection





:analytic_account_id: Analytic Account, many2one





:last_worked_date: Date of Last Cost/Work, date, readonly

    *Date of the latest work done on this account.*



:starting_mail_price: Starting Mail Price, float





:user_id: Account Manager, many2one





:item_ids: Catalogue, one2many





:to_invoice: Reinvoice Costs, many2one

    *Check this field if you plan to automatically generate invoices based on the costs in this analytic account: timesheets, expenses, ...You can configure an automatic invoice rate on analytic accounts.*



:total_cost: Total Costs, float, readonly

    *Total of costs for this account. It includes real costs (from invoices) and indirect costs, like time spent on timesheets.*



:date_start: Date Start, date





:company_id: Company, many2one, required





:segment_ids: Segment, one2many





:parent_id: Parent analytic account, many2one





:state: State, selection, required





:quantity_planned: planned Quantity, char, readonly

    *The planned quantity is an estimation of the usable quantity of addresses you  will get after delivery, deduplication and cleaning
    This is usually the quantity used to order the manufacturing of the mailings*



:complete_name: Account Name, char, readonly





:real_margin: Real Margin, float, readonly

    *Computed using the formula: Invoiced Amount - Total Costs.*



:debit: Debit, float, readonly





:forwarding_charge: Forwarding Charge, float





:pricelist_id: Sale Pricelist, many2one





:type: Account type, selection





:quantity: Quantity, float, readonly





:manufacturing_costs: Manufacturing Costs, float





:journal_rate_ids: Invoicing Rate per Journal, one2many





:description: Description, text





:amount_invoiced: Invoiced Amount, float, readonly

    *Total invoiced*



:forwarding_charges: Forwarding Charges, float





:credit: Credit, float, readonly





:child_ids: Childs Accounts, one2many





:user_product_ids: Users/Products Rel., one2many





:ca_invoiced: Invoiced Amount, float, readonly

    *Total customer invoiced amount for this account.*



:sale_rate: Sale Rate (%), float

    *This is the planned sale rate (in percent) for this commercial proposition*



:user_ids: User, many2many, readonly





:remaining_ca: Remaining Revenue, float, readonly

    *Computed using the formula: Max Invoice Price - Invoiced Amount.*



:quantity_delivered: Delivered Quantity, char, readonly

    *The delivered quantity is the number of addresses you receive from the broker.*



:code1: Code, char, readonly





:hours_qtt_invoiced: Invoiced Hours, float, readonly

    *Number of hours that can be invoiced plus those that already have been invoiced.*



:active: Active, boolean





:hours_quantity: Hours Tot, float, readonly

    *Number of hours you spent on the analytic account (from timesheet). It computes on all journal of type 'general'.*



:theorical_margin: Theorical Margin, float, readonly

    *Computed using the formula: Theorial Revenue - Total Costs*



:ca_theorical: Theorical Revenue, float, readonly

    *Based on the costs you had on the project, what would have been the revenue if all these costs have been invoiced at the normal sale price provided by the pricelist.*



:quantity_wanted: Wanted Quantity, char, readonly

    *The wanted quantity is the number of addresses you wish to get for that segment.
    This is usually the quantity used to order Customers Lists
    The wanted quantity could be AAA for All Addresses Available*



:sm_price: Starting Mail Price, float





:keep_segments: Keep Segments, boolean





:name: Account name, char, required





:customer_pricelist_id: Items Pricelist, many2one





:notes: Notes, text





:force_sm_price: Force Starting Mail Price, boolean





:address_ids: Partners Contacts, many2many





:real_margin_rate: Real Margin Rate (%), float, readonly

    *Computes using the formula: (Real Margin / Total Costs) * 100.*



:revenue_per_hour: Revenue per Hours (real), float, readonly

    *Computed using the formula: Invoiced Amount / Hours Tot.*



:month_ids: Month, many2many, readonly





:quantity_real: Real Quantity, char, readonly

    *The real quantity is the number of addresses you really get in the file.*



:payment_methods: Payment Methods, many2many





:line_ids: Analytic entries, one2many





:balance: Balance, float, readonly





:camp_id: Campaign, many2one, required





:remaining_hours: Remaining Hours, float, readonly

    *Computed using the formula: Maximum Quantity - Hours Tot.*


Object: The origin of the adresses of a list
############################################



:code: Code, char, required





:name: Name, char, required




Object: Type of the adress list
###############################



:code: Code, char, required





:name: Name, char, required




Object: A list of addresses proposed by an adresses broker
##########################################################



:other_cost: Other Cost, float





:selection_cost: Selection Cost Per Thousand, float





:broker_cost: Broker Cost, float

    *The amount given to the broker for the list renting*



:code: Code, char, required





:product_id: Product, many2one, required





:per_thousand_price: Price per Thousand, float





:update_frq: Update Frequency, integer





:currency_id: Currency, many2one





:country_id: Country, many2one





:broker_discount: Broker Discount (%), float





:recruiting_origin: Recruiting Origin, many2one

    *Origin of the recruiting of the adresses*



:broker_id: Broker, many2one





:delivery_cost: Delivery Cost, float





:list_type: Type, many2one





:invoice_base: Invoicing based on, selection

    *Net or raw quantity on which is based the final invoice depending of the term negociated with the broker.
    Net : Usable quantity after deduplication
    Raw : Delivered quantity
    Real : Realy used qunatity*



:owner_id: Owner, many2one





:notes: Description, text





:name: Name, char, required




Object: A File of addresses delivered by an addresses broker
############################################################



:segment_ids: Segments, one2many, readonly





:code: Code, char, required





:customers_list_id: Customers List, many2one





:delivery_date: Delivery Date, date





:name: Name, char, required




Object: A subset of addresses coming from a customers file
##########################################################



:code: Account code, char





:last_worked_invoiced_date: Date of Last Invoiced Cost, date, readonly

    *If invoice from the costs, this is the date of the latest work or cost that have been invoiced.*



:ca_to_invoice: Uninvoiced Amount, float, readonly

    *If invoice from analytic account, the remaining amount you can invoice to the customer based on the total costs.*



:analytic_account_id: Analytic Account, many2one





:quantity_cleaned_cleaner: Cleaned Quantity, integer

    *The quantity of wrong addresses removed by the cleaner.*



:quantity_dedup_cleaner: Deduplication Quantity, integer

    *The quantity of duplicated addresses removed by the cleaner.*



:quantity_max: Maximal quantity, float





:quantity_usable: Usable Quantity, integer, readonly

    *The usable quantity is the number of addresses you have after delivery, deduplication and cleaning.*



:contact_id: Contact, many2one





:company_currency_id: Currency, many2one, readonly





:date: Date End, date





:last_invoice_date: Last Invoice Date, date, readonly

    *Date of the last invoice created for this analytic account.*



:crossovered_budget_line: Budget Lines, one2many





:amount_max: Max. Invoice Price, float





:package_ok: Used in Package, boolean





:hours_qtt_non_invoiced: Uninvoiced Hours, float, readonly

    *Number of hours (from journal of type 'general') that can be invoiced if you invoice based on analytic account.*



:partner_id: Associated partner, many2one





:all_add_avail: All Adresses Available, boolean

    *Used to order all adresses available in the customers list based on the segmentation criteria*



:split_id: Split, many2one





:note: Notes, text





:last_worked_date: Date of Last Cost/Work, date, readonly

    *Date of the latest work done on this account.*



:start_census: Start Census (days), integer

    *The recency is the time since the latest purchase.
    For example : A 0-30 recency means all the customers that have purchased in the last 30 days*



:user_id: Account Manager, many2one





:to_invoice: Reinvoice Costs, many2one

    *Check this field if you plan to automatically generate invoices based on the costs in this analytic account: timesheets, expenses, ...You can configure an automatic invoice rate on analytic accounts.*



:total_cost: Total Costs, float, readonly

    *Total of costs for this account. It includes real costs (from invoices) and indirect costs, like time spent on timesheets.*



:quantity_purged: Purged Quantity, integer, readonly

    *The purged quantity is the number of addresses removed from deduplication and cleaning.*



:date_start: Date Start, date





:customers_file_id: Customers File, many2one, readonly





:company_id: Company, many2one, required





:proposition_id: Proposition, many2one





:reuse_id: Reuse, many2one





:parent_id: Parent analytic account, many2one





:state: State, selection, required





:customers_list_id: Customers List, many2one, required





:complete_name: Account Name, char, readonly





:real_margin: Real Margin, float, readonly

    *Computed using the formula: Invoiced Amount - Total Costs.*



:debit: Debit, float, readonly





:pricelist_id: Sale Pricelist, many2one





:type: Account type, selection





:quantity: Quantity, float, readonly





:quantity_cleaned_dedup: Cleaned Quantity, integer

    *The quantity of wrong addresses removed by the deduplicator.*



:quantity_dedup_dedup: Deduplication Quantity, integer

    *The quantity of duplicated addresses removed by the deduplicator.*



:journal_rate_ids: Invoicing Rate per Journal, one2many





:description: Description, text





:amount_invoiced: Invoiced Amount, float, readonly

    *Total invoiced*



:quantity_planned: planned Quantity, integer

    *The planned quantity is an estimation of the usable quantity of addresses you  will get after delivery, deduplication and cleaning
    This is usually the quantity used to order the manufacturing of the mailings*



:credit: Credit, float, readonly





:child_ids: Childs Accounts, one2many





:user_product_ids: Users/Products Rel., one2many





:ca_invoiced: Invoiced Amount, float, readonly

    *Total customer invoiced amount for this account.*



:user_ids: User, many2many, readonly





:remaining_ca: Remaining Revenue, float, readonly

    *Computed using the formula: Max Invoice Price - Invoiced Amount.*



:quantity_delivered: Delivered Quantity, integer

    *The delivered quantity is the number of addresses you receive from the broker.*



:code1: Code, char, readonly





:hours_qtt_invoiced: Invoiced Hours, float, readonly

    *Number of hours that can be invoiced plus those that already have been invoiced.*



:active: Active, boolean





:hours_quantity: Hours Tot, float, readonly

    *Number of hours you spent on the analytic account (from timesheet). It computes on all journal of type 'general'.*



:deduplication_level: Deduplication Level, integer

    *The deduplication level defines the order in which the deduplication takes place.*



:theorical_margin: Theorical Margin, float, readonly

    *Computed using the formula: Theorial Revenue - Total Costs*



:ca_theorical: Theorical Revenue, float, readonly

    *Based on the costs you had on the project, what would have been the revenue if all these costs have been invoiced at the normal sale price provided by the pricelist.*



:quantity_wanted: Wanted Quantity, integer

    *The wanted quantity is the number of addresses you wish to get for that segment.
    This is usually the quantity used to order Customers Lists
    The wanted quantity could be AAA for All Addresses Available*



:name: Account name, char, required





:end_census: End Census (days), integer





:address_ids: Partners Contacts, many2many





:real_margin_rate: Real Margin Rate (%), float, readonly

    *Computes using the formula: (Real Margin / Total Costs) * 100.*



:revenue_per_hour: Revenue per Hours (real), float, readonly

    *Computed using the formula: Invoiced Amount / Hours Tot.*



:segmentation_criteria: Segmentation Criteria, text





:month_ids: Month, many2many, readonly





:quantity_real: Real Quantity, integer

    *The real quantity is the number of addresses that are really in the customers file (by counting).*



:line_ids: Analytic entries, one2many





:balance: Balance, float, readonly





:remaining_hours: Remaining Hours, float, readonly

    *Computed using the formula: Maximum Quantity - Hours Tot.*


Object: dm.campaign.proposition.item
####################################



:product_id: Product, many2one, required





:price: Sale Price, float





:qty_real: Real Quantity, integer





:proposition_id: Commercial Proposition, many2one





:qty_planned: Planned Quantity, integer





:item_type: Item Type, selection





:offer_step_type_id: Offer Step Type, many2one





:notes: Notes, text




Object: dm.campaign.purchase_line
#################################



:type_document: Document Type, selection





:campaign_group_id: Campaign Group, many2one





:product_id: Product, many2one, required





:togroup: Apply to Campaign Group, boolean





:product_category: Product Category, selection





:trigger: Trigger, selection





:notes: Notes, text





:date_planned: Scheduled date, datetime, required





:campaign_id: Campaign, many2one





:date_delivery: Delivery Date, datetime, readonly





:uom_id: UOM, many2one, required





:desc_from_offer: Insert Description from Offer, boolean





:state: State, selection, readonly





:type_quantity: Quantity Type, selection





:quantity_warning: Warning, char, readonly





:purchase_order_ids: Campaign Purchase Line, one2many





:date_order: Order date, datetime, readonly





:type: Type, selection





:quantity: Total Quantity, integer, required




Object: dm.campaign.manufacturing_cost
######################################



:amount: Amount, float





:name: Description, char, required





:campaign_id: Campaign, many2one




Object: dm.campaign.proposition.prices_progression
##################################################



:percent_prog: Percentage Prices Progression, float





:fixed_prog: Fixed Prices Progression, float





:name: Name, char, required




Object: dm.order
################



:customer_code: Customer Code, char





:zip: Zip Code, char





:segment_code: Segment Code, char





:country: Country, char





:offer_step_code: Offer Step Code, char





:title: Title, char





:customer_firstname: First Name, char





:customer_add4: Address4, char





:state: Status, selection, readonly





:zip_summary: Zip Summary, char





:customer_lastname: Last Name, char





:customer_add1: Address1, char





:raw_datas: Raw Datas, char





:distribution_office: Distribution Office, char





:customer_add2: Address2, char





:customer_add3: Address3, char




Object: res.partner
###################



:ean13: EAN13, char





:property_account_position: Fiscal Position, many2one

    *The fiscal position will determine taxes and the accounts used for the the partner.*



:ref_companies: Companies that refers to partner, one2many





:canal_id: Favourite Channel, many2one





:property_product_pricelist: Sale Pricelist, many2one

    *This pricelist will be used, instead of the default one,                     for sales to the current partner*



:name_official: Official Name, char





:title: Title, char





:parent_id: Main Company, many2one





:membership_cancel: Cancel membership date, date, readonly





:alert_advertising: Adv.Alert, boolean

    *Partners description to be shown when inserting new advertising sale*



:decoy_for_campaign: Used for Campaigns, boolean

    *Define if this decoy address can be used with campaigns*



:import_procent: Import (%), integer





:client_media_ids: Client for Media, many2many





:lastname: Last Name, char





:child_ids: Partner Ref., one2many





:payment_type_customer: Payment type, many2one

    *Payment type of the customer*



:export_year: Export date, date

    *year of the export_procent value*



:name: Name, char, required





:decoy_external_ref: External Reference, char

    *The reference of the decoy address for the owner*



:debit_limit: Payable Limit, float





:property_account_receivable: Account Receivable, many2one, required

    *This account will be used, instead of the default one, as the receivable account for the current partner*



:domiciliation_bool: Domiciliation, boolean





:decoy_for_renting: Used for File Renting, boolean

    *Define if this decoy address can be used with used with customers files renting*



:article_ids: Articles, many2many





:dir_exclude: Dir. exclude, boolean

    *Exclusion from the Members directory*



:logo: Logo, binary





:name_old: Former Name, char





:activity_description: Activity Description, text





:alert_events: Event Alert, boolean

    *Partners description to be shown when inserting new subscription to a meeting*



:invoice_special: Invoice Special, boolean





:state_id2: Customer State, many2one

    *status of the partner as a customer*



:debit: Total Payable, float, readonly

    *Total amount you have to pay to this supplier.*



:supplier: Supplier, boolean

    *Check this box if the partner is a supplier. If it's not checked, purchase people will not see it when encoding a purchase order.*



:ref: Code, char, readonly





:alert_others: Other alert, boolean

    *Partners description to be shown when inserting new sale not treated by _advertising, _events, _legalisations, _Membership*



:import_year: Import Date, date

    *year of the import_procent value*



:free_member: Free member, boolean





:membership_amount: Membership amount, float

    *The price negociated by the partner*



:address: Addresses, one2many





:active: Active, boolean





:dir_date_publication: Publication Date, date





:wall_exclusion: Not in Walloon DB, boolean

    *exclusion of this partner from the walloon database*



:property_product_pricelist_purchase: Purchase Pricelist, many2one

    *This pricelist will be used, instead of the default one, for purchases from the current partner*



:country: Country, many2one





:invoice_nbr: Nbr of invoice to print, integer

    *number of additive invoices to be printed for this customer*



:invoice_paper: Bank Transfer Type, selection





:credit: Total Receivable, float, readonly

    *Total amount this customer owns you.*



:country_relation: Country Relation, one2many





:signature: Signature, binary





:invoice_public: Invoice Public, boolean





:employee_nbr: Nbr of Employee (Area), integer

    *Nbr of Employee in the area of the CCI*



:comment: Notes, text





:decoy_owner: Decoy Address Owner, many2one

    *The partner this decoy address belongs to*



:country_ids: Allowed Countries, many2many





:language_ids: Other Languages, many2many





:header: Header (.odt), binary





:member_lines: Membership, one2many





:alert_legalisations: Legal. Alert, boolean

    *Partners description to be shown when inserting new legalisation*



:city: City, char





:dir_date_last: Partner Data Date, date

    *Date of latest update of the partner data by itself (via paper or Internet)*



:user_id: Dedicated Salesman, many2one

    *The internal user that is in charge of communicating with this partner if any.*



:magazine_subscription: Magazine subscription, selection





:vat: VAT, char

    *Value Added Tax number. Check the box if the partner is subjected to the VAT. Used by the VAT legal statement.*



:website: Website, char





:credit_limit: Credit Limit, float





:answers_ids: Answers, many2many





:alert_explanation: Warning, text





:customer: Customer, boolean

    *Check this box if the partner is a customer.*



:date_founded: Founding Date, date

    *Date of foundation of this company*



:employee_nbr_total: Nbr of Employee (Tot), integer

    *Nbr of Employee all around the world*



:dir_date_accept: Good to shoot Date, date

    *Date of last acceptation of Bon a Tirer*



:membership_start: Start membership date, date, readonly





:alert_membership: Membership Alert, boolean

    *Partners description to be shown when inserting new ship sale*



:membership_stop: Stop membership date, date, readonly





:state_id: Partner State, many2one

    *status of activity of the partner*



:relation_ids: Partner Relation, one2many





:prospect_media_ids: Prospect for Media, many2many





:domiciliation: Domiciliation Number, char





:date: Date, date





:decoy_address: Decoy Address, boolean

    *A decoy address is an address used to identify unleagal uses of a customers file*



:dir_presence: Dir. Presence, boolean

    *Present in the directory of the members*



:property_account_payable: Account Payable, many2one, required

    *This account will be used, instead of the default one, as the payable account for the current partner*



:property_stock_supplier: Supplier Location, many2one

    *This stock location will be used, instead of the default one, as the source location for goods you receive from the current partner*



:training_authorization: Checks Auth., char

    *Formation and Language Checks Authorization number*



:events: Events, one2many





:associate_member: Associate member, many2one





:dir_name2: 1st Shortcut name , char

    *First shortcut in the members directory, pointing to the dir_name field*



:dir_name3: 2nd Shortcut name , char

    *Second shortcut*



:bank_ids: Banks, one2many





:vat_subjected: VAT Legal Statement, boolean

    *Check this box if the partner is subjected to the VAT. It will be used for the VAT legal statement.*



:state_ids: Allowed States, many2many





:export_procent: Export(%), integer





:decoy_media_ids: decoy address for Media, many2many





:property_stock_customer: Customer Location, many2one

    *This stock location will be used, instead of the default one, as the destination location for goods you send to this partner*



:lang: Language, selection

    *If the selected language is loaded in the system, all documents related to this partner will be printed in this language. If not, it will be english.*



:dir_name: Name in Member Dir., char

    *Name under wich the partner will be inserted in the members directory*



:membership_state: Current membership state, selection, readonly





:activity_code_ids: Activity Codes, one2many





:magazine_subscription_source: Mag. Subscription Source, char





:property_payment_term: Payment Term, many2one

    *This payment term will be used, instead of the default one, for the current partner*



:payment_type_supplier: Payment type, many2one

    *Payment type of the supplier*



:category_id: Categories, many2many




Object: dm.customer.order
#########################



:offer_step_id: Offer Step, many2one





:note: Notes, text





:state: Status, selection, readonly





:customer_id: Customer, many2one





:segment_id: Segment, many2one




Object: Segmentation
####################



:customer_date_criteria_ids: Customers Date Criteria, one2many





:order_text_criteria_ids: Customers Order Textual Criteria, one2many





:code: Code, char, required





:name: Name, char, required





:notes: Description, text





:order_boolean_criteria_ids: Customers Order Boolean Criteria, one2many





:order_numeric_criteria_ids: Customers Order Numeric Criteria, one2many





:customer_numeric_criteria_ids: Customers Numeric Criteria, one2many





:customer_boolean_criteria_ids: Customers Boolean Criteria, one2many





:sql_query: SQL Query, text





:order_date_criteria_ids: Customers Order Date Criteria, one2many





:customer_text_criteria_ids: Customers Textual Criteria, one2many




Object: Customer Segmentation Textual Criteria
##############################################



:operator: Operator, selection





:segmentation_id: Segmentation, many2one





:value: Value, char





:field: Customers Field, many2one




Object: Customer Segmentation Numeric Criteria
##############################################



:operator: Operator, selection





:segmentation_id: Segmentation, many2one





:value: Value, float





:field: Customers Field, many2one




Object: Customer Segmentation Boolean Criteria
##############################################



:operator: Operator, selection





:segmentation_id: Segmentation, many2one





:value: Value, selection





:field: Customers Field, many2one




Object: Customer Segmentation Date Criteria
###########################################



:operator: Operator, selection





:segmentation_id: Segmentation, many2one





:to_value: To, datetime





:from_value: From, datetime





:field: Customers Field, many2one




Object: Customer Order Segmentation Textual Criteria
####################################################



:operator: Operator, selection





:segmentation_id: Segmentation, many2one





:value: Value, char





:field: Customers Field, many2one




Object: Customer Order Segmentation Numeric Criteria
####################################################



:operator: Operator, selection





:segmentation_id: Segmentation, many2one





:value: Value, float





:field: Customers Field, many2one




Object: Customer Order Segmentation Date Criteria
#################################################



:operator: Operator, selection





:segmentation_id: Segmentation, many2one





:to_value: To, datetime





:from_value: From, datetime





:field: Customers Field, many2one




Object: dm.offer.history
########################



:date: Drop Date, date





:offer_id: Offer, many2one, required





:code: Code, char





:campaign_id: Name, many2one





:responsible_id: Responsible, many2one




Object: dm.ddf.plugin
#####################



:name: DDF Plugin Name, char





:file_fname: Filename, char





:file_id: File Content, binary




Object: dm.document.template
############################



:plugin_ids: Plugin, many2many





:dynamic_fields: Fields, many2many





:name: Template Name, char




Object: dm.customer.plugin
##########################



:date: Date, date





:plugin_id: Plugin, many2one





:customer_id: Customer Name, many2one





:value: Value, char




Object: dm.offer.document.category
##################################



:parent_id: Parent, many2one





:complete_name: Category, char, readonly





:name: Name, char, required




Object: dm.offer.document
#########################



:copywriter_id: Copywriter, many2one





:name: Name, char, required





:document_template_plugin_ids: Dynamic Plugins, many2many





:lang_id: Language, many2one





:category_ids: Categories, many2many





:state: Status, selection, readonly





:code: Code, char, required





:has_attachment: Has Attachment, char, readonly





:document_template_field_ids: Dynamic Fields, many2many





:document_template_id: Document Template, many2one





:step_id: Offer Step, many2one


