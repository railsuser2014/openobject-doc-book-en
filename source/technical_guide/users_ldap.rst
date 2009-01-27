
Module Authenticate users with ldap server (*users_ldap*)
=========================================================
:Module: users_ldap
:Name: Authenticate users with ldap server
:Version: 5.0.0.1
:Directory: users_ldap
:Web: http://tinyerp.com/

Description
-----------

::

  Add support for authentication by ldap server

Dependencies
------------

 * base - installed

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

Object: res.company.ldap
########################

.. index::
  single: res.company.ldap object
.. 


:sequence: Sequence, integer



.. index::
  single: sequence field
.. 




:ldap_password: LDAP password, char, required



.. index::
  single: ldap_password field
.. 




:ldap_server: LDAP Server address, char, required



.. index::
  single: ldap_server field
.. 




:company: Company, many2one, required



.. index::
  single: company field
.. 




:ldap_base: LDAP base, char, required



.. index::
  single: ldap_base field
.. 




:create_user: Create user, boolean

    *Create the user if not in database*

.. index::
  single: create_user field
.. 




:ldap_server_port: LDAP Server port, integer, required



.. index::
  single: ldap_server_port field
.. 




:user: Model user, many2one

    *Model used for user creation*

.. index::
  single: user field
.. 




:ldap_binddn: LDAP binddn, char, required



.. index::
  single: ldap_binddn field
.. 




:ldap_filter: LDAP filter, char, required



.. index::
  single: ldap_filter field
.. 

