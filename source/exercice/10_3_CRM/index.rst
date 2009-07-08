********************************
Customer Relationship Management
********************************

Configure the CRM
=================

As to develop your prototype for NotSoTiny, you will have to install the
CRM modules. You need to manage:

* The leads
* The business opportunities
* The phone calls
* The shared calendars
* The quotations

.. note:: Exercice 1 - Install required CRM modules

    Install the modules needed in the above requirements.

.. note:: Exercice 2 - Create the menus

    Once all modules are installed, you should configure the system and
    create the different menus according to the following sections:

    * Leads Management
    * Business Opportunities
    * Phone Calls
    * Shared Calendars


.. note:: Exercice 3 - Quotation generation

    Install the module that allows you to convert one or a list of business
    opportunities to a quotation.



TODO: configure categories ???


A CRM flow
==========

As to prepare the demonstration of your prototype, we will simulate a real
business case, from the first meeting with the cutomer to the quotation
for a particular project.

Each year, the NotSoTiny company participate to the "House & Design" fair
in Paris. During this fair, the company will meet about 200 prospects in
three days.

.. note:: Exercice 4 - The fair

    Encode the fair as a campaign in the CRM.

At the end of each days, the different salesman present at the fairs encode
all business cards they got from prospects in the system. They put a maximum
of information relative to the prospect on the lead form. Then, a few days later,
salesman from NotSoTiny will contact each lead one by one to qualify it and
check if we have an opportunity with this customer.

.. note:: Exercice 5 - Encode the following leads in the system

    ... to describe ...

If the lead seems interresting, the salesman can convert it to an opportunity
and create a partner form. Suppose Luc is processing some of the most important
leads of the fair. He will notice the lead "...".

As the lead is very interresting, he will convert it to a business opportunity
and a partner. On the business opportunity, he can provide more information like
the expected revenue (5.000 k€).


.. note:: Exercice 6 - Convert lead to partner and business opportunity

    Thomas, the salesman, connect in the system and check available leads. He
    selects the lead "..." and convert it to an opportunity as it seems very
    interresting and he would like to do followups on this request.

As to fill in the partner form, Thomas will call the lead on the phone.


.. note:: Exercice 7 - Fills in the complete data on partner form

    Fill in the address to the related partner.

While discussing on the phone with the prospect, Thomas planify a meeting for
Luc. He also asks the customer to send his complete requirements by email
before the meeting so that he can provide information to Luc to prepare his
customer meeting efficiently.

.. note:: Exercice 8 - Schedule a meeting

    From the partner form, schedule a meeting for Luc. This meeting is organised
    in the customer's office and relates to the business opportunity "..."

A few days later, the customer calls to the office. Eric is replying on the
phone. The customer want to provide more information about the shelves he
is looking for. He wanted red shelves and he would like Thomas to bring a
catalog of shelves with him when going to the customer office.

.. note:: Exercice 9 - Encode a phone call

    Eric encode the summary of the phone call. He relates this phonecall
    to the opportunity "...".

On wednesday 12th of febreuary, Luc prepares his meeting before going to
the customer. He opens the partner form and checks all activities that have
been made with this partner during the past 15 days.


.. note:: Exercice 10 - Check partner form

    Check all events on the partner form.


Luc visits the customer and proposed him a quotation. As they are no more requests
than the provided quotation on the business opportunity, he will also need to
close the lead.


.. note:: Exercice 11 - Create a quotation from the business opportunity

    Sell the following products:

    * A Kitchen Design Project
    * A shelve 100cm

    Don't forget to close the opportunity as we will track on the quotation
    now.



Managing with the CRM
=====================

Luc, the salesmanager, wants to check the quality of his sales team.


.. note:: Exercice 12 - Check the average delay to close an opportunity

    Find a way to know what's the average time (in hours) to respond to 
    a customer request (close a business opportunity).

Luc noticed that the average time to close a business opportunity is
7 days. This delay seems too long for him. As ha want to improve the quality
of his sales team, he'd like to receive a warning by email each time a business
opportunity is not closed within the next 5 days after his creation.


.. note:: Exercice 13 - Reminder by email

    Send a reminder to the responsible if the business opportunity is not
    closed after 5 days. For leads, he accepted only 3 days before closing
    them. Put Luc in CC, when such reminder are sent.


The company have different policies to manage unqualified leads and real
business opportunities. Leads are put in a pool of unassigned leads when
they are created. Then, the different users will take leads and assign
them to themselves periodically.

For business opportunities, it's different. All business opportunities
should be assigned to Luc. Then, luc decide if he wants to assign the
case to someone else or keep it to him.


.. note:: Exercice 14 - Assignation and pool of available cases

    Find a way to get all unassigned leads. Find a way to automatically
    assign business opportunities to luc when they are created.


