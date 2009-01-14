
.. todo:: This section covers the 4.2 version of OpenERP

Gentoo Server Install
"""""""""""""""""""""

An ebuild suggestion has been sent to the Gentoo Bugzilla. Hopefully they will integrate
pydot (Gentoo Bug 106983), tinyerp-server (106982) and tinyerp-client (107045) into Portage.
Until then, you can either use the ebuilds from the bug reports, or doing it the way
described below.

This package depends on

  * >=dev-db/postgresql-7.4
  * dev-python/pypgsql
  * dev-python/reportlab
  * dev-python/pyparsing
  * media-gfx/pydot [Formerly known as dev-python/pydot]

Important: emerge egenix-mx-base before psycopg!

  * =dev-python/psycopg-1*
  * dev-libs/libxml2
  * dev-libs/libxslt
  * dev-python/pyxml [Seems to need this as well]

Note that psycopg version 2.* installs as the python package psycopg2 which won't work,
therefore we install version 1.* above.

Download the Distribution File
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

  # cd /tmp
  # wget http://openerp.com/download/stable/source/tinyerp-server-4.2.3.4.tar.gz
  # tar xvzf tinyerp-server-4.2.3.4.tar.gz

Setup a System Account
^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

  # adduser -m terp

Install the Distribution
^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

  # cd tinyerp-server-4.2.3.4
  # ./setup.py install --prefix=/usr/local

Note you have to manually correct the path to your tinyerp-server install in /usr/local/bin/
tinyerp-server to use the correct prefix because of a ?bug? that causes setup.py to ignore
it when making the script.

Create the PostgreSQL Database
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

  # createuser --username=postgres --no-createdb --no-adduser terp
    CREATE USER
  # createdb --username=postgres --owner=terp --encoding=UNICODE terp
    CREATE DATABASE

Create Log and PID directories
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

  mkdir /var/log/TinyERP
  chown terp /var/log/TinyERP/
  mkdir /var/run/TinyERP
  chown terp /var/run/TinyERP/

Initialize the Database and Start the Server
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

English
#######

Note for our first run we initialize the entire database and save a config file into
~/.terp_serverrc and then stop the server(so we know it finished).

.. code-block:: bash

  # su terp -c "/usr/local/bin/tinyerp-server --init=all --pidfile=/var/run/TinyERP/tinyerp-server.pid --logfile=/var/log/TinyERP/tinyerp-server.log -s --stop-after-init"

French
######

.. code-block:: bash

  # su terp -c "/usr/local/bin/tinyerp-server --init=all-fr --pidfile=/var/run/TinyERP/tinyerp-server.pid --logfile=/var/log/TinyERP/tinyerp-server.log -s --stop-after-init"
  # ./tinyerp_server.py-v--i18n-import=/usr/share/doc/tinerp-server-3.0.2/i18n/french_fr-2_0_8_1.csv-lfr

More languages are available.

Start the Server
^^^^^^^^^^^^^^^^

.. code-block:: bash

  # start-stop-daemon --start --chuid=terp:terp --background --exec /usr/local/bin/tinyerp-server -- -c /home/terp/.terp_serverrc

Note replace /home/terp/.terp_serverrc with the correct location of the configuration file
created above with -s, for some reason the default path is not picked up correctly here.

Stop the Server
^^^^^^^^^^^^^^^

.. code-block:: bash

  # start-stop-daemon --stop --pidfile /var/run/TinyERP/tinyerp-server.pid

Additionally, the following /etc/init.d/tinyerp-server script may be used:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

  #!/sbin/runscript==
  # Copyright 1999-2006 Gentoo Foundation
  # Distributed under the terms of the GNU General Public License, v2 or later
  # $Header: /var/cvsroot/gentoo-x86/www-apps/trac/files/tracd.initd,v 1.1 2006/02/22 22:11:43 dju Exp $

  BASE=TinyERP
  PID=/var/run/$BASE/$BASE.pid
  PROGRAM=/usr/local/bin/tinyerp-server
  USER=terp

  depend() {
        need net
  }

  start() {
        ebegin "Starting $BASE"
        start-stop-daemon -v --chuid=terp --background --start --exec $PROGRAM
        eend $?
  }

  stop() {
        ebegin "Stopping $BASE"
        start-stop-daemon --stop --pidfile $PID
        end $?
  }

Append '-lfr' to start it in French language mode. This should really be stored in a ``/etc/init.d/tinyerp-server`` script. You should note two things.

::

  # The server does not fork itself to daemon mode. You will have to do this explicitly.
  # The server logs to standard out, not to syslog and not to standard error. You should redirect the output to a file.

Gentoo Client Install
"""""""""""""""""""""

This package depends on

  * >=dev-lang/python-2.3
  * dev-python/pygtk (need to @@USE=gnome@@ to enable Glade bindings)

Download the Distribution File
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

  # cd /tmp
  # wget http://tinyerp.org/download/sources/tinyerp-client-3.0.2.tar.gz
  # tar xvzf tinyerp_client-v2.0.8.tar.gz

Install the Distribution
^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

  # cd tinyerp-client-3.0.2
  # ./setup.py --prefix=/usr/local

Start the Client
^^^^^^^^^^^^^^^^

.. code-block:: bash

  $ tinyerp-client

should start the client. A few useful command line options are available:

-u

      Set the user name (default is admin)

-p

      Set the connection port (default is 8069)

-s

      Set the connection host (default is localhost)

More options are available.

If you run into the following errors:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  * gobject.GError: Failed to open file '/usr/share/pixmaps/tinyerp-client/flag.png':
    No such file or directory
  * AssertionError: Could not find path for /usr/local/lib/python2.4/site-packages/
    tinyerp-client/terp.glade !

then your path needs to be corrected in ~/.terprc. Here are the correct paths for this
install:

::

  [path]
  pixmaps = /usr/local/share/pixmaps/tinyerp-client
  share = /usr/local/share/tinyerp-client

Add a Shortcut
^^^^^^^^^^^^^^

There are icons in /usr/share/pixmaps/tinyerp-client to be used for GUI systems. You will
probably want to use one of images named ``tinyerp-icon-32x32.png`` or so.

::

  /usr/share/applications/tinyerp.desktop:
  [Desktop Entry]
  Name=Tiny ERP
  Categories=Application;ERM;
  Comment=Integrated Resource Planner
  Exec=/usr/bin/tinyerp-client
  Icon=tinyerp-icon-32x32.png
  Terminal=0
  Type=Application
  Encoding=UTF-8

