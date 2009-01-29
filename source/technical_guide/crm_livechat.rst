
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



:name: Jabber Account, char, required





:server: Server, char, required





:ssl: SSL Info, selection





:login: Account Login, char, required





:password: Account Password, char, required





:port: Port Number, char




Object: LiveChat Account
########################



:max_per_user: Maximum Customer per User, integer





:session_delay: Minutes to Close a session, integer

    *Put here to number of minutes after which a session is considered as closed*



:state: State, selection





:user_ids: Users Accounts, one2many





:name: Livechat Account, char, required




Object: LiveChat Visitors
#########################



:available: Available IP, char

    *If empty, the acount is available/not used*



:state: State, selection, required





:jabber_id: Jabber Account, many2one, required





:name: Account Name, char, required





:available_date: Available Date, datetime




Object: LiveChat Users
######################



:jabber_id: Jabber Account, many2one, required





:user_id: User, many2one, required





:name: User Name, char, required





:livechat_id: Livechat, many2one, required





:languages: Language Regex, char





:state: State, selection, required




Object: LiveChat Log
####################



:note: History, text





:user_id: User, many2one





:name: Date and Time, datetime, required





:livechat_id: Livechat, many2one, required


