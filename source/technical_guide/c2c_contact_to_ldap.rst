
.. module:: c2c_contact_to_ldap
    :synopsis: Camptocamp Partner extension to synchronize TinyERP with ldap 
    :noindex:
.. 

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

Camptocamp Partner extension to synchronize TinyERP with ldap (*c2c_contact_to_ldap*)
=====================================================================================
:Module: c2c_contact_to_ldap
:Name: Camptocamp Partner extension to synchronize TinyERP with ldap
:Version: 1.1
:Author: Camptocamp
:Directory: c2c_contact_to_ldap
:Web: http://www.camptocamp.com
:Official module: no
:Quality certified: no

Description
-----------

::

  
  Live partner address synchronization through a LDAP module (inetOrgPerson). 
  Tiny becomes the master of the LDAP. Each time an addresse is deleted, created or updated the same is done in the ldap (a new record is pushed).
  The LDAP configuration is done in the company view. There can be one different LDAP per company! Do not forget to activate
  the LDAP link in the configuration. 
  The used LDAP depends on the current user company.
  	
  This module does not allows bulk batching synchronisation into the LDAP and is thus not suitable for an instant use with an existing LDAP.
  n order to use it with an existing LDAP you have to alter the uid of contact in your LDAP. The uid should be terp_ plus the TinyERP contact id (for example terp_10).  
  	
  N.B: the modue requires the python-ldap library
  
  ---------------------------------------------------------------------------------------------------------------------------------------
  Ce module interface les partenaires TinyERP avec un repository LDAP existant. Ainsi, TinyERP devient le master, l'interface unique
  de saisie des partenaires de l'entreprise. Tous ce qui est renseigné dans TinyERP est automatiquement reporté dans 
  LDAP (ajout, suppression, modification). 
  
  L'avantage d'utiliser un tel système est la constitution d'une base de données
  client unique , qui pourra s'interfacer avec un client mail (Outlook, Thunderbird, etc..) pour avoir la complétion des adresses dans la 
  rédaction des mails. De plus, de nombreux systèmes de téléphonie utilisent maintenant une telle base pour la gestion des appels 
  (click to dial ou remontée de fiche).
  
  

Dependencies
------------

 * :mod:`base`
 * :mod:`c2c_partner_address`

Reports
-------

None


Menus
-------


None


Views
-----


None



Objects
-------

None
