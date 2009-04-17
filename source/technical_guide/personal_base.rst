
.. module:: personal_base
    :synopsis: Personal Base 
    :noindex:
.. 

.. raw:: html

      <br />
    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. tip:: This module is part of the Open ERP software, the leading Open Source 
  enterprise management system. If you want to discover Open ERP, check our 
  `screencasts <href="http://openerp.tv>`_ or download 
  `Open ERP <href="http://openerp.com>`_ directly.

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/personal_base"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Personal Base (*personal_base*)
===============================
:Module: personal_base
:Name: Personal Base
:Version: 5.0.1.1
:Author: Sandas
:Directory: personal_base
:Web: www.sandas.eu
:Official module: no
:Quality certified: no

Description
-----------

::

  Sandas Personal Financials base module.

Download links
--------------

You can download this module as a zip file in the following version:

  * `trunk </download/modules/trunk/personal_base.zip>`_


Dependencies
------------

 * :mod:`base`
 * :mod:`account`

Reports
-------

None


Menus
-------

 * Administration/Personal
 * Financial Management/Account Entries
 * Financial Management/Account Entries/New Account Entry
 * Financial Management/Account Entries/Confirmed Account Entries
 * Financial Management/Account Entries/Draft Account Entries
 * Financial Management/Account Entries/Confirmed Account Entries/Confirmed Account Lines
 * Financial Management/Accounts Definition
 * Financial Management/Chart of Accounts
 * Administration/Personal/Account Types
 * Administration/Personal/Create Account Types
 * Administration/Personal/Actions After Login

Views
-----

 * personal.base.account.entry.tree (tree)
 * personal.base.account.entry.form (form)
 * personal.base.account.entry.line.tree (tree)
 * personal.base.account.entry.line.tree (tree)
 * personal.base.account.entry.line.form (form)
 * personal.base.account.form (form)
 * personal.base.account.tree (tree)
 * personal.base.account.tree (tree)
 * personal.base.account.type.tree (tree)
 * personal.base.account.type.form (form)


Objects
-------

Object: Account Type (personal.base.account.type)
#################################################



:name: Acc. Type Name, char, required





:sign: Sign, selection, required




Object: Account (personal.base.account)
#######################################



:note: Note, text





:user_id: User, many2one, required





:name: Name, char, required





:type_id: Account Type, many2one, required





:child_ids: Childs Codes, one2many





:currency_id: Currency, many2one, required





:parent_id: Parent Code, many2one





:unit_test: unit_test, boolean





:balance: Balance, float, readonly




Object: Account Entry (personal.base.account.entry)
###################################################



:note: Note, text





:created_in_model_id: Created in Model, many2one, required, readonly





:user_id: User, many2one, required





:name: Description, char, required





:currency_id: Currency, many2one





:state: State, selection, required, readonly





:unit_test: unit_test, boolean





:date: Date, date, required





:line_ids: Entries, one2many




Object: Account Entry Line (personal.base.account.entry.line)
#############################################################



:user_id: User, many2one, required





:name: Description, char





:debit_amount: Debit Amount, float





:credit_amount: Credit Amount, float





:amount_base_with_sign: Amount, float, readonly





:amount_base: Amount Base, float





:currency_id: Currency, many2one, required





:parent_id: Entry, many2one, required





:state: State, selection, required, readonly





:unit_test: unit_test, boolean





:currency_rate: Currency Rate, float, required





:date: Date, date, required





:balance: Balance, float, readonly





:account_id: Account, many2one, required




Object: personal.base.action.login (personal.base.action.login)
###############################################################



:name: Name, char





:action_id: Action, many2one, required


