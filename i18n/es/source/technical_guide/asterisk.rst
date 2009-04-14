
.. i18n: .. module:: asterisk
.. i18n:     :synopsis: Asterisk 
.. i18n:     :noindex:
.. i18n: .. 

.. module:: asterisk
    :synopsis: Asterisk 
    :noindex:
.. 

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. i18n: Asterisk (*asterisk*)
.. i18n: =====================
.. i18n: :Module: asterisk
.. i18n: :Name: Asterisk
.. i18n: :Version: 5.0.0.1proto2
.. i18n: :Author: Tiny
.. i18n: :Directory: asterisk
.. i18n: :Web: 
.. i18n: :Official module: no
.. i18n: :Quality certified: no

Asterisk (*asterisk*)
=====================
:Module: asterisk
:Name: Asterisk
:Version: 5.0.0.1proto2
:Author: Tiny
:Directory: asterisk
:Web: 
:Official module: no
:Quality certified: no

.. i18n: Description
.. i18n: -----------

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   Manages a list of asterisk servers and IP phones.
.. i18n:   This module implements a system to popup the partner form based on phone calls.
.. i18n:   This is still a proof of concept, that have been made during Tiny ERP's technical training session.

::

  Manages a list of asterisk servers and IP phones.
  This module implements a system to popup the partner form based on phone calls.
  This is still a proof of concept, that have been made during Tiny ERP's technical training session.

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

.. i18n:  * Sys Admin
.. i18n:  * Sys Admin/Configuration
.. i18n:  * Sys Admin/Configuration/Asterisk Server
.. i18n:  * Sys Admin/Configuration/IP Phones
.. i18n:  * Sys Admin/Get Partner From Call

 * Sys Admin
 * Sys Admin/Configuration
 * Sys Admin/Configuration/Asterisk Server
 * Sys Admin/Configuration/IP Phones
 * Sys Admin/Get Partner From Call

.. i18n: Views
.. i18n: -----

Views
-----

.. i18n:  * Asterisk Server (tree)
.. i18n:  * Asterisk Server (form)
.. i18n:  * IP Phone (tree)
.. i18n:  * IP Phone (form)

 * Asterisk Server (tree)
 * Asterisk Server (form)
 * IP Phone (tree)
 * IP Phone (form)

.. i18n: Objects
.. i18n: -------

Objects
-------

.. i18n: Object: asterisk.server (asterisk.server)
.. i18n: #########################################

Object: asterisk.server (asterisk.server)
#########################################

.. i18n: :host: Server Host, char, required

:host: Server Host, char, required

.. i18n: :login: Login, char

:login: Login, char

.. i18n: :password: Password, char

:password: Password, char

.. i18n: :port: Server Port, integer, required

:port: Server Port, integer, required

.. i18n: :name: Asterisk Server, char, required

:name: Asterisk Server, char, required

.. i18n: Object: IP Phone (asterisk.phone)
.. i18n: #################################

Object: IP Phone (asterisk.phone)
#################################

.. i18n: :current_callerid: Current Caller, char

:current_callerid: Current Caller, char

.. i18n: :user_id: User, many2one, required

:user_id: User, many2one, required

.. i18n: :name: Phone Name, char, required

:name: Phone Name, char, required

.. i18n: :ip: Phone IP, char

:ip: Phone IP, char

.. i18n: :state: State, selection

:state: State, selection

.. i18n: :phoneid: Phone ID, char

:phoneid: Phone ID, char

.. i18n: :asterisk_id: Asterisk Server, many2one, required

:asterisk_id: Asterisk Server, many2one, required
