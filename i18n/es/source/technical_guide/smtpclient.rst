
.. i18n: .. module:: smtpclient
.. i18n:     :synopsis: Email Client 
.. i18n:     :noindex:
.. i18n: .. 

.. module:: smtpclient
    :synopsis: Email Client 
    :noindex:
.. 

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. i18n: Email Client (*smtpclient*)
.. i18n: ===========================
.. i18n: :Module: smtpclient
.. i18n: :Name: Email Client
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: smtpclient
.. i18n: :Web: http://www.openerp.com/
.. i18n: :Official module: no
.. i18n: :Quality certified: no

Email Client (*smtpclient*)
===========================
:Module: smtpclient
:Name: Email Client
:Version: 5.0.1.0
:Author: Tiny
:Directory: smtpclient
:Web: http://www.openerp.com/
:Official module: no
:Quality certified: no

.. i18n: Description
.. i18n: -----------

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   Email Client module that provides:
.. i18n:       Sending Email
.. i18n:       Use Multiple Server
.. i18n:       Multi Threading
.. i18n:       Multi Attachment

::

  Email Client module that provides:
      Sending Email
      Use Multiple Server
      Multi Threading
      Multi Attachment

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

.. i18n:  * Administration/Configuration
.. i18n:  * Administration/Configuration/Servers
.. i18n:  * Administration/Configuration/Servers/SMTP Server

 * Administration/Configuration
 * Administration/Configuration/Servers
 * Administration/Configuration/Servers/SMTP Server

.. i18n: Views
.. i18n: -----

Views
-----

.. i18n:  * report.smtp.server.graph (graph)
.. i18n:  * report.smtp.server.tree (tree)
.. i18n:  * report.smtp.server.form (form)
.. i18n:  * \* INHERIT smtp.company.form (form)
.. i18n:  * email.smtpclient.form (form)
.. i18n:  * email.smtpclient.form (tree)
.. i18n:  * email.smtpclient.history.tree (tree)
.. i18n:  * email.smtpclient.history.form (form)

 * report.smtp.server.graph (graph)
 * report.smtp.server.tree (tree)
 * report.smtp.server.form (form)
 * \* INHERIT smtp.company.form (form)
 * email.smtpclient.form (form)
 * email.smtpclient.form (tree)
 * email.smtpclient.history.tree (tree)
 * email.smtpclient.history.form (form)

.. i18n: Objects
.. i18n: -------

Objects
-------

.. i18n: Object: Email Client (email.smtpclient)
.. i18n: #######################################

Object: Email Client (email.smtpclient)
#######################################

.. i18n: :body: Message, text

:body: Message, text

.. i18n:     *The message text that will be send along with the email which is send through this server*

    *The message text that will be send along with the email which is send through this server*

.. i18n: :history_line: History, one2many

:history_line: History, one2many

.. i18n: :code: Verification Code, char

:code: Verification Code, char

.. i18n: :from: Email From, char, required, readonly

:from: Email From, char, required, readonly

.. i18n: :name: Server Name, char, required

:name: Server Name, char, required

.. i18n: :test_email: Test Message, text

:test_email: Test Message, text

.. i18n: :server: SMTP Server, char, required, readonly

:server: SMTP Server, char, required, readonly

.. i18n: :date_create: Date Create, date, required, readonly

:date_create: Date Create, date, required, readonly

.. i18n: :ssl: Use SSL?, boolean, readonly

:ssl: Use SSL?, boolean, readonly

.. i18n: :state: Server Status, selection, readonly

:state: Server Status, selection, readonly

.. i18n: :email: Email Address, char, required, readonly

:email: Email Address, char, required, readonly

.. i18n: :server_statistics: Statistics, one2many

:server_statistics: Statistics, one2many

.. i18n: :user: User Name, char, required, readonly

:user: User Name, char, required, readonly

.. i18n: :active: Active, boolean

:active: Active, boolean

.. i18n: :verify_email: Verify Message, text, readonly

:verify_email: Verify Message, text, readonly

.. i18n: :password: Password, char, required, readonly

:password: Password, char, required, readonly

.. i18n: :type: Server Type, selection, required

:type: Server Type, selection, required

.. i18n: :port: SMTP Port, char, required, readonly

:port: SMTP Port, char, required, readonly

.. i18n: :users_id: Users Allowed, many2many

:users_id: Users Allowed, many2many

.. i18n: Object: Email Client History (email.smtpclient.history)
.. i18n: #######################################################

Object: Email Client History (email.smtpclient.history)
#######################################################

.. i18n: :server_id: Smtp Server, many2one, required

:server_id: Smtp Server, many2one, required

.. i18n: :user_id: Username, many2one, readonly

:user_id: Username, many2one, readonly

.. i18n: :name: Description, text, required, readonly

:name: Description, text, required, readonly

.. i18n: :resource_id: Resource ID, integer, readonly

:resource_id: Resource ID, integer, readonly

.. i18n: :date_create: Date, datetime, readonly

:date_create: Date, datetime, readonly

.. i18n: :model: Model, many2one, readonly

:model: Model, many2one, readonly

.. i18n: :email: Email, char, readonly

:email: Email, char, readonly

.. i18n: Object: Server Statistics (report.smtp.server)
.. i18n: ##############################################

Object: Server Statistics (report.smtp.server)
##############################################

.. i18n: :model: Model, char, readonly

:model: Model, char, readonly

.. i18n: :no: Total No., integer, readonly

:no: Total No., integer, readonly

.. i18n: :server_id: Server ID, many2one, readonly

:server_id: Server ID, many2one, readonly

.. i18n: :name: Server, char, readonly

:name: Server, char, readonly

.. i18n: :history: History, char, readonly

:history: History, char, readonly

.. i18n: Object: res.company.address (res.company.address)
.. i18n: #################################################

Object: res.company.address (res.company.address)
#################################################

.. i18n: :email: Email Address, many2one, required

:email: Email Address, many2one, required

.. i18n: :name: Address Type, selection, required

:name: Address Type, selection, required

.. i18n: :company_id: Company, many2one, required

:company_id: Company, many2one, required
