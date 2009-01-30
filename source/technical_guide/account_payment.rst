
.. module:: account_payment
    :synopsis: Payment Management
    :noindex:
.. 

Payment Management (*account_payment*)
======================================
:Module: account_payment
:Name: Payment Management
:Version: 5.0.1.1
:Directory: account_payment
:Web: 
:Is certified: yes

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

Object: Payment type (payment.type)
###################################



:note: Description, text

    *Description of the payment type that will be shown in the invoices*



:active: Active, boolean





:code: Code, char, required

    *Specify the Code for Payment Type*



:name: Name, char, required

    *Payment Type*



:suitable_bank_types: Suitable bank types, many2many




Object: Payment mode (payment.mode)
###################################



:journal: Journal, many2one, required

    *Cash Journal for the Payment Mode*



:type: Payment type, many2one, required

    *Select the Payment Type for the Payment Mode.*



:name: Name, char, required

    *Mode of Payment*



:bank_id: Bank account, many2one, required

    *Bank Account for the Payment Mode*


Object: Payment Order (payment.order)
#####################################



:date_prefered: Preferred date, selection, required

    *Choose an option for the Payment Order:'Fixed' stands for a date specified by you.'Directly' stands for the direct execution.'Due date' stands for the scheduled date of execution.*



:user_id: User, many2one, required





:reference: Reference, char, required





:date_done: Execution date, date, readonly





:date_planned: Scheduled date if fixed, date

    *Select a date if you have chosen Preferred Date to be fixed.*



:payment_type_name: Payment type name, char, readonly





:state: State, selection





:mode: Payment mode, many2one, required

    *Select the Payment Mode to be applied.*



:date_created: Creation date, date, readonly





:line_ids: Payment lines, one2many





:total: Total, float, readonly





:type: Type, selection, readonly





:name: Name, char, readonly




Object: Payment Line (payment.line)
###################################



:company_currency: Company Currency, many2one, readonly





:ml_inv_ref: Invoice Ref., many2one, readonly





:create_date: Created, datetime, readonly





:name: Your Reference, char, required





:state: Communication Type, selection, required





:order_id: Order, many2one, required





:communication: Communication, char, required

    *Used as the message between ordering customer and current company.Depicts 'What do you want to say to the receipent about this oder?'*



:bank_id: Destination Bank account, many2one





:communication2: Communication 2, char

    *The successor message of Communication.*



:currency: Partner Currency, many2one, required





:amount: Amount in Company Currency, float, readonly

    *Payment amount in the company currency*



:info_partner: Destination Account, text, readonly

    *Address of the Ordering Customer.*



:date: Payment Date, date

    *If no payment date is specified, the bank will treat this payment line directly*



:ml_date_created: Effective Date, date, readonly

    *Invoice Effective Date*



:move_line_id: Entry line, many2one

    *This Entry Line will be referred for the information of the ordering customer.*



:info_owner: Owner Account, text, readonly

    *Address of the Main Partner*



:amount_currency: Amount in Partner Currency, float, required

    *Payment amount in the partner currency*



:partner_id: Partner, many2one, required

    *The Ordering Customer*



:ml_maturity_date: Maturity Date, date, readonly


