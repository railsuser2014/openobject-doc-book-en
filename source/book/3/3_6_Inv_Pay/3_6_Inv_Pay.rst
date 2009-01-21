
.. 135

From invoice to payment
#######################

Summary

* Basic accounting workflow

* Invoices

* Receipts

* Management reports

* Reconciliation

* Managing payment orders

Keywords

* chart of accounts

* reconciliation

* balance sheet

* tax

* invoices

* credit note

* payments

* statements of account

* cash

 *This chapter traces the basic accounting workflow in Open ERP, from entering an invoice to registering payment. The various operations are described, from the entry of accounting receipts and the treatment of the reconciliation process, including payment orders.* 


Accounting is at the heart of managing a company: all the company's operations have an impact there. It has an informational role (how much cash is there? what debts need to be repaid? what's the stock valuation?) and, because of the information it provides, a reliable and detailed accounting system can and should have a major decision-making role.

In most real companies, accounting is limited to producing statutory reports and satisfying the directors' curiosity about certain strategic decisions, and to printing the balance sheet and the income statement several times a year. Even then there's often several weeks of delay between reality and the report.

.. tip::   **Advice**  *valuing your accounting function* 

	In many small companies, the accounting function is poorly used.

	Not only do you see the data for documents being entered into the system twice, but also the results are often just used to produce legal documentation and periodic printouts, some weeks later, of the balance and income statements.

	By contrast, integrating your accounts with your management system means that you can:

	* reduce data entry effort – you only need do it once,

	* run your processes with the benefit of financial vision: for example in managing projects, negotiating contracts, and forecasting cash flow,

	* easily get hold of useful information when you need it, such as a customer's credit position.

So accounting is too often under-utilized. The information it brings makes it a very effective tool for running the company if it's integrated into the management system. Accounting information really is necessary in all of your company's processes for you to be effective, for example:

* for preparing quotations it's important to know the precise financial position of the client, and to see a history of any delays in payment,

* if a given customer has exceeded their credit limit, accounting can automatically stop further deliveries to the customer,

* if a project budget is 80% consumed but the project is only 20% complete you could renegotiate with the client, or review and reign in the objectives of the project,

* if you need to improve your company's cash flow then you could plan your services projects on the basis of billing rates and payment terms of the various projects, and not just delivery dates – you could work on short-term client projects in preference to R&D projects, for example.

Open ERP's general accounting and analytic accounting handle these needs well because of the close integration between all of the application modules. Furthermore, the transactions, the actions and the financial analyses happen in real time, so that you can not only monitor the situation but also manage it effectively.

The accounting module in Open ERP covers general accounting, analytic accounting, and auxiliary and budgetary accounting. It's double-entry, multi-currency and multi-company.

.. index::
   single: Accounting
.. 

.. tip::   **Terminology**  *Accounting* 

	* General accounting (or financial accounting) is for identifying the assets and liabilities of the business. It's managed using double-entry accounting which ensures that each transaction is credited to one account and debited from another.

	* Analytical accounting (or management accounting, or cost accounting) is an independent accounting system which reflects the general accounts but is structured along axes that represent the company's management needs.

	* Auxiliary accounting reflects the accounts of customers and/or suppliers.

	* Budgetary accounts predefine the expected allocation of resources, usually at the start of a financial year.

.. index::
   single: Accounting; Multi-company
.. 

.. tip::   **Method**  *Multi-company* 

	There is a choice of methods for integrating Open ERP in a multi-company environment:

	* if the companies hold few documents in common (such as products, or partners - any Open ERP resource), you should install separate databases,

	* if the companies share many documents, you can register them in the same database and install Open ERP's multi-company documents to finely manage access rights,

	* it's possible to synchronize specified document types in several databases using the synchro module.

One of the great advantages of integrating accounts with all of the other modules is in avoiding the double entry of data into accounting documents. So in Open ERP an Order automatically generates an Invoice, and the Invoice automatically generates the accounting entries. These in turn generate tax submissions, customer reminders, and so on. Such strong integration enables you to:

* reduce data entry work,

* greatly reduce the number of data entry errors,

* get information in real time and enable very fast reaction times (for bill reminders, for example),

* exert timely control over all areas of company management.

.. tip::   **Advice**  *For accountants* 

	When you create a database you can elect to install only the accounting modules by choosing the Accounting Only profile.

	You should install the web portal. With appropriate rights management, this allows trustees to provide customers with real-time access to their data. It also gives them the opportunity to work on certain documents that have no direct accounting impact, such as budgets.

	This can provide an added-value service that greatly improves the interaction between trustees and their clients.

All the accounts are held in the default currency (which is specified in the company definition), but each account and/or transaction can also have a secondary currency (which is defined in the account). The value of multi-currency transactions is then tracked in both currencies.

Open ERP preparation
=====================

You'll need two databases for this chapter:

* \ ``openerp_ch06X``\  , which should be a restored copy of\ `` openerp_ch02``\  , the database you created through Chapter 2. It's referenced throughout the main body of this chapter because it contains demonstration data that illustrates points made in the chapter.

* \ ``openerp_ch06``\  , which should be a restored copy of \ ``openerp_ch04,``\   the database you created through Chapter 4. You can follow the instructions in this chapter to extend this database, though you'd have to generate your own data to do so.

To be able to backup and restore these databases you'll need to know your super-administrator password.

You'll also need your system's \ ``addons``\   directory to be writable, since you'll load new modules into it later in the chapter – they're not provided in the core 4.2 release of Open ERP.

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

