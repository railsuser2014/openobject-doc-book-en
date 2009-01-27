
Module Managing sales and deliveries by journal (*purchase_journal*)
====================================================================
:Module: purchase_journal
:Name: Managing sales and deliveries by journal
:Version: 5.0.1.0
:Directory: purchase_journal
:Web: http://www.tinyerp.com

Description
-----------

::

  None

Dependencies
------------

 * stock - installed
 * purchase - installed

Reports
-------

None


Menus
-------

 * Purchase Management/Configuration
 * Purchase Management/Configuration/Purchases Journals
 * Purchase Management/Purchases by Journal
 * Purchase Management/Purchases by Journal/My Open Journals
 * Purchase Management/Purchases by Journal/All Open Journals
 * Purchase Management/Reporting
 * Purchase Management/Reporting/This Month
 * Purchase Management/Reporting/This Month/Purchases by Journal
 * Purchase Management/Reporting/All Months
 * Purchase Management/Reporting/All Months/Purchases by Journal

Views
-----

 * \* INHERIT stock.picking.journal.view.form (form)
 * \* INHERIT stock.picking.purchase.journal.view.tree (tree)
 * purchase_journal.purchase.journal.form (form)
 * purchase_journal.purchase.journal.tree (tree)
 * \* INHERIT purchase.order.journal.view.form (form)
 * \* INHERIT purchase.order.journal.view.tree (tree)
 * purchase_journal.purchase.stats.tree (tree)
 * purchase_journal.purchase.stats.form (form)


Objects
-------

Object: purchase Journal
########################

.. index::
  single: purchase Journal object
.. 


:code: Code, char, required



.. index::
  single: code field
.. 




:user_id: Responsible, many2one, required



.. index::
  single: user_id field
.. 




:name: Journal, char, required



.. index::
  single: name field
.. 




:note: Note, text



.. index::
  single: note field
.. 




:state: Creation date, selection, required



.. index::
  single: state field
.. 




:purchase_stats_ids: purchase Stats, one2many, readonly



.. index::
  single: purchase_stats_ids field
.. 




:date: Journal date, date, required



.. index::
  single: date field
.. 




:date_created: Creation date, date, required, readonly



.. index::
  single: date_created field
.. 




:date_validation: Validation date, date, readonly



.. index::
  single: date_validation field
.. 



Object: Purchases Orders by Journal
###################################

.. index::
  single: Purchases Orders by Journal object
.. 


:count: # of Lines, integer, readonly



.. index::
  single: count field
.. 




:price_total: Total Price, float, readonly



.. index::
  single: price_total field
.. 




:name: Month, date, readonly



.. index::
  single: name field
.. 




:state: Order State, selection, readonly



.. index::
  single: state field
.. 




:journal_id: Journal, many2one, readonly



.. index::
  single: journal_id field
.. 




:price_average: Average Price, float, readonly



.. index::
  single: price_average field
.. 




:quantity: Quantities, float, readonly



.. index::
  single: quantity field
.. 

