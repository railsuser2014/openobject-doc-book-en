
.. _part2-crm-opport:

Optimizing your Sales Cycle through Opportunities
=================================================

While a lead represents the first contact with a prospect yet to be qualified, a sales opportunity represents a potential contract. Each opportunity has to be followed up by a salesperson (or sales team) spending time to qualify the opportunity, and this either by making a quotation or cancelling the opportunity.

Leads are generally handled by the dozen, with the automation of certain responses or emails.
Opportunities, on the contrary, are usually tracked one by one by the salespeople, because an opportunity involves a negotiation process with the customer to be.

Just like for leads, OpenERP provides specific features to handle sales opportunities efficiently. All opportunities can be found in the menu :menuselection:`Sales --> Sales --> Opportunities`.

With opportunities, you can manage and keep track of your sales pipeline by creating specific customer- or prospect-related sales documents to follow up potential sales. Information such as expected revenue, opportunity stage, expected closing date, communication history, next action date, next action, and much more can be stored.

Opportunities can be connected to the email gateway: new emails may create opportunities, each of them automatically gets the history of the conversation with the customer. You and your sales team(s) will be able to plan meetings and phone calls from opportunities, convert them into quotations, manage related documents, track all customer-related activities, and much more.

.. tip:: Attachments

      By default, you can keep attachments in OpenERP to make sure all linked documents are directly accessible. At the top side
      of the screen, under ``Attachments``, click the *Add* button to start linking documents to your opportunity. You can add attachments in the same way for leads,
      for instance.
      If you also want those documents to be indexed (not for pictures), you should install the Knowledge Application.

Converting Leads into Customers or Opportunities
------------------------------------------------

If the salesperson thinks that the lead has been well qualified and that there is a real opportunity, following the contact he had with the prospect, he can easily convert the lead into a partner / opportunity using the button :guilabel:`Convert to Opportunity`.

Clicking the `Convert to Opportunity` button offers several possibilities, allowing you also to avoid duplicate partners:

* You can decide to just create the opportunity and keep the contact data from the lead without creating a customer,
 
* You can convert to an opportunity, and create a new customer if it does not exist yet, or merge the contact with an existing customer,

* You first create a customer, and later you convert the lead to an opportunity.

.. tip:: Convert to Opportunity

      When you click the `Convert to Opportunity` button and the email address of the new contact is filled out, OpenERP will check whether
      this email address corresponds to an email address of an existing customer. If so, OpenERP will directly propose to merge the new
      contact with the customer found.  

When you click the :guilabel:`Convert to Opportunity` button and the customer already exists, OpenERP opens a window allowing you to select:

* whether you want to create a new opportunity,

* whether you want to add this lead to an existing opportunity (merge). 

OpenERP shows the title of the opportunity (taken from the lead description) and the partner.

.. figure:: images/crm_lead_convert.png
   :scale: 75
   :align: center

   *Converting a Lead into a Sales Opportunity*.

.. figure:: images/crm_opport_data.png
   :scale: 75
   :align: center

   *Convert to opportunity (merge with existing)*


The Kanban View: Everything at a Glance
----------------------------

In order to improve the end user productivity, we developed a drag & drop kanban view for some documents. This new view allows users to easily reorganize their records while allowing them to maintain a global overview.

In kanban view of Opportunities where you can now pick between different stages in the kanban view: New, Qualification, Proposition, Negotiation, Won or Lost. This will help you understand and visualize better the status of your opportunitites and decide what to tackle first. 

As opposed to 6.1., when you access Opportunities in 7.0. there are no extra buttons or unnecesary tabs. 

.. figure:: images/crm_opport_kanban.png
   :scale: 60
   :align: center

   *Kanban view of Opportunity*

.. _ch-team:

Adapting OpenERP to your Sales Organization
-------------------------------------------

.. index::
   single: sales

Your sales organization may be composed of several groups which for instance address different customer segments or geographies, sell different products and services and often manage different sales cycles.  As a manager you will want to track the performance not only for each individual but also for each group.

OpenERP allows you to do that by defining `Sales Teams`. A sales team is a group of sales people who are performing a similar position. Implementing sales teams is a powerful tool. It allows you to: 

* Assign leads or opportunities according to their nature to a sales team first. Then according to the company’s policy, the opportunities can be assigned to a given individual. For example opportunities can be assigned to a `Western Region sales team` or `Eastern Region sales team` in the first place according to their location. Each sales person may pick unassigned opportunities in his sales team according to his availability,

* You can group your sales teams according to a tree structure (hierarchy). This allows you to have a view of your sales activity at different granular levels (local, regional, national for instance),

* Some sales teams may manage their opportunities through different sales cycles. For instance a car dealership which addresses both the residential and corporate customers, will have different sales cycles.  

* For each sales team, you can assign a responsible user and an email address that will be used when creating or replying to emails from OpenERP. This will be proposed by default in OpenERP when you create an event for this customer.

.. note:: Sales Teams 

        To define your Sales Teams, go to :menuselection:`Sales --> Configuration --> Sales Teams`.

Let us take the example of a bank to explain how you can define your sales teams. A bank has several departments, such as Insurance, Accounts, Assets, Credit Management. Each department may be divided into several subdepartments. For Insurance, this could be Group Insurance and Home Insurance. The hierarchical structure of your Sales Teams could then be as follows:

* Insurance Sales Team
     * Group Insurance
     * Home Insurance

* Accounts Sales Team

* Assets Sales Team

* Credit Management Sales Team

Defining the Key Steps of your Sales Cycle
------------------------------------------

Each company will have similar, yet customized stages to qualify opportunities.

To see & define stages for Opportunity qualification, go to :menuselection:`Sales --> Configuration -->  Leads & Opportunities --> Stages`. 

The key steps of your Sales Cycle are what OpenERP calls ``Stages``. You can use the stages to improve your sales capacity, because they allow you to find out the reasons why deals succeed or fail.

Stages will allow salesmen to easily track where a specific opportunity is positioned in the sales cycle. One of the frequent difficulties in using stages is that different sales people may assess differently in which stage their sales opportunity should be. You can avoid this by clearly stating what you expect as a result for each stage. This way, your sales teams will use the same stages throughout the qualification process, allowing the sales manager to get accurate and consistent information. We also recommend to limit the number of stages in your sales cycle to make them easy to follow up.

As you progress in your sales cycle, and move from one stage to another, you can expect to have more precise information about a given opportunity. For example, when setting an opportunity as 'Qualified', you may decide that the salesman has to enter the "Expected Revenue" and the "Expected Closing Date." You can also have the probability changed automatically when changing stages, by selecting the "Change Probability Automatically" checkbox. If checked, OpenERP will set the probability of the opportunity to the probability defined in the stage. If you set a probability of 0% (Lost) or 100% (Won), OpenERP will assign the corresponding stage when the opportunity is marked as Lost or Won.

As an example, to track your opportunities, you can assign the following stages to the sales team. For each stage, you assume you will define criteria that have to be met prior to moving to the next stage. 

1. New - Segment your opportunities into territories.

2. Qualified – Attract the prospect’s interest, determine whether the prospect has a need.

   What is the expected result?
    * The need to buy the product/service has been confirmed,
    * Confirm that there is a budget.

3. Proposition – Discuss some solutions to determine the customer’s preferences, recommend specific solutions to answer the customer's needs.

   What is the expected result?
    * Demo and/or Proposal given,
    * Decision maker confirmed his interest to purchase,
    * Preliminary pricing confirmed/agreed upon.

4. Negotiation – Submit the final proposal to the customer and begin the negotiation process.

   What is the expected result?
    * Negotiation concluded,
    * Contract terms/conditions agreed upon,
    * Contract submitted for signature.

5. Won/Lost – Register the final step of the opportunity.

   What is the expected result?
    * Contract signed / not signed,
    * Next steps.

If you decide to add a stage, you will have to configure it with some basic information. In case you are really keen on states, we kept the state concept through the stage in order to associate your stage to a state (new, open, pending, close). You can do this by accessing the stage configuration form.

.. figure:: images/crm_opport_stages.png
   :scale: 60
   :align: center

   *Example of Opportunity Stages*

The stages are now conveniently placed on the top right hand of each of opportunity. In this way, you can easily change the status of the opportunity in just one click.

.. figure:: images/crm_stages_on_opport.png
   :scale: 60
   :align: center

   *Stages on Opportunity*.

OpenERP also has other sales configuration options; you can define your `Campaigns`, allowing you to keep track of the event your leads and opportunities refer to. Examples of campaigns are Google Adwords, an event you are hosting, a newsletter.  
With `Sales Tags` you identify your prospect's needs (e.g. Needs Training, Needs OpenERP Online), while `Channels` help you to keep visibility on how the lead or opportunity entered the system (email, website, referred by an existing customer). 

Planning your Next Actions
--------------------------

When a lead has been converted into an opportunity, the latter can be assigned to any salesperson. You might designate an opportunity manager in the company who is responsible for assigning the new opportunities to different salespeople according to the job they do, their location or availability.

Of course, OpenERP allows you to automate such steps in your sales cycle. With `Automated Rules` you can tell the system for instance to automatically assign opportunities to a sales person or to change the status of an opportunity according to specific criteria.

.. note:: Automated Actions

       To access the CRM rules, use the :menuselection:`Settings --> Technical --> Automated Actions --> Automated Actions` menu.

Let's give an example of what you can use Automated Actions for. Suppose you want to have OpenERP assign opportunities for customers in the IT Services category directly to Thomas, your IT salesperson. Thomas should be assigned automatically when a lead is converted to an opportunity by clicking the `Convert to Opportunity` button in the *Leads* screen. This can be set through the ``Object`` field in the `Automated Actions` form; just select `Lead To Opportunity Partner`.

The screenshots below illustrate how you can tell OpenERP to do this automatically for you. 

*Step 1*

.. figure:: images/crm_autom_act1.png
   :scale: 100
   :align: center

   *Conditions Tab of Automated Actions*.

*Step 2*

.. figure:: images/crm_autom_act2.png
   :scale: 75
   :align: center

   *Actions Tab of Automated Actions*.

Planning your next actions also refers to filling fields or performing actions manually, without interference of automated rules. It is important that you fill all the opportunity fields accurately. To ensure good follow-up and prioritise your opportunities, make sure to register the ``Next Action Date`` and the ``Next Action`` in the Opportunity.

You can use the filters to group by ``Priority`` and then click the ``Next Action Date`` column to sort by next action date to easily follow up your opportunities and know exactly what you have to do.


Planning your Meetings & Calls Effectively
------------------------------------------

Planning your meetings & calls does not only allow you to structure your work, but also to improve your sales skills by learning from your call & meeting history. For both Meetings & Calls, you can enter a complete report of what you discuss!

As explained in chapter :ref:`crm-flow`, you can schedule a meeting directly from an opportunity. When you create a meeting from an opportunity, related fields will be prefilled from the opportunity.
For the ease of reading, Thomas will schedule a new meeting from an opportunity here and set Luc, the Sales Manager, as the person responsible for the meeting. He wants to send Luc a reminder 1 day before the meeting starts.

.. note:: Schedule a Meeting from an Opportunity

   To plan the meeting, Thomas clicks the `Meeting` button in the **Opportunity** and clicks the `Week` button in the Calendar view. He uses the drag and drop function to schedule the meeting for Luc. He plans the meeting next Wednesday from 2 pm to 3 pm. He sets Luc as the person responsible and sets a reminder to be send 1 day before the start of the meeting. He also changes the ``Next Action Date`` in the opportunity to the meeting date. 

You can also schedule a meeting directly from a **Customer** form by clicks the `Meetings` button. If you stay in the Month view of the Calendar, you just have to click the day you want the meeting to be planned, let's say Thursday in two weeks. A meeting form will be displayed, with the name of the customer and the date prefilled.

In the **Meeting** window, enter the meeting data such as meeting subject, Attendees, Tags. In the weekly and daily views, you can also press the left mouse button in the calendar and slide the mouse along to create an event of several hours. OpenERP then opens an entry screen for a new meeting.
You can add reminders (or ``Alarms``) to your meetings and send invitations, either to persons from your own company, partner contacts or external people (just specify the email address directly in the invitation). 

.. tip:: Alarms or Meeting Reminders

     Add your own alarms through :menuselection:`Sales --> Configuration --> Calendar --> Alarms`. You might want to be warned one week in advance of the meeting, so all you have to do is create your own alarm. The screenshot below will show you how to do this.
     
.. figure:: images/alarm.png
   :scale: 60
   :align: center

   *Defining your Own Alarms*.

Add events through :menuselection:`Sales --> Configuration --> Calendar --> Events`
     
.. figure:: images/crm_meeting_form.png
   :scale: 75
   :align: center

   *Entering a new Event*.


You can filter the My Events by selecting them from the list at the right of the screen.

.. figure:: images/crm_calendar_month.png
   :scale: 50
   :align: center

   *Monthly Meeting Calendar*.

Weekly meeting Calendar seems like following screenshot.

.. figure:: images/crm_calendar_week.png
   :scale: 50
   :align: center

   *Weekly Meeting Calendar*.

.. index:: calendars

You can change the Calendar view for meetings and return to the list, form view by using the buttons at the top right. OpenERP's usual search tools and filters enable you to filter the events displayed in the calendar or, for example, to display the calendar for only some employees at a time.

.. tip:: Related Responsible

      When you hover your mouse cursor over a meeting in Calendar view, the related responsible will be displayed.

Of course, you can access this OpenERP calendar from your smartphone. For more information about this feature, please refer to chapter :ref:`ch-sync1`.

OpenERP also allows you to manage incoming (`inbound`) and outgoing (`outbound`) calls. Even from the **Phone Calls** list view, you can directly edit a call (change the status, convert it to an opportunity or schedule a meeting). For every call, you can enter notes about the outcome. While on the phone with your prospect or customer, you can directly schedule a meeting, schedule another call or convert your call to an opportunity. There is no need for you to scroll to several menus to do what you have to: plan an action as a result of your call.

Call management may be used for other needs than planning, such as:

* Entering customer calls so that you keep a record of the communication attached to a partner or a
  sales opportunity,

* Calling out to large lists of prospects,

* Scheduling recurring calls or next actions.

.. note:: Schedule a Phone Call directly

       Go to :menuselection:`Sales --> Phone Calls --> Scheduled Calls` to register incoming calls or `Outbound` to register outgoing calls.

Of course, OpenERP also allows you to schedule a phone call directly from an **Opportunity** form through the related ``Schedule/Log Call`` button.

.. note:: Phone Calls in Meeting Calendar

       To have one calendar with both your meetings and your phone calls, you may choose to enter phone calls as a meeting, with a specific meeting Tags, `Phone Call`.

Scheduling Closing Dates
------------------------

To keep track of the coming sales pipeline, you should enter the expected closing date for each opportunity. By doing this, from the **Opportunities** screen you can easily filter your pipeline by ``Exp. Closing`` (button in Group by). This is a clear way to forecast the expected revenues. You can also use this filter to check whether the expected closing date has been set.

Simply by adding an expected closing date, the sales team can manage the sales process more efficiently and effectively.

.. figure::  images/crm_opport_closing.png
   :align: center
   :scale: 60

   *Closing Dates*

.. Copyright © Open Object Press. All rights reserved.

.. You may take electronic copy of this publication and distribute it if you don't
.. change the content. You can also print a copy to be read by yourself only.

.. We have contracts with different publishers in different countries to sell and
.. distribute paper or electronic based versions of this book (translated or not)
.. in bookstores. This helps to distribute and promote the OpenERP product. It
.. also helps us to create incentives to pay contributors and authors using author
.. rights of these sales.

.. Due to this, grants to translate, modify or sell this book are strictly
.. forbidden, unless Tiny SPRL (representing Open Object Press) gives you a
.. written authorisation for this.

.. Many of the designations used by manufacturers and suppliers to distinguish their
.. products are claimed as trademarks. Where those designations appear in this book,
.. and Open Object Press was aware of a trademark claim, the designations have been
.. printed in initial capitals.

.. While every precaution has been taken in the preparation of this book, the publisher
.. and the authors assume no responsibility for errors or omissions, or for damages
.. resulting from the use of the information contained herein.

.. Published by Open Object Press, Grand Rosière, Belgium

