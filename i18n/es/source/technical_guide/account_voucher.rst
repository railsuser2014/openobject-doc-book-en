
.. i18n: .. module:: account_voucher
.. i18n:     :synopsis: Accounting - Voucher Management (Official, Quality Certified)
.. i18n:     :noindex:
.. i18n: .. 

.. module:: account_voucher
    :synopsis: Accounting - Voucher Management (Official, Quality Certified)
    :noindex:
.. 

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. i18n: Accounting - Voucher Management (*account_voucher*)
.. i18n: ===================================================
.. i18n: :Module: account_voucher
.. i18n: :Name: Accounting - Voucher Management
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: account_voucher
.. i18n: :Web: http://www.openerp.com
.. i18n: :Official module: yes
.. i18n: :Quality certified: yes

Accounting - Voucher Management (*account_voucher*)
===================================================
:Module: account_voucher
:Name: Accounting - Voucher Management
:Version: 5.0.1.0
:Author: Tiny
:Directory: account_voucher
:Web: http://www.openerp.com
:Official module: yes
:Quality certified: yes

.. i18n: Description
.. i18n: -----------

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   India Accounting module includes all the basic requirenment of 
.. i18n:   Basic Accounting, plus new things which available are:
.. i18n:       * New Invoice - (Local, Retail)
.. i18n:       * Invoice Report
.. i18n:       * Tax structure
.. i18n:       * Journals 
.. i18n:       * VAT Declaration report
.. i18n:       * Accounting Periods

::

  India Accounting module includes all the basic requirenment of 
  Basic Accounting, plus new things which available are:
      * New Invoice - (Local, Retail)
      * Invoice Report
      * Tax structure
      * Journals 
      * VAT Declaration report
      * Accounting Periods

.. i18n: Dependencies
.. i18n: ------------

Dependencies
------------

.. i18n:  * :mod:`base`
.. i18n:  * :mod:`account`

 * :mod:`base`
 * :mod:`account`

.. i18n: Reports
.. i18n: -------

Reports
-------

.. i18n:  * Voucher Report

 * Voucher Report

.. i18n: Menus
.. i18n: -------

Menus
-------

.. i18n:  * Financial Management/Voucher Entries
.. i18n:  * Financial Management/Voucher Entries/Receipt Vouchers
.. i18n:  * Financial Management/Voucher Entries/Receipt Vouchers/Cash Receipts
.. i18n:  * Financial Management/Voucher Entries/Receipt Vouchers/Cash Receipts/Draf Cash Receipt
.. i18n:  * Financial Management/Voucher Entries/Receipt Vouchers/Cash Receipts/Pro-forma Cash Receipt
.. i18n:  * Financial Management/Voucher Entries/Receipt Vouchers/Cash Receipts/Posted Cash Receipt
.. i18n:  * Financial Management/Voucher Entries/Receipt Vouchers/Cash Receipts/Cancel Cash Receipt
.. i18n:  * Financial Management/Voucher Entries/Receipt Vouchers/Cash Receipts/New Cash Receipt
.. i18n:  * Financial Management/Voucher Entries/Receipt Vouchers/Bank Receipts
.. i18n:  * Financial Management/Voucher Entries/Receipt Vouchers/Bank Receipts/New Bank Receipt
.. i18n:  * Financial Management/Voucher Entries/Payment Vouchers
.. i18n:  * Financial Management/Voucher Entries/Payment Vouchers/Cash Payments
.. i18n:  * Financial Management/Voucher Entries/Payment Vouchers/Cash Payments/New Cash Payment
.. i18n:  * Financial Management/Voucher Entries/Payment Vouchers/Bank Payments
.. i18n:  * Financial Management/Voucher Entries/Payment Vouchers/Bank Payments/New Bank Payment
.. i18n:  * Financial Management/Voucher Entries/Other Vouchers
.. i18n:  * Financial Management/Voucher Entries/Other Vouchers/Contra Voucher
.. i18n:  * Financial Management/Voucher Entries/Other Vouchers/Journal Sale Voucher
.. i18n:  * Financial Management/Voucher Entries/Other Vouchers/Journal Purchase Voucher

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

.. i18n: Views
.. i18n: -----

Views
-----

.. i18n:  * \* INHERIT account.form (form)
.. i18n:  * \* INHERIT account.form (form)
.. i18n:  * \* INHERIT account.form (form)
.. i18n:  * \* INHERIT account.form (form)
.. i18n:  * account.voucher.tree (tree)
.. i18n:  * account.voucher.form (form)

 * \* INHERIT account.form (form)
 * \* INHERIT account.form (form)
 * \* INHERIT account.form (form)
 * \* INHERIT account.form (form)
 * account.voucher.tree (tree)
 * account.voucher.form (form)

.. i18n: Objects
.. i18n: -------

Objects
-------

.. i18n: Object: Accounting Voucher (account.voucher)
.. i18n: ############################################

Object: Accounting Voucher (account.voucher)
############################################

.. i18n: :move_ids: Real Entry, many2many

:move_ids: Real Entry, many2many

.. i18n: :account_id: Account, many2one, required, readonly

:account_id: Account, many2one, required, readonly

.. i18n: :reference: Voucher Reference, char

:reference: Voucher Reference, char

.. i18n: :amount: Amount, float

:amount: Amount, float

.. i18n: :reference_type: Reference Type, selection, required

:reference_type: Reference Type, selection, required

.. i18n: :company_id: Company, many2one, required

:company_id: Company, many2one, required

.. i18n: :number: Number, char, readonly

:number: Number, char, readonly

.. i18n: :currency_id: Currency, many2one, required, readonly

:currency_id: Currency, many2one, required, readonly

.. i18n: :journal_id: Journal, many2one, required, readonly

:journal_id: Journal, many2one, required, readonly

.. i18n: :state: State, selection, readonly

:state: State, selection, readonly

.. i18n: :payment_ids: Voucher Lines, one2many

:payment_ids: Voucher Lines, one2many

.. i18n: :narration: Narration, text, readonly

:narration: Narration, text, readonly

.. i18n: :date: Date, date, readonly

:date: Date, date, readonly

.. i18n: :period_id: Period, many2one, required

:period_id: Period, many2one, required

.. i18n: :type: Type, selection, readonly

:type: Type, selection, readonly

.. i18n: :move_id: Account Entry, many2one

:move_id: Account Entry, many2one

.. i18n: :name: Name, char, required, readonly

:name: Name, char, required, readonly

.. i18n: Object: Voucher Line (account.voucher.line)
.. i18n: ###########################################

Object: Voucher Line (account.voucher.line)
###########################################

.. i18n: :ref: Ref., char

:ref: Ref., char

.. i18n: :name: Description, char, required

:name: Description, char, required

.. i18n: :partner_id: Partner, many2one, required

:partner_id: Partner, many2one, required

.. i18n: :account_analytic_id: Analytic Account, many2one

:account_analytic_id: Analytic Account, many2one

.. i18n: :amount: Amount, float

:amount: Amount, float

.. i18n: :voucher_id: Voucher, many2one

:voucher_id: Voucher, many2one

.. i18n: :type: Type, selection

:type: Type, selection

.. i18n: :account_id: Account, many2one, required

:account_id: Account, many2one, required
