
Module Payment Management (*account_payment*)
=============================================
:Module: account_payment
:Name: Payment Management
:Version: 5.0.1.1
:Directory: account_payment
:Web: 

Description
-----------

::

  This module provide :
      * a more efficient way to manage invoice payment.
      * a basic mechanism to easily plug various automated payment.

Dependencies
------------

 * account - installed

Reports
-------

 * Payment Order

Menus
-------

 * Financial Management/Payment
 * Financial Management/Configuration/Payment
 * Financial Management/Configuration/Payment/Payment Mode
 * Financial Management/Payment/Payment Orders
 * Financial Management/Payment/Payment Orders/Draft Payment Order
 * Financial Management/Payment/Payment Orders/Payment Orders to Validate
 * Financial Management/Payment/Payment Orders/New Payment Order

Views
-----

 * \* INHERIT account.move.line.form.inherit (form)
 * account.move.line.tree (tree)
 * payment.type.form (form)
 * payment.mode.tree (tree)
 * payment.mode.form (form)
 * payment.order.form (form)
 * payment.order.tree (tree)
 * Payment Line (form)
 * Payment Lines (tree)
 * \* INHERIT account.bank.statement.form.inherit (form)
 * \* INHERIT account.invoice.supplier.form.inherit (form)


Objects
-------

Object: Payment type
####################

.. index::
  single: Payment type object
.. 


:note: Description, text

    *Description of the payment type that will be shown in the invoices*

.. index::
  single: note field
.. 




:active: Active, boolean



.. index::
  single: active field
.. 




:code: Code, char, required

    *Specify the Code for Payment Type*

.. index::
  single: code field
.. 




:name: Name, char, required

    *Payment Type*

.. index::
  single: name field
.. 




:suitable_bank_types: Suitable bank types, many2many



.. index::
  single: suitable_bank_types field
.. 



Object: Payment mode
####################

.. index::
  single: Payment mode object
.. 


:journal: Journal, many2one, required

    *Cash Journal for the Payment Mode*

.. index::
  single: journal field
.. 




:type: Payment type, many2one, required

    *Select the Payment Type for the Payment Mode.*

.. index::
  single: type field
.. 




:name: Name, char, required

    *Mode of Payment*

.. index::
  single: name field
.. 




:bank_id: Bank account, many2one, required

    *Bank Account for the Payment Mode*

.. index::
  single: bank_id field
.. 



Object: Payment Order
#####################

.. index::
  single: Payment Order object
.. 


:date_prefered: Preferred date, selection, required

    *Choose an option for the Payment Order:'Fixed' stands for a date specified by you.'Directly' stands for the direct execution.'Due date' stands for the scheduled date of execution.*

.. index::
  single: date_prefered field
.. 




:user_id: User, many2one, required



.. index::
  single: user_id field
.. 




:reference: Reference, char, required



.. index::
  single: reference field
.. 




:date_done: Execution date, date, readonly



.. index::
  single: date_done field
.. 




:date_planned: Scheduled date if fixed, date

    *Select a date if you have chosen Preferred Date to be fixed.*

.. index::
  single: date_planned field
.. 




:payment_type_name: Payment type name, char, readonly



.. index::
  single: payment_type_name field
.. 




:state: State, selection



.. index::
  single: state field
.. 




:mode: Payment mode, many2one, required

    *Select the Payment Mode to be applied.*

.. index::
  single: mode field
.. 




:date_created: Creation date, date, readonly



.. index::
  single: date_created field
.. 




:line_ids: Payment lines, one2many



.. index::
  single: line_ids field
.. 




:total: Total, float, readonly



.. index::
  single: total field
.. 




:type: Type, selection, readonly



.. index::
  single: type field
.. 




:name: Name, char, readonly



.. index::
  single: name field
.. 



Object: Payment Line
####################

.. index::
  single: Payment Line object
.. 


:company_currency: Company Currency, many2one, readonly



.. index::
  single: company_currency field
.. 




:ml_inv_ref: Invoice Ref., many2one, readonly



.. index::
  single: ml_inv_ref field
.. 




:create_date: Created, datetime, readonly



.. index::
  single: create_date field
.. 




:name: Your Reference, char, required



.. index::
  single: name field
.. 




:state: Communication Type, selection, required



.. index::
  single: state field
.. 




:order_id: Order, many2one, required



.. index::
  single: order_id field
.. 




:communication: Communication, char, required

    *Used as the message between ordering customer and current company.Depicts 'What do you want to say to the receipent about this oder?'*

.. index::
  single: communication field
.. 




:bank_id: Destination Bank account, many2one



.. index::
  single: bank_id field
.. 




:communication2: Communication 2, char

    *The successor message of Communication.*

.. index::
  single: communication2 field
.. 




:currency: Partner Currency, many2one, required



.. index::
  single: currency field
.. 




:amount: Amount in Company Currency, float, readonly

    *Payment amount in the company currency*

.. index::
  single: amount field
.. 




:info_partner: Destination Account, text, readonly

    *Address of the Ordering Customer.*

.. index::
  single: info_partner field
.. 




:date: Payment Date, date

    *If no payment date is specified, the bank will treat this payment line directly*

.. index::
  single: date field
.. 




:ml_date_created: Effective Date, date, readonly

    *Invoice Effective Date*

.. index::
  single: ml_date_created field
.. 




:move_line_id: Entry line, many2one

    *This Entry Line will be referred for the information of the ordering customer.*

.. index::
  single: move_line_id field
.. 




:info_owner: Owner Account, text, readonly

    *Address of the Main Partner*

.. index::
  single: info_owner field
.. 




:amount_currency: Amount in Partner Currency, float, required

    *Payment amount in the partner currency*

.. index::
  single: amount_currency field
.. 




:partner_id: Partner, many2one, required

    *The Ordering Customer*

.. index::
  single: partner_id field
.. 




:ml_maturity_date: Maturity Date, date, readonly



.. index::
  single: ml_maturity_date field
.. 

