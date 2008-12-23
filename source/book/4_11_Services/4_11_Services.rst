

The Management of Services
###########################


Summary

* Management of prices

* Management of contracts

* Invoicing processes

* Enterprise planning

* Expense reimbursements

Keywords

* pricelist

* contract

* employee

* invoicing

* planning

* expense receipts

 *This chapter focuses on the management of contracts, and the services associated with that. The complete process of managing services is studied here: from defining prices and contracts to automatically invoicing the services, through planning and the treatment of additional costs such as expense receipts.* 

Price management policies
===========================

Some companies are notorious for their complicated pricelists. Many forms of price variation are used, such as end-of-year refunds, discounts, changes of terms and conditions with time, various prepayments, cascaded rebates, seasonal promotions, and progressive price reductions.

.. tip::   *Terminology* 

	In some accounting jurisdictions you have to differentiate between the three following terms:

	* Rebate: reimbursement to the client, usually at the end of the year, that depends on the quantity of goods purchased over a period.

	* Refund: reduction on the order line or invoice line if a certain quantity of goods is purchased at one time or is sold in a framework of a promotional activity.

	* Reduction: A one-off reduction resulting from a quality defect or a variation in a product's conformance to a specification.

Intelligent price management is difficult, because it requires you to integrate several conditions from clients and suppliers to create estimates quickly or to invoice automatically. But if you have an efficient price management mechanism you can often keep margins raised and respond quickly to changes in market conditions. A good price management system gives you scope for varying any and all of the relevant factors when you're negotiating a contract.

To help you work most effectively, Open ERP's pricelist principles are extremely powerful yet are based on simple and generic rules. You can develop both sales pricelists and purchase pricelists for products capable of accommodating conditions such as the date period, the quantity requested and the type of product.

.. tip::   **Don't Confuse**  *The different prices* 

	It's important not to confuse the sale price and the base price of a product. In the basic configuration of Open ERP the sale price is made equal to the base price marked on the product file but you can vary the sale price in response to other customer conditions.

	It's the same for purchase price and standard cost. Purchase price is your suppliers' selling price, which changes in response to different criteria such as quantities, dates, and supplier. This is automatically set by the accounting system. You'll find that the two prices have been set to the same for all products by default with the demonstration data, which can be a source of confusion since you're free to set the standard cost to something different.

Each pricelist is calculated from defined policies, so you'll have as many sales pricelists as active sales policies in the company. For example a company that sells products through three sales channels could create the following price lists:

	#. Main distribution:

	- pricelist for Walbury,

	- pricelist for TesMart,

	#. Postal Sales.

	#. Walk-in customers.

\ ``Autumn``\  \ ``Summer``\  \ ``Summer Sales``\  \ ``Winter``\  \ ``Spring``\  

Each pricelist is expressed in a single currency. If your company sells products in several currencies you'll have to create as many pricelists as you have currencies.

The prices on a pricelist can depend on another list, which means that you don't have to repeat the definition of all conditions for each product. So a pricelist in USD can be based on a pricelist in EUR. If the currency conversion rates between EUR and USD change, or the EUR prices change, the USD rates can be automatically adjusted.

Creating pricelists
---------------------

To define a pricelist use the menu  *Products > Pricelists > Pricelists* .

For each list you have to define:

* a  *Name*  for the list,

* a  *Type*  of list: \ ``Sale``\   for customers or \ ``Purchase``\   for suppliers,

* the  *Currency*  in which the prices are expressed.

.. tip::   **Terminology**  *Consumer Price* 

	If you install the module edi a third type of list appears – the Consumer Price, which defines the price displayed for the end user. This doesn't have to match your selling price to an intermediary or distributor.

Pricelist versions
^^^^^^^^^^^^^^^^^^^

Once the list is defined you must provide it with at least one version. To do that use the menu  *Products > Pricelists > Pricelist Versions* . The version contains all of the rules that enable you to calculate a price for a product and a given quantity.

So set the  *Name*  of this associated version. If the list only has a single version you can use the same name for the pricelist and the version. In the  *Pricelist*  field select the pricelist you created.

Then indicate the  *Start date*  and  *End date*  of this version. The fields are both optional: if you don't set any dates the version will be permanently active. Use the  *Active*  field in the versions to activate or disable a pricelist version.

.. tip::   **Note**  **  *Automatically updating the sale pricelist* 

	It's possible to make any sale pricelist depend on one of the other pricelists. So you can decide to make your sale pricelist depend on your supplier's purchase pricelist, to which you add a margin. The prices are automatically calculated as a function of the purchase price and need no further manual adjustment.

Rules for calculating price
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A pricelist version is made up of a set of rules that apply to the product base prices.


	.. image::  images/service_pricelist_line.png
	   :align: center

*Detail of a rules in a pricelist version*

You define the conditions for a rule in the first part of the definition screen labeled  *Rules Test Match* . The rule applies to the  *Product*  or  *Product Template*  and/or the named  *Product Category* . If a rule is applied to a category then it is automatically applied to all of its subcategories too (using the tree structure for product categories).

If you set a minimum quantity in  *Min. Quantity*  the rule will only apply to a quantity the same as or larger than that indicated. This lets you set reduced rates in stages that depend on ordered quantities.

Several rules can be applied to an order. Open ERP evaluates these rules in sequence to select which to apply to the specified price calculation. If several rules are valid only the first in sequence is used for the calculation. The  *Sequence*  field determines the order, starting with the lowest number.

Once a rule has been selected, the system has to determine how to calculate the price from the rule. This operation is based on the criteria set out in the lower part of the form, labeled  *Price Computation* .

The first field you have to complete is labeled  *Based on* . You must indicate the mode of calculating the partner price. You have the choice between:

* the \ ``List Price set``\   in the product file,

* the \ ``Standard Cost set``\   in the product file,

* an \ ``Other Pricelist``\   given in the field  *If Other Pricelist* ,

* the price that varies as a function of a supplier defined in the \ ``Partner section of the product form``\  .

Several other criteria can be considered and added to the list, as you'll see in the following section.

Next, various operations can be applied to the base price to calculate the sales or purchase price for the partner at the specified quantities. To calculate it you apply the formula shown on the form:

Price = Base Price x (1 – Field1) + Field2

 *Field1* \ ``0.20``\  \ ``-0.15``\  

 *Field2*  *Field1* 

 *Rounding Method* \ ``0.05``\  \ ``45.66``\  \ ``45.65``\  \ ``14,567``\  \ ``100``\  \ ``14,600``\  

.. tip::   **Attention**  *Swiss special situation* 

	In Switzerland, the smallest monetary unit is 5 cents. There aren't any 1 or 2 cent coins. So you set Open ERP's rounding to 0.05 to round everything in a Swiss franc pricelist.

 *Field2* \ ``9.99``\  \ ``10``\  \ ``-0.01``\   *Field2* 

 *Min. Margin*  *Max. Margin* \ ``10``\  \ ``10``\  \ ``0``\  

Once the pricelist is defined you can assign it to a partner. To do this, find a Partner and select its  *Properties*  tab. You can then change the  *Purchase Pricelist*  and the  *Sale Pricelist*  that's loaded by default for the partner.

Default pricelists
^^^^^^^^^^^^^^^^^^^


	.. image::  images/product_pricelist_default.png
	   :align: center

*Default pricelists after the installation of Open ERP*

When you install the software two pricelists are created by default: one for sales and one for purchase. These each contain only one pricelist version and only one line in that version.

 *List Price* 

The price for purchases that's defined in the Default Purchase Pricelist is set in the same way by the Standard Cost of the product in the product file.

Case of using pricelists
-------------------------

Let's take the case of an IT systems trading company, for whom the following product categories have been configured:

All products

	#. Accessories

                * Printers

                * Scanners

                * Keyboards and Mice

	#. Computers

                * Portables

	                - Large-screen portables

                * Computers

	                - Office Computers

	                - Professional Computers



In addition, the products presented in the table below are defined in the currency of the installed chart of accounts.

 **Examples of products with their different prices**

TABLE

.. csv-table:: 
   "Product ","List Price","Standard Price","Default supplier price",
   "Acclo Portable","1 200 ","887 ","893 ",
   "Toshibishi Portable","1 340 ","920 ","920 ",
   "Berrel Keyboard","100 ","50 ","50 ",
   "Office Computer","1 400 ","1 000 ","1 000 ",

Defining the list price
^^^^^^^^^^^^^^^^^^^^^^^^^

Now define the sale price for resellers like this:

* For portable computers, the sale price is calculated from the list price of the supplier Acclo, with a supplement of 23% on the cost of purchase.

* For all other products the sale price is given by the standard cost in the product file, on which 31% is added. The price must end in “.99”.

* The sale price of Berrel keyboards is fixed at 60 for a minimum quantity of 5 keyboards purchased. Otherwise it uses the rule above.

Assume that the Acclo pricelist is defined in Open ERP. The pricelist for resellers and the pricelist version then contains three lines:

	#. \ ``Acclo``\  line:

                *  *Product Category* : \ ``Portables``\  ,

                *  *Based on* : \ ``Other pricelist``\  ,

                *  *Pricelist if other* : \ ``Acclo pricelist``\  ,

                *  *Field1* : \ ``-0.23``\  ,

                *  *Sequence* : \ ``1``\  .

	#. \ ``Berrel Keyboard``\  line:

                *  *Product Template* : \ ``Berrel Keyboard``\  ,

                *  *Min. Quantity* : \ ``5``\  ,

                *  *Field1* : \ ``1.0``\  ,

                *  *Field2* : \ ``60``\  ,

                * Sequence: \ ``2``\  .

	#. \ ``Other products``\  line:

                *  *Based on:* \ ``Standard Price``\  ,

                *  *Field1* : \ ``-0.31``\  ,

                *  *Field2* : \ ``-0.01``\  ,

                *  *Sequence* : \ ``3``\  .

                 *Sequence* 

Also note that to fix a price of 60 for the 5 Berrel Keyboards, the formula \ ``Price = Base Price x (1 – 1.0) + 60``\   has been used.

Establishing customer contract conditions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The trading company can now set specific conditions to a customer, such as the company TinAtwo, who might have signed a valid contract with the following conditions:

* For Toshibishi portables, TinAtwo benefits from a discount of 5% of resale price.

* For all other products, the resale conditions are unchanged.

The list price for TinAtwo, called “TinAtwo contract”, contains two rules:

	#. \ ``Toshibishi portable``\  line:

                *  *Product* : \ ``Toshibishi Portable``\  ,

                *  *Based on* : \ ``Other pricelist``\  ,

                *  *Pricelist if other* : \ ``Reseller pricelist``\  ,

                *  *Field1* : \ ``0.05``\  ,

                *  *Sequence* : \ ``1``\  .

	#. \ ``Other Products``\  

                *  *Product: * 

                *  *Based on* : \ ``Other pricelist``\  ,

                *  *Pricelist if other* : \ ``Reseller pricelist``\  ,

                *  *Sequence* : \ ``2``\  .

                \ ``TinAtwo``\   *Properties*  *Sale Pricelist* \ ``TinAtwo Contract``\   *Start date*  *End date* 

Then when salespeople prepare an estimate for TinAtwo prices proposed will automatically be calculated from the contract conditions.

Other bases of price calculation
---------------------------------

Open ERP provides a way of making prices depend on any field of the product form, not just the two predefined fields: \ ``List Price``\   and \ ``Cost Price``\  .

To do this, use the menu  *Products > Configuration > Price Types* . Then create a new entry corresponding to a new type of price. Enter the name of the field (for example: \ ``Public Price``\  ) and the the product field that it corresponds to ( *Public Price* ) and the currency that it's expressed in. New fields are added to the product file so that they can be used in calculations.

Once you've done this you can make a dependency on the new type of price in the pricelist.

 *Weight*  *Volume* 

Managing the price in several currencies
-----------------------------------------

Since each pricelist is defined in a single currency you must create separate pricelists for the other currencies that you sell in. So, if your trading company wants to start a product catalog in a new currency, you have several possibilities:

* Code the price in a new independent pricelist and maintain the lists in the two currencies separately.

* Create a field in the product form for the new currency and make the pricelist depend on the new field: the prices are then maintained separately, but in the product file.

Create a new pricelist for the second currency and make this list depend either on another pricelist or on a product price: the conversion between currencies will be done automatically at the latest rates. This solution is generally the most flexible and the simplest to maintain as prices change with time.

Managing Service Contracts
===========================

Contracts can take different forms within Open ERP, depending on their nature. So you can have several distinct types of service contract, such as:

* fixed-price contracts

* cost-reimbursement contracts, invoiced when services are completed,

* fixed-price contracts, invoiced monthly as services are carried out

.. tip::   **Case**  *Contract quotations* 

	Some companies commit to contracts on the basis of a requested volume at a certain price for a defined period. In this case the contract is represented by a pricelist for that specific customer.

	The pricelist is linked in the Properties tab of the customer's Partner form, so that it is brought up whenever anything is bought from or sold to this partner (depending on whether it's a purchase or sales agreement). Open ERP automatically selects a price based on this agreed pricelist.

Fixed Price contracts
-----------------------

Fixed price contracts for the sale of services are represented in Open ERP by a Sales Order. In this case, the supply of services is managed just like all other stockable or consumable products. 

You can add new orders using the menu  *Sales Management > Sales Order* .

The new Sales Order document starts in the \ ``Quotation``\   state, so the estimate has no accounting impact on the system until it's confirmed. When you approve the document, your estimate moves into the state \ ``In Progress``\  .


	.. image::  images/service_sale_workflow.png
	   :align: center

*Process for handling a Sales Order*

Once the order has been approved, Open ERP will automatically generate an invoice and/or a delivery document proposal based on the parameters you set in the order. 

The invoice will be managed by the system depending on the setting of the field  *Shipping Policy*  on the order's second tab,  *Other data* :

*  *Payment before delivery* : Open ERP creates an invoice in the \ ``Draft``\   state. Once this is confirmed and paid the delivery is activated.

*  *Automatic Invoice after delivery* : the delivery order is produced when the order is validated. A draft invoice is then created when the delivery has been completed.

*  *Shipping & Manual Invoice* : Open ERP starts the delivery from the confirmation of the order, and adds a button which you manually click when you're ready to create an invoice.

*  *Invoice from the Packings* 

.. tip::   **Attention**  **  *Delivery of an order* 

	The term 'delivery' should be taken in the broadest sense in Open ERP. The effect of a delivery depends on the configuration of the sold product.

	If its type is either Stockable Product or Consumable, Open ERP will make a request for it to be sent for packing. If the product's type is Service Open ERP's scheduler will create a task in the project management system, or create a subcontract purchase order if the product's Procure Method is Make to Order.

	Invoicing after delivery does as it says: invoicing for the services when the tasks have been closed.

When you sign a new contract you can just enter the order into the system and Open ERP will track the order.

This works well for small orders. But for larger value services orders you might want to invoice several times through the contract, for example:

* 30% on order,

* 40% on completion,

* 30% one month after the system has gone into production.

In this case you should create several invoices for the one order. You've two options for this:

* Don't handle invoicing automatically from the order but carry out manual invoicing instead,

* Create draft invoices and then link to them in the third tab  *History* , in the  *Related Invoices*  section. When you create an invoice from the order, Open ERP deducts the amounts of the invoices already linked to the order to calculate the proposed invoice value.

Cost-reimbursement contracts
-----------------------------

Some contracts aren't invoiced from a price fixed on the order but from the cost of the services carried out. That's usually what happens in the building sector or in large projects.

The approach you use for this is totally different because instead of using the sales order as the basis of the invoice you must use the analytic accounts. For this you have to install the module \ ``hr_timesheet_invoice``\  .

An analytic account is created for each new contract. The following fields must be completed in this analytic account:

*  *Partner* : partner associated with the contract,

*  *Sale Pricelist* 

*  *Invoicing* 

The selection of an invoicing rate is an indirect way of specifying that the project will be invoiced on the basis of analytic costs. This can take different forms, such as delivery of services, purchase of raw materials, and expense reimbursements.

.. tip::   **Advice**  *Pricelists and billing rates* 

	You can select a pricelist on the analytic account without having to use it to specify billing rates.

	This case is for a client project that is to be invoiced, but not directly from the analytic costs. Putting the price list on the analytic account makes it possible to compare the actual sales with the best case where all the services would be invoiced. To get this comparison you have to print the analytic balance from the analytic account.

Services are then entered onto timesheets by the various people who work on the project. Periodically the project manager or account manager uses the following menu to prepare an invoice:  *Financial Management > Periodical Processing > Invoicing on a Time basis > Uninvoiced Hours* .

Open ERP then displays all of the costs that haven't yet been invoiced. You can filter the proposed list and click the appropriate action button to generate the corresponding invoices. You can select the level of detail which is reported on the invoice, such as the date and details of the services.


	.. image::  images/service_timesheet_invoice.png
	   :align: center

*Screen for invoicing services*

 *Project Management > Analytic Accounts* 

.. tip::   **Point**  *Project Management and analytic accounts* 

	The menu Project Management > Analytic Accounts is only available once you have installed the module account_analytic_analysis. It provides various global financial and operational views of a project manager's projects.

Select a project and open its analytic entries using the  *Costs to invoice*  button. You'll find a list of costs that can be invoiced to the client:

* time worked,

* expense reimbursement,

* purchase of raw materials.

You can then invoice the selected lines using the action  *Invoice costs* .

Fixed-price contracts invoiced as services are worked
-------------------------------------------------------

For larger-value projects, fixed-price invoicing based on the sales order isn't always appropriate. In the case of a services project planned to run for about six months. invoicing could be based on the following:

* 30% on order,

* 30% at the project mid-point,

* 40% at delivery.

Such an approach is often used in a company but there are other options. This method of invoicing can pose many problems for the organization and invoicing of the project:

* It's extremely difficult to determine if the project is on track or not.. The endpoint is fuzzy, which can result in a tricky discussion with the client at the moment of final invoicing.

* If the project takes more or less time than forecast, it will effectively result in under- or over- invoicing during the project.

* Whether you get a proper return can depend on the client. For example if the client takes a long time to sign off on project acceptance you can't invoice the remaining 40% even though you might have supplied the agreed service properly.

* The account manager and the project manager are often different people. The project manager has to alert the account manager the moment that the client can be invoiced, but that moment easily can be forgotten or mistaken.

* The project can be fixed for service costs but have agreed extras, such as reimbursement for travel expenses. Invoicing from the order doesn't adapt well to such an approach.

Open ERP provides a third method for invoicing services that can be useful on long projects. This consists of invoicing the project periodically on the basis of time worked up to a fixed amount that can't be exceeded. At the end of the project a final invoice or a credit note is generated to meet the total amount of value fixed for the project.

To configure such a project you must set an invoicing rate, a pricelist and a maximum amount on the analytic account for the project. The services are then invoiced throughout the project by the different project or account managers, just like projects that are invoiced by time used. The managers can apply a refund on the final invoice if the project takes more time to complete than permitted under the contract.

When the project is finished you can generate the closing invoice using the  *Final Invoice*  button on the analytic account. This automatically calculates the final balance of the bill, taking the amounts already charged into account. If the amount already invoiced is greater than the maximum agreed amount then Open ERP generates a draft credit note.

This approach offers many advantages compared with the traditional methods of invoicing in phases for fixed-price contracts:

* Fixed-price contracts and cost-reimbursable contracts are invoiced in the same way, which makes the company's invoicing process quite simple and systematic even when the projects are mixed.

* Everything is invoiced on the basis of worked time, making it easy to forecast invoicing from plans linked to the different analytical accounts.

* This method of proceeding educates project managers just as much as the client because refunds have to be given for work done if the project slips.

* Invoicing follows the course of the project and avoids a supplier's dependence on the goodwill of the client in approving certain phases.

* Invoicing of expenses follows the same workflow and is therefore very simple.

.. tip::   **Advice**  *Negotiating contracts* 

	In contract negotiation, invoicing conditions are often neglected by the client. So it can often be straightforward to apply this method of invoicing.

Contracts limited to a quantity
---------------------------------

Finally certain contracts are expressed in terms of a quantity rather than a fixed amount. Support contracts comprising a number of prepaid hours are a case in point. To generate such contracts in Open ERP you should start by installing the module \ ``account_analytic_analysis``\  .

Then you can set a maximum number of hours for each analytic account. When employees enter their time worked on the support contract in the timesheets, the hours are automatically deducted from the maximum set on each analytic account.

You must also name someone in the company responsible for renewing expired contracts. They become responsible for searching through the list of accounts showing negative remaining hours.

The client contract can be limited to a certain quantity of hours, and it can also be limited in time. For that, you set an end date for the corresponding analytic account.

Planning that improves leadership
===================================

Planning in a company often takes the form of a regular meeting between the different teams. Each team has a certain number of projects and objectives that they must organize and establish priorities for.

Ideally these planning meetings should be short but regular and systematic. They can be weekly or monthly depending on the type of activity. A planning meeting often runs in three phases:

	#. Minutes of the preceding period, and analysis of the work done compared with the planned work.

	#. Introduction of new projects.

	#. Planning the next period.

The planning function covers several objectives which will be described in this section:

* planning live projects against the commitments that have been made to clients,

* determining staffing (HR) requirements in the coming month,

* setting work for each employee or team for the periods to come,

* analyzing the work done in the preceding periods,

* passing the high-level objectives to lower levels in the company's hierarchy.

.. tip::   **Advice**  *Social role of planning* 

	Some project managers think that they can manage planning on their own. They're commonly overworked and think that meetings are a waste of time.

	Even if staff really can manage their work for themselves, note that this regular meeting is also aimed at reassurance. Without it you can get into unduly stressful situations from:

	* feelings of overwork because they have lost sight of their priorities,

	* lack of feedback and tracking of the work actually completed,

	* an impression of poor organization if that hasn't been made explicit.

	So the social role of planning shouldn't be neglected. We have often experienced a background of stress in a company stemming from a lack of communication and planning.

Planning by time or by tasks?
-------------------------------

There are two major approaches to enterprise planning: planning by task and planning by time. You can manage both with Open ERP.

In planning by task, the project manager assigns tasks from the different projects to each employee over a given period. Employees then carry out precisely the work they've been assigned by the project manager.

Planning by time consists of allocating, for each employee, some time on each of the different projects for the period concerned. The tasks for each project are ordered by priority and can be directly assigned to a user or left unassigned. Each employee then chooses the task that he or she will do next, based on the plans and the relative priorities of the tasks.


	.. image::  images/service_planning_time.png
	   :align: center

*Monthly planning for work time of each employee*

The figure shows a monthly planning session where plans are being made for each employee to spend a number of days' work on various different projects.

In this time-focused planning approach, clients' priorities don't figure in the planning any more, but are explicit in the task list instead. So this approach helps you separate the planning of human resources on projects from the task prioritization within a project.

	.. note::  *Example Comparing the two planning methods* 

			To illustrate the difference between planning by time and planning by task, take the case of an IT project that's estimated to be around six months of work. This project is managed by iterative cycles of development of around a month and a presentation is made to the client at the end of each cycle to track the progress of the project. At this meeting you plan what must be carried out for the following month. At the end of the month the account manager for the project invoices the client for the work done on the project.

			Suppose that the project encounters a delay because it is more complex than expected. There are two ways of resolving the delay if you have no further resources: you can be late in your delivery of the planned functions or on time, but with fewer functions than planned. 

			If your planning is based on phases and tasks you'll report at the client meeting that it will take several weeks to complete everything that was planned for the current phase. Conversely, if you're planning by time you'll keep the meeting with the client to close the present development phase and plan the new one, but only be able to present part of the planned functionality.

			If the client is sensitive to delay, the first approach will cause acute unhappiness. You'll have to re-plan the project and all of its future phases to take account of that delay. Some problems are also likely to occur later with invoicing, because it will be difficult for you to invoice any work that has been completed late but hasn't yet been shown to the client.

			The second approach will require you to report on the functions that haven't been completed, and on how they would fit into a future planning phase. However that won't involve a break in the working time allocated to the project. You'd then generate two different lists: a staffing plan for the different projects, and the list of tasks prioritized for the client's project. This approach offers a number of advantages over the first one:

			* The client will have the choice of delaying the end of the project by planning an extra phase, or letting go of some minor functions to be able to deliver a final system more rapidly,

			* The client may re-plan the functions taking the new delay into account.

			* You'll be able to make the client gradually aware of the fact that project progress has come under pressure and that work is perhaps more complex than had been estimated at the outset. 

			* A delay in the delivery of several of the functions won't necessarily affect either monthly invoicing or project planning.

			Being able to separate human resource planning from task prioritization simplifies your management of complex issues, such as adjusting for employee holidays or handling the constantly changing priorities within projects.

Creating plans
---------------

\ ``report_analytic_planning``\   *Human Resources > Planning > Planning* 

On each planning line you should enter the user, the analytic account concerned, and the quantity of time allocated. The quantity will be expressed in hours or in days depending on the unit of measure used. For each line you can add a brief note about the work to be done.

Once the plan has been saved, use the other tabs of the planning form to check that the amount of time allocated to the employees or to the projects is right. The time allocated must correspond to the employees' employment contract, for example 37.5 hours per week. The forecast time for the project must match the commitments that you've made with client.

You should ideally complete all the planning for the current period. You can also complete some lines in the planning of future months – reserving resources on different project in response to your client commitments, for example This enables you to manage your available human resources for the months ahead.

Using planning well
---------------------

Plans can be printed and/or sent to employees by email. If you install the module \ ``board_project``\  , each employee can be given access to a dashboard that graphically shows the time allocated to him or her on a project and the time that's been worked so far. So each employee can decide which projects should be prioritized.

The employee then selects a task in the highest priority project. She ideally chooses either a task that has been directly assigned to her, or one which is high on the priority list that she's capable of completing, but is not yet directly assigned to anybody.

At the end of the period you can compare the duration of effective work on the different project to that of the initial estimate. Print the plan to obtain a comparison of the planned working time and the real time worked. 


	.. image::  images/planning_stat.png
	   :align: center

*Comparison of planned hours, worked hours and the productivity of employees by project*

You can also study several of your project's figures from the menu  *Human Resources > Reporting > Planning* .

Planning at all levels of the hierarchy
-----------------------------------------

To put planning in place across the whole company you can use a system of planning delegation. For this, install the module \ ``report_analytic_planning_delegate``\  .

When you've installed this module, the planning entry form changes to reflect the hierarchical structure of the company. To enter data into a plan line you can:

* assign time on a project to an employee,

* assign time on a project to a department manager for his whole team.

You can now allocate the working time on projects for the whole of a department, without having to detail each employee's tasks. Then when a department manager creates his own plan he will find what's required of his group by his management at the bottom of the form. At the top of the form there's the place for assigning project work in detail to each member of department.

If you don't have to plan time to work on a final draft you can do it on an analytic account that relies on child accounts. This means that you can create plans to meet top-level objectives of the senior management team and then cascade them down through the different departments to establish a time budget for each employee. Each manager then uses his own plans for managing his level in the hierarchy.

Treatment of expenses
=======================

Employee expenses are charges incurred on behalf of the company. The company then reimburses these expenses to the employee. The receipts encountered most frequently are:

* car travel, reimbursed per unit of distance (mile or kilometer),

* restaurant expenses, reimbursed based on the bill,

* other purchases, such as stationery and books, destined for the company but carried out by the employee.

An integrated process
-----------------------


	.. image::  images/service_expense_workflow.png
	   :align: center

*Process for dealing with expense reimbursements*

Expenses generated by employees are grouped into periods of a week or a month. At the end of the period the employee confirms all of her expenses and a summary sheet is sent to the department manager. The manager is responsible for approving all the expense requests generated by his team. The expenses sheet must be signed by the employee, who also attaches her receipts there.

Once the sheet has been approved by the head of department it is sent to accounts, who register the company's liability to the employee. Accounting can then pay this invoice and reimburse the employee who originally advanced the money.

Some receipts are for project expenses, so these can then be attached to an analytic account. The costs incurred are then added to the supplementary cost of the analytic account when the invoice is approved.

You often need to invoice expenses to a client, depending on the precise contract that's been negotiated. Traveling and subsistence expenses are generally handled this way. These can be recharged to the client at the the end of the month if the contract price has been negotiated plus expenses.

If you have to go through many steps to reclaim expenses, it can all quickly become too cumbersome, especially for those employees who claim large numbers of different expense lines. If you've got a good system that integrates the management of these claims, such as the one described, you can avoid many problems and subtly increase staff productivity.

If your systems handle expenses well then you can avoid significant losses by setting your terms of sale effectively. In fixed-price contracts, expense reimbursements are usually invoiced according to the actual expense. It's in your interests to systematize their treatment, and automate the process to the maximum, to recharge as much as you are contractually able.

Claiming expenses
-------------------

Install the module \ ``hr_expenses``\   to automate the management of expense claims. Users can then enter their expenses using the menu  *Human Resources > Expenses > My Expenses* .

\ ``Draft``\  

The various expenses accepted by the company must previously have been created using Open ERP's product form. You could, for example, create a product with the following parameters for the reimbursement of travel expenses by car at 0.25 per kilometer:

*  *Product* : \ ``Car travel``\  ,

*  *Unit of measure* : \ ``km``\  ,

*  *Standard Cost* : \ ``0.25``\  ,

*  *Sale price* : \ ``0.30``\  ,

*  *Type of product* : \ ``Service``\  .

The employee keeps her expenses sheet in the \ ``Draft``\   state while completing it throughout the period. At the end of the period (week or month) she can confirm her expense form using the  *Confirm*  button on the form. This puts it into the state \ ``Waiting for validation``\  . 

At the end of the period the department manager can access the list of expense forms waiting for approval using the menu  *Human resources > Expenses > All expenses > Expenses waiting for validation* . 

.. tip::   **Attention**  *Management of roles* 

	You must assign the role Human Resources – Expenses to a user to enable that user to approve these expenses. You'd generally assign this role only to those people responsible for projects or departments

	You can also assign the role Human Resources – Invoicing Expenses to users responsible for creating invoices. These roles may overlap (so the same person who approves your accounting group's expenses may also be responsible for creating invoices).

	To find out more about the management of roles look at chapter 13.

The department manager can then approve the expenses, which automatically creates a supplier invoice in the employee's name so that the employee can be reimbursed. An analytic account is coded onto each line of the invoice. When the invoice is confirmed, general and analytic accounting entries are automatically generated as they would be with any other invoice.

If you establish your invoicing on the basis of service time or analytic costs, the expense will automatically be recharged to the client when the client invoice is generated for services associated with the project.

Invoicing from timesheets lets you prepare your invoices all within the one integrated system - all the expenses and timesheets for a project's client.



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

