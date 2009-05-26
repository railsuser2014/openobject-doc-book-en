
.. i18n: Statutory taxes and accounts
.. i18n: ============================

Statutory taxes and accounts
============================

.. i18n: This section deals with statutory taxes and accounts which are legally required from the company:

This section deals with statutory taxes and accounts which are legally required from the company:

.. i18n: * the taxation structure provided by Open ERP,
.. i18n: 
.. i18n: * the accounts ledgers,
.. i18n: 
.. i18n: * account balance (used to produce the income statement and balance sheet),
.. i18n: 
.. i18n: * the different journals (general, centralized and detailed),
.. i18n: 
.. i18n: * the tax declaration.

* the taxation structure provided by Open ERP,

* the accounts ledgers,

* account balance (used to produce the income statement and balance sheet),

* the different journals (general, centralized and detailed),

* the tax declaration.

.. i18n: .. tip:: Other declarations
.. i18n: 
.. i18n: 	In addition to the legal declarations available in the accounts modules,
.. i18n: 	Open ERP supplies declarations based on the functionality in other modules.
.. i18n: 	
.. i18n: 	.. index::
.. i18n: 	   single: module; report_instrastat
.. i18n: 
.. i18n: 	You can, for example, install the :mod:`report_intrastat` module for intra-stat declarations
.. i18n: 	about sending goods to and receiving goods from other countries.

.. tip:: Other declarations

	In addition to the legal declarations available in the accounts modules,
	Open ERP supplies declarations based on the functionality in other modules.
	
	.. index::
	   single: module; report_instrastat

	You can, for example, install the :mod:`report_intrastat` module for intra-stat declarations
	about sending goods to and receiving goods from other countries.

.. i18n: .. index:: tax

.. index:: tax

.. i18n: Taxation
.. i18n: --------

Taxation
--------

.. i18n: You can attach taxes to financial transactions so that you can

You can attach taxes to financial transactions so that you can

.. i18n: * add taxes to the amount that you pay or get paid,
.. i18n: 
.. i18n: * report on the taxes in various categories that you should pay the tax authorities,
.. i18n: 
.. i18n: * track taxes in your general accounts,
.. i18n: 
.. i18n: * manage the payment and refund of taxes using the same mechanisms that Open ERP uses for other
.. i18n:   monetary transactions.

* add taxes to the amount that you pay or get paid,

* report on the taxes in various categories that you should pay the tax authorities,

* track taxes in your general accounts,

* manage the payment and refund of taxes using the same mechanisms that Open ERP uses for other
  monetary transactions.

.. i18n: Since the detailed tax structure is a mechanism for carrying out governments' policies, and the
.. i18n: collecting of taxes so critical to their authorities, tax requirements and reporting can be
.. i18n: complex. Open ERP has a flexible mechanism for handling taxation that can be configured through its
.. i18n: GUI or through data import mechanisms to meet the requirements of many various tax jurisdictions.

Since the detailed tax structure is a mechanism for carrying out governments' policies, and the
collecting of taxes so critical to their authorities, tax requirements and reporting can be
complex. Open ERP has a flexible mechanism for handling taxation that can be configured through its
GUI or through data import mechanisms to meet the requirements of many various tax jurisdictions.

.. i18n: The taxation mechanism can also be used to handle other tax-like financial transactions, such as
.. i18n: royalties to authors based on the value of transactions through an account.

The taxation mechanism can also be used to handle other tax-like financial transactions, such as
royalties to authors based on the value of transactions through an account.

.. i18n: Setting up a tax structure
.. i18n: ^^^^^^^^^^^^^^^^^^^^^^^^^^

Setting up a tax structure
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. i18n: Three main objects are involved in the tax system in Open ERP:

Three main objects are involved in the tax system in Open ERP:

.. i18n: * a :guilabel:`Tax Case` (or :guilabel:`Tax Code`), used for tax reporting, that can be set up in a hierarchical
.. i18n:   structure so that multiple codes can be formed into trees in the same way as a Chart of Accounts.
.. i18n: 
.. i18n: * a :guilabel:`Tax`, the basic tax object that contains the rules for calculating tax on the financial
.. i18n:   transaction it's attached to, and is linked to the General Accounts and to the Tax Cases. A tax can
.. i18n:   contain multiple child taxes and base its calculation on those taxes rather than the base
.. i18n:   transaction, providing considerable flexibility. Each tax belongs to a :guilabel:`Tax Group` (currently just
.. i18n:   \ ``VAT``\   or \ ``Other``\  ).
.. i18n: 
.. i18n: * the :guilabel:`General Accounts`, that record the taxes owing and paid. Since the general accounts are
.. i18n:   discussed elsewhere in this part of the book and are not tax-specific, they won't be detailed in
.. i18n:   this section.

* a :guilabel:`Tax Case` (or :guilabel:`Tax Code`), used for tax reporting, that can be set up in a hierarchical
  structure so that multiple codes can be formed into trees in the same way as a Chart of Accounts.

* a :guilabel:`Tax`, the basic tax object that contains the rules for calculating tax on the financial
  transaction it's attached to, and is linked to the General Accounts and to the Tax Cases. A tax can
  contain multiple child taxes and base its calculation on those taxes rather than the base
  transaction, providing considerable flexibility. Each tax belongs to a :guilabel:`Tax Group` (currently just
  \ ``VAT``\   or \ ``Other``\  ).

* the :guilabel:`General Accounts`, that record the taxes owing and paid. Since the general accounts are
  discussed elsewhere in this part of the book and are not tax-specific, they won't be detailed in
  this section.

.. i18n: You can attach zero or more :guilabel:`Supplier Tax` and :guilabel:`Customer Tax` items to products, so that you can
.. i18n: account separately for purchase and sales taxes (or Input and Output VAT – where VAT is Value
.. i18n: Added Tax). Because you can attach more than one tax, you can handle a VAT or Sales Tax separately
.. i18n: from an Eco Tax on the same product.

You can attach zero or more :guilabel:`Supplier Tax` and :guilabel:`Customer Tax` items to products, so that you can
account separately for purchase and sales taxes (or Input and Output VAT – where VAT is Value
Added Tax). Because you can attach more than one tax, you can handle a VAT or Sales Tax separately
from an Eco Tax on the same product.

.. i18n: You can also attach a :guilabel:`Default Tax` to a Partner, which replaces any taxes belonging to
.. i18n: the same Tax Group that may have been defined in a Product.

You can also attach a :guilabel:`Default Tax` to a Partner, which replaces any taxes belonging to
the same Tax Group that may have been defined in a Product.

.. i18n: So you can define a \ ``Tax Exempt``\   tax in the \ ``VAT``\   group and assign it to partners who
.. i18n: declare themselves to be charities. All product sales to a charity would then be VAT free even if
.. i18n: the products themselves carry various tax rates, but non-VAT taxes such as Eco-taxes can still be
.. i18n: applied.

So you can define a \ ``Tax Exempt``\   tax in the \ ``VAT``\   group and assign it to partners who
declare themselves to be charities. All product sales to a charity would then be VAT free even if
the products themselves carry various tax rates, but non-VAT taxes such as Eco-taxes can still be
applied.

.. i18n: Tax Cases
.. i18n: ^^^^^^^^^

Tax Cases
^^^^^^^^^

.. i18n: Tax Cases are also known in Open ERP as Tax Codes. They're used for tax reporting, and can be set
.. i18n: up in a hierarchical structure to form trees in the same way as a Chart of Accounts.

Tax Cases are also known in Open ERP as Tax Codes. They're used for tax reporting, and can be set
up in a hierarchical structure to form trees in the same way as a Chart of Accounts.

.. i18n: To create a new Tax Case, use the menu :menuselection:`Financial Management --> Configuration -->
.. i18n: Taxes --> Tax Codes`. You define the following fields:

To create a new Tax Case, use the menu :menuselection:`Financial Management --> Configuration -->
Taxes --> Tax Codes`. You define the following fields:

.. i18n: *  :guilabel:`Tax Case Name` : a unique name required to identify the Case,
.. i18n: 
.. i18n: *  :guilabel:`Company` : a required link that attaches the Case to a specific company, such as the
.. i18n:    Main Company,
.. i18n: 
.. i18n: *  :guilabel:`Case Code` : an optional short code for the case,
.. i18n: 
.. i18n: *  :guilabel:`Parent Code` : a link to a parent Tax Case that forms the basis of the tree structure
.. i18n:    like a Chart of Accounts,
.. i18n: 
.. i18n: *  :guilabel:`Sign for Parent` : choose 1.00 to add the total to the parent account or -1.00 to
.. i18n:    subtract it,
.. i18n: 
.. i18n: *  :guilabel:`Description` : a free text field for documentation purposes.

*  :guilabel:`Tax Case Name` : a unique name required to identify the Case,

*  :guilabel:`Company` : a required link that attaches the Case to a specific company, such as the
   Main Company,

*  :guilabel:`Case Code` : an optional short code for the case,

*  :guilabel:`Parent Code` : a link to a parent Tax Case that forms the basis of the tree structure
   like a Chart of Accounts,

*  :guilabel:`Sign for Parent` : choose 1.00 to add the total to the parent account or -1.00 to
   subtract it,

*  :guilabel:`Description` : a free text field for documentation purposes.

.. i18n: You can also see two read-only fields:

You can also see two read-only fields:

.. i18n: *  :guilabel:`Year Sum` : a single figure showing the total accumulated on this case for the
.. i18n:    financial year.
.. i18n: 
.. i18n: *  :guilabel:`Period Sum` : a single figure showing the total accumulated on this case for the
.. i18n:    current financial period (perhaps 1 month or 3 months).

*  :guilabel:`Year Sum` : a single figure showing the total accumulated on this case for the
   financial year.

*  :guilabel:`Period Sum` : a single figure showing the total accumulated on this case for the
   current financial period (perhaps 1 month or 3 months).

.. i18n: You will probably need to create two tax cases for each different tax rate that you have to define,
.. i18n: one for the tax itself and one for the invoice amount that the tax is based on. And you'll create
.. i18n: tax cases that you won't link to Tax objects (similar to General Account \ ``View``\   types) just
.. i18n: to organize the tree structure.

You will probably need to create two tax cases for each different tax rate that you have to define,
one for the tax itself and one for the invoice amount that the tax is based on. And you'll create
tax cases that you won't link to Tax objects (similar to General Account \ ``View``\   types) just
to organize the tree structure.

.. i18n: To view the structure that you've constructed you can use the menu :menuselection:`Financial
.. i18n: Management --> Reporting --> Taxes Report --> Chart of Taxes`. This tree view reflects the structure of the 
.. i18n: :guilabel:`Tax Cases` and shows the current tax situation.

To view the structure that you've constructed you can use the menu :menuselection:`Financial
Management --> Reporting --> Taxes Report --> Chart of Taxes`. This tree view reflects the structure of the 
:guilabel:`Tax Cases` and shows the current tax situation.

.. i18n: Tax objects
.. i18n: ^^^^^^^^^^^

Tax objects
^^^^^^^^^^^

.. i18n: Tax objects calculate tax on the financial transactions that they're attached to, and are linked to
.. i18n: the General Accounts and to the Tax Cases.

Tax objects calculate tax on the financial transactions that they're attached to, and are linked to
the General Accounts and to the Tax Cases.

.. i18n: To create a new Tax Case, use the menu :menuselection:`Financial Management --> Configuration -->
.. i18n: Financial Accounting --> Taxes --> Taxes`. You define the following fields:

To create a new Tax Case, use the menu :menuselection:`Financial Management --> Configuration -->
Financial Accounting --> Taxes --> Taxes`. You define the following fields:

.. i18n: *  :guilabel:`Tax Name` : a unique name required for this tax (such as \ ``12% Sales VAT``\  ),
.. i18n: 
.. i18n: *  :guilabel:`Company` : a required link to a company associated with the tax, such as the Main
.. i18n:    Company,
.. i18n: 
.. i18n: *  :guilabel:`Tax Group` : \ ``VAT``\   or \ ``Other``\  , used to determine which taxes on products
.. i18n:    can be substituted by taxes on partners,
.. i18n: 
.. i18n: *  :guilabel:`Tax Type` : a required field directing how to calculate the tax: \ ``Percent``\  , 
.. i18n:    \``Fixed``\  , \ ``None``\   or \ ``Python Code``\  , (the latter is found in the :guilabel:`Compute Code`
.. i18n:    field in the :guilabel:`Special Computation` tab),
.. i18n: 
.. i18n: *  :guilabel:`Applicable Type` : a required field that indicates whether the base amount should be
.. i18n:    used unchanged (when the value is \ ``True``\  ) or whether it should be processed by Python Code in
.. i18n:    the :guilabel:`Applicable Code` field in the :guilabel:`Special Computation` tab when the value is \ ``Code``\  ),
.. i18n: 
.. i18n: *  :guilabel:`Amount` : a required field whose meaning depends on the Tax Type, being a multiplier
.. i18n:    on the base amount when the :guilabel:`Tax Type` is \ ``Percent``\  , and a fixed amount added to the base
.. i18n:    amount when the :guilabel:`Tax Type` is \ ``Fixed``\  ,
.. i18n: 
.. i18n: *  :guilabel:`Include in base amount` : when checked, the tax is added to the base amount and not
.. i18n:    shown separately,
.. i18n: 
.. i18n: *  :guilabel:`Domain` : is only used in special developments, not in the core Open ERP system,
.. i18n: 
.. i18n: *  :guilabel:`Invoice Tax Account` :a General Account used to record invoiced tax amounts, which may
.. i18n:    be the same for several taxes or split so that one tax is allocated to one account,
.. i18n: 
.. i18n: *  :guilabel:`Refund Tax Account` : a General Account used to record invoiced tax refunds, which may
.. i18n:    be the same as the Invoice Tax Account or, in some tax jurisdictions, must be separated,
.. i18n: 
.. i18n: *  :guilabel:`Tax on Children` : when checked, the tax calculation is applied to the output from other
.. i18n:    tax calculations specified in the :guilabel:`Childs Tax Account` field (so you can have taxes on
.. i18n:    taxes), otherwise the calculation is applied to the base amount on the transaction,
.. i18n: 
.. i18n: *  :guilabel:`Tax included in Price` : when checked, the total value shown includes this tax,
.. i18n: 
.. i18n: *  :guilabel:`Tax Application` : selects whether the tax is applicable to Sale, Purchase or All
.. i18n:    transactions,
.. i18n: 
.. i18n: *  :guilabel:`Child Tax Accounts` : other tax accounts that can be used to supply the figure for
.. i18n:    taxation.

*  :guilabel:`Tax Name` : a unique name required for this tax (such as \ ``12% Sales VAT``\  ),

*  :guilabel:`Company` : a required link to a company associated with the tax, such as the Main
   Company,

*  :guilabel:`Tax Group` : \ ``VAT``\   or \ ``Other``\  , used to determine which taxes on products
   can be substituted by taxes on partners,

*  :guilabel:`Tax Type` : a required field directing how to calculate the tax: \ ``Percent``\  , 
   \``Fixed``\  , \ ``None``\   or \ ``Python Code``\  , (the latter is found in the :guilabel:`Compute Code`
   field in the :guilabel:`Special Computation` tab),

*  :guilabel:`Applicable Type` : a required field that indicates whether the base amount should be
   used unchanged (when the value is \ ``True``\  ) or whether it should be processed by Python Code in
   the :guilabel:`Applicable Code` field in the :guilabel:`Special Computation` tab when the value is \ ``Code``\  ),

*  :guilabel:`Amount` : a required field whose meaning depends on the Tax Type, being a multiplier
   on the base amount when the :guilabel:`Tax Type` is \ ``Percent``\  , and a fixed amount added to the base
   amount when the :guilabel:`Tax Type` is \ ``Fixed``\  ,

*  :guilabel:`Include in base amount` : when checked, the tax is added to the base amount and not
   shown separately,

*  :guilabel:`Domain` : is only used in special developments, not in the core Open ERP system,

*  :guilabel:`Invoice Tax Account` :a General Account used to record invoiced tax amounts, which may
   be the same for several taxes or split so that one tax is allocated to one account,

*  :guilabel:`Refund Tax Account` : a General Account used to record invoiced tax refunds, which may
   be the same as the Invoice Tax Account or, in some tax jurisdictions, must be separated,

*  :guilabel:`Tax on Children` : when checked, the tax calculation is applied to the output from other
   tax calculations specified in the :guilabel:`Childs Tax Account` field (so you can have taxes on
   taxes), otherwise the calculation is applied to the base amount on the transaction,

*  :guilabel:`Tax included in Price` : when checked, the total value shown includes this tax,

*  :guilabel:`Tax Application` : selects whether the tax is applicable to Sale, Purchase or All
   transactions,

*  :guilabel:`Child Tax Accounts` : other tax accounts that can be used to supply the figure for
   taxation.

.. i18n: .. tip:: Using Child Taxes
.. i18n: 
.. i18n: 	You can use child taxes when you have a complex tax situation that you want to hide your end users
.. i18n: 	from.
.. i18n: 	For example, you might define a motor mileage expenses product with a composite tax made up of two
.. i18n: 	child taxes –
.. i18n: 	a non-reclaimable private element and a reclaimable business element (which is the case in some
.. i18n: 	European countries).
.. i18n: 
.. i18n: 	When your staff come to claim motor mileage, they do not need to know about this taxation,
.. i18n: 	but the accounting impact of their claim will be automatically managed in Open ERP.

.. tip:: Using Child Taxes

	You can use child taxes when you have a complex tax situation that you want to hide your end users
	from.
	For example, you might define a motor mileage expenses product with a composite tax made up of two
	child taxes –
	a non-reclaimable private element and a reclaimable business element (which is the case in some
	European countries).

	When your staff come to claim motor mileage, they do not need to know about this taxation,
	but the accounting impact of their claim will be automatically managed in Open ERP.

.. i18n: The fields above apply the taxes that you specify and record them in the general accounts but don't
.. i18n: provide you with the documentation that your tax authorities might need. For this use the Tax
.. i18n: Declaration tab to define which Tax Cases should be used for this tax:

The fields above apply the taxes that you specify and record them in the general accounts but don't
provide you with the documentation that your tax authorities might need. For this use the Tax
Declaration tab to define which Tax Cases should be used for this tax:

.. i18n: *  :guilabel:`Invoices/Base Code` : tax case to record the invoiced amount that the tax is based on,
.. i18n: 
.. i18n: *  :guilabel:`Invoices/Tax Code` : tax case to record the invoiced tax amount
.. i18n: 
.. i18n: *  :guilabel:`Credit Notes/Refund Base Code` : tax case to record the refund invoice amount that the tax
.. i18n:    is based on,
.. i18n: 
.. i18n: *  :guilabel:`Credit Notes/Refund Tax Code` : tax case to record the refund invoice tax amount.

*  :guilabel:`Invoices/Base Code` : tax case to record the invoiced amount that the tax is based on,

*  :guilabel:`Invoices/Tax Code` : tax case to record the invoiced tax amount

*  :guilabel:`Credit Notes/Refund Base Code` : tax case to record the refund invoice amount that the tax
   is based on,

*  :guilabel:`Credit Notes/Refund Tax Code` : tax case to record the refund invoice tax amount.

.. i18n: Use of Taxes on Products, Partners, Projects and Accounts
.. i18n: ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Use of Taxes on Products, Partners, Projects and Accounts
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. i18n: When you've created a tax structure consisting of Tax Cases and Tax objects, you can use the taxes
.. i18n: in your various business objects so that financial transactions can be associated with taxes and
.. i18n: tax-like charges.

When you've created a tax structure consisting of Tax Cases and Tax objects, you can use the taxes
in your various business objects so that financial transactions can be associated with taxes and
tax-like charges.

.. i18n: .. tip:: Retail Customers
.. i18n: 
.. i18n: 	When you're retailing to end users rather than selling to a business,
.. i18n: 	you may want to (or be required to) show tax-inclusive prices on your invoicing documents rather
.. i18n: 	than a tax-exclusive price plus tax.
.. i18n: 	
.. i18n: 	.. index::
.. i18n: 	   single: module; account_tax_include
.. i18n: 	
.. i18n: 	To do this in Open ERP just install the :mod:`account_tax_include` module.
.. i18n: 	Each invoice is given a new :guilabel:`Price method` field, in which you choose 
.. i18n: 	:guilabel:`Tax included` or :guilabel:`Tax excluded`.
.. i18n: 	Prices are then displayed appropriately.

.. tip:: Retail Customers

	When you're retailing to end users rather than selling to a business,
	you may want to (or be required to) show tax-inclusive prices on your invoicing documents rather
	than a tax-exclusive price plus tax.
	
	.. index::
	   single: module; account_tax_include
	
	To do this in Open ERP just install the :mod:`account_tax_include` module.
	Each invoice is given a new :guilabel:`Price method` field, in which you choose 
	:guilabel:`Tax included` or :guilabel:`Tax excluded`.
	Prices are then displayed appropriately.

.. i18n: You can assign a tax to a Partner so that it overrides any tax defined in a Product. You'd do this,
.. i18n: for example, if a partner was a charity and paid a lower or zero rate of VAT or Sales Tax on its
.. i18n: purchases. Assuming that you have an appropriate Charities VAT or Sales Tax in the \ ``VAT``\  :guilabel:`Tax
.. i18n: Group`, use the menu :menuselection:`Partners --> Partners` to open and edit a Partner form for the
.. i18n: charity, then:

You can assign a tax to a Partner so that it overrides any tax defined in a Product. You'd do this,
for example, if a partner was a charity and paid a lower or zero rate of VAT or Sales Tax on its
purchases. Assuming that you have an appropriate Charities VAT or Sales Tax in the \ ``VAT``\  :guilabel:`Tax
Group`, use the menu :menuselection:`Partners --> Partners` to open and edit a Partner form for the
charity, then:

.. i18n: * select the :guilabel:`Properties` tab,
.. i18n: 
.. i18n: * set the :guilabel:`Default Tax` field to the \ ``Charities VAT``\   tax.

* select the :guilabel:`Properties` tab,

* set the :guilabel:`Default Tax` field to the \ ``Charities VAT``\   tax.

.. i18n: You can assign multiple taxes to a Product. Assuming you have set up the appropriate taxes, you
.. i18n: would use the menu :menuselection:`Products --> Products` to open and edit a Product definition,
.. i18n: then:

You can assign multiple taxes to a Product. Assuming you have set up the appropriate taxes, you
would use the menu :menuselection:`Products --> Products` to open and edit a Product definition,
then:

.. i18n: * select one or more :guilabel:`Customer Taxes`  for any products that you might sell, which may
.. i18n:   include a \ ``Sales Tax``\   or \ ``Output VAT``\  , and a \ ``Sales Eco Tax``\  ,
.. i18n: 
.. i18n: * select one or more :guilabel:`Supplier Taxes` for any products that you might purchase, which may
.. i18n:   include a \ ``Purchase Tax``\   or \ ``Input VAT``\  , and a \ ``Purchase Eco Tax``\  .

* select one or more :guilabel:`Customer Taxes`  for any products that you might sell, which may
  include a \ ``Sales Tax``\   or \ ``Output VAT``\  , and a \ ``Sales Eco Tax``\  ,

* select one or more :guilabel:`Supplier Taxes` for any products that you might purchase, which may
  include a \ ``Purchase Tax``\   or \ ``Input VAT``\  , and a \ ``Purchase Eco Tax``\  .

.. i18n: Generally, when you make a purchase or sale, the taxes assigned to the product are used to calculate
.. i18n: the taxes owing or owed. But when you make a transaction with a partner that has a :guilabel:`Default Tax`
.. i18n: defined, for example a sale to a charity with \ ``Charities ``\  \ ``Tax``\  , that tax will be used
.. i18n: in place of other Product taxes in the same group – in this case replacing the standard \ ``Sales
.. i18n: Tax``\   or \ ``Output VAT``\  .

Generally, when you make a purchase or sale, the taxes assigned to the product are used to calculate
the taxes owing or owed. But when you make a transaction with a partner that has a :guilabel:`Default Tax`
defined, for example a sale to a charity with \ ``Charities ``\  \ ``Tax``\  , that tax will be used
in place of other Product taxes in the same group – in this case replacing the standard \ ``Sales
Tax``\   or \ ``Output VAT``\  .

.. i18n: You can also assign multiple taxes to a Project, so that invoices from the Project carry an
.. i18n: appropriate rate of tax (project invoicing is dealt with in detail in :ref:`ch-projects`).

You can also assign multiple taxes to a Project, so that invoices from the Project carry an
appropriate rate of tax (project invoicing is dealt with in detail in :ref:`ch-projects`).

.. i18n: .. index::
.. i18n:    single: module; import_export

.. index::
   single: module; import_export

.. i18n: .. note:: Tax regions
.. i18n: 
.. i18n: 	The third-party module :mod:`import_export` (currently in ``addons-extra`` 
.. i18n: 	can be used to extend Open ERP's tax system,
.. i18n: 	so that you can assign taxes to different accounts depending on the location of the Partner.
.. i18n: 	The :guilabel:`Partner` is given a new :guilabel:`Partner Location` field that can be set to Local,
.. i18n: 	Europe or Outside,
.. i18n: 	so that taxes and tax bases can be channelled to different accounts.
.. i18n: 
.. i18n: 	This module could be the basis of more ambitious location-based tax accounting.

.. note:: Tax regions

	The third-party module :mod:`import_export` (currently in ``addons-extra`` 
	can be used to extend Open ERP's tax system,
	so that you can assign taxes to different accounts depending on the location of the Partner.
	The :guilabel:`Partner` is given a new :guilabel:`Partner Location` field that can be set to Local,
	Europe or Outside,
	so that taxes and tax bases can be channelled to different accounts.

	This module could be the basis of more ambitious location-based tax accounting.

.. i18n: And you can assign multiple taxes to an account so that when you transfer money through the account
.. i18n: you attract a tax amount. In such a case, this 'tax' may not be legally-required taxation but
.. i18n: something tax-like, for example authors' royalties or sales commission.

And you can assign multiple taxes to an account so that when you transfer money through the account
you attract a tax amount. In such a case, this 'tax' may not be legally-required taxation but
something tax-like, for example authors' royalties or sales commission.

.. i18n: .. index::
.. i18n:    single: balance sheet

.. index::
   single: balance sheet

.. i18n: The accounts ledgers and the balance sheet
.. i18n: ------------------------------------------

The accounts ledgers and the balance sheet
------------------------------------------

.. i18n: To print the balance of accounts or the accounts ledgers you should turn to the Chart of Accounts.
.. i18n: To do that go to the menu :menuselection:`Financial Management --> Charts --> Charts of Accounts`.

To print the balance of accounts or the accounts ledgers you should turn to the Chart of Accounts.
To do that go to the menu :menuselection:`Financial Management --> Charts --> Charts of Accounts`.

.. i18n: Select the accounting period and type of moves (all entries or just posted entries) you're interested in
.. i18n: and click :guilabel:`Open Charts` to display the chart in a tree view, then select one
.. i18n: or several accounts for analysis by clicking and highlighting the appropriate line(s). 
.. i18n: Click the :guilabel:`General Ledger`, the :guilabel:`Account
.. i18n: balance`, or an :guilabel:`Analytic check` in the :guilabel:`Reports` toolbar at the right. 
.. i18n: If you select an account which has sub-accounts in the
.. i18n: hierarchy you automatically analyze both that account and its child accounts.

Select the accounting period and type of moves (all entries or just posted entries) you're interested in
and click :guilabel:`Open Charts` to display the chart in a tree view, then select one
or several accounts for analysis by clicking and highlighting the appropriate line(s). 
Click the :guilabel:`General Ledger`, the :guilabel:`Account
balance`, or an :guilabel:`Analytic check` in the :guilabel:`Reports` toolbar at the right. 
If you select an account which has sub-accounts in the
hierarchy you automatically analyze both that account and its child accounts.

.. i18n: .. index::
.. i18n:    single: module; account_simulation

.. index::
   single: module; account_simulation

.. i18n: .. tip::  Simulated balance
.. i18n: 
.. i18n: 	While you're printing account balances,
.. i18n: 	if you have installed the :mod:`account_simulation` module from addons-extra,
.. i18n: 	Open ERP asks you which level of
.. i18n: 	simulation to execute.
.. i18n: 
.. i18n: 	Results will vary depending on the level selected.
.. i18n: 	You could, for example, print the balance depending on various methods of amortization:
.. i18n: 
.. i18n: 	* the normal IFRS method,
.. i18n: 
.. i18n: 	* the French method.
.. i18n: 
.. i18n: 	More generally it enables you to make analyses using other simulation levels that you could
.. i18n: 	expect.

.. tip::  Simulated balance

	While you're printing account balances,
	if you have installed the :mod:`account_simulation` module from addons-extra,
	Open ERP asks you which level of
	simulation to execute.

	Results will vary depending on the level selected.
	You could, for example, print the balance depending on various methods of amortization:

	* the normal IFRS method,

	* the French method.

	More generally it enables you to make analyses using other simulation levels that you could
	expect.

.. i18n: .. index::
.. i18n:    single: module; account_reporting

.. index::
   single: module; account_reporting

.. i18n: The :mod:`account_reporting` module was developed to provide configurable reports for balance sheets
.. i18n: or earnings statements in legally required formats.

The :mod:`account_reporting` module was developed to provide configurable reports for balance sheets
or earnings statements in legally required formats.

.. i18n: .. index:: journal

.. index:: journal

.. i18n: The accounting journals
.. i18n: -----------------------

The accounting journals
-----------------------

.. i18n: To obtain the different journals use the menu :menuselection:`Financial Management --> Reporting -->
.. i18n: Journals`.

To obtain the different journals use the menu :menuselection:`Financial Management --> Reporting -->
Journals`.

.. i18n: .. index::
.. i18n:    single: module; sale_journal
.. i18n:    single: module; purchase_journal

.. index::
   single: module; sale_journal
   single: module; purchase_journal

.. i18n: .. note::  Journals
.. i18n: 
.. i18n: 	Note there are different types of journal in Open ERP
.. i18n: 
.. i18n: 	* accounting journals (detailed in this chapter),
.. i18n: 
.. i18n: 	* purchase journals (for distributing supplies provided on certain dates),
.. i18n: 
.. i18n: 	* sales journals (for example classifying sales by their type of trade),
.. i18n: 
.. i18n: 	* the invoice journals (to classify sales by mode of invoicing - daily / weekly / monthly - and
.. i18n: 	  automating the tasks.
.. i18n: 
.. i18n: 	To get access to these different journals install the modules :mod:`sale_journal` (found at the time of
.. i18n: 	writing in ``addons``, so available in a standard installation) and :mod:`purchase_journal` (found in
.. i18n: 	``addons-extra`` at the time of writing, so needing special installation).

.. note::  Journals

	Note there are different types of journal in Open ERP

	* accounting journals (detailed in this chapter),

	* purchase journals (for distributing supplies provided on certain dates),

	* sales journals (for example classifying sales by their type of trade),

	* the invoice journals (to classify sales by mode of invoicing - daily / weekly / monthly - and
	  automating the tasks.

	To get access to these different journals install the modules :mod:`sale_journal` (found at the time of
	writing in ``addons``, so available in a standard installation) and :mod:`purchase_journal` (found in
	``addons-extra`` at the time of writing, so needing special installation).

.. i18n: .. todo:: which reports are these - the Reports to the right?

.. todo:: which reports are these - the Reports to the right?

.. i18n: Then select one or several journals and click :guilabel:`Print`. Open ERP then proposes various reports:

Then select one or several journals and click :guilabel:`Print`. Open ERP then proposes various reports:

.. i18n: * detailed accounting entries,
.. i18n: 
.. i18n: * general journal,
.. i18n: 
.. i18n: * journal grouped by account.

* detailed accounting entries,

* general journal,

* journal grouped by account.

.. i18n: .. figure::  images/account_journal_print.png
.. i18n:    :scale: 50
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Printing a journal*

.. figure::  images/account_journal_print.png
   :scale: 50
   :align: center

   *Printing a journal*

.. i18n: Tax declaration
.. i18n: ---------------

Tax declaration
---------------

.. i18n: Information required for a tax declaration is automatically generated by Open ERP from invoices. In
.. i18n: the section on invoicing you'll have seen that you can get details of tax information from the area
.. i18n: at the bottom left of an invoice.

Information required for a tax declaration is automatically generated by Open ERP from invoices. In
the section on invoicing you'll have seen that you can get details of tax information from the area
at the bottom left of an invoice.

.. i18n: You can also get the information from the accounting entries in the columns to the right.

You can also get the information from the accounting entries in the columns to the right.

.. i18n: Open ERP keeps a tax chart that you can reach from the menu :menuselection:`Financial Management
.. i18n: --> Periodical Processing --> Taxes`. The structure of the chart is for calculating the tax
.. i18n: declaration but also all the other taxes can be calculated (such as the French DEEE).

Open ERP keeps a tax chart that you can reach from the menu :menuselection:`Financial Management
--> Periodical Processing --> Taxes`. The structure of the chart is for calculating the tax
declaration but also all the other taxes can be calculated (such as the French DEEE).

.. i18n: .. index::
.. i18n:    single: TVA
.. i18n:    single: VAT

.. index::
   single: TVA
   single: VAT

.. i18n: .. figure::  images/account_tax_chart.png
.. i18n:    :scale: 50
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Example of a Belgian TVA (VAT) declaration*

.. figure::  images/account_tax_chart.png
   :scale: 50
   :align: center

   *Example of a Belgian TVA (VAT) declaration*

.. i18n: The tax chart represents the amount of each area of the tax declaration for your country. It's
.. i18n: presented in a hierarchical structure which lets you see the detail only of what interests you and
.. i18n: hides the less interesting subtotals. This structure can be altered as you wish to fit your needs.

The tax chart represents the amount of each area of the tax declaration for your country. It's
presented in a hierarchical structure which lets you see the detail only of what interests you and
hides the less interesting subtotals. This structure can be altered as you wish to fit your needs.

.. i18n: You can create several tax charts if your company is subject to different types of tax or tax-like
.. i18n: accounts, such as:

You can create several tax charts if your company is subject to different types of tax or tax-like
accounts, such as:

.. i18n: * authors' rights,
.. i18n: 
.. i18n: * ecotaxes such as the French DEEE for recycling electrical equipment.

* authors' rights,

* ecotaxes such as the French DEEE for recycling electrical equipment.

.. i18n: Each accounting entry can then be linked to one of the tax accounts. This association is done
.. i18n: automatically by the taxes which had previously been configured in the invoice lines.

Each accounting entry can then be linked to one of the tax accounts. This association is done
automatically by the taxes which had previously been configured in the invoice lines.

.. i18n: .. tip:: Tax declaration
.. i18n: 
.. i18n: 	Some accounting software manages the tax declaration in a dedicated general account.
.. i18n: 	The declaration is then limited to the balance in the specified period.
.. i18n: 	In Open ERP you can create an independent chart of taxes, which has several advantages:
.. i18n: 
.. i18n: 	* it's possible to allocate only a part of the tax transaction,
.. i18n: 
.. i18n: 	* it's not necessary to manage several different general accounts depending on the type of sale and
.. i18n: 	  type of tax,
.. i18n: 
.. i18n: 	* you can restructure your chart of taxes as you need.

.. tip:: Tax declaration

	Some accounting software manages the tax declaration in a dedicated general account.
	The declaration is then limited to the balance in the specified period.
	In Open ERP you can create an independent chart of taxes, which has several advantages:

	* it's possible to allocate only a part of the tax transaction,

	* it's not necessary to manage several different general accounts depending on the type of sale and
	  type of tax,

	* you can restructure your chart of taxes as you need.

.. i18n: At any time you can check your chart of taxes for a given period using the report
.. i18n: :menuselection:`Financial Management --> Reporting --> Taxes Reports --> Print Taxes Report`.

At any time you can check your chart of taxes for a given period using the report
:menuselection:`Financial Management --> Reporting --> Taxes Reports --> Print Taxes Report`.

.. i18n: This data is updated in real time. That's very useful because it enables you to preview at any time
.. i18n: the tax that you owe at the start and end of the month or quarter.

This data is updated in real time. That's very useful because it enables you to preview at any time
the tax that you owe at the start and end of the month or quarter.

.. i18n: Furthermore, for your tax declaration you can click on one of the tax accounts to investigate the
.. i18n: detailed entries that make up the full amount. This helps you search for errors such as when you've
.. i18n: entered an invoice at full tax rate when it should have been zero-rated for an inter-community trade or for
.. i18n: a charity.

Furthermore, for your tax declaration you can click on one of the tax accounts to investigate the
detailed entries that make up the full amount. This helps you search for errors such as when you've
entered an invoice at full tax rate when it should have been zero-rated for an inter-community trade or for
a charity.

.. i18n: In some countries, tax can be calculated on the basis of payments received rather than invoices
.. i18n: sent. In this instance choose :guilabel:`Base on` \ ``Payments``\   instead of :guilabel:`Base on` \
.. i18n: ``Invoices``\   in the :guilabel:`Select period` field. Even if you make your declaration on the
.. i18n: basis of invoices sent and received it can be helpful to compare the two reports to see the
.. i18n: amount of tax that you pay but haven't yet received from your customers.

In some countries, tax can be calculated on the basis of payments received rather than invoices
sent. In this instance choose :guilabel:`Base on` \ ``Payments``\   instead of :guilabel:`Base on` \
``Invoices``\   in the :guilabel:`Select period` field. Even if you make your declaration on the
basis of invoices sent and received it can be helpful to compare the two reports to see the
amount of tax that you pay but haven't yet received from your customers.

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
