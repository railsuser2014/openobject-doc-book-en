
.. index:: Payment Terms

Payment Terms
=============

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

