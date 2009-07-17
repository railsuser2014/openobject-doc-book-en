
.. i18n: Leads
.. i18n: =====

Leads
=====

.. i18n: A lead represents a potential customer or a possible future business or sales opportunity. They
.. i18n: aren't usually qualified yet and they aren't yet assigned to an individual person for following up.
.. i18n: When a lead needs to be followed up, it's converted to a partner and/or a sales opportunity.

A lead represents a potential customer or a possible future business or sales opportunity. They
aren't usually qualified yet and they aren't yet assigned to an individual person for following up.
When a lead needs to be followed up, it's converted to a partner and/or a sales opportunity.

.. i18n: For example, the following events could result in the creation of one or several leads:

For example, the following events could result in the creation of one or several leads:

.. i18n: * A business card from a prospective customer met briefly at an exhibition: you must contact him
.. i18n:   again to qualify the lead and to know if there is any possibility of a key sales opportunity,
.. i18n: 
.. i18n: * A database of potential customers in a given sector and region. The potential customers must be
.. i18n:   contacted again individually or using a mass mailing to determine which contacts need to be followed
.. i18n:   up,
.. i18n: 
.. i18n: * A contact that you've been given by a friend. You must then qualify it before starting to assign a
.. i18n:   salesperson to the contact,
.. i18n: 
.. i18n: * A form completed on your website directly integrated into Open ERP. Before converting the form
.. i18n:   into a sale proposition or opportunity, you should read and handle the person's request.

* A business card from a prospective customer met briefly at an exhibition: you must contact him
  again to qualify the lead and to know if there is any possibility of a key sales opportunity,

* A database of potential customers in a given sector and region. The potential customers must be
  contacted again individually or using a mass mailing to determine which contacts need to be followed
  up,

* A contact that you've been given by a friend. You must then qualify it before starting to assign a
  salesperson to the contact,

* A form completed on your website directly integrated into Open ERP. Before converting the form
  into a sale proposition or opportunity, you should read and handle the person's request.

.. i18n:     .. note:: Separation of sales services
.. i18n: 
.. i18n:         In companies of a certain type, you often distinguish between the sales department and the
.. i18n:         presales department.
.. i18n:         The role of the presales department is to acquire and qualify new leads,
.. i18n:         and the role of the sales department is to crystallize the sales opportunities or work with
.. i18n:         existing customers.

    .. note:: Separation of sales services

        In companies of a certain type, you often distinguish between the sales department and the
        presales department.
        The role of the presales department is to acquire and qualify new leads,
        and the role of the sales department is to crystallize the sales opportunities or work with
        existing customers.

.. i18n: System users in the pre-sales department will usually work on leads. Once these leads are
.. i18n: converted into customers or sales opportunities the sales department pays individual attention to
.. i18n: each opportunity.

System users in the pre-sales department will usually work on leads. Once these leads are
converted into customers or sales opportunities the sales department pays individual attention to
each opportunity.

.. i18n: Entering prospects into the system
.. i18n: ----------------------------------

Entering prospects into the system
----------------------------------

.. i18n: New prospects are usually entered as a lead in the system. This means that you don't create a
.. i18n: partner form or sales opportunity until you have qualified whether the lead is interesting or not.
.. i18n: If the new contact is indeed interesting you then enter the data on into a partner form and,
.. i18n: eventually, a sales opportunity.

New prospects are usually entered as a lead in the system. This means that you don't create a
partner form or sales opportunity until you have qualified whether the lead is interesting or not.
If the new contact is indeed interesting you then enter the data on into a partner form and,
eventually, a sales opportunity.

.. i18n: To enter a lead manually use the menu :menuselection:`CRM & SRM --> Sales --> Leads --> New Lead`. A
.. i18n: form opens to let you enter data about this new contact.

To enter a lead manually use the menu :menuselection:`CRM & SRM --> Sales --> Leads --> New Lead`. A
form opens to let you enter data about this new contact.

.. i18n: .. figure:: images/crm_lead_new.png
.. i18n:    :scale: 50
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Creating a new lead*

.. figure:: images/crm_lead_new.png
   :scale: 50
   :align: center

   *Creating a new lead*

.. i18n: Leads have a status that depends on the qualification work that's been carried out:

Leads have a status that depends on the qualification work that's been carried out:

.. i18n: * ``Draft`` : the lead data has been entered, any work has not yet been done and a salesperson has not
.. i18n:   yet been assigned to the request,
.. i18n: 
.. i18n: * ``Open`` : the lead is being handled,
.. i18n: 
.. i18n: * ``Closed`` : the lead has been converted into a partner and/or a sales opportunity,
.. i18n: 
.. i18n: * ``Waiting`` : the lead is waiting for a response from the customer,
.. i18n: 
.. i18n: * ``Cancelled`` : the lead has been cancelled because the salesperson has decided that it's not worth
.. i18n:   following up.

* ``Draft`` : the lead data has been entered, any work has not yet been done and a salesperson has not
  yet been assigned to the request,

* ``Open`` : the lead is being handled,

* ``Closed`` : the lead has been converted into a partner and/or a sales opportunity,

* ``Waiting`` : the lead is waiting for a response from the customer,

* ``Cancelled`` : the lead has been cancelled because the salesperson has decided that it's not worth
  following up.

.. i18n: When a new lead has been created it's automatically put into the open state.

When a new lead has been created it's automatically put into the open state.

.. i18n: You can also import a huge list of leads. That's useful if you've bought a database of
.. i18n: potential prospects and you want to load them all into the system to handle them all at the same time.

You can also import a huge list of leads. That's useful if you've bought a database of
potential prospects and you want to load them all into the system to handle them all at the same time.

.. i18n: To do that you should start with a list of leads in CSV format. If your prospects are provided in
.. i18n: another format it's easy to convert them to the CSV format using Microsoft Excel or OpenOffice Calc.
.. i18n: Open the leads list using the menu :menuselection:`CRM & SRM --> Sales -> Leads -> My Leads`. At
.. i18n: the bottom of the list click on the :guilabel:`Import` link. Open ERP opens a form for importing the
.. i18n: data.

To do that you should start with a list of leads in CSV format. If your prospects are provided in
another format it's easy to convert them to the CSV format using Microsoft Excel or OpenOffice Calc.
Open the leads list using the menu :menuselection:`CRM & SRM --> Sales -> Leads -> My Leads`. At
the bottom of the list click on the :guilabel:`Import` link. Open ERP opens a form for importing the
data.

.. i18n: .. figure:: images/crm_lead_import.png
.. i18n:    :scale: 50
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Importing leads into the system*

.. figure:: images/crm_lead_import.png
   :scale: 50
   :align: center

   *Importing leads into the system*

.. i18n: You then define which columns are present in your CSV file in the correct order. Then select your file
.. i18n: and click on :guilabel:`Import`. Check in the chapter about system administration, :ref:`ch-config`, for more
.. i18n: information on import and export.

You then define which columns are present in your CSV file in the correct order. Then select your file
and click on :guilabel:`Import`. Check in the chapter about system administration, :ref:`ch-config`, for more
information on import and export.

.. i18n: .. tip:: Various Imports
.. i18n: 
.. i18n:     Importing and Exporting data in Open ERP is a generic function available to all resources.
.. i18n:     So you can import and export such lists as partners, sales opportunities, accounting entries,
.. i18n:     products and pricelists.

.. tip:: Various Imports

    Importing and Exporting data in Open ERP is a generic function available to all resources.
    So you can import and export such lists as partners, sales opportunities, accounting entries,
    products and pricelists.

.. i18n: There are other methods of importing leads automatically or semi-automatically:

There are other methods of importing leads automatically or semi-automatically:

.. i18n: * Using the Outlook or Thunderbird plugin to insert new leads directly from an email client after a
.. i18n:   salesperson sees promising emails,
.. i18n: 
.. i18n: * Using the email gateway for each incoming email from a certain address (such as
.. i18n:   info@mycompany.com) creating a lead automatically from the contents of the email,
.. i18n: 
.. i18n: * Using Open ERP's XML-RPC web-services to connect to a form on your website.

* Using the Outlook or Thunderbird plugin to insert new leads directly from an email client after a
  salesperson sees promising emails,

* Using the email gateway for each incoming email from a certain address (such as
  info@mycompany.com) creating a lead automatically from the contents of the email,

* Using Open ERP's XML-RPC web-services to connect to a form on your website.

.. i18n: These different methods are described in the next CRM chapter, :ref:`ch-crm`.

These different methods are described in the next CRM chapter, :ref:`ch-crm`.

.. i18n: Organizing leads
.. i18n: ----------------

Organizing leads
----------------

.. i18n: To help the users organize and handle leads efficiently, Open ERP provides several menus in the CRM
.. i18n: system that can be used depending on the needs of each:

To help the users organize and handle leads efficiently, Open ERP provides several menus in the CRM
system that can be used depending on the needs of each:

.. i18n: * :menuselection:`Leads --> New Lead` opens an entry form directly onto a new lead. This menu can
.. i18n:   usefully be put into your shortcuts,
.. i18n: 
.. i18n: * :menuselection:`Leads --> My Leads` gives a list of all the leads (both open and not) which you're
.. i18n:   linked to,
.. i18n: 
.. i18n: * :menuselection:`Leads --> My Leads --> My Current Leads` gives a list of all your leads that you
.. i18n:   still need to handle (your open, draft and waiting leads),
.. i18n: 
.. i18n: * :menuselection:`Leads --> My Leads --> My Current Leads --> My Pending Leads` gives a list of all your
.. i18n:   leads that that are still waiting for a customer response. This enables you to check periodically on
.. i18n:   your work to do,
.. i18n: 
.. i18n: * :menuselection:`Leads --> All Leads` is a list of all the leads assigned to different salespeople.
.. i18n:   This menu as those beneath it are used by managers to check on each person's work.

* :menuselection:`Leads --> New Lead` opens an entry form directly onto a new lead. This menu can
  usefully be put into your shortcuts,

* :menuselection:`Leads --> My Leads` gives a list of all the leads (both open and not) which you're
  linked to,

* :menuselection:`Leads --> My Leads --> My Current Leads` gives a list of all your leads that you
  still need to handle (your open, draft and waiting leads),

* :menuselection:`Leads --> My Leads --> My Current Leads --> My Pending Leads` gives a list of all your
  leads that that are still waiting for a customer response. This enables you to check periodically on
  your work to do,

* :menuselection:`Leads --> All Leads` is a list of all the leads assigned to different salespeople.
  This menu as those beneath it are used by managers to check on each person's work.

.. i18n: .. figure:: images/crm_leads_list.png
.. i18n:    :scale: 50
.. i18n:    :align: center
.. i18n: 
.. i18n:    *List of leads to be handled*

.. figure:: images/crm_leads_list.png
   :scale: 50
   :align: center

   *List of leads to be handled*

.. i18n: Leads are prioritized. Salespeople should ideally start at the top of the list. They then open a
.. i18n: form to describe the lead. At this stage they contact the suspected customer by email or phone and enter the
.. i18n: result of the contact on the lead form.

Leads are prioritized. Salespeople should ideally start at the top of the list. They then open a
form to describe the lead. At this stage they contact the suspected customer by email or phone and enter the
result of the contact on the lead form.

.. i18n: They can then change the status of the lead to a state that depends on the response from the
.. i18n: suspect:

They can then change the status of the lead to a state that depends on the response from the
suspect:

.. i18n: * ``Cancelled`` : not to be followed as a lead,
.. i18n: 
.. i18n: * ``Waiting`` : waiting for a response from the suspect.

* ``Cancelled`` : not to be followed as a lead,

* ``Waiting`` : waiting for a response from the suspect.

.. i18n: Converting leads into customers or opportunities
.. i18n: ------------------------------------------------

Converting leads into customers or opportunities
------------------------------------------------

.. i18n: If a lead is interesting you convert it into a partner in the system. To do that, push the button
.. i18n: :guilabel:`Convert to Partner`. Open ERP opens a partner form with the information from the lead entered
.. i18n: into it. At this stage you can add more information such as the exact partner address and the
.. i18n: contact details.

If a lead is interesting you convert it into a partner in the system. To do that, push the button
:guilabel:`Convert to Partner`. Open ERP opens a partner form with the information from the lead entered
into it. At this stage you can add more information such as the exact partner address and the
contact details.

.. i18n: The created partner is automatically attached to the lead, which enables you to keep complete
.. i18n: traceability from the lead. To do that look at the second tab in the lead :guilabel:`History`.

The created partner is automatically attached to the lead, which enables you to keep complete
traceability from the lead. To do that look at the second tab in the lead :guilabel:`History`.

.. i18n: If the salesperson thinks that there is a real opportunity with the lead, following the contact, he
.. i18n: can convert it into a sales opportunity using the button :guilabel:`Convert to Opportunity`. Open ERP then
.. i18n: opens a window asking the title of the opportunity, the estimated revenue and the percentage success
.. i18n: of converting to a sale.

If the salesperson thinks that there is a real opportunity with the lead, following the contact, he
can convert it into a sales opportunity using the button :guilabel:`Convert to Opportunity`. Open ERP then
opens a window asking the title of the opportunity, the estimated revenue and the percentage success
of converting to a sale.

.. i18n: .. figure:: images/crm_lead_convert.png
.. i18n:    :scale: 50
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Converting a lead into a sales opportunity*

.. figure:: images/crm_lead_convert.png
   :scale: 50
   :align: center

   *Converting a lead into a sales opportunity*

.. i18n: Some companies have more advanced processes for the qualification of a lead. They pass through
.. i18n: several steps, such as first call, renewing contact, waiting for a verbal agreement. You can then
.. i18n: use the field :guilabel:`Step` that is found up to the right of the lead definition. To move it
.. i18n: automatically through the next step, you can use the button that looks like a right arrow.

Some companies have more advanced processes for the qualification of a lead. They pass through
several steps, such as first call, renewing contact, waiting for a verbal agreement. You can then
use the field :guilabel:`Step` that is found up to the right of the lead definition. To move it
automatically through the next step, you can use the button that looks like a right arrow.

.. i18n: .. Copyright © Open Object Press. All rights reserved.

.. Copyright © Open Object Press. All rights reserved.

.. i18n: .. You may take electronic copy of this publication and distribute it if you don't
.. i18n: .. change the content. You can also print a copy to be read by yourself only.

.. You may take electronic copy of this publication and distribute it if you don't
.. change the content. You can also print a copy to be read by yourself only.

.. i18n: .. We have contracts with different publishers in different countries to sell and
.. i18n: .. distribute paper or electronic based versions of this book (translated or not)
.. i18n: .. in bookstores. This helps to distribute and promote the Open ERP product. It
.. i18n: .. also helps us to create incentives to pay contributors and authors using author
.. i18n: .. rights of these sales.

.. We have contracts with different publishers in different countries to sell and
.. distribute paper or electronic based versions of this book (translated or not)
.. in bookstores. This helps to distribute and promote the Open ERP product. It
.. also helps us to create incentives to pay contributors and authors using author
.. rights of these sales.

.. i18n: .. Due to this, grants to translate, modify or sell this book are strictly
.. i18n: .. forbidden, unless Tiny SPRL (representing Open Object Press) gives you a
.. i18n: .. written authorisation for this.

.. Due to this, grants to translate, modify or sell this book are strictly
.. forbidden, unless Tiny SPRL (representing Open Object Press) gives you a
.. written authorisation for this.

.. i18n: .. Many of the designations used by manufacturers and suppliers to distinguish their
.. i18n: .. products are claimed as trademarks. Where those designations appear in this book,
.. i18n: .. and Open Object Press was aware of a trademark claim, the designations have been
.. i18n: .. printed in initial capitals.

.. Many of the designations used by manufacturers and suppliers to distinguish their
.. products are claimed as trademarks. Where those designations appear in this book,
.. and Open Object Press was aware of a trademark claim, the designations have been
.. printed in initial capitals.

.. i18n: .. While every precaution has been taken in the preparation of this book, the publisher
.. i18n: .. and the authors assume no responsibility for errors or omissions, or for damages
.. i18n: .. resulting from the use of the information contained herein.

.. While every precaution has been taken in the preparation of this book, the publisher
.. and the authors assume no responsibility for errors or omissions, or for damages
.. resulting from the use of the information contained herein.

.. i18n: .. Published by Open Object Press, Grand Rosière, Belgium

.. Published by Open Object Press, Grand Rosière, Belgium
