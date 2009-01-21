
TinyERP Version 3.3.0 on SuSE Linux 10.1
""""""""""""""""""""""""""""""""""""""""

01. Install SuSE 10.1 from SuSE-DVD

   * Standard-Installation (suggested Software)
      (install Python 2.4.3(download from http://download.opensuse.org) and Acrobat Reader 7.0)
      (works with Python 2.5.x on SuSE 10.2 and 10.3 RC1)
      (use kpdf or evince instead of Acrobat Reader for performance reasons)

02. Additional packages and dependencies from SuSE-DVD installed

   * bison
   * checkinstall
   * findutils-locate
   * flex
   * gcc
   * gcc-c++
   * gd

03. Additional packages and dependencies for TinyERP from SuSE-DVD installed

   * graphviz
   * libpqxx
   * libpqxx-devel (Download from [1])
   * libxml2-python
   * libxslt-python
   * postgresql
   * postgresql-devel
   * postgresql-contrib
   * postgrespl-libs
   * postgresql-pl
   * postgresql-server
   * python-devel
   * python-egenix-mx-base (download from [1])
   * python-gtk
   * python-idle
   * python-imaging
   * python-openssl (optionally for secure conection)

04. The linux-OS-user "postgres" was created with the installation of postgresql

05. Change user

   * su

06. Start Postgresql (with first start postgresql-database-structure will be created)

   * rcpostgresql start

07. Edit file "pg_hba.conf"

   * cd /var/lib/pgsql/data
   * add/activate following lines in "pg_hba.conf"
   * local all all trust
   * host all all 127.0.0.1 255.255.255.255 trust

08. Create a database and user, see Setup a Postgresql user and database for details.

09. Change user

   * su

10. Create directory

   * mkdir /usr/down (or as you prefer)

11. Download to /usr/down

   * ReportLab_2_0.tgz http://www.reportlab.org/downloads.html
   * psycopg-1.1.21.tar.gz http://initd.org/tracker/psycopg/wiki/PsycopgOne

::

   ./configure --with-postgres-includes=/usr/include/pgsql --with-mxdatetime-includes=/
   usr/local/lib/python2.5/site-packages/mx/DateTime/mxDateTime

Note: You may need the mxDateTime site-package. Download it from here. Make sure you
scroll down to find your distribution.

   * pyparsing-1.4.2.tar.gz http://sourceforge.net/projects/pyparsing/
   * for SuSE10.3 RC1: Python Time Zone Library PyTZ http://sourceforge.net/project/showfiles.php?group_id=79122&package_id=80455&release_id=469616
   * tinyerp-client-3.3.0.tar.gz
   * tinyerp-server-3.3.0.tar.gz

12. Install pyparsing

   * cd /usr/down
   * tar xvfz pyparsing-1.4.2.tar.gz
   * cd pyparsing-1.4.2
   * python setup.py install

13. Install reportlab

   * cd /usr/down
   * tar xvfz ReportLab_2_0.tgz
   * cd /ReportLab-2_0/reportlab
   * python setup.py install

14. Install psycopg

   * cd /usr/down
   * tar xvfz psycopg-1.1.21.tar.gz
   * cd psycopg-1.1.21
   * ::

       ./configure --with-postgres-includes=/usr/include/pgsql \
       --with-postgres-libraries=/usr/lib/postgresql \
       --with-mxdatetime-includes=/usr/lib/python2.4/site-packages/mx/DateTime/mxDateTime
   * make
   * make install

15. Install TinyERP 3.3.0 - or whatever version number is current

   * Downloads to /usr/down
   * tinyerp-client-3.3.0.tar.gz
   * tinyerp-server-3.3.0.tar.gz
   * tar xvfz tinyerp-client-3.3.0.tar.gz
   * tar xvfz tinyerp-server-3.3.0.tar.gz

16. Start TinyERP Server 3.3.0

   * cd /usr/down/tinyerp-server-3.3.0/bin
   * python tinyerp-server.py -d terp -r terp -w tinyerp
      (-w tinyerp when entered as password in step 08, otherwise the password you
      entered)

17. Start TinyERP Client 3.3.0

   * open new console (normal user)
   * cd /usr/down/tinyerp-client-3.3.0/bin
   * python tinyerp-client.py

18. The user for testing

   * login : demo
   * pass : demo

19. eTiny installation (WEB-Interface) (SuSE 10.3 RC1)

   * su
   * easy_install TurboGears
   * easy_install matplotlib
   * exit
   * cd /usr/down
   * download eTiny (Version)
   * tar xzf eTiny (Version).tar.gz
   * cd /usr/down/eTiny (Version)
   * ./start-tinyerp.py
   * login http://servername or IP-number:8080

   * select architecture + CD / DVD
      or
   * Internet Installation Repository for single packages

