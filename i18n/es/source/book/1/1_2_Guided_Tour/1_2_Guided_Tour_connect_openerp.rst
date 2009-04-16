
.. i18n: To connect to Open ERP
.. i18n: =======================

To connect to Open ERP
=======================

.. i18n: Since this is the first time you've connected to it you'll have to
.. i18n: go through the Setup wizard in steps:

Since this is the first time you've connected to it you'll have to
go through the Setup wizard in steps:

.. i18n: 	#.  :guilabel:`Select a profile` : select ``Minimal Profile`` and click :guilabel:`Next`.
.. i18n: 
.. i18n: 	#.  At the :guilabel:`Define Main Company` step you should select your own :guilabel:`Company Name` and 
.. i18n: 	    :guilabel:`Currency`, and address details on the first tab :guilabel:`General Information`; 
.. i18n: 	    and add more details on the second tab :guilabel:`Report Information` including a logo,
.. i18n: 	    if you have one, that appears on reports. Click :guilabel:`Next`.
.. i18n: 
.. i18n: 	#.  At the :guilabel:`Summary` page you can go back to change details if you need.
.. i18n: 	    Click the :guilabel:`Install` button.
.. i18n: 
.. i18n: 	#.  Finally, at the :guilabel:`Installation done` page, click :guilabel:`Start Configuration`.
.. i18n: 	
.. i18n: Configuration consists of a set of wizards that help you through options for the installed modules.
.. i18n: Hardly anything is installed so this is a very simple process at the moment.
.. i18n:    
.. i18n:     #.  At the first screen click :guilabel:`Continue` to go into the first wizard. 
.. i18n:         Choose :guilabel:`View Mode` : :guilabel:`Simplified Interface`
.. i18n:         and then click :guilabel:`Set` to save it.
.. i18n: 
.. i18n:     #.  Click :guilabel:`Skip Step` to step over the next wizard, which would enable you to add other users.
.. i18n: 
.. i18n:     #.  You've now reached the end of the configuration so click :guilabel:`Continue` to start using the
.. i18n:         system as the Administrator.

	#.  :guilabel:`Select a profile` : select ``Minimal Profile`` and click :guilabel:`Next`.

	#.  At the :guilabel:`Define Main Company` step you should select your own :guilabel:`Company Name` and 
	    :guilabel:`Currency`, and address details on the first tab :guilabel:`General Information`; 
	    and add more details on the second tab :guilabel:`Report Information` including a logo,
	    if you have one, that appears on reports. Click :guilabel:`Next`.

	#.  At the :guilabel:`Summary` page you can go back to change details if you need.
	    Click the :guilabel:`Install` button.

	#.  Finally, at the :guilabel:`Installation done` page, click :guilabel:`Start Configuration`.
	
Configuration consists of a set of wizards that help you through options for the installed modules.
Hardly anything is installed so this is a very simple process at the moment.
   
    #.  At the first screen click :guilabel:`Continue` to go into the first wizard. 
        Choose :guilabel:`View Mode` : :guilabel:`Simplified Interface`
        and then click :guilabel:`Set` to save it.

    #.  Click :guilabel:`Skip Step` to step over the next wizard, which would enable you to add other users.

    #.  You've now reached the end of the configuration so click :guilabel:`Continue` to start using the
        system as the Administrator.

.. i18n: .. index::
.. i18n:    single:  administrator

.. index::
   single:  administrator

.. i18n: Once you're displaying the main menu you're able to see the following screen items, 
.. i18n: as shown in screenshot :ref:`fig-oech2-main`:

Once you're displaying the main menu you're able to see the following screen items, 
as shown in screenshot :ref:`fig-oech2-main`:

.. i18n: * the :guilabel:`Preferences` toolbar to the top right, showing the user name, links to the :guilabel:`Home` page,
.. i18n:   :guilabel:`Preferences`, :guilabel:`About` and :guilabel:`Logout`,
.. i18n: 
.. i18n: * just below you'll find information about the :guilabel:`Request` system,
.. i18n: 
.. i18n: * links to the :guilabel:`MAIN MENU` and the :guilabel:`SHORTCUTS`,
.. i18n: 
.. i18n: * information about copyright and the database you're logged into at the bottom of the page,
.. i18n: 
.. i18n: * the main contents of the window with by the menu toolbar to the left: links generally line up on
.. i18n:   the right but there are none to show at the moment.

* the :guilabel:`Preferences` toolbar to the top right, showing the user name, links to the :guilabel:`Home` page,
  :guilabel:`Preferences`, :guilabel:`About` and :guilabel:`Logout`,

* just below you'll find information about the :guilabel:`Request` system,

* links to the :guilabel:`MAIN MENU` and the :guilabel:`SHORTCUTS`,

* information about copyright and the database you're logged into at the bottom of the page,

* the main contents of the window with by the menu toolbar to the left: links generally line up on
  the right but there are none to show at the moment.

.. i18n: .. _fig-oech2-main:
.. i18n: 
.. i18n: .. figure:: images/main_window_openerp_ch02.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *The Main Menu of the openerp_ch02 database*

.. _fig-oech2-main:

.. figure:: images/main_window_openerp_ch02.png
   :scale: 75
   :align: center

   *The Main Menu of the openerp_ch02 database*

.. i18n: Two menus are available on the left:

Two menus are available on the left:

.. i18n: * :menuselection:`Partners`,
.. i18n: 
.. i18n: * :menuselection:`Administration`.

* :menuselection:`Partners`,

* :menuselection:`Administration`.

.. i18n: .. index::
.. i18n:    single: Preferences

.. index::
   single: Preferences

.. i18n: Preferences toolbar
.. i18n: ---------------------

Preferences toolbar
---------------------

.. i18n: When you're connected to Open ERP the Preferences toolbar indicates which user you're connected as.
.. i18n: So it should currently be showing :guilabel:`Welcome Administrator` (unless you logged in as another
.. i18n: user and it's reflecting the name of that user instead).

When you're connected to Open ERP the Preferences toolbar indicates which user you're connected as.
So it should currently be showing :guilabel:`Welcome Administrator` (unless you logged in as another
user and it's reflecting the name of that user instead).

.. i18n: You'll find a link to the :guilabel:`Home` page to its right. This takes you to either the
.. i18n: dashboard or the available menus, depending on the user configuration. In the case of the \
.. i18n: ``openerp_ch02``\ database so far the Home page is the Main Menu. But in general each user of the
.. i18n: system is presented with a dashboard that's designed to show performance indicators and urgent
.. i18n: documents that are most useful to someone of the user's position in the company. You'll see how to
.. i18n: assign dashboards to different users in a later chapter, :ref:`ch-config`.

You'll find a link to the :guilabel:`Home` page to its right. This takes you to either the
dashboard or the available menus, depending on the user configuration. In the case of the \
``openerp_ch02``\ database so far the Home page is the Main Menu. But in general each user of the
system is presented with a dashboard that's designed to show performance indicators and urgent
documents that are most useful to someone of the user's position in the company. You'll see how to
assign dashboards to different users in a later chapter, :ref:`ch-config`.

.. i18n: .. index::
.. i18n:    single: timezone

.. index::
   single: timezone

.. i18n: .. tip::  Multi-nationals and time zones
.. i18n: 
.. i18n: 	If you have users in different countries, they can configure their own timezone. Timestamp displays
.. i18n: 	are then adjusted by reference to the user's own localization setting.
.. i18n: 
.. i18n: 	So if you have a team in India and a team in England, the times will automatically be converted. If
.. i18n: 	an Indian employee sets her working hours from 9 to 6 that will be converted and saved in the
.. i18n: 	server's timezone. When the English users want to set up a meeting with an Indian user, the Indian
.. i18n: 	user's available time will be converted to English time.

.. tip::  Multi-nationals and time zones

	If you have users in different countries, they can configure their own timezone. Timestamp displays
	are then adjusted by reference to the user's own localization setting.

	So if you have a team in India and a team in England, the times will automatically be converted. If
	an Indian employee sets her working hours from 9 to 6 that will be converted and saved in the
	server's timezone. When the English users want to set up a meeting with an Indian user, the Indian
	user's available time will be converted to English time.

.. i18n: The next element in the Toolbar is a link to :guilabel:`Preferences`. By clicking that link you
.. i18n: reach a page where the current user can set their password, a timezone, a working language, and
.. i18n: a signature:

The next element in the Toolbar is a link to :guilabel:`Preferences`. By clicking that link you
reach a page where the current user can set their password, a timezone, a working language, and
a signature:

.. i18n: * The :guilabel:`Password` field gives the user the opportunity to change their own password.
.. i18n:   You should take steps (perhaps written policies) to prevent users making these too trivial. 
.. i18n: 
.. i18n: * The :guilabel:`Language` field enables the user's working language to be changed. But first the
.. i18n:   system must be loaded with other languages for the user to be able to choose an alternative, which
.. i18n:   is described in the next subsection of this chapter. This is a mandatory field, although might
.. i18n:   initially be set as blank.
.. i18n: 
.. i18n: * The :guilabel:`Timezone` setting indicates the user's location to Open ERP. This can be different
.. i18n:   from that of the server. All of the dates in the system are converted to the user's timezone
.. i18n:   automatically.
.. i18n: 
.. i18n: * The :guilabel:`Signature` field gives the user a place for the signature attached to messages sent
.. i18n:   from within Open ERP. 

* The :guilabel:`Password` field gives the user the opportunity to change their own password.
  You should take steps (perhaps written policies) to prevent users making these too trivial. 

* The :guilabel:`Language` field enables the user's working language to be changed. But first the
  system must be loaded with other languages for the user to be able to choose an alternative, which
  is described in the next subsection of this chapter. This is a mandatory field, although might
  initially be set as blank.

* The :guilabel:`Timezone` setting indicates the user's location to Open ERP. This can be different
  from that of the server. All of the dates in the system are converted to the user's timezone
  automatically.

* The :guilabel:`Signature` field gives the user a place for the signature attached to messages sent
  from within Open ERP. 

.. i18n: The :guilabel:`About` link gives information about the development of the Open ERP software and 
.. i18n: various links to other information.

The :guilabel:`About` link gives information about the development of the Open ERP software and 
various links to other information.

.. i18n: The :guilabel:`Logout` link enables you to logout and return to the original login page. You can
.. i18n: then login to another database, or to the same database as another user. This page also gives you
.. i18n: access to the super-administrator functions for managing databases on this server.

The :guilabel:`Logout` link enables you to logout and return to the original login page. You can
then login to another database, or to the same database as another user. This page also gives you
access to the super-administrator functions for managing databases on this server.

.. i18n: The :guilabel:`Requests` link sits just below this toolbar. It is only visible if you're logged into
.. i18n: a database. If your database is new it will say :guilabel:`No request`. You can click on that link
.. i18n: to look at requests that have been sent to you at any time.

The :guilabel:`Requests` link sits just below this toolbar. It is only visible if you're logged into
a database. If your database is new it will say :guilabel:`No request`. You can click on that link
to look at requests that have been sent to you at any time.

.. i18n: .. index::
.. i18n:    single: installation; language

.. index::
   single: installation; language

.. i18n: Installing a new language
.. i18n: ^^^^^^^^^^^^^^^^^^^^^^^^^^^

Installing a new language
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. i18n: Each user of the system can work in his or her own language. More than twenty languages are
.. i18n: currently available besides English. Users select their working language using the Preferences link.
.. i18n: You can also assign a language to a partner (customer or supplier), in which case all the documents
.. i18n: sent to that partner will be automatically translated into that language.

Each user of the system can work in his or her own language. More than twenty languages are
currently available besides English. Users select their working language using the Preferences link.
You can also assign a language to a partner (customer or supplier), in which case all the documents
sent to that partner will be automatically translated into that language.

.. i18n: .. attention:: More information about languages
.. i18n: 
.. i18n: 	The base version of Open ERP is translated into the following languages: English, German, Chinese,
.. i18n: 	Spanish, Italian, Hungarian, Dutch, Portuguese, Romanian, Swedish and Czech.
.. i18n: 
.. i18n: 	But other languages are also available: Arabic, Afghan,
.. i18n: 	Austrian, Bulgarian, Indonesian, Finnish, Thai, Turkish and Vietnamese..

.. attention:: More information about languages

	The base version of Open ERP is translated into the following languages: English, German, Chinese,
	Spanish, Italian, Hungarian, Dutch, Portuguese, Romanian, Swedish and Czech.

	But other languages are also available: Arabic, Afghan,
	Austrian, Bulgarian, Indonesian, Finnish, Thai, Turkish and Vietnamese..

.. i18n: As administrator you can install a new main working language into the system.

As administrator you can install a new main working language into the system.

.. i18n: 	#. Select :menuselection:`Administration` in the Menu Toolbar and click
.. i18n: 	   :menuselection:`Translations --> Load an Official Translation` in the main menu window,
.. i18n: 
.. i18n: 	#. Select the language to install, \ ``French``\  for example, and click on :guilabel:`Start
.. i18n: 	   Installation`,
.. i18n: 
.. i18n: 	#. When the message :guilabel:`Installation done` appears in the :guilabel:`Language file loaded` window,
.. i18n: 	   click :guilabel:`OK` to return to  the menu. (Your system will actually need the French locale loaded
.. i18n: 	   to be able to do this, so you may not be successful here.)

	#. Select :menuselection:`Administration` in the Menu Toolbar and click
	   :menuselection:`Translations --> Load an Official Translation` in the main menu window,

	#. Select the language to install, \ ``French``\  for example, and click on :guilabel:`Start
	   Installation`,

	#. When the message :guilabel:`Installation done` appears in the :guilabel:`Language file loaded` window,
	   click :guilabel:`OK` to return to  the menu. (Your system will actually need the French locale loaded
	   to be able to do this, so you may not be successful here.)

.. i18n: To see the effects of this installation change the preferences of your user to change the working
.. i18n: language (you may first need to ensure that you have explicitly selected English as your language,
.. i18n: rather than keep the default, before you're given the French option). 
.. i18n: The main menu is immediately translated in the selected language. If you're using the GTK
.. i18n: client you'll first have to close the menu then open a new main menu to start seeing things in the
.. i18n: new language.

To see the effects of this installation change the preferences of your user to change the working
language (you may first need to ensure that you have explicitly selected English as your language,
rather than keep the default, before you're given the French option). 
The main menu is immediately translated in the selected language. If you're using the GTK
client you'll first have to close the menu then open a new main menu to start seeing things in the
new language.

.. i18n: .. note:: Navigating the menu
.. i18n: 
.. i18n:    From this point in the book navigation from the main menu is written as a series of menu entries
.. i18n:    connected by the :menuselection:`-->` character. Instead of seeing “ Select Administration in
.. i18n:    the Menu toolbar then click Translations > Load an Official Translation ” you'll just get “ use menu
.. i18n:    :menuselection:`Administration --> Translations --> Load an Official Translation` ”.

.. note:: Navigating the menu

   From this point in the book navigation from the main menu is written as a series of menu entries
   connected by the :menuselection:`-->` character. Instead of seeing “ Select Administration in
   the Menu toolbar then click Translations > Load an Official Translation ” you'll just get “ use menu
   :menuselection:`Administration --> Translations --> Load an Official Translation` ”.

.. i18n: .. index:: requests

.. index:: requests

.. i18n: Requests as a mechanism for internal communication
.. i18n: ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Requests as a mechanism for internal communication
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. i18n: Requests are a powerful communication mechanism between users of the system. They're also used by
.. i18n: Open ERP itself to send system messages to users.

Requests are a powerful communication mechanism between users of the system. They're also used by
Open ERP itself to send system messages to users.

.. i18n: They have distinct advantages over traditional emails:

They have distinct advantages over traditional emails:

.. i18n: * requests are linked to other Open ERP documents,
.. i18n: 
.. i18n: * an event's history is attached to the request,
.. i18n: 
.. i18n: * you can monitor events effectively from the messages they've sent.

* requests are linked to other Open ERP documents,

* an event's history is attached to the request,

* you can monitor events effectively from the messages they've sent.

.. i18n: Open ERP uses this mechanism to inform users about certain system events. For example if there's a
.. i18n: problem concerning the procurement of a product a request is sent by Open ERP to the production
.. i18n: manager.

Open ERP uses this mechanism to inform users about certain system events. For example if there's a
problem concerning the procurement of a product a request is sent by Open ERP to the production
manager.

.. i18n: Send a request to get an understanding of its functionality:

Send a request to get an understanding of its functionality:

.. i18n: 	#. Click on the :guilabel:`Requests` link that should currently be showing :guilabel:`No Requests`.
.. i18n: 	   This opens a window that lists all of your waiting requests.
.. i18n: 
.. i18n: 	#. Click :guilabel:`New` to create and send a new request.
.. i18n: 
.. i18n: 	#. Complete the subject of the request, such as \ ``How are things?``\  then give a description of the
.. i18n: 	   enquiry in the field.
.. i18n: 
.. i18n: 	#. Click the :guilabel:`Search` button to the right of the :guilabel:`To` field and select
.. i18n: 	   :guilabel:`Administrator` in the window that opens (that's the user that you're already connected
.. i18n: 	   as).
.. i18n: 
.. i18n: 	#. You can then link this request to other system documents using the :guilabel:`References` field,
.. i18n: 	   which could, for example, be a partner or a quotation or a disputed invoice.
.. i18n: 
.. i18n: 	#. Click :guilabel:`Send` to send the request to the intended recipient – that's yourself in this
.. i18n: 	   case. Then click :guilabel:`MAIN MENU` to return to the original screen.

	#. Click on the :guilabel:`Requests` link that should currently be showing :guilabel:`No Requests`.
	   This opens a window that lists all of your waiting requests.

	#. Click :guilabel:`New` to create and send a new request.

	#. Complete the subject of the request, such as \ ``How are things?``\  then give a description of the
	   enquiry in the field.

	#. Click the :guilabel:`Search` button to the right of the :guilabel:`To` field and select
	   :guilabel:`Administrator` in the window that opens (that's the user that you're already connected
	   as).

	#. You can then link this request to other system documents using the :guilabel:`References` field,
	   which could, for example, be a partner or a quotation or a disputed invoice.

	#. Click :guilabel:`Send` to send the request to the intended recipient – that's yourself in this
	   case. Then click :guilabel:`MAIN MENU` to return to the original screen.

.. i18n: .. figure:: images/request_tab.png
.. i18n:    :align: center
.. i18n:    :scale: 80
.. i18n: 
.. i18n:    *Creating a new request*

.. figure:: images/request_tab.png
   :align: center
   :scale: 80

   *Creating a new request*

.. i18n: To check your requests:

To check your requests:

.. i18n: 	#. Click on the link to the right of the :guilabel:`Requests` label to open a list of your
.. i18n: 	   requests. (It's possible that you'll still see the statement :guilabel:`No Requests` because this
.. i18n: 	   information is updated periodically ather than instantly.) The list of requests then opens and you
.. i18n: 	   can see the requests you've been sent there.
.. i18n: 
.. i18n: 	#. Click the :guilabel:`Edit` icon, represented by a pencil, at the right hand end of the request
.. i18n: 	   line. That opens the request in edit mode.
.. i18n: 
.. i18n: 	#. You can then click the :guilabel:`Reply` button and make your response in the
.. i18n: 	   :guilabel:`Request` field that appears in place of the original message.
.. i18n: 
.. i18n: 	#. Click :guilabel:`Send` to save your response and send it to the original sender.

	#. Click on the link to the right of the :guilabel:`Requests` label to open a list of your
	   requests. (It's possible that you'll still see the statement :guilabel:`No Requests` because this
	   information is updated periodically ather than instantly.) The list of requests then opens and you
	   can see the requests you've been sent there.

	#. Click the :guilabel:`Edit` icon, represented by a pencil, at the right hand end of the request
	   line. That opens the request in edit mode.

	#. You can then click the :guilabel:`Reply` button and make your response in the
	   :guilabel:`Request` field that appears in place of the original message.

	#. Click :guilabel:`Send` to save your response and send it to the original sender.

.. i18n: .. note:: Requests vs. email
.. i18n: 
.. i18n: 	The advantage of an Open ERP request compared with a set of emails about one thread of discussion
.. i18n: 	is that a request contains all of the conversation in one place. You can easily monitor a whole
.. i18n: 	discussion with the appropriate documents attached, and quickly review a list of incomplete
.. i18n: 	discussions with the history within each request.

.. note:: Requests vs. email

	The advantage of an Open ERP request compared with a set of emails about one thread of discussion
	is that a request contains all of the conversation in one place. You can easily monitor a whole
	discussion with the appropriate documents attached, and quickly review a list of incomplete
	discussions with the history within each request.

.. i18n: Look at the request and its history, then close it.

Look at the request and its history, then close it.

.. i18n: 	#. Click on the :guilabel:`History` tab in the :guilabel:`Request` form to see the
.. i18n: 	   original request and all of the responses. By clicking on each line you could get more information
.. i18n: 	   on each element.
.. i18n: 
.. i18n: 	#. Return to the first tab, :guilabel:`Request` and click :guilabel:`End of Request` to set it to \
.. i18n: 	   ``closed``\.   This then appears greyed out.

	#. Click on the :guilabel:`History` tab in the :guilabel:`Request` form to see the
	   original request and all of the responses. By clicking on each line you could get more information
	   on each element.

	#. Return to the first tab, :guilabel:`Request` and click :guilabel:`End of Request` to set it to \
	   ``closed``\.   This then appears greyed out.

.. i18n: The request is no longer active. It's not visible to searches and won't appear in your list of
.. i18n: waiting requests.

The request is no longer active. It's not visible to searches and won't appear in your list of
waiting requests.

.. i18n: .. tip:: Trigger dates
.. i18n: 
.. i18n: 	You can send a request with a future date. This request won't appear in the recipient's waiting
.. i18n: 	list until the indicated date. This mechanism is very useful for setting up alerts before an
.. i18n: 	important event.

.. tip:: Trigger dates

	You can send a request with a future date. This request won't appear in the recipient's waiting
	list until the indicated date. This mechanism is very useful for setting up alerts before an
	important event.

.. i18n: .. index::
.. i18n:    single: user; configuration

.. index::
   single: user; configuration

.. i18n: Configuring Users
.. i18n: -------------------

Configuring Users
-------------------

.. i18n: The database you created contains minimal functionality but can be extended to include all of the
.. i18n: potential functionality available to Open ERP. About the only functions actually available in this
.. i18n: minimal database are Partners and Currencies – and these only because the definition of your main
.. i18n: company required this. And because you chose to include demonstration data, both Partners and
.. i18n: Currencies were installed with some samples.

The database you created contains minimal functionality but can be extended to include all of the
potential functionality available to Open ERP. About the only functions actually available in this
minimal database are Partners and Currencies – and these only because the definition of your main
company required this. And because you chose to include demonstration data, both Partners and
Currencies were installed with some samples.

.. i18n: .. index::
.. i18n:    single: administrator

.. index::
   single: administrator

.. i18n: Because you logged in as Administrator, you have all the access you need to configure users. Click
.. i18n: :menuselection:`Administration --> Users --> Users` to display the list of users defined in the
.. i18n: system. A second user, \ ``Demo User``\  , is also present in the system as part of the
.. i18n: demonstration data. Click the \ ``Demo User``\   name to open a non-editable form on that user.

Because you logged in as Administrator, you have all the access you need to configure users. Click
:menuselection:`Administration --> Users --> Users` to display the list of users defined in the
system. A second user, \ ``Demo User``\  , is also present in the system as part of the
demonstration data. Click the \ ``Demo User``\   name to open a non-editable form on that user.

.. i18n: Click the :guilabel:`Security`  tab to see that the demo user is a member of only the ``Employee`` group,
.. i18n: has no roles
.. i18n: and is subject to no specialized rules. The \ ``admin``\   user is different, as you can see if you
.. i18n: follow the same sequence to review the its definition. It's a member of the \ ``admin``\   group,
.. i18n: which gives it more advanced rights to configure new users.

Click the :guilabel:`Security`  tab to see that the demo user is a member of only the ``Employee`` group,
has no roles
and is subject to no specialized rules. The \ ``admin``\   user is different, as you can see if you
follow the same sequence to review the its definition. It's a member of the \ ``admin``\   group,
which gives it more advanced rights to configure new users.

.. i18n: .. index:: 
.. i18n:    single: user; access
.. i18n:    single: user; role
.. i18n:    single: user; group

.. index:: 
   single: user; access
   single: user; role
   single: user; group

.. i18n: .. tip::  Roles, Groups and Users
.. i18n: 
.. i18n: 	Users and groups provide the structure for specifying access rights to different documents. Their
.. i18n: 	setup answers the question “Who has access to what?”
.. i18n: 
.. i18n: 	Roles are used in business processes for permitting or blocking certain steps in the workflow of a
.. i18n: 	given document. For example you can assign the role of approving an invoice. Roles answer the
.. i18n: 	question “Who should do what?”

.. tip::  Roles, Groups and Users

	Users and groups provide the structure for specifying access rights to different documents. Their
	setup answers the question “Who has access to what?”

	Roles are used in business processes for permitting or blocking certain steps in the workflow of a
	given document. For example you can assign the role of approving an invoice. Roles answer the
	question “Who should do what?”

.. i18n: Click :menuselection:`Administration --> Users --> Groups`  below the main menu to open the list of
.. i18n: groups defined in the system. If you open the form view of the \ ``admin``\   group by clicking its
.. i18n: name in the list, the first tab give you the list of all the users who belong to this group.

Click :menuselection:`Administration --> Users --> Groups`  below the main menu to open the list of
groups defined in the system. If you open the form view of the \ ``admin``\   group by clicking its
name in the list, the first tab give you the list of all the users who belong to this group.

.. i18n: Click the Security tab and it gives you details of the access rights for that group. These are
.. i18n: detailed later in :ref:`ch-config`, but you can already see there further up in the window, the list of menus
.. i18n: reserved for the admin group. By convention, the \ ``admin``\   in Open ERP has rights of access to
.. i18n: the :menuselection:`Configuration`  menu in each section. So \ ``Partners / Configuration``\   is
.. i18n: found in the list of access rights but \ ``Partners``\   isn't found there because it's accessible
.. i18n: to all users.

Click the Security tab and it gives you details of the access rights for that group. These are
detailed later in :ref:`ch-config`, but you can already see there further up in the window, the list of menus
reserved for the admin group. By convention, the \ ``admin``\   in Open ERP has rights of access to
the :menuselection:`Configuration`  menu in each section. So \ ``Partners / Configuration``\   is
found in the list of access rights but \ ``Partners``\   isn't found there because it's accessible
to all users.

.. i18n: You can create some new users to integrate them into the system. Assign them to predefined groups to
.. i18n: grant them certain access rights. Then try their access rights when you login as these users.
.. i18n: Management defines these access rights as described in :ref:`ch-config`.

You can create some new users to integrate them into the system. Assign them to predefined groups to
grant them certain access rights. Then try their access rights when you login as these users.
Management defines these access rights as described in :ref:`ch-config`.

.. i18n: .. note::  Changes to default access rights
.. i18n: 
.. i18n: 	New versions of Open ERP differ from earlier versions of Open ERP and Tiny ERP in this area:
.. i18n: 	many groups have been predefined and access to many of the menus and objects are keyed to these
.. i18n: 	groups by default.
.. i18n: 	This is quite a contrast to the rather liberal approach in 4.2.2 and before, where access rights
.. i18n: 	could be defined but were not activated by default.

.. note::  Changes to default access rights

	New versions of Open ERP differ from earlier versions of Open ERP and Tiny ERP in this area:
	many groups have been predefined and access to many of the menus and objects are keyed to these
	groups by default.
	This is quite a contrast to the rather liberal approach in 4.2.2 and before, where access rights
	could be defined but were not activated by default.

.. i18n: .. index::
.. i18n:    single: partner; managing

.. index::
   single: partner; managing

.. i18n: Managing partners
.. i18n: -------------------

Managing partners
-------------------

.. i18n: In Open ERP, a partner represents an entity that you do business with. That can be a prospect, a
.. i18n: customer, a supplier, or even an employee of your company.

In Open ERP, a partner represents an entity that you do business with. That can be a prospect, a
customer, a supplier, or even an employee of your company.

.. i18n: List of partners
.. i18n: ^^^^^^^^^^^^^^^^^

List of partners
^^^^^^^^^^^^^^^^^

.. i18n: Click :menuselection:`Partners --> Partners`  in the main menu to open the list of partners. Then
.. i18n: click the name of the first partner to get hold of the details – a form appears with several tabs
.. i18n: on it:

Click :menuselection:`Partners --> Partners`  in the main menu to open the list of partners. Then
click the name of the first partner to get hold of the details – a form appears with several tabs
on it:

.. i18n: * the :guilabel:`General` tab contains the main information about the company, such as its corporate
.. i18n:   name, its primary language, your different contacts at that partner and the categories it belongs
.. i18n:   to.
.. i18n: 
.. i18n: * the :guilabel:`Sales & Purchases` tab contains information that's slightly less immediate.
.. i18n: 
.. i18n: * the :menuselection:`History` tab contains the history of all the events that the partner has
.. i18n:   been involved in. These events are created automatically by different system documents: invoices,
.. i18n:   orders, support requests and so on, from a list that can be configured in the system. 
.. i18n:   These give you a rapid view of the partner's history on a single
.. i18n:   screen.
.. i18n: 
.. i18n: * the :menuselection:`Notes` tab is an area for free text notes.

* the :guilabel:`General` tab contains the main information about the company, such as its corporate
  name, its primary language, your different contacts at that partner and the categories it belongs
  to.

* the :guilabel:`Sales & Purchases` tab contains information that's slightly less immediate.

* the :menuselection:`History` tab contains the history of all the events that the partner has
  been involved in. These events are created automatically by different system documents: invoices,
  orders, support requests and so on, from a list that can be configured in the system. 
  These give you a rapid view of the partner's history on a single
  screen.

* the :menuselection:`Notes` tab is an area for free text notes.

.. i18n: To the right of the form is a list of Reports, Actions and Links related to a partner. Click some of 
.. i18n: them to get a feel for their use.

To the right of the form is a list of Reports, Actions and Links related to a partner. Click some of 
them to get a feel for their use.

.. i18n: .. figure:: images/partner.png
.. i18n:    :align: center
.. i18n:    :scale: 80
.. i18n: 
.. i18n:    *Partner form*

.. figure:: images/partner.png
   :align: center
   :scale: 80

   *Partner form*

.. i18n: .. index::
.. i18n:    single: partner; category

.. index::
   single: partner; category

.. i18n: .. tip::  Partner Categories
.. i18n: 
.. i18n: 	Partner Categories enable you to segment different partners according to their relation with you
.. i18n: 	(client, prospect, supplier, and so on). A partner can belong to several categories – for example
.. i18n: 	it may be both a customer and supplier at the same time.
.. i18n: 	
.. i18n: 	But there are also Customer, Supplier and Rental checkboxes on the partner form, which are different.
.. i18n: 	These checkboxes are designed to enable Open ERP to quickly select what should appear on some of the
.. i18n: 	system drop-down selection boxes. They, too, need to be set correctly.

.. tip::  Partner Categories

	Partner Categories enable you to segment different partners according to their relation with you
	(client, prospect, supplier, and so on). A partner can belong to several categories – for example
	it may be both a customer and supplier at the same time.
	
	But there are also Customer, Supplier and Rental checkboxes on the partner form, which are different.
	These checkboxes are designed to enable Open ERP to quickly select what should appear on some of the
	system drop-down selection boxes. They, too, need to be set correctly.

.. i18n: Partner Categories
.. i18n: ^^^^^^^^^^^^^^^^^^^

Partner Categories
^^^^^^^^^^^^^^^^^^^

.. i18n: You can list your partners by category using the menu :menuselection:`Partners --> Partners by
.. i18n: category` . This opens a hierarchical structure of categories where each category can be divided
.. i18n: into sub-categories. Click a category to obtain a list of partners in that category. For example,
.. i18n: click all of the partners in the category :menuselection:`Supplier`  or :menuselection:`Supplier -->
.. i18n: Components Supplier`. You'll see that if a company is in a subcategory (such as
.. i18n: :guilabel:`Components Supplier` ) then it will also show up when you click the parent category (such
.. i18n: as :guilabel:`Supplier`).

You can list your partners by category using the menu :menuselection:`Partners --> Partners by
category` . This opens a hierarchical structure of categories where each category can be divided
into sub-categories. Click a category to obtain a list of partners in that category. For example,
click all of the partners in the category :menuselection:`Supplier`  or :menuselection:`Supplier -->
Components Supplier`. You'll see that if a company is in a subcategory (such as
:guilabel:`Components Supplier` ) then it will also show up when you click the parent category (such
as :guilabel:`Supplier`).

.. i18n: .. figure:: images/main_window_partner_menu_config.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Categories of partner in a hierarchical structure, for example Customer, Prospect, Supplier*

.. figure:: images/main_window_partner_menu_config.png
   :scale: 75
   :align: center

   *Categories of partner in a hierarchical structure, for example Customer, Prospect, Supplier*

.. i18n: The administrator can define new categories. So you'll create a new category and link it to a
.. i18n: partner:

The administrator can define new categories. So you'll create a new category and link it to a
partner:

.. i18n: 	#. Use :menuselection:`Partners --> Configuration --> Partner Categories` to reach a list
.. i18n: 	   of the same categories as above but in a list view rather than a hierarchical tree structure.
.. i18n: 
.. i18n: 	#. Click :guilabel:`New` to open an empty form for creating a new category
.. i18n: 
.. i18n: 	#. Enter \ ``My Prospects``\  in the field :guilabel:`Name of Category`. Then click on the
.. i18n: 	   :guilabel:`Search` icon to the right of the :guilabel:`Parent Category` field and select 
.. i18n: 	   \ ``Prospect``\  in the list that appears.
.. i18n: 
.. i18n: 	#. Then save your new category using the :guilabel:`Save` button.

	#. Use :menuselection:`Partners --> Configuration --> Partner Categories` to reach a list
	   of the same categories as above but in a list view rather than a hierarchical tree structure.

	#. Click :guilabel:`New` to open an empty form for creating a new category

	#. Enter \ ``My Prospects``\  in the field :guilabel:`Name of Category`. Then click on the
	   :guilabel:`Search` icon to the right of the :guilabel:`Parent Category` field and select 
	   \ ``Prospect``\  in the list that appears.

	#. Then save your new category using the :guilabel:`Save` button.

.. i18n: .. tip:: Required Fields
.. i18n: 
.. i18n: 	Fields colored blue are required. If you try to save the form while any of these fields are empty
.. i18n: 	the field turns red to indicate that there's a problem. It's impossible to save the form until
.. i18n: 	you've completed every required field.

.. tip:: Required Fields

	Fields colored blue are required. If you try to save the form while any of these fields are empty
	the field turns red to indicate that there's a problem. It's impossible to save the form until
	you've completed every required field.

.. i18n: You can review your new category structure using :menuselection:`Partners --> Partners by category`. 
.. i18n: You should see the new structure of \ ``Prospects / My Prospects``\   there.

You can review your new category structure using :menuselection:`Partners --> Partners by category`. 
You should see the new structure of \ ``Prospects / My Prospects``\   there.

.. i18n: .. figure:: images/main_window_partner_tab.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Creating a new partner category*

.. figure:: images/main_window_partner_tab.png
   :scale: 75
   :align: center

   *Creating a new partner category*

.. i18n: To create a new partner and link it to this new category open a new partner form to modify it.

To create a new partner and link it to this new category open a new partner form to modify it.

.. i18n: 	#. In the :guilabel:`General` tab, type \ ``New Partner``\  into the :guilabel:`Name` field.
.. i18n: 
.. i18n: 	#. Then click on the search icon to the right of the :guilabel:`Categories` field and select your
.. i18n: 	   new category from the list that appears: \ ``Prospect / My Prospects``\
.. i18n: 
.. i18n: 	#. Then save your partner by clicking :guilabel:`Save`  The partner now belongs in the category 
.. i18n: 	   \ ``Prospect / My prospects.``\
.. i18n: 
.. i18n: 	#. Monitor your modification in the menu :menuselection:`Partners --> Partners by category`. Select
.. i18n: 	   the category :guilabel:`My Prospect`. The list of partners opens and you'll find your new partner
.. i18n: 	   there in that list.

	#. In the :guilabel:`General` tab, type \ ``New Partner``\  into the :guilabel:`Name` field.

	#. Then click on the search icon to the right of the :guilabel:`Categories` field and select your
	   new category from the list that appears: \ ``Prospect / My Prospects``\

	#. Then save your partner by clicking :guilabel:`Save`  The partner now belongs in the category 
	   \ ``Prospect / My prospects.``\

	#. Monitor your modification in the menu :menuselection:`Partners --> Partners by category`. Select
	   the category :guilabel:`My Prospect`. The list of partners opens and you'll find your new partner
	   there in that list.

.. i18n: .. tip:: Searching for documents
.. i18n: 
.. i18n: 	If you need to search through a long list of partners it's best to use the available search
.. i18n: 	criteria rather than scroll through the whole partner list. It's a habit that'll save you a lot of
.. i18n: 	time in the long run as you search for all kinds of documents.

.. tip:: Searching for documents

	If you need to search through a long list of partners it's best to use the available search
	criteria rather than scroll through the whole partner list. It's a habit that'll save you a lot of
	time in the long run as you search for all kinds of documents.

.. i18n: .. note::  Example Categories of partners
.. i18n: 
.. i18n: 	A partner can be assigned to several categories. These enable you to create alternative
.. i18n: 	classifications as necessary, usually in a hierarchical form.
.. i18n: 
.. i18n: 	Here are some structures that are often used:
.. i18n: 
.. i18n: 	* geographical locations,
.. i18n: 
.. i18n: 	* interest in certain product lines,
.. i18n: 
.. i18n: 	* subscriptions to newsletters,
.. i18n: 
.. i18n: 	* type of industry.

.. note::  Example Categories of partners

	A partner can be assigned to several categories. These enable you to create alternative
	classifications as necessary, usually in a hierarchical form.

	Here are some structures that are often used:

	* geographical locations,

	* interest in certain product lines,

	* subscriptions to newsletters,

	* type of industry.

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
