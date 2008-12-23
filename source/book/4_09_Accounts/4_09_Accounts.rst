

Analytic Accounts
###################

Summary

* Introduction

* Configuration

* Accounting Entries

* Financial Analysis

Keywords

* analytic accounts

* task

* project

* profitability

* chart of accounts

* journal

* budget

 *Sitting at the heart of your company's processes, analytic accounts (or cost accounts) are indispensable tools for managing your operations well. Unlike your financial accounts they're for more than accountants, they're for general managers and project managers too.* 

You need a common way of referring to each user, service, or document to integrate all your company's processes effectively. Such a common basis is provided by analytic accounts (or management accounts, or cost accounts, as they're also called) in Open ERP.

Analytic accounts are often presented as a foundation for strategic enterprise decisions. But because of all the information they pull together, Open ERP's analytic accounts can be a useful management tool, at the center of most system processes

There are several reasons for this:

*  reflect your entire management activity,

* unlike the general accounts, the structure of the analytic accounts isn't regulated by legal obligations, so each company can adapt it to its needs.

.. tip::   **Advantage**  *Independence from general accounts* 

	In some software packages, analytic accounts are managed as an extension of general accounts – for example, by using the two last digits of the account code to represent analytic accounts.

	In Open ERP, analytic accounts are linked to general accounts but are treated totally independently. So you can enter various different analytic operations that have no counterpart in the general financial accounts.

While the structure of the general chart of accounts is imposed by law, the analytic chart of accounts is built to fit a company's needs closely.

Just as in the general accounts, you'll find accounting entries in the different analytic accounts. Each analytic entry can be linked to a general account, or not, as you wish. Conversely, an entry in a general account can be linked to one, several, or no corresponding analytic accounts.

You'll discover many advantages of this independent representation below. For the more impatient, here are some of those advantages:

* you can manage many different analytic operations,

* you can modify an analytic plan on the fly, during the course of an activity, because of its independence,

* you can avoid an explosion in the number of general accounts,

* even those companies that don't use Open ERP's general accounts can use the analytic accounts for management.

.. tip::   **Important**  *Who gains from analytic accounts?* 

	Unlike general accounts, analytic accounts in Open ERP aren't about accounting so much as a management tool for everyone in the company. That's why they're also called management accounts.

	The main users of analytic accounts are the directors, general managers and project managers.

Analytic accounts make up a powerful tool that can be used in different ways. The trick is to create your own analytic structure for a chart of accounts that closely matches your company's needs. 

To each enterprise its own analytic chart
===========================================

To illustrate analytic accounts clearly, you can follow three use cases, each in one of three different types of company:

	#. An industrial manufacturing enterprise.

	#. A law firm.

	#. An IT services company.

Case 1: an industrial manufacturing enterprise
-----------------------------------------------

In industry, you'll often find analytic charts of accounts structured into the departments and products that the company itself is built on.

So the objective is to examine the costs, sales and margins by department and by product. The first level of the structure comprises the different departments and the lower levels represent the product ranges that the company makes and sells. 

	.. note::  *Example Analytic representation of the chart of accounts for an industrial manufacturing company* 

		#. Marketing Department

		#. Commercial Department

		#. Administration Department

		#. Production

			* Product Range 1

			* Sub-groups

			* Product Range 2

In daily use it's useful to mark the analytic account on each purchase invoice. The analytic account is the one to which the costs of that purchase should be allocated. When the invoice is approved it will automatically generate the entries for both the general and the corresponding analytic accounts. So, for each entry on the general accounts there's at least one analytic entry that allocates costs to the department that incurred them.

Here's a possible breakdown of some general accounting entries for the example above, allocated to various analytic accounts:


.. csv-table::  **Breakdown of general and analytic accounting entries (Case 1)**
   :header: "General accounts","","","","","Analytic accounts",""
   :widths: 10,5,5,5,2,10,8
   
   "Title","Account","Debit","Credit","","Account","Value"
   "Purchase of Raw Material","600","1500","","","Production / Range 1","1 500"
   "Subcontractors","602","450","","","Production / Range 2","-450"
   "Credit Note for defective materials","600","","200","","Production / Range 1","200"
   "Transport charges","613","450","","","Production / Range 1","-450"
   "Staff costs","6201","10000","","","Marketing","-2 000"
   "","","","","","Commercial","-3 000"
   "","","","","","Administrative","-1 000"
   "","","","","","Production / Range 1","-2 000"
   "","","","","","Production / Range 2"," 2 000"
   "PR ","614","450","","","Marketing"," 450 "

The analytic representation by department enables you to investigate the costs allocated to each department in the company.

So the analytic chart of accounts shows the distribution of the company's costs using the example above:



.. csv-table::  **Analytic chart of accounts (Case 1)**
   :header: "Account","Total"
   :widths: 10, 5
   
   "Marketing Department","-2 450 "
   "Commercial Department","-3 000 "
   "Administration Department","-1 000 "
   "Production","-6 200 "
   "Product Range 1","-3 750"
   "Product Range 2","-2 450"

In this example of a hierarchical structure in Open ERP you can analyze not only the costs of each product range but also the costs of the whole of production. The balance of a summary account ( *Production* ) is the sum of the balances of the child accounts.

A report that relates both general accounts and analytic accounts enables you to get a breakdown of costs within a given department. An analysis of the Production / Product Range 1 department is shown in this table:



.. csv-table:: **Report merging both general and analytic accounts for a department (Case 1)**
   :header: "Production / Product Range 1",""
   :widths: 10,5
   
   "General Account","Amount"
   "600 – Raw Materials"," 1 300"
   "613 – Transport charges","- 450"
   "6201 – Staff costs","-2 000"
   "Total","-3 750"



The examples above are based on a breakdown of the costs of the company. Analytic allocations can be just as effective for sales. That gives you the profitability (sales - costs) of different departments.

.. tip::   **Alternative**  *Representation by unique product range* 

	This analytic representation by department and by product range is usually used by trading companies and industry.

	A variant of this is not to break it down by commercial and marketing departments but to assign each cost to its corresponding product range. This will give you an analysis of the profitability of each product range.

	Choosing one over the other depends on how you look at your marketing effort. Is it a global cost allocated in some general way or does each product range have responsibility for its own marketing costs?

Case 2: a law firm
-------------------

Law firms generally adopt management by case where each case represents a current client file. All of the expenses and products are then attached to a given file.

A principal preoccupation of law firms is the invoicing of hours worked and the profitability by case and by employee.

Mechanisms used for encoding the hours worked will be covered in detail in the following chapter. Like most system processes, hours worked are integrated into the analytic accounting. Every time an employee enters a timesheet for a number of hours, that automatically generates analytic accounts corresponding to the cost of those hours in the case concerned. The hourly charge is a function of the employee's salary.

So a law firm will opt for an analytic representation which reflects the management of the time that employees work on the different client cases.

	.. note::  *Example Representation of an analytic chart of accounts for a law firm* 

		#. Absences

			* Paid Absences

			* Unpaid Absences

		#. Internal Projects

			* Administrative

			* Others

		#. Client cases

			* Client 1

			* Case 1.1

			* Case 1.2

			* Client 2

			* Case 2.1

All expenses and sales are then attached to a case. This gives the profitability of each case and, at a consolidated level, of each client.

Billing for the different cases is a bit unusual. The cases don't match any entry on the general account and nor do they come from purchase or sale invoices. They're represented by the various analytic operations and don't have exact counterparts in the general accounts. They're calculated on the basis of the hourly cost per employee. These entries are automatically created on billing worksheets.

At the end of the month when you pay salaries and benefits, you integrate them into the general accounts but not in the analytic accounts, because they've already been accounted for in billing each account. A report that relates data from the analytic and general accounts then lets you compare the totals, so you can readjust your estimates of hourly cost per employee depending on the time actually worked.

The following table gives an example of different analytic entries that you can find for your analytic account:


.. csv-table::  **Analytic entries for the account chart (Case 2)**
   :header: "Title","Account","Amount","","General Account","Debit","Credit"
   :widths: 15, 10, 8 ,2,15 ,8,8
   
   "Study the file (1 h)","Case 1.1","-15","","","",""
   "Search for information (3 h)","Case 1.1","-45","","","",""
   "Consultation (4 h)","Case 2.1","-60","","","",""
   "Service charges","Case 1.1","280","","705 – Billing services","","280"
   "Stationery purchase","Administrative","-42","","601 – Furniture purchase","42",""
   "Fuel Cost -Client trip","Case 1.1","-35","","613 – Transports","35",""
   "Staff salaries","","","","6201 – Salaries","","3 000"

You'll instantly see that it allows you to make a detailed study of the profitability of different transactions. In this example the cost of Case 1.1 is 95.00 (the sum of the analytic costs of studying the files, searching for information and service charges), but has been invoiced for 280.00, which gives you a gross profit of 185.00.

But an interest in analytical accounts isn't limited to a simple analysis of the profitability of different cases.

This same data can be used for automatic recharging of the services to the client at the end of the month. To invoice clients just take the analytic costs in that month and apply a selling price factor to generate the invoice. Invoicing mechanisms for this are explained in greater detail in chapter 11. If the client requires details of the services used on the case, you can then print the service entries in the analytic account for this case.

.. tip::   **Advantage**  *Invoicing analytic costs* 

	Most software that manages billing enables you to recharge for hours worked. In Open ERP these services are automatically represented by analytic costs. But many other Open ERP documents can also generate analytic costs, such as credit notes and purchases of goods.

	So when you invoice the client at the end of the month it's possible for you to include all the analytic costs, not just the hours worked. So, for example you can easily recharge the whole cost of your journeys to the client.

Case 3 : An IT Services Company
---------------------------------

Most IT services companies face the following problems:

* project planning,

* invoicing, profitability and financial follow-up of projects,

* managing support contracts.

To deal with these problems you'd use an analytic chart of accounts structured by project and by contract. A representation of that is given in the following example.

	.. note::  *Example Analytic representation of a chart of accounts for an IT Services company* 

		#. Internal Projects

			* Administrative and Commercial

			* Research and Development

		#. Client Projects

			* Client 1

			* Project 1.1

			* Project 1.2

			* Client 2

			* Project 2.1

			* Project 2.2

		#. Support Contracts – 20h

			* Customer X

			* Customer Y

The management of services, expenditures and sales is similar to that presented above for lawyers. Invoicing and the study of profitability are also similar.

But now look at support contracts. These contracts are usually limited to a prepaid number of hours. Each service posted in the analytic accounts shows the remaining available hours of support. For the management of support contracts you'd use the quantities and not the amounts in the analytic entries. 

In Open ERP each analytic line lists the number of units sold or used, as well as what you'd usually find there – the amount in currency units (USD or GBP, or whatever other choice you make). So you can sum the quantities sold and used on each analytic account to determine whether any hours of the support contract remain.

To differentiate services from other costs in the analytic account you use the concept of the analytic journal. Analytic entries are then allocated into the different journals:

* service journal,

* expense journal,

* sales journal,

* purchase journal.

So to obtain the detailed breakdown of a support contract you only have to look at the service journal for the analytic account corresponding to the contract in question.

Finally, the analytic account can be used to forecast future needs. For example, monthly planning of staff on different projects can be seen as an analytic budget limited to the service journal. Accounting entries are expressed in quantities (such as number of hours, and numbers of products) and in amounts in units of currency (USD or GBP perhaps). 

So you can set up planning on the basis just of quantities. Analyzing the analytic budget enables you to compare the budget (that is, your plan) to the services actually carried out by month end.

.. tip::   **Advice**  *Cash Budgets* 

	Problems of cash management are amongst the main difficulties encountered by small growing businesses. It's really difficult to predict the amount of cash that will be available when a company is young and rapidly growing. 

	If the company adopts management by case, then staff planning can be represented on the analytic accounts report, as you have seen. 

	But since you know your selling price for each of the different projects, you can see that it's easy to use the plan in the analytic accounts to precisely anticipate the amounts that you'll invoice in the coming months.

Putting analytic accounts in place
===================================

For the initial setup of good analytic accounts you should:

* set up the chart of accounts,

* create the different journals.

Setting up the chart of accounts
---------------------------------

Start by choosing the most suitable analytic representation for your company before entering it into Open ERP. To create the different analytic accounts, use the menu  *Financial Management > Configuration > Analytic Accounts > Analytic Accounts* .


	.. image::  images/account_analytic_form.png
	   :align: center

*Setting up an analytic account*

To create an analytic account you have to complete the main fields:

* the  *Account Name* ,

* the  *Account Code* , which is used as a shortcut for selecting the account,

* the  *Account type* , just like general accounts the \ ``View``\   type is used for virtual accounts which are used only to create a hierarchical structure and for subtotals, and not to store accounting entries,

* the  *Parent analytic account* , which defines the hierarchy between the accounts.

If the project is for a limited time you can define a start and end date here. The  *State*  field is used to indicate whether the project is running (\ ``Open``\  ), waiting for information from the client (Pending), \ ``Draft``\   or \ ``Closed``\  .

Finally, if the analytic account is a client project you can complete the fields about the partner, which you'd need so that you can invoice the partner:

* the  *Associated partner* ,

* a  *Sale Pricelist* , which shows how services linked to the project should be charged,

* a  *Max. Invoice Price* , showing the maximum invoice price regardless of actual overspend,

* a  *Max. Quantity* , for contracts with a fixed limit of hours to use,

* an  *Invoicing*  field, which defines an invoicing rate and whether the project should be invoiced automatically from the services represented by the costs in the analytic account.

.. tip::   **Methods**  *Invoicing* 

	You have several methods available to you in Open ERP for automated invoicing:

	* Service companies usually use invoicing from purchase orders, analytic accounts or, more rarely, project management tasks.

	* Manufacturing and trading companies more often use invoicing from deliveries or customer purchase orders.


	.. image::  images/account_analytic_chart.png
	   :align: center

*Example of an analytic chart for projects*

Once you've defined the different analytic accounts you can view your chart through the menu  *Financial Management > Charts > Analytic Charts of Accounts* .

.. tip::   **Technique**  *Setting up an analytic account* 

	The setup screen for an analytic account can vary greatly depending on the modules installed in your database. For example, you'll only see information about recharging services if you have the module hr_timesheet_invoice installed.

	Some of these modules add helpful management statistics to the analytic account. The most useful is probably the module account_analytic_analysis, which adds such information as indicators about your margins, invoicing amounts, and latest service dates and invoice dates.

Creating Journals
-------------------

Once the analytic chart has been created for your company you have to create the different journals. These enable you to categorize the different accounting entries by their type:

* services,

* expense reimbursements,

* purchases of materials,

* miscellaneous expenditure,

* sales,

* situation entries (special situations, such as installation of the software).

.. tip::   **Attention**  *Minimal journals* 

	At a minimum you have to create one analytic journal for Sales and one for Purchases. If you don't create these two, Open ERP won't validate invoices linked to an analytic account because it wouldn't be able to create an analytic accounting entry automatically.


	.. image::  images/account_analytic_journal.png
	   :align: center

*Creating an analytic journal*

To define your analytic journals, use the menu  *Financial Management > Configuration > Journal > Analytic Journal Definition* .

It's easy to create an analytic journal. Just give it a  *Name* , a  *Code*  and a  *Type* . The types available are:

* \ ``Sales``\  , for sales to customers and for credit notes,

* \ ``Purchases``\  , for purchases and miscellaneous expenses,

* \ ``Cash``\  , for financial entries,

* \ ``Situation``\  , to adjust accounts when starting an activity, or at the end of the financial year,

* \ ``General``\  , for all other entries.

The type of journal enables the software to automatically select the analytic journal based on the nature of the operation. For example if you enter an invoice for a customer, Open ERP will automatically search for an analytic journal of type \ ``Sales``\  .

Analytic records
=================

Just as in general accounting, analytic entries must belong to an account and an analytic journal.

Analytic records can be distinguished from general records by the following characteristics:

* they're not necessarily legal accounting documents,

* they don't necessarily belong to an existing accounting period,

* they're managed according to their date and not an accounting period,

* they don't generate both a debit and a credit entry, but a positive amount (income) or a negative amount (cost).


	.. image::  images/account_analytic_move.png
	   :align: center

*Analytic account records for a customer project*

The figure represents the entries on an analytic account for a customer project.

You can see there:

* the service costs for staff working on the project,

* the costs for reimbursing the expenses of a return journey to the customer,

* purchases of goods that have been delivered to the customer,

* sales for recharging these costs.

Automated entries
-------------------

Analytic accounting is totally integrated with the other Open ERP modules, so you never have to re-enter the records. They're automatically generated by the following operations:

* confirmation of an invoice generates analytic entries for sales or purchases connected to the account shown in the invoice line,

* the entry of a service generates an analytic entry for the cost of this service to the given project,

* the manufacture of a product generates an entry for the manufacturing cost of each operation in the product range.

Other documents linked to one of these three operations produce analytic records indirectly. For example, when you're entering a customer sales order you can link it to the customer's analytic account. When you're managing by case or project, mark the project with that order. This order will then generate a customer invoice, which will be linked to the analytic account. When the invoice is validated it will automatically create general and analytic accounting records for the corresponding project.

Expense receipts from an employee can be linked to an analytic account for reimbursement. When a receipt is approved by the company, a purchase invoice is created. This invoice represents a debit on the company in favor of the employee. Each line of the purchase invoice is then linked to an analytic account which automatically allocates the costs for that receipt to the corresponding project.

To visualize the general entries following these different actions you can use one of the following menus:

	#. To see all of the entries:  *Financial Management > Entries > Analytic Entries > Analytic Entries* 

	#. To see the entries per account, click the  *Analytic Account * ield of any of the lines of Analytic Entries to see the details of that entry, then use the analytic  *Account name* to start a search of all entries with that name (just click the Date hyperlink on a line in the web client, or double-click the line in the GTK client).

	#. To see all of the entries by Journal:  *Financial Management > Entries > Analytic Entries > Entries by journal*  and then click on one of the journal names.

.. tip::   **Note**  *Reviewing a hierarchical account* 

	In the chart of analytic accounts, if you click on an account Open ERP opens a window showing the corresponding analytic entries. 

	It was intended that if you do that on a View-type account Open ERP opens all of the entries belonging to its child accounts. That can be very useful for opening entries belonging to several accounts, such as all project clients. (It didn't do that in version 4.2.2 – later versions may be fixed.) 

Manual record entry
---------------------

Even though most analytic entries are produced automatically by the other Open ERP documents it's sometimes necessary to make manual record entries. It's usually needed for certain analytic operations that have no counterpart in the general accounts.

To make manual record entries, use the menu  *Financial Management > Entries > Analytic Entries > Entries by journal* .

.. tip::   **Comment**  *Analytic entries* 

	To make an analytic entry, Open ERP asks you to specify a general account. This is given only for information in the different cross-reports. It won't create any new entries in the general accounts.

Select a journal and complete the different fields. Write an expense as a negative figure and income as a positive figure.

.. tip::   **Note**  *Entering a date* 

	To enter a date in the editable list you can use the calendar widget in the web client or, in the GTK client, if you enter just the day of the month Open ERP automatically completes the month and year when you press the tab key (Tab).

	.. note::  *Example Cost redistribution* 

For example 

			One of the uses of manual data entry for analytic operations is reallocation of costs. For example, if a development has been done for a given project but can be used again for another project you can reallocate part of the cost to the other project.

			In this case, make a positive entry on the first account and a negative entry for the same amount on the account of the second project.

Financial Analysis
===================

Various reports designed for financial analysis are based on the analytic accounts. Most of those are available directly from the tree of accounts or from the form view of the account.

Analysis per account
---------------------

 *Print* 

*  *Analytic Balance* ,

*  *Inverted Analytic Balance* ,

*  *Cost Ledger* , 

*  *Cost Ledger (quantities only)* .

Analytic Balance
^^^^^^^^^^^^^^^^^


	.. image::  images/analytic_balance.png
	   :align: center

*The analytic balance presents the breakdown of each project by the nature of the operations given by the financial accounts*

The analytic balance is a report that relates the analytic accounts to the general accounts. It gives, for a given period, the balances of the analytic accounts broken down by general account.

This report is useful for analyzing the profitability of projects. It gives you the profitability of a project for the different operations that you used to carry out the project.

Inverted Analytic Balance
^^^^^^^^^^^^^^^^^^^^^^^^^^^

The inverted analytic balance provides a similar report relating the general accounts and the analytic accounts. This report shows, for a given period, the balances of the general accounts broken down by the selected analytic accounts.


	.. image::  images/analytic_balance_inverse.png
	   :align: center

*The inverted analytic balance indicates the breakdown of operations by the nature of the different the analytic accounts (projects)*

This enables you to analyze your costs by general account. For example, if you examine your general account for staff salaries you can obtain all your salary costs broken down by the different analytic (or project) accounts.

The cost ledger
^^^^^^^^^^^^^^^^^

While the two reports above provide results summed by account, the cost ledger provides all of the detailed entries for the selected accounts. It enables a detailed analysis of each operation carried out on one or several projects.


	.. image::  images/analytic_cost_ledger.png
	   :align: center

*The analytic cost ledger gives a detailed history of the entries in an analytic account*

The cost ledger (quantities only)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The last report gives the detail of entries for an analytic account and a list of selected journals. Only quantities are reported for this analysis, not costs and revenues. 


	.. image::  images/analytic_cost_ledger_quantity.png
	   :align: center

*The cost ledger (quantities only) gives a history of an analytic account.*

The report is frequently used to print the number of hours worked on a project, without showing the costs and revenues. So you can show it to a client as a record of the hours worked on a particular project.

To restrict the report to hours worked, without including sales and purchases, select only the services journal to print the report.

.. tip::   **Note **  *M*  *ultiple printing* 

	To print several analytic accounts at once you can make a multiple selection on the different account in the tree of accounts. For that select account lines using the Ctrl-Click keyboard and mouse combination.

	Then click on Print in the tree or list view to export the whole selection into a single PDF document.

.. tip::   **Note**  **  *Multi-company* 

	In a multi-company environment each company can have its own general chart of accounts on the same database. The two general charts of accounts are then independent but can be linked in a third chart using a view account to do the consolidation.

	If the different companies collaborate on joint projects they may all share the same analytic chart of accounts. In this environment, the cross-related reports like the balance and inverted balance are extremely useful because they enable you to make an analysis per company by linking up to the general accounts.

Key indicators
---------------

If you use analytic accounts with a structure of accounts by project client you should install the \ ``account_analytic_analysis``\   module. This module adds three new tabs to the analytic account form:

* management indicators in the  *Analysis summary*  tab,

* monthly statistics in the  *Stats by month*  tab,

* statistics on each user in the  *Stats by user*  tab.


	.. image::  images/account_analytic_analysis.png
	   :align: center

*Management indicators for an analytic account*

The figure shows all of the management indicators.

These indicators enable you to quickly see the following elements:

* project profitability,

* whether you can still invoice any services to the client, or not,

* the amount of services to invoice,

* the different margins.


	.. image::  images/account_analytic_analysis_month.png
	   :align: center

*Breakdown of monthly costs for an analytic account*

The real revenue is given by the amount invoiced to the client. The theoretical revenue is given by the sale price of different project costs which could be invoiced to the client. These give different margin figures.

For example, in the case of a fixed price project contract, the real sale price at the end of the project will be equal to the contract negotiated with the client. The theoretical price gives the amount that would have been invoiced if you had charged for all the time worked.

To give project managers a direct view of their different projects, the \ ``account_analytic_analysis``\   module creates new menus in the Project management module in  *Project Management > Analytic Accounts* .


	.. image::  images/account_analytic_project_menu.png
	   :align: center

*Analytic accounts in Project Management*

These different menus give quick views that are very useful for live projects. For each project you can check if there are uninvoiced services, and see the last invoice date and the last uninvoiced service date, and reports on the amounts received and those planned. Project managers have therefore all the information necessary to manage their project well, shown in a single page.

In the following chapters you'll see how each project manager can use this information to carry out the different operations needed to manage the project, such as automatic invoicing, project planning, keeping customers up to date, and budgeting for resources.

.. tip::   **A step further**  *Analytic Budgets* 

	There's been no discussion of analytic budgets in this section because at the time this book was being prepared, the module that handles them was being completely rewritten.

	Nevertheless, it's worth trying them because they offer the possibility of::

	* forecasting projects in the medium term,

	* controlling project costs,

	* comparing with the general accounts.

