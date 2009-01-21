
Mandriva
""""""""

2008.1
^^^^^^

After a base or full install do the following.

Get requirements

::

  # urpmi.addmedia --distrib --mirrorlist '$MIRRORLIST'
  # urpmi postgresql8.3 psycopg reportlab wget python-matplotlib python-imaging python-libxslt
  # urpmi libpython2.5-devel gcc python-lxml python-pyxml gnome-python-gtkspelllibgtkspell0
  # urpmi --auto-select --auto
  # cd /usr/src
  # mkdir openerp
  # cd openerp
  # bzr co lp:~openerp/openobject-addons/4.2
  # bzr co lp:~openerp/openobject-addons/4.2-extra-addons
  # bzr co lp:~openerp/openobject-client/4.2
  # bzr co lp:~openerp/openobject-client-web/4.2
  # bzr co lp:~openerp/openobject-server/4.2

Get Turbogears

::

  # cd /usr/src
  # wget http://www.turbogears.org/download/tgsetup.py
  # python tgsetup.py

Setup PostgreSQL

::

  # service postgresql start
  # su postgresql
  $ createuser --createdb --no-createrole --no-superuser -P openerp
   Enter password for new role:
   Enter it again:
  $ createdb -U postgres -O openerp --encoding=UNICODE openerp
  $ exit

Install Server

::

  # cd /usr/src/openerp/server
  # python setup.py install

Configure Server

::

  # vi /usr/lib/python2.5/site-packages/tinyerp-server/tools/config.py
      Note on 64 bit machines it is /usr/lib64... and the python version may vary

Install Web Client

::

  # cd /usr/src/openerp/web
  # python setup.py install

Configure Web Client

2008
^^^^

Required Packages

::

  # urpmi postgresql-server python

2007.1
^^^^^^

Required Packages

::

  # urpmi postgresql-server python

2007
^^^^

Required Packages

::

  # urpmi postgresql-server python

2006
^^^^

Required Packages

::

  # urpmi postgresql-server python

2005
^^^^

Packages Installation

  * urpmi egenix-mx-base-2.0.5-3mdk.i586.rpm libxml2-python libxslt-python postgresql
    libpython2.4-devel postgresql-server graphviz egenix-mx-base
  * sources of pyparsing (http://sourceforge.net/projects/pyparsing/)
  * sources of psycopg (http://initd.org/projects/psycopg1) -- use version 1.x
  * sources of egenix-mx-base (http://www.egenix.com/files/python/eGenix-mx-
    Extensions.html#Download-mxBASE)
  * sources of python-reportlab because there are unicodes problems with the python-
    reportlab v1.19-2 (http://www.reportlab.org/downloads.html)

Compilation of psycopg

  * urpmi postgresql-devel (installation of pgsql)
  * decompression of psycopg and of egenix-mx-date
  * go in the psycopg created

To start the compilation, you have to modify the references include in postgresql and
mxbase

  * ./configure --with-postgres-includes=/usr/include/pgsql --with-mxdatetime-
    includes=DIR/egenix-mx-base-2.0.6/mx/DateTime/mxDateTime/
  * make then make install which place the module psycopg.so in /usr/lib/python-2.4/
    site-packages

Installation of pyparsing

  * decompress pyparsing archival
  * python setup.py install

Installation of python-reportlab

  * decompress the archival
  * cp -R reportlab_1_20/reportlab /usr/lib/python2.4/site-packages/ (pour la version
    1.20)

Starting and setting up PostgreSQL

::

  service postgresql start
  chkconfig --add postgresql

When the installations are done, you have to create a database, see
:ref:`setup-a-postgresql-user-and-database-link` for details.

Files server Moves

  * cp -R TinyERP /usr/local/src/

Links Creation

  * ln -s /usr/local/src/TinyERP/server/bin/tinyerp_server.py /usr/bin/tinyerp_server

French Import on the serveur

  * su -c "tinyerp_server --i18n-import=PATH/french_fr-2_1.csv -lFR" XXX

French accounting Import

  * fichier server/bin/addons/account.__terp__.py
  * write "datas/account_pcg_france.xml"
  * then, update the plan by starting the server with "--update=all"

