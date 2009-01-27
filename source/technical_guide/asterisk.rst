
Module Asterisk (*asterisk*)
============================
:Module: asterisk
:Name: Asterisk
:Version: 5.0.0.1proto2
:Directory: asterisk
:Web: 

Description
-----------

::

  Manages a list of asterisk servers and IP phones.
  This module implements a system to popup the partner form based on phone calls.
  This is still a proof of concept, that have been made during Tiny ERP's
  technical training session.

Dependencies
------------

 * base - installed

Reports
-------

None


Menus
-------

 * Sys Admin
 * Sys Admin/Configuration
 * Sys Admin/Configuration/Asterisk Server
 * Sys Admin/Configuration/IP Phones
 * Sys Admin/Get Partner From Call

Views
-----

 * Asterisk Server (tree)
 * Asterisk Server (form)
 * IP Phone (tree)
 * IP Phone (form)


Objects
-------

Object: asterisk.server
#######################

.. index::
  single: asterisk.server object
.. 


:host: Server Host, char, required



.. index::
  single: host field
.. 




:login: Login, char



.. index::
  single: login field
.. 




:password: Password, char



.. index::
  single: password field
.. 




:port: Server Port, integer, required



.. index::
  single: port field
.. 




:name: Asterisk Server, char, required



.. index::
  single: name field
.. 



Object: IP Phone
################

.. index::
  single: IP Phone object
.. 


:current_callerid: Current Caller, char



.. index::
  single: current_callerid field
.. 




:user_id: User, many2one, required



.. index::
  single: user_id field
.. 




:name: Phone Name, char, required



.. index::
  single: name field
.. 




:ip: Phone IP, char



.. index::
  single: ip field
.. 




:state: State, selection



.. index::
  single: state field
.. 




:phoneid: Phone ID, char



.. index::
  single: phoneid field
.. 




:asterisk_id: Asterisk Server, many2one, required



.. index::
  single: asterisk_id field
.. 

