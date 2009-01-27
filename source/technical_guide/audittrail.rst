
Module Audit Trail (*audittrail*)
=================================
:Module: audittrail
:Name: Audit Trail
:Version: 5.0.1.0
:Directory: audittrail
:Web: http://www.openerp.com

Description
-----------

::

  Allows the administrator to track every user operations on all objects of the system.
      Subscribe Rules for read, write, create and delete on objects and check logs

Dependencies
------------

 * base - installed
 * account - installed
 * purchase - installed
 * mrp - installed

Reports
-------

None


Menus
-------

 * Administration/Audittrails
 * Administration/Audittrails/Rules
 * Administration/Audittrails/Rules/Subscribed Rules
 * Administration/Audittrails/Logs
 * Administration/Audittrails/View Logs

Views
-----

 * audittrail.rule.form (form)
 * audittrail.rule.tree (tree)
 * audittrail.log.form (form)
 * audittrail.log.tree (tree)


Objects
-------

Object: audittrail.rule
#######################

.. index::
  single: audittrail.rule object
.. 


:log_read: Log reads, boolean



.. index::
  single: log_read field
.. 




:log_unlink: Log deletes, boolean



.. index::
  single: log_unlink field
.. 




:user_id: Users, many2many



.. index::
  single: user_id field
.. 




:name: Rule Name, char, required



.. index::
  single: name field
.. 




:log_write: Log writes, boolean



.. index::
  single: log_write field
.. 




:object_id: Object, many2one, required



.. index::
  single: object_id field
.. 




:log_create: Log creates, boolean



.. index::
  single: log_create field
.. 




:state: State, selection, required



.. index::
  single: state field
.. 




:action_id: Action ID, many2one



.. index::
  single: action_id field
.. 



Object: audittrail.log
######################

.. index::
  single: audittrail.log object
.. 


:user_id: User, many2one



.. index::
  single: user_id field
.. 




:name: Name, char



.. index::
  single: name field
.. 




:timestamp: Date, datetime



.. index::
  single: timestamp field
.. 




:object_id: Object, many2one



.. index::
  single: object_id field
.. 




:line_ids: Log lines, one2many



.. index::
  single: line_ids field
.. 




:res_id: Resource Id, integer



.. index::
  single: res_id field
.. 




:method: Method, selection



.. index::
  single: method field
.. 



Object: audittrail.log.line
###########################

.. index::
  single: audittrail.log.line object
.. 


:log: Log ID, integer



.. index::
  single: log field
.. 




:log_id: Log, many2one



.. index::
  single: log_id field
.. 




:old_value: Old Value, text



.. index::
  single: old_value field
.. 




:field_id: Fields, many2one, required



.. index::
  single: field_id field
.. 




:old_value_text: Old value Text, text



.. index::
  single: old_value_text field
.. 




:field_description: Field Description, char



.. index::
  single: field_description field
.. 




:new_value: New Value, text



.. index::
  single: new_value field
.. 




:new_value_text: New value Text, text



.. index::
  single: new_value_text field
.. 

