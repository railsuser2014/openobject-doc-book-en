
Module CCI Translation (*cci_translation*)
==========================================
:Module: cci_translation
:Name: CCI Translation
:Version: 5.0.1.0
:Directory: cci_translation
:Web: http://www.openerp.com

Description
-----------

::

  cci translation

Dependencies
------------

 * base - installed
 * cci_account - installed

Reports
-------

None


Menus
-------

 * Translation
 * Translation/Translation Dossier
 * Translation/Credit Line
 * Translation/Letter of Credence

Views
-----

 * translation.folder.form (form)
 * translation.folder.tree (tree)
 * credit.line.form (form)
 * credit.line.tree (tree)
 * letter.credence.form (form)
 * letter.credence.tree (tree)
 * \* INHERIT res.partner.form.translation (form)


Objects
-------

Object: Credit line
###################



:from_date: From Date, date, required





:customer_credit: Customer Max Credit, float, required





:to_date: To Date, date, required





:name: Name, char, required





:global_credit: Global Credit, float, required




Object: Translation Folder
##########################



:awex_amount: AWEX Amount, float, readonly





:credit_line_id: Credit Line, many2one, readonly





:name: Name, text, required





:invoice_id: Invoice, many2one





:order_desc: Description, char, required





:base_amount: Base Amount, float, required, readonly





:purchase_order: Purchase Order, many2one





:awex_eligible: AWEX Eligible, boolean, readonly





:state: State, selection, readonly





:order_date: Order Date, date, required





:partner_id: Partner, many2one, required




Object: Letter of Credence
##########################



:emission_date: Emission Date, date, required





:asked_amount: Asked Amount, float, required


