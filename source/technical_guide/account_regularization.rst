
.. module:: account_regularization
    :synopsis: Account Regularizations 
    :noindex:
.. 

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

Account Regularizations (*account_regularization*)
==================================================
:Module: account_regularization
:Name: Account Regularizations
:Version: 5.0.1.0
:Author: ACYSOS S.L.
:Directory: account_regularization
:Web: 
:Official module: no
:Quality certified: no

Description
-----------

::

  This module creates a new object in accounting,very similar to the account models named 
  account.regularization. 
  Within this object you can define regularization moves, 
  This is, accounting moves that will automatically calculate the balance of a set of accounts, 
  Set it to 0 and transfer the difference to a new account. This is used, for example with tax declarations 
  or in some countries to create the 'Profit and Loss' regularization

Dependencies
------------

 * :mod:`account`

Reports
-------

None


Menus
-------

 * Financial Management/Periodical Processing/Regularizations

Views
-----

 * account.regularization.form (form)


Objects
-------

Object: Account Regularization Model (account.regularization)
#############################################################



:balance_calc: Regularization time calculation, selection, required





:name: Name, char, required





:credit_account_id: Result account, credit, many2one, required





:move_ids: Regularization Moves, one2many





:account_ids: Accounts to balance, many2many, required





:debit_account_id: Result account, debit, many2one, required


