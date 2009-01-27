
Module Purchase - Purchase Tender (*purchase_tender*)
=====================================================
:Module: purchase_tender
:Name: Purchase - Purchase Tender
:Version: 5.0.0.1
:Directory: purchase_tender
:Web: http://tinyerp.com/

Description
-----------

::

  This module allows you to manage your Purchase Tenders. When a purchase order is created, you now have the opportunity to save the related tender. 
      This new object will regroup and will allow you to easily keep track and order all your purchase orders.

Dependencies
------------

 * purchase - installed

Reports
-------

None


Menus
-------

 * Purchase Management/Purchase Tenders
 * Purchase Management/Purchase Tenders/Purchase Tenders
 * Purchase Management/Purchase Tenders/Purchase Tenders/Draft Purchase Tenders
 * Purchase Management/Purchase Tenders/Purchase Tenders/Open Purchase Tenders
 * Purchase Management/Purchase Tenders/New Purchase Tenders

Views
-----

 * \* INHERIT purchase.order.tree.inherit (tree)
 * \* INHERIT purchase.order.form.inherit (form)
 * purchase.tender.form (form)
 * purchase.tender.tree (tree)


Objects
-------

Object: Purchase Tender
#######################

.. index::
  single: Purchase Tender object
.. 


:user_id: Responsible, many2one



.. index::
  single: user_id field
.. 




:name: Tender Reference, char, required



.. index::
  single: name field
.. 




:date_end: Date End, datetime



.. index::
  single: date_end field
.. 




:date_start: Date Start, datetime



.. index::
  single: date_start field
.. 




:state: State, selection, required



.. index::
  single: state field
.. 




:purchase_ids: Purchase Orders, one2many



.. index::
  single: purchase_ids field
.. 




:description: Description, text



.. index::
  single: description field
.. 

