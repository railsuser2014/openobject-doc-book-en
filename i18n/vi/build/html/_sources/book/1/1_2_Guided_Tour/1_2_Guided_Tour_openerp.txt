
.. i18n: Guided Tour of Open ERP
.. i18n: =======================

Guided Tour of Open ERP
=======================

.. i18n: You'll now explore the database \ ``openerp_ch02``\   with these profile modules installed to give
.. i18n: you an insight into the coverage of the core Open ERP software.

You'll now explore the database \ ``openerp_ch02``\   with these profile modules installed to give
you an insight into the coverage of the core Open ERP software.

.. i18n: .. tip:: Translating new modules
.. i18n: 
.. i18n: 	When you've installed a new module and are using additional languages to English you have to reload
.. i18n: 	the translation file. New terms introduced in these modules aren't translated by default. To do
.. i18n: 	this use :menuselection:`Administration --> Translations --> Load an Official Translation`.

.. tip:: Translating new modules

	When you've installed a new module and are using additional languages to English you have to reload
	the translation file. New terms introduced in these modules aren't translated by default. To do
	this use :menuselection:`Administration --> Translations --> Load an Official Translation`.

.. i18n: Depending on the user you're connected as the page appears differently from the Main Menu that
.. i18n: showed before. Using the installation sequence above, certain dashboards may be assigned as various
.. i18n: users' home pages. They show a summary of the information required to start the day effectively. A
.. i18n: project dashboard might contains:

Depending on the user you're connected as the page appears differently from the Main Menu that
showed before. Using the installation sequence above, certain dashboards may be assigned as various
users' home pages. They show a summary of the information required to start the day effectively. A
project dashboard might contains:

.. i18n: * a list of the next tasks to carry out,
.. i18n: 
.. i18n: * a list of the next deadlines,
.. i18n: 
.. i18n: * public notes about projects,
.. i18n: 
.. i18n: * a planning chart of hours required,
.. i18n: 
.. i18n: * the timesheet.

* a list of the next tasks to carry out,

* a list of the next deadlines,

* public notes about projects,

* a planning chart of hours required,

* the timesheet.

.. i18n: Each of the lists can be reordered by clicking on the heading of a column – first in ascending
.. i18n: then in descending order as you click repeatedly. To get more information about any particular entry
.. i18n: click on the name in the first column, or if you want to show a particular panel click :guilabel:`Zoom`
.. i18n: above it.

Each of the lists can be reordered by clicking on the heading of a column – first in ascending
then in descending order as you click repeatedly. To get more information about any particular entry
click on the name in the first column, or if you want to show a particular panel click :guilabel:`Zoom`
above it.

.. i18n: .. figure:: images/admin_project_dashboard.png
.. i18n:    :align: center
.. i18n:    :scale: 75
.. i18n: 
.. i18n:    *Project Dashboard*

.. figure:: images/admin_project_dashboard.png
   :align: center
   :scale: 75

   *Project Dashboard*

.. i18n: Users' home pages are automatically reassigned during the creation or upgrading of a database. It's
.. i18n: usual to assign a dashboard to someone's home page but any Open ERP screen can be assigned to the
.. i18n: home page of any user.

Users' home pages are automatically reassigned during the creation or upgrading of a database. It's
usual to assign a dashboard to someone's home page but any Open ERP screen can be assigned to the
home page of any user.

.. i18n: .. index::
.. i18n:    single: shortcut

.. index::
   single: shortcut

.. i18n: .. tip:: Creating shortcuts
.. i18n: 
.. i18n: 	Each user has access to many menu items throughout all of the available menu hierarchy. But in
.. i18n: 	general an employee uses only a small part of the system's functions.
.. i18n: 
.. i18n: 	So you can define shortcuts for the most-used menus. These shortcuts are personal for each user. To
.. i18n: 	create a new shortcut open the select menu and click on the :guilabel:`Add` link to the far right of
.. i18n: 	:guilabel:`SHORTCUTS`.
.. i18n: 
.. i18n: 	To change or replace a link click :guilabel:`SHORTCUTS`. Open ERP then opens a list of
.. i18n: 	editable shortcuts.

.. tip:: Creating shortcuts

	Each user has access to many menu items throughout all of the available menu hierarchy. But in
	general an employee uses only a small part of the system's functions.

	So you can define shortcuts for the most-used menus. These shortcuts are personal for each user. To
	create a new shortcut open the select menu and click on the :guilabel:`Add` link to the far right of
	:guilabel:`SHORTCUTS`.

	To change or replace a link click :guilabel:`SHORTCUTS`. Open ERP then opens a list of
	editable shortcuts.

.. i18n: The following sections present an overview of the main functions of Open ERP. Some areas are
.. i18n: covered in more detail in the following chapters of this book and you'll find many other functions
.. i18n: available in the optional modules. Functions are presented in the order that they appear on the main
.. i18n: menu.

The following sections present an overview of the main functions of Open ERP. Some areas are
covered in more detail in the following chapters of this book and you'll find many other functions
available in the optional modules. Functions are presented in the order that they appear on the main
menu.

.. i18n: .. index::
.. i18n:    single: Partners

.. index::
   single: Partners

.. i18n: Partners
.. i18n: --------

Partners
--------

.. i18n: To familiarize yourself with Open ERP's interface, you'll start work with information about
.. i18n: partners. Clicking :menuselection:`Partners --> Partners` brings up a list of partners that were
.. i18n: automatically loaded when you created the database with :guilabel:`Load Demonstration Data` checked.

To familiarize yourself with Open ERP's interface, you'll start work with information about
partners. Clicking :menuselection:`Partners --> Partners` brings up a list of partners that were
automatically loaded when you created the database with :guilabel:`Load Demonstration Data` checked.

.. i18n: .. index::
.. i18n:    single: partner; search

.. index::
   single: partner; search

.. i18n: Search for a partner
.. i18n: ^^^^^^^^^^^^^^^^^^^^

Search for a partner
^^^^^^^^^^^^^^^^^^^^

.. i18n: Above the partner list you'll see a search form that enables you to quickly filter the partners. Two
.. i18n: tabs are available for searching – :guilabel:`Basic Search` and :guilabel:`Advanced Search`. The
.. i18n: latter simply shows more fields to narrow your selection.

Above the partner list you'll see a search form that enables you to quickly filter the partners. Two
tabs are available for searching – :guilabel:`Basic Search` and :guilabel:`Advanced Search`. The
latter simply shows more fields to narrow your selection.

.. i18n: If you've applied no filter, the list shows every partner in the system. For space reasons this list
.. i18n: shows only the first few partners. If you want to display other records you can search for them or
.. i18n: navigate through the whole list using the :guilabel:`First`, :guilabel:`Previous`, :guilabel:`Next`, :guilabel:`Last` arrows.

If you've applied no filter, the list shows every partner in the system. For space reasons this list
shows only the first few partners. If you want to display other records you can search for them or
navigate through the whole list using the :guilabel:`First`, :guilabel:`Previous`, :guilabel:`Next`, :guilabel:`Last` arrows.

.. i18n: .. figure:: images/partner_search_tab.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Standard partner search*

.. figure:: images/partner_search_tab.png
   :scale: 75
   :align: center

   *Standard partner search*

.. i18n: .. note:: List limits
.. i18n: 
.. i18n: 	By default the list in the GTK client shows only the first 80 records, to avoid overloading the
.. i18n: 	network and the server.
.. i18n: 
.. i18n: 	But you can change that limit by clicking the + icon to the left of the search criteria,
.. i18n: 	and you can change the offset so that it starts further down the whole list than the first entry.
.. i18n: 
.. i18n: 	Similarly the list in the web client shows only the first 20, 40, 60, 80 or 100 records.
.. i18n: 
.. i18n: 	The actual number can be switched by clicking on the number and selecting one of the other limits,
.. i18n: 	but you can't select any other limit (so, unlike the GTK client you can't select hundreds or
.. i18n: 	thousands).

.. note:: List limits

	By default the list in the GTK client shows only the first 80 records, to avoid overloading the
	network and the server.

	But you can change that limit by clicking the + icon to the left of the search criteria,
	and you can change the offset so that it starts further down the whole list than the first entry.

	Similarly the list in the web client shows only the first 20, 40, 60, 80 or 100 records.

	The actual number can be switched by clicking on the number and selecting one of the other limits,
	but you can't select any other limit (so, unlike the GTK client you can't select hundreds or
	thousands).

.. i18n: If you click on the name of a partner the form view corresponding to that partner opens in Read-Only
.. i18n: mode. In the list you could alternatively click the pencil icon to open the same form in Edit mode.
.. i18n: Once you have a form you can toggle between the two modes by clicking :guilabel:`Save` or :guilabel:`Cancel` when in
.. i18n: Edit mode and :guilabel:`Edit` when in Read-Only mode.

If you click on the name of a partner the form view corresponding to that partner opens in Read-Only
mode. In the list you could alternatively click the pencil icon to open the same form in Edit mode.
Once you have a form you can toggle between the two modes by clicking :guilabel:`Save` or :guilabel:`Cancel` when in
Edit mode and :guilabel:`Edit` when in Read-Only mode.

.. i18n: When you're in Read-Only mode you can navigate through the whole list you selected, as though you
.. i18n: were in the List view. In Read-Only mode you can also click :guilabel:`Search` to see the form in
.. i18n: List view again.

When you're in Read-Only mode you can navigate through the whole list you selected, as though you
were in the List view. In Read-Only mode you can also click :guilabel:`Search` to see the form in
List view again.

.. i18n: .. index::
.. i18n:    single: partner; view form

.. index::
   single: partner; view form

.. i18n: Partner form
.. i18n: ^^^^^^^^^^^^

Partner form
^^^^^^^^^^^^

.. i18n: The partner form contains several tabs, all referring to the current record:

The partner form contains several tabs, all referring to the current record:

.. i18n: *  :guilabel:`General`,
.. i18n: 
.. i18n: *  :guilabel:`Suppliers & Customers`,
.. i18n: 
.. i18n: *  :guilabel:`History`,
.. i18n: 
.. i18n: *  :guilabel:`Notes`.

*  :guilabel:`General`,

*  :guilabel:`Suppliers & Customers`,

*  :guilabel:`History`,

*  :guilabel:`Notes`.

.. i18n: The fields in a tab aren't all of the same type – some (such as :guilabel:`Name`) contain free
.. i18n: text, some (such as the :guilabel:`Language`) enable you to select a value from a list of options,
.. i18n: others give you a view of another object (such as :guilabel:`Partner Contacts` – because a partner
.. i18n: can have several contacts) or a list of link to another object (such as :guilabel:`Categories`).
.. i18n: There are checkboxes (such as the :guilabel:`Active` field in the :guilabel:`Suppliers & Customers` tab),
.. i18n: numeric fields (such as :guilabel:`Credit Limit`) and date fields (such as :guilabel:`Date`).

The fields in a tab aren't all of the same type – some (such as :guilabel:`Name`) contain free
text, some (such as the :guilabel:`Language`) enable you to select a value from a list of options,
others give you a view of another object (such as :guilabel:`Partner Contacts` – because a partner
can have several contacts) or a list of link to another object (such as :guilabel:`Categories`).
There are checkboxes (such as the :guilabel:`Active` field in the :guilabel:`Suppliers & Customers` tab),
numeric fields (such as :guilabel:`Credit Limit`) and date fields (such as :guilabel:`Date`).

.. i18n: The :guilabel:`History` tab gives a quick overview of things that have happened to the partner – an
.. i18n: overview of useful information such as orders, open invoices and support requests. Events are
.. i18n: generated automatically by Open ERP from changes in other documents that refer to this partner.

The :guilabel:`History` tab gives a quick overview of things that have happened to the partner – an
overview of useful information such as orders, open invoices and support requests. Events are
generated automatically by Open ERP from changes in other documents that refer to this partner.

.. i18n: It's possible to add events manually, such as a note recording a phone call. To add a new event
.. i18n: click :guilabel:`Create new record.` to the right of the :guilabel:`Partner Events`  field. That
.. i18n: opens a new :guilabel:`Partner Events` dialog box enabling an event to be created and added to the
.. i18n: current partner.

It's possible to add events manually, such as a note recording a phone call. To add a new event
click :guilabel:`Create new record.` to the right of the :guilabel:`Partner Events`  field. That
opens a new :guilabel:`Partner Events` dialog box enabling an event to be created and added to the
current partner.

.. i18n: Actions possible on a partner
.. i18n: ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Actions possible on a partner
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. i18n: To the right of the partner form is a toolbar containing a list of possible :guilabel:`Reports` , 
.. i18n: :guilabel:`Actions`, and quick :guilabel:`Links` about the partner displayed in the form.

To the right of the partner form is a toolbar containing a list of possible :guilabel:`Reports` , 
:guilabel:`Actions`, and quick :guilabel:`Links` about the partner displayed in the form.

.. i18n: You can generate PDF documents about the selected object (or, in list view, about one or more
.. i18n: selected objects) using certain buttons in the :guilabel:`Reports` section of the toolbar:

You can generate PDF documents about the selected object (or, in list view, about one or more
selected objects) using certain buttons in the :guilabel:`Reports` section of the toolbar:

.. i18n: *  :guilabel:`Labels` : print address labels for the selected partners,

*  :guilabel:`Labels` : print address labels for the selected partners,

.. i18n: Certain actions can be started by the following buttons in the :guilabel:`Actions` section of the
.. i18n: toolbar:

Certain actions can be started by the following buttons in the :guilabel:`Actions` section of the
toolbar:

.. i18n: *  :guilabel:`Company Architecture` : opens a window showing the partners and their children in a
.. i18n:    hierarchical structure.
.. i18n: 
.. i18n: *  :guilabel:`Send SMS` : enables you to send an SMS to selected partners. This system uses the bulk
.. i18n:    SMS facilities of the Clickatell® company http://clickatell.com.
.. i18n: 
.. i18n: *  :guilabel:`Mass Mailing` : enables you to send an email to a selection of partners.

*  :guilabel:`Company Architecture` : opens a window showing the partners and their children in a
   hierarchical structure.

*  :guilabel:`Send SMS` : enables you to send an SMS to selected partners. This system uses the bulk
   SMS facilities of the Clickatell® company http://clickatell.com.

*  :guilabel:`Mass Mailing` : enables you to send an email to a selection of partners.

.. i18n: .. index::
.. i18n:    single: buttons; reports, actions, links

.. index::
   single: buttons; reports, actions, links

.. i18n: .. tip:: Reports, Actions and Links in the GTK client
.. i18n: 
.. i18n: 	When you're viewing a form in the GTK client, the buttons to the right of the form are shortcuts to
.. i18n: 	the same Reports, Actions and Links as described in the text. When you're viewing a list (such as
.. i18n: 	the partner list) those buttons aren't available to you. Instead, you can reach Reports and Actions
.. i18n: 	through two of the buttons in the toolbar at the top of the list – Print and Action.

.. tip:: Reports, Actions and Links in the GTK client

	When you're viewing a form in the GTK client, the buttons to the right of the form are shortcuts to
	the same Reports, Actions and Links as described in the text. When you're viewing a list (such as
	the partner list) those buttons aren't available to you. Instead, you can reach Reports and Actions
	through two of the buttons in the toolbar at the top of the list – Print and Action.

.. i18n: Partners are used throughout the Open ERP system in other documents. For example, the menu
.. i18n: :menuselection:`Sales Management --> Sales Orders --> All Sales Orders` brings up all the Sales
.. i18n: Orders in list view. Click the name of a partner rather than the order number on one of those lines
.. i18n: and you'll get the Partner form rather than the Sales Order form.

Partners are used throughout the Open ERP system in other documents. For example, the menu
:menuselection:`Sales Management --> Sales Orders --> All Sales Orders` brings up all the Sales
Orders in list view. Click the name of a partner rather than the order number on one of those lines
and you'll get the Partner form rather than the Sales Order form.

.. i18n: .. tip:: Right clicks and shortcuts
.. i18n: 
.. i18n: 	In the GTK client you don't get hyperlinks to other document types. Instead, you can right-click in
.. i18n: 	a list view to show the linked fields (that is fields having a link to other forms) on that line.
.. i18n: 
.. i18n: 	In the web client you'll see hyperlink shortcuts on several of the fields on a form that's in Read-
.. i18n: 	Only mode, so that you can move onto the form for those entries. When the web form is in Edit mode,
.. i18n: 	you can instead hold down the control button on the keyboard and right-click with the mouse button
.. i18n: 	in the field, to get all of the linked fields in a pop-up menu just as you would with the GTK
.. i18n: 	client.
.. i18n: 
.. i18n: 	You can quickly try this out by going to any one of the sales orders in :menuselection:`Sales
.. i18n: 	Management --> Sales Order --> All Sales Orders` and seeing what you can reach from the
.. i18n: 	:guilabel:`Customer` field on that sales order form using either the web client with the form in
.. i18n: 	both read-only and in edit mode, or with the GTK client.

.. tip:: Right clicks and shortcuts

	In the GTK client you don't get hyperlinks to other document types. Instead, you can right-click in
	a list view to show the linked fields (that is fields having a link to other forms) on that line.

	In the web client you'll see hyperlink shortcuts on several of the fields on a form that's in Read-
	Only mode, so that you can move onto the form for those entries. When the web form is in Edit mode,
	you can instead hold down the control button on the keyboard and right-click with the mouse button
	in the field, to get all of the linked fields in a pop-up menu just as you would with the GTK
	client.

	You can quickly try this out by going to any one of the sales orders in :menuselection:`Sales
	Management --> Sales Order --> All Sales Orders` and seeing what you can reach from the
	:guilabel:`Customer` field on that sales order form using either the web client with the form in
	both read-only and in edit mode, or with the GTK client.

.. i18n: .. figure:: images/familiarization_sale_partner.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Links for a partner appear in an order form*

.. figure:: images/familiarization_sale_partner.png
   :scale: 75
   :align: center

   *Links for a partner appear in an order form*

.. i18n: Before moving on to the next module, take a quick look into the :menuselection:`Partners -->
.. i18n: Configuration`  menu, particularly :menuselection:`Partner Categories`  and  :menuselection:`Localisation` menus.
.. i18n: They contain some of the demonstration data that you installed when you created the database.

Before moving on to the next module, take a quick look into the :menuselection:`Partners -->
Configuration`  menu, particularly :menuselection:`Partner Categories`  and  :menuselection:`Localisation` menus.
They contain some of the demonstration data that you installed when you created the database.

.. i18n: .. index::
.. i18n:    single: Accounting and Finance
.. i18n:    single: Financial Management

.. index::
   single: Accounting and Finance
   single: Financial Management

.. i18n: Financial Management
.. i18n: --------------------

Financial Management
--------------------

.. i18n: The chapters in :ref:`part-genacct` in this book are dedicated to general and analytic accounting. 
.. i18n: A brief overview of
.. i18n: the functions provided by these modules is given here as an introduction.

The chapters in :ref:`part-genacct` in this book are dedicated to general and analytic accounting. 
A brief overview of
the functions provided by these modules is given here as an introduction.

.. i18n: Accounting is totally integrated into all of the company's functions, whether it's general,
.. i18n: analytic, budgetary or auxiliary accounting. Open ERP's accounting function is double-entry and
.. i18n: supports multiple company divisions and multiple companies, as well as multiple currencies and
.. i18n: languages.

Accounting is totally integrated into all of the company's functions, whether it's general,
analytic, budgetary or auxiliary accounting. Open ERP's accounting function is double-entry and
supports multiple company divisions and multiple companies, as well as multiple currencies and
languages.

.. i18n: Accounting that's integrated throughout all of the company's processes greatly simplifies the work
.. i18n: of entering accounting data, because most of the entries are generated automatically while other
.. i18n: documents are being processed. You can avoid entering data twice in Open ERP, which is commonly a
.. i18n: source of errors and delays.

Accounting that's integrated throughout all of the company's processes greatly simplifies the work
of entering accounting data, because most of the entries are generated automatically while other
documents are being processed. You can avoid entering data twice in Open ERP, which is commonly a
source of errors and delays.

.. i18n: So Open ERP's accounting isn't just for financial reporting – it's also the anchorpoint for many
.. i18n: of a company's management processes. For example if one of your accountants puts a customer on
.. i18n: credit hold then that will immediately block any other action related to that company's credit (such
.. i18n: as a sale or a delivery).

So Open ERP's accounting isn't just for financial reporting – it's also the anchorpoint for many
of a company's management processes. For example if one of your accountants puts a customer on
credit hold then that will immediately block any other action related to that company's credit (such
as a sale or a delivery).

.. i18n: Open ERP also provides integrated analytical accounting, which enables management by business
.. i18n: activity or project and provides very detailed levels of analysis. You can control your operations
.. i18n: based on business management needs, rather than on the charts of accounts that generally meet only
.. i18n: statutory requirements.

Open ERP also provides integrated analytical accounting, which enables management by business
activity or project and provides very detailed levels of analysis. You can control your operations
based on business management needs, rather than on the charts of accounts that generally meet only
statutory requirements.

.. i18n: .. index::
.. i18n:    single: Dashboards

.. index::
   single: Dashboards

.. i18n: Dashboards
.. i18n: ----------

Dashboards
----------

.. i18n: Dashboards give you an overview of all the information that's important to you on a single page. The
.. i18n: :menuselection:`Dashboards` menu gives you access to predefined boards for
.. i18n: :menuselection:`Financial Management`, :menuselection:`Manufacturing` and :menuselection:`Project Management`.

Dashboards give you an overview of all the information that's important to you on a single page. The
:menuselection:`Dashboards` menu gives you access to predefined boards for
:menuselection:`Financial Management`, :menuselection:`Manufacturing` and :menuselection:`Project Management`.

.. i18n: .. note:: Dashboards
.. i18n: 
.. i18n: 	Unlike most other ERP systems and classic statistically-based systems,
.. i18n: 	Open ERP can provide dashboards to all of the system's users, and not just to a select few
.. i18n: 	such as directors and accountants.
.. i18n: 
.. i18n: 	Users can each have their own dashboard, adapted to their needs,
.. i18n: 	to enable them to manage their own work effectively.
.. i18n: 	For example a developer using the :guilabel:`Project Dashboard` can see such information
.. i18n: 	as a list of the next tasks, task completion history and an analysis of the state of progress of
.. i18n: 	the relevant projects.

.. note:: Dashboards

	Unlike most other ERP systems and classic statistically-based systems,
	Open ERP can provide dashboards to all of the system's users, and not just to a select few
	such as directors and accountants.

	Users can each have their own dashboard, adapted to their needs,
	to enable them to manage their own work effectively.
	For example a developer using the :guilabel:`Project Dashboard` can see such information
	as a list of the next tasks, task completion history and an analysis of the state of progress of
	the relevant projects.

.. i18n: Dashboards are dynamic, which lets you navigate easily around the whole information base.
.. i18n: Using the icons above a graph, for example, you can filter the data or zoom into the graph. You can
.. i18n: click on any element of the list to get detailed statistics on the selected element.

Dashboards are dynamic, which lets you navigate easily around the whole information base.
Using the icons above a graph, for example, you can filter the data or zoom into the graph. You can
click on any element of the list to get detailed statistics on the selected element.

.. i18n: Dashboards are adaptable to the needs of each user and each company.

Dashboards are adaptable to the needs of each user and each company.

.. i18n: .. note:: Construction of dashboards
.. i18n: 
.. i18n: 	Open ERP contains a dashboard editor. It lets you construct your own dashboard to fit your
.. i18n: 	specific needs using only a few clicks.

.. note:: Construction of dashboards

	Open ERP contains a dashboard editor. It lets you construct your own dashboard to fit your
	specific needs using only a few clicks.

.. i18n: .. index::
.. i18n:    single: Products

.. index::
   single: Products

.. i18n: Products
.. i18n: --------

Products
--------

.. i18n: In Open ERP, product means a raw material, a stockable product, a consumable or a service. You can
.. i18n: work with whole products or with templates that separate the definition of products and variants.

In Open ERP, product means a raw material, a stockable product, a consumable or a service. You can
work with whole products or with templates that separate the definition of products and variants.

.. i18n: For example if you sell t-shirts in different sizes and colors:

For example if you sell t-shirts in different sizes and colors:

.. i18n: * the product template is the “T-shirt” which contains information common to all sizes and all
.. i18n:   colors,
.. i18n: 
.. i18n: * the variants are “Size:S” and “Color:Red”, which define the parameters for that size and
.. i18n:   color,
.. i18n: 
.. i18n: * the final product is thus the combination of the two – t-shirt in size S and color Red.

* the product template is the “T-shirt” which contains information common to all sizes and all
  colors,

* the variants are “Size:S” and “Color:Red”, which define the parameters for that size and
  color,

* the final product is thus the combination of the two – t-shirt in size S and color Red.

.. i18n: The value of this approach for some sectors is that you can just define a template in detail and all
.. i18n: of its available variants briefly rather than every item as an entire product.

The value of this approach for some sectors is that you can just define a template in detail and all
of its available variants briefly rather than every item as an entire product.

.. i18n: 	.. note::  *Example Product templates and variants*
.. i18n: 
.. i18n: 			A product can be defined as a whole or as a product template and several variants. The variants
.. i18n: 			can be in one or several dimensions, depending on the installed modules.
.. i18n: 
.. i18n: 			For example, if you work in textiles, the variants on the product template for “T-shirt” are:
.. i18n: 
.. i18n: 			* Size (S, M, L, XL, XXL),
.. i18n: 
.. i18n: 			* Colour (white, grey, black, red),
.. i18n: 
.. i18n: 			* Quality of Cloth (125g/m2, 150g/m2, 160g/m2, 180g/m2),
.. i18n: 
.. i18n: 			* Collar (V, Round).
.. i18n: 			
.. i18n: 			.. index::
.. i18n: 			   single: module; product_variant_multi
.. i18n: 
.. i18n: 			This separation of variant types requires the optional module :mod:`product_variant_multi`. Using it
.. i18n: 			means that you can avoid an explosion in the number of products to manage in the database. If you
.. i18n: 			take the example above it's easier to manage a template with 15 variants in four different types
.. i18n: 			than 160 completely different products. This module is available in the ``addons-extra`` list (it had
.. i18n: 			not been updated, at the time of writing, to work in release 5.0 of Open ERP).

	.. note::  *Example Product templates and variants*

			A product can be defined as a whole or as a product template and several variants. The variants
			can be in one or several dimensions, depending on the installed modules.

			For example, if you work in textiles, the variants on the product template for “T-shirt” are:

			* Size (S, M, L, XL, XXL),

			* Colour (white, grey, black, red),

			* Quality of Cloth (125g/m2, 150g/m2, 160g/m2, 180g/m2),

			* Collar (V, Round).
			
			.. index::
			   single: module; product_variant_multi

			This separation of variant types requires the optional module :mod:`product_variant_multi`. Using it
			means that you can avoid an explosion in the number of products to manage in the database. If you
			take the example above it's easier to manage a template with 15 variants in four different types
			than 160 completely different products. This module is available in the ``addons-extra`` list (it had
			not been updated, at the time of writing, to work in release 5.0 of Open ERP).

.. i18n: The :menuselection:`Products` menu gives you access to the definition of products and their
.. i18n: constituent templates and variants, and to price lists.

The :menuselection:`Products` menu gives you access to the definition of products and their
constituent templates and variants, and to price lists.

.. i18n: .. index::
.. i18n:    single: Product; Consumable

.. index::
   single: Product; Consumable

.. i18n: .. tip::  Consumables
.. i18n: 
.. i18n: 	In Open ERP a consumable is a physical product which is treated like a stockable product except
.. i18n: 	that stock management isn't taken into account by the system. You could buy it, deliver it or
.. i18n: 	produce it but Open ERP will always assume that there's enough of it in stock. It never triggers a
.. i18n: 	procurement exception.

.. tip::  Consumables

	In Open ERP a consumable is a physical product which is treated like a stockable product except
	that stock management isn't taken into account by the system. You could buy it, deliver it or
	produce it but Open ERP will always assume that there's enough of it in stock. It never triggers a
	procurement exception.

.. i18n: Open a product form to see the information that describes it. Several different types of product can
.. i18n: be found in the demonstration data, giving quite a good overview of the possible options.

Open a product form to see the information that describes it. Several different types of product can
be found in the demonstration data, giving quite a good overview of the possible options.

.. i18n: Price lists (:menuselection:`Products --> Pricelists`) determine the purchase and selling prices and
.. i18n: adjustments derived from the use of different currencies. The :menuselection:`Default Purchase
.. i18n: Pricelist` uses the product's :guilabel:`Cost`  field to base a Purchase price on. The
.. i18n: :menuselection:`Default Sale Pricelist` uses the product's :guilabel:`List Price` field to base a
.. i18n: Sales price on when issuing a quote.

Price lists (:menuselection:`Products --> Pricelists`) determine the purchase and selling prices and
adjustments derived from the use of different currencies. The :menuselection:`Default Purchase
Pricelist` uses the product's :guilabel:`Cost`  field to base a Purchase price on. The
:menuselection:`Default Sale Pricelist` uses the product's :guilabel:`List Price` field to base a
Sales price on when issuing a quote.

.. i18n: Price lists are extremely flexible and enable you to put a whole price management policy in place.
.. i18n: They're composed of simple rules that enable you to build up a rule set for most complex situations:
.. i18n: multiple discounts, selling prices based on purchase prices, price reductions, promotions on whole
.. i18n: product ranges and so on.

Price lists are extremely flexible and enable you to put a whole price management policy in place.
They're composed of simple rules that enable you to build up a rule set for most complex situations:
multiple discounts, selling prices based on purchase prices, price reductions, promotions on whole
product ranges and so on.

.. i18n: You can find many optional modules to extend product functionality through the Open ERP website,
.. i18n: such as:

You can find many optional modules to extend product functionality through the Open ERP website,
such as:

.. i18n: .. index::
.. i18n:    single: module; membership

.. index::
   single: module; membership

.. i18n: * :mod:`membership` : for managing the subscriptions of members of a company,

* :mod:`membership` : for managing the subscriptions of members of a company,

.. i18n:   .. index::
.. i18n:      single: module; product_electronic

  .. index::
     single: module; product_electronic

.. i18n: * :mod:`product_electronic` : for managing electronic products,

* :mod:`product_electronic` : for managing electronic products,

.. i18n:   .. index::
.. i18n:      single: module; product_extended

  .. index::
     single: module; product_extended

.. i18n: * :mod:`product_extended` : for managing production costs,

* :mod:`product_extended` : for managing production costs,

.. i18n:   .. index::
.. i18n:      single: module; product_expiry

  .. index::
     single: module; product_expiry

.. i18n: * :mod:`product_expiry` : for agro-food products where items must be retired after a certain
.. i18n:   period,

* :mod:`product_expiry` : for agro-food products where items must be retired after a certain
  period,

.. i18n:   .. index::
.. i18n:      single: module; product_lot_foundry

  .. index::
     single: module; product_lot_foundry

.. i18n: * :mod:`product_lot_foundry` : for managing forged metal products.

* :mod:`product_lot_foundry` : for managing forged metal products.

.. i18n:   .. index::
.. i18n:      single: Human Resources
.. i18n:      single: HR

  .. index::
     single: Human Resources
     single: HR

.. i18n: Human Resources
.. i18n: ---------------

Human Resources
---------------

.. i18n: Open ERP's Human Resources Management modules provide such functionality as:

Open ERP's Human Resources Management modules provide such functionality as:

.. i18n: * management of staff and the holiday calendar,
.. i18n: 
.. i18n: * management of employment contracts,
.. i18n: 
.. i18n: * benefits management,
.. i18n: 
.. i18n: * management of holiday and sickness breaks,
.. i18n: 
.. i18n: * managing claims processes,
.. i18n: 
.. i18n: * management of staff performance,
.. i18n: 
.. i18n: * management of skills and competencies.

* management of staff and the holiday calendar,

* management of employment contracts,

* benefits management,

* management of holiday and sickness breaks,

* managing claims processes,

* management of staff performance,

* management of skills and competencies.

.. i18n: .. index::
.. i18n:    single: modules; hr_
.. i18n:    single: module; hr

.. index::
   single: modules; hr_
   single: module; hr

.. i18n: Most of these functions are provided from optional modules whose name starts with \ ``hr_``\
.. i18n: rather than the core :mod:`hr` module, but they're all loaded into the main :menuselection:`Human
.. i18n: Resources` menu.

Most of these functions are provided from optional modules whose name starts with \ ``hr_``\
rather than the core :mod:`hr` module, but they're all loaded into the main :menuselection:`Human
Resources` menu.

.. i18n: The different issues are handled in detail in the fourth part of this book :ref:`part-ops`, dedicated to internal
.. i18n: organization and to the management of a services business.

The different issues are handled in detail in the fourth part of this book :ref:`part-ops`, dedicated to internal
organization and to the management of a services business.

.. i18n: .. index::
.. i18n:    single: inventory control
.. i18n:    single: Stock Management
.. i18n: ..

.. index::
   single: inventory control
   single: Stock Management
..

.. i18n: Stock Management
.. i18n: ----------------

Stock Management
----------------

.. i18n: The various sub-menus under :menuselection:`Stock Management` together provide operations you need to manage stock.
.. i18n: You can:

The various sub-menus under :menuselection:`Stock Management` together provide operations you need to manage stock.
You can:

.. i18n: * define your warehouses and structure them around locations and layouts of your choosing,
.. i18n: 
.. i18n: * manage inventory rotation and stock levels,
.. i18n: 
.. i18n: * execute packing orders generated by the system,
.. i18n: 
.. i18n: * execute deliveries with delivery notes and calculate delivery charges,
.. i18n: 
.. i18n: * manage lots and serial numbers for traceability,
.. i18n: 
.. i18n: * calculate theoretical stock levels and automate stock valuation,
.. i18n: 
.. i18n: * create rules for automatic stock replenishment.

* define your warehouses and structure them around locations and layouts of your choosing,

* manage inventory rotation and stock levels,

* execute packing orders generated by the system,

* execute deliveries with delivery notes and calculate delivery charges,

* manage lots and serial numbers for traceability,

* calculate theoretical stock levels and automate stock valuation,

* create rules for automatic stock replenishment.

.. i18n: Packing orders and deliveries are usually defined automatically by calculating requirements based on
.. i18n: sales. Stores staff use picking lists generated by Open ERP, produced automatically in order of
.. i18n: priority.

Packing orders and deliveries are usually defined automatically by calculating requirements based on
sales. Stores staff use picking lists generated by Open ERP, produced automatically in order of
priority.

.. i18n: Stock management is, like accounting, double-entry. So stocks don't appear and vanish magically
.. i18n: within a warehouse, they just get moved from place to place. And, just like accounting, such a
.. i18n: double-entry system gives you big advantages when you come to audit stock because each missing item
.. i18n: has a counterpart somewhere.

Stock management is, like accounting, double-entry. So stocks don't appear and vanish magically
within a warehouse, they just get moved from place to place. And, just like accounting, such a
double-entry system gives you big advantages when you come to audit stock because each missing item
has a counterpart somewhere.

.. i18n: Most stock management software is limited to generating lists of products in warehouses. Because of
.. i18n: its double-entry system Open ERP automatically manages customer and suppliers stocks as well, which
.. i18n: has many advantages: complete traceability from supplier to customer, management of consigned stock,
.. i18n: and analysis of counterpart stock moves.

Most stock management software is limited to generating lists of products in warehouses. Because of
its double-entry system Open ERP automatically manages customer and suppliers stocks as well, which
has many advantages: complete traceability from supplier to customer, management of consigned stock,
and analysis of counterpart stock moves.

.. i18n: Furthermore, just like accounts, stock locations are hierarchical, so you can carry out analyses at
.. i18n: various levels of detail.

Furthermore, just like accounts, stock locations are hierarchical, so you can carry out analyses at
various levels of detail.

.. i18n: .. index::
.. i18n:    single: CRM
.. i18n:    single: Customer Relationship Management
.. i18n:    single: SRM
.. i18n:    single: Supplier Relationship Management
.. i18n: ..

.. index::
   single: CRM
   single: Customer Relationship Management
   single: SRM
   single: Supplier Relationship Management
..

.. i18n: Customer and Supplier Relationship Management
.. i18n: ---------------------------------------------

Customer and Supplier Relationship Management
---------------------------------------------

.. i18n: Open ERP provides many tools for managing relationships with partners. These are available through
.. i18n: the :menuselection:`CRM & SRM` menu.

Open ERP provides many tools for managing relationships with partners. These are available through
the :menuselection:`CRM & SRM` menu.

.. i18n: .. tip::  :guilabel:`CRM & SRM`
.. i18n: 
.. i18n: 	``CRM`` stands for Customer Relationship Management, a standard term for systems that manage client and
.. i18n: 	customer relations. ``SRM`` stands for Supplier Relationship Management, and is commonly used for
.. i18n: 	functions that manage your communications with your suppliers.

.. tip::  :guilabel:`CRM & SRM`

	``CRM`` stands for Customer Relationship Management, a standard term for systems that manage client and
	customer relations. ``SRM`` stands for Supplier Relationship Management, and is commonly used for
	functions that manage your communications with your suppliers.

.. i18n: The concept of a “case” is used to handle arbitrary different types of relationship, each
.. i18n: derived from a generic method. You can use it for all types of communication such as order
.. i18n: enquiries, quality problems, management of a call center, record tracking, support requests and job
.. i18n: offers.

The concept of a “case” is used to handle arbitrary different types of relationship, each
derived from a generic method. You can use it for all types of communication such as order
enquiries, quality problems, management of a call center, record tracking, support requests and job
offers.

.. i18n: Open ERP ensures that each case is handled effectively by the system's users, customers and
.. i18n: suppliers. It can automatically reassign a case, track it for the new owner, send reminders by email
.. i18n: and raise other Open ERP documentation and processes.

Open ERP ensures that each case is handled effectively by the system's users, customers and
suppliers. It can automatically reassign a case, track it for the new owner, send reminders by email
and raise other Open ERP documentation and processes.

.. i18n: All operations are archived, and an email gateway lets you update a case automatically from emails
.. i18n: sent and received. A system of rules enables you to set up actions that can automatically improve
.. i18n: your process quality by ensuring that open cases never escape attention.

All operations are archived, and an email gateway lets you update a case automatically from emails
sent and received. A system of rules enables you to set up actions that can automatically improve
your process quality by ensuring that open cases never escape attention.

.. i18n: As well as those functions, you've got tools to improve the productivity of all staff in their daily
.. i18n: work:

As well as those functions, you've got tools to improve the productivity of all staff in their daily
work:

.. i18n: * a document editor that interfaces with OpenOffice.org,
.. i18n: 
.. i18n: * interfaces to synchronize your contacts and Outlook Calendar with Open ERP,
.. i18n: 
.. i18n: * an Outlook plugin enabling you to automatically store your emails and their attachments in a
.. i18n:   Document Management System integrated with Open ERP,
.. i18n: 
.. i18n: * a portal for your suppliers and customers that enables them to access certain data on your system.

* a document editor that interfaces with OpenOffice.org,

* interfaces to synchronize your contacts and Outlook Calendar with Open ERP,

* an Outlook plugin enabling you to automatically store your emails and their attachments in a
  Document Management System integrated with Open ERP,

* a portal for your suppliers and customers that enables them to access certain data on your system.

.. i18n: You can implement a continuous improvement policy for all of your services, by using some of the
.. i18n: statistical tools in Open ERP to analyze the different communications with your partners. With
.. i18n: these, you can execute a real improvement policy to manage your service quality.

You can implement a continuous improvement policy for all of your services, by using some of the
statistical tools in Open ERP to analyze the different communications with your partners. With
these, you can execute a real improvement policy to manage your service quality.

.. i18n: The management of customer relationships is detailed in the second section of this book (see
.. i18n: :ref:`part2-crm`).

The management of customer relationships is detailed in the second section of this book (see
:ref:`part2-crm`).

.. i18n: .. index::
.. i18n:    single: Purchase Management

.. index::
   single: Purchase Management

.. i18n: Purchase Management
.. i18n: -------------------

Purchase Management
-------------------

.. i18n: Purchase management enables you to track your suppliers' price quotations and convert them into
.. i18n: Purchase Orders as you require. Open ERP has several methods of monitoring invoices and tracking
.. i18n: the receipt of ordered goods.

Purchase management enables you to track your suppliers' price quotations and convert them into
Purchase Orders as you require. Open ERP has several methods of monitoring invoices and tracking
the receipt of ordered goods.

.. i18n: You can handle partial deliveries in Open ERP, so you can keep track of items that are still to be
.. i18n: delivered on your orders, and you can issue reminders automatically.

You can handle partial deliveries in Open ERP, so you can keep track of items that are still to be
delivered on your orders, and you can issue reminders automatically.

.. i18n: Open ERP's replenishment management rules enable the system to generate draft purchase orders
.. i18n: automatically, or you can configure it to run a lean process driven entirely by current production
.. i18n: needs.

Open ERP's replenishment management rules enable the system to generate draft purchase orders
automatically, or you can configure it to run a lean process driven entirely by current production
needs.

.. i18n: Project Management
.. i18n: ------------------

Project Management
------------------

.. i18n: Open ERP's project management tools enable you to handle the definition of tasks and the
.. i18n: specification of requirements for those tasks, efficient allocation of resources to the
.. i18n: requirements, project planning, scheduling and automatic communication with partners.

Open ERP's project management tools enable you to handle the definition of tasks and the
specification of requirements for those tasks, efficient allocation of resources to the
requirements, project planning, scheduling and automatic communication with partners.

.. i18n: All projects are hierarchically structured. You can review all of the projects from the menu
.. i18n: :menuselection:`Project Management --> All Projects`. To view a project's plans, select a project
.. i18n: line and then click :guilabel:`Print`. Then select :guilabel:`Gantt diagram` to obtain a graphical
.. i18n: representation of the plan.

All projects are hierarchically structured. You can review all of the projects from the menu
:menuselection:`Project Management --> All Projects`. To view a project's plans, select a project
line and then click :guilabel:`Print`. Then select :guilabel:`Gantt diagram` to obtain a graphical
representation of the plan.

.. i18n: .. todo:: This isn't working. Gantt charts aren't displaying right.

.. todo:: This isn't working. Gantt charts aren't displaying right.

.. i18n: .. figure:: images/familiarization_project_gantt.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Project Planning*

.. figure:: images/familiarization_project_gantt.png
   :scale: 75
   :align: center

   *Project Planning*

.. i18n: You can run projects related to Services or Support, Production or Development – it's a universal
.. i18n: module for all enterprise needs.

You can run projects related to Services or Support, Production or Development – it's a universal
module for all enterprise needs.

.. i18n: Project Management is described in :ref:`ch-projects`.

Project Management is described in :ref:`ch-projects`.

.. i18n: .. index::
.. i18n:    single: Production Management
.. i18n:    single: Manufacturing

.. index::
   single: Production Management
   single: Manufacturing

.. i18n: Manufacturing
.. i18n: -------------

Manufacturing
-------------

.. i18n: Open ERP's production management capabilities enable companies to plan, automate, and track
.. i18n: manufacturing and product assembly. Open ERP supports multi-level bills of materials and lets you
.. i18n: substitute subassemblies dynamically, at the time of sales ordering. You can create virtual sub-
.. i18n: assemblies for reuse on several products with phantom bills of materials.

Open ERP's production management capabilities enable companies to plan, automate, and track
manufacturing and product assembly. Open ERP supports multi-level bills of materials and lets you
substitute subassemblies dynamically, at the time of sales ordering. You can create virtual sub-
assemblies for reuse on several products with phantom bills of materials.

.. i18n: .. index::
.. i18n:    single: bill of materials
.. i18n:    single: BoM

.. index::
   single: bill of materials
   single: BoM

.. i18n: .. note:: BoMs, routing, workcenters
.. i18n: 
.. i18n: 	These documents describe the materials that make up a larger assembly. They're commonly called
.. i18n: 	Bills of Materials or BoMs.
.. i18n: 
.. i18n: 	They're linked to routings which list the operations needed to carry out the manufacture or
.. i18n: 	assembly of the product.
.. i18n: 
.. i18n: 	Each operation is carried out at a workcenter, which can be a machine, a tool, or a person.

.. note:: BoMs, routing, workcenters

	These documents describe the materials that make up a larger assembly. They're commonly called
	Bills of Materials or BoMs.

	They're linked to routings which list the operations needed to carry out the manufacture or
	assembly of the product.

	Each operation is carried out at a workcenter, which can be a machine, a tool, or a person.

.. i18n: Production orders based on your company's requirements are scheduled automatically by the system,
.. i18n: but you can also run the schedulers manually whenever you want. Orders are worked out by calculating
.. i18n: the requirements from sales, through bills of materials, taking current inventory into account. The
.. i18n: production schedule is also generated from the various lead times defined throughout, using the same
.. i18n: route

Production orders based on your company's requirements are scheduled automatically by the system,
but you can also run the schedulers manually whenever you want. Orders are worked out by calculating
the requirements from sales, through bills of materials, taking current inventory into account. The
production schedule is also generated from the various lead times defined throughout, using the same
route

.. i18n: The demonstration data contains a list of products and raw materials with various classifications
.. i18n: and ranges. You can test the system using this data.

The demonstration data contains a list of products and raw materials with various classifications
and ranges. You can test the system using this data.

.. i18n: .. index::
.. i18n:    single: Sales Management

.. index::
   single: Sales Management

.. i18n: Sales Management
.. i18n: ----------------

Sales Management
----------------

.. i18n: The :menuselection:`Sales Management` menu gives you roughly the same functionality as the
.. i18n: :menuselection:`Purchase Management` menu – the ability to create new orders and to review the
.. i18n: existing orders in their various states – but there are important differences in the workflows.

The :menuselection:`Sales Management` menu gives you roughly the same functionality as the
:menuselection:`Purchase Management` menu – the ability to create new orders and to review the
existing orders in their various states – but there are important differences in the workflows.

.. i18n: Confirmation of an order triggers delivery of the goods, and invoicing timing is defined by a
.. i18n: setting in each individual order.

Confirmation of an order triggers delivery of the goods, and invoicing timing is defined by a
setting in each individual order.

.. i18n: Delivery charges can be managed using a grid of tariffs for different carriers.

Delivery charges can be managed using a grid of tariffs for different carriers.

.. i18n: Document Management
.. i18n: -------------------

Document Management
-------------------

.. i18n: Open ERP integrates a complete document management system that not only 
.. i18n: carried out the functions of a standard DMS, but also integrates with all
.. i18n: of its system-generated documents such as Invoices and Quotations. What's more
.. i18n: it keeps all of this synchronized.

Open ERP integrates a complete document management system that not only 
carried out the functions of a standard DMS, but also integrates with all
of its system-generated documents such as Invoices and Quotations. What's more
it keeps all of this synchronized.

.. i18n: Process Management
.. i18n: ------------------

Process Management
------------------

.. i18n: Many documents have a workflow of their own, and also take part in cross-functional processes.
.. i18n: Take a document that could be expected to have a workflow, such as a Sales Order, and
.. i18n: then click the :guilabel:`Process` button above its form to see the full process.

Many documents have a workflow of their own, and also take part in cross-functional processes.
Take a document that could be expected to have a workflow, such as a Sales Order, and
then click the :guilabel:`Process` button above its form to see the full process.

.. i18n: .. figure:: images/guided_tour_process.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Process for a Sales Order*
.. i18n:    
.. i18n: You can see the position of that particular document in its process, if you have selected
.. i18n: a single document, by the solid bar on one of the process nodes. You also link
.. i18n: to documents and menus for each of the stages.

.. figure:: images/guided_tour_process.png
   :scale: 75
   :align: center

   *Process for a Sales Order*
   
You can see the position of that particular document in its process, if you have selected
a single document, by the solid bar on one of the process nodes. You also link
to documents and menus for each of the stages.

.. i18n: There is a clear distinction between a cross-functional process (that is currently only
.. i18n: shown in the web client) and the detailed document workflow (that is shown in both the
.. i18n: web client from a process node, and the GTK client from the 
.. i18n: :menuselection:`Plugins > Execute a Plugin...` menu and clicking either 
.. i18n: the :guilabel:`Print Workflow` or the the :guilabel:`Print Workflow (Complex)` option.

There is a clear distinction between a cross-functional process (that is currently only
shown in the web client) and the detailed document workflow (that is shown in both the
web client from a process node, and the GTK client from the 
:menuselection:`Plugins > Execute a Plugin...` menu and clicking either 
the :guilabel:`Print Workflow` or the the :guilabel:`Print Workflow (Complex)` option.

.. i18n: .. figure:: images/purchase_workflow.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Workflow for a Purchase Order*

.. figure:: images/purchase_workflow.png
   :scale: 75
   :align: center

   *Workflow for a Purchase Order*

.. i18n: Alongside the document management system, the process visualization features make Open ERP
.. i18n: far better for documentation than similar systems.

Alongside the document management system, the process visualization features make Open ERP
far better for documentation than similar systems.

.. i18n: Other functions
.. i18n: ---------------

Other functions
---------------

.. i18n: You've been through a brisk, brief overview of many of the main functional areas of Open ERP. 
.. i18n: Some of these – a large proportion of the core modules – are treated in more detail 
.. i18n: in the following chapters.

You've been through a brisk, brief overview of many of the main functional areas of Open ERP. 
Some of these – a large proportion of the core modules – are treated in more detail 
in the following chapters.

.. i18n: You can use the menu :menuselection:`Administration --> Modules Management --> Modules --> 
.. i18n: Uninstalled modules` to find the remaining modules that have been loaded into your installation but
.. i18n: not yet installed in your database. Some modules have only minor side-effects to Open ERP (such as
.. i18n: :mod:`base_iban`), some have quite extensive effects (such as the various charts of accounts), and
.. i18n: some make fundamental additions (such as :mod:`multi_company`).

You can use the menu :menuselection:`Administration --> Modules Management --> Modules --> 
Uninstalled modules` to find the remaining modules that have been loaded into your installation but
not yet installed in your database. Some modules have only minor side-effects to Open ERP (such as
:mod:`base_iban`), some have quite extensive effects (such as the various charts of accounts), and
some make fundamental additions (such as :mod:`multi_company`).

.. i18n: But there are now more than three hundred modules available. If you've connected to the Internet,
.. i18n: and if your \ ``addons``\   directory is writable as described at the beginning of this chapter, you
.. i18n: can download new modules using the menu :menuselection:`Administration --> Modules Management -->
.. i18n: Update Modules List`.

But there are now more than three hundred modules available. If you've connected to the Internet,
and if your \ ``addons``\   directory is writable as described at the beginning of this chapter, you
can download new modules using the menu :menuselection:`Administration --> Modules Management -->
Update Modules List`.

.. i18n: A brief description is available for each module, but the most thorough way of understanding their
.. i18n: functionality is to install one and try it. So, pausing only to prepare another test database to try
.. i18n: it out on, just download and install the modules that appear interesting.

A brief description is available for each module, but the most thorough way of understanding their
functionality is to install one and try it. So, pausing only to prepare another test database to try
it out on, just download and install the modules that appear interesting.

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
