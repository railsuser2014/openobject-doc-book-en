
.. index::
   single: accounts; start of year

Entries at the start of a year
==============================

To upgrade your various accounts, create a Journal of type :guilabel:`Situation` in :guilabel:`Centralized
counterpart` mode to avoid a counterpart on each line.

For each account that needs upgrading, enter account data in the journal. For this operation use the
menu :menuselection:`Financial Management --> Entries Encoding --> Entries Encoding by Line`.

You can also use Open ERP's generic import tool if you load the balance of each of your accounts
from other accounting software.

Example Steps:

1. `Financial Management -> Configuration -> Periods -> Fiscal Year` : Create a fiscal Year with monthly periods

2. `Financial Management -> Configuration -> General Accounts -> Accounts Definition` : Create an account 'Opening Balance Account' (Account Type: 'Equity' (not sure about that, but it's working), Sign: 'Positive', Deferral Method: 'None', Reconcile: 'No')

3. `Financial Management -> Configuration -> Journal -> Journal Definition` : Create a new Journal 'Opening Bal Journal' (Type: 'Situation', View: 'Journal View', Entry Sequence: 'Account Journal', Default Debit Account: 'Opening Balance Account', Default Credit Account: 'Opening Balance Account', Centralized Counterpart: 'Yes')

4. Best to create a csv-file with the first line:
	"Account","Effective date","Journal","Name","Period","Debit","Credit"
   And the data-lines like this:
	"1000","2008-01-16","Opening Bal Journal","Opening Balance Entry","01/01 - 31/01",0,53828

5. `Financial Management -> Entries -> Entries by Journal` : Choose 'Opening Bal Journal'

6. Menu `Form -> Import dat`': Choose the file to import, 'Auto Detect', 'Ok'

