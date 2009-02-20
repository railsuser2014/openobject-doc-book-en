
.. module:: users_ldap
    :synopsis: Authenticate users with ldap server 
    :noindex:
.. 

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

Authenticate users with ldap server (*users_ldap*)
==================================================
:Module: users_ldap
:Name: Authenticate users with ldap server
:Version: 5.0.0.1
:Author: Tiny
:Directory: users_ldap
:Web: http://www.openerp.com//
:Official module: no
:Quality certified: no

Description
-----------

::

  Add support for authentication by ldap server

Dependencies
------------

 * :mod:`base`

Reports
-------

None


Menus
-------


None


Views
-----

 * \* INHERIT res.company.form.inherit.users_ldap (form)


Objects
-------

Object: res.company.ldap (res.company.ldap)
###########################################



:sequence: Sequence, integer





:ldap_password: LDAP password, char, required





:ldap_server: LDAP Server address, char, required





:company: Company, many2one, required





:ldap_base: LDAP base, char, required





:create_user: Create user, boolean

    *Create the user if not in database*



:ldap_server_port: LDAP Server port, integer, required





:user: Model user, many2one

    *Model used for user creation*



:ldap_binddn: LDAP binddn, char, required





:ldap_filter: LDAP filter, char, required


