
CentOS
""""""

Centos http://www.centos.org/ is based on RedHat

CentOS is free and its packages aim to be 100% RedHat compliant.

Installation OpenERP on CentOS is quite easy because the packages in this distribution are
up to date.

I read the Debian howto and had to do the following :

Automatic installation of packages from a CentOS download mirror you choose (with system-
install-packages when downloading).

  * PyXML
  * libxml2
  * postgresql
  * postgresql-devel
  * python-devel
  * libxslt-python
  * graphviz (from www.graphviz.org site)

Psycopg
^^^^^^^

Download source tar.gz and compile as usual. don't forget to configure with this parameter::

  $ ./configure with-postgres-includes = /usr/include/pgsql/server
  $ make
  $ make install

NOTE: It appears you need version 1 with postgresql8 on centos5 and it doesn't build
cleanly. RPMS can be found at

http://centos.karan.org/el5/extras/testing/i386/RPMS/python-psycopg-1.1.21-7.el5.kb.i386.rpm

or

http://centos.karan.org/el5/extras/testing/x86_64/RPMS/python-psycopg-1.1.21-7.el5.kb.x86_64.rpm

If you want to use psycopg2, you'll need to following these instructions to get it to work:

First, download the psycopg2 package.::

  $ cd /usr/src/
  $ wget http://www.initd.org/pub/software/psycopg/psycopg2-latest.tar.gz
  $ tar -xzvf psycopg2-latest.tar.gz
  $ rm -rf psycopg2-latest.tar.gz
  $ cd psycopg2
  $ python setup.py install

This last command will install the psycopg2 program in the correct python directory based on
where python packages are usually kept. On my (Haulbag's) system, it installed it to /usr/
lib/python2.3/site-packages/psycopg2 and, unfortunately, the OpenERP Server installation
didn't know where to find it. If that happens to you, just copy the /usr/lib/python2.3/site-
packages/psycopg2 to /usr/lib/python2.3/site-packages/psycopg like this: ::

  $ cp -a /usr/lib/python2.3/site-packages/psycopg2 /usr/lib/python2.3/site-packages/
  psycopg

Now, OpenERP will find it where it is expecting it and will compile and install normally.

Reportlab
^^^^^^^^^

Check python path::

  $ python -c 'import sys ; print sys.path'

You should have /usr/lib/python2.3 in this path.

From http://reportlab.org/downloads.html, download the sources, put the "reportlab" folder
into /usr/lib/python2.3/site-packages.

In the same directory (site-packages), write a reportlab.pth file containing the string
reportlab.

Postgresql
^^^^^^^^^^

You have to create a database, see :ref:`setup-a-postgresql-user-and-database-link` for details.

With this, TERP will have to be started by user Open ERP

Python Imaging Library (PIL)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

from the site www.pythonware.com download archive "imaging" Uncompress, enter the new
directory and install with : ::

  $ python setup.py install

Pyparsing
^^^^^^^^^

From http://sourceforge.net/projects/pyparsing/, download archive.

Uncompress, enter the new directory and install with : ::

  $ python setup.py install

Download and Install OpenERP Server
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The process goes something like this (the example is for downloading the 4.1.1 version):

  $ cd /usr/src
  $ wget http://www.tinyerp.com/download/development/source/tinyerp-server-4.1.1.tar.gz
  $ tar -xzvf tinyerp-server-4.1.1.tar.gz
  $ rm -rf tinyerp-server-4.1.1.tar.gz
  $ cd tinyerp-server-4.1.1
  $ python setup.py install

This will build and copy all of the files to the correct locations. Note the final output of
the build process to see where things got installed so you can start the server. For my
system, I (Haulbag) found the executable by doing a ::

  $ updatedb
  $ locate tinyerp

and found that the executable was /usr/lib/python2.3/site-packages/tinyerp-server/
tinyerp_server.py

Run the server
^^^^^^^^^^^^^^

Go where you installed the server, for example:

  $ cd /usr/local/2.0.7/server/bin/
  $ su tinyerp
  $ ./tinyerp-server.py

NOTE on CentOS5, September 2007
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Must install also Egenix MX Python extensions (yum install mx)

Psycopg2 gives problems: ::

  psycopg.register_type(psycopg.new_type((1082,), "date", lambda x:x))

AttributeError: 'module' object has no attribute 'register_type'

Better install pyscopg using yum install python-psycopg

And finaly, a dependency needed for tinyerp-server: install http://kent.dl.sourceforge.net/
sourceforge/pytz/pytz-2006p.tar.gz (uncompress, and then python setup.py install as usual)

NOTE on CentOS 5.2, September 2008
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Japan Shah has a good page on preparing for openerp here: http://openerp-on-
centos.blogspot.com/ There is a bash file of the same lines here: http://
cdnpayroll.gemlog.ca/centos52_openerp.txt

If you are not able to install python-psycopg try this,

Enable epel Repository by::

  rpm -Uvh http://download.fedora.redhat.com/pub/epel/5/i386/epel-release-5-2.noarch.rpm

and then try::

  yum install python-psycopg.i386

