
How-to install Open ERP on Slackware 11.0
"""""""""""""""""""""""""""""""""""""""""

Using Slackware (some reminders)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Generalities
############

More information is available at Slackware site: http://slackware.com. Slackware is a Linux
distribution created and maintained by Patrick Volkerding. Unlike most other Linux
distributions :

  * It uses a BSD-like system for managing run levels. All start-up (and shutdown)
    scripts reside in /etc/rc.d/ directory.
  * Software installation doesn't use rpm nor deb packages but tgz ones (slackware-
    specific). Each package contains files to install and install scripts.
  * Most post-installation configuration is made by editing text files (generally well
    documented).

How-to install a package on Slackware
#####################################

1. Using package management tools

Main package-management tools for Slackware don't manage dependences -- this is taken care
by Pat. All use command-lines and/or ncurses based menus All should be used as root, of
course :

  * pkgtool to delete/install/view files in packages (and some more features I won't
    speak about)
  * installpkg and removepkg (guess to do what ?)
  * slackpkg (can download packages for mirrors and install it)

Better use slackpkg when installing a package from a mirror (when it's officially
maintened), it's a very easy to use and powerfull tool (man slackpkg to know more), kind of
a front-end for pkgtool. You can find on the net contributed packages. If you'd like to
install one (at your own risks, as ususal), just download it somewhere, cd to there and
issue "installpkg some_package" command.

2. What if I can't find any usable Slackware package (neither official nor contributed) for
an app ?

In such a case you'll have to download source code from the net then:

  * preferably make a Slackware package of it (there are tools to do that) and install
    it with "installpkg my_package"
  * or use the usual ./configure [options] && make && make install method

In the latter case, remember that slackware uses mostly --prefix=/usr (not /usr/local) to
install apps.

Note: I put manually installed apps in /home/software/ or in /usr/local/ not to mess up my
system.

Requested software (should be installed before tiny ERP Server and/or Client)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For the sake of simplicity, let's suppose you did install all software developpment tools
and libraries -- mostly found in the d/ and l/ series on the installation media or on a
mirror. This include Python-2.4.3 of course, as well as libxml2-2.6.26 and libxslt-1.1.17.
If not, please do it first.

Now, let's concentrate on apps not found on Slackware official mirrors or which should be
updated (this is the case for Cairo).

Warning. I'm not sure all following apps are really needed to install Tiny ERP. All I can
say is I did install it and was able to install and launch server- and client-side Tiny ERP
apps. I mainly used informations given by tigmmi (thanks to him) on this thread : http://openerp.com/forum/viewtopic.php?t=2519.
Please complete/correct following informations as
needed.

In S/C column of table below, S mean "needed for Tiny ERP Server" C "needed for Tiny ERP
Client".\\ In How-to column of table below, install "manually" stand for: either make a
Slackware package yourself or use the "./configure etc." way (see above). In how-to column,
"as a Python package" stand for: "tar xvzf <package-name>", "cd" into the resulting
directory, "su" (to become root), "python setup.py install". \\ In any case of "manual" or
"as a Python package" installation, remember to always read README and/or INSTALL files
found in compressed archive before installing.

+-----+---------------+--------------+--------------------------------------------+------------------+--------------------+
|     |               |              |                                            |                  |                    |
|     |               |              | File needed                                |                  |                    |
| S/C | Software      | Version used |                                            | How-to install   | Notes              |
|     |               |              |                                            | it               |                    |
|     |               |              | Website to get it                          |                  |                    |
+=====+===============+==============+============================================+==================+====================+
|     |               |              |                                            |                  |                    |
|     |               |              | postgresql-8.2.0-i486-                     |                  |                    |
|     |               |              | 1kjz.tgz                                   |                  |                    |
| S   | PostgreSQL    | 8.2.0        |                                            | installpkg       | Packaged by Ken    |
|     |               |              |                                            |                  | Zalewski           |
|     |               |              | http://www.linuxpackages.net               |                  |                    |
|     |               |              |                                            |                  |                    |
+-----+---------------+--------------+--------------------------------------------+------------------+--------------------+
|     |               |              |                                            |                  |                    |
|     |               |              | ReportLab_2_0.tgz                          |                  |                    |
|     |               |              |                                            |                  |                    |
| S   | ReportLab     | 2.0          |                                            | See note below   | download           |
|     |               |              | http://www.reportlab.org/downloads.html    |                  | userguide.pdf too  |
|     |               |              |                                            |                  |                    |
|     |               |              |                                            |                  |                    |
+-----+---------------+--------------+--------------------------------------------+------------------+--------------------+
|     |               |              |                                            |                  |                    |
|     |               |              | pygtk-2.8.6-i486-                          |                  | Packaged by        |
|     |               |              | 1kan.tgz                                   |                  | kanedaa,           |
| C   | PyGTK         | 2.8.6        |                                            | installpkg       |                    |
|     |               |              |                                            |                  |                    |
|     |               |              | http://www.linuxpackages.net               |                  | http://            |
|     |               |              |                                            |                  | kaneda.bohater.net |
+-----+---------------+--------------+--------------------------------------------+------------------+--------------------+
|     |               |              |                                            |                  |                    |
|     |               |              |                                            |                  | uninstall Cairo    |
|     |               |              | cairo-1.2.6.tar.gz                         |                  | Slackware package  |
|     |               |              |                                            |                  | first if need be   |
| C   | Cairo         | 1.2.6        |                                            | manually         |                    |
|     |               |              | http://cairographics.org/releases/         |                  |                    |
|     |               |              |                                            |                  |(slackpkg remove    |
|     |               |              |                                            |                  | cairo or removepkg |
|     |               |              |                                            |                  | cairo-1.0.4)       |
+-----+---------------+--------------+--------------------------------------------+------------------+--------------------+
|     |               |              |                                            |                  |                    |
|     |               |              | pycairo-1.2.6.tar.gz                       |                  |                    |
|     |               |              |                                            |                  | Install Cairo      |
| C   | PyCairo       | 1.2.6        |                                            | manually or as a | first and see      |
|     |               |              | http://cairographics.org/releases/         | Python package   | INSTALL file       |
|     |               |              |                                            |                  |                    |
|     |               |              |                                            |                  |                    |
+-----+---------------+--------------+--------------------------------------------+------------------+--------------------+
|     |               |              |                                            |                  |                    |
|     |               |              | egenix-mx-base-                            |                  |                    |
|     | eGenix.com mx |              | 2.0.6.tar.gz                               | as a Python      |                    |
| S   | base          | 2.0.6        |                                            | package          |                    |
|     |               |              |                                            |                  |                    |
|     |               |              | http://www.egenix.com/                     |                  |                    |
+-----+---------------+--------------+--------------------------------------------+------------------+--------------------+
|     |               |              |                                            |                  |                    |
|     |               |              | psycopg-1.1.21.tar.gz                      |                  |                    |
|     |               |              |                                            |                  | See note below     |
| S   | Psycopg       | 1.1.21       |                                            | manually         | before installing  |
|     |               |              | http://initd.org/tracker/psycopg           |                  |                    |
|     |               |              |                                            |                  |                    |
+-----+---------------+--------------+--------------------------------------------+------------------+--------------------+
|     |               |              |                                            |                  |                    |
|     |               |              | Imaging-1.1.6.tar.gz                       |                  |                    |
|     |               |              |                                            |                  |                    |
| S   | Imaging       | 1.1.6        |                                            | as a Python      |                    |
|     |               |              | http://www.pythonware.com/products/pil/    | package          |                    |
|     |               |              |                                            |                  |                    |
|     |               |              |                                            |                  |                    |
+-----+---------------+--------------+--------------------------------------------+------------------+--------------------+
|     |               |              |                                            |                  |                    |
|     |               |              | pyparsing-1.4.4.tar.gz                     |                  |                    |
|     |               |              |                                            |                  |                    |
|     |               |              |                                            | as a Python      |                    |
| S   | Pyparsing     | 1.4.4        | http://pyparsing.wikispaces.co             | package          |                    |
|     |               |              | http://sourceforge.net/projects/pyparsing/ |                  |                    |
|     |               |              |                                            |                  |                    |
+-----+---------------+--------------+--------------------------------------------+------------------+--------------------+

Notes.

  * Other Slackware packages and Slackbuils are available on Italian site http://www.slacky.eu.
    AFAIK they work well and follow Slackware packaging rules &
    recommandations. There you'll find e.g. PostgreSQL, PyGTK and Imaging.
  * To install ReportLab read instructions in userguide.pdf. In brief:

::

  su
  mv ReportLab_2_0.tgz /usr/lib/python2.4/site-packages
  cd /usr/lib/python2.4/site-packages
  tar xvzf ReportLab_2_0.tgz
  rm ReportLab_2_0.tgz
  cd reportlab_2_O
  python

  import reportlab #type this in the python interpreter (prompt is >>>) then quit with Ctl-D=]

..

  * Version installed of Psycopg: 1.1, even if obsoleted by Psycopg 2 as mentionned
    here: http://initd.org/tracker/psycopg. File to downlad: psycopg-1.1.21.tar.gz.
    Version 2 should'nt be used at time of this writing (December 23, 2006).
  * Suggested options to configure Psycopg :

::

  ./configure --with-postgres-includes=/usr/include/postgresql \
  --with-postgres-libraries=/usr/lib/postgresql \
  --with-mxdatetime-includes=/usr/lib/python2.4/site-packages/mx/DateTime/mxDateTime=]

..

  * Install eGenix.com mx base before installing Psycopg, as it should be included per
    the configure options above.
  * Important After installing postgresql, check file /var/lib/pgsql/data/pg_hba.conf
    and edit it if necessary. It should contain following lines :

# "local" is for Unix domain socket connections only

::

  local all all trust

# IPv4 local connections:

::

  host all all 127.0.0.1/32 trust

in order to be able to connect to the server from the local host.

Tiny ERP Server and Client installation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

First, download and unpack the needed packages
##############################################

Download the packages from here: `Open Report`_:

.. _Open Report: http://openerp.com/component/option,com_vfm/Itemid,61/dir,stable|source/

You should get three files:

 * tinyerp-server-4.0.0.tar.gz
 * tinyerp-client-4.0.0.tar.gz
 * tinyerp-server-4.0.0-setup.patch

Then unpack compressed archives :

::

  tar xvzf tinyerp-server-4.0.0.tar.gz
  tar xvzf tinyerp-client-4.0.0.tar.gz

This will create two directories :

::

  tinyerp-server-4.0.0
  tinyerp-client-4.0.0

Then (optionnal), install the package for the server
####################################################

Note: I must admit I did'nt do that at first.

Patch then run setup.py script included in tinyerp-server-4.0.0 directory:

::

  cd to/that/directory
  mv ../tinyerp-server-4.0.0-setup.patch .
  patch -p1 <tinyerp-server-4.0.0-setup.patch"
  su
  python setup.py install

It mainly install tinyerp-server as a package into /usr/lib/python2.4/site-packages/
directory \\

Secondarily, it write in tinyerp-server-4.0.0 directory a startup script called tinyererp-
server whose content follows: ::

  #!/bin/sh
  cd /usr/lib/python2.4/site-packages/tinyerp-server
  exec /usr/bin/python ./tinyerp-server.py $@

You could use this script to start the server when you boot Slackware. E.g. rename it
rc.tinyerp-server, make it executable, put it in /etc/rc.d and execute it from /etc/rc.d/
rc.local. Obviously you should have started posgresql first (this will be the case if you
have made executable /etc/rc.d/rc.postgresql script installed by the postgresql package)

Now, create a database and user
###############################

If you are going to connect yourself locally I suggest you use your Linux user name. The
name suggested for the database is 'terp' which should be owned by the user you created.

See :ref:`setup-a-postgresql-user-and-database-link` in this manual for details.

Let's start the server
######################

Remember : PostgresSQL should be running before you start the server

Start the server under the same identity as the user you created in PostgreSQL

Either use aforementioned startup script, or issue following commands: ::

  cd /wherever_it_is/tinyerp-server/bin
  ./tinyerp-server.py

First time you start the server, it will populate the 'terp' database with needed tables.

Eventually, start the client
############################

::

  cd /wherever_it_is/tinyerp-client/bin
  ./tinyerp-client.py

..

  * Answer the greetings questions,
  * find File/Connect in the menu,
  * login as user demo, password demo or as user admin, password admin.

Didier Spaier

