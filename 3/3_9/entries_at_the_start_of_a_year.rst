
.. index::
   single: accounts; start of year

Opening Entries
===============

To upgrade your various accounts, create a Journal of type :guilabel:`Opening/Closing Situation` in :guilabel:`Centralised
counterpart` mode to avoid a counterpart on each line.

For each account that needs upgrading, enter account data in the journal. For this operation, use the
menu :menuselection:`Accounting --> Journal Entries --> Journal Items`.

You can also use OpenERP's generic import tool if you load the balance of each of your accounts
from other accounting software.

Example Steps:

1. :menuselection:`Accounting --> Configuration --> Financial Accounting --> Periods --> Fiscal Year` : Create a fiscal year with monthly periods

.. not sure about below, but it is working
2. :menuselection:`Accounting --> Configuration --> Financial Accounting --> Accounts --> Accounts` : Create an account ``Opening Balance Account`` (`Account Type`: ``Equity``, `Reconcile`: ``No``)

3. :menuselection:`Accounting --> Configuration --> Financial Accounting --> Journals --> Journals` : Create a new journal ``Opening Bal Journal`` (`Type`: ``Opening/Closing Situation``, `View`: ``Journal View``, `Entry Sequence`: ``Account Journal``, `Default Debit Account`: ``Opening Balance Account``, `Default Credit Account`: ``Opening Balance Account``, `Centralized Counterpart`: ``Yes``)

4. It is best to create a csv-file with the first line:
	"Account","Effective date","Journal","Name","Period","Debit","Credit"
   And the data-lines like this:
	"1000","2008-01-16","Opening Bal Journal","Opening Balance Entry","01/01 - 31/01",0,53828

5. :menuselection:`Accounting --> Configuration --> Financial Accounting --> Journals --> Journals` : Choose ``Opening Bal Journal``

6. :menuselection:`Accounting --> Journal Entries --> Journal Items` : While the form is still in List view, click :guilabel:`Import` from the :guilabel:`Other Options` section at the bottom right of the list.

.. Copyright © Open Object Press. All rights reserved.

.. You may take electronic copy of this publication and distribute it if you don't
.. change the content. You can also print a copy to be read by yourself only.

.. We have contracts with different publishers in different countries to sell and
.. distribute paper or electronic based versions of this book (translated or not)
.. in bookstores. This helps to distribute and promote the OpenERP product. It
.. also helps us to create incentives to pay contributors and authors using author
.. rights of these sales.

.. Due to this, grants to translate, modify or sell this book are strictly
.. forbidden, unless Tiny SPRL (representing Open Object Press) gives you a
.. written authorisation for this.

.. Many of the designations used by manufacturers and suppliers to distinguish their
.. products are claimed as trademarks. Where those designations appear in this book,
.. and Open Object Press was aware of a trademark claim, the designations have been
.. printed in initial capitals.

.. While every precaution has been taken in the preparation of this book, the publisher
.. and the authors assume no responsibility for errors or omissions, or for damages
.. resulting from the use of the information contained herein.

.. Published by Open Object Press, Grand Rosière, Belgium
