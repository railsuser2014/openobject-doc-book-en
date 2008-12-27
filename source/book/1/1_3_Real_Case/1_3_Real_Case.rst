

Developing a real case from purchase to sale: a complete workflow
###################################################################

Summary

* Use case

* Functional needs

* Installing and configuring modules

* Database setup

* Test of a purchase – sale workflow

Keywords

* sale

* purchase

* stock

* workflow

 *Now that you've discovered some of the many possibilities of Open ERP from a tour of the demonstration database, you'll develop a real case. An empty database provides the starting point for testing a classic workflow from product purchase to sale, completing your guided tour and your familiarization with Open ERP.* 


A database loaded with demonstration data is very useful for understanding Open ERP's general capabilities. But to explore Open ERP through a lens of your own company's needs you should start with an empty database. You'll work in this chapter on a minimal database containing no demonstration data so that there is no confusion about what you created. And you'll keep the database you've created so that you can build on it throughout the rest of this book.

You'll develop a real case through the following phases:

	#. Specify a real case.

	#. Describe the functional needs.

	#. Configure the system with the essential modules.

	#. Carry out the necessary data loading.

	#. Test the system with your database.

The case is deliberately extremely simple to provide you with a foundation for the more complex situations you'll handle in reality. Throughout this chapter it's assumed that you're accessing Open ERP through its web interface.

Use case
=========

Configure a system that enables you to:

* buy products from a supplier,

* stock the products in a warehouse,

* sell these products to a customer.

The system should support all aspects of invoicing, payments to suppliers and receipts from customers.

Functional requirements
=========================

For working out the business case you'll have to model:

* the suppliers,

* the customers,

* some products,

* inventory for despatch,

* a purchase order,

* a sale order,

* invoices,

* payments.

To test the system you'll need at least one supplier, one customer, one product, a warehouse, a minimal chart of accounts and a bank account.

Database creation
===================

Use the technique outlined in Chapter 1 to create a new database, \ ``openerp_ch03``\  . This database will be free of data and contain the least possible amount of functionality as a starting point. You'll need to know your super administrator password for this – or you'll have to find somebody who does have it to create this seed database. You won't be able to use the \ ``openerp_ch1``\   or \ ``openerp_ch2``\   databases that you might have created so far in this book because they both contain demonstration data.

Start the database creation process from the  *Database Administration*  page by clicking  *Create*  and then completing the following fields on the  *Create Database*  form:

*  *Super administrator password* : by default it's \ ``admin``\  , if you or your system administrator haven't changed it,

*  *New database name* : \ ``openerp_ch03``\  ,

*  *Load Demonstration Data*  checkbox: \ ``not checked``\  ,

*  *Default Language* : \ ``English``\  .

Installing and configuring modules
===================================

All of the functional needs are provided by core modules from Open ERP:

* product management (the  *product*  module),

* inventory control (the  *stock*  module),

* accounting and finance (the  *account*  module),

* purchase management (the  *purchase*  module),

* sales management (the  *sale*  module).

Connect to the new \ ``openerp_ch03``\   database as user \ ``admin``\   with its default password \ ``admin``\   (you might have to wait a few seconds before the system will allow you to connect if you've only just created it). Since this is the first time you've connected to it you'll have to go through the Setup wizard in steps:

	#.  *Select a profile*  select  *Profile* \ ``Minimal Profile``\  

	#.  *Define Main Company* and  *Report Header*  leave everything untouched on this page.

	#.  *Summary*  just click the  *Install* button.

	#.  *Installation done*  click  *Ok* 

Use the menu  *Administration > Modules Management > Modules > Uninstalled Modules*  to show the list of all modules that are registered within Open ERP but as yet uninstalled. Then:

	#. Enter \ ``product``\  into the  *Name* field and click  *Filter* to list the product module.

	#. Click the name \ ``product``\  in the list to display the product module in form view, rather than the list view that a search displays.

	#. Click the  *Install* button on the product module form.

	#. Click the  *Search* button at the top of the form to toggle back to the list view with search selection fields on it.

	#. Search for the sale module then select it, too, as you did with product, to show it in form view.

	#. Click the  *Dependencies* tab to see that you'll automatically be loading the \ ``product``\   \ ``stock``\  and \ ``mrp``\  modules along with the \ ``sale``\  module.

	#. Return to the  *Module* tab and then click its  *Install* button.

	#. Click  *Apply Upgrades* in the toolbar to the right.

	#. When the  *System Upgrade* form appears, review the list of Modules to update – it may be longer than you had expected, and now includes all the modules you need, because the dependencies themselves had their own dependencies.

	#. Click  *Start Upgrade*  wait for  *System Upgrade Done* to be displayed, then click  *Close* on that form.

	#. The main menu now displays all of the menu items that were loaded by the modules you installed.


Database setup
===============

You'll create all the elements in the database that you need to carry out the use case. These are specified in the functional requirements.

Personalizing the Main Company
-------------------------------

Start to personalize your database by renaming the  *Main Company*  from its default of \ ``Tiny sprl``\   to the name of your own company or (in this case) another example company. When you print standard documents such as quotations, orders and invoices you'll find this personalization information used in the document headers and footers. 

To do this, click  *Partners > Partners*  and click the name of the only company there, which is \ ``Tiny sprl``\  . This gives you a read-only view form view of the company, so make it editable by clicking the  *Edit*  button to the upper left of the form. 

.. tip::   **Web client**  *Editable form* 



	When toggling from the list view to the form view of an item, you can generally click its name in the list view to show a non-editable view or the pencil icon along the right-hand end of the line to open it in an editable view. You can toggle between editable and non-editable once you're in form view.

Change the following:

*  *Name* : \ ``Ambitious Plumbing Enterprises``\  ,

*  *Contact Name* : \ ``George Turnbull``\  .

and any other fields you like, such as the address and phone numbers, then  *Save* . This adds one Contact to the Partner, which is sufficient for the example.

From the  *Main Menu* , click  *Administration > Configuration > Base > Define Main Company*  and edit the entry there:

*  *Company Name* : \ ``AmbiPlum``\  ,

*  *Partner* : should already show \ ``Ambitious Plumbing Enterprises``\  ,

*  *Report Header* : \ ``Ambitious Plumbing Enterprises``\  ,

*  *Report Footer 1* : \ ``Best Plumbing Services, Great Prices``\  ,

*  *Report Footer 2* : \ ``Ambitious – our Registered Company Details``\  .

You can leave the currency at its default setting of \ ``EUR``\   for this example. Or you can change it in the Main Company ( *Administration > Configuration > Base > Main Company* ) and the two default Pricelists ( *Product > Pricelists > Pricelists* ) if you feel compelled to do that. 

.. tip::   **Alternative**  *Currency* 


	The examples in this book are in USD and EUR. You would use your main currency, perhaps CAD, CNY, GBP, or IDR, in their place.

Creating partner categories, partners and their contacts
---------------------------------------------------------

You'll now create a suppliers category and a customers category. Partner categories are useful for organizing groups of partners but have no special behavior that affects partners, so you can assign them as you like. Then you'll define one supplier and one customer, with a contact for each. 

To do this use the menu  *Partners > Configuration > Categories > Edit Categories* . Click  *New*  to open a new form for defining  *Partner Categories* . Define the two categories that follow by just entering their  *Category Name*  and saving them: 

* \ ``Suppliers``\  ,

* \ ``Customers``\  .

Then create two partners from the menu  *Partners > Partners* . Click on the  *New*  button to open a blank form and then add the following data for the first partner first:

*  *Name* : \ ``Plumbing Component Suppliers``\  ,

*  *Contact Name* : \ ``Jean Poolley``\  ,

*  *Address Type* : \ ``Default``\  ,

* add \ ``Suppliers``\   to the  *Categories*  field by selecting it from the Search List,

* then save the partner by clicking the  *Save*  button. 

.. tip::   **Note**  *Contact Types* 



	If you've recorded several contacts for the same partner you can specify which contact is used for various documents by specifying the Address Type.

	For example the delivery address can differ from the invoice address for a partner. If the Address Types are correctly assigned, then Open ERP can automatically select the appropriate address during the creation of the document – an invoice is addressed to the contact that's been assigned the Address Type of Invoice, otherwise to the Default address.

For the second partner, proceed just as you did for the first, with the following data:

*  *Name* : \ ``Smith and Offspring``\  ,

*  *Contact Name* : \ ``Stephen Smith``\  ,

*  *Address Type* : \ ``Default``\  .

Then add \ ``Customers``\   in the  *Categories*  field.  *Save*  the form. To check your work you can go to the menu  *Partners > Partner Categories*  and click on each category in turn to see the companies in the category.

.. tip::   **Note**  *Multiple Partner Categories* 



	If this partner was also a supplier then you'd add Suppliers to the categories as well, but there's no need to do so in this example. You can assign a partner to multiple categories at all levels of the hierarchy.

Creating products and their categories
---------------------------------------

Unlike partner categories and their assigned partners, product categories do have an effect on the products assigned to them – and a product may belong to only one category. Select the menu  *Products > Configuration > Product Categories*  and click  *New*  to get an empty form for defining a product category. 

Enter \ ``Radiators``\   in the  *Name*  field and, watching the  *Product Categories*  form closely, click  *Save* . You'll see that other fields, specifically those in the  *Accounting Properties*  section, have been automatically filled in with values of accounts and journals. These are the values that will affect products – equivalent fields in a product will take on these values if they, too, are blank when their form is saved. 

.. tip::   **Definition**  *Properties fields* 



	Properties have a rather unusual behavior. They're defined by parameters in the menu Administration > Custom > Properties, and they update fields only when a form is saved, and only when the fields are empty at the time the form is saved. You can manually override any of these properties as you need.

	Properties fields are used all over the Open ERP system and particularly extensively in a multi-company environment. There, property fields in a partner form can be populated with different values depending on the user's company.

	For example the payment conditions for a partner could differ depending on the company from which it's addressed.

.. tip::   **Definition**  *UOM* 



	UOM is an abbreviation for Unit of Measure. Open ERP manages multiple units of measure for each product: you can buy in tons and sell in kgs, for example. The conversion between each category is made automatically (so long as you have set up the conversion rate in the product form first).

.. tip::   **Advantage**  *Managing double units of measure* 



	The whole management of stock can be carried out with double units of measure (UOM and UOS – for Unit of Sale). For example an agro-food company can stock and sell ham by piece but buy and value it by weight. There's no direct relationship between these two units so a weighing operation has to be done.

	This functionality is crucial in the agro-food industry, and can be equally important in fabrication, chemicals and many other industries.

Now create a new product:

	#. Go to the  *Products > Products* menu and click  *New* 

	#. Create a product – type \ ``Titanium Alloy Radiator``\  in the  *Name* field,

	#. Click the Search icon to the right of the  *Category* field to select the  *Radiators* category,

	#. The  *Product Type* field should stay as \ ``Stockable Product``\   its default value. The fields  *Procure Method*   *Default UOM* and  *Purchase UOM* should also stay at their default values: in fact every other field remains untouched.

                .. image::  images/product.png
               	   :scale: 95
                

	#. Click on the  *Procurement* tab and enter \ ``57.50``\  into the  *Cost Price* field and \ ``132.50``\  into the  *List Price* field,

	#. Click the  *Properties* tab, then click  *Save* and observe that  *Inventory Properties* have taken on new values (just as the Accounting Properties did in the product category) but  *Accounting Properties* here remain empty. When product transactions occur, the Income and Expense accounts that you've just defined in the Product Category are used by the Product nless an account is specified here, directly in the product, to override that. 

	#. Once the product is saved it changes to a non-editable state. If you had entered data incorrectly or left a required field blank, the form would have stayed editable and you'd need to click from tab to tab to find a field colored red, with an error message below it, that would have to be correctly filled in.

Stock locations
-----------------

Click  *Inventory Control > Location Structure*  to see the hierarchy of stock locations. These locations have been defined by the minimal default data loaded when the database was created. You'll use this default structure in this example.

	#. From the  *Main Menu*  click on  *Inventory Control > Configuration > Locations* to reach a list view of the locations (not the tree view)

	#. Click on the name of a location, such as \ ``Company``\   to open a descriptive form view. Each location has a  *Location type*  and a  *Parent Location* that defines he hierarchical structure. An  *Inventory Account* can also be assigned to a location.

	#. From the  *Main Menu*  click  *Inventory Control > Configuration > Warehouses* to view a list of warehouses.

.. tip::   **Note**  *Valuation of stock* 



	If you want real-time stock valuation that tracks stock movements you must assign an account to each stock location. As product items are added to and taken from each location Open ERP generates an account entry for that location defined by the configuration of the product being moved – and a stock valuation based (in the current versions of Open ERP) on either Standard Cost or Average Price.

	For example, if you assign an account to the Supplier location you'll be able see the value of stock that you've taken from the supplier. Its contents should be valued in your accounts. Thus it manages inventory on consignment.

A Warehouse contains an input location, a stock location and an output location for sold products. You can associate a warehouse with a partner to give the warehouse an address. That doesn't have to be your own company (although it can be): you can easily specify another partner who may be holding stock on your behalf.

.. tip::   **Attention**  *Location Structure* 



	Each warehouse is composed of three locations: Input, Output and Stock. Your available stock is given by the contents of the Stock location.

	The Input location can be placed as a child of the Stock location, which means that when Stock is interrogated for product quantities, it also takes account of the contents of the Input location. The Output location must never be placed as a child of Stock, since items in Output, which are packed ready for customer shipment, should not be considered as available for sale elsewhere.

Setting up a chart of accounts
-------------------------------

You can set up a chart of accounts during the creation of a database, but for this exercise you'll start with the minimal chart that's built into the core of Tiny ERP (just a handful of required accounts without hierarchy, tax or subtotals). 

A number of account charts have been predefined for Open ERP, some of which meet the needs of national authorities (the number of those created for Open ERP is growing as various contributors create and freely publish them). You can take one of those without changing it if it's suitable, or you can take anything as your starting point and design a complete chart of accounts to meet your exact needs, including accounts for inventory, asset depreciation, equity and taxation.

You can also run multiple charts of accounts in parallel – so you can put all of your transaction accounts into several charts, with different arrangements for taxation and depreciation, aggregated differently for various needs.

Before you can use any chart of accounts for anything you need to specify a Fiscal Year. This defines the different time periods available for accounting transactions. To do so:

	#. Select  *Financial Management > Configuration > Periods > Fiscal Years* and click  *New* to open a blank  *Fiscal Year* definition form.

	#. Give a name to that  *Fiscal Year* (such as inancial Year 2008 and a  *Code* (Y2008, then select the  *Start date* and  *End date*  which should be a year apart and (for this example) straddle today's date.

	#. Then click on one of the buttons  *Create Monthly Periods* or  *Create 3 Months Periods* to create an appropriate set of periods for the fiscal year, as shown in the figure below.  *Save* this.


.. image::  images/def_fiscal_year_tab.png
   :align: center

*Defining a fiscal year and the accounting periods within it*


Click  *Financial Management > Charts > Charts of Accounts*  and then click  *Open Charts*  on the  *Fiscal Year*  that you've just created to see a hierarchical structure of the accounts. You can click on the expand/collapse icon of the top tree node to show the detail of this minimal chart.

Make a backup of the database
-------------------------------

If you know the super-administrator password, make a backup of your database using the procedure described at the very end of Chapter 1. Then restore it to a new database: \ ``testing``\  .

This operation enables you to test the new configuration on \ ``testing``\   so that you can be sure everything works as designed. Then if the tests are successful you can make a new database from \ ``openerp_ch03``\  , perhaps called \ ``production``\  , for your real work.

From here on, connect to this new \ ``testing``\   database logged in as \ ``admin``\   if you can. If you have to make corrections, do that on \ ``openerp_ch03``\   and copy it to a new \ ``testing``\   database to continue checking it.

Or you can just continue working with the \ ``openerp_ch03``\   database to get through this chapter. You can recreate \ ``openerp_ch03``\   quite quickly if something goes wrong and you can't recover from it but, again, you'd need to know your super-administrator password for that.

Testing a Purchase-Sale workflow
=================================

To familiarize yourself with the system workflow you'll test a purchase-sale workflow in two phases. 

The first consists of product purchase, which requires the following operations:

	#. Place a purchase order with Plumbing Component Suppliers for 10 Titanium Alloy Radiators at a unit price of 60.00.

	#. Receive these products at your Goods In.

	#. Generate a purchase invoice.

	#. Pay your supplier.

Following this, you'll sell some of these products, using this sequence:

	#. Receive a sales order for 6 Titanium Alloy Radiators from Smith and Sons, sold at a unit price of 130.00.

	#. Despatch the products.

	#. Invoice the customer.

	#. Receive the payment.

Purchase Order
---------------

To place a Purchase Order with your supplier, use the menu  *Purchase Management > Purchase Order*  for a new Purchase Order form.

Complete the following fields:

*  *Warehouse* : \ ``Warehouse``\  . Although this is not a required field, the selection here automatically fills in the required field  *Delivery Destination*  on the  *Purchase Shippings*  tab.

*  *Partner* : \ ``Plumbing Component Suppliers``\  .

As you complete the  *Partner*  field, Open ERP automatically completes the  *Address*  field and the  *Price List*  field from information it takes out of the Partner record. Then click on the  *Save Parent and Create New Record*  icon to the right of the  *Order Line*  field. This automatically saves the body of the  *Purchase Order* , and changes to a  *Create New Record*  icon. Click that to open the  *Purchase Order Line*  window.

Enter the following information

*  *Product* : \ ``Titanium Alloy Radiator``\   - type in part of this name then click the  *Search / Open a resource*  icon at the end of the line to complete it,

When you've selected a product on the product line, Open ERP automatically completes the following fields from information it finds in the Product record:

*  *Product UOM* : the unit of measure for this product,

*  *Description* : the detailed description of the product,

*  *Scheduled date* : based on the product lead time,

*  *Unit price* : the unit price of the product,

*  *Analytic account* : if any account is specified then it will appear on the order line,

*  *Taxes* : applicable taxes defined in the partner, if specified, otherwise in the product, if specified.

You can edit any of these fields to suit the requirements of the purchase order at the time of entry. Change the  *Unit Price*  to \ ``56.00``\  .

Also enter:

*  *Quantity* : \ ``10``\  .

 *Save*  the order line and close the  *Purchase Order Line*  window by clicking the  *Close*  button. You can then confirm the whole one-line order by clicking  *Save* , which makes the form non-editable. It's now in a state of \ ``Request for Quotation``\  , so click  *Confirm Purchase Order* , which corresponds to an approval from a manager or from Accounts within your own company and moves the order into \ ``Confirmed``\   state.

Finally click  *Approved by Supplier*  to indicate the supplier's acknowledgment of the order. The order becomes \ ``Approved``\  . If you click the  *Purchase Shippings*  tab you'll see the  *Picking List*  that has been created ready for your Goods In department to use.

.. tip::   **Attention**  *Visibility of a window* 



	Sometimes a child window, such as the Purchase Order Line window, loses focus and disappears behind the main window. If a window doesn't open as you expect, check that it's not hiding behind the main window: do this by minimizing the main window to your task bar.

Receiving Goods
-----------------

After confirming the order you'd wait for the delivery of the products from your supplier. Typically this would be somebody in Stores rather than Purchasing, who would:

	#. Open the menu  *Inventory Control > Packing Lists > Getting Goods > Packings to be Received*  using the expand/collapse icon rather than clicking directly on  *Packing Lists* 

	#. When the  *Packing list* window appears, select the name of the entry in the list (\ ``IN:1``\   to display the Packing List itself – you'd usually do a search for the supplier name or order number in a list that was larger than this – then click  *Validate* to load the  *Make Packing* form.

	#. Click  *Make Picking* to indicate that you're receiving the whole quantity of 10 units.

At this point you've accepted 10 units into your company, in a location defined by the Warehouse that you specified near the top of your Purchase Order.

To check actual stock levels, use the menu  *Inventory Control > Location Structure* , find \ ``Stock``\   in the hierarchy using the expand/collapse controls to make your way through the tree and click it. That will show everything in the \ ``Stock``\   location and below it – including  *Real stock*  (the actual quantity recorded in that location and below it) and  *Virtual stock*  (the quantities expected in future when all receipts and despatches have been made) – both \ ``10``\   in this case.

Alternatively you could click the top-level \ ``Locations``\   line to highlight it (not the \ ``Locations``\   text itself), and then click the  *Print*  button to the top right of the form to test the available different reports (such as  *Lots by Location* ). You'll see that you've now got \ ``10``\   pieces of \ ``Titanium Alloy Radiator``\   in the location \ ``Input``\   and \ ``-10``\   pieces in the location \ ``Suppliers``\   as shown in the next Figure.


.. image::  images/lots_by_location_pdf.png
   :align: center

*List of products and their stock levels*


.. tip::   **Web client**  *Returning to Open ERP after printing PDF reports* 



	When you're using the web client, documents such as this are not part of the standard web page but are generated in PDF format, which you can print or attach to email or save on disk. So you don't get the standard Open ERP navigation links on these pages.

	Open ERP is not fully consistent in the display of these pages in version 4.2.2, so the PDF page is not brought up in a new tab or window as it should be (and as it is in other areas of Open ERP), but replaces the standard Open ERP web-format pages.

	Once you've finished looking at the PDF document you'll have a strong temptation to just close the window, but that'll completely close Open ERP for you! Instead, click the Back button in your web browser to return to Open ERP.

.. tip::   **Advantage**  *Traceability in double-entry* 



	Open ERP operates a double-entry stock transfer scheme similar to double-entry accounting. Because of this you can carry out various analyses of stock levels in your warehouse, along with the corresponding levels in virtual locations at your supplier. Supplier locations show negative levels once you've received goods in your company, as you can see in the Figure.

Control of purchase invoices
-----------------------------

When you've received an invoice from your supplier (which would usually be your Accounts department) go to the menu  *Financial Management > Invoices > Supplier Invoice > Draft Supplier Invoices*  to open a list of supplier invoices waiting for receipt (you'll have to use the expand/collapse icon on  *Supplier Invoice*  rather than click the text, which would create a new Invoice). These invoices enable your Accounts Department to match the the price and quantities ordered against the price and quantities on the supplier's invoice – it's not uncommon to receive an invoice showing details more favourable to the supplier than those agreed at the time of purchase.

In this example, you created an invoice automatically when you confirmed the supplier's Purchase Order. That's because the  *Invoicing Control*  field on the order was set to \ ``On Order``\   (the default option). Other options enable you to create invoices at the time of receiving goods or manually. The initial state of an invoice is \ ``Draft``\  .

Now click the invoice for your order \ ``PO/001``\   to display its contents. You can compare the goods that you've recorded there with the invoice received from your supplier. If there's a difference it's possible to change the order lines to, for example, add a delivery charge. Click  *Validate*  to confirm the invoice and put it into the \ ``Open``\   state.

Accounting entries are generated automatically once the invoice is validated. To see the effects on your chart of accounts, use the menu  *Financial Management > Charts > Chart of Accounts* .

Paying the supplier
---------------------

Select the menu  *Financial Management > Invoices > Supplier Invoices > Open Supplier Invoices*  to obtain a list of supplier invoices that haven't yet been paid. Click the  *Edit*  (pencil) icon to the right end of the line for the invoice derived from \ ``PO/001``\   to open the invoice form in editable mode. In practice you'd search for the invoice by order number or, more generally, for invoices nearing their payment date.

Click  *Pay Invoice*  in the toolbar to the right of the form, which opens a Window with a description of the payment. Select \ ``Bank Journal``\   in the  *Journal*  field. Then click  *Pay Invoice*  to the top left of the form, which carries out the payment action within Open ERP and returns you to the main menu.

.. tip::   **Comment**  *Payment of an invoice* 



	The method described here is for companies that don't use their accounting system to pay bills – just to record them. If you're using the accounting module fully other, more efficient, methods let you manage payments, such as entering account statements, reconciling paperwork, using tools for preparing payments, interfacing with banks.

You can monitor the accounting impact of paying the invoice through the chart of accounts available from the menu  *Financial Management > Charts > Chart of Accounts* . Open ERP automatically creates accounting entries from the payment and can reconcile the payment to the invoice.

From Sales Proposal to Sales Order
-----------------------------------

In Open ERP, sales proposals and sales orders are managed using documents that are based on the same common functionality as purchase orders, so you'll recognize the following documents in general but notice changes to their detail and to their workflows. To create a new sales proposal, use the menu  *Sales Management > Sales Order*  which creates a new order in a state of \ ``Quotation``\  , then:

	#. Select \ ``Default Shop``\  in the  *Shop* field. The shop is linked to a warehouse, which defines the location that you'll use to despatch goods from.

	#. Select the  *Partner* \ ``Smith and Sons``\   This has the effect of automatically completing several other fields:  *Ordering Contact*   *Invoice Address*   *Shipping Address* and the  *Pricelist* \ ``Default Sale Pricelist``\   They're all only defaults so these fields can be modified as you need.


	        .. image::  images/order.png
        	   :align: center

	#. Click the  *Save Parent and Create new record* icon to the right of the  *Sales Order Lines* field. It saves the main order form and becomes a new  *Create new record* icon. Click that to open a  *Sales Order Lines* window.

	#. Select the product \ ``Titanium Alloy Radiator``\   Although the  *Product* field isn't itself required, it's used by Open ERP to select the specific product so that several other fields can be automatically completed on the order line of the proposal, such s:  *Description*   *Product UOM*   *Unit Price*   *Delivery Delay* and  *Taxes* 

	#. Change the  *Quantity* to \ ``6``\  and the  *Unit Price* to \ ``130.00``\   Then click  *Save* and the line appears on the quotation form. A blank order line form reappears so that you can enter another line, but it's enough now just to click  *Close* to return to the order form.

	#. On the  *Other data* tab of this Sales Order select a  *Shipping Policy* of \ ``Automatic Invoice after Delivery``\  from the dropdown menu list.

	#. Return to the first tab  *Sale Order* and validate the document by clicking  *Confirm Order*  which calculates prices and the changes the order's state from \ ``Quotation``\  to \ ``In Progress``\   If you were in negotiation with the prospective customer you'd keep clicking  *Compute* and  *Save*  keeping the document in \ ``Quotation``\  state for as long as necessary.

	#. In the last tab of the order,  *History*  you can see the  *Picking List* that's been created and you'll be able to see any invoices that relate to this order when they're generated.

From the  *Main Menu*  click  *Products > Products*  to display a list of products: just the one, \ ``Titanium Alloy Radiator``\  , currently exists in this example. Its  *Real Stock*  still shows \ ``10.00``\   but its  *Virtual Stock*  now shows \ ``4.00``\   to reflect the new future requirement of 6 units for despatch.

Preparing goods for despatch to customers
-------------------------------------------

The stores manager selects the menu  *Inventory Control > Packing Lists > Sending Goods > Confirmed Packings Awaiting Assignation*  to get a list of orders to despatch. In this example there's only one, \ ``OUT:1``\  , so click the text to open the  *Picking List* . 

.. tip::   **Advice**  *Calculating Requirements* 



	At the moment your Sales Order is waiting for products to be reserved to fulfil it. A stock reservation activity takes place periodically to calculate the needs, which also takes customer priorities into account. The calculation can be started from the menu Production > Calculate Requirements. Running this automatically reserves products. 

	If you don't want to have to work out your stock needs but have a lean workflow you can install the mrp_jit (Just In Time) module.

Although Open ERP has automatically been made aware that items on this order will need to be despatched, it has not yet assigned any specific items from any location to fulfil it. It's ready to move \ ``6.00``\  \ ``Titanium Alloy Radiators``\   from the  *Stock*  location to the  *Output*  location (which were defined by the Sale Shop in the Sales Order), so start this process by clicking  *Assign* . The  *Move*  line has now changed from the \ ``Confirmed``\   state to the \ ``Assigned``\   state.

Create a  *Packing List*  document by clicking the  *Packing List*  button in the  *Reports*  section of the toolbar to the right of the form, and also a  *Despatch Note*  by clicking the  *Delivery Report*  button there. These are both created in a new window or tab of your browser so they can be printed off and then closed.

Now click  *Validate*  on the  *Packing List*  to mark the move that you'd be making physically in your Stores. A  *Make Packing*  form appears enabling you to transfer \ ``6``\   units (or another number if you choose) between locations and pack them into a package in the process. Click  *Make Packing*  to the top left of the form to do the transfer. The  *Move*  line has now changed state to \ ``Done``\  .

The goods are now in your Output Bay, which had been defined by default in Open ERP as  *Output* , as a single package with a  *Lot Number*  of \ ``OUT:1``\  . 

To register when a carrier picks up the package, use the menu  *Inventory Control > Delivery Order > Delivery Orders to Process* . Select the appropriate line \ ``OUT:1``\   to open the  *Stock Move*  form, then click  *Move Lot* . Its state changes to \ ``Moved``\  . Packing is defined by Sales Orders so if you pack fewer packages than are on order Open ERP automatically manages the remainder for future delivery. 

To analyze stock movements that you've made during these operations use the following steps:

	#. Select menu  *Inventory Control > Locations Structure* 

	#. Select the first line by clicking somewhere along it (but don't click on the \ ``Locations``\  text itself) then click on the  *Print* icon above the list further over to the right.

	#. Select the report  *Lots by location* and click the  *OK* button to get a detailed report of Stocks for each location. You should see the following data:

	- -10 in the *Suppliers* location,

	- 6 in the *Customers* location,

	- 4 in your company's *Input* location.


.. tip::   **Note**  *Location Hierarchy* 

	The 10 Titanium Alloy Radiators can be found in the Input location after they've been received, instead of the location Stock. But they're still considered as being part of stock because Input is a child location of Stock.

	If you want to put a Quality Control station at Goods In, all you need to do is put Input up to the same level as Stock. Then you'd manually move items from Input to Stock when they pass your Goods In checks.

Invoicing Goods
-----------------

Use the menu  *Financial Management > Invoices > Customer Invoice > Draft Customer Invoices*  to open a list of invoices generated by Open ERP. These are in the \ ``Draft``\   state, which means that they don't yet have any presence in the accounting system. You'll find a draft invoice has been created for the order \ ``SO/001``\   once you have despatched the goods because you'd selected \ ``Automatic Invoice after Delivery``\  .

Once you confirm an invoice, Open ERP assigns it a unique number, and all of the corresponding accounting entries are generated. So open the invoice and click  *Create*  to do that and move the invoice into an \ ``Open``\   state.

You can send your customer the invoice for payment at this stage. Click  *Invoices*  from the  *Reports*  section of the toolbar at the right of the form to get a PDF document that can be printed or emailed to the customer.

You can also attach the PDF document to the Open ERP invoice record. Save the PDF somewhere convenient on your PC (such as on your desktop). Then click the  *Add an attachment to this resource*  button to the top right of the invoice form (it looks like a clipboard). Browse to the file you just saved (\ ``record.pdf``\   if you didn't change its name) from the  *Attachments*  dialog box that pops up, and  *Close*  the dialog box. This gives you a permanent non-editable record of your invoice on the Open ERP system.

Review your chart of accounts to check the impact of these activities on your accounting. You'll see the new revenue line from the invoice.

Customer Payment
-----------------

Registering an invoice payment by a customer is essentially the same as the process of paying a supplier. From the menu  *Financial Management > Invoices > Customer Invoice > Open Customer Invoices* , click the name of the invoice that you want to mark as paid:

	#. Use the  *Pay Invoice* button in the  *Action* section of the toolbar at the right to open a window that enables you to register the payment.

	#. Select the  *Journal* \ ``Bank Journal``\  and click  *Pay Invoice*  The invoice is then marked as paid, and you're returned to the  *Main Menu* 


.. image::  images/familiarization_invoice.png
   :align: center

*A screen showing the invoice to be paid*


Check your Chart of Accounts as before to see that you now have a healthy bank balance in the \ ``Petty Cash``\   account.



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

