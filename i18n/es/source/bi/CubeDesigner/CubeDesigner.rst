
.. i18n: Goal of Cube Designer
.. i18n: =====================

Goal of Cube Designer
=====================

.. i18n: The goal is to develop a User Friendly Cube Designer for Open Object - BI that allows a user to define and / or modify an OLAP cube definition starting from any database. (Oracle, MySQL, PostgreSQL). This has to be user friendly so that a end-user can define his own cube on his own database without any development knowledge.

The goal is to develop a User Friendly Cube Designer for Open Object - BI that allows a user to define and / or modify an OLAP cube definition starting from any database. (Oracle, MySQL, PostgreSQL). This has to be user friendly so that a end-user can define his own cube on his own database without any development knowledge.

.. i18n: Basic features
.. i18n: --------------

Basic features
--------------

.. i18n: The cube designer of the OpenObject – BI Solutions helps the User to Create New cubes and Modify the existing cubes. First the User checks the connection with its database and if he is connected after that only the user can create cubes in two ways 
.. i18n: #Wizard Flow
.. i18n: #Generic Flow. 

The cube designer of the OpenObject – BI Solutions helps the User to Create New cubes and Modify the existing cubes. First the User checks the connection with its database and if he is connected after that only the user can create cubes in two ways 
#Wizard Flow
#Generic Flow. 

.. i18n: Wizard Flow
.. i18n: +++++++++++

Wizard Flow
+++++++++++

.. i18n: In the wizard flow a wizard will guide the user through the entire process of cube creation. Navigation can be done through Next and Previous button.

In the wizard flow a wizard will guide the user through the entire process of cube creation. Navigation can be done through Next and Previous button.

.. i18n: .. note::
.. i18n:         Clicking on the “Save” button on every form causes the data to be written in the database and simultaneously the  “Next” button is activated and the user is navigated to the next form.
.. i18n:         Next button will not be activated until the data is “Saved”.

.. note::
        Clicking on the “Save” button on every form causes the data to be written in the database and simultaneously the  “Next” button is activated and the user is navigated to the next form.
        Next button will not be activated until the data is “Saved”.

.. i18n: Generic Flow
.. i18n: ++++++++++++

Generic Flow
++++++++++++

.. i18n: The cube can be modified / created by the user in a normal way.

The cube can be modified / created by the user in a normal way.

.. i18n: :Modify / Create A Schema:

:Modify / Create A Schema:

.. i18n: The user specifies the desired schema name.
.. i18n: He selects the desired database or creates it with the help of [new].
.. i18n: He specifies the schema description.
.. i18n: He saves it.

The user specifies the desired schema name.
He selects the desired database or creates it with the help of [new].
He specifies the schema description.
He saves it.

.. i18n: :Modify / Create A Fact Table:

:Modify / Create A Fact Table:

.. i18n: User Makes a perticuler Type for Fact table
.. i18n: He select desired database or Schema for perticular Fact Table and also create by  its own [new] button.
.. i18n:   
.. i18n: :Modify / Create A Database:

User Makes a perticuler Type for Fact table
He select desired database or Schema for perticular Fact Table and also create by  its own [new] button.
  
:Modify / Create A Database:

.. i18n: User specifies the “General Parameters”
.. i18n: He specifies the “Connection Parameters” that specify which database is used for the connection with which port number.
.. i18n: He tests the connection for error and the “Connection URL” is generated.
.. i18n: On connection string being correct the new database is created.

User specifies the “General Parameters”
He specifies the “Connection Parameters” that specify which database is used for the connection with which port number.
He tests the connection for error and the “Connection URL” is generated.
On connection string being correct the new database is created.

.. i18n: :Modify / Create A Cube:

:Modify / Create A Cube:

.. i18n: The user provides desired cube name along with the fact tables and schema name.
.. i18n: The user can select the already created fact tables via a drop down box or can create a new fact table by clicking on [new].
.. i18n: Same goes for schema too.
.. i18n: The dimensions and measures at this point will be empty as they are not created as of now.

The user provides desired cube name along with the fact tables and schema name.
The user can select the already created fact tables via a drop down box or can create a new fact table by clicking on [new].
Same goes for schema too.
The dimensions and measures at this point will be empty as they are not created as of now.

.. i18n: :Modify / Create  A Dimension:

:Modify / Create  A Dimension:

.. i18n: The user  provides with the dimension name. 
.. i18n: The cube name that was provided by him will appear in the drop down box. He can select a cube name from the list else he can create a new cube by clicking on [new]. 
.. i18n: Hierarchies are absent.

The user  provides with the dimension name. 
The cube name that was provided by him will appear in the drop down box. He can select a cube name from the list else he can create a new cube by clicking on [new]. 
Hierarchies are absent.

.. i18n: :Modify / Create A Hierarchies:

:Modify / Create A Hierarchies:

.. i18n: The user provides the hierarchy name.
.. i18n: The dimension name will come in the dropdown box.
.. i18n: User can create a new dimension by clicking on [new]. 
.. i18n: User will provide with the hierarchy field name,sequence,hierarchy type,all member and default member fields. 
.. i18n: User will give the fact table by selecting it from a drop down box or by creating a new fact table altogether by clicking on [new]

The user provides the hierarchy name.
The dimension name will come in the dropdown box.
User can create a new dimension by clicking on [new]. 
User will provide with the hierarchy field name,sequence,hierarchy type,all member and default member fields. 
User will give the fact table by selecting it from a drop down box or by creating a new fact table altogether by clicking on [new]

.. i18n: :Modify / Create A Levels:

:Modify / Create A Levels:

.. i18n: The user has to specify the  level name,column name,column id,level class,table name,sequence and hierarchy.
.. i18n: Hierarchy will appear in the drop down box. 
.. i18n: He can create a new hierarchy by clicking on [new]. 

The user has to specify the  level name,column name,column id,level class,table name,sequence and hierarchy.
Hierarchy will appear in the drop down box. 
He can create a new hierarchy by clicking on [new]. 

.. i18n: .. note::
.. i18n:         Clicking on the "Save" button on every form causes the data to be written in the database.
.. i18n:         Double Click on row opens modification window of respective record.

.. note::
        Clicking on the "Save" button on every form causes the data to be written in the database.
        Double Click on row opens modification window of respective record.

.. i18n: :Modify / Create  A Measures:

:Modify / Create  A Measures:

.. i18n: The user  provides with the Measure name. 
.. i18n: The cube name that was provided by him will appear in the drop down box. He can select a cube name from the list else he can create a new cube by clicking on the [new]. 
.. i18n: It defines the all calculation / aggregation with fact column name.
.. i18n: Here all calculation / aggregation are interdepended with the fields of fact column name, aggregator, data type and format of string.

The user  provides with the Measure name. 
The cube name that was provided by him will appear in the drop down box. He can select a cube name from the list else he can create a new cube by clicking on the [new]. 
It defines the all calculation / aggregation with fact column name.
Here all calculation / aggregation are interdepended with the fields of fact column name, aggregator, data type and format of string.
