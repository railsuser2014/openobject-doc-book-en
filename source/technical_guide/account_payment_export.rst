
Module Payment Order Export (*account_payment_export*)
======================================================
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

.. index::
  single: Payment Export History object
.. 


:create_uid: Creation User, many2one, required, readonly



.. index::
  single: create_uid field
.. 




:create_date: Creation Date, datetime, required, readonly



.. index::
  single: create_date field
.. 




:note: Creation Log, text, readonly



.. index::
  single: note field
.. 




:payment_order_id: Payment Order Reference, many2one, readonly



.. index::
  single: payment_order_id field
.. 




:state: Status, selection, readonly



.. index::
  single: state field
.. 




:file: Saved File, binary, readonly



.. index::
  single: file field
.. 



Object: Payment Method For Export
#################################

.. index::
  single: Payment Method For Export object
.. 


:name: Name, char



.. index::
  single: name field
.. 




:shortcut: Shortcut, char



.. index::
  single: shortcut field
.. 



Object: Charges Codes For Export
################################

.. index::
  single: Charges Codes For Export object
.. 


:name: Code, char, required



.. index::
  single: name field
.. 




:description: Description, text



.. index::
  single: description field
.. 

