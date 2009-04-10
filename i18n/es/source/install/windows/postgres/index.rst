
.. i18n: .. index::
.. i18n:    single: Installation; PostgreSQL (windows)
.. i18n:    single: PostgreSQL; Installation (windows)
.. i18n: .. 

.. index::
   single: Installation; PostgreSQL (windows)
   single: PostgreSQL; Installation (windows)
.. 

.. i18n: .. _windows_postgresql-server-installation:
.. i18n: 
.. i18n: PostgreSQL Server installation and configuration
.. i18n: ================================================

.. _windows_postgresql-server-installation:

PostgreSQL Server installation and configuration
================================================

.. i18n: Installing PostgreSQL Server
.. i18n: ----------------------------

Installing PostgreSQL Server
----------------------------

.. i18n: You can download the windows installer from
.. i18n: the `PostgreSQL download page <http://www.postgresql.org/download/windows>`__

You can download the windows installer from
the `PostgreSQL download page <http://www.postgresql.org/download/windows>`__

.. i18n: Depending on your need, choose either the *One Click Installer* or the
.. i18n: *pgInstaller* and click on the executable you've just downloaded.

Depending on your need, choose either the *One Click Installer* or the
*pgInstaller* and click on the executable you've just downloaded.

.. i18n: .. index::
.. i18n:    single: PostgreSQL; setup a user (windows)
.. i18n:    single: PostgreSQL; setup a database (windows)
.. i18n: .. 

.. index::
   single: PostgreSQL; setup a user (windows)
   single: PostgreSQL; setup a database (windows)
.. 

.. i18n: Setup a PostgreSQL user
.. i18n: -----------------------

Setup a PostgreSQL user
-----------------------

.. i18n: When the installations of the required software are done, you have to create a
.. i18n: PostgreSQL user. Open ERP will use this user to connect to PostgreSQL.

When the installations of the required software are done, you have to create a
PostgreSQL user. Open ERP will use this user to connect to PostgreSQL.

.. i18n: Add a user
.. i18n: ++++++++++

Add a user
++++++++++

.. i18n: Start a windows console (run the ``cmd`` command in *Start menu -> Run*).

Start a windows console (run the ``cmd`` command in *Start menu -> Run*).

.. i18n: Change directory to the *Postgresql* ``bin`` directory
.. i18n: (eg. ``c:\\Program Files\\PosgtreSQL\\8.3\\bin``) or add this directory to 
.. i18n: your *PATH* environment variable.

Change directory to the *Postgresql* ``bin`` directory
(eg. ``c:\\Program Files\\PosgtreSQL\\8.3\\bin``) or add this directory to 
your *PATH* environment variable.

.. i18n: The default superuser for PostgreSQL is called *postgres*. His password was
.. i18n: chosen during the PostgreSQL installation.

The default superuser for PostgreSQL is called *postgres*. His password was
chosen during the PostgreSQL installation.

.. i18n: In your windows console, type::
.. i18n: 
.. i18n:     C:\Program Files\PostgreSQL\8.3\bin>createuser.exe --createdb --username postgres --no-createrole --pwprompt openuser
.. i18n:     Enter password for new role: XXXXXXXXXX
.. i18n:     Enter it again:XXXXXXXXXX
.. i18n:     Password: YYYYYYYYYY

In your windows console, type::

    C:\Program Files\PostgreSQL\8.3\bin>createuser.exe --createdb --username postgres --no-createrole --pwprompt openuser
    Enter password for new role: XXXXXXXXXX
    Enter it again:XXXXXXXXXX
    Password: YYYYYYYYYY

.. i18n:   * line 1 is the command itself
.. i18n:   * line 2 asks you the new user's password
.. i18n:   * line 3 asks you to confirm the new user's password
.. i18n:   * line 4 asks you the *postgres* user's password

  * line 1 is the command itself
  * line 2 asks you the new user's password
  * line 3 asks you to confirm the new user's password
  * line 4 asks you the *postgres* user's password

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
