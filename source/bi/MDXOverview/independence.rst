Independent yet Integrated to OpenERP
-------------------------------------

MDXAlchemy engine is totally independent of OpenERP. It does not rely on OpenERP modules for its functionality. 
Yet being so diversified from OpenERP, it is fully integrated to OpenERP.

MDXAlchemy can be installed/intergrated as an internal module of OpenERP and it makes itself ready to assist OpenERP.

It is made of two major components, a cube engine and SQL Alchemy. It uses SQL Alchemy for connecting to the database and cube engine processes the data to form the cube for the user.


Supported Databases
-------------------

OpenObject BI takes care of independent database functionality.

It supports connectivity with most of the leading Databases programs.

Just a compatible Dialect and valid connection parameters is all that is needed to use a database.

The Dialect is used to describe how to talk to a specific kind of database. Dialects are included with SQLAlchemy for SQLite, Postgres, MySQL, MS-SQL, Firebird, Informix, and Oracle; these can be described as Python modules present in the sqlalchemy.databases package. Each dialect requires the appropriate DBAPI drivers to be installed separately.

Downloads for each DBAPI to connect to supported Databases are as follows:


* Postgres: psycopg2_

* SQLite  : pysqlite_

* MySQL   : MySQLDB_

* Oracle  : cx_Oracle_

* MS-SQL  : pyodbc_  (recommended) adodbapi pymssql

* Firebird:  kinterbasdb_

* Informix:  informixdb_


.. _psycopg2: http://www.initd.org/tracker/psycopg/wiki/PsycopgTwo

.. _pysqlite: http://initd.org/tracker/pysqlite

.. _MySQLDB: http://sourceforge.net/projects/mysql-python

.. _cx_Oracle: http://www.cxtools.net/default.aspx?nav=home

.. _pyodbc: http://pyodbc.sourceforge.net

.. _kinterbasdb: http://kinterbasdb.sourceforge.net/

.. _informixdb: http://informixdb.sourceforge.net/


