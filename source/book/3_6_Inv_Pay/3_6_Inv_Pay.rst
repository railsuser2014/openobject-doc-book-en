

From invoice to payment
#########################

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

.. tip::   **Terminology**  *Accounting* 

	* General accounting (or financial accounting) is for identifying the assets and liabilities of the business. It's managed using double-entry accounting which ensures that each transaction is credited to one account and debited from another.

	* Analytical accounting (or management accounting, or cost accounting) is an independent accounting system which reflects the general accounts but is structured along axes that represent the company's management needs.

	* Auxiliary accounting reflects the accounts of customers and/or suppliers.

	* Budgetary accounts predefine the expected allocation of resources, usually at the start of a financial year.

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

Accounting workflow and the automatic generation of invoices
=============================================================

The chart below shows the financial workflow followed by each invoice.

	.. image::  images/account_flow.png

*Accounting workflow for invoicing and payment*


In general, when you use all of Open ERP's functionality, invoices don't need to be entered manually. Draft invoices are generated automatically from other documents such as Purchase Orders.

Draft Invoices
---------------

The system generates invoice proposals which are initially set to the \ ``Draft``\   state. While these invoices remain unconfirmed they have no accounting impact within the system. There's nothing to stop users creating their own invoices if they want to.

The information that's needed for invoicing is automatically taken from the Partner form (such as payment conditions and the invoice address) or from the Product (such as the account to be used) or from a combination of the two (such as applicable Taxes and the Price of the product).

.. tip::   **Advantage**  *Draft invoices* 

	There are several advantages in working with Draft invoices:

	* You've got an intermediate validation state before the invoice is approved. This is very useful when your accountants aren't the people creating the initial invoice, but are still required to approve it before the invoice is entered into the accounts.

	* This enables you to create invoices in advance, without approving them at the same time. You're also able to list all of the invoices awaiting approval.

Open or Pro-Forma Invoices
---------------------------

It's possible to approve (or validate) an invoice in the \ ``Open``\   or \ ``Pro Forma``\   state. A Pro Forma invoice doesn't yet have an invoice number, but the accounting entries on the invoice that's created correspond to the amounts that Open ERP will record as the customer's payables.

.. tip::   **Comment**  *Pro Forma invoices* 

	In some countries, you're not allowed to generate accounting entries from pro forma invoices. You create instead a report from the purchase order, which prints a pro forma invoice, which has no accounting consequences within the system. 

	You can use the module described in Chapter 13 to create this report.

An open invoice has a unique invoice number. The invoice is sent to the customer and is marked on the system as awaiting payment.

Reconciling invoice entries and payments
-----------------------------------------

In Open ERP an invoice is considered to be paid when its accounting entries have been reconciled with the payment entries. If there hasn't been a reconciliation an invoice can remain in the open state until you have entered the payment.

.. tip::   **Attention**  *Payment and reconciliation* 

	To avoid surprises, it's important to understand the idea of reconciliation and its link with invoice payment.

	You'll find both a Reconciled field and the Paid checkbox on an invoice. They differ from each other only if an invoice has been paid (using reconciliation of records) but has subsequently been marked as unreconciled

.. tip::   **Terminology**  *Reconciliation* 

	Reconciliation links entries in a single account that cancel each other out – they're reconciled to each other (sum of credits = sum of debits).

	This is generally applied to payments against corresponding invoices.

Without the reconciliation process, Open ERP would be incapable of marking invoices that have been paid. Suppose that you've got the following situation for the Smith and Offspring customer:

* Invoice 145: 50,

* Invoice 167: 120,

* Invoice 184: 70.

If you receive a payment of 120, Open ERP will delay reconciliation because there's a choice of invoices to pay. It could either reconcile the payment against invoices 145 and 184 or against invoice 167.

You can cancel an invoice if the  *Allow Cancelling Entries*  function has been activated in the journal and the entries haven't yet been reconciled. You could then move it from \ ``Canceled``\  , through the \ ``Draft``\   state to modify it and regenerate it.

.. tip::   **Note**  *Treatment in Lots* 

	Usually, different transactions are grouped together and handled at the same time rather than invoice by invoice. This is called batch work or lot handling.

	You can select several documents in the list of invoices: check the checkboxes of the interesting lines using the web client and click the appropriate shortcut button at the right; or shift-click the lines using the mouse in the GTK client and use the action or print button at the top – these give you the option of one of a number of possible actions on the selected objects.

At regular intervals, and independently of the invoices, an automatic import procedure or a manual accounts procedure can be used to bring in bank statements. These comprise all of the payments of suppliers and customers and general transactions, such as between accounts.

When an account is validated, the corresponding accounting entries are automatically generated by Open ERP.

Invoices are marked as paid when accounting entries on the invoice have been reconciled with accounting entries about their payment.

This reconciliation transaction can be carried out at various places in the process, depending on your preference:

* at data entry for the accounting statement,

* manually from the account records,

* automatically using Open ERP's intelligent reconciliation.

You can create the accounting records directly, without using the invoice and account statements. To do this, use the rapid data entry form in a journal. Some accountants prefer this approach because they're used to thinking in terms of accounting records rather than in terms of invoices and payments.

You should really use the forms designed for invoices and bank statements rather than manual data entry records, however. These are simpler and are managed within an error-control system.

A records-based system
-----------------------

All the accounting transactions in Open ERP are based on records, whether they're created by an invoice or created directly.

So partner reminders are generated simply from the list of unreconciled entries in the trade receivables account for that partner. In a single reminder you'll find the whole set of unpaid invoices as well as unreconciled payments, such as advances.

Similarly, financial statements such as the general ledger, account balance, aged balance (or chronological balance) and the various journals, are all based on accounting entries. It doesn't matter if you generated the entry from an invoice form or directly in the invoice journal. It's the same for the tax declaration and other statutory financial statements.

When using integrated accounting, you should still go through the standard billing process because some modules are directly dependent on invoice documents. For example, a customer sale order can be configured to wait for payment of the invoice before triggering a delivery. In such a case, Open ERP automatically generates a draft invoice to send to the client.

Invoicing
===========

In Open ERP, the concept of “invoice” includes the following documents:

* the customer invoice,

* the supplier invoice,

* a customer credit note,

* a supplier credit note.

Only the invoice type and the representation mode differ for each of the four documents. But they're all stored in the same object type in the system.

You get the correct form for each of the four types of invoice from the menu you use to open it. The name of the tab enables you to tell the invoice types apart when you're working on them.

.. tip::   **Technique**  *Types of invoice* 

	There are many advantages in deriving the different types of invoice from the same object. The two most important are:

	* In a multi-company environment with inter-company invoicing, a customer invoice in one company becomes a supplier invoice for the other.

	* This enables you to work and search for all invoices from the same menu. If you're looking for an invoicing history, Open ERP provides both supplier and customer invoices in the same list, as well as credit notes.

.. tip::   **Terminology**  *Credit Note* 

	A credit note is a document that enables you to cancel an invoice or part of an invoice.

To access invoices in Open ERP, use the submenus of  *Financial Management > Invoices* .

Most of the time, invoices are generated automatically by Open ERP as they are generated from other processes in the system. So it's not usually necessary to create them manually, but simply approve or validate them. Open ERP uses the following different ways of generating invoices: 

* from Supplier or Customer Orders,

* from reception or despatch of goods,

* from work carried out (timesheets, see chapter 10),

* from closed tasks (see chapter 12),

* from fee charges or other rechargeable expenses (see chapter 11).

The different processes generate \ ``Draft``\   invoices. These must then be approved by a suitable system user and sent to the customer. The different invoicing methods are detailed in the following sections and chapters.

To get the list of draft invoices generated by Open ERP, you can use the menu  *Financial Management > Invoices > Customer Invoices > Draft Customer Invoices* . You'll find a similar menu for Purchase Invoices that haven't yet been received or approved:  *Financial Management > Invoices > Supplier Invoices > Draft Supplier Invoices* .

It's also possible to enter invoices manually. This is usually done for invoices that aren't associated with an Order (usually purchase orders) or credit notes. Also if the system hasn't been configured correctly you might need to edit the invoice before sending it to the customer.

For example, if you haven't noted that the customer is tax-exempt, the invoice you generate from an Order will contain tax at the normal rates. It's then possible to edit this out of the invoice before validating it.

Entering a customer invoice
-----------------------------

The principle of entering data for invoices in Open ERP is very simple, as it enables non-accountant users to create their own invoices. This means that your accounting information can be kept up to date all the time as orders are placed and received, and their taxes are calculated.

At the same time it allows people who have more accounting knowledge to keep full control over the accounting entries that are being generated. Each value proposed by Open ERP can be modified later if needed. 

Start by manually entering a customer invoice. Use  *Financial Management > Invoices > Customer Invoices*  for this.

A new invoice form opens for entering information.

	.. image::  images/account_invoice_new.png
	
*Entering a new invoice*


The document is composed of three parts:

* the top of the invoice, with customer information,

* the main body of the invoice, with detailed invoice lines,

* the bottom of the page, with detail about the taxes, and the totals.

To enter a document in Open ERP you should always fill in fields in the order that they appear on screen. Doing it this way means that some of the later fields are filled in automatically from the selections made in earlier fields. So select the Partner, and the following fields are completed automatically:

* the invoice address corresponds to the partner contact that was given the address type of \ ``Invoice``\   in the partner form (or otherwise the address type of \ ``Default``\  ),

* the partner account corresponds to the account given in the Properties which is found in the third tab of the partner form. By default the software is configured with account \ ``Accounts Receivable``\  .,

* a payment condition can be specified for this case or, if it's been defined by default, in the  *Properties*  area of the partner form. Payment conditions are generated by rules for the payment of the invoice. For example: 50% in 21 days and 50% in 60 days from the end of the month. 

.. tip::   **Definition**  *Properties fields* 

	The Properties fields on the Partner form or the Product form are multi-company fields. The value that the user sees in these fields depends on the company that the user works for.

	If you work in a multi-company environment that's using one database, you have several charts of accounts. Asset and liability accounts for a partner depend on the company that the user works for.

.. tip::   **Note**  *Seeing partner relationships* 

	You can always reach more information from a relation field in Open ERP. In the web client a relation is a hyperlink if the form is read-only – it takes you to the main form for that entity, with all of the actions and links. In the web client in edit mode, and in the GTK client, you can press the keyboard Ctrl button at the same time as right-clicking in the field to get a drop-down dialog with links and other options. So you could click on a partner field to rapidly get the partner's:

	* current sales and purchases,

	* CRM requests,

	* open invoices,

	* accounts records,

	* payable and receivable accounts.

You can then add a short Description to the invoice and select the currency that you want to invoice in.

.. tip::   **Attention**  *Invoice Description* 

	The invoice description is more of a title than a comment. If you want to add more detailed comments you can use the Notes field at the bottom of the second tab Other Information.

Once the invoice heading is saved you must enter the different invoice lines. You could use either of two techniques:

* enter the whole field manually,

* use a product to complete the different fields automatically.

So select the product \ ``Titanium Alloy Radiator``\   in the product field in an invoice line. The following fields are then completed automatically:

*  *Description* : this comes from the product, in the language of the partner,

*  *Credit/debit account* : determined by the purchase or sales account defined in the product properties. If no account is specified in the product form, Open ERP use the properties of the category that the product is associated with.

*  *Unit of Measure* : this is defined by default in the product form,

*  *Unit price* : this is given by the list price in the product form and is expressed without taxes,

*  *Taxes* : provided by the product form and the partner form.

.. tip::   **Note**  *Managing the price with tax included* 

	By default, Open ERP invoices and processes the price without taxes – they're managed as a separate figure. If you want to have invoices provided with tax included you can install the module account_tax_include.

	The module adds a field on each invoice that enables you to indicate if the invoice is tax exclusive or tax inclusive.

.. tip::   **Note**  *Information about the product* 

	When you're entering invoice data it can sometimes be useful to get hold of more information about the product you're invoicing. Since you're already in edit mode, you'd press the Ctrl key and use a right mouse-click on the Product field (in both the web and the GTK clients). Then select the available reports. Open ERP provides three standard reports about the product

	* forecasts of future stock,

	* product cost structure,

	* location of the product in your warehouses.

It's possible to enter several invoice lines and modify the values that are automatically suggested by Open ERP.

Once the invoice lines have been entered, you can click  *Calculate*  on the invoice to get the following information:

* details of tax calculated,

* tax rate,

* total taxes,

* total price.

In the  *Taxes*  area at the bottom left of the invoice you'll find the details of the totals calculated for different tax rates used in the invoice.

.. tip::   **Technique**  *Tax Calculations* 

	You can double-click on one of the lines in the tax summary areas in the invoice.

	Open ERP then shows you the detail of the tax charges which will effectively be your tax declaration at the end of the month.

	It shows you the total that will be computed in the different parts of the legal declaration. This enables you to manage the declaration in Open ERP automatically.


	.. image::  images/account_invoice_tva.png

*Detail of tax charges on an invoice*

Before approving the invoice you can modify the date and the accounting period, which are entered by default as today's date. These fields are found on the second tab  *Other Information* .

.. tip::   **Note**  *Invoice layout* 

	If you want to make your invoice layout more elaborate you can install the module account_invoice_layout. This enables you to add various elements between the lines such as subtotals, sections, separators and notes.

Click  *Validate*  when you want to approve the invoice. It moves from the \ ``Draft``\   state to the \ ``Open``\   state.

When you've validated an invoice, Open ERP gives it a unique number from a defined sequence. By default it takes the form \ ``Year / Sequence Number``\   for example \ ``2008/00101``\  . If you want to modify the sequence numbers use the menu  *Administration > Custom > Sequences > Sequences* .

Accounting entries corresponding to this invoice are automatically generated when you approve the invoice. You can verify the detail of this by clicking the  *Open*  icon for the  *Transactions*  field in the second tab of the invoice.

Managing taxes
^^^^^^^^^^^^^^^

Details on the product form and the partner form determine the selection of applicable taxes for an invoice line. By default Open ERP takes account of all the taxes defined in the product form. If a tax is defined in the Properties tab of the Partner form then Open ERP will base its tax calculation on the Partner taxes instead, so a Partner that is defined as tax-exempt, for example, will take precedence over taxes defined in the Product.

Take the case of the following product

* Applicable taxes:

	- TVA: 19.6% type TVA

	- DEEE: 5.5, type DEEE


.. tip::  **Definition**  *DEEE tax*

	The DEEE tax (disposal of electronic and electrical equipment) is an ecological tax that was imposed in France from 2007. It's applied to batteries to finance their recycling and is a fixed sum that's applied to the before-tax figure on the invoice

If you trade with a company in your own country, and your country has a DEEE-type tax, the applicable taxes for this invoice will be:

* DEEE: 5.5,

* TVA: 19.6%.

If you sell to a customer in another company in the community (intracommunity), instead, then tax is not charged. Your foreign partners would then be zero-rated by selecting a 0% tax in the 4th tab,  *Properties* . When you create an invoice for this customer, Open ERP will calculate the following taxes on the product:

* DEEE: 5.5,

* TVA intracommunity: 0%.

If you haven't coded the parameters in the customer form correctly, Open ERP will suggest incorrect taxes in the invoice. That's not an insuperable problem because you can always modify the information directly in the invoice before approving it.

.. tip::   **Advice**  *Occasional invoices* 

	When you create an invoice for a product that will only be bought or sold once you don't have to encode a new product. But you'll have to provide quite a bit of information manually on the invoice line:

	* sale price,

	* applicable taxes, 

	* account,

	* product description.

Cancelling an invoice
^^^^^^^^^^^^^^^^^^^^^^^

By default Open ERP won't allow you to cancel an invoice once it has been approved. Since accounting entries have been created you theoretically can't go back and delete them. However in many cases it's more convenient to cancel an invoice when there's an error than to produce a credit note and reconcile the two entries. Your attitude to this will be influenced by current legislation in your accounting jurisdiction and your adherence to accounting purity.

Open ERP accommodates either approach. Canceling an invoice can be permitted by checking the box  *Allow Cancelling Entries*  in the Journal corresponding to this invoice. You'll then be allowed to cancel the invoice if the following two conditions are met:

	#. The accounting entries haven't been reconciled or paid: if they have then you'll have to cancel the reconciliation. 

	#. The accounting period or the fiscal year hasn't already been closed: if it has then no modification is possible.

Cancelling an invoice has the effect of automatically modifying the corresponding accounting entries.

When the invoice has been canceled you then have the possibility of putting it back into the \ ``Draft``\   state. This means that you can modify it and approve it again later.

.. tip::   **Advice**  *Numbering invoices* 

	Some countries require you to have contiguously number invoices with no break in the sequence. If, after canceling an invoice that you're not regenerating, you find yourself with a break in the numbering you must go and modify the sequence, redo the invoice and replace the sequence number with its original value.

	You can control the sequences using the menu Administration > Custom > Sequences > Sequences.

Attention: canceling an invoice will cause a break in the number sequence of your invoices. You're strongly advised to recreate this invoice and re-approve it to fill the hole in the numbering.

.. tip::   **Advantage**  *Duplicating a document* 

	The duplication function can be applied to all the system documents: you can duplicate anything – a product, an order, or a delivery.

----------------

	.. note::  *Some points* 

		#. Duplicating invoices

			Instead of entering a new invoice each time, you can base an invoice on a similar preceding one and duplicate it. To do this, first search for a suitable existing one. In the web client, show the invoice in read-only (non-editable) form view, then click Duplicate. In the GTK client, select Form > Duplicate from the top menu.

			The duplication creates a new invoice in the Draft state. That enables you to modify it before approving it. Duplicating documents in Open ERP is an intelligent function, which enables the duplicated invoice to be given its own sequence number, today's date, and the draft state, even if the preceding invoice has been paid.

		#. Saving partner preferences

			Open ERP has many functions to help you enter data quickly. If you invoice the same products frequently for the same partner you can save the last invoice preferences using conditional default values.

			To test this functionality, create an invoice for a given partner and add several lines. Then click on the name on an invoice line and select Make this a default value. Check the box that indicates this default should apply only to this partner.

			Then the next time you establish an invoice for this partner the invoice lines will be automatically created and you'll only have to modify the quantities before confirming the invoice.

			For taxes you're advised to put the default amount in the invoice lines (in France it would be 19.6%, in Belgium 21%, in the UK 17.5%). Doing this you won't forget to add tax when you're manually entering invoices.

		#. Getting information from a right-click

			As you're creating an invoice you'll often find you need extra information about the partner to help you complete the invoice. In Open ERP to obtain more information on any field all you need do is hold down the Ctrl key and click the right button on the mouse, and then Open ERP will automatically show you information linked to this partner, such as: 

			* tasks completed

			* benefit details

			* most recent invoices

			* latest orders

			Do the same to get information about the products you're invoicing,. For example: is there enough stock? When will you be getting more stocks in? What are the costs and normal list prices for this product?

			By making this information easily accessible while you're invoicing, Open ERP greatly simplifies your work in creating the invoice.

Creating a supplier invoice
-----------------------------

The form that manages supplier invoices is very similar to the one for customer invoices. However, it's been adapted to simplify rapid data entry and monitoring of the amounts recorded.

.. tip::   **Method**  *Entering data* 

	Many companies don't code up supplier invoices but simply enter accounting data corresponding to the purchase journal.

	This particularly applies to users that have focused on the accounting system rather than all the capabilities provided by an ERP system. The two approaches reach the same accounting result: some prefer one and others prefer the other depending on their skills.

	However, when you use the Purchase Management functions in Open ERP you should work directly on invoices because they provide Purchase Orders or Goods Receipt documents.

To encode a new supplier invoice, use the menu  *Financial Management > Invoices > Supplier Invoice* .

Everything is similar to the customer invoice, starting with the  *Journal*  and then the  *Partner* , which will automatically complete the following fields

*  *Invoice address* , 

* partner *Account* :

Unlike the customer invoice you don't have to enter payment conditions – simply a  *Due Date* . And if you don't give a due date, Open ERP assumes that this invoice will be paid in cash. If you want to code in more complete payment conditions than just due date you can use the  *Payment Term*  field which you can find on the second tab,  *Other Info* .

After that you enter the invoice  *Total*  with taxes included. Open ERP uses this amount to check whether all invoice lines have been entered correctly before it will let you validate the invoice.

Indicate the  *Currency*  if the invoice isn't going to use the default currency, then you can enter the  *Invoice lines* .

Just like the customer invoice you have the choice of entering all the information manually or using a product to complete many of the fields automatically. Entering a product, all of the following values are completed automatically:

* the product  *Account*  is completed from the properties of the product form or the Category of the product if nothing is defined on the product itself,

* the  *Taxes*  come from the product form and/or the partner form, based on the same principles as the customer invoice,

* the  *Quantity*  is set at 1 by default but can be changed manually,

* the  *Unit Price*  is calculated automatically from the total price after deducting all the different applicable taxes,

Click  *Calculate*  to verify that the different amounts correspond to those indicated on the paper invoice from the supplier. When you approve the invoice, Open ERP verifies that the total amount indicated in the header correspond to the sum of the amounts without tax on the invoice lines and the different applicable taxes.

.. tip::   **Note**  *The Calculate button* 

	Even though you should calculate the invoice before approving it you don't have to push the Calculate button. If you approve the invoice directly the software calculates the different taxes itself and verifies the total.

	This button is only used for making a pre-check of the amount displayed before you confirm it finally.

Open ERP automatically completes the  *Date Invoiced*  and the accounting period, but you can still change these values manually in the second tab on the invoice before saving it.

.. tip::   **Terminology**  *Dates and Accounting Periods* 

	Accounting periods are treated as legal period declarations. For example a tax declaration for an invoice depends on the accounting period and not on the date of invoicing.

	Depending on whether your declarations are made monthly or quarterly, the fiscal year contains either twelve or four accounting periods.

	The dates are shown in the document you created in the accounting system. They're used for calculating due dates.

The two pieces of information don't have to have the same date. Suppose for example that you receive an invoice on the 5th January but it's dated 31st December in the previous year by your supplier. In this case you can code it into the January accounting period and put the invoice date as 31st December. The due date will be based on the 31st December data, but the invoice will be recognized in the current fiscal year for the tax declaration.

You can find that the amounts don't correspond with what your supplier has given you on paper for reasons that can include:

* the supplier made a calculation error,

* the amounts have been rounded differently.

.. tip::   **Technique**  *Rounding Tax* 

	It often happens that a supplier adds 1 to the total because the tax calculation has been rounded upwards. Some tax amounts aren't valid because of this rounding.

	For example it's impossible to arrive at the amount of 145.50 if you're working to a precision of 2 decimal places and a rate of 19.6%:

	* 121.65 x 1.196 = 145.49

	* 121.66 x 1.196 = 145.51

In this case you can modify a value in the lines that the total's based on, or the total amount of taxes at the bottom left of the form: both are editable so that you can modify them to adjust the total.

When the totals tally you can validate the invoice. Open ERP then generates the corresponding accounting entries. You can manage those entries using the  *Account*  fields on the invoice and on each of the invoice lines. 

Credit Notes
-------------

Entering a customer credit note is almost identical to entering a customer invoice. You just start from the menu  *Financial Accounting > Invoices > Customer Refunds* .

Similarly, entering a supplier credit note is the same as that of the supplier invoice and so you use the menu  *Financial Accounting > Invoices > Supplier Refunds* .

It's easy to generate a credit note quickly from an existing invoice. To do this, select a customer or supplier invoice and click  *Refund invoice*  on the toolbar to the right. Open ERP opens a new credit note form for you in the \ ``Draft``\   state so that you can modify it before approval.

.. tip::   **Note**  *Crediting several invoices* 

	You can refund several invoices in one operation. From the web client you'd display a list of invoices and then click the checkboxes alongside the ones you want to refund. Then click the Refund invoice action from the Right toolbar. 

	In the GTK client you'd make a multiple selection of invoices by Ctrl-clicking whichever lines you want to select. Then you'd execute the action by clicking the Action (gears) icon on the icon toolbar and selecting Refund invoice.

Invoice payment
-----------------

The invoice is automatically marked as paid by Open ERP once invoice entries have been reconciled with payment entries. You yourself don't have to mark the invoices as paid: Open ERP manages that when you reconcile your payments.

.. tip::   **Advice**  *Reconciling a credit note* 

	Generally you reconcile the invoice's accounting entries with their payment(s). But you can also reconcile an invoice with the entries from the corresponding credit note instead, to mutually cancel them.

You've probably noticed the  *Pay Invoice*  action button in the toolbar to the right of the invoice form. This lets you enter payments and get entries reconciled very quickly. This functionality is usually employed by companies that use Open ERP as a simple billing system and not for complete accounting. They encode their payment on different invoices manually.

You probably shouldn't use this functionality if you have all of your accounting in Open ERP. It's much more convenient to manage the payment of invoices when you're entering bank statements and cash transactions. These allow better control of financial transactions and permit greater flexibility in areas such as:

* advance and partial payments of invoices,

* payment of several invoices by several payments,

* fine-grained management of different due dates on the same invoices,

* management of adjustments if there are different amounts to those on the invoice.

Accounting entries
===================

Various methods of creating accounting entries can be used. You've already seen how an invoice creates its own entries, for example.

This section deals, in order, with

* managing bank statements,

* managing cash,

* manual journal entries,

You'll see here how to proceed with entering financial transactions. In Open ERP you use the same form for handling bank statements and for managing cash. The two types of transaction differ only in the journal that's used.

Managing bank statements
-------------------------

Open ERP provides a visual tool for managing bank statements that simplifies data entry into accounts. As soon as a statement entry is validated the corresponding accounting entries are automatically generated by Open ERP. This lets non-accounting people to enter financial transactions without fussing about such things as credit, debit and counterparts

Start by entering a statement line. To do that use the menu  *Financial Management > Entries > Statements* . A data entry form for statements then opens.

	.. image::  images/account_statement.png
	
*Data entry form for a bank statement*


The statement reference ( *Name* ) and the  *Date*  are automatically suggested by Open ERP from the preceding statement line. You can configure your own reference by managing sequences in the Administration menu.

You must then select the  *Journal* . Ideally, when you're configuring your company you'd create at least one journal for each bank account and one journal for petty cash in your company. So select the journal corresponding to the bank account whose statement you're handling.

The currency that you're using for the statement line is that of the selected journal. If you're entering statement lines for an account in American dollars (USD) the amounts must be entered in \ ``USD``\  . The currency is automatically converted to the company's main currency when you confirm the entry, using the rates in effect at the date of entry (which means that you'd need valid currency conversion rates to be created first).

The initial balance is completed automatically by Open ERP based on the final balance of the preceding statement. You can modify this value and force another value. This enables you to enter statements in the order of your choice. Also if you've lost a page of your statement you can enter the following ones immediately and you're not forced to wait for a duplicate from the bank.

So, complete the final balance, which corresponds to the last value on the account after all of the statement entries. This amount will be the control for operations before approving the statement.

Then you must enter all the lines on the statement. Each line corresponds to a banking transaction.

Enter the transaction line. When you type the Partner name, Open ERP automatically proposes the corresponding account. The total amount due for the customer or supplier is pre-completed by Open ERP ( *Amount* ). This gives you a simple indication of the effective payment. You must the enter the amount that appears on your statement line: a negative sign for a withdrawal and a positive sign for a cash payment or deposit.

When the payment entry has been made it's possible to reconcile this directly with the accounting entry for the invoices. Press the  *Ctrl*  key on the keyboard (necessary for the web client, though not the GTK client) and then press the  *F1*  key while your cursor is in the  *Reconcile*  field on the payment line.


	.. image::  images/account_statement_reconcile.png
	
*Reconciliation from data entry of the bank statement*

The reconciliation form then appears. To the right you'll find the amount for payment. You must then select the invoices paid by this transaction (Entries). To enable you to reconcile this the amount of payment must correspond exactly with one or several due dates of invoice.

.. tip::   **Method**  *Reconciliation* 

	Other methods of reconciliation are possible: from accounting entries, when saving the payment directly on an invoice, or using the automatic reconciliation tool. But if you can, you should do a reconciliation when you're encoding the payment because that's the time when you have all of the information you need to hand for reconciling the payment with the corresponding invoice

.. tip::   **Attention**  *Partial reconciliation* 

	In Open ERP, only total reconciliation is possible. To enter a partial payment for an invoice, several methods are given you:

	* Don't reconcile that payment amount, just reconcile the entire balance. 

	* Reconcile at once, but make an accounting adjustment in the partner's credit account. In this case the invoice will be marked as paid.

If you see a difference between the payment and the invoices to reconcile, you can note the difference in the second part of the form –  *Write-off* . You must then indicate which account should be used for the adjustment. The main reasons explaining the difference are usually:

* losses and profits,

* exchange differences,

* discounts given for rapid payment.

When the reconciliation is complete, that's to say that the payment is equal to the sum of the due payments and the adjustments then you can close the reconciliation form.

The reconciliation operation is optional – you could very well do it later or not do it at all. It's got two significant effects, however:

* marking that the invoices have been paid,

* preventing the payment and invoice amounts from appearing on customer reminder letters. Unless you've reconciled them the customer will see the invoice and payment amounts on her reminder letter (which won't alter the balance due since they'll just cancel each other out).

Finally, once you have entered the various lines of your bank statement you can validate it. Open ERP then automatically generates the corresponding accounting entries if the balance calculated equals the final balance indicated in the header. The reconciled invoices are marked as paid at that point.

A user with advanced accounting skills can enter accounting entries directly into the bank journal. The resulting account is the same but the operation is more complex because you must know the accounts to use and must have mastered the ideas of credit and debit.

Cash Management
-----------------

To manage cash, you use the same form as before. At the start of the day you must indicate the opening amount of cash in the entry (starting balance). Instead of confirming the entry immediately you can let it remain in the Draft state.

All the transactions throughout the day are then entered in this statement. When you close the cash till, generally at the end of the day, you must enter the amount found in the cash till in the field  *Final Balance* . Then confirm the statement to close the day's cash statement and automatically generate the corresponding accounting entries.

.. tip::   **Attention**  *Validating the statement* 

	Accounting entries are only generated when the statement is confirmed. So if the total statement hasn't been approved (that's to say at the end of the day, in the case of petty cash) you shouldn't be surprised if partner payments haven't been deducted from their corresponding account.

Manual entry in a journal
---------------------------

Invoices and statements produce accounting entries in different journals. But you could equally create entries directly in a journal without using the forms to help you. This functionality is often used for various entry transactions.

To do this, use the following menu:  *Financial Management > Entries > Journal Entries* . You can also use the menu  *Open Journals* , which is a shortcut from the journals or periods which already have accounting entries but which haven't yet been closed.

Select the journal and the accounting period. A window opens, enabling you to enter the accounting data in an editable list. You can then enter data from a supplier invoice.

As you'll recall, these entries are usually generated automatically by Open ERP. If you haven't created an invoice you'll have to enter values manually.

Fill these fields manually in this order:

*  *Effective Date* : invoice date,

*  *Move* : leave this empty so that Open ERP can fill it in automatically from the next number in sequence for line validations,

*  *Ref.* : reference from the supplier invoice,

*  *Partner Ref.* : partner concerned,

*  *Account* : account for the purchase line (\ ``Products Purchase``\  ),

*  *Name* : description of the invoice line (Titanium Alloy Radiator),

*  *Credit* : \ ``1196``\  .

Press the Enter key on your keyboard to validate this first line. The next sequence number is assigned to your accounting entry. Your line is then colored red and takes the \ ``Draft``\   state. When a line is in the draft state then it's not yet reflected in the accounts. Open ERP won't validate that line until the balancing entry is made (so the credit amounts must balance the debit amounts for that set of entries).

Open ERP now proposes the balancing accounting line to be filled in. If the account used (in this case account \ ``600``\  ) includes taxes by default in its definition Open ERP automatically proposes taxes associated with the amount entered. At this stage you can modify and validate this second line of the account, or replace it with other information such as a second purchase line.

When you've entered all of the data from your lines, Open ERP automatically proposes counterpart entries to you, based on the credit entries. If you validate it, the accounting entries are all matched together and the lines move from the \ ``Draft``\   state (red) to the \ ``Open``\   state (black).

.. tip::   **Note**  *Completing a balancing entry* 

	When an accounting entry is matched, Open ERP moves it to the open state automatically and prepares to enter the next data.

	If you want to add some other balancing lines you can enter the number of the entry on the new line that you're entering. In this case the whole line stays at Draft until the whole set balances to zero.

Process of reconciliation
---------------------------

The reconciliation operation consists of matching entries in different accounts to indicate that they are related. Generally reconciliation is used for:

* matching invoice entries to payments so that invoices are marked as paid and customers don't get payment reminder letters (reconciliation in a customer account),

* matching deposits and chequewithdrawals with their respective payments,

* matching invoices and credit notes to cancel them out.

A reconciliation must be carried out on a list of accounting entries by an accountant, so that the sum of credits equals the sum of the debits for the matched entries.

Reconciliation in Open ERP can only be carried out in accounts that have been configured as reconcilable (the  *Reconcile*  field).

.. tip::   **Don't confuse**  *Account reconciliation and bank statement reconciliation* 

	It's important not to confuse the reconciliation of accounting entries with bank statement reconciliation. The first consists of linking account entries with each other, while the second consists of verifying that your bank statement corresponds with the entries of that account in your accounting system.

There are different methods of reconciling entries. You've already seen the reconciliation of entries while doing data entry in an account. Automatic and manual reconciliations are described here.

Automatic reconciliation
^^^^^^^^^^^^^^^^^^^^^^^^^

For automatic reconciliation, you'll be asking Open ERP to make its own search for entries to reconcile in a series of accounts. It tries to find entries for each partner where the amounts correspond.

Depending on the level of complexity that you choose when you start running the tool, the software could reconcile from two to nine entries at the same time. For example, if you select level 5, Open ERP will reconcile three invoices and two payments if the total amounts correspond.


	.. image::  images/account_reconcile_auto.png

*Form for automatic reconciliation*

To start the reconciliation tool, click  *Financial management > Periodical Processing > Reconciliation > Automatic Reconciliation* .

A form opens, asking you for the following information:

*  *Account to reconcile* : you can select one, several, or all reconcilable accounts,

* the period to take into consideration ( *Start of Period*  /  *End of Period* ),

* the  *Reconciliation Power*  (from \ ``2``\   to \ ``9``\  ),

* information needed for the adjustment (details for the  *Write-Off Move* ).

.. tip::  

	You can reconcile:

	* all the Accounts Receivable – your customer accounts of type Debtor,

	* all the Accounts Payable – your supplier accounts of type Creditor.

The adjustment option enables you to reconcile entries even if their amounts aren't exactly equivalent. For example, Open ERP permits foreign customers whose accounts are in different currencies to have a difference of up to 0.50 units of currency and put the difference in a write-off account.

.. tip::   **Attention**  *Limit of write-off adjustments* 

	You shouldn't make the adjustment limits too large. Companies that introduced substantial automatic write-off adjustments have found that all employee expense reimbursements below the limit were written off automatically!

.. tip::   **Note**  *Default values* 

	If you start the automatic reconciliation tool regularly you should set the default values for each field by pressing the Ctrl key and using the right-click mouse button (when the form is in edit mode using the web client, or just using the GTK client). This means that you won't have to re-type all the fields each time.

Manual reconciliation
^^^^^^^^^^^^^^^^^^^^^^^

For manual reconciliation, open the entries for reconciling an account through the menu  *Financial Management > Periodical Processing > Reconciliation > Manual Reconciliation* . You can also call up manual reconciliation from any screen that shows accounting entries.

Select entries that you want to reconcile. From the selection, Open ERP indicates the sum of debits and credits for the selected entries. When these are equal you can click the  *Reconcile Entries*  button to reconcile the entries.

	.. note::  *Example Real case of using reconciliation* 

			Suppose that you're entering customer order details. At the moment you ask “what's outstanding on the customer account ?” (that is the list of unpaid invoices and unreconciled payments). To review it from the order form, right-click the mouse button on the Partner field and select the view Receivables and Payables. Open ERP opens a history of unreconciled accounting entries on screen.


	                .. image::  images/account_sample2_entries.png
	                    :scale: 80
	                

			You notice an invoice for 1900 and a payment two weeks later of 1900 with the same reference. You can select the two lines in that view. The total at the bottom of the page shows you that the credit amount equals the debit amount for the selected line. Click Reconcile Entries to reconcile the two lines.

			After this these lines can't be selected and won't appear when the entries are listed again. If there's a difference between the two entries, Open ERP suggests that you make an adjustment. This adjustment is a compensating entry that enables a complete reconciliation. You must therefore specify the journal and the account to be used for the adjustment.

For example, if you want to reconcile the following entries:



.. csv-table:: **Entries for reconciliation**
   :header: "Date","Ref.","Description","Account","Debit","Credit"
   :widths: 12, 5, 15, 5,5,5
   
   "12 May 08","FAC23","Car hire","4010","544.50",""
   "25 May 08","FAC44","Car insurance","4010","100.00",""
   "31 May 08","PAY01","Invoices n° 23, 44","4010","","644.00"
   
On reconciliation, Open ERP shows a difference of 0.50. At this stage you have two possibilities:

* don't reconcile, and the customer receives a request for 0.50,

* reconcile and accept an adjustment of 0.50 that you will take from the P&L account.

Open ERP generates the following account automatically:


.. csv-table:: **Write-off account**
   :header: "Date","Ref.","Description","Account","Debit","Credit"
   :widths: 12, 5, 15, 5,5,5
   
   "Date","Ref.","Description","Account","Debit","Credit"
   "03 Jun 08","AJ001","Adjustment: profits and losses","4010","","0.50"
   "03 Jun 08","AJ001","Adjustment: profits and losses","XXX","0.50",""


The two invoices and the payment will be reconciled in the first adjustment line. The two invoices will then be automatically marked as paid.

Management of payments
=======================

Open ERP gives you forms for preparing, validating and executing payment orders. This enables you to manage issues such as:

	#. Payment provided on several due dates.

	#. Automatic payment dates.

	#. Separating payment preparation and payment approval in your company.

	#. Preparing an order during the week containing several payments, then creating a payment file at the end of the week.

	#. Creating a file for electronic payment which can be sent to a bank for execution.

	#. Splitting payments dependent on the balances available in your various bank accounts.

Process for managing payment orders
-------------------------------------

To use the tool for managing payments you must first install the module \ ``account_payment``\  . It's part of the core Open ERP system.

The workflow for managing payment is as follows:


	.. image::  images/account_payment_flow.png
	
*Workflow for handling payments to suppliers*

The system enables you to enter a series of payments to be carried out from your various bank accounts. Once the different payments have been registered you can validate the payment orders. During validation you can modify and approve the the payment orders, sending the order to the bank for electronic funds transfer or just printing chequesas you wish.

For example if you have to pay a supplier's invoice for a large amount you can split the payments amongst several bank accounts according to their available balance. To do this you can prepare several Draft orders and validate them once you're satisfied that the split is correct.

This process can also be regularly scheduled. In some companies, a payment order is kept in Draft state and payments are added to the draft list each day. At the end of the week it's an accountant's job to work on all of the waiting payment orders.

Once the payment order is confirmed there's still a validation step for an accountant to carry out. You could imagine that these orders would be prepared by an accounts clerk, and then approved by a manager to go ahead with payment.

.. tip::   **A step further**  *Payment Workflow* 

	An Open ERP workflow is associated with each payment order. To see a visualization of it you'll have to use the GTK client. Select a payment order and click Plugins > Print workflow from the top menu.

	You can integrate more complex workflow rules to manage payment orders by adapting the workflow. For example, in some companies payments must be approved by a manager under certain cash flow or value limit conditions.

	.. image::  images/account_payment_workflow.png
	
*Payments workflow*

When the accounting manager validates the document, Open ERP generates a banking file with all the payment orders. You can then just send the file over your electronic connection with your bank to execute all your payments.

In small businesses it's usually the same person who enters the payment orders and who validates them. In this case you should just click the two buttons, one after the other, to confirm the payment.

Preparation and execution of orders.
-------------------------------------

To enter a payment order, use the menu  *Financial Management > Payment > Payment Orders* .

	.. image::  images/account_payment_order.png
	   :scale: 95
	
*Entering a payment order*

Open ERP then suggests a reference number for your payment order. As usual, you can change the start point for this sequence from the  *Administration*  menu.

You then have to choose a payment mode from the various methods available to your company. These have to be configured when you set the accounting system up using menus  *Financial Management > Configuration > Payment Type*  and  *Financial Management > Configuration > Payment Mode* . Some examples are:

* Cheques

* Bank transfer,

* Visa card on a FORTIS account,

* Petty cash.

Then you must indicate the  *Preferred date*  for payment:

* \ ``Due date``\  : each operation will be effected at the invoice deadline date,

* \ ``Directly``\  : the operations will be effected when the orders are validated,

* \ ``Fixed date``\  : you must specify an effective payment date in the  *Scheduled date if fixed*  field that follows.

The date is particularly important for the preparation of electronic transfers because banking interfaces enable you to select a future execution date for each operation. So to configure your Open ERP most simply you can choose to pay all invoices automatically by their deadline.

You must then select the invoices to pay. They can be manually entered in the field  *Payment Line*  but it's easier to add them automatically. For that, click  *Add payment *  *lines*  and Open ERP will then propose lines with payment deadlines. For each deadline you can see:

* the invoice  *Effective date* ,

* the reference  *Ref.*  and description of the invoice,  *Name* ,

* the deadline for the invoice,

* the amount to be paid in the company's default currency,

* the amount to be paid in the currency of the invoice.

You can then accept the payment proposed by Open ERP or select the entries that you'll pay or not pay on that order. Open ERP gives you all the necessary information to make a payment decision for each line item:

* account,

* supplier's bank account,

* amount that will be paid,

* amount to pay,

* the supplier,

* total amount owed to the supplier,

* due date,

* date of creation.

You can modify the first three fields on each line: the account, the supplier's bank account and the amount that will be paid. This arrangement is very practical because it gives you complete visibility of all the company's trade payables. You can pay only a part of an invoice, for example, and in preparing your next payment order Open ERP automatically suggests payment of the remainder owed.

When the payment has been prepared correctly, click  *Confirm* . The payment then changes to the \ ``Open``\   state and a new button appears that can be used to start the payment process. Depending on the chosen payment method, Open ERP provides a file containing all of the payment orders. You can send this to the bank to make the payment transfers.

In future versions of Open ERP it's expected that the system will be able to prepare and print cheques.

