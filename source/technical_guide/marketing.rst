
Module Marketing Campaigns (*marketing*)
========================================
:Module: marketing
:Name: Marketing Campaigns
:Version: 5.0.1.0
:Directory: marketing
:Web: http://tinyerp.com/module_crm_marketing.html

Description
-----------

::

  Marketing management module

Dependencies
------------

 * base - installed

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

Object: campaign.campaign
#########################

.. index::
  single: campaign.campaign object
.. 


:info: Description, text



.. index::
  single: info field
.. 




:date_stop: Stop Date, date



.. index::
  single: date_stop field
.. 




:name: Name, char, required



.. index::
  single: name field
.. 




:date_start: Start Date, date



.. index::
  single: date_start field
.. 




:planned_costs: Planned Costs, float



.. index::
  single: planned_costs field
.. 




:costs: Initial Costs, float



.. index::
  single: costs field
.. 




:step_id: Campaign Steps, one2many



.. index::
  single: step_id field
.. 




:planned_revenue: Planned Revenue, float



.. index::
  single: planned_revenue field
.. 



Object: campaign.step
#####################

.. index::
  single: campaign.step object
.. 


:info: Description, text



.. index::
  single: info field
.. 




:name: Step Name, char, required



.. index::
  single: name field
.. 




:procent: Success Rate (0<x<1), float



.. index::
  single: procent field
.. 




:stop_date: Stop Date, date



.. index::
  single: stop_date field
.. 




:campaign_id: Campaign, many2one



.. index::
  single: campaign_id field
.. 




:priority: Sequence, integer, required



.. index::
  single: priority field
.. 




:costs: Step Costs, float



.. index::
  single: costs field
.. 




:active: Active, boolean



.. index::
  single: active field
.. 




:max_try: Max Attemps, integer



.. index::
  single: max_try field
.. 




:start_date: Start Date, date



.. index::
  single: start_date field
.. 



Object: campaign.partner
########################

.. index::
  single: campaign.partner object
.. 


:part_adr_id: Partner Address, many2one, required



.. index::
  single: part_adr_id field
.. 




:info: Comments, text



.. index::
  single: info field
.. 




:user_id: Salesman, many2one



.. index::
  single: user_id field
.. 




:name: Name / Reference, char, required



.. index::
  single: name field
.. 




:date_recall: Call again on, datetime



.. index::
  single: date_recall field
.. 




:notes: Prospect Notes, text



.. index::
  single: notes field
.. 




:campaign_id: Campaign, many2one



.. index::
  single: campaign_id field
.. 




:contact: Partner Contact, char



.. index::
  single: contact field
.. 




:priority: Priority, selection, required



.. index::
  single: priority field
.. 




:history_ids: History, one2many



.. index::
  single: history_ids field
.. 




:step: Step, many2one, required



.. index::
  single: step field
.. 




:state: State, selection, readonly



.. index::
  single: state field
.. 




:active: Active, boolean



.. index::
  single: active field
.. 




:partner_id: Partner, many2one, required



.. index::
  single: partner_id field
.. 



Object: campaign.partner.history
################################

.. index::
  single: campaign.partner.history object
.. 


:info: Comments, text



.. index::
  single: info field
.. 




:name: History, char, required



.. index::
  single: name field
.. 




:camp_partner_id: Prospect, many2one, readonly



.. index::
  single: camp_partner_id field
.. 




:step_attempt: Attempt, integer, readonly



.. index::
  single: step_attempt field
.. 




:date: Date, datetime, readonly



.. index::
  single: date field
.. 




:step_id: Step, many2one, readonly



.. index::
  single: step_id field
.. 

