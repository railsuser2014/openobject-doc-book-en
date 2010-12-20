
.. index::
   single: accounts; start of year

Opening Entries
===============

To upgrade your various accounts, create a Journal of type :guilabel:`Opening/Closing Situation` in :guilabel:`Centralized
counterpart` mode to avoid a counterpart on each line.

For each account that needs upgrading, enter account data in the journal. For this operation use the
menu :menuselection:`Accounting --> Journal Entries --> Journal Items`.

You can also use Open ERP's generic import tool if you load the balance of each of your accounts
from other accounting software.

Example Steps:

1. :menuselection:`Accounting --> Configuration --> Financial Accounting --> Periods --> Fiscal Year` : Create a fiscal Year with monthly periods

2. :menuselection:`Accounting --> Configuration --> Financial Accounting --> Accounts --> Accounts` : Create an account 'Opening Balance Account' (Account Type: 'Equity' (not sure about that, but it is working),Reconcile: 'No')

3. :menuselection:`Accountingt --> Configuration --> Financial Accounting --> Journals --> Journals` : Create a new Journal 'Opening Bal Journal' (Type: 'Opening/Closing Situation', View: 'Journal View', Entry Sequence: 'Account Journal', Default Debit Account: 'Opening Balance Account', Default Credit Account: 'Opening Balance Account', Centralized Counterpart: 'Yes')

4. Best to create a csv-file with the first line:
	"Account","Effective date","Journal","Name","Period","Debit","Credit"
   And the data-lines like this:
	"1000","2008-01-16","Opening Bal Journal","Opening Balance Entry","01/01 - 31/01",0,53828

5. :menuselection:`Accountingt --> Configuration --> Financial Accounting --> Journals --> Journals` : Choose 'Opening Bal Journal'

6. Menu `Form -> Import data`: Choose the file to import, 'Auto Detect', 'Ok'

