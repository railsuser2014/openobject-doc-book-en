Marketing Campaigns
===================

.. index::
   single: Actions
   single: Activity
   single: Workflow
   single: Object
   single: Criteria
   single: Conditions
   single: Workitem
   single: Startflag
   single: Boolean
   single: Dot Notation
   single: Attributes
   single: Marketing
   single: Campaigns


OpenERP offers a set of modules allowing you to easily create and track your Marketing Campaigns.
With the Marketing application you define your direct marketing campaigns, which can be displayed in List or Diagram view (process). 

To use the email functionality, you have to configure your email account.
Go to :menuselection:`Sales --> Configuration --> Emails --> Email Servers`. Configure your server (i.e. Google). The object defines where you want the emails to enter (e.g. as a Lead). (See :ref:`ch-crm-fetchmail`)

Click the `Fetch email` button to get the emails directly. OpenERP also automatically creates a Scheduled Action to fetch the mails every 5 minutes. The email is automatically created as a lead (according to the object used).

Automate your Leads with Marketing Campaigns
--------------------------------------------
*Example with the email marketing campaign we follow at OpenERP for our SAAS offer.*

Whenever someone subscribes to OpenERP online he/she fills a form which becomes the lead of OpenERP SaaS offer Campaign. Our SaaS salesperson triggers the marketing campaign by sending an introductory email of services we offer and thanking for subscribing for the one month free trial. Based on the response, we plot whether the lead is interested in OpenERP SAAS offer, Training or buying the OpenERP book. Significantly these are our subsets and based on their cues we send them emails catering those respective needs. If they respond back, they are converted into an opportunity and thereby on subscription of our services they become our partner.
In lack of response, we send them another reminder regarding the offer after a week's duration. If they still do not respond, our salesperson gives a voluntary call inquiring their needs. Hence, like a flowchart we can trigger a respective activity for every possible cue. The chances of leads going unattended becomes very low, and for every lead we have a predefined method of treating it, and we could measure it with our goals. Based on the goals, we can also evaluate the effectiveness of our campaign and analyze if there is a room for improvement.
 
*What are the questions you should focus on?*

Designing every marketing campaign is mostly a long term process, and the success of any campaign depends on the research and the effectiveness in the selection of customers in the campaign. There are certain questions that every marketeer always asks while designing a campaign:

* What would be our marketing campaign?

* Who would be the target audience?

* How would we measure the effectiveness of our campaign?
 
The OpenERP campaign works on the basic principle of lead automation. A lead is created based on a specific response by a customer towards a stimuli. E.g: Filling the subscription form on your website.
The first step is defining the campaign i.e. the sequence of steps to be performed. On defining the campaign we trigger a set of activities in the marketing campaign module of OpenERP.
Based on the lead automation we define the sequence of steps we ought to follow, the modes of creating and processing these activities and the cost involved with these campaigns. Thus after each activity and based on its respective stimuli we can trigger the next event of the respective campaign.
 
*Why is the Segment important?*

The two most important points for any successful campaign are the adoption of a concrete methodology of execution, and choosing the right segment: a target loop of customers to whom our campaign would be directed. Inappropriate focus on a segment would result in the campaign being misfired and our efforts would reach deaf ears.

Through the `Segment` tab in the **Campaign** module we can define our segment for the Campaign activity, since it is possible that with every step downwards, our segment gets narrowed in terms of number. You can also synchronize the entire campaign steps based on our defined segments.
 
*How is Marketing Campaign related to CRM?*

The Marketing Campaign module is closely synchronized with the Sales Management Business Application (CRM). Initially,let us consider the segment we cater in the campaign as Leads. Goals are set for each campaign which would be considered as a desired state. Once a lead accomplishes our objective criteria of goals, we change their status by converting them into Opportunity (i.e. we should give focused attention to those leads). Once the lead satisfies our final objective, we would consider them as a partner/customer and close that lead.

*Email Templates*

For each email template, you can have OpenERP generate a Wizard Action / Button that will be related to the object. So if you choose to do marketing campaigns for leads, the action will be added to the right side panel of the Lead form.

Defining a Marketing Campaign in OpenERP
----------------------------------------

Please notice that it requires some technical knowledge to configure Marketing Campaigns.
To be able to see, create, edit campaign, users need to be in the Marketing / User group.

0. Introduction

A campaign defines a workflow of activities that items/objects entering the campaign will go through. Items are selected by segments. Segments are automatically processed every few hours and inject new items into the campaign, according to a given set of criteria.
It is possible to watch the campaign as it is running, by following the campaign "workitems". A workitem represents a given object/item passing through a given campaign activity. Workitems are left behind when the item proceeds to the next activities. This allows an easy analysis and reporting on the running campaign.
Each activity may execute an action upon activation depending on a dynamic condition. When the condition is not met, the workitem is cancelled/deleted; if the condition is met, the action is executed, the workitem is marked as ``Done``, and propagated to the next activities.

1. Campaigns (:menuselection:`Marketing --> Campaigns --> Campaigns`)

Campaign
  Each campaign is made of activities and transitions, and must be defined on any specific object the system knows about
  (e.g. Leads, Opportunities, Employees, Partners).

Mode
  A campaign can be in one of 4 modes:

 * ``Test Directly``: process the whole campaign in one go, ignoring any delay put on transitions, and does not actually execute the actions, so the result is simply the set of corresponding campaign workitems (see below). Any time a segment adds new items in the campaign they will be processed in the same manner.

 * ``Test in Realtime``: process the campaign but does not actually execute the actions, so the result is simply the set of corresponding campaign workitems (see below). Any time a segment adds new items in the campaign, they will be processed in the same manner.

 * ``With Manual confirmation``: No action will be executed automatically, a human intervention is needed to let workitems proceed into the flow. It is like a step-by-step manual process using the `Campaign Followup` menu. You can ignore the time delays and force any step of the campaign, implementing the campaign at your pace i.e. (you have a test email and want to see if the steps and templates work to your liking). You will see that the actions set are defined as ``To Do`` and ``Done`` and the page has to be refreshed to see the next activity defined by the campaign note: the campaign sends real messages to the actual targets, be warned.

 * ``Normal``: the campaign is processed normally, all actions are executed automatically at the scheduled date. Pay attention that in this status, the campaign sends real messages to the actual targets.

Regardless of the current mode of the campaign, any workitem can be manually executed or cancelled at any time (even if it is scheduled in the future) through *Campaign Followup*.

Resource
  Specifies where the campaign will get the information from, i.e. the OpenERP object linked (e.g. Leads, Opportunities,
  Employees, Partners).


Activities
  Activities are steps in the campaign. Each activity is optionally linked to previous and next activities through transitions.

Each activity has:

   * one optional condition that stops the campaign,

   * one action to be executed when the activity is activated and the condition is True (could be a 'do nothing' action),

   * one optional signal (ignore it),

   * a start flag (see below).

*Start Activity*

Activities that have the Start flag set will receive a new workitem corresponding to each new resource/object entering the campaign. It is possible to have more than one Start Activity, but not less than one.

*Activity Conditions*

[a Boolean expression, made of clauses combined using boolean operators: AND, OR, NOT]
Each condition is the criterion that decides whether the activity is going to be activated for a given workitem, or just cancelled.
It is an arbitrary expression composed of simple tests on attributes of the object, possibly combined using *or*, *and* & *not* operators.

See section 6.1 at bottom for reference on Comparators.

The individual tests can use the "object" name to refer to the object/resource it originates from (e.g the lead), using a "dot notation" to refer to its attributes. Some examples on a CRM Lead resource:

   * object.name == 'GTK Survey Lead'  would select only leads whose title is exactly "GTK Survey Lead",

   * object.state == 'pending' would select Pending leads only,

   * object.country_id.code == 'be' would select leads whose country field is set to Belgium,

   * object.country_id.name == 'Belgium' would select leads whose country field is set to Belgium.

Tests can also use a 'workitem' name to refer to the actual item, denoting the position of the object in the campaign. This can be useful to access some specific attributes, such as the segment that selected this item. Some examples:

   * workitem.segment_id.name == 'GTK Survey EU Zone1 - Industry Consulting/Technology'  would select leads that entered this campaign through the "GTK Survey EU Zone1 - Industry Consulting/Technology" segment,

   * 'EU Zone1' in workitem.segment_id.name would select only leads that entered the campaign through a segment that has "EU Zone1" in its name.

.. tip:: In the GTK client you can use :menuselection:`Help --> Enable Debug mode tooltips` to see the attribute name of every field in a form. These are the same that you can use during import/export with CSV files.

You can also use the special formula re.search(PATTERN_TO_SEARCH, ATTRIBUTE_TO_SEARCH) where PATTERN_TO_SEARCH is a character string delimited with quotes, and ATTRIBUTE_TO_SEARCH uses the dot notation above to refer to a field of the object.
For example, for CRM leads:

   * re.search('Plan to sell: True', object.description) would be true if the Notes on a Lead contain this text: "Plan to sell: True". Be careful that all spaces, etc., do matter, so you may use the special pattern characters as detailed at the bottom to account for small variations,

   * re.search('Plan to.*True', object.description) would be true if the Notes on a Lead contain this text: "Plan to" followed later on by "True".

You can combine individual tests using boolean operators and parentheses.
Some examples on a CRM Lead resource:

   * object.state != 'pending' and ( re.search('Plan to sell:.*True',object.description)  and not re.search('Plan to use:.*True',object.description))  would be true if the lead is NOT in Pending state and it contains "Plan to sell"  but not "Plan to use".

Guidelines for Creating a Campaign
----------------------------------

 * It is a good idea to have an initial activity that will change some fields on the objects entering the campaign to mark them as such, and avoid mixing them in other processes (e.g. set a specific state and Sales Team on a CRM lead being processed by a campaign). You can also define a time delay so that the campaign seems more human (note if the answer comes in a matter of seconds or minutes, it is computer generated).

 * Put a stop condition on each subsequent activity in the campaign, to get items out of the campaign as soon as the goal is achieved (e.g. every activity has a partial condition on the state of the item, if CRM Leads stops being Pending, the campaign ends for that case).

2. Email Templates (:menuselection:`Marketing --> Configuration --> Email Template --> Templates`)

Email templates are composed of the following information:

 * The Email headers: to, from, cc, bcc, subject

 * The raw HTML body, with the low-level markup and formatting

 * The plain-text body

Headers and bodies can contain place-holders for dynamic contents that will be replaced in the final email with the actual content.


3. Campaign Segments

Segments are processed automatically according to a predefined schedule set in the menu :menuselection:`Administration --> Configuration --> Scheduled Actions`. It could be set to process every 4 hours or every minute, for example.
This is the only entry point in a campaign at the moment.

*Segment filters*

Segments select resources via filters, exactly the same kind of filter that can be used in advanced search views on any list in OpenERP. You can actually create them easily by saving your advanced search criteria as new filters.
Filters mainly consist of a domain expressing the criteria of selection on a model (the resource).
See the section 10.3 at the bottom for more information on the syntax for these filters.

For Leads, the following filter would select draft Leads from any European country with "Plan for use: True" or "Plan for sell: False" specified in the body:
|    [  ('type','=','lead'), 
|       ('state', '=', 'draft'),
|       ('country_id.name', 'in', ['Belgium',
|       'Netherlands',
|       'Luxembourg',
|       'United Kingdom',
|       'France',
|       'Germany',
|       'Finland',
|       'Denmark',
|       'Norway',
|       'Austria',
|       'Switzerland',
|       'Italy',
|       'Spain',
|       'Portugal',
|       'Ireland',
|       ]),
|        '|', 
|            ('description', 'ilike', 'Plan for use: True'), 
|            ('description', 'ilike', 'Plan for sell: False')
|      ]

6. Miscellaneous References, examples:

6.1 Reference of Comparison Operators:

 * ==: Equal

 * !=: Not Equal

 * <: Bigger than

 * >: Smaller Than

 * <=: Bigger than or equal to

 * >=: Smaller than or equal to

 * in: to check that a given text is included somewhere in another text. e.g "a" in "dabc" is True

6.2 Reference of Pattern/Wildcard characters

 * `.` (dot) represents any character (but just one)

 * `*` means that the previous pattern can be repeated 0 or more times

 * `+` means that the previous pattern can be repeated 1 or more times 

 * `?` means that the previous pattern is optional (0 or 1 times)

 * `.*` would represent any character, repeated in 0 or more occurrences 

 * `.+` would represent at least 1 character (but any)

 * `5?` would represent an optional 5 character

6.3 Reference of filter domains

Generic format is:  [ (criterion_1), (criterion_2) ] to filter for resources matching both criteria.
It is possible to combine criteria differently with the following operators:

   * '&' is the boolean AND operator and will make a new criterion by combining the next 2 criteria (always 2). This is also the implicit operator when no operator is specified.

     * for example:  [ (criterion_1), '&', (criterion_2), (criterion_3) ] means criterion_1 AND (criterion_2 AND criterion_3)

   * '|' is the boolean OR operator and will make a new criterion by combining the next 2 criteria (always 2)

     * for example:  [ (criterion_1), '|', (criterion_2), (criterion_3) ] means criterion_1 AND (criterion_2 OR criterion_3)

   * '!' is the boolean NOT operator and will make a new criterion by reversing the value of the next criterion (always only 1)

     * for example:  [ (criterion_1), '!', (criterion_2), (criterion_3) ] means criterion_1 AND (NOT criterion_2) AND criterion_3

Criterion format is:  ( 'field_path_operand', 'operator', value )

Where:

   * field_path_operand specifies the name of an attribute or a path starting with an attribute to reach the value we want to compare

   * operator is one of the possible operator: 

     * '=' , '!=' : equal and different

     * '<', '>', '>=', '<=' :  greater or lower than or equal

     * 'in', 'not in' : present or absent in a list of value. Values must be specified as [ value1, value2 ], e.g. [ 'Belgium', 'Croatia' ]

     * 'ilike' : search for string value in the operand

   * value is the text or number or list value to compare with field_path_operand using comparator

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


