
.. index::
   single: Installation; PostgreSQL
   single: PostgreSQL; Installation
.. 

.. _postgresql-server-installation:

PostgreSQL Server installation and configuration
================================================

Installing PostgreSQL Server
----------------------------

The `PostgreSQL download page <http://www.postgresql.org/download/linux>`__
lists the available installation methods. Choose the one that suits your needs
best.

Example on Ubuntu
+++++++++++++++++

On Ubuntu, install the **postgresql** package: ::

  sudo apt-get install postgresql

.. index::
   single: PostgreSQL; setup a user
   single: PostgreSQL; setup a database
.. 

Setup a PostgreSQL user
+++++++++++++++++++++++

When the installations of the required software are done, you have to create a
PostgreSQL user. Open ERP will use this user to connect to PostgreSQL.

Add a user
++++++++++

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

, assuming you want to create the *openuser* role.

Option explanations:

  * ``--createdb`` : the new user will be able to create new databases
  * ``--username postgres`` : *createuser* will use the *postgres* user (superuser)
  * ``--no-createrole`` : the new user will not be able to create new users
  * ``--pwprompt`` : *createuser* will ask you the new user's password
  * ``openuser`` the new user's name

You can now start the Open ERP Server. You will probably need to modify the
Open ERP configuration file to your need.

Case insensitive searches issue
+++++++++++++++++++++++++++++++

For an installation which need full UTF8 character support consider to use
postgres >= 8.2.x. Prior to this Open ERP search will eventually not return the
expected results for case insensitive searches, which are used for searching
partners, products etc.

Example: ::

    SELECT 'x' FROM my_table WHERE 'bét' ilike 'BÉT'
    --matches only in 8.2.x

