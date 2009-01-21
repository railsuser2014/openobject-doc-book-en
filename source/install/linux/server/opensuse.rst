
OpenSuse 11.0
"""""""""""""

Add repository
^^^^^^^^^^^^^^

The first thing we must do is to add a repository in Yast

::

  $ yast2 repositories

Add a Specify Url

  http://download.opensuse.org/repositories/home:/octo47:/openerp/openSUSE_11.0/

Install packages
^^^^^^^^^^^^^^^^

Install all packages listed below in yast software manager (some might be installed
already). Use the search tool:

::

  openerp-client openerp-server python-ReportLab python-egenix-mx-base python-matplotlib python-numpy python-parsing python-psycopg

Database PostgreSQL
^^^^^^^^^^^^^^^^^^^

Installation
############

Install PostgreSQL 8.2.x with yast2 softwaremanager.

.. note:: Now PostgreSQL 8.3 works with TinyERP 4.2 with 4.2.3.2 and later

Launch PostgreSQL
#################

Launch PostgreSQL.Type:

::

  $ su
  $ /etc/rc.d/postgresql start
  $ exit

Create the database
###################

When the PostgreSQL are done, you have to create a database.Type:

::

  $ su - postgres
  $ createuser -U postgres --createdb --no-adduser -P terp
  $ createdb -U postgres -O terp --encoding=UNICODE terp
  $ exit

See Setup a Postgresql user and database for details.

It is not recommended to use another username for the database user, as the distinction
between the system user and the database user is not strong enough at this point in time
(version 2.4) and it might result in you not being able to create new databases from the
client interfaces.

Starting the server
^^^^^^^^^^^^^^^^^^^

Start the tinyerp-server as user "postgres".

::

  $ sudo su postgres
  $ tinyerp-server

If your server still doesn't start, you can check the logs in real time by using the
command

::

  $ sudo tail -f /var/log/tinyerp.log

Connecting with TinyERP/OpenERP client
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you have installed the client,

Type in the console:

::

  $ tinyerp-client

If you haven't created any other account yet, use admin/admin to connect with the client,
and define the installation settings (your company details, mainly).

Creating more databases
^^^^^^^^^^^^^^^^^^^^^^^

Creating more databases can normally be done through the rich TinyERP/OpenERP client, by
using the File -> Databases -> New database menu (using the default password "admin" if
you haven't changed it).

