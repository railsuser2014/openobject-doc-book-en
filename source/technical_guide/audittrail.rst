
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



:log_read: Log reads, boolean





:log_unlink: Log deletes, boolean





:user_id: Users, many2many





:name: Rule Name, char, required





:log_write: Log writes, boolean





:object_id: Object, many2one, required





:log_create: Log creates, boolean





:state: State, selection, required





:action_id: Action ID, many2one




Object: audittrail.log
######################



:user_id: User, many2one





:name: Name, char





:timestamp: Date, datetime





:object_id: Object, many2one





:line_ids: Log lines, one2many





:res_id: Resource Id, integer





:method: Method, selection




Object: audittrail.log.line
###########################



:log: Log ID, integer





:log_id: Log, many2one





:old_value: Old Value, text





:field_id: Fields, many2one, required





:old_value_text: Old value Text, text





:field_description: Field Description, char





:new_value: New Value, text





:new_value_text: New value Text, text


