
.. module:: marketing
    :synopsis: Marketing Campaigns
    :noindex:
.. 

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

Marketing Campaigns (*marketing*)
=================================
:Module: marketing
:Name: Marketing Campaigns
:Version: 5.0.1.0
:Directory: marketing
:Web: http://tinyerp.com/module_crm_marketing.html
:Is certified: no

Description
-----------

::

  Marketing management module

Dependencies
------------

 * :mod:`base`

Reports
-------

None


Menus
-------

 * Marketing Operations
 * Marketing Operations/Campaigns
 * Marketing Operations/Configuration
 * Marketing Operations/Configuration/Campaign Definition

Views
-----

 * campaign.campaign.view (tree)
 * campaign.campaign.view (form)
 * campaign.step.tree (tree)
 * campaign.step.form (form)
 * campaign.partner.tree (tree)
 * campaign.partner.form (form)
 * campaign.partner.history.form (form)
 * campaign.partner.history.tree (tree)


Objects
-------

Object: campaign.campaign (campaign.campaign)
#############################################



:info: Description, text





:date_stop: Stop Date, date





:name: Name, char, required





:date_start: Start Date, date





:planned_costs: Planned Costs, float





:costs: Initial Costs, float





:step_id: Campaign Steps, one2many





:planned_revenue: Planned Revenue, float




Object: campaign.step (campaign.step)
#####################################



:info: Description, text





:name: Step Name, char, required





:procent: Success Rate (0<x<1), float





:stop_date: Stop Date, date





:campaign_id: Campaign, many2one





:priority: Sequence, integer, required





:costs: Step Costs, float





:active: Active, boolean





:max_try: Max Attemps, integer





:start_date: Start Date, date




Object: campaign.partner (campaign.partner)
###########################################



:part_adr_id: Partner Address, many2one, required





:info: Comments, text





:user_id: Salesman, many2one





:name: Name / Reference, char, required





:date_recall: Call again on, datetime





:notes: Prospect Notes, text





:campaign_id: Campaign, many2one





:contact: Partner Contact, char





:priority: Priority, selection, required





:history_ids: History, one2many





:step: Step, many2one, required





:state: State, selection, readonly





:active: Active, boolean





:partner_id: Partner, many2one, required




Object: campaign.partner.history (campaign.partner.history)
###########################################################



:info: Comments, text





:name: History, char, required





:camp_partner_id: Prospect, many2one, readonly





:step_attempt: Attempt, integer, readonly





:date: Date, datetime, readonly





:step_id: Step, many2one, readonly


