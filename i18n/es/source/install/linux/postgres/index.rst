
.. i18n: .. index::
.. i18n:    single: Installation; PostgreSQL
.. i18n:    single: PostgreSQL; Installation
.. i18n: .. 

.. index::
   single: Installation; PostgreSQL
   single: PostgreSQL; Installation
.. 

.. i18n: .. _postgresql-server-installation:
.. i18n: 
.. i18n: PostgreSQL Server installation and configuration
.. i18n: ================================================

.. _postgresql-server-installation:

PostgreSQL Server installation and configuration
================================================

.. i18n: Installing PostgreSQL Server
.. i18n: ----------------------------

Installing PostgreSQL Server
----------------------------

.. i18n: The `PostgreSQL download page <http://www.postgresql.org/download/linux>`__
.. i18n: lists the available installation methods. Choose the one that suits your needs
.. i18n: best.

The `PostgreSQL download page <http://www.postgresql.org/download/linux>`__
lists the available installation methods. Choose the one that suits your needs
best.

.. i18n: Example on Ubuntu
.. i18n: +++++++++++++++++

Example on Ubuntu
+++++++++++++++++

.. i18n: On Ubuntu, install the **postgresql** package: ::
.. i18n: 
.. i18n:   sudo apt-get install postgresql

On Ubuntu, install the **postgresql** package: ::

  sudo apt-get install postgresql

.. i18n: .. index::
.. i18n:    single: PostgreSQL; setup a user
.. i18n:    single: PostgreSQL; setup a database
.. i18n: .. 

.. index::
   single: PostgreSQL; setup a user
   single: PostgreSQL; setup a database
.. 

.. i18n: Setup a PostgreSQL user
.. i18n: +++++++++++++++++++++++

Setup a PostgreSQL user
+++++++++++++++++++++++

.. i18n: When the installations of the required software are done, you have to create a
.. i18n: PostgreSQL user. Open ERP will use this user to connect to PostgreSQL.

When the installations of the required software are done, you have to create a
PostgreSQL user. Open ERP will use this user to connect to PostgreSQL.

.. i18n: Add a user
.. i18n: ++++++++++

Add a user
++++++++++

.. i18n: The default superuser for PostgreSQL is called *postgres*. We will use it below
.. i18n: as an example. If you wish to use it as well, you may need to login as this
.. i18n: user first. ::
.. i18n: 
.. i18n:     johndoe$ sudo su - postgres
.. i18n:     password: XXXXXXXXXX
.. i18n:     postgres$ createuser --createdb --no-createrole --pwprompt openuser
.. i18n:     Enter password for new role: XXXXXXXXXX
.. i18n:     Enter it again: XXXXXXXXXX
.. i18n:     CREATE ROLE
.. i18n:     postgres$

The default superuser for PostgreSQL is called *postgres*. We will use it below
as an example. If you wish to use it as well, you may need to login as this
user first. ::

    johndoe$ sudo su - postgres
    password: XXXXXXXXXX
    postgres$ createuser --createdb --no-createrole --pwprompt openuser
    Enter password for new role: XXXXXXXXXX
    Enter it again: XXXXXXXXXX
    CREATE ROLE
    postgres$

.. i18n: , assuming you want to create the *openuser* role.

, assuming you want to create the *openuser* role.

.. i18n: Option explanations:

Option explanations:

.. i18n:   * ``--createdb`` : the new user will be able to create new databases
.. i18n:   * ``--username postgres`` : *createuser* will use the *postgres* user (superuser)
.. i18n:   * ``--no-createrole`` : the new user will not be able to create new users
.. i18n:   * ``--pwprompt`` : *createuser* will ask you the new user's password
.. i18n:   * ``openuser`` the new user's name

  * ``--createdb`` : the new user will be able to create new databases
  * ``--username postgres`` : *createuser* will use the *postgres* user (superuser)
  * ``--no-createrole`` : the new user will not be able to create new users
  * ``--pwprompt`` : *createuser* will ask you the new user's password
  * ``openuser`` the new user's name

.. i18n: You can now start the Open ERP Server. You will probably need to modify the
.. i18n: Open ERP configuration file to your need.

You can now start the Open ERP Server. You will probably need to modify the
Open ERP configuration file to your need.

.. i18n: Case insensitive searches issue
.. i18n: +++++++++++++++++++++++++++++++

Case insensitive searches issue
+++++++++++++++++++++++++++++++

.. i18n: For an installation which need full UTF8 character support consider to use
.. i18n: postgres >= 8.2.x. Prior to this Open ERP search will eventually not return the
.. i18n: expected results for case insensitive searches, which are used for searching
.. i18n: partners, products etc.

For an installation which need full UTF8 character support consider to use
postgres >= 8.2.x. Prior to this Open ERP search will eventually not return the
expected results for case insensitive searches, which are used for searching
partners, products etc.

.. i18n: Example: ::
.. i18n: 
.. i18n:     SELECT 'x' FROM my_table WHERE 'bét' ilike 'BÉT'
.. i18n:     --matches only in 8.2.x

Example: ::

    SELECT 'x' FROM my_table WHERE 'bét' ilike 'BÉT'
    --matches only in 8.2.x
