
Module CRM - Livechat Jabber Client (*crm_livechat*)
====================================================
:Module: crm_livechat
:Name: CRM - Livechat Jabber Client
:Version: 5.0.1.3
:Directory: crm_livechat
:Web: http://tinyerp.com/

Description
-----------

::

  This module allows you to configure and manage a livechat on your website.
  So that your salesman can directly talk with your users in your website, using
  their normal jabber account. This project includes two parts:
  * An OpenERP module to manage everything
  * A python Ajax client to set on your website for the end-user interface.
  
  It allows you to define:
  * XMPP (Jabber) Accounts for your users
  * XMPP Accounts for anonymous customers
  
  Then based one some events (a customer visiting some pages), it can open a
  window so that the visitor can directly talk with your teams. It goes to a
  jabber user according to what you configured in the OpenERP interface.

Dependencies
------------

 * base - installed

Reports
-------

None


Menus
-------

 * CRM & SRM/Live Chat
 * CRM & SRM/Live Chat/Configuration
 * CRM & SRM/Live Chat/Configuration/Jabber Accounts
 * CRM & SRM/Live Chat/Configuration/Live Chat Sessions
 * CRM & SRM/Live Chat/Configuration/Visitors Accounts
 * CRM & SRM/Live Chat/Configuration/Users Accounts
 * CRM & SRM/Live Chat/Live Chat Logs

Views
-----

 * Jabber Account Form (form)
 * Jabber Account Tree (tree)
 * LiveChat Sessions (form)
 * Live Chat Tree (tree)
 * partners Accounts (form)
 * partners Accounts (tree)
 * Users Accounts (form)
 * Users Accounts (tree)
 * log Accounts (form)
 * Livechat Logs (tree)


Objects
-------

Object: Livechat Account
########################

.. index::
  single: Livechat Account object
.. 


:name: Jabber Account, char, required



.. index::
  single: name field
.. 




:server: Server, char, required



.. index::
  single: server field
.. 




:ssl: SSL Info, selection



.. index::
  single: ssl field
.. 




:login: Account Login, char, required



.. index::
  single: login field
.. 




:password: Account Password, char, required



.. index::
  single: password field
.. 




:port: Port Number, char



.. index::
  single: port field
.. 



Object: LiveChat Account
########################

.. index::
  single: LiveChat Account object
.. 


:max_per_user: Maximum Customer per User, integer



.. index::
  single: max_per_user field
.. 




:session_delay: Minutes to Close a session, integer

    *Put here to number of minutes after which a session is considered as closed*

.. index::
  single: session_delay field
.. 




:state: State, selection



.. index::
  single: state field
.. 




:user_ids: Users Accounts, one2many



.. index::
  single: user_ids field
.. 




:name: Livechat Account, char, required



.. index::
  single: name field
.. 



Object: LiveChat Visitors
#########################

.. index::
  single: LiveChat Visitors object
.. 


:available: Available IP, char

    *If empty, the acount is available/not used*

.. index::
  single: available field
.. 




:state: State, selection, required



.. index::
  single: state field
.. 




:jabber_id: Jabber Account, many2one, required



.. index::
  single: jabber_id field
.. 




:name: Account Name, char, required



.. index::
  single: name field
.. 




:available_date: Available Date, datetime



.. index::
  single: available_date field
.. 



Object: LiveChat Users
######################

.. index::
  single: LiveChat Users object
.. 


:jabber_id: Jabber Account, many2one, required



.. index::
  single: jabber_id field
.. 




:user_id: User, many2one, required



.. index::
  single: user_id field
.. 




:name: User Name, char, required



.. index::
  single: name field
.. 




:livechat_id: Livechat, many2one, required



.. index::
  single: livechat_id field
.. 




:languages: Language Regex, char



.. index::
  single: languages field
.. 




:state: State, selection, required



.. index::
  single: state field
.. 



Object: LiveChat Log
####################

.. index::
  single: LiveChat Log object
.. 


:note: History, text



.. index::
  single: note field
.. 




:user_id: User, many2one



.. index::
  single: user_id field
.. 




:name: Date and Time, datetime, required



.. index::
  single: name field
.. 




:livechat_id: Livechat, many2one, required



.. index::
  single: livechat_id field
.. 

