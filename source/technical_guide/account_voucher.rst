
Module Accounting - Voucher Management (*account_voucher*)
==========================================================
:Module: account_voucher
:Name: Accounting - Voucher Management
:Version: 5.0.1.0
:Directory: account_voucher
:Web: http://www.openerp.com

Description
-----------

::

  India Accounting module includes all the basic requirenment of 
  Basic Accounting, plus new things which available are:
      * New Invoice - (Local, Retail)
      * Invoice Report
      * Tax structure
      * Journals 
      * VAT Declaration report
      * Accounting Periods

Dependencies
------------

 * base - installed
 * account - installed

Reports
-------

 * Voucher Report

Menus
-------

 * Financial Management/Voucher Entries
 * Financial Management/Voucher Entries/Receipt Vouchers
 * Financial Management/Voucher Entries/Receipt Vouchers/Cash Receipts
 * Financial Management/Voucher Entries/Receipt Vouchers/Cash Receipts/Draf Cash Receipt
 * Financial Management/Voucher Entries/Receipt Vouchers/Cash Receipts/Pro-forma Cash Receipt
 * Financial Management/Voucher Entries/Receipt Vouchers/Cash Receipts/Posted Cash Receipt
 * Financial Management/Voucher Entries/Receipt Vouchers/Cash Receipts/Cancel Cash Receipt
 * Financial Management/Voucher Entries/Receipt Vouchers/Cash Receipts/New Cash Receipt
 * Financial Management/Voucher Entries/Receipt Vouchers/Bank Receipts
 * Financial Management/Voucher Entries/Receipt Vouchers/Bank Receipts/New Bank Receipt
 * Financial Management/Voucher Entries/Payment Vouchers
 * Financial Management/Voucher Entries/Payment Vouchers/Cash Payments
 * Financial Management/Voucher Entries/Payment Vouchers/Cash Payments/New Cash Payment
 * Financial Management/Voucher Entries/Payment Vouchers/Bank Payments
 * Financial Management/Voucher Entries/Payment Vouchers/Bank Payments/New Bank Payment
 * Financial Management/Voucher Entries/Other Vouchers
 * Financial Management/Voucher Entries/Other Vouchers/Contra Voucher
 * Financial Management/Voucher Entries/Other Vouchers/Journal Sale Voucher
 * Financial Management/Voucher Entries/Other Vouchers/Journal Purchase Voucher

Views
-----

 * \* INHERIT account.form (form)
 * \* INHERIT account.form (form)
 * \* INHERIT account.form (form)
 * \* INHERIT account.form (form)
 * account.voucher.tree (tree)
 * account.voucher.form (form)


Objects
-------

Object: Accounting Voucher
##########################

.. index::
  single: Accounting Voucher object
.. 


:move_ids: Real Entry, many2many



.. index::
  single: move_ids field
.. 




:account_id: Account, many2one, required, readonly



.. index::
  single: account_id field
.. 




:reference: Voucher Reference, char



.. index::
  single: reference field
.. 




:amount: Amount, float



.. index::
  single: amount field
.. 




:reference_type: Reference Type, selection, required



.. index::
  single: reference_type field
.. 




:company_id: Company, many2one, required



.. index::
  single: company_id field
.. 




:number: Number, char, readonly



.. index::
  single: number field
.. 




:currency_id: Currency, many2one, required, readonly



.. index::
  single: currency_id field
.. 




:journal_id: Journal, many2one, required, readonly



.. index::
  single: journal_id field
.. 




:state: State, selection, readonly



.. index::
  single: state field
.. 




:payment_ids: Voucher Lines, one2many



.. index::
  single: payment_ids field
.. 




:narration: Narration, text, readonly



.. index::
  single: narration field
.. 




:date: Date, date, readonly



.. index::
  single: date field
.. 




:period_id: Period, many2one, required



.. index::
  single: period_id field
.. 




:type: Type, selection, readonly



.. index::
  single: type field
.. 




:move_id: Account Entry, many2one



.. index::
  single: move_id field
.. 




:name: Name, char, required, readonly



.. index::
  single: name field
.. 



Object: Voucher Line
####################

.. index::
  single: Voucher Line object
.. 


:ref: Ref., char



.. index::
  single: ref field
.. 




:name: Description, char, required



.. index::
  single: name field
.. 




:partner_id: Partner, many2one, required



.. index::
  single: partner_id field
.. 




:account_analytic_id: Analytic Account, many2one



.. index::
  single: account_analytic_id field
.. 




:amount: Amount, float



.. index::
  single: amount field
.. 




:voucher_id: Voucher, many2one



.. index::
  single: voucher_id field
.. 




:type: Type, selection



.. index::
  single: type field
.. 




:account_id: Account, many2one, required



.. index::
  single: account_id field
.. 

