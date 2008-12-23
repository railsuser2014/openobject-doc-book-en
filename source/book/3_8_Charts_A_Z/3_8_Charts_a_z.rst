

The A to Z of Configuring Accounts
###################################

Summary

* Charts of Accounts

* Journals

* Accounting Periods and Fiscal Years

* Payment Terms

Keywords

* chart of accounts

* journal

* accounting year

* fiscal year

* fiscal period

* payment terms

* control

 *Accounts must be configured to meet your company's needs. This chapter explains how to modify your chart of accounts, journals, access rights, initial account balances, and default values for the initial configuration of your Open ERP accounts.* 

Assuming, always, that it calculates accurately, the best accounting software would be marked out by its usability and simplicity of data entry, and flexibility in configuring its different components. These would let you modify the accounting module easily to meet your own needs so that you can optimize it for the way you want to use it.

Open ERP lets you adapt and reconfigure many functions to ease the task of data entry:

* adding controls for data entry,

* customizing the screens,

* filling fields automatically during data entry with data that's already known to the system. 

Chart of Accounts
===================

On installation, the software is given a default chart of accounts that's the same regardless of your country. To install the chart of accounts and tax definitions for your own country install the module \ ``l10n_XX``\   where XX represents your country code in two letters. For example to get the chart of accounts for France install the module \ ``l10n_fr``\  . 

Some of these pre-built modules are comprehensive and accurate, others have rather more tentative status and are simply indicators of the possibilities. You can modify these, or build your own accounts onto the default chart, or replace it entirely with a custom chart.

You view active charts of accounts using the menu  *Financial Management > Charts > Charts of Accounts* .

.. tip::   **Advantage**  *Hierarchical charts* 

	Most accounting software packages represent their charts of accounts in the form of a list. You can do this in Open ERP as well if you want to, but its tree view offers several advantages:

	* it lets you show and calculate only the accounts that interest you,

	* it enables you to get a global view of accounts (when you show only summary accounts)

	* it simplifies searches semantically

	* it's more intuitive, because you can search for accounts on the basis of their classification

	* it's flexible because you can easily restructure them.

The structure of the chart of accounts is hierarchical, with account subtotals called account views. You can develop a set of account views to contain only those elements that interest you.

To get the detail of the account entries that are important to you, all you need to do is click the account. You can also click the  *Print*  icon after selecting one or several accounts (do a  *Ctrl-click*  on each line you want to select). The software gives you a choice of at least two reports: print the ledger or the balance of the selected accounts.

Displaying the chart of accounts can take several seconds because Open ERP calculates the debits, credits and balance for each account in real time. If you just want to work with a chart of accounts that has structure but shows no totals, use the function  *Financial Management > Charts > Charts of Accounts > Fast Charts of Accounts* .

Creating a chart of accounts
-----------------------------

	.. image::  images/account_form.png
	   :align: center

*Definition of an account*

To add, modify or delete existing accounts, use the menu  *Financial Management > Configuration > General Accounts > Accounts Definitions* .

.. tip::   **Advantage**  *Multi-lingual fields* 

	In Open ERP multi-lingual fields are marked by a small flag to their right. Click on the flag to get a translation of the value of the field in the different installed languages. You can also edit the translation.

	This enables you to efficiently manage other languages as you need them The field's value appears in the language of the logged-in user or, in the case of reports printed for a partner, that of the partner.

The main account fields are:

*  *Name* : the name of the account is a multi-lingual field, which is why there's a little flag to the right. Give the field a name.

*  *Active* : if you deactivate an account (by unchecking the box) it will no longer be visible in the chart of accounts but can be reactivated later. Only accounts which aren't needed for account entries can be deactivated.

*  *Account Type* : account types determine an account's use in each journal. By default the following types are available: \ ``View``\  , \ ``Receivable``\  , \ ``Payable``\  , \ ``Income``\  , \ ``Expense``\  , \ ``Tax``\  , \ ``Cash``\   *, * \ ``Asset``\  , \ ``Equity``\  . You can add new types through the menu:  *Financial Management > Configuration > *  *Charts of Accounts > Type of Accounts* . Use the \ ``View``\   type for accounts that make up the structure of the charts and have no account data inputs of their own.

.. tip::   **Comment**  *Type of account* 

	The account types are mainly used as an informative title, The only two types that have any particular effect are Receivables and Payables.

	These two types are used by reports on partner credits and debits. They're calculated from the list of unreconciled entries in the accounts of one of these two types.

*  *Account Number* : the code isn't limited in number of digits. Use code 0 for all root accounts.

*  *Currency* : the default currency for that account.

*  *Deferral Method* : determines how to treat the account and its entries at the closing of the books at the end of the year. Four methods are available:

	- Balance: an entry is generated for the account balance and carried across to the new year (generally used for bank accounts),

	- None: no accounting entries are transferred across to the new financial year (generally for classes 6 and 7),

	- Detail: all entries are kept for the new fiscal year,

	- Unreconciled: only unreconciled entries are carried over to the new fiscal year (usually used for third-party accounts).

*  *Reconcile* : determines if you can reconcile the entries in this account. Activate this field for partner accounts and for chequing (checking) accounts.

*  *Parents* : determines which account is the parent of this one, to create the tree structure of the chart of accounts.

*  *Default Taxes* : this is the default tax applied to purchases or sales using this account. It enables the system to generate tax entries automatically when entering data in a journal manually.

The tree structure of the accounts can be altered as often and as much as you wish without recalculating any of the individual entries. So you can easily restructure your account during the year to reflect the reality of the company better.

Using virtual charts of accounts
---------------------------------

The structure of a chart of accounts is imposed by the legislation in effect in the country of concern. Unfortunately that structure doesn't always correspond to the view that a company's CEO needs.

In Open ERP you can use the concept of virtual charts of accounts to manage several different representations of the same accounts simultaneously. These representations can be shown in real time with no additional data entry.

So your general chart of accounts can be the one imposed by the statutes of your country, and your CEO can then have other virtual charts as necessary, based on the accounts in the general chart. For example the CEO can create a view per department, a cash-flow and liquidity view, or consolidated accounts for different companies.

The most interesting thing about virtual charts of accounts is that they can be used in the same way as the default chart of accounts for the whole organization. For example you can establish budgets from your consolidated accounts or from the accounts from one of your companies.

.. tip::   **Advantage**  *Virtual accounts* 

	Virtual accounts enable you to provide different representations of one or several existing charts of accounts. Creating and restructuring virtual accounts has no impact on the accounting entries. You can then use the virtual charts with no risk of altering the general chart of accounts or future accounting entries.

	Because they're used only to get different representation of the same entries they're very useful for:

	* consolidating several companies in real time,

	* depreciation calculations,

	* cash-flow views,

	* getting more useful views than those imposed by statute,

	* presenting summary charts to other users that are appropriate to their general system rights.

	So there are good reasons for viewing the execution of financial transactions through virtual charts, such as budgets and financial indicators based on special views of the company.

To create a new chart of accounts you should create a root account using the menu  *Financial Management > Configuration > General Accounts > Accounts Definition* . Your top level account should have  *Code* \ ``0``\   and  *Type* \ ``View``\  . Then you can choose your structure by creating other accounts of  *Type* \ ``View``\   as necessary. Check your virtual structure using the menu  *Financial Management > Charts > Charts of Accounts* .

Finally, when you've got your structure, you must make the general accounts and virtual accounts match. For that search the general accounts and ensure that each non-\ ``View``\   account there also has a virtual account in the field  *Parents* .

You can then check through your general chart of accounts as well as your virtual charts which give you another representation of the company. All the actions and states in your general account are also available in the virtual accounts.

Finally you can also make virtual charts of accounts from other virtual charts. That can give an additional dimension for financial analysis.

Journals
=========

All your accounting entries must appear in an accounting journal. So you must, at a minimum, create a Sales Journal for customer invoices, a Purchase Journal for supplier invoices and a Cash Journal for cash and bank transactions.

Configuring a Journal
-----------------------

To view, edit or create new journals use the menu  *Financial Management > Configuration > Journals > Definition of Journals* .

Just like General accounts, the journals can be deactivated to make them invisible: uncheck the  *Active*  checkbox for that.


	.. image::  images/account_journal_form.png
	   :align: center

*Definition of an accounting journal*

You have to associate a view with each journal. The journal view indicates the fields that must be visible and required to enter accounting data in that journal. The view determines both the order of the fields and the properties of each field. For example the field  *Account Number*  must appear when entering data in the bank journal but not in the other journals.

Before creating a new view for a journal check that there's nothing similar already defined for another journal. You should only create a new view for new types of journal.

.. tip::   **Note**  *Customizing views* 

	You'll often have to edit a journal view. For example, for a journal in a foreign currency you add a field for the currency and this currency must be in the journal view.

	Conversely, to simplify data entry the journal view for the bank is quite different from one of the invoicing journals.

You can also create a sequence for each journal. This sequence gives the automatic numbering for accounting entries. Or several journals can use the same sequence if you want to define one for them all.

The credit and debit account by default permit the automatic generation of counterpart entries when you're entering data in the journal quickly. For example, in a bank journal you should put an associated bank account for default matching credits and debits, so that you don't have to create counterparts for each transaction manually.

A journal can be marked as being centralized. When you do this, the counterpart entries won't be owned by each entry but globally for the given journal and period. You'll then have a credit line and a debit line centralized for each entry in one of these journals, meaning that both credit and debit appear on the same line.

Controls and aids for data entry
---------------------------------

You can carry out two types of control on Journals in Open ERP – controls over the financial accounts and access controls for groups of users. In addition to these controls you can also apply all of the rights management detailed in Chapter 13.

To avoid mistakes while entering accounts data, you can place conditions in the general accounts about who can use a given account. To do this, you must list all the accounts or valid account types in the second tab,  *Entry Control* . If you haven't added any accounts there, Open ERP applies no restriction on data entry in the accounts or journals. If you list accounts and the types of account that can be used in a journal, Open ERP prevents you from using any account not in that list. This verification step starts from the moment you save the entry.

This functionality is useful for limiting possible data entry errors. Also, in a bank journal it's possible to restrict the accounts that can be linked to a bank to classes 1 to 5. Using this you'd help prevent the user from making any false entries in the journal.

.. tip::   **Advice**  *Control of data entry* 

	In accounting it's not a good idea to allow a data entry directly from bank account A to bank account B. If you enter a transaction from bank A to bank B the transaction will be accounted for twice.

	To prevent this problem, pass the transaction through intermediate account C. At the time of data entry the system checks the type of account that's accepted in the bank journal: only accounts that aren't of type Bank are accepted.

	If your accountant defines this control properly, non-accounting users are prevented from transferring payment from one bank to another, reducing your risks.

Periods and fiscal years
=========================

.. tip::   **Terminology**  *Periods and fiscal years* 

	A fiscal year corresponds to twelve months for a company. In many countries, the fiscal year corresponds to a calendar year but that's not the case in others.

	The fiscal year is divided into monthly or three-monthly accounting periods.

Open ERP's management of the fiscal year is flexible enough to enable you to work on several years at the same time. This gives you several advantages, such as creating three-year budgets, and states straddling several calendar years.

Defining a period or a fiscal year
-----------------------------------

To define your fiscal year use the menu  *Financial Management > Configuration > Periods > Fiscal Year* . You can create several years in advance to define long-term budgets. 


	.. image::  images/account_period.png
	   :align: center

*Defining a financial year and periods*

First enter the date of the first day of your fiscal year and the last day. Then to create the periods click one of the two buttons at the bottom depending on whether you want to create twelve 1-month or four 3-month periods:

*  *Create monthly periods* ,

*  *Create 3-monthly periods* .

Closing the end of the year
-----------------------------

To close the end the year, use the following menu:  *Financial Management > End of year processing > Close a Fiscal Year* . A form opens asking you for the essential information it needs to create entries to start the following year.



When the year is closed you can no longer create or modify any financial transactions in that year. So you should always make a backup of the database before closing the fiscal year. Closing a year isn't obligatory and you could easily do that sometime in the following year when your accounts are finally sent to the statutory authorities, and no further modifications are permitted.


	.. image::  images/account_fy_close.png
	   :align: center

*Closing a financial year*

It's also possible to close an accounting period. You could for example close a monthly period when a tax declaration has been made. When a period is closed you can't modify any of the entries in that period. To close an accounting period use the menu  *Financial Management > End of Year Processing > Close a Period* .

Payment Terms
===============

You can define whatever payment terms you need in Open ERP. Payment terms determine the due dates for paying an invoice.

To define new payment terms, use the menu  *Financial Management > Configuration > Payment Terms > Payment Terms* .

The figure below represents the following payment term: 35% on delivery, the balance 15 days after the end of the month.


	.. image::  images/account_payment_term.png
	   :align: center

*Configuring payment terms*

To configure new conditions start by giving a name to the  *Payment Term*  field. Text that you put in the field  *Description*  is used on invoices, so enter a clear description of the payment terms there.

Then create individual lines for calculating the terms in the section  *Payment Term* . You must give each line a name ( *Line Name* ). These give an informative title and don't affect the actual calculation of terms. The  *Sequence*  field lets you define the order in which the rules are evaluated.

The  *Value*  field enables you to calculate the amount to pay for each line:

* \ ``Percent``\  : the line corresponds to a percentage of the total amount, the factor being given in Amount. The number indicated in the Amount must take a value between 0 and 1.

* \ ``Fixed amount``\  : this is a fixed value given by the  *Amount*  box.

* \ ``Balance``\  : indicates the balance remaining after accounting for the other lines.

Think carefully about setting the last line of the calculation to \ ``Balance``\   to avoid rounding errors. The highest sequence number is evaluated last.

The two last fields,  *Number of Days*  and  *Condition* , enable the calculation of the delay in payment for each line, The delay  *Condition*  can be set to \ ``Net Days``\   or \ ``End of Month``\  . For example if you set it to 15 days from the end of the month Open ERP adds 15 days to today's date and then sets the payment date to be the end of the month that the new date is in. So the payment date for 15 days from month end will be:

* 31 January if today is 5 January,

* 28 February if today is 20 January.

You can then add payment terms to a Partner through the  *Properties*  on the partner form.

Entries at the start of a year
===============================

To upgrade your various accounts, create a Journal of type  *Situation*  in  *Centralized counterpart*  mode to avoid a counterpart on each line.

For each account that needs upgrading, enter account data in the journal. For this operation use the menu  *Financial Management > Entries > Journal Entries* .

You can also use Open ERP's generic import tool if you load the balance of each of your accounts from other accounting software.

