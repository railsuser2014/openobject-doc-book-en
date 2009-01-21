
.. index::
   single: Payments Order
.. 

.. 162

Management of payments
======================

Open ERP gives you forms for preparing, validating and executing payment orders. This enables you to manage issues such as:

	#. Payment provided on several due dates.

	#. Automatic payment dates.

	#. Separating payment preparation and payment approval in your company.

	#. Preparing an order during the week containing several payments, then creating a payment file at the end of the week.

	#. Creating a file for electronic payment which can be sent to a bank for execution.

	#. Splitting payments dependent on the balances available in your various bank accounts.

Process for managing payment orders
-----------------------------------

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
------------------------------------

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

You must then select the invoices to pay. They can be manually entered in the field  *Payment Line*  but it's easier to add them automatically. For that, click  *Add payment lines*  and Open ERP will then propose lines with payment deadlines. For each deadline you can see:

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

