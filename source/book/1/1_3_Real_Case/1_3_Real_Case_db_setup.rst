
Database setup
==============

You'll create all the elements in the database that you need to carry out the use case. These are
specified in the functional requirements.

.. index::
   single: accounts; configuring
   
Configuring Accounts
--------------------

You need to start off with a minimal set of accounts, and to do that you will need a couple of
account types. You can structure your accounts into a chart at any time (and, in fact, you can
structure them into several additional charts at the same time as you'll see in the chapter
:ref:`ch-configacct`), so you don't need to be concerned unduly about structure.

.. index::
   single: account types

Account Types
^^^^^^^^^^^^^

Create account types using :menuselection:`Financial Management --> Configuration --> 
Financial Accounting --> Financial Accounts --> Account Types` and then clicking the
:guilabel:`New` button. You'll need the following four types, the first of which is shown
in figure :ref:`fig-oech03accty`.

============== ======== ========  =============== =============== ===============
Acc. Type Name Code     Sequence  Sign on Reports Deferral Method Partner Account
============== ======== ========  =============== =============== ===============
View           view     5         Positive        None            unchecked
Income         income   5         Positive        Unreconciled    unchecked         
Expense        expense  5         Positive        Unreconciled    unchecked
Cash           cash     5         Positive        Balance         unchecked
============== ======== ========  =============== =============== ===============


.. _fig-oech03accty:

.. figure::  images/openerp_ch03_acctype.png
   :align: center
   :scale: 80

   *New Account Type*
   
Accounts
^^^^^^^^

Create accounts using :menuselection:`Financial Management --> Configuration --> 
Financial Accounting --> Financial Accounts --> List of Accounts` and then clicking the
:guilabel:`New` button. 

You need accounts to handle the purchase and sales orders that haven't yet been paid,
two more for the receipt and shipping of goods, and one for the payment and receipt of funds. 
And one 'organizing' account that's just a view of the other five. So
you'll need the following six accounts, one of which is shown
in :ref:`fig-oech03accts`.

============= ==== ============= =============== ============ =========
Name          Code Internal Type Parent          Account Type Reconcile
============= ==== ============= =============== ============ =========
Minimal Chart 0    View                          View         unchecked
Payable       AP   Payable       0 Minimal Chart Expense      checked
Receivable    AR   Receivable    0 Minimal Chart Income       checked
Cash          C    Others        0 Minimal Chart Cash         unchecked
Purchases     P    Others        0 Minimal Chart Expense      unchecked
Sales         S    Others        0 Minimal Chart Income       unchecked
============= ==== ============= =============== ============ =========

.. _fig-oech03accts:

.. figure::  images/openerp_ch03_accts.png
   :align: center
   :scale: 80

   *New Account*

The :guilabel:`Account Type` entry is taken from the list of types that you just created.
Although it looks a bit like a text box, it doesn't behave in quite the same way.
A single :kbd:`Del` or :kbd:`Backspace` keystroke is all you need to delete the whole text,
and when you type the name (or part of the name) you still need to associate that text
with the entry by clicking the :guilabel:`Search` icon to the right of the field.

.. index::
   single: properties; defining

Properties
^^^^^^^^^^

You now define some default properties so that you don't have to think about
which account is used for which transaction every time you do something.
The main new properties are the four that associate accounts payable and receivable
to partners, and expenses and income to product categories.

Create properties using :menuselection:`Administration --> Configuration --> 
Properties --> Default Properties` and then clicking the :guilabel:`New` button. 

============================== ========= ================== =============================== ===============
Name                           Company   Fields             Value                           Parent Resource
============================== ========= ================== =============================== ===============
property_account_payable       Tiny sprl Account Payable    (account.account) AP Payable    (None) 
property_account_receivable    Tiny sprl Account Receivable (account.account) AR Receivable (None) 
property_account_expense_categ Tiny sprl Expense Account    (account.account) P Purchases   (None) 
property_account_income_categ  Tiny sprl Income Account     (account.account) S Sales       (None) 
============================== ========= ================== =============================== ===============

.. tip:: Mistakes in configuring accounts and properties

   It's easy to make mistakes in configuring the accounts and their properties, but the consequences
   are not immediately obvious. You'll mostly discover mistakes when trying to make a Purchase or
   Sale Order (see later, for example, :ref:`sect-PO`), where the accounts are required fields or,
   if you're diligent, when you set up Partners. 
   
   If you configure them correctly at this stage then fields will be completed automatically and you'll
   never know a thing. If you don't configure all this correctly then you won't be able to save the
   order form until you have corrected the problem or until you manually set the accounts. 
   
   Since this configuration is quite tedious you'd be best finding a certified Chart of Accounts that
   that has already been set up to meet your needs, if you can find one.

.. index::
   single: journals; configuring

Configuring Journals
--------------------

You'll also need to configure some journals, which are used to record the transactions from one account
to another when invoices are raised and then paid. Create journals from the menu
:menuselection:`Financial Management --> Configuration --> 
Financial Accounting --> Financial Journals` and then clicking the :guilabel:`New` button. 

===================== ==== ============= ================= ================ ===================== ======================
Journal Name          Code Type          View              Entry Sequence   Default Debit Account Default Credit Account
===================== ==== ============= ================= ================ ===================== ======================
Purchase Journal      PUJ  Purchase      Journal View      Purchase Journal P Purchases           P Purchases
Sale Journal          SAJ  Sale          Journal View      Sale Journal     S Sales               S Sales
Bank Journal          BNK  Cash          Cash Journal View Account Journal  C Cash                C Cash
===================== ==== ============= ================= ================ ===================== ======================

.. tip:: Mistakes in configuring journals

   It's easy to make mistakes in configuring the journals, too, and the consequences
   are also not immediately obvious. You'll mostly discover mistakes when creating an invoice
   (which happens at different points in the process depending on your configuration).
   In this example, validating a Purchase Order creates a draft invoice 
   (see later, again for example, :ref:`sect-PO`), where a journal is required. 
   
   As with accounts and properties, if you configure them correctly at this stage then 
   the fields will be completed automatically and you'll never know a thing. 
   If you don't configure all this correctly then there will be errors with the
   order form or corresponding draft invoice
   until you have corrected the problem or until you manually set the journal. 

.. _sect-ConfiCo:

.. index::
   single: Main Company; configuring

Configuring the Main Company
----------------------------

Start to configure your database by renaming the :guilabel:`Main Company` from its default of \
``Tiny sprl``\   to the name of your own company or (in this case) another example company. When you
print standard documents such as quotations, orders and invoices you'll find this configuration
information used in the document headers and footers.

To do this, click :menuselection:`Partners --> Partners`  and click the name of the only company
there, which is \ ``Tiny sprl``\  . This gives you a read-only view form view of the company, so
make it editable by clicking the :guilabel:`Edit` button to the upper left of the form.

.. tip:: Editable form in the web client

	When toggling from the list view to the form view of an item, you can generally click its name in
	the list view to show a non-editable view or the pencil icon by the left-hand edge of the line to
	open it in an editable view. You can toggle between editable and non-editable once you're in form
	view.

Change the following:

*  :guilabel:`Name` : \ ``Ambitious Plumbing Enterprises``\  ,

*  :guilabel:`Contact Name` : \ ``George Turnbull``\  .

Before you save this, look at the partner's accounting setup by clicking the fifth tab
:guilabel:`Accounting`. The fields :guilabel:`Account Receivable` and :guilabel:`Account Payable`
have account values in them that were taken from the account properties you just created.
You don't have to accept those values: you can enter any suitable account you like at this stage, 
although Open ERP constrains the selection to ones that make accounting sense.

Back at the first tab, :guilabel:`General`change  any other fields you like, 
such as the address and phone numbers, then :guilabel:`Save`. This
changes one Contact for the Partner, which is sufficient for the example.

From the :guilabel:`MAIN MENU`, click :menuselection:`Administration --> Users --> Company Structure -->
Companies` and edit the only entry there:

*  :guilabel:`Company Name` : \ ``AmbiPlum``\  ,

*  :guilabel:`Partner` : should already show \ ``Ambitious Plumbing Enterprises``\  ,

*  :guilabel:`Report Header` : \ ``Ambitious Plumbing``\  ,

*  :guilabel:`Report Footer 1` : \ ``Best Plumbing Services, Great Prices``\  ,

*  :guilabel:`Report Footer 2` : \ ``Ambitious – our Registered Company Details``\  .

Figure :ref:`fig-oech03co` shows the effect of this.
You can also change various other company-wide parameters for reports and scheduling in the other tabs,
and you can upload a company logo of a specific size for the reports. Click :guilabel:`Save` to store this.

.. _fig-oech03co:

.. figure::  images/openerp_ch03_co.png
   :align: center
   :scale: 75

   *Changing company details*

You can leave the currency at its default setting of \ ``EUR``\ for this example. Or you can
change it in this Company and the two default Pricelists (:menuselection:`Products --> Pricelists --> Pricelists`) if
you feel compelled to do that.

.. note::  Currency

	The examples in this book are in USD and EUR. You, the reader, could use your home currency
	(perhaps CAD, CNY, GBP, or IDR) in their place.

.. index::
   single: partner
   pair: partner; category
   pair: partner; contact

Creating partner categories, partners and their contacts
--------------------------------------------------------

You'll now create a suppliers category and a customers category. Partner categories are useful for
organizing groups of partners but have no special behavior that affects partners, so you can assign
them as you like. Then you'll define one supplier and one customer, with a contact for each.

To do this use the menu :menuselection:`Partners --> Configuration --> Partner Categories`and
click :guilabel:`New` to open a new form for defining :guilabel:`Partner Categories`.
Define the two categories that follow by just entering their :guilabel:`Category Name` and saving
them:

* \ ``Suppliers``\  ,

* \ ``Customers``\  .

Then create two partners from the menu :menuselection:`Partners --> Partners`. Click on the
:guilabel:`New` button to open a blank form and then add the following data for the first partner
first:

* :guilabel:`Name` : \ ``Plumbing Component Suppliers``\  ,

* :guilabel:`Customer` checkbox : \ ``unchecked``\  ,

* :guilabel:`Supplier` checkbox : \ ``checked``\  ,

* :guilabel:`Contact Name` : \ ``Jean Poolley``\  ,

* :guilabel:`Address Type` : \ ``Default``\  ,

* add \ ``Suppliers``\   to the :guilabel:`Categories` field by selecting it from the Search List,

* then save the partner by clicking the :guilabel:`Save` button. 

Figure :ref:`fig-oech03part` shows the result. 

.. _fig-oech03part:

.. figure::  images/openerp_03_part.png
   :align: center
   :scale: 80

   *New Partner Form*

.. note:: Contact Types

	If you've recorded several contacts for the same partner you can specify which contact is used for
	various documents by specifying the Address Type.

	For example the delivery address can differ from the invoice address for a partner. If the Address
	Types are correctly assigned, then Open ERP can automatically select the appropriate address
	during the creation of the document – an invoice is addressed to the contact that's been assigned
	the Address Type of Invoice, otherwise to the Default address.

For the second partner, proceed just as you did for the first, with the following data:

* :guilabel:`Name` : \ ``Smith and Offspring``\ ,

* :guilabel:`Customer` checkbox : \ ``checked``\ ,

* :guilabel:`Supplier` checkbox : \ ``unchecked``\ ,

* :guilabel:`Contact Name` : \ ``Stephen Smith``\ ,

* :guilabel:`Address Type` : \ ``Default``\ .

Then add \ ``Customers``\   in the :guilabel:`Categories` field. :guilabel:`Save` the form. To check
your work you can go to the menu :menuselection:`Partners --> Partner Categories` and click on each
category in turn to see the companies in the category.

.. note:: Multiple Partner Categories

	If this partner was also a supplier then you'd add Suppliers to the categories as well, but there's
	no need to do so in this example. You can assign a partner to multiple categories at all levels of
	the hierarchy.

.. index::
   single: product
   pair: product; category

Creating products and their categories
--------------------------------------

Unlike partner categories and their assigned partners, product categories do have an effect on the
products assigned to them – and a product may belong to only one category. Select the menu
:menuselection:`Products --> Configuration --> Product Categories` and click :guilabel:`New` to get
an empty form for defining a product category.

Enter \ ``Radiators``\   in the :guilabel:`Name` field. You'll see that other fields, specifically those
in the :guilabel:`Accounting Properties` section, have been automatically filled in with values of
accounts and journals. These are the values that will affect products – equivalent fields in a
product will take on these values if they, too, are blank when their form is saved.
Click :guilabel:`Save`.

.. note:: Properties fields

	Properties have a rather unusual behavior. They're defined by parameters in the menus in 
	:menuselection:`Administration --> Configuration --> Properties`, and they update fields only when a form
	is saved, and only when the fields are empty at the time the form is saved. You can manually
	override any of these properties as you need.

	Properties fields are used all over the Open ERP system and particularly extensively in a multi-
	company environment. There, property fields in a partner form can be populated with different
	values depending on the user's company.

	For example the payment conditions for a partner could differ depending on the company from which
	it's addressed.

.. note:: UOM

	UOM is an abbreviation for Unit of Measure. Open ERP manages multiple units of measure for each
	product: you can buy in tons and sell in kgs, for example. The conversion between each category is
	made automatically (so long as you have set up the conversion rate in the product form first).

.. tip::  Managing double units of measure

	The whole management of stock can be carried out with double units of measure (UOM and UOS – for
	Unit of Sale). For example an agro-food company can stock and sell ham by piece but buy and value
	it by weight. There's no direct relationship between these two units so a weighing operation has to
	be done.

	This functionality is crucial in the agro-food industry, and can be equally important in
	fabrication, chemicals and many other industries.

Now create a new product:

#.	Go to the :menuselection:`Products --> Products` menu and click :guilabel:`New`.

#.	Create a product – type \ ``Titanium Alloy Radiator``\  in the :guilabel:`Name` field.

#.	Click the :guilabel:`Search` icon to the right of the :guilabel:`Category` field to select the
	:guilabel:`Radiators` category.

#.	The :guilabel:`Product Type` field should stay as \ ``Stockable Product``\   its default value.
	The fields :guilabel:`Procure Method`, :guilabel:`Supply Method`, :guilabel:`Default UOM`, 
	and :guilabel:`Purchase UOM` should
	also stay at their default values: in fact every other field in this tab remains untouched.

	.. figure:: images/product.png
	   :align: center
	   :scale: 75
           
	   *Product Form*

#.	Click on the :guilabel:`Prices & Suppliers` tab and enter \ ``57.50``\  into the :guilabel:`Cost Price`
	field and \ ``132.50``\  into the :guilabel:`Sale Price` field.

#.	Click the :guilabel:`Accounting` tab, then click :guilabel:`Save` and observe that
	:guilabel:`Accounting Properties` here remain empty. When product
	transactions occur, the Income and Expense accounts that you've just defined in the Product
	Category are used by the Product unless an account is specified here, directly in the product, to
	override that.

#.	Once the product is saved it changes to a non-editable state. If you had entered data
	incorrectly or left a required field blank, the form would have stayed editable and you'd need to
	click from tab to tab to find a field colored red, with an error message below it, that would have
	to be correctly filled in.

.. index::
   single: stock; location

Stock locations
---------------

Click :menuselection:`Stock Management --> Stock Locations Structure` to see the hierarchy of stock
locations. These locations have been defined by the minimal default data loaded when the database
was created. You'll use this default structure in this example.

Open ERP has three predefined top-level location types , ``Physical Locations`` and ``Partner Locations``
that act as their names suggest, and ``Virtual Locations`` that are used by Open ERP for its own purposes.

	#.	From the :guilabel:`Main Menu` click on :menuselection:`Stock Management --> Configuration -->
		Locations` to reach a list view of the locations (not the tree view).

	#.	Click on the name of a location, such as \ ``Physical Locations/Tiny SPRL``\  to open a descriptive form view. Each
		location has a :guilabel:`Location type` and a :guilabel:`Parent Location` that defines the hierarchical structure.
		An :guilabel:`Inventory Account` can also be assigned to a location. While you're here you should change 
		the location's name to Ambitious Plumbing Enterprises, since it was named before you changed the
		company name.

	#.	From the :menuselection:`Main Menu` click :menuselection:`Stock Management --> Configuration
		--> Warehouses` to view a list of warehouses. There's only the one at the moment, which
		should also be renamed from ``Tiny SPRL`` to ``Ambitious Plumbing Enterprises``.

.. todo:: Get this, below, right!

.. tip:: Valuation of stock

	If you want real-time stock valuation that tracks stock movements you must assign an account to
	each stock location. As product items are added to and taken from each location Open ERP generates
	an account entry for that location defined by the configuration of the product being moved – and
	a stock valuation based (in the current versions of Open ERP) on either Standard Cost or Average
	Price.

	For example, if you assign an account to the Supplier location you'll be able see the value of
	stock that you've taken from the supplier. Its contents should be valued in your accounts. Thus it
	manages inventory on consignment.

A Warehouse contains an input location, a stock location and an output location for sold products.
You can associate a warehouse with a partner to give the warehouse an address. That doesn't have to
be your own company (although it can be): you can easily specify another partner who may be holding
stock on your behalf.

.. index::
   single: location structure

.. note:: Location Structure

	Each warehouse is composed of three locations :guilabel:`Location Input`, :guilabel:`Location Output`, and 
	:guilabel:`Location Stock`. Your available stock is given by the contents of the :guilabel:`Location Stock` 
	and its child locations.

	So the :guilabel:`Location Input` can be placed as a child of the :guilabel:`Location Stock`, which means 
	that when :guilabel:`Location Stock` is interrogated for product quantities, it also takes account of the 
	contents of the :guilabel:`Location Input`. :guilabel:`Location Input` could be used as a goods-in QC location.
	The :guilabel:`Location Output` must never be placed as a child of :guilabel:`Location Stock`, 
	since items in :guilabel:`Location Output`, which can be considered to be
	packed ready for customer shipment, should not be thought of as available for sale elsewhere.
	
	In the default configuration, Open ERP uses the same ``Stock`` location for both Input and Output because it
	is easier to understand when you're starting out.

.. index::
   single: account; chart
   single: chart of accounts

Setting up a chart of accounts
------------------------------

You can set up a chart of accounts during the creation of a database, but for this exercise you'll
start with the minimal chart that you created (just a handful of required
accounts without hierarchy, tax or subtotals).

A number of account charts have been predefined for Open ERP, some of which meet the needs of
national authorities (the number of those created for Open ERP is growing as various contributors
create and freely publish them). You can take one of those without changing it if it's suitable, or
you can take anything as your starting point and design a complete chart of accounts to meet your
exact needs, including accounts for inventory, asset depreciation, equity and taxation.

You can also run multiple charts of accounts in parallel – so you can put all of your transaction
accounts into several charts, with different arrangements for taxation and depreciation, aggregated
differently for various needs.

Before you can use any chart of accounts for anything you need to specify a Fiscal Year. This
defines the different time periods available for accounting transactions. An initial Fiscal Year
was created during the database setup so you don't need to do any more on this.

Click :menuselection:`Financial Management --> Charts --> Charts of Accounts` and then click
:guilabel:`Open Charts` to open a new
:guilabel:`Account charts` form where you define exactly what you want to see. 
Click :guilabel:`Open Charts` to accept the defaults and see a
hierarchical structure of the accounts.

.. index::
   pair: database; backup

Make a backup of the database
-----------------------------

If you know the super-administrator password, make a backup of your database using the procedure
described at the very end of :ref:`ch-inst`. Then restore it to a new database: \ ``testing``\  .

This operation enables you to test the new configuration on \ ``testing``\   so that you can be sure
everything works as designed. Then if the tests are successful you can make a new database from \
``openerp_ch03``\  , perhaps called \ ``live``\ or  \ ``production``\ , for your real work.

From here on, connect to this new \ ``testing``\   database logged in as \ ``admin``\   if you can.
If you have to make corrections, do that on \ ``openerp_ch03``\   and copy it to a new \
``testing``\   database to continue checking it.

Or you can just continue working with the \ ``openerp_ch03``\   database to get through this
chapter. You can recreate \ ``openerp_ch03``\   quite quickly if something goes wrong and you can't
recover from it but, again, you'd need to know your super-administrator password for that.

.. Copyright © Open Object Press. All rights reserved.

.. You may take electronic copy of this publication and distribute it if you don't
.. change the content. You can also print a copy to be read by yourself only.

.. We have contracts with different publishers in different countries to sell and
.. distribute paper or electronic based versions of this book (translated or not)
.. in bookstores. This helps to distribute and promote the Open ERP product. It
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

