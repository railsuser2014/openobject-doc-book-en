
.. index::
   single: Installation; PostgreSQL (windows)
   single: PostgreSQL; Installation (windows)
.. 

.. _postgresql-server-installation:

PostgreSQL Server installation and configuration
================================================

Installing PostgreSQL Server
----------------------------

You can download the windows installer from
the `PostgreSQL download page <http://www.postgresql.org/download/windows>`__

Depending on your need, choose either the *One Click Installer* or the
*pgInstaller* and click on the executable you've just downloaded.

.. index::
   single: PostgreSQL; setup a user (windows)
   single: PostgreSQL; setup a database (windows)
.. 

Setup a PostgreSQL user
-----------------------

When the installations of the required software are done, you have to create a
PostgreSQL user. Open ERP will use this user to connect to PostgreSQL.

Add a user
++++++++++

Start a windows console (run the ``cmd`` command in *Start menu -> Run*).

Change directory to the *Postgresql* ``bin`` directory
(eg. ``c:\\Program Files\\PosgtreSQL\\8.3\\bin``) or add this directory to 
your *PATH* environment variable.

The default superuser for PostgreSQL is called *postgres*. His password was
chosen during the PostgreSQL installation.

In your windows console, type: ::

    C:\Program Files\PostgreSQL\8.3\bin>createuser.exe --createdb --username postgres --no-createrole --pwprompt openuser
    Enter password for new role: XXXXXXXXXX
    Enter it again:XXXXXXXXXX
    Password: YYYYYYYYYY
.. 

  * line 1 is the command itself
  * line 2 asks you the new user's password
  * line 3 asks you to confirm the new user's password
  * line 4 asks you the *postgres* user's password

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

