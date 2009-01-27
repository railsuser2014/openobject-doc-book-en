
Module Sales: Avertising Sales (*sale_advertising*)
===================================================
:Module: sale_advertising
:Name: Sales: Avertising Sales
:Version: 5.0.0.1
:Directory: sale_advertising
:Web: http://tinyerp.com/

Description
-----------

::

  This module allow you to use the Sale Management to encode your advertising sales ... TODO

Dependencies
------------

 * sale - installed

Reports
-------

None


Menus
-------

 * Sales Management/Advertising
 * Sales Management/Advertising/Advertising Issue
 * Sales Management/Advertising/Advertising Proof
 * Sales Management/Advertising/All Advertising Sale Orders

Views
-----

 * \* INHERIT sale.order.form.inherit (form)
 * \* INHERIT sale.order.form.inherit.line (form)
 * \* INHERIT sale.order.line.form.inherit.line2 (form)
 * sale.advertising.issue.form (form)
 * sale.advertising.issue.tree (tree)
 * sale.advertising.proof.form (form)
 * sale.advertising.proof.tree (tree)
 * \* INHERIT product.product.form.inherit (form)


Objects
-------

Object: Sale Advertising Issue
##############################

.. index::
  single: Sale Advertising Issue object
.. 


:issue_date: Issue Date, date, required



.. index::
  single: issue_date field
.. 




:medium: Medium, many2one, required



.. index::
  single: medium field
.. 




:name: Name, char, required



.. index::
  single: name field
.. 




:default_note: Default Note, text



.. index::
  single: default_note field
.. 




:state: State, selection



.. index::
  single: state field
.. 



Object: Sale Advertising Proof
##############################

.. index::
  single: Sale Advertising Proof object
.. 


:address_id: Delivery Address, many2one, required



.. index::
  single: address_id field
.. 




:target_id: Target, many2one, required



.. index::
  single: target_id field
.. 




:name: Name, char, required



.. index::
  single: name field
.. 




:number: Number of Copies, integer, required



.. index::
  single: number field
.. 

