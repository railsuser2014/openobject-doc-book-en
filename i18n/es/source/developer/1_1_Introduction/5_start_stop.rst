
.. i18n: OpenERP Server and Web Client - Start/Stop
.. i18n: ==========================================

OpenERP Server and Web Client - Start/Stop
==========================================

.. i18n: OpenERP 4.2
.. i18n: -----------

OpenERP 4.2
-----------

.. i18n: First check that all the required dependencies are installed. Then create the terp database. You have to make sure that your user has the correct credentials to create databases with PostgreSQL. For more information on this subject please refer to the PostgreSQL manual.::
.. i18n: 
.. i18n: 	$ createdb terp --encoding=unicode

First check that all the required dependencies are installed. Then create the terp database. You have to make sure that your user has the correct credentials to create databases with PostgreSQL. For more information on this subject please refer to the PostgreSQL manual.::

	$ createdb terp --encoding=unicode

.. i18n: Once the database created, you can start OpenERP. The content of the database will automatically be created at the first start.::
.. i18n: 
.. i18n: 	$ ./tinyerp-server.py

Once the database created, you can start OpenERP. The content of the database will automatically be created at the first start.::

	$ ./tinyerp-server.py

.. i18n: OpenERP 5.0 and above
.. i18n: ---------------------

OpenERP 5.0 and above
---------------------

.. i18n:     * Check that all the required dependencies are installed.
.. i18n:     * Make sure you are logged on as a user that has catalog admin rights in PostgreSQL. Refer to the PostgreSQL manual for more info on this.
.. i18n:     * Start the OpenERP Server 

    * Check that all the required dependencies are installed.
    * Make sure you are logged on as a user that has catalog admin rights in PostgreSQL. Refer to the PostgreSQL manual for more info on this.
    * Start the OpenERP Server 

.. i18n: ::
.. i18n: 
.. i18n: 	./openerp-server.py

::

	./openerp-server.py

.. i18n:     * Finally connect to the server with the GTK Client or eTiny and use the Create Database option to create your database 

    * Finally connect to the server with the GTK Client or eTiny and use the Create Database option to create your database 
