
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

.. index::
  single: dm.trademark object
.. 


:code: Code, char, required



.. index::
  single: code field
.. 




:name: Name, char, required



.. index::
  single: name field
.. 




:header: Header (.odt), binary



.. index::
  single: header field
.. 




:signature: Signature, binary



.. index::
  single: signature field
.. 




:logo: Logo, binary



.. index::
  single: logo field
.. 




:partner_id: Partner, many2one



.. index::
  single: partner_id field
.. 



Object: dm.media
################

.. index::
  single: dm.media object
.. 


:name: Media, char, required



.. index::
  single: name field
.. 



Object: dm.offer.category
#########################

.. index::
  single: dm.offer.category object
.. 


:child_ids: Childs Category, one2many



.. index::
  single: child_ids field
.. 




:parent_id: Parent, many2one



.. index::
  single: parent_id field
.. 




:complete_name: Category, char, readonly



.. index::
  single: complete_name field
.. 




:name: Name, char, required



.. index::
  single: name field
.. 



Object: dm.offer.production.cost
################################

.. index::
  single: dm.offer.production.cost object
.. 


:name: Name, char, required



.. index::
  single: name field
.. 



Object: dm.offer
################

.. index::
  single: dm.offer object
.. 


:code: Code, char, required



.. index::
  single: code field
.. 




:purchase_note: Purchase Notes, text



.. index::
  single: purchase_note field
.. 




:production_category_ids: Production Categories, many2many



.. index::
  single: production_category_ids field
.. 




:last_modification_date: Last Modification Date, char, readonly



.. index::
  single: last_modification_date field
.. 




:keywords: Keywords, text



.. index::
  single: keywords field
.. 




:preoffer_type: Type, selection



.. index::
  single: preoffer_type field
.. 




:offer_origin_id: Original Offer, many2one



.. index::
  single: offer_origin_id field
.. 




:copywriter_id: Copywriter, many2one



.. index::
  single: copywriter_id field
.. 




:forbidden_state_ids: Forbidden States, many2many



.. index::
  single: forbidden_state_ids field
.. 




:category_ids: Categories, many2many



.. index::
  single: category_ids field
.. 




:preoffer_original_id: Original Offer Idea, many2one



.. index::
  single: preoffer_original_id field
.. 




:state: Status, selection, readonly



.. index::
  single: state field
.. 




:version: Version, float



.. index::
  single: version field
.. 




:production_cost: Production Cost, many2one



.. index::
  single: production_cost field
.. 




:history_ids: History, one2many, readonly



.. index::
  single: history_ids field
.. 




:type: Type, selection



.. index::
  single: type field
.. 




:purchase_category_ids: Purchase Categories, many2many



.. index::
  single: purchase_category_ids field
.. 




:name: Name, char, required



.. index::
  single: name field
.. 




:child_ids: Childs Category, one2many



.. index::
  single: child_ids field
.. 




:preoffer_offer_id: Offer, many2one



.. index::
  single: preoffer_offer_id field
.. 




:recommended_trademark: Recommended Trademark, many2one



.. index::
  single: recommended_trademark field
.. 




:translation_ids: Translations, one2many, readonly



.. index::
  single: translation_ids field
.. 




:active: Active, boolean



.. index::
  single: active field
.. 




:order_date: Order Date, date



.. index::
  single: order_date field
.. 




:lang_orig: Original Language, many2one



.. index::
  single: lang_orig field
.. 




:legal_state: Legal State, selection



.. index::
  single: legal_state field
.. 




:quotation: Quotation, char



.. index::
  single: quotation field
.. 




:step_ids: Offer Steps, one2many



.. index::
  single: step_ids field
.. 




:offer_responsible_id: Responsible, many2one



.. index::
  single: offer_responsible_id field
.. 




:notes: General Notes, text



.. index::
  single: notes field
.. 




:fixed_date: Fixed Date, date



.. index::
  single: fixed_date field
.. 




:planned_delivery_date: Planned Delivery Date, date



.. index::
  single: planned_delivery_date field
.. 




:forbidden_country_ids: Forbidden Countries, many2many



.. index::
  single: forbidden_country_ids field
.. 




:delivery_date: Delivery Date, date



.. index::
  single: delivery_date field
.. 



Object: dm.offer.translation
############################

.. index::
  single: dm.offer.translation object
.. 


:date: Date, date



.. index::
  single: date field
.. 




:language_id: Language, many2one



.. index::
  single: language_id field
.. 




:offer_id: Offer, many2one, required



.. index::
  single: offer_id field
.. 




:notes: Notes, text



.. index::
  single: notes field
.. 




:translator_id: Translator, many2one



.. index::
  single: translator_id field
.. 



Object: dm.offer.step.type
##########################

.. index::
  single: dm.offer.step.type object
.. 


:name: Name, char, required



.. index::
  single: name field
.. 




:code: Code, char, required



.. index::
  single: code field
.. 




:description: Description, text



.. index::
  single: description field
.. 




:flow_stop: Flow Stop, boolean



.. index::
  single: flow_stop field
.. 




:flow_start: Flow Start, boolean



.. index::
  single: flow_start field
.. 



Object: dm.offer.step
#####################

.. index::
  single: dm.offer.step object
.. 


:incoming_transition_ids: Incoming Transition, one2many, readonly



.. index::
  single: incoming_transition_ids field
.. 




:code: Code, char, readonly



.. index::
  single: code field
.. 




:purchase_note: Purchase Notes, text



.. index::
  single: purchase_note field
.. 




:origin_id: Origin, many2one



.. index::
  single: origin_id field
.. 




:floating date: Floating date, boolean



.. index::
  single: floating date field
.. 




:quotation: Quotation, char



.. index::
  single: quotation field
.. 




:manufacturing_constraint_ids: Manufacturing Constraints, one2many



.. index::
  single: manufacturing_constraint_ids field
.. 




:desc: Description, text



.. index::
  single: desc field
.. 




:media_ids: Medias, many2many



.. index::
  single: media_ids field
.. 




:item_ids: Items, many2many



.. index::
  single: item_ids field
.. 




:parent_id: Parent, many2one



.. index::
  single: parent_id field
.. 




:state: Status, selection, readonly



.. index::
  single: state field
.. 




:outgoing_transition_ids: Outgoing Transition, one2many



.. index::
  single: outgoing_transition_ids field
.. 




:flow_start: Flow Start, boolean



.. index::
  single: flow_start field
.. 




:type: Type, many2one, required



.. index::
  single: type field
.. 




:offer_id: Offer, many2one, required



.. index::
  single: offer_id field
.. 




:document_ids: DTP Documents, one2many



.. index::
  single: document_ids field
.. 




:trademark_note: Trademark Notes, text



.. index::
  single: trademark_note field
.. 




:dtp_note: DTP Notes, text



.. index::
  single: dtp_note field
.. 




:doc_number: Number of documents of the mailing, integer



.. index::
  single: doc_number field
.. 




:history_ids: History, one2many



.. index::
  single: history_ids field
.. 




:split_mode: Split mode, selection



.. index::
  single: split_mode field
.. 




:mailing_at_dates: Mailing at dates, boolean



.. index::
  single: mailing_at_dates field
.. 




:legal_state: Legal State, char



.. index::
  single: legal_state field
.. 




:trademark_category_ids: Trademark Categories, many2many



.. index::
  single: trademark_category_ids field
.. 




:dtp_category_ids: DTP Categories, many2many



.. index::
  single: dtp_category_ids field
.. 




:name: Name, char, required



.. index::
  single: name field
.. 




:notes: Notes, text



.. index::
  single: notes field
.. 




:production_note: Production Notes, text



.. index::
  single: production_note field
.. 




:interactive: Interactive, boolean



.. index::
  single: interactive field
.. 




:planning_note: Planning Notes, text



.. index::
  single: planning_note field
.. 



Object: dm.offer.step.transition.trigger
########################################

.. index::
  single: dm.offer.step.transition.trigger object
.. 


:code: Code, char, required



.. index::
  single: code field
.. 




:name: Trigger Name, char, required



.. index::
  single: name field
.. 



Object: dm.offer.step.transition
################################

.. index::
  single: dm.offer.step.transition object
.. 


:delay: Offer Delay, integer, required



.. index::
  single: delay field
.. 




:step_from: From Offer Step, many2one, required



.. index::
  single: step_from field
.. 




:media_id: Media, many2one, required



.. index::
  single: media_id field
.. 




:condition: Trigger Condition, many2one, required



.. index::
  single: condition field
.. 




:step_to: To Offer Step, many2one, required



.. index::
  single: step_to field
.. 



Object: dm.offer.step.history
#############################

.. index::
  single: dm.offer.step.history object
.. 


:date: Date, date



.. index::
  single: date field
.. 




:step_id: Offer, many2one



.. index::
  single: step_id field
.. 




:state: Status, selection



.. index::
  single: state field
.. 




:user_id: User, many2one



.. index::
  single: user_id field
.. 



Object: dm.offer.step.item
##########################

.. index::
  single: dm.offer.step.item object
.. 


:name: Description, char, required



.. index::
  single: name field
.. 




:offer_step_id: Offer Step, many2one



.. index::
  single: offer_step_id field
.. 




:offer_step_type: Offer Step Type, char, readonly



.. index::
  single: offer_step_type field
.. 




:price: Price, float



.. index::
  single: price field
.. 




:item_type: Item Type, selection



.. index::
  single: item_type field
.. 




:product_ids: Products, many2many



.. index::
  single: product_ids field
.. 




:purchase_constraints: Purchase Constraints, text



.. index::
  single: purchase_constraints field
.. 




:notes: Notes, text



.. index::
  single: notes field
.. 



Object: dm.offer.step.manufacturing_constraint
##############################################

.. index::
  single: dm.offer.step.manufacturing_constraint object
.. 


:offer_step_id: Offer Step, many2one



.. index::
  single: offer_step_id field
.. 




:country_ids: Country, many2many



.. index::
  single: country_ids field
.. 




:name: Description, char, required



.. index::
  single: name field
.. 




:constraint: Manufacturing Description, text



.. index::
  single: constraint field
.. 



Object: dm.campaign.group
#########################

.. index::
  single: dm.campaign.group object
.. 


:code: Code, char, readonly



.. index::
  single: code field
.. 




:name: Campaign group name, char, required



.. index::
  single: name field
.. 




:quantity_wanted_total: Total Wanted Quantity, char, readonly



.. index::
  single: quantity_wanted_total field
.. 




:campaign_ids: Campaigns, one2many, readonly



.. index::
  single: campaign_ids field
.. 




:quantity_usable_total: Total Usable Quantity, char, readonly



.. index::
  single: quantity_usable_total field
.. 




:quantity_planned_total: Total planned Quantity, char, readonly



.. index::
  single: quantity_planned_total field
.. 




:project_id: Project, many2one, readonly



.. index::
  single: project_id field
.. 




:purchase_line_ids: Purchase Lines, one2many



.. index::
  single: purchase_line_ids field
.. 




:quantity_delivered_total: Total Delivered Quantity, char, readonly



.. index::
  single: quantity_delivered_total field
.. 



Object: dm.campaign.type
########################

.. index::
  single: dm.campaign.type object
.. 


:code: Code, char, required



.. index::
  single: code field
.. 




:name: Description, char, required



.. index::
  single: name field
.. 




:description: Description, text



.. index::
  single: description field
.. 



Object: dm.overlay
##################

.. index::
  single: dm.overlay object
.. 


:trademark_id: Trademark, many2one, required



.. index::
  single: trademark_id field
.. 




:country_ids: Country, many2many, required



.. index::
  single: country_ids field
.. 




:code: Code, char, readonly



.. index::
  single: code field
.. 




:dealer_id: Dealer, many2one, required



.. index::
  single: dealer_id field
.. 




:bank_account_id: Account, many2one



.. index::
  single: bank_account_id field
.. 



Object: dm.campaign
###################

.. index::
  single: dm.campaign object
.. 


:code: Account code, char



.. index::
  single: code field
.. 




:cleaner_id: Cleaner, many2one

    *The cleaner is a partner responsible to remove bad addresses from the customers list*

.. index::
  single: cleaner_id field
.. 




:contact_id: Contact, many2one



.. index::
  single: contact_id field
.. 




:address_ids: Partners Contacts, many2many



.. index::
  single: address_ids field
.. 




:crossovered_budget_line: Budget Lines, one2many



.. index::
  single: crossovered_budget_line field
.. 




:quantity_usable_total: Total Usable Quantity, char, readonly



.. index::
  single: quantity_usable_total field
.. 




:proposition_ids: Proposition, one2many



.. index::
  single: proposition_ids field
.. 




:last_worked_date: Date of Last Cost/Work, date, readonly

    *Date of the latest work done on this account.*

.. index::
  single: last_worked_date field
.. 




:dealer_id: Dealer, many2one

    *The dealer is the partner the campaign is planned for*

.. index::
  single: dealer_id field
.. 




:manufacturing_cost_ids: Manufacturing Costs, one2many



.. index::
  single: manufacturing_cost_ids field
.. 




:company_id: Company, many2one, required



.. index::
  single: company_id field
.. 




:parent_id: Parent analytic account, many2one



.. index::
  single: parent_id field
.. 




:pricelist_id: Sale Pricelist, many2one



.. index::
  single: pricelist_id field
.. 




:project_id: Project, many2one, readonly

    *Generating the Retro Planning will create and assign the different tasks used to plan and manage the campaign*

.. index::
  single: project_id field
.. 




:ca_to_invoice: Uninvoiced Amount, float, readonly

    *If invoice from analytic account, the remaining amount you can invoice to the customer based on the total costs.*

.. index::
  single: ca_to_invoice field
.. 




:cust_file_task_ids: Customer Files tasks, one2many



.. index::
  single: cust_file_task_ids field
.. 




:child_ids: Childs Accounts, one2many



.. index::
  single: child_ids field
.. 




:quantity_wanted_total: Total Wanted Quantity, char, readonly



.. index::
  single: quantity_wanted_total field
.. 




:user_ids: User, many2many, readonly



.. index::
  single: user_ids field
.. 




:campaign_group_id: Campaign group, many2one



.. index::
  single: campaign_group_id field
.. 




:item_task_ids: Items Procurement tasks, one2many



.. index::
  single: item_task_ids field
.. 




:theorical_margin: Theorical Margin, float, readonly

    *Computed using the formula: Theorial Revenue - Total Costs*

.. index::
  single: theorical_margin field
.. 




:dtp_task_ids: DTP tasks, one2many



.. index::
  single: dtp_task_ids field
.. 




:name: Account name, char, required



.. index::
  single: name field
.. 




:notes: Notes, text



.. index::
  single: notes field
.. 




:translation_state: Translation Status, selection, readonly



.. index::
  single: translation_state field
.. 




:quantity_planned_total: Total planned Quantity, char, readonly



.. index::
  single: quantity_planned_total field
.. 




:remaining_hours: Remaining Hours, float, readonly

    *Computed using the formula: Maximum Quantity - Hours Tot.*

.. index::
  single: remaining_hours field
.. 




:last_worked_invoiced_date: Date of Last Invoiced Cost, date, readonly

    *If invoice from the costs, this is the date of the latest work or cost that have been invoiced.*

.. index::
  single: last_worked_invoiced_date field
.. 




:customer_file_state: Customers Files Status, selection, readonly



.. index::
  single: customer_file_state field
.. 




:last_invoice_date: Last Invoice Date, date, readonly

    *Date of the last invoice created for this analytic account.*

.. index::
  single: last_invoice_date field
.. 




:dtp_purchase_line_ids: DTP Purchase Lines, one2many



.. index::
  single: dtp_purchase_line_ids field
.. 




:package_ok: Used in Package, boolean



.. index::
  single: package_ok field
.. 




:partner_id: Associated partner, many2one



.. index::
  single: partner_id field
.. 




:analytic_account_id: Analytic Account, many2one



.. index::
  single: analytic_account_id field
.. 




:revenue_per_hour: Revenue per Hours (real), float, readonly

    *Computed using the formula: Invoiced Amount / Hours Tot.*

.. index::
  single: revenue_per_hour field
.. 




:total_cost: Total Costs, float, readonly

    *Total of costs for this account. It includes real costs (from invoices) and indirect costs, like time spent on timesheets.*

.. index::
  single: total_cost field
.. 




:country_id: Country, many2one, required

    *The language and currency will be automaticaly assigned if they are defined for the country*

.. index::
  single: country_id field
.. 




:state: State, selection, required



.. index::
  single: state field
.. 




:debit: Debit, float, readonly



.. index::
  single: debit field
.. 




:amount_invoiced: Invoiced Amount, float, readonly

    *Total invoiced*

.. index::
  single: amount_invoiced field
.. 




:planning_state: Planning Status, selection, readonly



.. index::
  single: planning_state field
.. 




:user_product_ids: Users/Products Rel., one2many



.. index::
  single: user_product_ids field
.. 




:manufacturing_responsible_id: Responsible, many2one



.. index::
  single: manufacturing_responsible_id field
.. 




:overlay_id: Overlay, many2one



.. index::
  single: overlay_id field
.. 




:active: Active, boolean



.. index::
  single: active field
.. 




:real_margin_rate: Real Margin Rate (%), float, readonly

    *Computes using the formula: (Real Margin / Total Costs) * 100.*

.. index::
  single: real_margin_rate field
.. 




:credit: Credit, float, readonly



.. index::
  single: credit field
.. 




:month_ids: Month, many2many, readonly



.. index::
  single: month_ids field
.. 




:line_ids: Analytic entries, one2many



.. index::
  single: line_ids field
.. 




:items_state: Items Status, selection, readonly



.. index::
  single: items_state field
.. 




:trademark_id: Trademark, many2one



.. index::
  single: trademark_id field
.. 




:amount_max: Max. Invoice Price, float



.. index::
  single: amount_max field
.. 




:campaign_type: Type, many2one



.. index::
  single: campaign_type field
.. 




:dtp_state: DTP Status, selection, readonly



.. index::
  single: dtp_state field
.. 




:user_id: Account Manager, many2one



.. index::
  single: user_id field
.. 




:dtp_responsible_id: Responsible, many2one



.. index::
  single: dtp_responsible_id field
.. 




:manufacturing_purchase_line_ids: Manufacturing Purchase Lines, one2many



.. index::
  single: manufacturing_purchase_line_ids field
.. 




:type: Account type, selection



.. index::
  single: type field
.. 




:manufacturing_product: Manufacturing Product, many2one



.. index::
  single: manufacturing_product field
.. 




:offer_id: Offer, many2one, required

    *Choose the commercial offer to use with this campaign, only offers in open state can be assigned*

.. index::
  single: offer_id field
.. 




:ca_invoiced: Invoiced Amount, float, readonly

    *Total customer invoiced amount for this account.*

.. index::
  single: ca_invoiced field
.. 




:hours_quantity: Hours Tot, float, readonly

    *Number of hours you spent on the analytic account (from timesheet). It computes on all journal of type 'general'.*

.. index::
  single: hours_quantity field
.. 




:manufacturing_state: Manufacturing Status, selection, readonly



.. index::
  single: manufacturing_state field
.. 




:ca_theorical: Theorical Revenue, float, readonly

    *Based on the costs you had on the project, what would have been the revenue if all these costs have been invoiced at the normal sale price provided by the pricelist.*

.. index::
  single: ca_theorical field
.. 




:currency_id: Currency, many2one



.. index::
  single: currency_id field
.. 




:dtp_making_time: Making Time, float, readonly



.. index::
  single: dtp_making_time field
.. 




:to_invoice: Reinvoice Costs, many2one

    *Check this field if you plan to automatically generate invoices based on the costs in this analytic account: timesheets, expenses, ...You can configure an automatic invoice rate on analytic accounts.*

.. index::
  single: to_invoice field
.. 




:balance: Balance, float, readonly



.. index::
  single: balance field
.. 




:quantity_delivered_total: Total Delivered Quantity, char, readonly



.. index::
  single: quantity_delivered_total field
.. 




:item_responsible_id: Responsible, many2one



.. index::
  single: item_responsible_id field
.. 




:quantity_max: Maximal quantity, float



.. index::
  single: quantity_max field
.. 




:deduplicator_id: Deduplicator, many2one

    *The deduplicator is a partner responsible to remove identical addresses from the customers list*

.. index::
  single: deduplicator_id field
.. 




:company_currency_id: Currency, many2one, readonly



.. index::
  single: company_currency_id field
.. 




:hours_qtt_non_invoiced: Uninvoiced Hours, float, readonly

    *Number of hours (from journal of type 'general') that can be invoiced if you invoice based on analytic account.*

.. index::
  single: hours_qtt_non_invoiced field
.. 




:files_responsible_id: Responsible, many2one



.. index::
  single: files_responsible_id field
.. 




:date_start: Date Start, date



.. index::
  single: date_start field
.. 




:forwarding_charge: Forwarding Charge, float



.. index::
  single: forwarding_charge field
.. 




:lang_id: Language, many2one



.. index::
  single: lang_id field
.. 




:complete_name: Account Name, char, readonly



.. index::
  single: complete_name field
.. 




:real_margin: Real Margin, float, readonly

    *Computed using the formula: Invoiced Amount - Total Costs.*

.. index::
  single: real_margin field
.. 




:hours_qtt_invoiced: Invoiced Hours, float, readonly

    *Number of hours that can be invoiced plus those that already have been invoiced.*

.. index::
  single: hours_qtt_invoiced field
.. 




:router_id: Router, many2one

    *The router is the partner who will send the mailing to the final customer*

.. index::
  single: router_id field
.. 




:description: Description, text



.. index::
  single: description field
.. 




:manufacturing_task_ids: Manufacturing tasks, one2many



.. index::
  single: manufacturing_task_ids field
.. 




:remaining_ca: Remaining Revenue, float, readonly

    *Computed using the formula: Max Invoice Price - Invoiced Amount.*

.. index::
  single: remaining_ca field
.. 




:responsible_id: Responsible, many2one



.. index::
  single: responsible_id field
.. 




:date: Date End, date



.. index::
  single: date field
.. 




:item_purchase_line_ids: Items Purchase Lines, one2many



.. index::
  single: item_purchase_line_ids field
.. 




:code1: Code, char, readonly



.. index::
  single: code1 field
.. 




:payment_methods: Payment Methods, many2many



.. index::
  single: payment_methods field
.. 




:cust_file_purchase_line_ids: Customer Files Purchase Lines, one2many



.. index::
  single: cust_file_purchase_line_ids field
.. 




:journal_rate_ids: Invoicing Rate per Journal, one2many



.. index::
  single: journal_rate_ids field
.. 




:quantity: Quantity, float, readonly



.. index::
  single: quantity field
.. 



Object: dm.campaign.proposition
###############################

.. index::
  single: dm.campaign.proposition object
.. 


:initial_proposition_id: Initial proposition, many2one, readonly



.. index::
  single: initial_proposition_id field
.. 




:code: Account code, char



.. index::
  single: code field
.. 




:last_worked_invoiced_date: Date of Last Invoiced Cost, date, readonly

    *If invoice from the costs, this is the date of the latest work or cost that have been invoiced.*

.. index::
  single: last_worked_invoiced_date field
.. 




:ca_to_invoice: Uninvoiced Amount, float, readonly

    *If invoice from analytic account, the remaining amount you can invoice to the customer based on the total costs.*

.. index::
  single: ca_to_invoice field
.. 




:quantity_max: Maximal quantity, float



.. index::
  single: quantity_max field
.. 




:quantity_usable: Usable Quantity, char, readonly

    *The usable quantity is the number of addresses you have after delivery, deduplication and cleaning.*

.. index::
  single: quantity_usable field
.. 




:contact_id: Contact, many2one



.. index::
  single: contact_id field
.. 




:company_currency_id: Currency, many2one, readonly



.. index::
  single: company_currency_id field
.. 




:date: Date End, date



.. index::
  single: date field
.. 




:last_invoice_date: Last Invoice Date, date, readonly

    *Date of the last invoice created for this analytic account.*

.. index::
  single: last_invoice_date field
.. 




:crossovered_budget_line: Budget Lines, one2many



.. index::
  single: crossovered_budget_line field
.. 




:amount_max: Max. Invoice Price, float



.. index::
  single: amount_max field
.. 




:package_ok: Used in Package, boolean



.. index::
  single: package_ok field
.. 




:hours_qtt_non_invoiced: Uninvoiced Hours, float, readonly

    *Number of hours (from journal of type 'general') that can be invoiced if you invoice based on analytic account.*

.. index::
  single: hours_qtt_non_invoiced field
.. 




:keep_prices: Keep Prices At Duplication, boolean



.. index::
  single: keep_prices field
.. 




:partner_id: Associated partner, many2one



.. index::
  single: partner_id field
.. 




:proposition_type: Type, selection



.. index::
  single: proposition_type field
.. 




:analytic_account_id: Analytic Account, many2one



.. index::
  single: analytic_account_id field
.. 




:last_worked_date: Date of Last Cost/Work, date, readonly

    *Date of the latest work done on this account.*

.. index::
  single: last_worked_date field
.. 




:starting_mail_price: Starting Mail Price, float



.. index::
  single: starting_mail_price field
.. 




:user_id: Account Manager, many2one



.. index::
  single: user_id field
.. 




:item_ids: Catalogue, one2many



.. index::
  single: item_ids field
.. 




:to_invoice: Reinvoice Costs, many2one

    *Check this field if you plan to automatically generate invoices based on the costs in this analytic account: timesheets, expenses, ...You can configure an automatic invoice rate on analytic accounts.*

.. index::
  single: to_invoice field
.. 




:total_cost: Total Costs, float, readonly

    *Total of costs for this account. It includes real costs (from invoices) and indirect costs, like time spent on timesheets.*

.. index::
  single: total_cost field
.. 




:date_start: Date Start, date



.. index::
  single: date_start field
.. 




:company_id: Company, many2one, required



.. index::
  single: company_id field
.. 




:segment_ids: Segment, one2many



.. index::
  single: segment_ids field
.. 




:parent_id: Parent analytic account, many2one



.. index::
  single: parent_id field
.. 




:state: State, selection, required



.. index::
  single: state field
.. 




:quantity_planned: planned Quantity, char, readonly

    *The planned quantity is an estimation of the usable quantity of addresses you  will get after delivery, deduplication and cleaning
    This is usually the quantity used to order the manufacturing of the mailings*

.. index::
  single: quantity_planned field
.. 




:complete_name: Account Name, char, readonly



.. index::
  single: complete_name field
.. 




:real_margin: Real Margin, float, readonly

    *Computed using the formula: Invoiced Amount - Total Costs.*

.. index::
  single: real_margin field
.. 




:debit: Debit, float, readonly



.. index::
  single: debit field
.. 




:forwarding_charge: Forwarding Charge, float



.. index::
  single: forwarding_charge field
.. 




:pricelist_id: Sale Pricelist, many2one



.. index::
  single: pricelist_id field
.. 




:type: Account type, selection



.. index::
  single: type field
.. 




:quantity: Quantity, float, readonly



.. index::
  single: quantity field
.. 




:manufacturing_costs: Manufacturing Costs, float



.. index::
  single: manufacturing_costs field
.. 




:journal_rate_ids: Invoicing Rate per Journal, one2many



.. index::
  single: journal_rate_ids field
.. 




:description: Description, text



.. index::
  single: description field
.. 




:amount_invoiced: Invoiced Amount, float, readonly

    *Total invoiced*

.. index::
  single: amount_invoiced field
.. 




:forwarding_charges: Forwarding Charges, float



.. index::
  single: forwarding_charges field
.. 




:credit: Credit, float, readonly



.. index::
  single: credit field
.. 




:child_ids: Childs Accounts, one2many



.. index::
  single: child_ids field
.. 




:user_product_ids: Users/Products Rel., one2many



.. index::
  single: user_product_ids field
.. 




:ca_invoiced: Invoiced Amount, float, readonly

    *Total customer invoiced amount for this account.*

.. index::
  single: ca_invoiced field
.. 




:sale_rate: Sale Rate (%), float

    *This is the planned sale rate (in percent) for this commercial proposition*

.. index::
  single: sale_rate field
.. 




:user_ids: User, many2many, readonly



.. index::
  single: user_ids field
.. 




:remaining_ca: Remaining Revenue, float, readonly

    *Computed using the formula: Max Invoice Price - Invoiced Amount.*

.. index::
  single: remaining_ca field
.. 




:quantity_delivered: Delivered Quantity, char, readonly

    *The delivered quantity is the number of addresses you receive from the broker.*

.. index::
  single: quantity_delivered field
.. 




:code1: Code, char, readonly



.. index::
  single: code1 field
.. 




:hours_qtt_invoiced: Invoiced Hours, float, readonly

    *Number of hours that can be invoiced plus those that already have been invoiced.*

.. index::
  single: hours_qtt_invoiced field
.. 




:active: Active, boolean



.. index::
  single: active field
.. 




:hours_quantity: Hours Tot, float, readonly

    *Number of hours you spent on the analytic account (from timesheet). It computes on all journal of type 'general'.*

.. index::
  single: hours_quantity field
.. 




:theorical_margin: Theorical Margin, float, readonly

    *Computed using the formula: Theorial Revenue - Total Costs*

.. index::
  single: theorical_margin field
.. 




:ca_theorical: Theorical Revenue, float, readonly

    *Based on the costs you had on the project, what would have been the revenue if all these costs have been invoiced at the normal sale price provided by the pricelist.*

.. index::
  single: ca_theorical field
.. 




:quantity_wanted: Wanted Quantity, char, readonly

    *The wanted quantity is the number of addresses you wish to get for that segment.
    This is usually the quantity used to order Customers Lists
    The wanted quantity could be AAA for All Addresses Available*

.. index::
  single: quantity_wanted field
.. 




:sm_price: Starting Mail Price, float



.. index::
  single: sm_price field
.. 




:keep_segments: Keep Segments, boolean



.. index::
  single: keep_segments field
.. 




:name: Account name, char, required



.. index::
  single: name field
.. 




:customer_pricelist_id: Items Pricelist, many2one



.. index::
  single: customer_pricelist_id field
.. 




:notes: Notes, text



.. index::
  single: notes field
.. 




:force_sm_price: Force Starting Mail Price, boolean



.. index::
  single: force_sm_price field
.. 




:address_ids: Partners Contacts, many2many



.. index::
  single: address_ids field
.. 




:real_margin_rate: Real Margin Rate (%), float, readonly

    *Computes using the formula: (Real Margin / Total Costs) * 100.*

.. index::
  single: real_margin_rate field
.. 




:revenue_per_hour: Revenue per Hours (real), float, readonly

    *Computed using the formula: Invoiced Amount / Hours Tot.*

.. index::
  single: revenue_per_hour field
.. 




:month_ids: Month, many2many, readonly



.. index::
  single: month_ids field
.. 




:quantity_real: Real Quantity, char, readonly

    *The real quantity is the number of addresses you really get in the file.*

.. index::
  single: quantity_real field
.. 




:payment_methods: Payment Methods, many2many



.. index::
  single: payment_methods field
.. 




:line_ids: Analytic entries, one2many



.. index::
  single: line_ids field
.. 




:balance: Balance, float, readonly



.. index::
  single: balance field
.. 




:camp_id: Campaign, many2one, required



.. index::
  single: camp_id field
.. 




:remaining_hours: Remaining Hours, float, readonly

    *Computed using the formula: Maximum Quantity - Hours Tot.*

.. index::
  single: remaining_hours field
.. 



Object: The origin of the adresses of a list
############################################

.. index::
  single: The origin of the adresses of a list object
.. 


:code: Code, char, required



.. index::
  single: code field
.. 




:name: Name, char, required



.. index::
  single: name field
.. 



Object: Type of the adress list
###############################

.. index::
  single: Type of the adress list object
.. 


:code: Code, char, required



.. index::
  single: code field
.. 




:name: Name, char, required



.. index::
  single: name field
.. 



Object: A list of addresses proposed by an adresses broker
##########################################################

.. index::
  single: A list of addresses proposed by an adresses broker object
.. 


:other_cost: Other Cost, float



.. index::
  single: other_cost field
.. 




:selection_cost: Selection Cost Per Thousand, float



.. index::
  single: selection_cost field
.. 




:broker_cost: Broker Cost, float

    *The amount given to the broker for the list renting*

.. index::
  single: broker_cost field
.. 




:code: Code, char, required



.. index::
  single: code field
.. 




:product_id: Product, many2one, required



.. index::
  single: product_id field
.. 




:per_thousand_price: Price per Thousand, float



.. index::
  single: per_thousand_price field
.. 




:update_frq: Update Frequency, integer



.. index::
  single: update_frq field
.. 




:currency_id: Currency, many2one



.. index::
  single: currency_id field
.. 




:country_id: Country, many2one



.. index::
  single: country_id field
.. 




:broker_discount: Broker Discount (%), float



.. index::
  single: broker_discount field
.. 




:recruiting_origin: Recruiting Origin, many2one

    *Origin of the recruiting of the adresses*

.. index::
  single: recruiting_origin field
.. 




:broker_id: Broker, many2one



.. index::
  single: broker_id field
.. 




:delivery_cost: Delivery Cost, float



.. index::
  single: delivery_cost field
.. 




:list_type: Type, many2one



.. index::
  single: list_type field
.. 




:invoice_base: Invoicing based on, selection

    *Net or raw quantity on which is based the final invoice depending of the term negociated with the broker.
    Net : Usable quantity after deduplication
    Raw : Delivered quantity
    Real : Realy used qunatity*

.. index::
  single: invoice_base field
.. 




:owner_id: Owner, many2one



.. index::
  single: owner_id field
.. 




:notes: Description, text



.. index::
  single: notes field
.. 




:name: Name, char, required



.. index::
  single: name field
.. 



Object: A File of addresses delivered by an addresses broker
############################################################

.. index::
  single: A File of addresses delivered by an addresses broker object
.. 


:segment_ids: Segments, one2many, readonly



.. index::
  single: segment_ids field
.. 




:code: Code, char, required



.. index::
  single: code field
.. 




:customers_list_id: Customers List, many2one



.. index::
  single: customers_list_id field
.. 




:delivery_date: Delivery Date, date



.. index::
  single: delivery_date field
.. 




:name: Name, char, required



.. index::
  single: name field
.. 



Object: A subset of addresses coming from a customers file
##########################################################

.. index::
  single: A subset of addresses coming from a customers file object
.. 


:code: Account code, char



.. index::
  single: code field
.. 




:last_worked_invoiced_date: Date of Last Invoiced Cost, date, readonly

    *If invoice from the costs, this is the date of the latest work or cost that have been invoiced.*

.. index::
  single: last_worked_invoiced_date field
.. 




:ca_to_invoice: Uninvoiced Amount, float, readonly

    *If invoice from analytic account, the remaining amount you can invoice to the customer based on the total costs.*

.. index::
  single: ca_to_invoice field
.. 




:analytic_account_id: Analytic Account, many2one



.. index::
  single: analytic_account_id field
.. 




:quantity_cleaned_cleaner: Cleaned Quantity, integer

    *The quantity of wrong addresses removed by the cleaner.*

.. index::
  single: quantity_cleaned_cleaner field
.. 




:quantity_dedup_cleaner: Deduplication Quantity, integer

    *The quantity of duplicated addresses removed by the cleaner.*

.. index::
  single: quantity_dedup_cleaner field
.. 




:quantity_max: Maximal quantity, float



.. index::
  single: quantity_max field
.. 




:quantity_usable: Usable Quantity, integer, readonly

    *The usable quantity is the number of addresses you have after delivery, deduplication and cleaning.*

.. index::
  single: quantity_usable field
.. 




:contact_id: Contact, many2one



.. index::
  single: contact_id field
.. 




:company_currency_id: Currency, many2one, readonly



.. index::
  single: company_currency_id field
.. 




:date: Date End, date



.. index::
  single: date field
.. 




:last_invoice_date: Last Invoice Date, date, readonly

    *Date of the last invoice created for this analytic account.*

.. index::
  single: last_invoice_date field
.. 




:crossovered_budget_line: Budget Lines, one2many



.. index::
  single: crossovered_budget_line field
.. 




:amount_max: Max. Invoice Price, float



.. index::
  single: amount_max field
.. 




:package_ok: Used in Package, boolean



.. index::
  single: package_ok field
.. 




:hours_qtt_non_invoiced: Uninvoiced Hours, float, readonly

    *Number of hours (from journal of type 'general') that can be invoiced if you invoice based on analytic account.*

.. index::
  single: hours_qtt_non_invoiced field
.. 




:partner_id: Associated partner, many2one



.. index::
  single: partner_id field
.. 




:all_add_avail: All Adresses Available, boolean

    *Used to order all adresses available in the customers list based on the segmentation criteria*

.. index::
  single: all_add_avail field
.. 




:split_id: Split, many2one



.. index::
  single: split_id field
.. 




:note: Notes, text



.. index::
  single: note field
.. 




:last_worked_date: Date of Last Cost/Work, date, readonly

    *Date of the latest work done on this account.*

.. index::
  single: last_worked_date field
.. 




:start_census: Start Census (days), integer

    *The recency is the time since the latest purchase.
    For example : A 0-30 recency means all the customers that have purchased in the last 30 days*

.. index::
  single: start_census field
.. 




:user_id: Account Manager, many2one



.. index::
  single: user_id field
.. 




:to_invoice: Reinvoice Costs, many2one

    *Check this field if you plan to automatically generate invoices based on the costs in this analytic account: timesheets, expenses, ...You can configure an automatic invoice rate on analytic accounts.*

.. index::
  single: to_invoice field
.. 




:total_cost: Total Costs, float, readonly

    *Total of costs for this account. It includes real costs (from invoices) and indirect costs, like time spent on timesheets.*

.. index::
  single: total_cost field
.. 




:quantity_purged: Purged Quantity, integer, readonly

    *The purged quantity is the number of addresses removed from deduplication and cleaning.*

.. index::
  single: quantity_purged field
.. 




:date_start: Date Start, date



.. index::
  single: date_start field
.. 




:customers_file_id: Customers File, many2one, readonly



.. index::
  single: customers_file_id field
.. 




:company_id: Company, many2one, required



.. index::
  single: company_id field
.. 




:proposition_id: Proposition, many2one



.. index::
  single: proposition_id field
.. 




:reuse_id: Reuse, many2one



.. index::
  single: reuse_id field
.. 




:parent_id: Parent analytic account, many2one



.. index::
  single: parent_id field
.. 




:state: State, selection, required



.. index::
  single: state field
.. 




:customers_list_id: Customers List, many2one, required



.. index::
  single: customers_list_id field
.. 




:complete_name: Account Name, char, readonly



.. index::
  single: complete_name field
.. 




:real_margin: Real Margin, float, readonly

    *Computed using the formula: Invoiced Amount - Total Costs.*

.. index::
  single: real_margin field
.. 




:debit: Debit, float, readonly



.. index::
  single: debit field
.. 




:pricelist_id: Sale Pricelist, many2one



.. index::
  single: pricelist_id field
.. 




:type: Account type, selection



.. index::
  single: type field
.. 




:quantity: Quantity, float, readonly



.. index::
  single: quantity field
.. 




:quantity_cleaned_dedup: Cleaned Quantity, integer

    *The quantity of wrong addresses removed by the deduplicator.*

.. index::
  single: quantity_cleaned_dedup field
.. 




:quantity_dedup_dedup: Deduplication Quantity, integer

    *The quantity of duplicated addresses removed by the deduplicator.*

.. index::
  single: quantity_dedup_dedup field
.. 




:journal_rate_ids: Invoicing Rate per Journal, one2many



.. index::
  single: journal_rate_ids field
.. 




:description: Description, text



.. index::
  single: description field
.. 




:amount_invoiced: Invoiced Amount, float, readonly

    *Total invoiced*

.. index::
  single: amount_invoiced field
.. 




:quantity_planned: planned Quantity, integer

    *The planned quantity is an estimation of the usable quantity of addresses you  will get after delivery, deduplication and cleaning
    This is usually the quantity used to order the manufacturing of the mailings*

.. index::
  single: quantity_planned field
.. 




:credit: Credit, float, readonly



.. index::
  single: credit field
.. 




:child_ids: Childs Accounts, one2many



.. index::
  single: child_ids field
.. 




:user_product_ids: Users/Products Rel., one2many



.. index::
  single: user_product_ids field
.. 




:ca_invoiced: Invoiced Amount, float, readonly

    *Total customer invoiced amount for this account.*

.. index::
  single: ca_invoiced field
.. 




:user_ids: User, many2many, readonly



.. index::
  single: user_ids field
.. 




:remaining_ca: Remaining Revenue, float, readonly

    *Computed using the formula: Max Invoice Price - Invoiced Amount.*

.. index::
  single: remaining_ca field
.. 




:quantity_delivered: Delivered Quantity, integer

    *The delivered quantity is the number of addresses you receive from the broker.*

.. index::
  single: quantity_delivered field
.. 




:code1: Code, char, readonly



.. index::
  single: code1 field
.. 




:hours_qtt_invoiced: Invoiced Hours, float, readonly

    *Number of hours that can be invoiced plus those that already have been invoiced.*

.. index::
  single: hours_qtt_invoiced field
.. 




:active: Active, boolean



.. index::
  single: active field
.. 




:hours_quantity: Hours Tot, float, readonly

    *Number of hours you spent on the analytic account (from timesheet). It computes on all journal of type 'general'.*

.. index::
  single: hours_quantity field
.. 




:deduplication_level: Deduplication Level, integer

    *The deduplication level defines the order in which the deduplication takes place.*

.. index::
  single: deduplication_level field
.. 




:theorical_margin: Theorical Margin, float, readonly

    *Computed using the formula: Theorial Revenue - Total Costs*

.. index::
  single: theorical_margin field
.. 




:ca_theorical: Theorical Revenue, float, readonly

    *Based on the costs you had on the project, what would have been the revenue if all these costs have been invoiced at the normal sale price provided by the pricelist.*

.. index::
  single: ca_theorical field
.. 




:quantity_wanted: Wanted Quantity, integer

    *The wanted quantity is the number of addresses you wish to get for that segment.
    This is usually the quantity used to order Customers Lists
    The wanted quantity could be AAA for All Addresses Available*

.. index::
  single: quantity_wanted field
.. 




:name: Account name, char, required



.. index::
  single: name field
.. 




:end_census: End Census (days), integer



.. index::
  single: end_census field
.. 




:address_ids: Partners Contacts, many2many



.. index::
  single: address_ids field
.. 




:real_margin_rate: Real Margin Rate (%), float, readonly

    *Computes using the formula: (Real Margin / Total Costs) * 100.*

.. index::
  single: real_margin_rate field
.. 




:revenue_per_hour: Revenue per Hours (real), float, readonly

    *Computed using the formula: Invoiced Amount / Hours Tot.*

.. index::
  single: revenue_per_hour field
.. 




:segmentation_criteria: Segmentation Criteria, text



.. index::
  single: segmentation_criteria field
.. 




:month_ids: Month, many2many, readonly



.. index::
  single: month_ids field
.. 




:quantity_real: Real Quantity, integer

    *The real quantity is the number of addresses that are really in the customers file (by counting).*

.. index::
  single: quantity_real field
.. 




:line_ids: Analytic entries, one2many



.. index::
  single: line_ids field
.. 




:balance: Balance, float, readonly



.. index::
  single: balance field
.. 




:remaining_hours: Remaining Hours, float, readonly

    *Computed using the formula: Maximum Quantity - Hours Tot.*

.. index::
  single: remaining_hours field
.. 



Object: dm.campaign.proposition.item
####################################

.. index::
  single: dm.campaign.proposition.item object
.. 


:product_id: Product, many2one, required



.. index::
  single: product_id field
.. 




:price: Sale Price, float



.. index::
  single: price field
.. 




:qty_real: Real Quantity, integer



.. index::
  single: qty_real field
.. 




:proposition_id: Commercial Proposition, many2one



.. index::
  single: proposition_id field
.. 




:qty_planned: Planned Quantity, integer



.. index::
  single: qty_planned field
.. 




:item_type: Item Type, selection



.. index::
  single: item_type field
.. 




:offer_step_type_id: Offer Step Type, many2one



.. index::
  single: offer_step_type_id field
.. 




:notes: Notes, text



.. index::
  single: notes field
.. 



Object: dm.campaign.purchase_line
#################################

.. index::
  single: dm.campaign.purchase_line object
.. 


:type_document: Document Type, selection



.. index::
  single: type_document field
.. 




:campaign_group_id: Campaign Group, many2one



.. index::
  single: campaign_group_id field
.. 




:product_id: Product, many2one, required



.. index::
  single: product_id field
.. 




:togroup: Apply to Campaign Group, boolean



.. index::
  single: togroup field
.. 




:product_category: Product Category, selection



.. index::
  single: product_category field
.. 




:trigger: Trigger, selection



.. index::
  single: trigger field
.. 




:notes: Notes, text



.. index::
  single: notes field
.. 




:date_planned: Scheduled date, datetime, required



.. index::
  single: date_planned field
.. 




:campaign_id: Campaign, many2one



.. index::
  single: campaign_id field
.. 




:date_delivery: Delivery Date, datetime, readonly



.. index::
  single: date_delivery field
.. 




:uom_id: UOM, many2one, required



.. index::
  single: uom_id field
.. 




:desc_from_offer: Insert Description from Offer, boolean



.. index::
  single: desc_from_offer field
.. 




:state: State, selection, readonly



.. index::
  single: state field
.. 




:type_quantity: Quantity Type, selection



.. index::
  single: type_quantity field
.. 




:quantity_warning: Warning, char, readonly



.. index::
  single: quantity_warning field
.. 




:purchase_order_ids: Campaign Purchase Line, one2many



.. index::
  single: purchase_order_ids field
.. 




:date_order: Order date, datetime, readonly



.. index::
  single: date_order field
.. 




:type: Type, selection



.. index::
  single: type field
.. 




:quantity: Total Quantity, integer, required



.. index::
  single: quantity field
.. 



Object: dm.campaign.manufacturing_cost
######################################

.. index::
  single: dm.campaign.manufacturing_cost object
.. 


:amount: Amount, float



.. index::
  single: amount field
.. 




:name: Description, char, required



.. index::
  single: name field
.. 




:campaign_id: Campaign, many2one



.. index::
  single: campaign_id field
.. 



Object: dm.campaign.proposition.prices_progression
##################################################

.. index::
  single: dm.campaign.proposition.prices_progression object
.. 


:percent_prog: Percentage Prices Progression, float



.. index::
  single: percent_prog field
.. 




:fixed_prog: Fixed Prices Progression, float



.. index::
  single: fixed_prog field
.. 




:name: Name, char, required



.. index::
  single: name field
.. 



Object: dm.order
################

.. index::
  single: dm.order object
.. 


:customer_code: Customer Code, char



.. index::
  single: customer_code field
.. 




:zip: Zip Code, char



.. index::
  single: zip field
.. 




:segment_code: Segment Code, char



.. index::
  single: segment_code field
.. 




:country: Country, char



.. index::
  single: country field
.. 




:offer_step_code: Offer Step Code, char



.. index::
  single: offer_step_code field
.. 




:title: Title, char



.. index::
  single: title field
.. 




:customer_firstname: First Name, char



.. index::
  single: customer_firstname field
.. 




:customer_add4: Address4, char



.. index::
  single: customer_add4 field
.. 




:state: Status, selection, readonly



.. index::
  single: state field
.. 




:zip_summary: Zip Summary, char



.. index::
  single: zip_summary field
.. 




:customer_lastname: Last Name, char



.. index::
  single: customer_lastname field
.. 




:customer_add1: Address1, char



.. index::
  single: customer_add1 field
.. 




:raw_datas: Raw Datas, char



.. index::
  single: raw_datas field
.. 




:distribution_office: Distribution Office, char



.. index::
  single: distribution_office field
.. 




:customer_add2: Address2, char



.. index::
  single: customer_add2 field
.. 




:customer_add3: Address3, char



.. index::
  single: customer_add3 field
.. 



Object: res.partner
###################

.. index::
  single: res.partner object
.. 


:ean13: EAN13, char



.. index::
  single: ean13 field
.. 




:property_account_position: Fiscal Position, many2one

    *The fiscal position will determine taxes and the accounts used for the the partner.*

.. index::
  single: property_account_position field
.. 




:ref_companies: Companies that refers to partner, one2many



.. index::
  single: ref_companies field
.. 




:canal_id: Favourite Channel, many2one



.. index::
  single: canal_id field
.. 




:property_product_pricelist: Sale Pricelist, many2one

    *This pricelist will be used, instead of the default one,                     for sales to the current partner*

.. index::
  single: property_product_pricelist field
.. 




:name_official: Official Name, char



.. index::
  single: name_official field
.. 




:title: Title, char



.. index::
  single: title field
.. 




:parent_id: Main Company, many2one



.. index::
  single: parent_id field
.. 




:membership_cancel: Cancel membership date, date, readonly



.. index::
  single: membership_cancel field
.. 




:alert_advertising: Adv.Alert, boolean

    *Partners description to be shown when inserting new advertising sale*

.. index::
  single: alert_advertising field
.. 




:decoy_for_campaign: Used for Campaigns, boolean

    *Define if this decoy address can be used with campaigns*

.. index::
  single: decoy_for_campaign field
.. 




:import_procent: Import (%), integer



.. index::
  single: import_procent field
.. 




:client_media_ids: Client for Media, many2many



.. index::
  single: client_media_ids field
.. 




:lastname: Last Name, char



.. index::
  single: lastname field
.. 




:child_ids: Partner Ref., one2many



.. index::
  single: child_ids field
.. 




:payment_type_customer: Payment type, many2one

    *Payment type of the customer*

.. index::
  single: payment_type_customer field
.. 




:export_year: Export date, date

    *year of the export_procent value*

.. index::
  single: export_year field
.. 




:name: Name, char, required



.. index::
  single: name field
.. 




:decoy_external_ref: External Reference, char

    *The reference of the decoy address for the owner*

.. index::
  single: decoy_external_ref field
.. 




:debit_limit: Payable Limit, float



.. index::
  single: debit_limit field
.. 




:property_account_receivable: Account Receivable, many2one, required

    *This account will be used, instead of the default one, as the receivable account for the current partner*

.. index::
  single: property_account_receivable field
.. 




:domiciliation_bool: Domiciliation, boolean



.. index::
  single: domiciliation_bool field
.. 




:decoy_for_renting: Used for File Renting, boolean

    *Define if this decoy address can be used with used with customers files renting*

.. index::
  single: decoy_for_renting field
.. 




:article_ids: Articles, many2many



.. index::
  single: article_ids field
.. 




:dir_exclude: Dir. exclude, boolean

    *Exclusion from the Members directory*

.. index::
  single: dir_exclude field
.. 




:logo: Logo, binary



.. index::
  single: logo field
.. 




:name_old: Former Name, char



.. index::
  single: name_old field
.. 




:activity_description: Activity Description, text



.. index::
  single: activity_description field
.. 




:alert_events: Event Alert, boolean

    *Partners description to be shown when inserting new subscription to a meeting*

.. index::
  single: alert_events field
.. 




:invoice_special: Invoice Special, boolean



.. index::
  single: invoice_special field
.. 




:state_id2: Customer State, many2one

    *status of the partner as a customer*

.. index::
  single: state_id2 field
.. 




:debit: Total Payable, float, readonly

    *Total amount you have to pay to this supplier.*

.. index::
  single: debit field
.. 




:supplier: Supplier, boolean

    *Check this box if the partner is a supplier. If it's not checked, purchase people will not see it when encoding a purchase order.*

.. index::
  single: supplier field
.. 




:ref: Code, char, readonly



.. index::
  single: ref field
.. 




:alert_others: Other alert, boolean

    *Partners description to be shown when inserting new sale not treated by _advertising, _events, _legalisations, _Membership*

.. index::
  single: alert_others field
.. 




:import_year: Import Date, date

    *year of the import_procent value*

.. index::
  single: import_year field
.. 




:free_member: Free member, boolean



.. index::
  single: free_member field
.. 




:membership_amount: Membership amount, float

    *The price negociated by the partner*

.. index::
  single: membership_amount field
.. 




:address: Addresses, one2many



.. index::
  single: address field
.. 




:active: Active, boolean



.. index::
  single: active field
.. 




:dir_date_publication: Publication Date, date



.. index::
  single: dir_date_publication field
.. 




:wall_exclusion: Not in Walloon DB, boolean

    *exclusion of this partner from the walloon database*

.. index::
  single: wall_exclusion field
.. 




:property_product_pricelist_purchase: Purchase Pricelist, many2one

    *This pricelist will be used, instead of the default one, for purchases from the current partner*

.. index::
  single: property_product_pricelist_purchase field
.. 




:country: Country, many2one



.. index::
  single: country field
.. 




:invoice_nbr: Nbr of invoice to print, integer

    *number of additive invoices to be printed for this customer*

.. index::
  single: invoice_nbr field
.. 




:invoice_paper: Bank Transfer Type, selection



.. index::
  single: invoice_paper field
.. 




:credit: Total Receivable, float, readonly

    *Total amount this customer owns you.*

.. index::
  single: credit field
.. 




:country_relation: Country Relation, one2many



.. index::
  single: country_relation field
.. 




:signature: Signature, binary



.. index::
  single: signature field
.. 




:invoice_public: Invoice Public, boolean



.. index::
  single: invoice_public field
.. 




:employee_nbr: Nbr of Employee (Area), integer

    *Nbr of Employee in the area of the CCI*

.. index::
  single: employee_nbr field
.. 




:comment: Notes, text



.. index::
  single: comment field
.. 




:decoy_owner: Decoy Address Owner, many2one

    *The partner this decoy address belongs to*

.. index::
  single: decoy_owner field
.. 




:country_ids: Allowed Countries, many2many



.. index::
  single: country_ids field
.. 




:language_ids: Other Languages, many2many



.. index::
  single: language_ids field
.. 




:header: Header (.odt), binary



.. index::
  single: header field
.. 




:member_lines: Membership, one2many



.. index::
  single: member_lines field
.. 




:alert_legalisations: Legal. Alert, boolean

    *Partners description to be shown when inserting new legalisation*

.. index::
  single: alert_legalisations field
.. 




:city: City, char



.. index::
  single: city field
.. 




:dir_date_last: Partner Data Date, date

    *Date of latest update of the partner data by itself (via paper or Internet)*

.. index::
  single: dir_date_last field
.. 




:user_id: Dedicated Salesman, many2one

    *The internal user that is in charge of communicating with this partner if any.*

.. index::
  single: user_id field
.. 




:magazine_subscription: Magazine subscription, selection



.. index::
  single: magazine_subscription field
.. 




:vat: VAT, char

    *Value Added Tax number. Check the box if the partner is subjected to the VAT. Used by the VAT legal statement.*

.. index::
  single: vat field
.. 




:website: Website, char



.. index::
  single: website field
.. 




:credit_limit: Credit Limit, float



.. index::
  single: credit_limit field
.. 




:answers_ids: Answers, many2many



.. index::
  single: answers_ids field
.. 




:alert_explanation: Warning, text



.. index::
  single: alert_explanation field
.. 




:customer: Customer, boolean

    *Check this box if the partner is a customer.*

.. index::
  single: customer field
.. 




:date_founded: Founding Date, date

    *Date of foundation of this company*

.. index::
  single: date_founded field
.. 




:employee_nbr_total: Nbr of Employee (Tot), integer

    *Nbr of Employee all around the world*

.. index::
  single: employee_nbr_total field
.. 




:dir_date_accept: Good to shoot Date, date

    *Date of last acceptation of Bon a Tirer*

.. index::
  single: dir_date_accept field
.. 




:membership_start: Start membership date, date, readonly



.. index::
  single: membership_start field
.. 




:alert_membership: Membership Alert, boolean

    *Partners description to be shown when inserting new ship sale*

.. index::
  single: alert_membership field
.. 




:membership_stop: Stop membership date, date, readonly



.. index::
  single: membership_stop field
.. 




:state_id: Partner State, many2one

    *status of activity of the partner*

.. index::
  single: state_id field
.. 




:relation_ids: Partner Relation, one2many



.. index::
  single: relation_ids field
.. 




:prospect_media_ids: Prospect for Media, many2many



.. index::
  single: prospect_media_ids field
.. 




:domiciliation: Domiciliation Number, char



.. index::
  single: domiciliation field
.. 




:date: Date, date



.. index::
  single: date field
.. 




:decoy_address: Decoy Address, boolean

    *A decoy address is an address used to identify unleagal uses of a customers file*

.. index::
  single: decoy_address field
.. 




:dir_presence: Dir. Presence, boolean

    *Present in the directory of the members*

.. index::
  single: dir_presence field
.. 




:property_account_payable: Account Payable, many2one, required

    *This account will be used, instead of the default one, as the payable account for the current partner*

.. index::
  single: property_account_payable field
.. 




:property_stock_supplier: Supplier Location, many2one

    *This stock location will be used, instead of the default one, as the source location for goods you receive from the current partner*

.. index::
  single: property_stock_supplier field
.. 




:training_authorization: Checks Auth., char

    *Formation and Language Checks Authorization number*

.. index::
  single: training_authorization field
.. 




:events: Events, one2many



.. index::
  single: events field
.. 




:associate_member: Associate member, many2one



.. index::
  single: associate_member field
.. 




:dir_name2: 1st Shortcut name , char

    *First shortcut in the members directory, pointing to the dir_name field*

.. index::
  single: dir_name2 field
.. 




:dir_name3: 2nd Shortcut name , char

    *Second shortcut*

.. index::
  single: dir_name3 field
.. 




:bank_ids: Banks, one2many



.. index::
  single: bank_ids field
.. 




:vat_subjected: VAT Legal Statement, boolean

    *Check this box if the partner is subjected to the VAT. It will be used for the VAT legal statement.*

.. index::
  single: vat_subjected field
.. 




:state_ids: Allowed States, many2many



.. index::
  single: state_ids field
.. 




:export_procent: Export(%), integer



.. index::
  single: export_procent field
.. 




:decoy_media_ids: decoy address for Media, many2many



.. index::
  single: decoy_media_ids field
.. 




:property_stock_customer: Customer Location, many2one

    *This stock location will be used, instead of the default one, as the destination location for goods you send to this partner*

.. index::
  single: property_stock_customer field
.. 




:lang: Language, selection

    *If the selected language is loaded in the system, all documents related to this partner will be printed in this language. If not, it will be english.*

.. index::
  single: lang field
.. 




:dir_name: Name in Member Dir., char

    *Name under wich the partner will be inserted in the members directory*

.. index::
  single: dir_name field
.. 




:membership_state: Current membership state, selection, readonly



.. index::
  single: membership_state field
.. 




:activity_code_ids: Activity Codes, one2many



.. index::
  single: activity_code_ids field
.. 




:magazine_subscription_source: Mag. Subscription Source, char



.. index::
  single: magazine_subscription_source field
.. 




:property_payment_term: Payment Term, many2one

    *This payment term will be used, instead of the default one, for the current partner*

.. index::
  single: property_payment_term field
.. 




:payment_type_supplier: Payment type, many2one

    *Payment type of the supplier*

.. index::
  single: payment_type_supplier field
.. 




:category_id: Categories, many2many



.. index::
  single: category_id field
.. 



Object: dm.customer.order
#########################

.. index::
  single: dm.customer.order object
.. 


:offer_step_id: Offer Step, many2one



.. index::
  single: offer_step_id field
.. 




:note: Notes, text



.. index::
  single: note field
.. 




:state: Status, selection, readonly



.. index::
  single: state field
.. 




:customer_id: Customer, many2one



.. index::
  single: customer_id field
.. 




:segment_id: Segment, many2one



.. index::
  single: segment_id field
.. 



Object: Segmentation
####################

.. index::
  single: Segmentation object
.. 


:customer_date_criteria_ids: Customers Date Criteria, one2many



.. index::
  single: customer_date_criteria_ids field
.. 




:order_text_criteria_ids: Customers Order Textual Criteria, one2many



.. index::
  single: order_text_criteria_ids field
.. 




:code: Code, char, required



.. index::
  single: code field
.. 




:name: Name, char, required



.. index::
  single: name field
.. 




:notes: Description, text



.. index::
  single: notes field
.. 




:order_boolean_criteria_ids: Customers Order Boolean Criteria, one2many



.. index::
  single: order_boolean_criteria_ids field
.. 




:order_numeric_criteria_ids: Customers Order Numeric Criteria, one2many



.. index::
  single: order_numeric_criteria_ids field
.. 




:customer_numeric_criteria_ids: Customers Numeric Criteria, one2many



.. index::
  single: customer_numeric_criteria_ids field
.. 




:customer_boolean_criteria_ids: Customers Boolean Criteria, one2many



.. index::
  single: customer_boolean_criteria_ids field
.. 




:sql_query: SQL Query, text



.. index::
  single: sql_query field
.. 




:order_date_criteria_ids: Customers Order Date Criteria, one2many



.. index::
  single: order_date_criteria_ids field
.. 




:customer_text_criteria_ids: Customers Textual Criteria, one2many



.. index::
  single: customer_text_criteria_ids field
.. 



Object: Customer Segmentation Textual Criteria
##############################################

.. index::
  single: Customer Segmentation Textual Criteria object
.. 


:operator: Operator, selection



.. index::
  single: operator field
.. 




:segmentation_id: Segmentation, many2one



.. index::
  single: segmentation_id field
.. 




:value: Value, char



.. index::
  single: value field
.. 




:field: Customers Field, many2one



.. index::
  single: field field
.. 



Object: Customer Segmentation Numeric Criteria
##############################################

.. index::
  single: Customer Segmentation Numeric Criteria object
.. 


:operator: Operator, selection



.. index::
  single: operator field
.. 




:segmentation_id: Segmentation, many2one



.. index::
  single: segmentation_id field
.. 




:value: Value, float



.. index::
  single: value field
.. 




:field: Customers Field, many2one



.. index::
  single: field field
.. 



Object: Customer Segmentation Boolean Criteria
##############################################

.. index::
  single: Customer Segmentation Boolean Criteria object
.. 


:operator: Operator, selection



.. index::
  single: operator field
.. 




:segmentation_id: Segmentation, many2one



.. index::
  single: segmentation_id field
.. 




:value: Value, selection



.. index::
  single: value field
.. 




:field: Customers Field, many2one



.. index::
  single: field field
.. 



Object: Customer Segmentation Date Criteria
###########################################

.. index::
  single: Customer Segmentation Date Criteria object
.. 


:operator: Operator, selection



.. index::
  single: operator field
.. 




:segmentation_id: Segmentation, many2one



.. index::
  single: segmentation_id field
.. 




:to_value: To, datetime



.. index::
  single: to_value field
.. 




:from_value: From, datetime



.. index::
  single: from_value field
.. 




:field: Customers Field, many2one



.. index::
  single: field field
.. 



Object: Customer Order Segmentation Textual Criteria
####################################################

.. index::
  single: Customer Order Segmentation Textual Criteria object
.. 


:operator: Operator, selection



.. index::
  single: operator field
.. 




:segmentation_id: Segmentation, many2one



.. index::
  single: segmentation_id field
.. 




:value: Value, char



.. index::
  single: value field
.. 




:field: Customers Field, many2one



.. index::
  single: field field
.. 



Object: Customer Order Segmentation Numeric Criteria
####################################################

.. index::
  single: Customer Order Segmentation Numeric Criteria object
.. 


:operator: Operator, selection



.. index::
  single: operator field
.. 




:segmentation_id: Segmentation, many2one



.. index::
  single: segmentation_id field
.. 




:value: Value, float



.. index::
  single: value field
.. 




:field: Customers Field, many2one



.. index::
  single: field field
.. 



Object: Customer Order Segmentation Date Criteria
#################################################

.. index::
  single: Customer Order Segmentation Date Criteria object
.. 


:operator: Operator, selection



.. index::
  single: operator field
.. 




:segmentation_id: Segmentation, many2one



.. index::
  single: segmentation_id field
.. 




:to_value: To, datetime



.. index::
  single: to_value field
.. 




:from_value: From, datetime



.. index::
  single: from_value field
.. 




:field: Customers Field, many2one



.. index::
  single: field field
.. 



Object: dm.offer.history
########################

.. index::
  single: dm.offer.history object
.. 


:date: Drop Date, date



.. index::
  single: date field
.. 




:offer_id: Offer, many2one, required



.. index::
  single: offer_id field
.. 




:code: Code, char



.. index::
  single: code field
.. 




:campaign_id: Name, many2one



.. index::
  single: campaign_id field
.. 




:responsible_id: Responsible, many2one



.. index::
  single: responsible_id field
.. 



Object: dm.ddf.plugin
#####################

.. index::
  single: dm.ddf.plugin object
.. 


:name: DDF Plugin Name, char



.. index::
  single: name field
.. 




:file_fname: Filename, char



.. index::
  single: file_fname field
.. 




:file_id: File Content, binary



.. index::
  single: file_id field
.. 



Object: dm.document.template
############################

.. index::
  single: dm.document.template object
.. 


:plugin_ids: Plugin, many2many



.. index::
  single: plugin_ids field
.. 




:dynamic_fields: Fields, many2many



.. index::
  single: dynamic_fields field
.. 




:name: Template Name, char



.. index::
  single: name field
.. 



Object: dm.customer.plugin
##########################

.. index::
  single: dm.customer.plugin object
.. 


:date: Date, date



.. index::
  single: date field
.. 




:plugin_id: Plugin, many2one



.. index::
  single: plugin_id field
.. 




:customer_id: Customer Name, many2one



.. index::
  single: customer_id field
.. 




:value: Value, char



.. index::
  single: value field
.. 



Object: dm.offer.document.category
##################################

.. index::
  single: dm.offer.document.category object
.. 


:parent_id: Parent, many2one



.. index::
  single: parent_id field
.. 




:complete_name: Category, char, readonly



.. index::
  single: complete_name field
.. 




:name: Name, char, required



.. index::
  single: name field
.. 



Object: dm.offer.document
#########################

.. index::
  single: dm.offer.document object
.. 


:copywriter_id: Copywriter, many2one



.. index::
  single: copywriter_id field
.. 




:name: Name, char, required



.. index::
  single: name field
.. 




:document_template_plugin_ids: Dynamic Plugins, many2many



.. index::
  single: document_template_plugin_ids field
.. 




:lang_id: Language, many2one



.. index::
  single: lang_id field
.. 




:category_ids: Categories, many2many



.. index::
  single: category_ids field
.. 




:state: Status, selection, readonly



.. index::
  single: state field
.. 




:code: Code, char, required



.. index::
  single: code field
.. 




:has_attachment: Has Attachment, char, readonly



.. index::
  single: has_attachment field
.. 




:document_template_field_ids: Dynamic Fields, many2many



.. index::
  single: document_template_field_ids field
.. 




:document_template_id: Document Template, many2one



.. index::
  single: document_template_id field
.. 




:step_id: Offer Step, many2one



.. index::
  single: step_id field
.. 

