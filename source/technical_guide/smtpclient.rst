
Module Email Client (*smtpclient*)
==================================
:Module: smtpclient
:Name: Email Client
:Version: 5.0.1.0
:Directory: smtpclient
:Web: http://tinyerp.com

Description
-----------

::

  Email Client module that provides:
      Sending Email
      Use Multiple Server
      Multi Threading
      Multi Attachment

Dependencies
------------

 * base - installed

Reports
-------

None


Menus
-------

 * Administration/Configuration
 * Administration/Configuration/Servers
 * Administration/Configuration/Servers/SMTP Server

Views
-----

 * report.smtp.server.graph (graph)
 * report.smtp.server.tree (tree)
 * report.smtp.server.form (form)
 * \* INHERIT smtp.company.form (form)
 * email.smtpclient.form (form)
 * email.smtpclient.form (tree)
 * email.smtpclient.history.tree (tree)
 * email.smtpclient.history.form (form)


Objects
-------

Object: Email Client
####################

.. index::
  single: Email Client object
.. 


:body: Message, text

    *The message text that will be send along with the email which is send through this server*

.. index::
  single: body field
.. 




:history_line: History, one2many



.. index::
  single: history_line field
.. 




:code: Verification Code, char



.. index::
  single: code field
.. 




:from: Email From, char, required, readonly



.. index::
  single: from field
.. 




:name: Server Name, char, required



.. index::
  single: name field
.. 




:test_email: Test Message, text



.. index::
  single: test_email field
.. 




:server: SMTP Server, char, required, readonly



.. index::
  single: server field
.. 




:date_create: Date Create, date, required, readonly



.. index::
  single: date_create field
.. 




:ssl: Use SSL?, boolean, readonly



.. index::
  single: ssl field
.. 




:state: Server Status, selection, readonly



.. index::
  single: state field
.. 




:email: Email Address, char, required, readonly



.. index::
  single: email field
.. 




:server_statistics: Statistics, one2many



.. index::
  single: server_statistics field
.. 




:user: User Name, char, required, readonly



.. index::
  single: user field
.. 




:active: Active, boolean



.. index::
  single: active field
.. 




:verify_email: Verify Message, text, readonly



.. index::
  single: verify_email field
.. 




:password: Password, char, required, readonly



.. index::
  single: password field
.. 




:type: Server Type, selection, required



.. index::
  single: type field
.. 




:port: SMTP Port, char, required, readonly



.. index::
  single: port field
.. 




:users_id: Users Allowed, many2many



.. index::
  single: users_id field
.. 



Object: Email Client History
############################

.. index::
  single: Email Client History object
.. 


:server_id: Smtp Server, many2one, required



.. index::
  single: server_id field
.. 




:user_id: Username, many2one, readonly



.. index::
  single: user_id field
.. 




:name: Description, text, required, readonly



.. index::
  single: name field
.. 




:resource_id: Resource ID, integer, readonly



.. index::
  single: resource_id field
.. 




:date_create: Date, datetime, readonly



.. index::
  single: date_create field
.. 




:model: Model, many2one, readonly



.. index::
  single: model field
.. 




:email: Email, char, readonly



.. index::
  single: email field
.. 



Object: Server Statistics
#########################

.. index::
  single: Server Statistics object
.. 


:model: Model, char, readonly



.. index::
  single: model field
.. 




:no: Total No., integer, readonly



.. index::
  single: no field
.. 




:server_id: Server ID, many2one, readonly



.. index::
  single: server_id field
.. 




:name: Server, char, readonly



.. index::
  single: name field
.. 




:history: History, char, readonly



.. index::
  single: history field
.. 



Object: res.company.address
###########################

.. index::
  single: res.company.address object
.. 


:email: Email Address, many2one, required



.. index::
  single: email field
.. 




:name: Address Type, selection, required



.. index::
  single: name field
.. 




:company_id: Company, many2one, required



.. index::
  single: company_id field
.. 

