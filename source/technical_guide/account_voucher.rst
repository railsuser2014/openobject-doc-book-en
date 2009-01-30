
.. module:: account_voucher
    :synopsis: Accounting - Voucher Management
    :noindex:
.. 

Accounting - Voucher Management (*account_voucher*)
===================================================
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

Object: Accounting Voucher (account.voucher)
############################################



:move_ids: Real Entry, many2many





:account_id: Account, many2one, required, readonly





:reference: Voucher Reference, char





:amount: Amount, float





:reference_type: Reference Type, selection, required





:company_id: Company, many2one, required





:number: Number, char, readonly





:currency_id: Currency, many2one, required, readonly





:journal_id: Journal, many2one, required, readonly





:state: State, selection, readonly





:payment_ids: Voucher Lines, one2many





:narration: Narration, text, readonly





:date: Date, date, readonly





:period_id: Period, many2one, required





:type: Type, selection, readonly





:move_id: Account Entry, many2one





:name: Name, char, required, readonly




Object: Voucher Line (account.voucher.line)
###########################################



:ref: Ref., char





:name: Description, char, required





:partner_id: Partner, many2one, required





:account_analytic_id: Analytic Account, many2one





:amount: Amount, float





:voucher_id: Voucher, many2one





:type: Type, selection





:account_id: Account, many2one, required


