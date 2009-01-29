
.. index::
   single: Installation; PostgreSQL
   single: PostgreSQL; Installation
.. 

.. _postgresql-server-installation:

PostgreSQL Server installation and configuration
================================================

Installing PostgreSQL Server
----------------------------

On Linux
++++++++

The `PostgreSQL download page <http://www.postgresql.org/download/linux>`__
lists the available installation methods. Choose the one that suits your needs
best.

Example on Ubuntu
"""""""""""""""""

On Ubuntu, install the **postgresql** package: ::

  sudo apt-get install postgresql

On Windows
++++++++++

You can download the windows installer from
the `PostgreSQL download page <http://www.postgresql.org/download/windows>`__

Depending on your need, choose either the *One Click Installer* or the
*pgInstaller* and click on the executable you've just downloaded.

.. index::
   single: PostgreSQL; setup a user
   single: PostgreSQL; setup a database
.. 

Setup a PostgreSQL user and database
++++++++++++++++++++++++++++++++++++

When the installations of the required software are done, you have to create a
database. The rights on the database are given to the postgres user by default.
You have to add the common-used user on which Open ERP is installed.

This assumes PostgreSQL is installed and running on your server.

For an installation which need full UTF8 character support consider to use
postgres >= 8.2.x. Prior to this Open ERP search will eventually not return the
expected results for case insensitive searches, which are used for searching
partners, products etc.

Example: ::

    SELECT 'x' FROM my_table WHERE 'bét' ilike 'BÉT'
    --matches only in 8.2.x

You have to create one database user and one database schema. (Make sure you
create an Unicode database, otherwise the server won't start correctly.)

The default superuser for PostgreSQL is called postgres. We will use it below
as an example. If you wish to use it as well, you may need to login as this
user first. ::

    johndoe$ sudo su - postgres
    password: XXXXXXXXXX
    postgres$

The default installation of PostgreSQL sets security to allow access without
password for localhost connections. This is called the trust security model.

If you run the database on the same host as the Open ERP server there is really
no need for a password, as long as you know what you are doing (or is alone on
the computer). To do without a password, simply leave the -P option out.::

    $ createuser -U postgres --createdb --no-adduser -P terp
    enter password:  XXXXXXXXXX
    repeat password: XXXXXXXXXX
    CREATE USER
    $ createdb -U postgres -O terp --encoding=UNICODE terp
    CREATE DATABASE

You can now start the Open ERP Server.

