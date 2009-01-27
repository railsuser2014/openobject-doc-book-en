
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

.. index::
  single: Credit line object
.. 


:from_date: From Date, date, required



.. index::
  single: from_date field
.. 




:customer_credit: Customer Max Credit, float, required



.. index::
  single: customer_credit field
.. 




:to_date: To Date, date, required



.. index::
  single: to_date field
.. 




:name: Name, char, required



.. index::
  single: name field
.. 




:global_credit: Global Credit, float, required



.. index::
  single: global_credit field
.. 



Object: Translation Folder
##########################

.. index::
  single: Translation Folder object
.. 


:awex_amount: AWEX Amount, float, readonly



.. index::
  single: awex_amount field
.. 




:credit_line_id: Credit Line, many2one, readonly



.. index::
  single: credit_line_id field
.. 




:name: Name, text, required



.. index::
  single: name field
.. 




:invoice_id: Invoice, many2one



.. index::
  single: invoice_id field
.. 




:order_desc: Description, char, required



.. index::
  single: order_desc field
.. 




:base_amount: Base Amount, float, required, readonly



.. index::
  single: base_amount field
.. 




:purchase_order: Purchase Order, many2one



.. index::
  single: purchase_order field
.. 




:awex_eligible: AWEX Eligible, boolean, readonly



.. index::
  single: awex_eligible field
.. 




:state: State, selection, readonly



.. index::
  single: state field
.. 




:order_date: Order Date, date, required



.. index::
  single: order_date field
.. 




:partner_id: Partner, many2one, required



.. index::
  single: partner_id field
.. 



Object: Letter of Credence
##########################

.. index::
  single: Letter of Credence object
.. 


:emission_date: Emission Date, date, required



.. index::
  single: emission_date field
.. 




:asked_amount: Asked Amount, float, required



.. index::
  single: asked_amount field
.. 

