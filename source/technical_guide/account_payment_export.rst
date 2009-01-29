
Payment Order Export (*account_payment_export*)
===============================================
:Module: account_payment_export
:Name: Payment Order Export
:Version: 5.0.1.0
:Directory: account_payment_export
:Web: 

Description
-----------

::

  This module allows to export payment orders.

Dependencies
------------

 * base_vat - installed
 * base_iban - installed
 * account_payment - installed

Reports
-------

None


Menus
-------

 * Financial Management/Configuration/Payment Export
 * Financial Management/Configuration/Payment Export/Payment Export Logs
 * Financial Management/Configuration/Payment/Payment Method
 * Financial Management/Configuration/Payment/Charges Code

Views
-----

 * \* INHERIT res.partner.form.code.inherit (form)
 * \* INHERIT res.partner.bank.form.code.inherit (form)
 * account.pay.tree (tree)
 * account.pay.form (form)
 * \* INHERIT res.bank.form.inherit (form)
 * payment.method.tree (tree)
 * payment.method.form (form)
 * charges.code.tree (tree)
 * charges.code.form (form)


Objects
-------

Object: Payment Export History
##############################



:create_uid: Creation User, many2one, required, readonly





:create_date: Creation Date, datetime, required, readonly





:note: Creation Log, text, readonly





:payment_order_id: Payment Order Reference, many2one, readonly





:state: Status, selection, readonly





:file: Saved File, binary, readonly




Object: Payment Method For Export
#################################



:name: Name, char





:shortcut: Shortcut, char




Object: Charges Codes For Export
################################



:name: Code, char, required





:description: Description, text


