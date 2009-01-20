
Ubuntu 8.10 (Intrepid Ibex)
"""""""""""""""""""""""""""

Install Client 4.2.3.4
^^^^^^^^^^^^^^^^^^^^^^

Install client dependencies: ::

  $ sudo apt-get install python-egenix-mxdatetime python-egenix-mxtools

Download OpenERP/TinyERP deb package from the official unstable Debian repository. (It's not
recommended to add this repository to your apt sources list. There are many *really* unstable
packages on it).

http://packages.debian.org/sid/all/tinyerp-client/download

After download, install: ::

  $ sudo dpkg -i tinyerp-client_4.2.3.4-1_all.deb

Install Server 4.2.3.4
^^^^^^^^^^^^^^^^^^^^^^

Install server dependencies: ::

  $ sudo apt-get install python-psycopg python-libxslt1 python-reportlab python-tz \
    libpq5 python-egenix-mxdatetime python-egenix-mxtools python-xml  python-lxml

Download OpenERP/TinyERP deb package from the official unstable Debian repository. (It's not
recommended add this repository to your apt sources list. There are many *really* unstable
packages on it).

http://packages.debian.org/sid/all/tinyerp-server/download

After download, install: ::

  $ sudo dpkg -i tinyerp-server_4.2.3.4-3_all.deb

Database PostgreSQL
###################

The server requires PostgreSQL database. To install type: ::

  $ sudo apt-get install postgresql

Create the database:

When the PostgreSQL are done, you have to create a database. Type: ::

  $ sudo su postgres
  $ createuser -U postgres --createdb --no-adduser -P terp
  $ createdb -U postgres -O terp --encoding=UNICODE terp
  $ exit

Set your DB password (created above) in /etc/default/tinyerp-server file: ::

  $ sudo gedit /etc/default/tinyerp-server

Like this: ::

  # Specify the database password (Default: not set).
  DATABASE_PASSWORD="my_role_password"

Restart Server
##############

After set the password we need restart the server: ::

  sudo /etc/init.d/tinyerp-server restart

Connecting with TinyERP/OpenERP client
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you have installed the client, use the Applications -> Internet -> Tiny ERP Client

The default connection settings should already be the ones you configured in the server's
configuration file.

If you haven't created any other account yet, use admin/admin to connect with the client,
and define the installation settings (your company details, mainly).

Hardy Heron (8.04) and Gutsy Gibbon (7.10)
""""""""""""""""""""""""""""""""""""""""""

Install packages
^^^^^^^^^^^^^^^^

Install all packages listed below (some might be installed already), or just type: ::

  $ sudo apt-get install python-xml python-libxml2 python-libxslt1 python-psycopg python-imaging \
    python-pyparsing python-reportlab graphviz python-tz python-pyopenssl gs-gpl python-matplotlib

Database PostgreSQL
^^^^^^^^^^^^^^^^^^^

Installation
############

Install PostgreSQL 8.2.x on Synaptic, or type: ::

  $ sudo apt-get install postgresql-8.2

Note: There some troubles related with PostregreSQL 8.3 as exposed in this bug report. Avoid
it on this TinyERP/OpenERP version (4.2.0-1ubuntu1).

.. note:: Now PostgreSQL 8.3 works with TinyERP 4.2 with 4.2.3.2 and later

Create the database
###################

When the PostgreSQL are done, you have to create a database.Type: ::

  $ sudo su postgres
  $ createuser -U postgres --createdb --no-adduser -P terp
  $ createdb -U postgres -O terp --encoding=UNICODE terp
  $ exit

See Setup a Postgresql user and database for details.

It is not recommended to use another username for the database user, as the distinction
between the system user and the database user is not strong enough at this point in time
(version 2.4) and it might result in you not being able to create new databases from the
client interfaces.

Install TinyERP 4.2.2 Server and Client
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. Note:: Ubuntu packages will create a terp system user that will be used to start the
          server and possibly (for some operations like creating a new database) to connect to the
          database.

32bits architecture
###################

There is now a repository which holds the new 4.2.2 of tinyerp for Ubuntu (it might also
work on debian).

The repository can be found on http://ubuntu.roomandspace.com/. Just go there and add the
repository, so this should update your 4.2.2 of tinyerp, but it does not automaticaly update
existing database, only a new installation is tested.

After add repository install from Synaptic, or type: ::

  $ sudo apt-get install tinyerp-server tinyerp-client

64bits architecture
###################

The repository does not work with x86_64 architecture, so you have to install them manualy.

First download TinyERP .deb files ("tinyerp-server_4.2.2-1_all.deb" and
"tinyerp-client_4.2.2-1_all.deb") directly from the repository folder.

  http://ubuntu.roomandspace.com/dists/hardy/main/binary-i386/

Now install the packages manualy. ::

  $ sudo dpkg --install <path>/tinyerp-client_4.2.2-1_all.deb
  $ sudo dpkg --install <path>/tinyerp-server_4.2.2-1_all.deb

Starting the server
^^^^^^^^^^^^^^^^^^^

Note: For 7.10 and Postgres 8.2, the default port for Postgres is 5432. However the config
file "/etc/default/tinyerp-server" has the postgres port set at 5433. You must change this
or you will get an error stating "cannot connect to server".

Note: For 8.04 and Postgres 8.3, the default port for Postgres is 5433, and you might have
the opposite problem that the port defined in the tiny configuration is 5432. You must
change this or you will get an error stating "cannot connect to server".

To change it, open a terminal and type: ::

  $ sudo nano /etc/default/tinyerp-server

When it comes up, scroll down to the setting for postgres and change to 5432. Press "ctrl o"
to save and "ctrl x" to exit. Restart the tinyerp-server. ::

  $ sudo /etc/init.d/tinyerp-server restart

The process will be started with a username depending on what USER you have defined in /etc/
default/tinyerp-server. For trial/development purposes, you can use your Ubuntu username.
However, for production environments, using a specific Ubuntu user for the TinyERP/OpenERP
process is recommended.

If your server still doesn't start, you can check the logs in real time by using the command

::

  $ sudo tail -f /var/log/tinyerp.log

Connecting with TinyERP/OpenERP client
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you have installed the client, use the Applications -> Internet -> Tiny ERP Client

The default connection settings should already be the ones you configured in the server's
configuration file.

If you haven't created any other account yet, use admin/admin to connect with the client,
and define the installation settings (your company details, mainly).

Creating more databases
^^^^^^^^^^^^^^^^^^^^^^^

Creating more databases can normally be done through the rich TinyERP/OpenERP client, by
using the File -> Databases -> New database menu (using the default password "admin" if you
haven't changed it).

However, and as reported on the forum, you might run into the error "Could not create
database" when doing that. On an Ubuntu (or Debian) server, this might be due to one of two
things, which you can check out on the Linux troubleshooting page

Adding a module
^^^^^^^^^^^^^^^

You can add modules through the Administration -> Modules management -> Import new module.

However, this depends on the permissions set on the /usr/share/tinyerp-server/addons/
directory. If not set correctly, you will receive the following error message: ::

  Error !
  Can not create the module file:
   /usr/lib/tinyerp-server/addons/[yourmodule].zip!

The directory indicated is actually a symbolic link to /usr/share/tinyerp-server/addons/

To make sure you can install new modules, you have to let the system user terp write in this
directory. For example, you could change the permissions by issuing the following command:

::

  sudo chown -R terp /usr/share/tinyerp-server/addons

Installation from source (for all versions)
"""""""""""""""""""""""""""""""""""""""""""

Using Synaptic Package Manager
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

get (some might be installed already)

::

  python-xml
  python-libxml2
  python-libxslt1
  python-psycopg
  python-imaging
  python-pyparsing
  python-reportlab
  graphviz
  postgresql
  python-tz
  python-pyopenssl
  gs-gpl
  python-matplotlib

Using command line : (cut/paste in a terminal)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

  $ sudo apt-get install python-xml python-libxml2 python-libxslt1 python-psycopg python- imaging python-pyparsing
  $ sudo apt-get install python-reportlab graphviz postgresql python-tz python-pyopenssl gs-gpl python-matplotlib
  $ sudo apt-get install python-lxml python-pychart python-hippocanvas

Creating the database
"""""""""""""""""""""

When the installations are done, you have to create a database, see
:ref:`setup-a-postgresql-user-and-database-link` for details.

TinyERP Server
""""""""""""""

And now (This does not need to be done if you install using Synaptic or apt-get) TinyERP
server must be decompressed and started;

::

  tar xzvf tinyerp_server-v...tar.gz
   cd server/bin
   tinyerp_server.py

Verbose version : Download and extract the TinyERP version of your choice. Run the server as
user "postgres" (by typing "sudo su postgres" and your password (of the default user, not
the postgres user) in the terminal) and then typing "python2.4 tinyerp-server.py" in
"tinyerp-server-directory/bin/". Your server is now running, check

::

  $ ps ax

Installing OpenERP Client on Ubuntu Linux Desktop
"""""""""""""""""""""""""""""""""""""""""""""""""

::

  apt-get install tinyerp-client python-tz python-psycopg python-matplotlib

Now you got TinyERP installed but it is an old version. I install the old version first
because the new version from Room and Space is missing the pixmaps. Do following to install
the new version.

Get deb file from Room and Space then execute the deb file from desktop, don't run as dpkg
otherwise you might not get all dependencies installed.

As a side note the server deb file from Room and Space, and probably the client as well will
also work on a debian box. I do have the server running on a Debian box. --gruessle 02:05, 4
October 2008 (UTC)

NOTES AND OLDIES
""""""""""""""""

for 7.04 ("feisty fawn"), if you are using the development version of tinyerp, you can use
python2.5 (by replacing the commands "python2.4 tinyerp-server.py" with "./tinyerp-
server.py" below). python2.5 was incompatible with 4.0 version of tinyerp.

Note: There's no need of creating a database outside of the tinyerp-client! Check Postgresql
setup page in this wiki. Download the tiny \*.tar.gz files (not the tiny-packages), extract
them, position in the tiny ``/bin directory and start tiny``.

There might be some problems with older versions of tinyERP. Search for the tinyERP-config
files ".terp_serverrc" and ".terprc" and change (or simply remove) them before starting a
new version. This search can be done with these commands in a terminal:

.. *

::

  $ sudo find / -name ".terprc" -print
  $ sudo find / -name ".terp_serverrc" -print

Older versions of Ubuntu (Breezy)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1.Modify the /etc/apt/source.lists (using a text editor like gedit, kate or nano (in this
example gedit is used - if you don`t have it - just replace gedit with the name of your
programm of choice))

::

  $ sudo gedit /etc/apt/sources.list
  # (then you`ll be asked to enter the root password)

- Uncomment these two lines or add it if it does not exist:

::

  deb http://fr.archive.ubuntu.com/ubuntu breezy universe multiverse
  deb-src http://fr.archive.ubuntu.com/ubuntu breezy universe multiverse

- Save the file and launch the apt command

2.Update the repository by typing

::

  $ sudo apt-get update

in command lines or GUI (ubuntu 5.10)

  System>administration>synaptic package manager

(if you're using kubutu or other ubuntu-based distributions you may have another packagemanager (like adept for kubuntu)

3.Install the required packages and postgresql database by typing (in command line)

::

  $ sudo apt-get install python2.4-xml python2.4-libxml2 python2.4-libxslt1 python2.4-psycopg \
    python2.4-imaging python2.4-pyparsing python2.4-reportlab graphviz postgresql-7.4

or with a GUI /package manager (Synaptic/Adept) (ubuntu 5.10)

  # select the following packages from the list and choose install

::

  python2.4-xml
  python2.4-libxml2
  python2.4-libxslt1
  python2.4-psycopg
  python2.4-imaging
  python2.4-pyparsing
  python2.4-reportlab
  graphviz
  postgresql-7.4

then commit the changes

Normally at this step the required packages are installed and the postgresql server is
launched. For TinyERP-server above v4.0.0 you don't have to set up postgresql as described
in STEP 4.1, just go to STEP 5 on this page. You will now go to the STEP 4.1 (You are now in
2.1.9.4 to configure your Postgresql database.)

5.Download the Tinyerp Server Package.

6.Decompress it (* means: enter the full path here of your download);

::

  $ cd /
  $ tar xzvf /home/.../tinyerp-server-v...tgz*
  $ sudo chown -R postgres server

7. Start tinyerp server

::

  $ sudo su postgres
  $ cd server
  $ ./bin/tinyerp-server.py -d terp -r postgres -w postgres

After shutting down the server, next time you only need to redo step 7

