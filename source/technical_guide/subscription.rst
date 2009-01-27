
Module Subscription and recurring operations (*subscription*)
=============================================================
:Module: subscription
:Name: Subscription and recurring operations
:Version: 5.0.1.0
:Directory: subscription
:Web: 

Description
-----------

::

  Module allows to create new documents and add subscription on that document.

Dependencies
------------

 * base - installed

Reports
-------

None


Menus
-------

 * Tools
 * Tools/Subscriptions
 * Tools/Subscriptions/Configuration
 * Tools/Subscriptions/All Subscriptions
 * Tools/Subscriptions/Configuration/Document Types

Views
-----

 * subscription.subscription.form (form)
 * subscription.subscription.tree (tree)
 * subscription.subscription.history.tree (tree)
 * subscription.subscription.history.form (form)
 * subscription.document.form (form)
 * subscription.document.tree (tree)
 * subscription.document.fields.form (form)
 * subscription.document.fields.tree (tree)


Objects
-------

Object: Subscription document
#############################

.. index::
  single: Subscription document object
.. 


:active: Active, boolean



.. index::
  single: active field
.. 




:model: Object, many2one, required



.. index::
  single: model field
.. 




:name: Name, char, required



.. index::
  single: name field
.. 




:field_ids: Fields, one2many



.. index::
  single: field_ids field
.. 



Object: Subscription document fields
####################################

.. index::
  single: Subscription document fields object
.. 


:field: Field, many2one, required



.. index::
  single: field field
.. 




:document_id: Subscription Document, many2one



.. index::
  single: document_id field
.. 




:value: Default Value, selection



.. index::
  single: value field
.. 



Object: Subscription
####################

.. index::
  single: Subscription object
.. 


:cron_id: Cron Job, many2one



.. index::
  single: cron_id field
.. 




:user_id: User, many2one, required



.. index::
  single: user_id field
.. 




:name: Name, char, required



.. index::
  single: name field
.. 




:date_init: First Date, datetime



.. index::
  single: date_init field
.. 




:notes: Notes, text



.. index::
  single: notes field
.. 




:interval_type: Interval Unit, selection



.. index::
  single: interval_type field
.. 




:exec_init: Number of documents, integer



.. index::
  single: exec_init field
.. 




:state: Status, selection



.. index::
  single: state field
.. 




:doc_lines: Documents created, one2many, readonly



.. index::
  single: doc_lines field
.. 




:doc_source: Source Document, reference, required



.. index::
  single: doc_source field
.. 




:interval_number: Interval Qty, integer



.. index::
  single: interval_number field
.. 




:partner_id: Partner, many2one



.. index::
  single: partner_id field
.. 




:active: Active, boolean



.. index::
  single: active field
.. 



Object: Subscription history
############################

.. index::
  single: Subscription history object
.. 


:date: Date, datetime



.. index::
  single: date field
.. 




:subscription_id: Subscription, many2one



.. index::
  single: subscription_id field
.. 




:document_id: Source Document, reference, required



.. index::
  single: document_id field
.. 

