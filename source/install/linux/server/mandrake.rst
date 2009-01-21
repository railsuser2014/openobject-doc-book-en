
Mandrake
""""""""

Mandrake 10.1 (Mandiva 3 CD) Dependences
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Packages Installation with the control center
#############################################

  * libpython2.3-devel-2.3.4-6.1.101mdk
  * libxml2-python-2.6.13-1.1.101mdk
  * libxslt-python-1.1.10-1mdk
  * python-2.3.4-6.1.101mdk
  * python-imaging-1.1.4-6mdk
  * python-reportlab-1.19.1mdk
  * postgresql-7.4.5-4.2.101mdk
  * postgresql-devel-7.4.5-4.2.101mdk
  * postgresql-contrib-7.4.5-4.2.101mdk
  * egenix-mx-base-2.0.1.1mdk

Download the package psycopg-1.1.18.tar.gz
##########################################

  * Decompress :
  * cd psycopg-1.1.18
  * su
  * ./configure--with-postgres-includes=/usr/include/pgsq-with-mxdatetime-
  * includes=/usr/lib/python2.3/site-packages/mx/DateTime/mxDateTime
  * make
  * make install

Download pyparsing_1.2.2.orig.tar.gz
####################################

  * Decompress :
  * cd pyparsing-1.2.2
  * su
  * python setup.py install

Install
#######

  * perl-GraphViz-1.8-4mdk

Configuration
^^^^^^^^^^^^^

When the installations are done, you have to create a database, see
:ref:`setup-a-postgresql-user-and-database-link` for details.

Then, you can start Open ERP.

