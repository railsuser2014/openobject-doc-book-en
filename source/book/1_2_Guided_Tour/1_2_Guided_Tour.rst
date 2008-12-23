

Guided Tour
#############

Summary

* The user interface 

* Installing functional modules

* Familiarization with the system using the demonstration data

Keywords

* modules

* functions

* configuration

* familiarization

* interface

* business process

 *Starting to discover Open ERP, using demonstration data supplied with the system to familiarize yourself with the user interface. This guided tour provides you with an introduction to many of the available system features.* 

You'd be forgiven a flicker of apprehension when you first sit at your computer to connect to Open ERP, since ERP systems are renowned for their complexity and for the time it takes to learn how to use them. These are, after all, Enterprise Resource Planning systems, capable of managing most elements of global enterprises, so they should be complicated, shouldn't they? But even if this is often the case for proprietary software, Open ERP is a bit of an exception in the class of management software.

Despite its comprehensiveness, Open ERP's interface and workflow management facilities are quite simple and intuitive to use. For this reason Open ERP is one of the few software packages with reference customers in both very small businesses (typically requiring simplicity) and large accounts (typically requiring wide functional coverage).

A two-phase approach provides a good guide for your first steps with Open ERP:

	#. Using a database containing demonstration data to get an overview of Open ERP's functionality (described in this chapter),

	#. Setting up a clean database to configure and populate a limited system for yourself (described in the next chapter).

To read this chapter effectively, make sure that you have access to an Open ERP server. The description in this chapter assumes that you're using the Open ERP web client unless it states otherwise. The general functionality differs little from one client to the other.

Database creation
===================

Use the technique outlined in Chapter 1 to create a new database, \ ``openerp_ch02``\  . This database will contain the demonstration data provided with Open ERP and a large proportion of the core Open ERP functionality. You'll need to know your super administrator password for this – or you'll have to find somebody who does have it to create this seed database.

Start the database creation process from the  *Database Administration*  page by clicking  *Create*  and then completing the following fields on the  *Create Database*  form:

*  *Super administrator password* , by default it's \ ``admin``\  , if you or your system administrator haven't changed it.

*  *New database name* : \ ``openerp_ch02``\  .

*  *Load Demonstration Data*  checkbox: \ ``checked``\  .

*  *Default Language* : \ ``English``\  .

To connect to Open ERP
=======================

Connect to the new \ ``openerp_ch02``\   database as user \ ``admin``\   with its default password \ ``admin``\   (you might have to wait a couple of seconds before the system will allow you to connect if you've only just created it). Since this is the first time you've connected to it you'll have to go through the Setup wizard in steps:

	#.  *Select a profile*  select  *Profile* \ ``Minimal Profile``\   since you'll be adding more modules in just a moment.

	#.  *Define Main Company* and  *Report Header*  change anything you like on this page to match your own situation. Only the  *Company Name* and  *Currency* are required but you should aim to put something relevant in all fields. If you alter the currency you'll need to click the  *Search / Open a resource* icon to the right of the field to register the name of the currency you type in.

	#.  *Summary*  just click the  *Install* button.

	#.  *Installation done*  click  *Ok* 

Now you're signed in as an administrator you'll be able to add functionality and modify database settings.

.. tip::   **Comment**  *Dashboard after connection* 

	If you'd installed any of the other profiles from the installation wizard you'd find that your login screen shows a dashboard with information related to your user account rather than the main menu.

	When that happens the main menu is still available, as you'll see later in this chapter. If you're using the web client you can reach the main menu by clicking the Main Menu link towards the top left of the window. If you're using the GTK client the main menu is in the first tab (which is hidden – it's the second tab containing the dashboard that's initially showing). 

Once you're displaying the main menu you're able to see the following screen items:

* the Preferences toolbar to the top right, showing the user name, links to the Home page, Preferences, About and Logout,

* just below you'll find information about the Request system,

* links to the Main Menu and the Shortcuts,

* information about copyright at the bottom of the page,

* the main contents of the window flanked by the menu toolbar to the left and some links up and to the right.


	.. image:: images/main_window_openerp_ch02.png
	   :align: center

*The Main Menu of the openerp_ch02 database*


Three menus are available on the left:

* Partners,

* Financial Management,

* Administration.

Preferences toolbar
---------------------

When you're connected to Open ERP the Preferences toolbar indicates which user you're connected as. So it should currently be showing  *Welcome Administrator*  (unless you logged in as another user and it's reflecting the name of that user instead).

You'll find a link to the  *Home*  page to its right. This takes you to either the dashboard or the available menus, depending on the user configuration. In the case of the \ ``openerp_ch02``\   database so far the Home page is the Main Menu. But in general each user of the system is presented with a dashboard that's designed to show performance indicators and urgent documents that are most useful to someone of the user's position in the company. You'll see how to assign dashboards to different users in Chapter 13.

.. tip::   **Note**  *Multi-nationals and time zones* 

	If you have users in different countries, they can configure their own timezone. Timestamp displays are then adjusted by reference to the user's own localization setting.

	So if you have a team in India and a team in England, the times will automatically be converted. If an Indian employee sets her working hours from 9 to 6 that will be converted and saved in the server's timezone. When the English users want to set up a meeting with an Indian user, the Indian user's available time will be converted to English time.

The next element in the Toolbar is a link to  *Preferences* . By clicking that link you reach a page where the current user can set a timezone and a working language:

* The  *Language*  field enables the user's working language to be changed. But first the system must be loaded with other languages for the user to be able to choose an alternative, which is described in the next subsection of this chapter.

* The  *Timezone*  setting indicates the user's location to Open ERP. This can be different from that of the server. All of the dates in the system are converted to the user's timezone automatically.

The  *About*  link gives information about the development of the Open ERP software.

The  *Logout*  link enables you to logout and return to the original login page. You can then login to another database, or to the same database as another user. This page also gives you access to the super-administrator functions for managing databases on this server.

The  *Requests*  link sits just below this toolbar. It is only visible if you're logged into a database. If your database is new it will say \ ``No request``\  . You can click on that link to look at requests that have been sent to you at any time.

Installing a new language
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Each user of the system can work in his or her own language. More than twenty languages are currently available besides English. Users select their working language using the Preferences link. You can also assign a language to a partner (customer or supplier), in which case all the documents sent to that partner will be automatically translated into that language.

.. tip::   **Key to reading**  *More information about languages* 

	The base version of Open ERP is translated into the following languages: English, German, Chinese, Spanish, Italian, Hungarian, Dutch, Portuguese, Romanian, Swedish and Czech.

	But other languages are also available in the Forge (http://tinyforge.org): Arabic, Afghan, Austrian, Bulgarian, Indonesian, Finnish, Thai, Turkish and Vietnamese..

As administrator you can install a new main working language into the system.

	#. Select  *Administration* in the Menu Toolbar and click  *Translations > Load New Language * n the main menu window.

	#. Select the language to install, \ ``French``\  for example, and click on  *Start Installation* 

	#. When the message  *Installation finished* appears, click  *OK* to return to the menu.

To see the effects of this installation change the preferences of your user to change the working language. The main menu is immediately translated in the selected language. If you're using the GTK client you'll first have to close the menu then open a new main menu to start seeing things in the new language.

.. tip::   **More information**  *Navigating the menu* 

	From this point in the book navigation from the main menu is written as a series of menu entries connected by the > character. Instead of seeing “Select Administration in the Menu toolbar then click Translations > Load New Language” you'll simply get “use menu Administration > Translations > Load New Language”.

Requests as a mechanism for internal communication
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Requests are a powerful communication mechanism between users of the system. They're also used by Open ERP itself to send system messages to users. 

They have distinct advantages over traditional emails:

* requests are linked to other Open ERP documents,

* an event's history is attached to the request,

* you can monitor events effectively from the messages they've sent.

Open ERP uses this mechanism to inform users about certain system events. For example if there's a problem concerning the restocking of a product a request is sent by Open ERP to the production manager.

Send a request to get an understanding of its functionality:

	#. Click on the  *Requests* link that should currently be showing  *No Requests*  This opens a window that lists all of your waiting requests.

	#. Click  *New* to create and send a new request.

	#. Complete the subject of the request, such as \ ``How are you?``\  then give a description of the enquiry in the field.

	#. Click the  *Search* button to the right of the  *Send to* field and select  *Administrator* in the window that opens (that's the user that you're already connected as).

	#. You can then link this request to other system documents using the  *References* field, which could, for example, be a partner or a quotation or a disputed invoice.

	#. Click  *Send* to send the request to the intended recipient – that's yourself in this case. Then click  *Main Menu* to return to the original screen.


	.. image:: images/request_tab.png
	   :align: center

*Creating a new request*

To check your requests:

	#. Click on the link to the right of the  *Requests* label to open a list of your requests. (It's possible that you'll still see the statement  *No Requests* because this information is updated periodically ather than instantly.) The list of requests then opens and you can see the requests you've been sent there.

	#. Click the  *Edit* icon, represented by a pencil, at the right hand end of the request line. That opens the request in edit mode.

	#. You can then click the  *Reply* button and make your response in the  *Request* field that appears in place of the original message.

	#. Click  *Send* to save your response and send it to the original sender.

.. tip::   **Advantage**  *Requests vs. email* 

	The advantage of an Open ERP request compared with a set of emails about one thread of discussion is that a request contains all of the conversation in one place. You can easily monitor a whole discussion with the appropriate documents attached, and quickly review a list of incomplete discussions with the history within each request.

Look at the request and its history, then close it.

	#. Click on the  *History* tab in the  *Request* form to see the original request and all of the responses. By clicking on each line you could get more information on each element.

	#. Return to the first tab,  *Request* and click End of * Request * o set it to \ ``closed``\   This then appears greyed out.

The request is no longer active. It's not visible to searches and won't appear in your list of waiting requests.

.. tip::   **Note**  *Trigger dates* 

	You can send a request with a future date. This request won't appear in the recipient's waiting list until the indicated date. This mechanism is very useful for setting up alerts before an important event. 

Configuring Users
-------------------

The database you created contains minimal functionality but can be extended to include all of the potential functionality available to Open ERP. About the only functions actually available in this minimal database are Partners and Currencies – and these only because the definition of your main company required this. And because you chose to include demonstration data, both Partners and Currencies were installed with some samples.

Because you logged in as Administrator, you have all the access you need to configure users. Click  *Administration > Users > Users*  to display the list of users defined in the system. A second user, \ ``Demo User``\  , is also present in the system as part of the demonstration data. Click the \ ``Demo User``\   name to open a non-editable form on that user.

Click the  *Security*  tab to see that the demo user is a member of no groups, has no roles and is subject to no specialized rules. The \ ``admin``\   user is different, as you can see if you follow the same sequence to review the its definition. It's a member of the \ ``admin``\   group, which gives it more advanced rights to configure new users.

.. tip::   **Definition**  *Roles, Groups and Users* 

	Users and groups provide the structure for specifying access right to different documents. Their setup answers the question “who has access to what?”

	Roles are used in business processes for permitting or blocking certain steps in the workflow of a given document. For example you can assign the role of approving an invoice. Roles answer the question “Who should do what?”

Click  *Administration > Users > Groups*  below the main menu to open the list of groups defined in the system. If you open the form view of the \ ``admin``\   group by clicking its name in the list, the first tab give you the list of all the users who belong to this group.

Click the Security tab and it gives you details of the access rights for that group. These are detailed in Chapter 13, but you can already see there further up in the window, the list of menus reserved for the admin group. By convention, the \ ``admin``\   in Open ERP has rights of access to the  *Configuration*  menu in each section. So \ ``Partners / Configuration``\   is found in the list of access rights but \ ``Partners``\   isn't found there because it's accessible to all users.

You can create some new users to integrate them into the system. Assign them to predefined groups to grant them certain access rights. Then try their access rights when you login as these users. Management defines these access rights as described in Chapter 13.

.. tip::   *Note* 

	This is an area where future versions of Open ERP are changing: many groups are being predefined and access to many of the menus and objects will be keyed to these groups by default. This is quite a contrast to the rather liberal approach in 4.2.2 and before, where access rights could be defined but were not activated by default.

Managing partners
-------------------

In Open ERP, a partner represents an entity that you do business with. That can be a prospect, a customer, a supplier, or even an employee of your company.

List of partners
^^^^^^^^^^^^^^^^^

Click  *Partners > Partners*  in the main menu to open the list of partners. Then click the name of the first partner to get hold of the details – a form appears with several tabs on it:

* the  *General*  tab contains the main information about the company, such as its corporate name, its primary language, your different contacts at that partner and the categories it belongs to.

* the  *Extra Info*  tab contains information that's slightly less immediate.

* the  *Event History*  tab contains the history of all the events that the partner has been involved in. These events are created automatically by different system documents: invoices, orders, support requests and so on. These give you a rapid view of the partner's history on a single screen.

* the  *Properties*  tab contains partner settings related to accounting, inventory and other areas: you can leave this alone for the moment.


	.. image:: images/partner.png
	   :align: center
	   :scale: 80

*Partner form*



.. tip::   **Definition**  *Partner Categories* 

	Partner Categories enable you to segment different partners according to their relation with you (client, prospect, supplier, and so on). A partner can belong to several categories – for example it may be both a customer and supplier at the same time.

Partner Categories
^^^^^^^^^^^^^^^^^^^

You can list your partners by category using the menu  *Partners > Partners by category* . This opens a hierarchical structure of categories where each category can be divided into sub-categories. Click a category to obtain a list of partners in that category. For example, click all of the partners in the category  *Supplier*  or  *Supplier > Components Supplier* . You'll see that if a company is in a subcategory (such as  *Components Supplier* ) then it will also show up when you click the parent category (such as  *Supplier* ). 


	.. image:: images/main_window_partner_menu_config.png
	:align: center

*Categories of partner in a hierarchical structure*  : *Customer,Prospect,Supplier...*


The administrator can define new categories. So you'll create a new category and link it to a partner:

	#. Use  *Partners > Configuration > Categories > Edit Category* to reach a list of the same categories as above but in a list view rather than a hierarchical tree structure.

	#. Click  *New* to open an empty form for creating a new category

	#. Enter \ ``My Prospects``\  in the field  *Name of Category*  Then click on the  *Search* icon to the right of the  *Parent Category* field and select \ ``Prospect``\  in the list that appears.

	#. Then save your new category using the Save button.

.. tip::   **Attention**  *Required Fields* 

	Fields colored blue are required. If you try to save the form while any of these fields are empty the field turns red to indicate that there's a problem. It's impossible to save the form until you've completed every required field.

You can review your new category structure using  *Partners > Partners by category* . You should see the new structure of \ ``Prospects / My Prospects``\   there.


	.. image:: images/main_window_partner_tab.png
	   :align: center

*Creating a new partner category : My prospects*


To create a new partner and link it to this new category open a new partner form to modify it.

	#. In the  *General* tab, type \ ``New Partner``\  into the  *Name* field.

	#. Then click on the search icon to the right of the  *Categories* field and select your new category from the list that appears: \ ``Prospect / My Prospects``\  

	#. Then save your partner by clicking  *Save*  The partner now belongs in the category \ ``Prospect / My prospects.``\  

	#. Monitor your modification in the menu  *Partners > Partners by category*  Select the category \ ``My Prospect``\   The list of partners opens and you'll find your new partner there in that list.

.. tip::   **Note**  *Searching for documents* 

	If you need to search through a long list of partners it's best to use the available search criteria rather than scroll through the whole partner list. It's a habit that'll save you a lot of time in the long run as you search for all kinds of documents.


---------------------


	.. note::  *Example Categories of partners* 

			A partner can be assigned to several categories. These enable you to create alternative classifications as necessary, usually in a hierarchical form.

			Here are some structures that are often used:

			* geographical locations,

			* interest in certain product lines,

			* subscriptions to newsletters,

			* type of industry.

Installing new functionality
=============================

All of Open ERP's functionality is contained in its many and various modules. Many of these, the core modules, are automatically loaded during the initial installation of the system and can be updated online later. Although they're mostly not installed in your database at the outset, they're available on your computer for immediate installation. Additional modules can also be loaded online from the official Open ERP site . These modules are inactive when they're loaded into the system, and can then be installed in a separate step. 

You'll start by checking if there are any updates available online that apply to your initial installation. Then you'll install a CRM module to complete your existing database.

Updating the Modules list
---------------------------

Click  *Administration > Modules Management > Update Modules List*  to start the updating tool. The  *Scan for new modules*  window opens showing the addresses that Open ERP will look in for downloading new modules (known as the repositories), and updating existing ones.

.. tip::   **Note**  *Remote module repositories* 

	If the repository list doesn't reflect your needs then you can edit it from Administration > Modules Management > Repositories. There you can link to new repositories by adding their URLs and disable listed ones by unchecking their Active checkbox. If you're not connected to the Internet then you probably want to disable anything there. 

	Your Open ERP installation must be configured with its addons directory as writable for you to be able to download anything at all. If it hasn't been, then you may need the assistance of a systems administrator to change your server's settings so that you can install new modules.

Click  *Check New Modules*  to start the download from the specified locations. When it's complete you'll see a  *New Modules * window indicating how many new modules were downloaded and how many existing modules were updated. Click  *OK*  to return to the updated list. 

It won't matter in this chapter if you can't download anything, but some of the later chapters refer to modules that aren't part of the core installation and have to be obtained from a remote repository.

.. tip::   **Technique**  *Modules* 

	All the modules available on your computer can be found in the addons directory of your Open ERP server. Each module there is represented by a directory carrying the name of the module or by a file with the module name and .zip appended to it. The file is in ZIP archive format and replicates the directory structure of unzipped modules.

.. tip::   **Attention**  *Searching through the whole list* 

	The list of modules shows only the first available modules. In the web client you can search or follow the First / Previous / Next / Last links to get to any point in the whole list, and you can change the number of entries listed by clicking the row number indicators between Previous and Next and selecting a different number from the default of 20.

	If you use the GTK client you can search, as you would with the web client, or use the + icon to the top left of the window to change the number of entries returned by the search from its default limit of 80, or its default offset of 0 (starting at the first entry) in the whole list.

Installing a module
---------------------

You'll now install a module named \ ``product``\  , which will enable you to manage the company's products. This is part of the core installation, so you don't need to load anything to make this work, but isn't installed in the Minimal Profile. 

Open the list of uninstalled modules from  *Administration > Modules Management > Uninstalled Modules* . Search for the module by entering the name \ ``product``\   in the search screen then clicking it in the list that appears below it to open it. The form that describes the module gives you useful information such as its version number, its status and a review of its functionality. Click  *Install*  and the status of the module changes to \ ``To be installed``\  .


	.. image:: images/install_product_module.png
	   :align: center

*Installation of the product module*
      


.. tip::   **Technique**  *Technical Guide* 

	If you select a module in any of the module lists by clicking on a module line and then on Technical Guide at the top right of the window, Open ERP produces a technical report on that module. It's helpful only if the module is installed, so the menu Administration > Modules Management > Installed Modules produces the most fruitful list. 

	This report comprises a list of all the objects and all the fields along with their descriptions. The report adapts to your system and reflects any modifications you've made and all the other modules you've installed. 

Click  *Apply Upgrades*  then  *Start Upgrades*  on the  *System Upgrade*  form that appears. Close the window when the operation has completed. Return to the main menu you'll see the new menu  *Products*  has become available.

.. tip::   **GTK client**  *Refreshing the menu* 

	After an update in the GTK client you'll have to open a new menu to refresh the content – otherwise you won't see the new menu item. To do that use the window menu Form > Refresh/Cancel.

Installing a module with its dependencies
-------------------------------------------

You'll now install the CRM module (Customer Relationship Management) using the same process as before.

	#. Use  *Administration > Modules Management > Uninstalled Modules* to get a list of modules to install. Search for the \ ``crm``\  module in that list.

	#. Install the module by clicking  *Install* and then  *Apply Upgrades* on the resulting module form, followed by  *Start Upgrade* on the toolbar to the right.

	#. When the update screen appears, Open ERP gives you the list of modules that it will install and update. You'll find two modules there – \ ``crm``\  (which you selected) and \ ``account``\   What's happened is that the \ ``crm``\  module lists the \ ``account``\  module as a dependency, and \ ``account``\  is not yet installed. So Open ERP automatically installs \ ``account``\  

	#. Start the upgrade to install both modules.

When you return to the main menu you'll find the new customer relationship management menu  *CRM & SRM* . You'll also see all the accounting functions that are now available in the  *Financial Management * menu.

There is no particular relationship between the modules installed and the menus added. Most of the core modules add complete menus but some also add submenus to menus already in the system. Other modules add menus and submenus as they need. Modules can also add additional fields to existing forms, or simply additional demonstration data or some settings specific to a given requirement.

.. tip::   **Technique**  *Dependencies between modules* 

	The module form shows two tabs. The first tab gives basic information about the module and the second gives a list of modules that this module depends on. So when you install a module, Open ERP automatically selects all the necessary dependencies to install this module.

	That's also how you develop the profile modules: they simply define a list of modules that you want in your profile as a set of dependencies.

Although you can install a module and all its dependencies at once, you can't remove them in one fell swoop – you'd have to uninstall module by module. Uninstalling is more complex than installing because you have to handle existing system data. 

.. tip::   **Attention**  *Uninstalling modules* 

	Although it works quite well, uninstalling modules isn't perfect in Open ERP. It's not guaranteed to return the system exactly to the state it was in before installation.

	So it's recommended that you make a backup of the database before installing your new modules so that you can test the new modules and decide whether they're suitable or not. If they're not then you can return to your backup. If they are, then you'll probably still reinstall the modules on your backup so that you don't have to delete all your test data.

	If you wanted to uninstall you would use the menu Administration > Modules Management > Installed Modules and then uninstall them in the inverse order of their dependencies: crm, account, product.

Installing additional functionality
-------------------------------------

To discover the full range of Open ERP's possibilities you can install many additional modules. Installing them with their demonstration data provides a convenient way of exploring the whole core system. When you build on the \ ``openerp_ch02``\   database you'll automatically include demonstration data because you checked the  *Load Demonstration Data*  checkbox when you originally created the database.

So click  *Administration > Modules Management > Update Modules List*  to upload and update to the latest versions of everything on the Open ERP site. If you don't have an internet connection, or if you're not permitted to modify your installation's \ ``addons``\   directory you can skip this step.

.. tip::   **Attention**  *Importing new modules* 

	You can only import new modules and update your existing ones if your system is configured to accept them. Your Open ERP addons directory must be writable by the system user that's running your Open ERP application for this, as described in the final section of Chapter 1.

Click  *Administration > Modules Management > Uninstalled modules*  to give you an overview of all of the modules available for installation.

To test several modules you won't have to install them all one by one. You can use the dependencies between modules to load several at once. For example, try loading the following modules:

* \ ``profile_accounting``\  ,

* \ ``profile_manufacturing``\  ,

* \ ``profile_service``\  .

To find these quickly, enter the word \ ``profile``\   in the  *Name*  field of the search form and click  *Filter*  to search for the relevant modules. Then install them one by one or all at once.

As you update you'll see thirty or so modules to be installed. When you close the  *System Upgrade Done*  form you'll be returned to a dashboard, not the main menu you had before. To get to the main menu, use the  *Main Menu*  link.

Guided Tour of Open ERP
=========================

You'll now explore the database \ ``openerp_ch02``\   with these profile modules installed to give you an insight into the coverage of the core Open ERP software.

.. tip::   **Attention**  *Translating new modules* 

	When you've installed a new module and are using additional languages to English you have to reload the translation file. New terms introduced in these modules aren't translated by default. To do this use Administration > Translation > Load a New Language.

Depending on the user you're connected as the page appears differently from the Main Menu that showed before. Using the installation sequence above, in version 4.2.2, the Project Dashboard for a project member is assigned as the Administrator's home page. It shows a summary of the information required to start the day effectively. The dashboard contains:

* a list of the next tasks to carry out,

* a list of the next deadlines,

* public notes about projects,

* a planning chart of hours required,

* the timesheet.

Each of the lists can be reordered by clicking on the heading of a column – first in ascending then in descending order as you click repeatedly. To get more information about any particular entry click on the name in the first column, or if you want to show a particular panel click  *Zoom*  above it. 


	.. image:: images/admin_project_dashboard.png
	   :scale: 95

*Project Dashboard*


Users' home pages are automatically reassigned during the creation or upgrading of a database. It's usual to assign a dashboard to someone's home page but any Open ERP screen can be assigned to the home page of any user.

.. tip::   **Note**  *Creating shortcuts* 

	Each user has access to many menu items throughout all of the available menu hierarchy. But in general an employee uses only a small part of the system's functions.

	So you can define shortcuts for the most-used menus. These shortcuts are personal for each user. To create a new shortcut open the select menu and click on the Add link to the right of shortcuts.

	To change or replace a link click on the Shortcuts link. Open ERP then opens a list of editable shortcuts.

The following sections present an overview of the main functions of Open ERP. Some areas are covered in more detail in the following chapters of this book and you'll find many other functions available in the optional modules. Functions are presented in the order that they appear on the main menu.

Partners
---------

To familiarize yourself with Open ERP's interface, you'll start work with information about partners. Clicking  *Partners > Partners*  brings up a list of partners that were automatically loaded when you created the database with  *Load Demonstration Data*  checked.

Search for a partner
^^^^^^^^^^^^^^^^^^^^^

Above the partner list you'll see a search form that enables you to quickly filter the partners. Two tabs are available for searching –  *Basic Search*  and  *Advanced Search* . The latter simply shows more fields to narrow your selection.

If you've applied no filter, the list shows every partner in the system. For space reasons this list shows only the first few partners (the web client defaults to \ ``20``\  , but you can select a maximum of \ ``100``\   on a page). If you want to display other records you can search for them or navigate through the whole list using the  *First*  /  *Previous*  /  *Next*  /  *Last*  arrows.


	.. image:: images/partner_search_tab.png
	   :align: center

*Standard partner search*


.. tip::   **GTK client**  *List limit of 80* 

	By default the list in the GTK client shows only the first 80 records, to avoid overloading the network and the server.

	But you can change that limit by clicking the + icon to the left of the search criteria, and you can change the offset so that it starts further down the whole list than the first entry. 

If you click on the name of a partner the form view corresponding to that partner opens in Read-Only mode. In the list you could alternatively click the pencil icon to open the same form in Edit mode. Once you have a form you can toggle between the two modes by clicking  *Save*  or  *Cancel*  when in Edit mode and  *Edit*  when in Read-Only mode.

When you're in Read-Only mode you can navigate through the whole list you selected, as though you were in the List view. In Read-Only mode you can also click  *Search*  to see the form in List view again.

Partner form
^^^^^^^^^^^^^

The partner form contains several tabs, all referring to the current record:

*  *General* ,

*  *Extra Info* ,

*  *Event History* ,

*  *Properties* .

The fields in a tab aren't all of the same type – some (such as  *Name* ) contain free text, some (such as the  *Language* ) enable you to select a value from a list of options, others give you a view of another object (such as  *Partner Contacts*  – because a partner can have several contacts) or a list of link to another object (such as  *Categories* ). There are checkboxes (such as the  *Active*  field in the  *Extra Info*  tab), numeric fields (such as  *Credit Limit* ) and date fields (such as  *Date* ).

The  *Events History*  tab gives a quick overview of things that have happened to the partner – an overview of useful information such as orders, open invoices and support requests. Events are generated automatically by Open ERP from changes in other documents that refer to this partner.

It's possible to add events manually, such as a note recording a phone call. To add a new event click  *Create new record*  to the right of the  *Partner Events*  field. That opens a new  *Partner Events*  dialog box enabling an event to be created and added to the current partner.

Actions possible on a partner
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To the right of the partner form is a toolbar containing a list of possible  *Reports* ,  *Actions* , and quick  *Links*  about the partner displayed in the form.

You can generate PDF documents about the selected object (or, in list view, about one or more selected objects) using the following buttons in the  *Reports*  section of the toolbar:

*  *Labels* : print address labels for the selected partners,

*  *Overdue payments* : generate followup letters for overdue payments from partners. Each letter is printed in the language of the partner or, by default, in English.

Certain actions can be started by the following buttons in the  *Actions*  section of the toolbar:

*  *Company Architecture* : opens a window showing the partners and their children in a hierarchical structure.

*  *Send SMS* : enables you to send an SMS to selected partners. This system uses the bulk SMS facilities of the Clickatell® company .

*  *Mass Mailing* : enables you to send an email to a selection of partners.

.. tip::   **GTK client**  *Reports, Actions and Links* 

	When you're viewing a form in the GTK client, the buttons to the right of the form are shortcuts to the same Reports, Actions and Links as described in the text. When you're viewing a list (such as the partner list) those buttons aren't available to you. Instead, you can reach Reports and Actions through two of the buttons in the toolbar at the top of the list – Print and Action. 

Partners are used throughout the Open ERP system in other documents. For example, the menu  *Sales Management > Sales Orders > All Sales Orders*  brings up all the Sales Orders in list view. Click the name of a partner rather than the order number on one of those lines and you'll get the Partner form rather than the Sales Order form.

.. tip::   **Note**  *Right click and shortcuts* 

	In the GTK client you don't get hyperlinks to other document types. Instead, you can right-click in a list view to show the linked fields (that is fields having a link to other forms) on that line. 

	In the web client you'll see hyperlink shortcuts on several of the fields on a form that's in Read-Only mode, so that you can move onto the form for those entries. When the web form is in Edit mode, you can instead hold down the control button on the keyboard and right-click with the mouse button in the field, to get all of the linked fields in a pop-up menu just as you would with the GTK client.

	You can quickly try this out by going to any one of the sales orders in Sales Management > Sales Order > All Sales Orders and seeing what you can reach from the partner field on that sales order form using either the web client with the form in both read-only and in edit mode, or with the GTK client.


---------
	
	.. image:: images/familiarization_sale_partner.png
	   :align: center
	   
*Links for a partner appear in an order form*


Before moving on to the next module, take a quick look into the  *Partners > Configuration*  menu, particularly  *Categories*  and  *Localisation* . They contain some of the demonstration data that you installed when you created the database.

Accounting and finance
-----------------------

Chapters 6 to 9 in this book are dedicated to general and analytic accounting. A brief overview of the functions provided by these modules is given here as an introduction.

Accounting is totally integrated into all of the company's functions, whether it's general, analytic, budgetary or auxiliary accounting. Open ERP's accounting function is double-entry and supports multiple company divisions and multiple companies, as well as multiple currencies and languages.

Accounting that's integrated throughout all of the company's processes greatly simplifies the work of inputting accounting data, because most of the entries are generated automatically while other documents are being processed. You can avoid entering data twice in Open ERP, which is commonly a source of errors and delays.

So Open ERP's accounting isn't just for financial reporting – it's also the anchor point for many of a company's management processes. For example if one of your accountants puts a customer on credit hold then that will immediately block any other action related to that company's credit (such as a sale or a delivery).

Open ERP also provides integrated analytical accounting, which enables management by business activity or project and provides very detailed levels of analysis. You can control your operations based on business management needs, rather than on the charts of accounts that generally meet only statutory requirements.

Dashboards
-----------

Dashboards give you an overview of all the information that's important to you on a single page. The  *Dashboards*  menu gives you access to predefined boards for  *Accounting* ,  *Production*  and  *Project Management* .

.. tip::   **Definition**  *Dashboards* 

	Unlike most other ERP systems and classic statistically-based systems, Open ERP lets dashboards be provided to all of the system's users, and not just to directors and accountants.

	Users can each have their own dashboard, adapted to their needs, to enable them to manage their own work effectively. For example a developer using the Project Dashboard can see such information as a list of the next tasks, task completion history and an analysis of the state of progress of the relevant projects.

Dashboards are dynamic, which enables you to easily navigate around the whole information base. Using the icons above a graph, for example, you can filter the data or zoom into the graph. You can click on any element of the list to get detailed statistics on the selected element.

Dashboards are adaptable to the needs of each user and each company.

.. tip::   **Note**  *Construction of dashboards* 

	Version 4.3 of Open ERP contains a dashboard editor. It enables you to construct your own dashboard to fit your specific needs using only a few clicks.

Products
---------

In Open ERP, product means a raw material, a stockable product, a consumable or a service. You can work with whole products or with templates that separate the definition of products and variants.

For example if you sell t-shirts in different sizes and colors:

* the product template is the “T-shirt” which contains information common to all sizes and all colors,

* the variants are “Size:S” and “Colour:Red”, which define the parameters for that size and color,

* the final product is thus the combination of the two – t-shirt in size S and color Red.

The value of this approach for some sectors is that you can just define a template in detail and all of its available variants briefly rather than every item as an entire product.

	.. note::  *Example Product templates and variants* 

			A product can be defined as a whole or as a product template and several variants. The variants can be in one or several dimensions, depending on the installed modules.

			For example, if you work in textiles, the variants on the product template for “T-shirt” are:

			* Size (S, M, L, XL, XXL),

			* Co lour (white, grey, black, red),

			* Quality of Cloth (125g/m2, 150g/m2, 160g/m2, 180g/m2),

			* Collar (V, Round).

			This separation of variant types requires the optional module fashion. Using it means that you can avoid an explosion in the number of products to manage in the database. If you take the example above it's easier to manage a template with 15 variants in four different types than 160 completely different products. This module is available in the extra_addons list (although it had not been updated, at the time of writing, to work in release 4.2.2 of Open ERP).

The  *Products*  menu gives you access to the definition of products and their constituent templates and variants, and to price lists.

.. tip::   **Terminology**  *Consumables* 

	In Open ERP a consumable is a physical product which is treated like a stockable product except that stock management isn't taken into account by the system. You could buy it, deliver it or produce it but Open ERP will always assume that there's enough of it in stock. It never triggers a restocking exception.

Open a product form to see the information that describes it. Several different types of product can be found in the demonstration data, giving quite a good overview of the possible options.

Price lists ( *Products > Pricelists* ) determine the purchase and selling prices and adjustments derived from the use of different currencies. The  *Default Purchase Pricelist*  uses the product's  *Cost*  field to base a Purchase price on. The  *Default Sale Pricelist*  uses the product's  *List Price*  field to base a Sales price on when issuing a quote.

Price lists are extremely flexible and enable you to put a whole price management policy in place. They're composed of simple rules that enable you to build up a rule set for most complex situations: multiple discounts, selling prices based on purchase prices, price reductions, promotions on whole product ranges and so on.

You can find many optional modules to extend product functionality through the Open ERP website, such as:

* \ ``membership``\  : for managing the subscriptions of members of a company,

* \ ``product_electronic``\  : for managing electronic products,

* \ ``product_extended``\  : for managing production costs,

* \ ``product_expiry``\  : for agro-food products where items must be retired after a certain period,

* \ ``product_lot_foundry``\  : for managing forged metal products.

Human Resources
-----------------

Open ERP's Human Resources Management modules provide such functionality as:

* management of staff and the holiday calendar,

* management of employment contracts,

* benefits management,

* management of holiday and sickness breaks,

* managing claims processes,

* management of staff performance,

* management of skills and competencies.

Most of these functions are provided from optional modules whose name starts with \ ``hr_``\   rather than the core HR module, but they're all loaded into the main  *Human Resources*  menu.

The different issues are handled in detail in the fourth section of this book, dedicated to internal organization and to the management of a services business.

Inventory Control
-------------------

The various sub-menus under Inventory Control together provide operations you need to manage stock. You can:

* define your warehouses and structure them around locations and layouts of your choosing,

* manage inventory rotation and stock levels,

* execute packing orders generated by the system,

* execute deliveries with delivery notes and calculate delivery charges,

* manage lots and serial numbers for traceability,

* calculate theoretical stock levels and automate stock valuation,

* create rules for automatic stock replenishment.

Packing orders and deliveries are usually defined automatically by calculating requirements based on sales. Stores staff use picking lists generated by Open ERP, produced automatically in order of priority.

Stock management is, like accounting, double-entry. So stocks don't appear and vanish magically within a warehouse, they just get moved from place to place. And, just like accounting, such a double-entry system gives you big advantages when you come to audit stock because each missing item has a counterpart somewhere. 

Most stock management software is limited to generating lists of products in warehouses. Because of its double-entry system Open ERP automatically manages customer and suppliers stocks as well, which has many advantages: complete traceability from supplier to customer, management of consigned stock, and analysis of counterpart stock moves.

Furthermore, just like accounts, stock locations are hierarchical, so you can carry out analyses at various levels of detail.

Customer and Supplier Relationship Management
-----------------------------------------------

Open ERP provides many tools for managing relationships with partners. These are available through the  *CRM & SRM*  menu.

.. tip::   **Terminology**  *CRM and SRM* 

	CRM stands for Customer Relationship Management, a standard term for systems that manage client and customer relations. SRM stands for Supplier Relationship Management, and is commonly used for functions that manage your communications with your suppliers.

The concept of a “case” is used to handle arbitrary different types of relationship, each derived from a generic method. You can use it for all types of communication such as order enquiries, quality problems, management of a call center, record tracking, support requests and job offers. 

Open ERP ensures that each case is handled effectively by the system's users, customers and suppliers. It can automatically reassign a case, track it for the new owner, send reminders by email and raise other Open ERP documentation and processes.

All operations are archived, and an email gateway lets you update a case automatically from emails sent and received. A system of rules enables you to set up actions that can automatically improve your process quality by ensuring that open cases never escape attention.

As well as those functions, you've got tools to improve the productivity of all staff in their daily work:

* a document editor that interfaces with OpenOffice.org,

* interfaces to synchronize your contacts and Outlook Calendar with Open ERP,

* an Outlook plugin enabling you to automatically store your emails and their attachments in a Document Management System integrated with Open ERP,

* a portal for your suppliers and customers that enables them to access certain data on your system.

You can implement a continuous improvement policy for all of your services, by using some of the statistical tools in Open ERP to analyze the different communications with your partners. With these, you can execute a real improvement policy to manage your service quality.

The management of customer relationships is detailed in the second section of this book (see Chapters 4 and 5).

Purchase Management
---------------------

Purchase management enables you to track your suppliers' price quotations and convert them into Purchase Orders as you require. Open ERP has several methods of monitoring invoices and tracking the receipt of ordered goods.

You can handle partial deliveries in Open ERP, so you can keep track of items that are still to be delivered on your orders, and you can issue reminders automatically.

Open ERP's replenishment management rules enable the system to generate draft purchase orders automatically, or you can configure it to run a lean process driven entirely by current production needs.

.. tip::   **Note**  *Workflow visualization* 

	Open ERP can show you the workflow of any operating process and the current state of a document following the workflow, to help you understand your company processes. This operation is available in the GTK client, not (at the time of writing) the web client.

	For example, open a supplier Purchase Order form in the GTK client. Click Plugins > Execute a Plugin, then select Print Workflow (complex) and click OK.

	As the Purchase Order progresses, you can keep reprinting the displayed workflow. The order's state is marked by nodes colored red.

---------

	.. image:: images/purchase_workflow.png
	   :align: center

*Purchase order workflow*


Project Management
-------------------

Open ERP's project management tools enable you to handle the definition of tasks and the specification of requirements for those tasks, efficient allocation of resources to the requirements, project planning, scheduling and automatic communication with partners.

All projects are hierarchically structured. You can review all of the projects from the menu  *Project Management > All Projects*  . To view a project's plans, select a project line and then click  *Print* . Then select  *Gantt diagram*  to obtain a graphical representation of the plan.


	.. image:: images/familiarization_project_gantt.png
	   :align: center

*Project Planning*


You can run projects related to Services or Support, Production or Development – it's a universal module for all enterprise needs.

Project Management is described in Chapter 12.

Production Management
-----------------------

Open ERP's production management capabilities enable companies to plan, automate, and track manufacturing and product assembly. Open ERP supports multi-level Bills of Materials and lets you substitute subassemblies dynamically, at the time of sales ordering. You can create virtual sub-assemblies for reuse on several products with Phantom Bills of Materials.

.. tip::   **Terminology**  *BoMs, routing, workcenters* 

	These documents describe the materials that make up a larger assembly. They're commonly called Bills of Materials or BoMs.

	They're linked to routings which list the operations needed to carry out the manufacture or assembly of the product.

	Each operation is carried out at a workcenter, which can be a machine, a tool, or a person.

Production orders based on your company's requirements are scheduled automatically by the system, but you can also run the schedulers manually whenever you want. Orders are worked out by calculating the requirements from sales, through Bills of Materials, taking current inventory into account. The production schedule is also generated from the various lead times defined throughout, using the same route

The demonstration data contains a list of products and raw materials with various classifications and ranges. You can test the system using this data.

Sales Management
-----------------

The Sales Management menu gives you roughly the same functionality as the Purchase Management menu – the ability to create new orders and to review the existing orders in their various states – but there are important differences in the workflows. 

Confirmation of an order triggers delivery of the goods, and invoicing timing is defined by a setting in each individual order. 

Delivery charges can be managed using a grid of tariffs for different carriers.

Other functions
-----------------

You've been through a brisk, brief overview of the main functional areas of Open ERP. Some of these – a large proportion of the core modules – are treated in more detail in the following chapters. 

You can use the menu  *Administration > Modules Management > Modules > Uninstalled Modules*  to find the remaining modules that have been loaded into your installation but not yet installed in your database. Some modules have only minor side-effects to Open ERP (such as \ ``base_iban``\  ), some have quite extensive effects (such as the various charts of accounts), and some make fundamental additions (such as \ ``multi_company``\  ).

But there are now more than three hundred modules available. If you've connected to the Internet, and if your \ ``addons``\   directory is writable as described at the beginning of this chapter, you can download new modules using the menu  *Administration > Modules Management > Update Modules List* . 

A brief description is available for each module, but the most thorough way of understanding their functionality is to install one and try it. So, pausing only to prepare another test database to try it out on, just download and install the modules that appear interesting.



.. Copyright © Open Object Press. All rights reserved.

.. You may take electronic copy of this publication and distribute it if you don't
.. change the content. You can also print a copy to be read by yourself only.

.. We have contracts with different publishers in different countries to sell and
.. distribute paper or electronic based versions of this book (translated or not)
.. in bookstores. This helps to distribute and promote the Open ERP product. It
.. also helps us to create incentives to pay contributors and authors using author
.. rights of these sales.

.. Due to this, grants to translate, modify or sell this book are strictly
.. forbidden, unless Tiny SPRL (representing Open Object Presses) gives you a
.. written authorisation for this.

.. Many of the designations used by manufacturers and suppliers to distinguish their
.. products are claimed as trademarks. Where those designations appear in this book,
.. and Open ERP Press was aware of a trademark claim, the designations have been
.. printed in initial capitals.

.. While every precaution has been taken in the preparation of this book, the publisher
.. and the authors assume no responsibility for errors or omissions, or for damages
.. resulting from the use of the information contained herein.

.. Published by Open ERP Press, Grand Rosière, Belgium

