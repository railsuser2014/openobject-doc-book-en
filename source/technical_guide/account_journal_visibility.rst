
.. module:: account_journal_visibility
    :synopsis: Accounting journal visibility
    :noindex:
.. 

Accounting journal visibility (*account_journal_visibility*)
============================================================
:Module: account_journal_visibility
:Name: Accounting journal visibility
:Version: 5.0.1.0
:Directory: account_journal_visibility
:Web: 

Description
-----------

::

  Using this module :
      when we open the journals list, people will only see journal for which they are allowed
      (means their group is specified on the journal definition). and also
      Only people in the group defined on the journal will be able to see the invoices of this journal.

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

 * \* INHERIT account.journal.form.inherit (form)


Objects
-------

None
