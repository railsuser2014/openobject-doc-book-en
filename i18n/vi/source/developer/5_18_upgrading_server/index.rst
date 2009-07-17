
.. i18n: =========================
.. i18n: Upgrading Server, Modules 
.. i18n: =========================

=========================
Upgrading Server, Modules 
=========================

.. i18n: The upgrade from version to version is automatic and doesn't need any special
.. i18n: scripting on the user's part. In fact, the server is able to automatically
.. i18n: rebuild the database and the data from a previously installed version.

The upgrade from version to version is automatic and doesn't need any special
scripting on the user's part. In fact, the server is able to automatically
rebuild the database and the data from a previously installed version.

.. i18n: The tables are rebuilt from the current module definitions. To rebuild the
.. i18n: tables, the server uses the definition of the objects and adds / modifies
.. i18n: database fields as necessary.

The tables are rebuilt from the current module definitions. To rebuild the
tables, the server uses the definition of the objects and adds / modifies
database fields as necessary.

.. i18n: To invoke a database upgrade after installing a new verion, you need to start
.. i18n: the server with the **--update=all** argument :

To invoke a database upgrade after installing a new verion, you need to start
the server with the **--update=all** argument :

.. i18n: ::
.. i18n: 
.. i18n: 	openerp-server.py --update=all

::

	openerp-server.py --update=all

.. i18n: You can also only upgrade specific modules, for example:

You can also only upgrade specific modules, for example:

.. i18n: ::
.. i18n: 
.. i18n: 	openerp-server.py --update=account,base

::

	openerp-server.py --update=account,base

.. i18n: The database is rebuilt according to information provided in XML files and
.. i18n: Python Classes. For more information on these functionalities, go to the
.. i18n: section `XML files
.. i18n: <http://openobject.com/wiki/index.php/Developers:Developper%27s_Book/The_modules/ModulesFilesDirs/ModulesFilesDirsXML>`_
.. i18n: and `Defining Objects
.. i18n: <http://openobject.com/wiki/index.php/Developers:Developper%27s_Book/Objects/ObjectsDefine>`_.

The database is rebuilt according to information provided in XML files and
Python Classes. For more information on these functionalities, go to the
section `XML files
<http://openobject.com/wiki/index.php/Developers:Developper%27s_Book/The_modules/ModulesFilesDirs/ModulesFilesDirsXML>`_
and `Defining Objects
<http://openobject.com/wiki/index.php/Developers:Developper%27s_Book/Objects/ObjectsDefine>`_.

.. i18n: You can also execute the server with **--init=all**. The server will then
.. i18n: rebuild the database according to the existing XML files on the system, delete
.. i18n: all existing data and return Open ERP to its basic configuration.

You can also execute the server with **--init=all**. The server will then
rebuild the database according to the existing XML files on the system, delete
all existing data and return Open ERP to its basic configuration.
