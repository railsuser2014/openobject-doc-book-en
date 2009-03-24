=========================
Upgrading Server, Modules 
=========================

The upgrade from version to version is automatic and doesn't need any special scripting on the user's part. In fact, the server is able to automatically rebuild the database and the data from a previously installed version.

The tables are rebuilt from the current module definitions. To rebuild the tables, the server uses the definition of the objects and adds / modifies database fields as necessary.

To invoke a database upgrade after installing a new verion, you need to start the server with the **--update=all** argument :

::
 
	tinyerp-server.py --update=all

You can also only upgrade specific modules, for example:

::

	tinyerp-server.py --update=account,base

The database is rebuilt according to information provided in XML files and Python Classes. For more information on these functionalities, go to the section `XML files <http://openobject.com/wiki/index.php/Developers:Developper%27s_Book/The_modules/ModulesFilesDirs/ModulesFilesDirsXML>`_ and `Defining Objects <http://openobject.com/wiki/index.php/Developers:Developper%27s_Book/Objects/ObjectsDefine>`_.

You can also execute the server with **--init=all**. The server will then rebuild the database according to the existing XML files on the system, delete all existing data and return Open ERP to its basic configuration. 
    

    
    

