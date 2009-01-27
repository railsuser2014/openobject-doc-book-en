
Module Account Regularizations (*account_regularization*)
=========================================================
:Module: account_regularization
:Name: Account Regularizations
:Version: 5.0.1.0
:Directory: account_regularization
:Web: 

Description
-----------

::

  This module creates a new object in accounting, 
  	very similar to the account models named account.regularization. 
  	Within this object you can define regularization moves, 
  	This is, accounting moves that will automatically calculate the balance of a set of accounts, 
  	Set it to 0 and transfer the difference to a new account. This is used, for example with tax declarations or in some countries to create the 'Profit and Loss' regularization

Dependencies
------------

 * account - installed

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

Object: Account Regularization Model
####################################

.. index::
  single: Account Regularization Model object
.. 


:balance_calc: Regularization time calculation, selection, required



.. index::
  single: balance_calc field
.. 




:name: Name, char, required



.. index::
  single: name field
.. 




:credit_account_id: Result account, credit, many2one, required



.. index::
  single: credit_account_id field
.. 




:move_ids: Regularization Moves, one2many



.. index::
  single: move_ids field
.. 




:account_ids: Accounts to balance, many2many, required



.. index::
  single: account_ids field
.. 




:debit_account_id: Result account, debit, many2one, required



.. index::
  single: debit_account_id field
.. 

