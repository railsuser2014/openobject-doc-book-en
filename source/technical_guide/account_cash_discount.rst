
.. module:: account_cash_discount
    :synopsis: Payement Term with Cash Discount
    :noindex:
.. 

Payement Term with Cash Discount (*account_cash_discount*)
==========================================================
:Module: account_cash_discount
:Name: Payement Term with Cash Discount
:Version: 5.0.1.0
:Directory: account_cash_discount
:Web: http://tinyerp.com/
:Is certified: no

Description
-----------

::

  This module adds cash discounts on payment terms. Cash discounts
      for a payment term can be configured with:
          * A number of days,
          * A discount (%),
          * A debit and a credit account

Dependencies
------------

 * account - installed

Reports
-------

None


Menus
-------


None


Views
-----

 * account.cash.discount.form (form)
 * account.cash.discount.tree (tree)
 * \* INHERIT account.payment.term.form (form)


Objects
-------

Object: Cash Discount (account.cash.discount)
#############################################



:payment_id: Associated Payment Term, many2one





:name: Name, char





:credit_account_id: Credit Account, many2one





:delay: Number of Days, integer, required





:discount: Discount (%), float, required





:debit_account_id: Debit Account, many2one


