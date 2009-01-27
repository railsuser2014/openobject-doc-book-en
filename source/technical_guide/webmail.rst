
Module Webmail (*webmail*)
==========================
:Module: webmail
:Name: Webmail
:Version: 5.0.1.0
:Directory: webmail
:Web: http://tinyerp.com

Description
-----------

::

  Webmail module covers:
          - Mail server configuration.
          - Sending and Receiving mail

Dependencies
------------

 * base - installed

Reports
-------

None


Menus
-------

 * Webmail
 * Webmail/Configuration
 * Webmail/Configuration/Server
 * Webmail/Compose Mail

Views
-----

 * webmail.server.tree (tree)
 * webmail.server.form (form)
 * webmail.tiny.user.form (form)
 * webmail.mailbox.tree (tree)
 * webmail.email.compose.form (form)
 * webmail.email.read.form (form)


Objects
-------

Object: User Configuration
##########################

.. index::
  single: User Configuration object
.. 


:server_conf_id: Configuration, one2many



.. index::
  single: server_conf_id field
.. 




:user_id: User, many2one



.. index::
  single: user_id field
.. 



Object: Mail Server Configuration
#################################

.. index::
  single: Mail Server Configuration object
.. 


:iconn_port: Port, integer



.. index::
  single: iconn_port field
.. 




:server_id: Mail Client, many2one



.. index::
  single: server_id field
.. 




:iserver_type: Server Type, selection



.. index::
  single: iserver_type field
.. 




:name: Name, char, required



.. index::
  single: name field
.. 




:oconn_type: SSL, boolean



.. index::
  single: oconn_type field
.. 




:oconn_port: Port, integer



.. index::
  single: oconn_port field
.. 




:iserver_name: Server Name, char, required



.. index::
  single: iserver_name field
.. 




:oserver_name: Server Name, char, required



.. index::
  single: oserver_name field
.. 




:iconn_type: SSL, boolean



.. index::
  single: iconn_type field
.. 




:password: Password, char, required



.. index::
  single: password field
.. 




:user_name: User Name, char, required



.. index::
  single: user_name field
.. 



Object: User Mailbox
####################

.. index::
  single: User Mailbox object
.. 


:parent_id: Parent Folder, many2one



.. index::
  single: parent_id field
.. 




:child_id: Child Folder, one2many



.. index::
  single: child_id field
.. 




:user_id: User, many2one



.. index::
  single: user_id field
.. 




:name: Name, char, required



.. index::
  single: name field
.. 




:account_id: Server, many2one



.. index::
  single: account_id field
.. 



Object: Email Tag
#################

.. index::
  single: Email Tag object
.. 


:user_id: User, many2one



.. index::
  single: user_id field
.. 




:name: Tag Name, char



.. index::
  single: name field
.. 




:account_id: Server, many2one



.. index::
  single: account_id field
.. 



Object: User Email
##################

.. index::
  single: User Email object
.. 


:body: Body, text



.. index::
  single: body field
.. 




:user_id: User, many2one



.. index::
  single: user_id field
.. 




:account_id: Server, many2one



.. index::
  single: account_id field
.. 




:cc: Cc, char



.. index::
  single: cc field
.. 




:tag_id: Tags, many2one



.. index::
  single: tag_id field
.. 




:bcc: Bcc, char



.. index::
  single: bcc field
.. 




:to: To, char



.. index::
  single: to field
.. 




:folder_id: Folder, many2one



.. index::
  single: folder_id field
.. 




:from_user: From, char



.. index::
  single: from_user field
.. 




:date: Date, datetime



.. index::
  single: date field
.. 




:active: Active, boolean



.. index::
  single: active field
.. 




:message_id: Message Id, char



.. index::
  single: message_id field
.. 




:subject: Subject, char



.. index::
  single: subject field
.. 

