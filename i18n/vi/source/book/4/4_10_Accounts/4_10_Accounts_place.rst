
.. i18n: .. index::
.. i18n:    single: analytic; accounts

.. index::
   single: analytic; accounts

.. i18n: Putting analytic accounts in place
.. i18n: ==================================

Putting analytic accounts in place
==================================

.. i18n: For the initial setup of good analytic accounts you should:

For the initial setup of good analytic accounts you should:

.. i18n: * set up the chart of accounts,
.. i18n: 
.. i18n: * create the different journals.

* set up the chart of accounts,

* create the different journals.

.. i18n: Setting up the chart of accounts
.. i18n: --------------------------------

Setting up the chart of accounts
--------------------------------

.. i18n: Start by choosing the most suitable analytic representation for your company before entering it into
.. i18n: Open ERP. To create the different analytic accounts, use the menu :menuselection:`Financial
.. i18n: Management --> Configuration --> Analytic Accounting --> Analytic Accounts --> New Analytic Account`.

Start by choosing the most suitable analytic representation for your company before entering it into
Open ERP. To create the different analytic accounts, use the menu :menuselection:`Financial
Management --> Configuration --> Analytic Accounting --> Analytic Accounts --> New Analytic Account`.

.. i18n: .. figure::  images/account_analytic_form.png
.. i18n:    :scale: 50
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Setting up an analytic account*

.. figure::  images/account_analytic_form.png
   :scale: 50
   :align: center

   *Setting up an analytic account*

.. i18n: To create an analytic account you have to complete the main fields:

To create an analytic account you have to complete the main fields:

.. i18n: * the :guilabel:`Account Name`,
.. i18n: 
.. i18n: * the :guilabel:`Account Code` : used as a shortcut for selecting the account,
.. i18n: 
.. i18n: * the :guilabel:`Account type` : just like general accounts the \ ``View``\   type is used for
.. i18n:   virtual accounts which are used only to create a hierarchical structure and for subtotals, and not
.. i18n:   to store accounting entries,
.. i18n: 
.. i18n: * the :guilabel:`Parent analytic account` : defines the hierarchy between the accounts.

* the :guilabel:`Account Name`,

* the :guilabel:`Account Code` : used as a shortcut for selecting the account,

* the :guilabel:`Account type` : just like general accounts the \ ``View``\   type is used for
  virtual accounts which are used only to create a hierarchical structure and for subtotals, and not
  to store accounting entries,

* the :guilabel:`Parent analytic account` : defines the hierarchy between the accounts.

.. i18n: If the project is for a limited time you can define a start and end date here. The :guilabel:`State`
.. i18n: field is used to indicate whether the project is running (\ ``Open``\  ), waiting for information
.. i18n: from the client (\ ``Pending``\ ), \ ``Draft``\   or \ ``Closed``\  .

If the project is for a limited time you can define a start and end date here. The :guilabel:`State`
field is used to indicate whether the project is running (\ ``Open``\  ), waiting for information
from the client (\ ``Pending``\ ), \ ``Draft``\   or \ ``Closed``\  .

.. i18n: Finally, if the analytic account is a client project you can complete the fields about the partner,
.. i18n: which you'd need so that you can invoice the partner:

Finally, if the analytic account is a client project you can complete the fields about the partner,
which you'd need so that you can invoice the partner:

.. i18n: * the :guilabel:`Associated partner`,
.. i18n: 
.. i18n: * a :guilabel:`Sale Pricelist`, which shows how services linked to the project should be charged,
.. i18n: 
.. i18n: * a :guilabel:`Max. Invoice Price`, showing the maximum invoice price regardless of actual
.. i18n:   overspend,
.. i18n: 
.. i18n: * a :guilabel:`Max. Quantity`, for contracts with a fixed limit of hours to use,
.. i18n: 
.. i18n: * an :guilabel:`Invoicing` field, which defines an invoicing rate and whether the project
.. i18n:   should be invoiced automatically from the services represented by the costs in the analytic account.

* the :guilabel:`Associated partner`,

* a :guilabel:`Sale Pricelist`, which shows how services linked to the project should be charged,

* a :guilabel:`Max. Invoice Price`, showing the maximum invoice price regardless of actual
  overspend,

* a :guilabel:`Max. Quantity`, for contracts with a fixed limit of hours to use,

* an :guilabel:`Invoicing` field, which defines an invoicing rate and whether the project
  should be invoiced automatically from the services represented by the costs in the analytic account.

.. i18n: .. index::
.. i18n:    single: invoicing

.. index::
   single: invoicing

.. i18n: .. tip:: Invoicing
.. i18n: 
.. i18n: 	You have several methods available to you in Open ERP for automated invoicing:
.. i18n: 
.. i18n: 	* Service companies usually use invoicing from purchase orders, analytic accounts or, more rarely,
.. i18n: 	  project management tasks.
.. i18n: 
.. i18n: 	* Manufacturing and trading companies more often use invoicing from deliveries or customer purchase
.. i18n: 	  orders.

.. tip:: Invoicing

	You have several methods available to you in Open ERP for automated invoicing:

	* Service companies usually use invoicing from purchase orders, analytic accounts or, more rarely,
	  project management tasks.

	* Manufacturing and trading companies more often use invoicing from deliveries or customer purchase
	  orders.

.. i18n: .. figure::  images/account_analytic_chart.png
.. i18n:    :scale: 50
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Example of an analytic chart for projects*

.. figure::  images/account_analytic_chart.png
   :scale: 50
   :align: center

   *Example of an analytic chart for projects*

.. i18n: Once you've defined the different analytic accounts you can view your chart through the menu
.. i18n: :menuselection:`Financial Management --> Charts --> Analytic Chart of Accounts`.

Once you've defined the different analytic accounts you can view your chart through the menu
:menuselection:`Financial Management --> Charts --> Analytic Chart of Accounts`.

.. i18n: .. index::
.. i18n:    single: module; hr_timesheet_invoice
.. i18n:    single: module; account_analytic_analysis

.. index::
   single: module; hr_timesheet_invoice
   single: module; account_analytic_analysis

.. i18n: .. tip:: Setting up an analytic account
.. i18n: 
.. i18n: 	The setup screen for an analytic account can vary greatly depending on the modules installed in
.. i18n: 	your database.
.. i18n: 	For example, you'll only see information about recharging services if you have the module
.. i18n: 	:mod:`hr_timesheet_invoice` installed.
.. i18n: 
.. i18n: 	Some of these modules add helpful management statistics to the analytic account.
.. i18n: 	The most useful is probably the module :mod:`account_analytic_analysis`,
.. i18n: 	which adds such information as indicators about your margins, invoicing amounts, and latest service
.. i18n: 	dates and invoice dates.

.. tip:: Setting up an analytic account

	The setup screen for an analytic account can vary greatly depending on the modules installed in
	your database.
	For example, you'll only see information about recharging services if you have the module
	:mod:`hr_timesheet_invoice` installed.

	Some of these modules add helpful management statistics to the analytic account.
	The most useful is probably the module :mod:`account_analytic_analysis`,
	which adds such information as indicators about your margins, invoicing amounts, and latest service
	dates and invoice dates.

.. i18n: Creating Journals
.. i18n: -----------------

Creating Journals
-----------------

.. i18n: Once the analytic chart has been created for your company you have to create the different journals.
.. i18n: These enable you to categorize the different accounting entries by their type:

Once the analytic chart has been created for your company you have to create the different journals.
These enable you to categorize the different accounting entries by their type:

.. i18n: * services,
.. i18n: 
.. i18n: * expense reimbursements,
.. i18n: 
.. i18n: * purchases of materials,
.. i18n: 
.. i18n: * miscellaneous expenditure,
.. i18n: 
.. i18n: * sales,
.. i18n: 
.. i18n: * situation entries (special situations, such as installation of the software).

* services,

* expense reimbursements,

* purchases of materials,

* miscellaneous expenditure,

* sales,

* situation entries (special situations, such as installation of the software).

.. i18n: .. index::
.. i18n:    single: journal; minimal journals

.. index::
   single: journal; minimal journals

.. i18n: .. note::  Minimal journals
.. i18n: 
.. i18n: 	At a minimum you have to create one analytic journal for Sales and one for Purchases.
.. i18n: 	If you don't create these two, Open ERP won't validate invoices linked to an analytic account
.. i18n: 	because it wouldn't be able to create an analytic accounting entry automatically.

.. note::  Minimal journals

	At a minimum you have to create one analytic journal for Sales and one for Purchases.
	If you don't create these two, Open ERP won't validate invoices linked to an analytic account
	because it wouldn't be able to create an analytic accounting entry automatically.

.. i18n: .. figure::  images/account_analytic_journal.png
.. i18n:    :scale: 50
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Creating an analytic journal*

.. figure::  images/account_analytic_journal.png
   :scale: 50
   :align: center

   *Creating an analytic journal*

.. i18n: To define your analytic journals, use the menu :menuselection:`Financial Management -->
.. i18n: Configuration --> Analytic Accounting --> Analytic Journal Definition` then click :guilabel:`New`..

To define your analytic journals, use the menu :menuselection:`Financial Management -->
Configuration --> Analytic Accounting --> Analytic Journal Definition` then click :guilabel:`New`..

.. i18n: It's easy to create an analytic journal. Just give it a :guilabel:`Name`, a :guilabel:`Code` and a :guilabel:`Type`. The
.. i18n: types available are:

It's easy to create an analytic journal. Just give it a :guilabel:`Name`, a :guilabel:`Code` and a :guilabel:`Type`. The
types available are:

.. i18n: * \ ``Sales``\  , for sales to customers and for credit notes,
.. i18n: 
.. i18n: * \ ``Purchases``\  , for purchases and miscellaneous expenses,
.. i18n: 
.. i18n: * \ ``Cash``\  , for financial entries,
.. i18n: 
.. i18n: * \ ``Situation``\  , to adjust accounts when starting an activity, or at the end of the financial
.. i18n:   year,
.. i18n: 
.. i18n: * \ ``General``\  , for all other entries.

* \ ``Sales``\  , for sales to customers and for credit notes,

* \ ``Purchases``\  , for purchases and miscellaneous expenses,

* \ ``Cash``\  , for financial entries,

* \ ``Situation``\  , to adjust accounts when starting an activity, or at the end of the financial
  year,

* \ ``General``\  , for all other entries.

.. i18n: The type of journal enables the software to automatically select the analytic journal based on the
.. i18n: nature of the operation. For example if you enter an invoice for a customer, Open ERP will
.. i18n: automatically search for an analytic journal of type \ ``Sales``\  .

The type of journal enables the software to automatically select the analytic journal based on the
nature of the operation. For example if you enter an invoice for a customer, Open ERP will
automatically search for an analytic journal of type \ ``Sales``\  .

.. i18n: .. Copyright © Open Object Press. All rights reserved.

.. Copyright © Open Object Press. All rights reserved.

.. i18n: .. You may take electronic copy of this publication and distribute it if you don't
.. i18n: .. change the content. You can also print a copy to be read by yourself only.

.. You may take electronic copy of this publication and distribute it if you don't
.. change the content. You can also print a copy to be read by yourself only.

.. i18n: .. We have contracts with different publishers in different countries to sell and
.. i18n: .. distribute paper or electronic based versions of this book (translated or not)
.. i18n: .. in bookstores. This helps to distribute and promote the Open ERP product. It
.. i18n: .. also helps us to create incentives to pay contributors and authors using author
.. i18n: .. rights of these sales.

.. We have contracts with different publishers in different countries to sell and
.. distribute paper or electronic based versions of this book (translated or not)
.. in bookstores. This helps to distribute and promote the Open ERP product. It
.. also helps us to create incentives to pay contributors and authors using author
.. rights of these sales.

.. i18n: .. Due to this, grants to translate, modify or sell this book are strictly
.. i18n: .. forbidden, unless Tiny SPRL (representing Open Object Press) gives you a
.. i18n: .. written authorisation for this.

.. Due to this, grants to translate, modify or sell this book are strictly
.. forbidden, unless Tiny SPRL (representing Open Object Press) gives you a
.. written authorisation for this.

.. i18n: .. Many of the designations used by manufacturers and suppliers to distinguish their
.. i18n: .. products are claimed as trademarks. Where those designations appear in this book,
.. i18n: .. and Open Object Press was aware of a trademark claim, the designations have been
.. i18n: .. printed in initial capitals.

.. Many of the designations used by manufacturers and suppliers to distinguish their
.. products are claimed as trademarks. Where those designations appear in this book,
.. and Open Object Press was aware of a trademark claim, the designations have been
.. printed in initial capitals.

.. i18n: .. While every precaution has been taken in the preparation of this book, the publisher
.. i18n: .. and the authors assume no responsibility for errors or omissions, or for damages
.. i18n: .. resulting from the use of the information contained herein.

.. While every precaution has been taken in the preparation of this book, the publisher
.. and the authors assume no responsibility for errors or omissions, or for damages
.. resulting from the use of the information contained herein.

.. i18n: .. Published by Open Object Press, Grand Rosière, Belgium

.. Published by Open Object Press, Grand Rosière, Belgium
