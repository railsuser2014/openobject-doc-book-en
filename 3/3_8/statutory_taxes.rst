
.. index::
   single: trial balance
   single: general ledger

General Ledger and Trial Balance
--------------------------------

A general ledger includes accounts with their debits and credits, and shows all transactions in an account, for one period, for several periods or for a financial year.

To print the `General Ledger`, you can use the menu :menuselection:`Accounting --> Reporting --> Legal Reports --> Accounting Reports --> General Ledger`.
You will find the following wizard which is used to filter the resulting report.

.. figure::  images/account_wizard_report.png
   :scale: 75
   :align: center

   *Preparing a General Ledger*

Select the proper options and journal(s) from the above wizard to print the `General Ledger`. The report can also be filtered by date or by period. When you choose to print the general ledger from one date to another, or for one or more periods, you can also have the initial balances printed for the periods preceding the periods you selected.
You can sort the report by date or by journal / partner.

.. figure::  images/account_general_ledger.png
   :scale: 65
   :align: center

   *General Ledger*

.. tip:: General Ledger for one or more accounts

    When you want to print the general ledger for one or more accounts, go to the menu :menuselection:`Accounting --> Configuration -> Financial Accounting --> Accounts --> Accounts`. Select the account(s) for which you want to print the general ledger and click the :guilabel:`General Ledger` report at the right side of the screen. 

While the general ledger displays transactions for an account, a trial balance will show one amount (either debit or credit) for each account. The aim of the trial balance is to prove that the total of all debit balances is equal to the total of all credit balances.

To print the `Trial Balance`, go to the menu :menuselection:`Accounting --> Reporting --> Legal Reports --> Accounting Reports --> Trial Balance`.
This report allows you to print or generate a PDF of your trial balance, allowing you to quickly check the balance of each of your accounts in a single report. A trial balance may include all accounts (even the ones without balance), only accounts with transactions or accounts of which the balance is not equal to zero. You can print a trial balance for all posted entries (meaning entries with a Valid state) or all entries, in which case the report will also print entries in a draft state. This option is useful, for instance, when your new financial year has just been opened, and you are preparing miscellaneous entries in the previous financial year.

.. figure::  images/account_trial_balance.png
   :scale: 65
   :align: center

   *Trial Balance*

.. tip:: Reporting for One or More Accounts

    You can print the `Trial Balance` report directly from the `Account` form too.

.. index::
   single: balance sheet
   single: profit & loss

Balance Sheet and Profit & Loss Report
--------------------------------------

OpenERP also offers a Balance Sheet and a Profit & Loss Report.

A `Balance Sheet` is a financial statement that summarises the assets, liabilities and shareholders' equity of a company at a specific point in time. These three balance sheet segments give investors an idea as to what the company owns and owes, as well as the amount invested by the shareholders.

The balance sheet complies with the formula below:

Assets = Liabilities + Shareholders' Equity.

A balance sheet is often described as a snapshot of a company's financial condition.

The accounts displayed in the Balance Sheet are linked to an account type for which the ``P&L / Balance Sheet`` parameter is set to Balance Sheet (either Assets or Liabilities account). To configure :guilabel:`Account Types`, go to :menuselection:`Accounting --> Configuration --> Financial Accounting --> Accounts --> Account Types`.

The Balance Sheet can be printed from the menu :menuselection:`Accounting --> Reporting --> Legal Reports --> Accounting Reports --> Balance Sheet`. You can print this report in Landscape mode too.

.. tip:: Reserve & Profit and Loss Account

    A Balance Sheet needs a reserve & profit and loss account, but instead of entering it each time you start the report, you can add a default Reserve & Profit and Loss account through the menu:menuselection:`Settings --> Companies --> Companies` on the ``Configuration`` tab. This account will be used as a counterpart to balance your accounts.

The `Profit & Loss Report` is a financial statement which gives a summary of the revenues, costs and expenses during a specific period of time. Such a report provides information that shows the ability of a company to generate profit by increasing revenue and reducing costs. The P&L statement is also known as an "Income Statement".

The purpose of the Profit & Loss Report is to show managers and accountants whether the company earned or lost money during the report period.

In general, the Profit and Loss report will be used to determine profit ratios, to examine sales prices and costs, and to set marketing budgets, for instance.

The accounts displayed in the Profit and Loss Report are linked to an account type for which the ``"P&L / Balance Sheet`` parameter is set to Profit & Loss (either Expense or Income account). To configure Account types, go to :menuselection:`Accounting --> Configuration --> Financial Accounting --> Account Types`.

The Profit and Loss report can be printed from the menu :menuselection:`Accounting --> Reporting --> Legal Reports --> Accounting Reports --> Profit And Loss`.


.. figure::  images/account_profit_loss.png
   :scale: 75
   :align: center

   *Profit and Loss Wizard*

.. figure::  images/account_profit_loss_report.png
   :scale: 75
   :align: center

   *Profit and Loss Report*

.. index:: journal

The Accounting Journals
-----------------------

A journal allows you to list entries in chronological order (by default according to date). Each entry posted in OpenERP is recorded in such a journal. To configure the different accounting journals go to the menu :menuselection:`Accounting --> Configuration --> Financial Accounting --> Journals --> Journals`.

.. figure::  images/account_journal_form.png
   :scale: 75
   :align: center

   *Defining a Journal*

OpenERP provides three main reports regarding the journals:

* To print `Journals`, use the menu :menuselection:`Accounting --> Reporting --> Legal Reports --> Journals --> Journals`. A Journal will show all entries per journal, e.g. sales entries, purchase entries, etc. Each transaction is mentioned, with date, reference, document number, account, partner, description and debit and credit amount. The Journal Report is printed per period and per journal.

.. figure::  images/account_journal_print.png
   :scale: 75
   :align: center

   *Printing a Journal*

* To print `General Journals`, use the menu :menuselection:`Accounting --> Reporting --> Legal Reports --> Journals --> General Journals`. A General Journal will print a page per period for any journal entries posted in that period, and totalised per journal. The report will show the period, the journal, debit, credit and balance.

.. figure::  images/account_gen_journal_print.png
   :scale: 75
   :align: center

   *Printing a General Journal*

* To print `Centralizing Journal`, use the menu :menuselection:`Accounting --> Reporting --> Legal Reports --> Journals --> Centralizing Journal`. A centralizing journal gives a summary per account for each journal and period of debit, credit and balance.


Tax Declaration
---------------

Information required for a tax declaration is automatically generated by OpenERP from invoices. In the section on invoicing, you will have seen that you can get details of tax information from the area at the bottom left of an invoice.

You can also get the tax information when you open a journal entry by looking at the columns to the right of each line.

OpenERP keeps a tax chart that you can reach from the menu :menuselection:`Accounting --> Charts --> Chart of Taxes`. The wizard will propose to display entries for the current period only, but you can also leave the period empty to see a complete financial year. The structure of the chart is for calculating the VAT declaration, but all the other taxes can be calculated as well (such as the French DEEE).

.. index::
   single: VAT

.. figure::  images/account_tax_chart.png
   :scale: 75
   :align: center

   *Example of a Belgian VAT Structure*

The tax chart represents the amount of each area of the VAT declaration for your country. It is presented in a hierarchical structure which lets you see the detail only of what interests you and hides the less interesting subtotals. This structure can be altered as you wish to fit your needs.

You can create several tax charts if your company is subject to different types of tax or tax-like accounts, such as:

* authors' rights,

* ecotaxes, such as the French DEEE for recycling electrical equipment.

Creating several charts of taxes allows you to print different declarations from the menu :menuselection:`Accounting --> Reporting --> Generic Reporting --> Taxes --> Taxes Report`. Simply select the declaration you want to print in the wizard.

Each accounting entry can then be linked to one of the tax accounts. This association is done automatically from the taxes which had previously been configured in the invoice lines.

.. tip:: Tax Declaration

        Some accounting software manages the tax declaration in a dedicated general account.
        The declaration is then limited to the balance in the specified period.
        In OpenERP, you can create an independent chart of taxes, which has several advantages:

        * it is possible to allocate only a part of the tax transaction,

        * it is not necessary to manage several general accounts depending on the type of sale and the type of tax,

        * you can restructure your chart of taxes as required.

At any time, you can check your chart of taxes for a given period using the report :menuselection:`Accounting --> Reporting --> Generic Reporting --> Taxes --> Taxes Report`.

Data is updated in real time. This is very useful because it enables you to preview at any time the tax that you owe at the start and end of the month or quarter.

Furthermore, for your tax declaration, you can click one of the tax accounts to investigate the detailed entries that make up the full amount. This helps you search for errors, such as when you have entered an invoice at full tax rate when it should have been zero-rated for an intracommunity trade or for charity.

Management Indicators
---------------------

With OpenERP you can also create your own financial reports. This feature is now included in standard OpenERP. Go to :menuselection:`Accounting -_> Configuration --> Financial Accounting --> Financial  Reports --> Account Reports` and click ``Create``.

Suppose we would like to create our company Balance Sheet. The first report to be created, should be a View report which will contain the final details. Keep the default Sequence 0.

Now create the ``Assets`` report, and set ``Balance Sheet`` as the parent for this report. Set the Sequence to 1.

Now create the ``Liabilities`` report, and set ``Balance Sheet`` as the parent for this report too. Set the Sequence to 2.

Both these reports are of the ``View`` type.

Apart from the ``View`` type, you can select three other types: ``Accounts``, ``Account Type`` and ``Report Value``.

* *Accounts*: here you can select view accounts or individual accounts that should be included in the report. View accounts offer the advantage that when new accounts are added as a child of such view account, they will automatically be printed on the report. When selecting individual accounts, you need to specifically add each newly created account to get the correct report.

* *Account Type*: selecting an account type means that all accounts related to the selected account type(s) will be printed on the report.

* *Report Value*: thanks to this value you can include the balance of existing reports in another report. Example: create a profit & loss report (view) including costs (account class 6) and income (account class 7). In the Balance Sheet, define a report Profit&Loss Balance, with Balance Sheet as the Parent. Set the type to Report Value and link it to the P&L view report you defined. This way, the balance sheet will print the Profit&Loss result.

.. figure::  images/financial_reports.png
   :scale: 75
   :align: center

   *Financial Reports*

Create a report to print the Asset accounts (class 2 from the Belgian ledger) on the Assets side of the report. As a Parent, define the Assets report; sequence 3, type Accounts. I fyou want to use all accounts of class 2, just select the class (view account). You can also select various asset accounts. You could also have set this report to Account Type, with type Immo.

If you just want the sum of the selected accounts to appear, you leave the settings as they are. Should you wish to print the account details as well, you can select the ``Display details`` checkbox. The report will then also print the selected account numbers.

To print the results, go to :menuselection:`Accounting --> Reporting --> Legal Reports --> Accounting Reports --> Financial Report`. Select the report you want to print (only reports of the View type will be displayed in the list). You can also print a report for specific periods or dates. If you select the ``Enable Comparison`` checkbox, an extra ``Comparison`` tab will appear in which you can, for instance, select periods from a previous financial year. You have to give the comparison column a name through the ``Column Label`` field.

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
