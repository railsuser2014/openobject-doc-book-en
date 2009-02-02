
.. module:: subscription
    :synopsis: Subscription and recurring operations
    :noindex:
.. 

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

Subscription and recurring operations (*subscription*)
======================================================
:Module: subscription
:Name: Subscription and recurring operations
:Version: 5.0.1.0
:Directory: subscription
:Web: 
:Is certified: yes

Description
-----------

::

  Module allows to create new documents and add subscription on that document.

Dependencies
------------

 * :mod:`base`

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

Object: Subscription document (subscription.document)
#####################################################



:active: Active, boolean





:model: Object, many2one, required





:name: Name, char, required





:field_ids: Fields, one2many




Object: Subscription document fields (subscription.document.fields)
###################################################################



:field: Field, many2one, required





:document_id: Subscription Document, many2one





:value: Default Value, selection




Object: Subscription (subscription.subscription)
################################################



:cron_id: Cron Job, many2one





:user_id: User, many2one, required





:name: Name, char, required





:date_init: First Date, datetime





:notes: Notes, text





:interval_type: Interval Unit, selection





:exec_init: Number of documents, integer





:state: Status, selection





:doc_lines: Documents created, one2many, readonly





:doc_source: Source Document, reference, required





:interval_number: Interval Qty, integer





:partner_id: Partner, many2one





:active: Active, boolean




Object: Subscription history (subscription.subscription.history)
################################################################



:date: Date, datetime





:subscription_id: Subscription, many2one





:document_id: Source Document, reference, required


