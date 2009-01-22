
Financial Analysis
##################

Summary

* Managing creditors and debtors

* Taxes

* Management Control and Financial Analysis

Keywords

* creditors / accounts payable

* debtors / accounts receivable

* escalation

* reports

* taxes

* management control

* analysis

* financial indicators 

* budgets

 *This chapter is devoted to statutory taxation and financial reporting from Open ERP. Whether you need reports about customers and suppliers, or statements for various statutory purposes, Open ERP enables you to carry out a whole range of parametric analyses of the financial health of your company.* 


Whether you want to analyze the general health of your company or review the status of an Account Receivable in detail, your company's accounts are the place to define your various business indicators.

To bring you the most accurate picture of your business, Open ERP's different accounting reports are flexible, and the results are calculated in real time. This enables you to automate recurring actions and to change your operations quickly when a company-wide problem (such cash reserves dropping too low, or receivables climbing too high) or a local problem (a client that hasn't paid, or a project budget overspend) occurs.

So this chapter describes the various reports and financial statements supplied by Open ERP's accounting module. It also describes how Open ERP handles purchase and sales taxation, and the reporting of taxation.

.. index::
   single: Accounts payable
.. 

Managing accounts payable / creditors and accounts receivable / debtors
=======================================================================

Open ERP provides numerous tools for managing customer and supplier accounts. You'll see here:

* financial analysis of partners, to understand the reports that enable you to carry out an analysis of all of your partners,

* multi-level reminders, which is an automatic system for preparing reminder letters or emails when invoices remain unpaid,

* detailed analysis of individual partners.

Financial analysis of partners
------------------------------

When members of your accounts department sign on to the Open ERP system, they're immediately presented with the  *Accounting Dashboard.*  By default it contains a useful graph for analyzing Receivables. To get access to it, install the module \ ``board_account``\  . Then look at it using the menu  *Dashboards > Accounting > Accounting Dashboard* .


	.. image::  images/account _board.png
	   :align: center

*Accounting Dashboard*

In the dashboard, the graph at the right entitled  *Aged Receivables*  represents your receivables week by week. That shows you at a glance the cumulative amount of your customer debtors by week.

All of Open ERP's graphs are dynamic. So you can, for example, filter the data by clicking  *Zoom*  and then  *Filter*  on the Search form. Or just click on  *Zoom*  to open in a larger window for a graph, then click  *Search*  to display this in a list view.

To obtain a more detailed report of the aged balance (or order by past date) use the menu  *Finance > Accounting > Reporting > Partner Accounts > Aged Partner balance* . 


	.. image::  images/account_balance.png
	   :align: center

*Aged balance using a 30 day period*

When opening that report, Open ERP asks for the name of the company, the fiscal period and the size of the interval to be analyzed (in days). Open ERP then calculates a table of credit balance by period. So if you request an interval of 30 days Open ERP generates an analysis of creditors for the past month, past two months, and so on.

For an analysis by partner you can use the partner balance that you get through the menu  *Financial Management > Reporting > Partner Accounts > Partner balance* . The system then supplies you with a PDF report containing one line per partner representing the cumulative credit balance. 


	.. image::  images/account_partner_balance.png
	   :align: center

*Partner balances*

If you want detailed information about a partner you can use the partner ledgers that you reach through the menu  *Financial Management > Reporting > Partner Accounts > Partner Ledger* .


	.. image::  images/account_partner_ledger.png
	   :align: center

*Partner ledger*

Finally you can look up individual account entries by searching for useful information. To search for account entries:

* by journal, go through the menu  *Financial Management > Entries > Entries by journal* ,

* by account, go through the menu  *Financial Management > Charts > Chart of Accounts*  and double-click the appropriate account,

* by making a global search, go through the menu  *Financial Management > Entries > Search Entries* 

* by partner, do it by right-clicking on the Partner field in any form that shows it, or by using the buttons to the right of the partner form.

.. tip::   **Advantage**  *Exporting entries* 

	It's helpful to remember that you can export all types of resource in Open ERP. From the web client you need to navigate to a search list for the resource then click the Export link at the bottom left of the list. From the GTK client you'd use the menu Form > Export. This enables you to easily make your own analysis in Microsoft Excel or OpenOffice.org Calc, by exporting accounting entries.
	
.. index::
  single: Follow-ups
..

Multi-step follow-ups
---------------------

To automate the management of followups (reminders) you must install the module \ ``account_followup``\  . This is installed automatically as part of the accounting profile, but is not part of the other profiles.

Once the module is installed configure your levels of followup using the menu  *Financial Management > Configuration > Payment Terms > Follow-Ups* .

The levels of follow-up are relative to the date of creation of an invoice and not the due date. This enables you to put payment conditions such as 'payable in 21 days' and send a reminder in 30 days, or the converse.

For each level you should define the number of days and create a note which will automatically be added into the reminder letter. The sequence determines the order of the level in ascending order.


.. csv-table::  **Example of configuring followup levels**
   :header: "Sequence","Level","Days","Description"
   :widths: 5, 5, 15, 15
   
   "1","Level 1","30 days net","First payment reminder"
   "2","Level 2","45 days net","Second reminder"
   "3","Level 3","60 days from end of month","Put on notice"

You can send your reminders by mail and/or email with the menu  *Financial Management > Periodic Handling > Send Follow-Ups* .


	.. image::  images/account_followup_wizard.png
	   :align: center

*Form for preparing follow-up letters*


Open ERP presents you with a list of partners who are due reminders, which you can modify before starting the procedure. On the second tab of the form you can supply the information you'll send in the email reminder.

The system then gives you a PDF report with all of the reminder letters for each partner. Each letter is produced in the language of the partner (if that's available) and you can therefore get letters in several languages in the same PDF on several pages.

To analyze the due date of customers and/or suppliers before starting the reminder procedure, use the submenus of  *Financial Management > Periodical Processing > Send Follow-Ups* :

*  *Receivable entries* ,

*  *Payable entries* .

So you obtain the list of unreconciled entries in Receivable and Payable type accounts. You can then modify the date and the last follow-up and the level of reminder for each entry.

To obtain a detailed report per partner use the menu  *Financial Management > Reporting > Follow-Ups* .

The different reports are classic Open ERP screens, so you can filter them and explore the elements in detail. 


	.. image::  images/account_followup.png
	   :align: center

*Summary screen for follow-ups*

Partner situation
-----------------

In daily use of Open ERP a senior manager will often need to search quickly for financial information amongst partner data. For this she can use the buttons to the right of form when she opens a partner form, to go directly to:

* a follow-up letter from the  *Overdue payments*  Report button,

* the list of  *Open Invoices* ,

* a shortcut to  *All account entries* ,

* the unclosed CRM requests from  *Open cases* ,

* a shortcut to the unreconciled  *Receivables and Payables* .

These links are also available to her when she right-clicks the mouse on a partner field on any form.

The  *Overdue payments*  report produces a PDF document which is used for follow-up but it doesn't modify any of the partner's accounting entries. It's use doesn't increase the follow-up level so you can use this report repeatedly without any problem.

In Open ERP you can search for a partner on the basis of the value of its trade receivables. So search for partners with a credit amount between 1 and 99999999 and you'll get a list of partners that owe you payment. You can then select the whole list and print follow-up letters for them all.

To the right of the partner form there's a shortcut to  *Open invoices* . This link includes all of the invoices defined in the systems, namely:

* customer invoices,

* supplier invoices,

* credit notes,

* supplier credit notes.

.. tip::   **Advice**  *Reminders from accounting entries* 

	Companies that do not have computerized records tend to keep track of payments from invoices and paperwork and not from a formal partner account

	It's better to create reminder letters from a partner's account receivable than from unpaid bills, however. By using the Open ERP system you can easily take account of all advances, unreconciled payments, credit notes and credit payments.

	So it's better to send a letter based on the accounting entries of invoices and unreconciled payments than just on a list of unpaid invoices.

In the links appearing on the partner form, two buttons enable the opening of partner accounting entries:

*  *All account entries* ,

*  *Receivables & Payables* .

The first button is useful for obtaining a historical analysis of the customer or supplier. You can get information about such significant items as sales volume and payment delays. The second button is a filter which shows only the open trade credits and debits for the partner.

Finally, keep in mind that all of the functions on the partner form are accessible from any Open ERP document by right-clicking with the mouse on a Partner field. This is extremely useful for gaining rapid access to information from any screen.

Statutory taxes and accounts
============================

This section deals with statutory taxes and accounts which are legally required from the company:

* the taxation structure provided by Open ERP,

* the accounts ledgers,

* account balance (used to produce the income statement and balance sheet),

* the different journals (general, centralized and detailed),

* the tax declaration.

.. tip::   **A step further**  *Other declarations* 

	In addition to the legal declarations available in the accounts modules, Open ERP supplies declarations based on the functionality in other modules.

	You can, for example, install the report_intrastat module for intra-stat declarations about sending goods to and receiving goods from other countries.

.. index::
   single: Taxation
.. 

Taxation
--------

You can attach taxes to financial transactions so that you can 

* add taxes to the amount that you pay or get paid,

* report on the taxes in various categories that you should pay the tax authorities,

* track taxes in your general accounts,

* manage the payment and refund of taxes using the same mechanisms that Open ERP uses for other monetary transactions. 

Since the detailed tax structure is a mechanism for carrying out governments' policies, and the collecting of taxes so critical to their tax authorities, tax requirements and reporting can be complex. Open ERP has a flexible mechanism for handling taxation that can be configured through its GUI or through data import mechanisms to meet the requirements of many various tax jurisdictions.

The taxation mechanism can also be used to handle other tax-like financial transactions, such as royalties to authors based on the value of transactions through an account.

.. index::
   single: Taxes; Tax structure
.. 

Setting up a tax structure
^^^^^^^^^^^^^^^^^^^^^^^^^^

Three main objects are involved in the tax system in Open ERP:

* a  *Tax Case*  (or  *Tax Code* ), used for tax reporting, that can be set up in a hierarchical structure so that multiple codes can be formed into trees in the same way as a Chart of Accounts.

* a  *Tax* , the basic tax object that contains the rules for calculating tax on the financial transaction it's attached to, and is linked to the General Accounts and to the Tax Cases. A tax can contain multiple child taxes and base its calculation on those taxes rather than the base transaction, providing considerable flexibility. Each tax belongs to a  *Tax Group*  (currently just \ ``VAT``\   or \ ``Other``\  ).

* the  *General Accounts* , that record the taxes owing and paid. Since the general accounts are discussed elsewhere in this part of the book and are not tax-specific, they won't be detailed in this section.

You can attach zero or more  *Supplier Taxes* and Customer taxes to products, so that you can account separately for purchase and sales taxes (or Input and Output VAT – where VAT is Value Added Tax). Because you can attach more than one tax, you can handle a VAT or Sales Tax separately from an Eco Tax on the same product.

You can also attach a  *Default Tax*  to a partner, which replaces any taxes belonging to the same Tax Group that may have been defined in a Product. 

So you can define a \ ``Tax Exempt``\   tax in the \ ``VAT``\   group and assign it to partners who declare themselves to be charities. All product sales to a charity would then be VAT free even if the products themselves carry various tax rates, but non-VAT taxes such as Eco-taxes can still be applied.

.. index::
   single: Taxes; Tax Cases
.. 

Tax Cases
^^^^^^^^^

Tax Cases are also known in Open ERP as Tax Codes. They're used for tax reporting, and can be set up in a hierarchical structure to form trees in the same way as a Chart of Accounts.

To create a new Tax Case, use the menu  *Financial Management > Configuration > Taxes > Tax Codes* . You define the following fields:

*  *Tax Case Name* : a unique name required to identify the Case,

*  *Company* : a required link that attaches the Case to a specific company, such as the Main Company,

*  *Case Code* : a short code for the case,

*  *Parent Code* : a link to a parent Tax Case that forms the basis of the tree structure like a Chart of Accounts,

*  *Sign for Parent* : choose 1.00 to add the total to the parent account or -1.00 to subtract it,

*  *Description* : a free text field for documentation purposes.

You can also see two read-only fields:

*  *Year Sum* : a single figure showing the total accumulated on this case for the financial year.

*  *Period Sum* : a single figure showing the total accumulated on this case for the current financial period (perhaps 1 month or 3 months).

You will probably need to create two tax cases for each different tax rate that you have to define, one for the tax itself and one for the invoice amount that the tax is based on. And you'll create tax cases that you won't link to Tax objects (similar to General Account \ ``View``\   types) just to organize the tree structure.

To view the structure that you've constructed you can use the menu  *Financial Management > Periodical Processing > Taxes* . This tree view reflects the structure of the Tax Cases and shows the current tax situation.


Tax objects
^^^^^^^^^^^

Tax objects calculate tax on the financial transactions that they're attached to, and are linked to the General Accounts and to the Tax Cases. 

To create a new Tax Case, use the menu  *Financial Management > Configuration > Taxes > Taxes* . You define the following fields:

*  *Tax Name* : a unique name required for this tax (such as \ ``12% Sales VAT``\  ),

*  *Company* : a required link to a company associated with the tax, such as the Main Company,

*  *Tax Group* : \ ``VAT``\   or \ ``Other``\  , used to determine which taxes on products can be substituted by taxes on partners,

*  *Tax Type* : a required field directing how to calculate the tax: \ ``Percent``\  , \ ``Fixed``\  , \ ``None``\   or \ ``Python Code``\  , (the latter is found in the  *Compute Code*  field in the  *Special Computation*  tab),

*  *Applicable Type* : a required field that indicates whether the base amount should be used unchanged (when the value is \ ``True``\  ) or whether it should be processed by Python Code in the  *Applicable Code*  field in the  *Special Computation*  tab when the value is \ ``Code``\  ),

*  *Amount* : a required field whose meaning depends on the Tax Type, being a multiplier on the base amount when the  *Tax Type*  is \ ``Percent``\  , and a fixed amount added to the base amount when the  *Tax Type*  is \ ``Fixed``\  ,

*  *Include in base amount* : when checked, the tax is added to the base amount and not shown separately,

*  *Domain* : is only used in special developments, not in the core Open ERP system,

*  *Invoice Tax Account* :a General Account used to record invoiced tax amounts, which may be the same for several taxes or split so that one tax is allocated to one account,

*  *Refund Tax Account* : a General Account used to record invoiced tax refunds, which may be the same as the Invoice Tax Account or, in some tax jurisdictions, must be separated,

*  *Tax on childs* : when checked, the tax calculation is applied to the output from other tax calculations specified in the  *Childs Tax Account* field (so you can have taxes on taxes), otherwise the calculation is applied to the base amount on the transaction,

*  *Childs Tax Account* : other tax accounts that can be used to supply the figure for taxation.

.. tip::   **Note**  *Using Child Taxes* 

	You can use child taxes when you have a complex tax situation that you want to hide your end users from. For example, you might define a motor mileage expenses product with a composite tax made up of two child taxes – a non-reclaimable private element and a reclaimable tax element (which is the case in some European countries). 

	When your staff come to claim motor mileage, they do not need to know about this taxation, but the accounting impact of their claim will be automatically managed in Open ERP.

The fields above apply the taxes that you specify and record them in the general accounts but don't provide you with the documentation that your tax authorities might need. For this use the Tax Declaration tab to define which Tax Cases should be used for this tax:

*  *Invoices/Base Code* : tax case to record the invoiced amount that the tax is based on,

*  *Invoices/Tax Code* : tax case to record the invoiced tax amount

*  *Refund Invoices/Base Code* : tax case to record the refund invoice amount that the tax is based on,

*  *Refund Invoices/Tax Code* : tax case to record the refund invoice tax amount.

Use of Taxes on Products, Partners, Projects and Accounts
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When you've created a tax structure consisting of Tax Cases and Tax objects, you can use the taxes in your various business objects so that financial transactions can be associated with taxes and tax-like charges. 

.. tip::   **Advice**  *Retail Customers* 

	When you're retailing to end users rather than selling to a business, you may want to (or be required to) show tax-inclusive prices on your invoicing documents rather than a tax-exclusive price plus tax. 

	To do this in Open ERP just install the account_tax_include module. Each invoice is given a new Price method field, in which you choose Tax included or Tax excluded. Prices are then displayed appropriately.

You can assign a tax to a Partner so that it overrides any tax defined in a Product. You'd do this, for example, if a
partner was a charity and paid a lower or zero rate of VAT or Sales Tax on its purchases. Assuming that you have an
appropriate Charities VAT or Sales Tax in the \ ``VAT``\   *Tax Group* , use the menu  *Partners > Partners* to open
and edit a Partner form for the charity, then:

* select the  *Properties*  tab,

* set the  *Default Tax*  field to the \ ``Charities VAT``\   tax.

You can assign multiple taxes to a Product. Assuming you have set up the appropriate taxes, you would use the menu  *Products > Products*  to open and edit a Product definition, then:

* select one or more  *Customer Taxes*  for any products that you might sell, which may include a \ ``Sales Tax``\   or \ ``Output VAT``\  , and a \ ``Sales Eco Tax``\  ,

* select one or more  *Supplier Taxes*  for any products that you might purchase, which may include a \ ``Purchase Tax``\   or \ ``Input VAT``\  , and a \ ``Purchase Eco Tax``\  .

Generally, when you make a purchase or sale, the taxes assigned to the product are used to calculate the taxes owing or owed. But when you make a transaction with a partner that has a  *Default Tax*  defined, for example a sale to a charity with \ ``Charities ``\  \ ``Tax``\  , that tax will be used in place of other Product taxes in the same group – in this case replacing the standard \ ``Sales Tax``\   or \ ``Output VAT``\  .

You can also assign multiple taxes to a Project, so that invoices from the Project carry an appropriate rate of tax (project invoicing is dealt with in detail in a later chapter).

.. tip::   **A step further**  *Tax regions* 

	The third-party module import_export can be used to extend Open ERP's tax system, so that you can assign taxes to different accounts depending on the location of the Partner. The Partner is given a new Partner Location field that can be set to Local, Europeor Outside, so that taxes and tax bases can be channeled to different accounts. 

	This module could be the basis of more ambitious location-based tax accounting.

And you can assign multiple taxes to an account so that when you transfer money through the account you attract a tax amount. In such a case, this 'tax' may not be legally-required taxation but something tax-like, for example authors' royalties or sales commission.

The accounts ledgers and the balance sheet
------------------------------------------

To print the balance of accounts or the accounts ledgers you should turn to the Chart of Accounts. To do that go to the menu  *Financial Management > Charts > Charts of Accounts* .

Select the accounting period you're interested in and click  *Open Charts* , then select one or several accounts for analysis by clicking and highlighting the appropriate line(s). Click the  *Print*  button and Open ERP asks you to select either the  *General Ledger* , the  *Account balance* , or an  *Analytic check* . If you select an account which has sub-accounts in the hierarchy you can automatically analyze that account and its child accounts.

.. tip::   **Advantage**  *Simulated balance* 

	While you're printing account balances, if you have installed the account_simulation module Open ERP asks you which level of simulation to execute.

	Results will vary depending on the level selected. You can, for example, print the balance depending on various methods of amortization:

	* the normal IFRS method,

	* the French method.

	More generally it enables you to make analyses using other simulation levels that you could expect..

At the moment of writing this book a new module is in the final stages of development for Open ERP – \ ``account_reporting``\  . It's being developed to enable the use of configurable reports for balance sheets or earnings statement in legally required formats.

.. index::
  single: Accounting; Journals
..

The accounting journals
-----------------------

To obtain the different journals use the menu  *Financial Management > Reporting > Printing Journals* .

.. tip::   **Terminology**  *Journals* 

	Note there are different types of journal in Open ERP

	* accounting journals (detailed in this chapter),

	* purchase journals (for distributing supplies provided or on certain dates),

	* sales journals (for example classifying sales by their type of trade),

	* the invoice journals (to classify sales by mode of invoicing: daily / weekly / monthly) and automating the tasks.

	To obtain these different journals install the modules sale_journal and purchase_journal.

Then select one or several journals and click  *Print* . Open ERP then proposes the three following reports:

* detailed accounting entries,

* general journal,

* journal grouped by account.


	.. image::  images/account_journal_print.png
	   :align: center

*Printing a journal*

.. index::
  single: Taxes; Tax declaration
..

Tax declaration
---------------

Information required for a tax declaration is automatically generated by Open ERP from invoices. In the section on invoicing you'll have seen that you can get details of tax information from the area at the bottom left of an invoice.

You can also get the information from the accounting entries in the columns to the right.

Open ERP keeps a tax chart that you can reach from the menu  *Financial Management > Periodical Processing > Taxes* . The structure of the chart is for calculating the tax declaration but also all the other taxes can be calculated (such as the French DEEE).


	.. image::  images/account_tax_chart.png
	   :align: center

*Example of a Belgian TVA (VAT) declaration*

The tax chart represents the amount of each area of the tax declaration for your country. It's presented in a hierarchical structure which lets you see the detail only of what interests you and hides the less interesting subtotals. This structure can be altered as you wish to fit your needs.

You can create several tax charts if your company is subject to different types of tax or tax-like accounts, such as:

* authors' rights,

* ecotaxes such as the French DEEE for recycling electrical equipment.

Each accounting entry can then be linked to one of the tax accounts. This association is done automatically by the taxes which had previously been configured in the invoice lines.

.. tip::   **Advantage**  *Tax declaration* 

	Some accounting software manages the tax declaration in a dedicated general account. The declaration is then limited to the balance in the specified period. In Open ERP you can create an independent chart of taxes, which has several advantages: 

	* it's possible to allocate only a part of the tax transaction

	* it's not necessary to manage several different general accounts depending on the type of sale and type of tax

	* you can restructure your chart of taxes as you need

At any time you can check your chart of taxes for a given period using the report:  *Financial Management > Reporting > Taxes Report* .

This data is updated in real time. That's very useful because it enables you at any time to preview the tax that you owe at the start and end of the month or quarter.

Furthermore, for your tax declaration you can click on one of the tax accounts to investigate the detailed entries that make up the full amount. This helps you search for errors such as when you've coded an invoice at full tax rate where it should be zero-rated for an inter-community trade or for a charity.

In some countries, tax can be calculated on the basis of payments received rather than invoices sent. In this instance choose  *Base on * \ ``Payments``\   instead of  *Base on * \ ``Invoices``\   in the  *Select *  *period*  form. Even if you make your declaration on the basis of invoices sent and received it can be interesting to compare the two reports to see the amount of tax that you pay but haven't yet received from your customers.



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

=======

Statutory taxes and accounts
============================

This section deals with statutory taxes and accounts which are legally required from the company:

* the taxation structure provided by Open ERP,

* the accounts ledgers,

* account balance (used to produce the income statement and balance sheet),

* the different journals (general, centralized and detailed),

* the tax declaration.

.. tip::   **A step further**  *Other declarations* 

	In addition to the legal declarations available in the accounts modules, Open ERP supplies declarations based on the functionality in other modules.

	You can, for example, install the report_intrastat module for intra-stat declarations about sending goods to and receiving goods from other countries.

Taxation
--------

You can attach taxes to financial transactions so that you can 

* add taxes to the amount that you pay or get paid,

* report on the taxes in various categories that you should pay the tax authorities,

* track taxes in your general accounts,

* manage the payment and refund of taxes using the same mechanisms that Open ERP uses for other monetary transactions. 

Since the detailed tax structure is a mechanism for carrying out governments' policies, and the collecting of taxes so critical to their tax authorities, tax requirements and reporting can be complex. Open ERP has a flexible mechanism for handling taxation that can be configured through its GUI or through data import mechanisms to meet the requirements of many various tax jurisdictions.

The taxation mechanism can also be used to handle other tax-like financial transactions, such as royalties to authors based on the value of transactions through an account.

Setting up a tax structure
^^^^^^^^^^^^^^^^^^^^^^^^^^

Three main objects are involved in the tax system in Open ERP:

* a  *Tax Case*  (or  *Tax Code* ), used for tax reporting, that can be set up in a hierarchical structure so that multiple codes can be formed into trees in the same way as a Chart of Accounts.

* a  *Tax* , the basic tax object that contains the rules for calculating tax on the financial transaction it's attached to, and is linked to the General Accounts and to the Tax Cases. A tax can contain multiple child taxes and base its calculation on those taxes rather than the base transaction, providing considerable flexibility. Each tax belongs to a  *Tax Group*  (currently just \ ``VAT``\   or \ ``Other``\  ).

* the  *General Accounts* , that record the taxes owing and paid. Since the general accounts are discussed elsewhere in this part of the book and are not tax-specific, they won't be detailed in this section.

You can attach zero or more  *Supplier Tax* es and Customer taxes to products, so that you can account separately for purchase and sales taxes (or Input and Output VAT – where VAT is Value Added Tax). Because you can attach more than one tax, you can handle a VAT or Sales Tax separately from an Eco Tax on the same product.

You can also attach a  *Default Tax*  to a partner, which replaces any taxes belonging to the same Tax Group that may have been defined in a Product. 

So you can define a \ ``Tax Exempt``\   tax in the \ ``VAT``\   group and assign it to partners who declare themselves to be charities. All product sales to a charity would then be VAT free even if the products themselves carry various tax rates, but non-VAT taxes such as Eco-taxes can still be applied.

Tax Cases
^^^^^^^^^

Tax Cases are also known in Open ERP as Tax Codes. They're used for tax reporting, and can be set up in a hierarchical structure to form trees in the same way as a Chart of Accounts.

To create a new Tax Case, use the menu  *Financial Management > Configuration > Taxes > Tax Codes* . You define the following fields:

*  *Tax Case Name* : a unique name required to identify the Case,

*  *Company* : a required link that attaches the Case to a specific company, such as the Main Company,

*  *Case Code* : a short code for the case,

*  *Parent Code* : a link to a parent Tax Case that forms the basis of the tree structure like a Chart of Accounts,

*  *Sign for Parent* : choose 1.00 to add the total to the parent account or -1.00 to subtract it,

*  *Description* : a free text field for documentation purposes.

You can also see two read-only fields:

*  *Year Sum* : a single figure showing the total accumulated on this case for the financial year.

*  *Period Sum* : a single figure showing the total accumulated on this case for the current financial period (perhaps 1 month or 3 months).

You will probably need to create two tax cases for each different tax rate that you have to define, one for the tax itself and one for the invoice amount that the tax is based on. And you'll create tax cases that you won't link to Tax objects (similar to General Account \ ``View``\   types) just to organize the tree structure.

To view the structure that you've constructed you can use the menu  *Financial Management > Periodical Processing > Taxes* . This tree view reflects the structure of the Tax Cases and shows the current tax situation.

Tax objects
^^^^^^^^^^^

Tax objects calculate tax on the financial transactions that they're attached to, and are linked to the General Accounts and to the Tax Cases. 

To create a new Tax Case, use the menu  *Financial Management > Configuration > Taxes > Taxes* . You define the following fields:

*  *Tax Name* : a unique name required for this tax (such as \ ``12% Sales VAT``\  ),

*  *Company* : a required link to a company associated with the tax, such as the Main Company,

*  *Tax Group* : \ ``VAT``\   or \ ``Other``\  , used to determine which taxes on products can be substituted by taxes on partners,

*  *Tax Type* : a required field directing how to calculate the tax: \ ``Percent``\  , \ ``Fixed``\  , \ ``None``\   or \ ``Python Code``\  , (the latter is found in the  *Compute Code*  field in the  *Special Computation*  tab),

*  *Applicable Type* : a required field that indicates whether the base amount should be used unchanged (when the value is \ ``True``\  ) or whether it should be processed by Python Code in the  *Applicable Code*  field in the  *Special Computation*  tab when the value is \ ``Code``\  ),

*  *Amount* : a required field whose meaning depends on the Tax Type, being a multiplier on the base amount when the  *Tax Type*  is \ ``Percent``\  , and a fixed amount added to the base amount when the  *Tax Type*  is \ ``Fixed``\  ,

*  *Include in base amount* : when checked, the tax is added to the base amount and not shown separately,

*  *Domain* : is only used in special developments, not in the core Open ERP system,

*  *Invoice Tax Account* :a General Account used to record invoiced tax amounts, which may be the same for several taxes or split so that one tax is allocated to one account,

*  *Refund Tax Account* : a General Account used to record invoiced tax refunds, which may be the same as the Invoice Tax Account or, in some tax jurisdictions, must be separated,

*  *Tax on childs* : when checked, the tax calculation is applied to the output from other tax calculations specified in the  *Childs Tax Account* field (so you can have taxes on taxes), otherwise the calculation is applied to the base amount on the transaction,

*  *Childs Tax Account* : other tax accounts that can be used to supply the figure for taxation.

.. tip::   **Note**  *Using Child Taxes* 

	You can use child taxes when you have a complex tax situation that you want to hide your end users from. For example, you might define a motor mileage expenses product with a composite tax made up of two child taxes – a non-reclaimable private element and a reclaimable tax element (which is the case in some European countries). 

	When your staff come to claim motor mileage, they do not need to know about this taxation, but the accounting impact of their claim will be automatically managed in Open ERP.

The fields above apply the taxes that you specify and record them in the general accounts but don't provide you with the documentation that your tax authorities might need. For this use the Tax Declaration tab to define which Tax Cases should be used for this tax:

*  *Invoices/Base Code* : tax case to record the invoiced amount that the tax is based on,

*  *Invoices/Tax Code* : tax case to record the invoiced tax amount

*  *Refund Invoices/Base Code* : tax case to record the refund invoice amount that the tax is based on,

*  *Refund Invoices/Tax Code* : tax case to record the refund invoice tax amount.

Use of Taxes on Products, Partners, Projects and Accounts
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When you've created a tax structure consisting of Tax Cases and Tax objects, you can use the taxes in your various business objects so that financial transactions can be associated with taxes and tax-like charges. 

.. tip::   **Advice**  *Retail Customers* 

	When you're retailing to end users rather than selling to a business, you may want to (or be required to) show tax-inclusive prices on your invoicing documents rather than a tax-exclusive price plus tax. 

	To do this in Open ERP just install the account_tax_include module. Each invoice is given a new Price method field, in which you choose Tax included or Tax excluded. Prices are then displayed appropriately.

You can assign a tax to a Partner so that it overrides any tax defined in a Product. You'd do this, for example, if a partner was a charity and paid a lower or zero rate of VAT or Sales Tax on its purchases. Assuming that you have an appropriate Charities VAT or Sales Tax in the \ ``VAT``\   *Tax Group* , use the menu  *Partners > Partners* to open and edit a Partner form for the charity, then:

* select the  *Properties*  tab,

* set the  *Default Tax*  field to the \ ``Charities VAT``\   tax.

You can assign multiple taxes to a Product. Assuming you have set up the appropriate taxes, you would use the menu  *Products > Products*  to open and edit a Product definition, then:

* select one or more  *Customer Taxes*  for any products that you might sell, which may include a \ ``Sales Tax``\   or \ ``Output VAT``\  , and a \ ``Sales Eco Tax``\  ,

* select one or more  *Supplier Taxes*  for any products that you might purchase, which may include a \ ``Purchase Tax``\   or \ ``Input VAT``\  , and a \ ``Purchase Eco Tax``\  .

Generally, when you make a purchase or sale, the taxes assigned to the product are used to calculate the taxes owing or owed. But when you make a transaction with a partner that has a  *Default Tax*  defined, for example a sale to a charity with \ ``Charities ``\  \ ``Tax``\  , that tax will be used in place of other Product taxes in the same group – in this case replacing the standard \ ``Sales Tax``\   or \ ``Output VAT``\  .

You can also assign multiple taxes to a Project, so that invoices from the Project carry an appropriate rate of tax (project invoicing is dealt with in detail in a later chapter).

.. tip::   **A step further**  *Tax regions* 

	The third-party module import_export can be used to extend Open ERP's tax system, so that you can assign taxes to different accounts depending on the location of the Partner. The Partner is given a new Partner Location field that can be set to Local, Europeor Outside, so that taxes and tax bases can be channeled to different accounts. 

	This module could be the basis of more ambitious location-based tax accounting.

And you can assign multiple taxes to an account so that when you transfer money through the account you attract a tax amount. In such a case, this 'tax' may not be legally-required taxation but something tax-like, for example authors' royalties or sales commission.

The accounts ledgers and the balance sheet
------------------------------------------

To print the balance of accounts or the accounts ledgers you should turn to the Chart of Accounts. To do that go to the menu  *Financial Management > Charts > Charts of Accounts* .

Select the accounting period you're interested in and click  *Open Charts* , then select one or several accounts for analysis by clicking and highlighting the appropriate line(s). Click the  *Print*  button and Open ERP asks you to select either the  *General Ledger* , the  *Account balance* , or an  *Analytic check* . If you select an account which has sub-accounts in the hierarchy you can automatically analyze that account and its child accounts.

.. tip::   **Advantage**  *Simulated balance* 

	While you're printing account balances, if you have installed the account_simulation module Open ERP asks you which level of simulation to execute.

	Results will vary depending on the level selected. You can, for example, print the balance depending on various methods of amortization:

	* the normal IFRS method,

	* the French method.

	More generally it enables you to make analyses using other simulation levels that you could expect..

At the moment of writing this book a new module is in the final stages of development for Open ERP – \ ``account_reporting``\  . It's being developed to enable the use of configurable reports for balance sheets or earnings statement in legally required formats.

The accounting journals
-----------------------

To obtain the different journals use the menu  *Financial Management > Reporting > Printing Journals* .

.. tip::   **Terminology**  *Journals* 

	Note there are different types of journal in Open ERP

	* accounting journals (detailed in this chapter),

	* purchase journals (for distributing supplies provided or on certain dates),

	* sales journals (for example classifying sales by their type of trade),

	* the invoice journals (to classify sales by mode of invoicing: daily / weekly / monthly) and automating the tasks.

	To obtain these different journals install the modules sale_journal and purchase_journal.

Then select one or several journals and click  *Print* . Open ERP then proposes the three following reports:

* detailed accounting entries,

* general journal,

* journal grouped by account.


	.. image::  images/account_journal_print.png
	   :align: center

*Printing a journal*

Tax declaration
---------------

Information required for a tax declaration is automatically generated by Open ERP from invoices. In the section on invoicing you'll have seen that you can get details of tax information from the area at the bottom left of an invoice.

You can also get the information from the accounting entries in the columns to the right.

Open ERP keeps a tax chart that you can reach from the menu  *Financial Management > Periodical Processing > Taxes* . The structure of the chart is for calculating the tax declaration but also all the other taxes can be calculated (such as the French DEEE).


	.. image::  images/account_tax_chart.png
	   :align: center

*Example of a Belgian TVA (VAT) declaration*

The tax chart represents the amount of each area of the tax declaration for your country. It's presented in a hierarchical structure which lets you see the detail only of what interests you and hides the less interesting subtotals. This structure can be altered as you wish to fit your needs.

You can create several tax charts if your company is subject to different types of tax or tax-like accounts, such as:

* authors' rights,

* ecotaxes such as the French DEEE for recycling electrical equipment.

Each accounting entry can then be linked to one of the tax accounts. This association is done automatically by the taxes which had previously been configured in the invoice lines.

.. tip::   **Advantage**  *Tax declaration* 

	Some accounting software manages the tax declaration in a dedicated general account. The declaration is then limited to the balance in the specified period. In Open ERP you can create an independent chart of taxes, which has several advantages: 

	* it's possible to allocate only a part of the tax transaction

	* it's not necessary to manage several different general accounts depending on the type of sale and type of tax

	* you can restructure your chart of taxes as you need

At any time you can check your chart of taxes for a given period using the report:  *Financial Management > Reporting > Taxes Report* .

This data is updated in real time. That's very useful because it enables you at any time to preview the tax that you owe at the start and end of the month or quarter.

Furthermore, for your tax declaration you can click on one of the tax accounts to investigate the detailed entries that make up the full amount. This helps you search for errors such as when you've coded an invoice at full tax rate where it should be zero-rated for an inter-community trade or for a charity.

In some countries, tax can be calculated on the basis of payments received rather than invoices sent. In this instance choose  *Base on* \ ``Payments``\   instead of  *Base on* \ ``Invoices``\   in the  *Select period*  form. Even if you make your declaration on the basis of invoices sent and received it can be interesting to compare the two reports to see the amount of tax that you pay but haven't yet received from your customers.

.. index::
  single: Financial Analysis
..

Company Financial Analysis
==========================

You'll see here the analysis tools for your company's financial situation, in particular:

* management indicators,

* budgets,

* the accounting dashboard.

Management Indicators
---------------------

.. tip::   **Terminology**  *Financial Indicators* 

	Indicators, sometimes called financial ratios, are tools for analyzing a company's finances. They enable you to compare two accounts or sets of accounts from the balance sheet or the profit and loss account, in the form of a ratio. They also let you measure the financial health of a company and make comparisons from one year to the next or against those of other companies.

To define accounting indicators in Open ERP you should install the module \ ``account_report``\  . When installing the module the usual financial indicators are registered in Open ERP.

You can consult your indicators, calculated in real time, from the menu  *Financial Management > Reporting > Custom Reports* .

Indicators defined by default in Open ERP are the following:

*  *Indicators of Working Capital* : determines if the company can pay its short term debts in normal conditions. It's calculated from \ ``(Stocks + Cash + Current Assets) / Current Liabilities``\  .

*  *Financial Ratios* : enables you to calculate the company's liquidity. It is defined as follows: \ ``( Current Assets – Stocks) / Current Liabilities``\  . 

*  *Fixed Assets* : in a going concern, the value of fixed assets are covered in the first place by owners' capital and in the second place by all of the long term liabilities. Ideally this indicator will be greater than 1.

.. tip::   **Advice**  *Calculation of indicators* 

	Calculating indicators can take quite a while in Open ERP because you have to analyze the whole company's accounting entries.

	So it's best not to calculate all of the indicators at once, but just a small selection to keep calculation time within limits.

Time analysis of indicators
^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can analyze the financial indicators along two axes. You must have a figure calculated at a particular instant of time when you compare accounts, balances and the ratios between them. But you can also calculate a time series to follow the change of a given indicator throughout the life of the company.

To do a temporal analysis of your indicators, you must install the module \ ``account_report_history``\   from the set of modules in extra_addons.

Once this module is installed, you can click on a financial indicator to get a graph of its evolution in time.


	.. image::  images/account_report_history.png
	   :align: center

*History of an accounting indicator*

Defining your own indicators
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can define your own indicators in Open ERP using the menu  *Financial Management > Configuration > Custom Reporting > New Reporting Item Formula* .


	.. image::  images/account_indicator_new.png
	   :align: center

*Defining a new indicator*

You should make sure that the accounts that you base indicators on are given unique account codes, because codes are used in the creation of formulae. Create a formula using the syntax indicated in the instructions at the bottom of the form:

* Sum of debits in a general account: \ ``debit('12345')``\  ,

* Sum of credits in a general account: \ ``credit('12345')``\  ,

* Balance of a general account: \ ``balance('12345')``\  ,

* Value of another indicator: \ ``report ('IND')``\  .

where:

* \ ``12345``\   represents the code of a general account,

* \ ``IND``\   represents the code of another indicator.

So, using this notation, the cash ratio is defined by \ ``balance('4', '5') / balance('1')``\   – that's the balance in accounts 4 and 5 divided by the balance in account 1.

.. index::
  single: Budgeting
..

Good management budgeting
-------------------------

Open ERP manages its budgets using both General and Analytic Accounts. You'll see how to do this here for General Accounts and then in Chapter 9 for Analytical Accounts.

Use the menu  *Financial Management > Configuration > Budgets > General Budgets*  to define a new budget.

.. tip::   **Advice**  *Budget Revisions* 

	Even though you can modify a budget at any time to make a revision of it, it's best if you don't do that.

	Rather than edit an existing budget document, make a new version so that you can keep your original estimates safe for comparison. This enables you to analyze your changing perspectives of the company from revision to revision.

Begin data entry by entering a  *Code*  and a  *Name*  in the first tab of your new budget. The budget  *Direction*  can be for \ ``Products``\   or \ ``Charges``\   – choose one. Then, in the second tab,  *Dotations/Expenses* , you can define the charges per period. For each period you can define a quantity and/or an amount spent in the default currency of the chart of accounts.

It's also possible to automatically create the different income and expenses over the periods of a single fiscal year. To do that, click  *Spread*  on the second tab. A window then opens requesting the fiscal year over which you want to budget, and the total quantities and amounts for that year. If you want your budget to cover several years, repeat this operation several times.

Once the charges have been generated you can modify them manually to revise the charges period by period. Once the amounts have been assigned over the period, you must specify the accounts for creating this budget on the third tab,  *Accounts* . 

To do this, click  *Add*  and make multiple selections for the different accounts to be represented in the budget. Once the three tabs are completed you can save your budget.

.. tip::   **Reminder**  *Multiple selection* 

	You can select several elements (accounts, partners, etc) at the same time from a list. In the web client, click the checkbox alongside their name in the list view. In the GTK client, click on each element with the mouse, while holding the Ctrl button down.


	.. image::  images/account_budget.png
	   :align: center

*Printing a budget*

To print a budget and make calculations of expenditure to budget use the menu  *Financial Management > Reporting > Print Budgets* . Open ERP then gives you a list of available budgets. Select one or more budgets and then click  *Print*  to configure the report. The following figure gives an example of a budget produced by Open ERP.

The Accounting Dashboard
------------------------


	.. image::  images/account_board.png
	   :align: center

*Accounting Dashboard*

If you've installed the module \ ``board_account``\  , Open ERP gives you an accounting dashboard that can be presented to your accounting staff as they sign into the system (if you have set it as their Home Page). This dashboard provides an analysis of the company's financial health at a glance.

This gives a description of the different parts of the dashboard, from top to bottom then from left to right:

*  *Analytic accounts to close* : when you're managing cases each analytical account is a project or a contract. This area gives the accounts that must be closed (for example, contracts expired, support hours exceeded).

*  *Accounts to invoice* : shows analytical accounts where there are charges to be invoiced.

*  *Draft invoices* : gives the list of invoices waiting to be approved by an accountant.

*  *Costs to invoice* : gives the weekly change which can be, but haven't yet been, invoiced.

*  *Aged receivables* : gives a weekly graph of the receivables that haven't yet been reconciled.

*  *Aged revenues* : gives a weekly graph of the company's turnover.

In each panel of the accountants' dashboard you can click the  *Zoom*  button at the top right to investigate the detail of your financial indicators

The Accounting dashboard is dynamically integrated, which means that you can navigate easily through the data if you want more detail about certain factors, and edit the entries if necessary.



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

