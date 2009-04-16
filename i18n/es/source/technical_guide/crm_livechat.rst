
.. i18n: .. module:: crm_livechat
.. i18n:     :synopsis: CRM - Livechat Jabber Client 
.. i18n:     :noindex:
.. i18n: .. 

.. module:: crm_livechat
    :synopsis: CRM - Livechat Jabber Client 
    :noindex:
.. 

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. i18n: CRM - Livechat Jabber Client (*crm_livechat*)
.. i18n: =============================================
.. i18n: :Module: crm_livechat
.. i18n: :Name: CRM - Livechat Jabber Client
.. i18n: :Version: 5.0.1.3
.. i18n: :Author: Tiny
.. i18n: :Directory: crm_livechat
.. i18n: :Web: http://www.openerp.com//
.. i18n: :Official module: no
.. i18n: :Quality certified: no

CRM - Livechat Jabber Client (*crm_livechat*)
=============================================
:Module: crm_livechat
:Name: CRM - Livechat Jabber Client
:Version: 5.0.1.3
:Author: Tiny
:Directory: crm_livechat
:Web: http://www.openerp.com//
:Official module: no
:Quality certified: no

.. i18n: Description
.. i18n: -----------

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   This module allows you to configure and manage a livechat on your website.
.. i18n:   So that your salesman can directly talk with your users in your website, using their normal 
.. i18n:   jabber account. 
.. i18n:   This project includes two parts:
.. i18n:   * An OpenERP module to manage everything
.. i18n:   * A python Ajax client to set on your website for the end-user interface.
.. i18n:   
.. i18n:   It allows you to define:
.. i18n:   * XMPP (Jabber) Accounts for your users
.. i18n:   * XMPP Accounts for anonymous customers
.. i18n:   
.. i18n:   Then based one some events (a customer visiting some pages), it can open a
.. i18n:   window so that the visitor can directly talk with your teams. It goes to a
.. i18n:   jabber user according to what you configured in the OpenERP interface.

::

  This module allows you to configure and manage a livechat on your website.
  So that your salesman can directly talk with your users in your website, using their normal 
  jabber account. 
  This project includes two parts:
  * An OpenERP module to manage everything
  * A python Ajax client to set on your website for the end-user interface.
  
  It allows you to define:
  * XMPP (Jabber) Accounts for your users
  * XMPP Accounts for anonymous customers
  
  Then based one some events (a customer visiting some pages), it can open a
  window so that the visitor can directly talk with your teams. It goes to a
  jabber user according to what you configured in the OpenERP interface.

.. i18n: Dependencies
.. i18n: ------------

Dependencies
------------

.. i18n:  * :mod:`base`

 * :mod:`base`

.. i18n: Reports
.. i18n: -------

Reports
-------

.. i18n: None

None

.. i18n: Menus
.. i18n: -------

Menus
-------

.. i18n:  * CRM & SRM/Live Chat
.. i18n:  * CRM & SRM/Live Chat/Configuration
.. i18n:  * CRM & SRM/Live Chat/Configuration/Jabber Accounts
.. i18n:  * CRM & SRM/Live Chat/Configuration/Live Chat Sessions
.. i18n:  * CRM & SRM/Live Chat/Configuration/Visitors Accounts
.. i18n:  * CRM & SRM/Live Chat/Configuration/Users Accounts
.. i18n:  * CRM & SRM/Live Chat/Live Chat Logs

 * CRM & SRM/Live Chat
 * CRM & SRM/Live Chat/Configuration
 * CRM & SRM/Live Chat/Configuration/Jabber Accounts
 * CRM & SRM/Live Chat/Configuration/Live Chat Sessions
 * CRM & SRM/Live Chat/Configuration/Visitors Accounts
 * CRM & SRM/Live Chat/Configuration/Users Accounts
 * CRM & SRM/Live Chat/Live Chat Logs

.. i18n: Views
.. i18n: -----

Views
-----

.. i18n:  * Jabber Account Form (form)
.. i18n:  * Jabber Account Tree (tree)
.. i18n:  * LiveChat Sessions (form)
.. i18n:  * Live Chat Tree (tree)
.. i18n:  * partners Accounts (form)
.. i18n:  * partners Accounts (tree)
.. i18n:  * Users Accounts (form)
.. i18n:  * Users Accounts (tree)
.. i18n:  * log Accounts (form)
.. i18n:  * Livechat Logs (tree)

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

.. i18n: Objects
.. i18n: -------

Objects
-------

.. i18n: Object: Livechat Account (crm_livechat.jabber)
.. i18n: ##############################################

Object: Livechat Account (crm_livechat.jabber)
##############################################

.. i18n: :name: Jabber Account, char, required

:name: Jabber Account, char, required

.. i18n: :server: Server, char, required

:server: Server, char, required

.. i18n: :ssl: SSL Info, selection

:ssl: SSL Info, selection

.. i18n: :login: Account Login, char, required

:login: Account Login, char, required

.. i18n: :password: Account Password, char, required

:password: Account Password, char, required

.. i18n: :port: Port Number, char

:port: Port Number, char

.. i18n: Object: LiveChat Account (crm_livechat.livechat)
.. i18n: ################################################

Object: LiveChat Account (crm_livechat.livechat)
################################################

.. i18n: :max_per_user: Maximum Customer per User, integer

:max_per_user: Maximum Customer per User, integer

.. i18n: :session_delay: Minutes to Close a session, integer

:session_delay: Minutes to Close a session, integer

.. i18n:     *Put here to number of minutes after which a session is considered as closed*

    *Put here to number of minutes after which a session is considered as closed*

.. i18n: :state: State, selection

:state: State, selection

.. i18n: :user_ids: Users Accounts, one2many

:user_ids: Users Accounts, one2many

.. i18n: :name: Livechat Account, char, required

:name: Livechat Account, char, required

.. i18n: Object: LiveChat Visitors (crm_livechat.livechat.partner)
.. i18n: #########################################################

Object: LiveChat Visitors (crm_livechat.livechat.partner)
#########################################################

.. i18n: :available: Available IP, char

:available: Available IP, char

.. i18n:     *If empty, the acount is available/not used*

    *If empty, the acount is available/not used*

.. i18n: :state: State, selection, required

:state: State, selection, required

.. i18n: :jabber_id: Jabber Account, many2one, required

:jabber_id: Jabber Account, many2one, required

.. i18n: :name: Account Name, char, required

:name: Account Name, char, required

.. i18n: :available_date: Available Date, datetime

:available_date: Available Date, datetime

.. i18n: Object: LiveChat Users (crm_livechat.livechat.user)
.. i18n: ###################################################

Object: LiveChat Users (crm_livechat.livechat.user)
###################################################

.. i18n: :jabber_id: Jabber Account, many2one, required

:jabber_id: Jabber Account, many2one, required

.. i18n: :user_id: User, many2one, required

:user_id: User, many2one, required

.. i18n: :name: User Name, char, required

:name: User Name, char, required

.. i18n: :livechat_id: Livechat, many2one, required

:livechat_id: Livechat, many2one, required

.. i18n: :languages: Language Regex, char

:languages: Language Regex, char

.. i18n: :state: State, selection, required

:state: State, selection, required

.. i18n: Object: LiveChat Log (crm_livechat.log)
.. i18n: #######################################

Object: LiveChat Log (crm_livechat.log)
#######################################

.. i18n: :note: History, text

:note: History, text

.. i18n: :user_id: User, many2one

:user_id: User, many2one

.. i18n: :name: Date and Time, datetime, required

:name: Date and Time, datetime, required

.. i18n: :livechat_id: Livechat, many2one, required

:livechat_id: Livechat, many2one, required
