
Debian
""""""

Install dependencies
^^^^^^^^^^^^^^^^^^^^

Distribution Lenny
##################

In Lenny, only PostgreSQL 8.3 is available, TinyERP 4.2.3.2 and later now works with
PostgreSQL 8.3,::

  $ sudo apt-get install postgresql

Pythons components::

  $ sudo apt-get install python-xml python-libxml2 python-libxslt1 python-psycopg
  python-imaging python-pyparsing
    python-reportlab graphviz python-tz python-pyopenssl gs-gpl python-matplotlib

Distribution Etch
#################

Database server::

  apt-get install postgresql-8.1

Python components::

  apt-get install python2.4 python2.4-psycopg python-libxml2 python2.4-xml python2.4-
  libxslt1 python-reportlab python2.4-imaging python-pyparsing graphviz python-tz
  python-pyopenssl gs-gpl python-matplotlib

To see another installation manual: http://leoliao1108.blogspot.com/2007/11/install-tinyerp-42-server-on-debian-40.html

Distribution Sarge
##################

Database server::

  apt-get install postgresql postgresql-client

Python components::

  apt-get install python2.3 python2.3-psycopg python2.3-libxml2 python2.3-xml
  python2.3-libxslt1 python2.3-reportlab
  python2.3-imaging python2.3-pyparsing graphviz python-tz

Database creation
^^^^^^^^^^^^^^^^^

When the installations are done, you have to create a database, see Setup a PostgreSQL
User and Database for details.

Server installation
^^^^^^^^^^^^^^^^^^^

Then download file to OpenERP Download section. The OpenERP server must be decompressed
and started;::

  tar xzvf tinyerp_server-v...tar.gz
  cd server/bin
  tinyerp_server.py

.. note:: on first initialisation you have to run with the 'tinyerp_server.py --init=all' switch

Binary packages
^^^^^^^^^^^^^^^

There are also a binary packages of OpenERP, see: :ref:`from-packages`

Miscelaneous
^^^^^^^^^^^^

For further information, you might want to check out the Ubuntu install documentation,
which has some additional information about databases creation


