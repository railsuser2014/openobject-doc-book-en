
Installation of the OpenERP Server on Windows
"""""""""""""""""""""""""""""""""""""""""""""

The server installation works on Windows 2000, 2003 and XP. It doesn't work on
Windows 98 or ME; Because there are some issues with PostgreSQL 8.

Dependencies
^^^^^^^^^^^^

Download, unarchive and install:

  * **Python 2.5**

    - http://www.python.org/download/

  * **libxml 2.6.30,(<-libxslt) for python 2.5**

    - http://users.skynet.be/sbi/libxml-python/
    - File: old libxml2-python-2.6.30.win32-py2.5.exe

  * **eGenix.com mx BASE Package - Windows Installer for Python 2.5**

    - File: egenix-mx-base-3.0.0.win32-py2.5.msi
    - http://www.egenix.com/products/python/mxBase/  (scroll down till section 'Downloads' and choose file)

  * **PIL 1.1.6 - Python Imaging Library**

    - File: PIL-1.1.6.win32-py2.5.exe
    - http://www.pythonware.com/products/pil/


  * **Psycopg 1.1.21**

    - File: win-psycopg25.zip
    - http://stickpeople.com/projects/python/win-psycopg/#Version1
    - Note: tinyserver is not working with psycopg 2!!

  * **Python parsing module 1.4**

    - http://sourceforge.net/project/showfiles.php?group_id=97203&package_id=104017

  * **Open Source ReportLab Toolkit/Library 2.1**

    - File: ReportLab_2_1.zip
    - http://www.reportlab.org/downloads.html

      + **Note**: 09/09/2008 The ReportLab Toolkit Version 1 is working well !

  * **PyTZ - Python Time Zone Library 2006p**

    - File: old pytz-2006p.zip
    - https://launchpad.net/pytz

      + http://pypi.python.org/pypi/pytz

  * **PostgreSQL 8.2**

    - http://www.postgresql.org/ftp/binary/

      + File: old postgresql-8.2.96-2.zip
      + Note: tinyserver version 4.2.2 is not working with postgresql 8.3!!

  * **AFPL PostScript** (for printing with workflow plug-in to pdf file)

    - http://pages.cs.wisc.edu/~ghost/

      + File: old gs851w32.exe

  * **matplotlib 0.91-2**

    - http://sourceforge.net/project/showfiles.php?group_id=80706
    - File: old matplotlib-0.91.2.win32-py2.5.exe

  * **GTK+/Win32 Development Environment 2**

    - File: gtk 2
    - http://gladewin32.sourceforge.net

      + http://downloads.sourceforge.net/gladewin32/gtk-dev-2.12.9-win32-2.exe
      + old gtk-dev-2.10.11-win32-1.exe

  * **pygtk 2 - Python Bindings for the GTK Widget Set**

    - http://www.pygtk.org/downloads.html
    - File: old pygtk-2.10.6-1.win32-py2.5.exe

  * **graphviz 2**

    - http://www.graphviz.org/pub/graphviz
    - File: old graphviz-2.10.exe

For tinyerp-server 4.2.3 install :

  * **pyxml**

    - http://openerp.com/forum/topic6239.html?highlight=pyxml

  * **numpy pour pyhton 2.5**

    - http://numpy.scipy.org/

The above mentioned versions were the most up-to-date ones on 20.02.2008. There
may be more recent versions available, so feel free to search for the packages
listed and download the latest stable release.

Install Python first by executing the .msi file; it's necessary for some
packages. It's helpful to add the Python installation directory to your PATH
environment variable. To do so rightclick on 'My Computer' -> 'Properties' ->
Tab 'Advanced' -> 'Environment Variables'. Have a look at the frame 'System
Variables' and search for 'path'. Click on 'Edit' and enter the path to python
(e.g. 'C:\Python25;').

To install libxml2-python, the eGenix mx Base package, pygtk, PIL, pyparsing,
GTK+, graphviz and matplotlib just run the executables. They should
automatically install the Lib\site-packages\ directory where Python is
installed.

Unarchive the Psycopg file to the Python "site-packages" directory
(default:"C:\Python25\Lib\site-packages"). The files should remain in a folder,
looking something like "C:\Python25\Lib\site-packages\win-psycopg25". Move the
psycopg.pyd and libpq.dll files from that folder to the [=DLLs=] directory
(default: "C:\Python25\[=DLLs=]\").

To install ReportLab and py-tz unarchive their files to appropriate
installation directories and open a command prompt. Navigate in the command
prompt to their respective unarchived directories and execute::

  C:\''unarchive directory''> python setup.py install

GTK+, graphviz, and PostgreSQL can be installed at any time before the OpenERP server
is initialized. To install GTK+ and graphviz run the executables.

PostgreSQL Installation
^^^^^^^^^^^^^^^^^^^^^^^

Install PostgreSQL 8 by executing the postgresql-8.0.msi file (the other .msi
file must also be present).

Make sure installation of Postrgres 8.2.x is on C: drive as it does not like to
initialize the service user when it is installed on other drives!

There are two sets of user names and passwords that will be important later on.
The first set is requested when you get to Service configuration during the
installation wizard. This is where a service account is setup for running the
PostgreSQL database server. You may not need this login in the future but
record it in case you do.

[[Image:pgsql_install.service_configuration.png]]

At the Initialize database cluster screen, you will need to input a Superuser
name and password. This login is for the internal database and will be
necessary to create your database for your OpenERP server.

[[Image:pgsql_install.init_cluster.admin_login_def.png]]

The default options for all the other screens should work just fine. Add the
bin folder of your PostgreSQL installation directory to your PATH environment
variable to use createdb without having to specify its location.

To create a database, simply use the tinyerp-client. On first start, cancel the
login window, go to 'File' : 'Database' : 'New database'. When you have entered
everything in the dialog window, click ok. If the client freezes, check the
terminal. Might be you have to enter the postgres user password on command
line, if it's asked for.

===All of the following instructions are not out of date for tinyerp-server (09/09/2008), may be are out of date for openerp :===

In manual mode in a cmd window you can create a database directory, start/stop
the postgresql, and create any number of database.  For initialization of a new
data directory for postgresql use ``initdb``, with ``-D`` option command from
postgresql bin directory.

To start postgresql use pg_ctl in same directory.

To create a database for your OpenERP server, open a command prompt (cmd
window) and use this manual command (the current working directory doesn't
matter if you have in PATH the postgresql bin directory)::

  createdb <your_tinyerp_databasename> --encoding=UNICODE --username=<your_database_admin_username>

or::

  createdb <your_tinyerp_databasename> -E UNICODE -U  <your_database_admin_username>

::

  Sample command prompt:
  <code bash>
  C:\terp\testserv>createdb terp --encoding=UNICODE --username postgresadmin
  Password: <enter password again>
  CREATE DATABASE

  C:\terp\testserv>


Your output may differ, and if you're prompted a second time for the password
just input it again. You can try the same command again, and after entering the
password it would display this error::

  createdb: database creation failed: ERROR: database "terp" already exists

Now you are ready to setup the OpenERP server.

OpenERP Server Installation
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Download and unarchive the latest tinyerp/Openerp server archive file  to the
directory you intend to use for installation (example: "C:\terp\"):

''( Note: winzip doesn't work, use unrar, 7zip --> www.7-zip.org or gzip + tar --> www.cygwin.com )''

''Note:'' Don't use brackets in path name (eg 'D:\[4]_dev\tinyerp-server-4.0.0-rc1\bin\'). This screws up glob.glob module (actually the Regex function).

**For TinyERP Server 3.1.1 - 4.2.3**

  * tinyerp-server-3.1.1.tar.gz to tinyerp-server-4.2.3.tar.gz
  * http://www.openerp.com/download.php

Note: No modifications to the source code are necessary as of version 2.1.0.

When you run Openerp-server for the first time it will initialize the database.
You don't run the setup.py file, but rather, the Openerp-server file (no
extension) located in the bin directory.

There are a few command line options added in v2.1.0 that specify the database
name, database username, and database password::

  -d <db name>, --database=<db name>
  -r <db user>, --user=<db user>
  -w <db password>, --password=<db password>

You can save these settings to a configuration file (recommended) by using "``-s``"
or "``--save``", necessary only once.

Run::

  python tinyerp_server.py --help

or::

  python Openerp-server --help

for more command line options.

Navigate to the bin directory (example: "c:\terp\tinyerp-server-2.1.1\bin\") and execute this command:

To start the tinyerp-server do one of cmd command::

  python tinyerp-server -d <db name> -r <db user> -w <db password> -s

for openerp may be::

  python Openerp-server -d <db name> -r <db user> -w <db password> -s

Or::

  python Openerp-server --database=<db name> --user=<db user>
                       --password=<db password> --save

Sample command usage::

  python tinyerp-server -d terp -r postgresadmin -w your_pass -s

Starting with the version 2.1.2, the command line options was changed: ::

  -d or --database      to specify the database name
  -r or --db_user       to specify the database user name
  -w or --db_password   to specify the database password
        --db_host       to specify the database host
        --db_port       to specify the database port

The first time you run this it will initialize the OpenERP server and its
PostgreSQL database. In the future, you may force the server to initialize by
using the "-i all" or "--init=all" command line option.

After running tinyerp-server.py or Openerp-server, you can confirm that your
server is running by the message::

  INFO:web-services:the server is running, waiting for connections...

The server is now running within this command prompt, so don't close it. To
shutdown the OpenERP server instance, simply close the command prompt with
Ctrl-Break.

In the future you can run your server from the command prompt using the same
command, or if you used the save option ("-s" or "--save") by simply entering::

  python tinyerp-server.py

or::

  python Openerp-server

Two accounts are created by default:

  # login: admin

    ##   password : admin

  # login: demo

    ##   password : demo

Connecting the OpenERP Client Locally
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The OpenERP clients version 2.0.11 or later should work without any further
modifications when running on the same machine as the server.

Do in a cmd window in the bin client directory::

  >python tinyerp-client.py

It has been suggested that for older versions you will need to modify the tdb = psycopg.connect(....) line in .\tinyerp-server-2.1.1\bin\sql_db.py to appear like:

.. code-block:: python

  tdb = psycopg.connect('dbname=%s user=%s password=%s' %
  (tools.config['database'],tools.config['user'], tools.config['password']),
  serialize=0)

.. 

This would properly define the OpenERP server's connection to the PostgreSQL
database, but it should be unnecessary for the most recent version, at least.

Connecting the tinyerp/OpenERP Client Remotely
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To connect OpenERP clients from other computers on the network, you will need
to specify the interface option to change the server's default IP address from
localhost (127.0.0.1) to the appropriate IP. You can do this using the
following option: ``--interface=<server IP address>``

Sample command usage::

  python tinyerp-server --interface=192.168.1.1 -s

Again, the "-s" or "--save" option will save your interface setting to a configuration file so it will be unnecessary thereafter unless it must be changed.

If you wish to use a different port, you can change it from the default (8069) to one you specify by using this option::

  -p <port #>

Or::

  --port=<port #>

Sample command usage::

  python tinyerp-server --interface=192.168.1.1 --port=8070 -s

When running the client, change the Server and Port parameters as necessary. If
you are using DNS to route your connections that will work fine also.

To print workflow to pdf file you need to modify the source file
print_instance_py from directory **tinyerp_server\bin\addons\base\ir\workflow**::

  C:\tiny_folder\tinyerp-server-3.1.0\bin\addons\base\ir\workflow\print_instance_py

the class *report_graph_instance* like this:

.. code-block:: python

  class report_graph_instance(object):
      def __init__(self, uid, ids, datas):
          try:
              import pydot
          except Exception, e:
              print 'Import Error for pydot, you will not be able to render workflows'
              print 'Consider Installing PyDot or dependencies: http://dkbza.org/pydot.html'
              raise e

          self.done = False
          cr = sql_db.db.cursor()
          print 'datas:'
          print datas['model']
          cr.execute('select * from wkf where osv=%s limit 1', (datas['model'],))
          wkfinfo = cr.dictfetchone()
          print 'wkfinfo:'
          print wkfinfo
          cr.execute('select id from wkf_instance where res_id=%d and wkf_id=%d order by state limit 1', (datas['id'], wkfinfo['id']))
          inst_id = cr.fetchone()[0]
          print 'inst_id:'
          print inst_id
          graph = pydot.Dot(fontsize = 16, label = "\\n\\nWorkflow: %s\\n OSV: %s"% (wkfinfo['name'], wkfinfo['osv']))
          print 'datas.get:'
          print datas.get('nested', False)
          graph_instance_get(cr, graph, inst_id, datas.get('nested', False))
          if sys.platform == 'win32':
              print 'win32-1'
              graph.write_ps('c:\\tmp\\terp_graph.ps', prog='dot')
              print 'win32-2'
              os.system('C:\\ghostscript_folder\\gs8.51\\lib\\ps2pdf c:\\tmp\\terp_graph.ps c:\\tmp\\terp_graph.pdf')
              print 'win32-3'
              #graph.write_jpg(str(inst_id)+'.jpg', prog='dot')
              #os.system('mspaint '+str(inst_id)+'.jpg')
              self.result = file('c:\\tmp\\terp_graph.pdf', 'rb+').read()
              print 'win32-4'
          else:
              graph.write_ps('/tmp/terp_graph.ps', prog='dot')
              os.system('/usr/bin/ps2pdf -sPAPERSIZE=a3 /tmp/terp_graph.ps /tmp/terp_graph.pdf')
              self.result = file('/tmp/terp_graph.pdf', 'rb+').read()
          cr.close()
          self.done = True

.. 


