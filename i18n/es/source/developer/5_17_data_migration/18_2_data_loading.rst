
.. i18n: Data Loading
.. i18n: ============

Data Loading
============

.. i18n: During Open ERP installation, two steps are necessary to create and feed the database:

During Open ERP installation, two steps are necessary to create and feed the database:

.. i18n:    1. Create the SQL tables
.. i18n:    2. Insert the different data into the tables 

   1. Create the SQL tables
   2. Insert the different data into the tables 

.. i18n: The creation (or modification in the case of an upgrade) of SQL tables is automated thanks to the description of objects in the server.

The creation (or modification in the case of an upgrade) of SQL tables is automated thanks to the description of objects in the server.

.. i18n: Into Open ERP, all the logic of the application is stored in the database. We find for example:

Into Open ERP, all the logic of the application is stored in the database. We find for example:

.. i18n:     * the definitions of the reports,
.. i18n:     * the object default values,
.. i18n:     * the form description of the interface client,
.. i18n:     * the relations between the menu and the client buttons, ... 

    * the definitions of the reports,
    * the object default values,
    * the form description of the interface client,
    * the relations between the menu and the client buttons, ... 

.. i18n: There must be a mechanism to describe, modify and reload the different data. These data are represented into a set of XML files that can possibly be loaded during start of the program in order to fill in the tables. 

There must be a mechanism to describe, modify and reload the different data. These data are represented into a set of XML files that can possibly be loaded during start of the program in order to fill in the tables. 
