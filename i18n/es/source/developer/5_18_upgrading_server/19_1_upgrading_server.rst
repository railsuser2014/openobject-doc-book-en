
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

.. i18n: Files: .XML
.. i18n: -----------
.. i18n: ::
.. i18n: 
.. i18n: 	%define=lightblue color=#27adfb%

Files: .XML
-----------
::

	%define=lightblue color=#27adfb%

.. i18n: Data can be inserted or updated into the PostgreSQL tables corresponding to the Tiny ERP objects using XML files. The general structure of a Tiny ERP XML file is as follows :
.. i18n: ::
.. i18n: 
.. i18n: 	 <?xml version="1.0"?>
.. i18n: 	 <terp>
.. i18n: 	     <data>
.. i18n: 		 <record model="model.name_1" id="id_name_1">
.. i18n: 		     <field name="field1">
.. i18n: 		         %lightblue%"field1 content"
.. i18n: 		     </field>
.. i18n: 		     <field name="field2">
.. i18n: 		         %lightblue%"field2 content"
.. i18n: 		     </field>
.. i18n: 		     (...)
.. i18n: 		 </record> 
.. i18n: 		 <record model="model.name_2" id="id_name_2">
.. i18n: 		     (...)
.. i18n: 		 </record>
.. i18n: 		 (...)
.. i18n: 	     </data>
.. i18n: 	 </terp> 

Data can be inserted or updated into the PostgreSQL tables corresponding to the Tiny ERP objects using XML files. The general structure of a Tiny ERP XML file is as follows :
::

	 <?xml version="1.0"?>
	 <terp>
	     <data>
		 <record model="model.name_1" id="id_name_1">
		     <field name="field1">
		         %lightblue%"field1 content"
		     </field>
		     <field name="field2">
		         %lightblue%"field2 content"
		     </field>
		     (...)
		 </record> 
		 <record model="model.name_2" id="id_name_2">
		     (...)
		 </record>
		 (...)
	     </data>
	 </terp> 

.. i18n: Fields content are strings that must be encoded as UTF-8 in XML files.

Fields content are strings that must be encoded as UTF-8 in XML files.

.. i18n: Let's review an example taken from the TinyERP source (base_demo.xml in the base module):
.. i18n: ::
.. i18n: 
.. i18n: 	   <record model="res.company" id="main_company">
.. i18n: 	       <field name="name">Tiny sprl</field>
.. i18n: 	       <field name="partner_id" ref="main_partner"/>
.. i18n: 	       <field name="currency_id" ref="EUR"/>
.. i18n: 	   </record>

Let's review an example taken from the TinyERP source (base_demo.xml in the base module):
::

	   <record model="res.company" id="main_company">
	       <field name="name">Tiny sprl</field>
	       <field name="partner_id" ref="main_partner"/>
	       <field name="currency_id" ref="EUR"/>
	   </record>

.. i18n: ::
.. i18n: 
.. i18n: 	   <record model="res.users" id="user_admin">
.. i18n: 	       <field name="login">admin</field>
.. i18n: 	       <field name="password">admin</field>
.. i18n: 	       <field name="name">Administrator</field>
.. i18n: 	       <field name="signature">Administrator</field>
.. i18n: 	       <field name="action_id" ref="action_menu_admin"/>
.. i18n: 	       <field name="menu_id" ref="action_menu_admin"/>
.. i18n: 	       <field name="address_id" ref="main_address"/>
.. i18n: 	       <field name="groups_id" eval="[(6,0,[group_admin])]"/>
.. i18n: 	       <field name="company_id" ref="main_company"/>
.. i18n: 	   </record>

::

	   <record model="res.users" id="user_admin">
	       <field name="login">admin</field>
	       <field name="password">admin</field>
	       <field name="name">Administrator</field>
	       <field name="signature">Administrator</field>
	       <field name="action_id" ref="action_menu_admin"/>
	       <field name="menu_id" ref="action_menu_admin"/>
	       <field name="address_id" ref="main_address"/>
	       <field name="groups_id" eval="[(6,0,[group_admin])]"/>
	       <field name="company_id" ref="main_company"/>
	   </record>

.. i18n: This last record defines the admin user :

This last record defines the admin user :

.. i18n:     * The fields login, password, etc are straightforward.
.. i18n:     * The **ref** attribute allows to fill relations between the records : 

    * The fields login, password, etc are straightforward.
    * The **ref** attribute allows to fill relations between the records : 

.. i18n: ::
.. i18n: 	
.. i18n: 	<field name="company_id" ref="main_company"/>

::
	
	<field name="company_id" ref="main_company"/>

.. i18n: ->The field @@company_id@@ is a many-to-one relation from the user object to the company object, and **main_company** is the id of to associate.

->The field @@company_id@@ is a many-to-one relation from the user object to the company object, and **main_company** is the id of to associate.

.. i18n:     * The **eval** attribute allows to put some python code in the xml: here the groups_id field is a many2many. For such a field, "[(6,0,[group_admin])]" means : Remove all the groups associated with the current user and use the list [group_admin] as the new associated groups (and group_admin is the id of another record). 
.. i18n: 
.. i18n:     * The **search** attribute allows to find the record to associate when you do not know its xml id. You can thus specify a search criteria to find the wanted record. The criteria is a list of tuples of the same form than for the predefined search method. If there are several results, an arbitrary one will be chosen (the first one): 

    * The **eval** attribute allows to put some python code in the xml: here the groups_id field is a many2many. For such a field, "[(6,0,[group_admin])]" means : Remove all the groups associated with the current user and use the list [group_admin] as the new associated groups (and group_admin is the id of another record). 

    * The **search** attribute allows to find the record to associate when you do not know its xml id. You can thus specify a search criteria to find the wanted record. The criteria is a list of tuples of the same form than for the predefined search method. If there are several results, an arbitrary one will be chosen (the first one): 

.. i18n: 	<field name="partner_id" search="[]" model="res.partner"/>

	<field name="partner_id" search="[]" model="res.partner"/>

.. i18n: ->This is a classical example of the use of @@search@@ in demo data: here we do not really care about which partner we want to use for the test, so we give an empty list. Notice the **model** attribute is currently mandatory. 

->This is a classical example of the use of @@search@@ in demo data: here we do not really care about which partner we want to use for the test, so we give an empty list. Notice the **model** attribute is currently mandatory. 

.. i18n: The Data
.. i18n: ++++++++

The Data
++++++++

.. i18n: Record Tag
.. i18n: """"""""""

Record Tag
""""""""""

.. i18n: Description
.. i18n: ~~~~~~~~~~~

Description
~~~~~~~~~~~

.. i18n: The addition of new data is made with the **record** tag. This one takes a mandatory attribute : **model**. Model is the object name where the insertion has to be done. The tag record can also take an optional attribute: **id**. If this attribute is given, a variable of this name can be used later on, in the same file, to make reference to the newly created resource ID.

The addition of new data is made with the **record** tag. This one takes a mandatory attribute : **model**. Model is the object name where the insertion has to be done. The tag record can also take an optional attribute: **id**. If this attribute is given, a variable of this name can be used later on, in the same file, to make reference to the newly created resource ID.

.. i18n: A **record** tag may contain field tags. They indicate the record's **fields** value. If a field is not specified the default value will be used.

A **record** tag may contain field tags. They indicate the record's **fields** value. If a field is not specified the default value will be used.

.. i18n: Example
.. i18n: ~~~~~~~
.. i18n: ::
.. i18n: 
.. i18n: 	<record model="ir.actions.report.xml" id="l0">
.. i18n: 	     <field name="model">account.invoice</field>
.. i18n: 	     <field name="name">Invoices List</field>
.. i18n: 	     <field name="report_name">account.invoice.list</field>
.. i18n: 	     <field name="report_xsl">account/report/invoice.xsl</field>
.. i18n: 	     <field name="report_xml">account/report/invoice.xml</field>
.. i18n: 	</record>

Example
~~~~~~~
::

	<record model="ir.actions.report.xml" id="l0">
	     <field name="model">account.invoice</field>
	     <field name="name">Invoices List</field>
	     <field name="report_name">account.invoice.list</field>
	     <field name="report_xsl">account/report/invoice.xsl</field>
	     <field name="report_xml">account/report/invoice.xml</field>
	</record>

.. i18n: field tag
.. i18n: ~~~~~~~~~

field tag
~~~~~~~~~

.. i18n: The attributes for the field tag are the following:

The attributes for the field tag are the following:

.. i18n:     * **name**
.. i18n:           o mandatory attribute indicating the field name 
.. i18n:     * **eval**
.. i18n:           o python expression that indicating the value to add 
.. i18n:     * **ref**
.. i18n:           o reference to an id defined in this file 

    * **name**
          o mandatory attribute indicating the field name 
    * **eval**
          o python expression that indicating the value to add 
    * **ref**
          o reference to an id defined in this file 

.. i18n: function tag
.. i18n: ~~~~~~~~~~~~

function tag
~~~~~~~~~~~~

.. i18n:     * model:
.. i18n:     * name:
.. i18n:     * eval
.. i18n:           o should evaluate to the list of parameters of the method to be called, excluding cr and uid 

    * model:
    * name:
    * eval
          o should evaluate to the list of parameters of the method to be called, excluding cr and uid 

.. i18n: Example
.. i18n: ~~~~~~~
.. i18n: ::
.. i18n: 
.. i18n: 	<function model="ir.ui.menu" name="search" eval="[[('name','=','Operations')]]"/>

Example
~~~~~~~
::

	<function model="ir.ui.menu" name="search" eval="[[('name','=','Operations')]]"/>

.. i18n: getitem tag

getitem tag

.. i18n: Takes a subset of the evaluation of the last child node of the tag.

Takes a subset of the evaluation of the last child node of the tag.

.. i18n:     * type
.. i18n:           - int or list 
.. i18n:     * index
.. i18n:     * int or string (a key of a dictionary) 

    * type
          - int or list 
    * index
    * int or string (a key of a dictionary) 

.. i18n: Example
.. i18n: ~~~~~~~

Example
~~~~~~~

.. i18n: Evaluates to the first element of the list of ids returned by the function node

Evaluates to the first element of the list of ids returned by the function node

.. i18n: .. code-block :: python

.. code-block :: python

.. i18n: 	<getitem index="0" type="list">
.. i18n: 	    <function model="ir.ui.menu" name="search" eval="[[('name','=','Operations')]]"/>
.. i18n: 	</getitem>

	<getitem index="0" type="list">
	    <function model="ir.ui.menu" name="search" eval="[[('name','=','Operations')]]"/>
	</getitem>

.. i18n: CSV Files 
.. i18n: ---------

CSV Files 
---------

.. i18n: Importing from a CSV
.. i18n: ++++++++++++++++++++

Importing from a CSV
++++++++++++++++++++

.. i18n: Instead of using .XML file, you can import .CSV files. It is simpler but the migration system does not migrate the data imported from the .CSV files. It's like the noupdate attribute in .XML files. It's also more difficult to keep track of relations between ressources and it is more slower at the installation of the server.

Instead of using .XML file, you can import .CSV files. It is simpler but the migration system does not migrate the data imported from the .CSV files. It's like the noupdate attribute in .XML files. It's also more difficult to keep track of relations between ressources and it is more slower at the installation of the server.

.. i18n: Use this only for demo data that will never been upgraded from one version of Tiny ERP to another.

Use this only for demo data that will never been upgraded from one version of Tiny ERP to another.

.. i18n: The name of the object is the name of the file before the first '-'. You must use one file per object to import. For example, to import a file with partners (including their multiple contacts and events), the file must be named like one of the following example:

The name of the object is the name of the file before the first '-'. You must use one file per object to import. For example, to import a file with partners (including their multiple contacts and events), the file must be named like one of the following example:

.. i18n:     * res.partner.csv
.. i18n:     * res.partner-tiny_demo.csv
.. i18n:     * res.partner-tiny.demo.csv 

    * res.partner.csv
    * res.partner-tiny_demo.csv
    * res.partner-tiny.demo.csv 

.. i18n: Structure of the CSV file
.. i18n: +++++++++++++++++++++++++

Structure of the CSV file
+++++++++++++++++++++++++

.. i18n: Have a look at the user manual for a complete description on how to construct your .CSV file.

Have a look at the user manual for a complete description on how to construct your .CSV file.

.. i18n: Usefull info:

Usefull info:

.. i18n:     * Separator of field: ,
.. i18n:     * Quote of fields: "
.. i18n:     * Encoding to use: UTF-8 

    * Separator of field: ,
    * Quote of fields: "
    * Encoding to use: UTF-8 

.. i18n: Export demo data and import it from a module
.. i18n: ++++++++++++++++++++++++++++++++++++++++++++

Export demo data and import it from a module
++++++++++++++++++++++++++++++++++++++++++++

.. i18n: You can import .CSV file that have been exported from the Tiny ERP client. This is interesting to create your own demo module. But both formats are not exactly the same, mainly due to the conversion: Structured Data -> Flat Data -> Structured Data.

You can import .CSV file that have been exported from the Tiny ERP client. This is interesting to create your own demo module. But both formats are not exactly the same, mainly due to the conversion: Structured Data -> Flat Data -> Structured Data.

.. i18n:     * The name of the column (first line of the .CSV file) use the end user term in his own language when you export from the client. If you want to import from a module, you must convert the first column using the fields names. Example, from the partner form: 

    * The name of the column (first line of the .CSV file) use the end user term in his own language when you export from the client. If you want to import from a module, you must convert the first column using the fields names. Example, from the partner form: 

.. i18n:     Name,Code,Contacts/Contact Name,Contacts/Street,Contacts/Zip

    Name,Code,Contacts/Contact Name,Contacts/Street,Contacts/Zip

.. i18n:         becomes 

        becomes 

.. i18n:     name,ref,address/name,address/street,address/zip 

    name,ref,address/name,address/street,address/zip 

.. i18n:     * When you export from the Tiny ERP client, you can select any many2one fields and their child's relation. When you import from a module, Tiny ERP tries to recreate the relation between the two resources. For example, do not export something like this from a sale order form - otherwise Tiny ERP will not be able to import your file: 

    * When you export from the Tiny ERP client, you can select any many2one fields and their child's relation. When you import from a module, Tiny ERP tries to recreate the relation between the two resources. For example, do not export something like this from a sale order form - otherwise Tiny ERP will not be able to import your file: 

.. i18n:     Order Description,Partner/Name,Partner/Payable,Partner/Address/Name 

    Order Description,Partner/Name,Partner/Payable,Partner/Address/Name 

.. i18n:     * To find the link for a many2one or many2many field, the server use the name_search function when importing. So, for a many2one field, it is better to export the field 'name' or 'code' of the related resource only. Use the more unique one. Be sure that the field you export is searchable by the name_search function. (the 'name' column is always searchable). 

    * To find the link for a many2one or many2many field, the server use the name_search function when importing. So, for a many2one field, it is better to export the field 'name' or 'code' of the related resource only. Use the more unique one. Be sure that the field you export is searchable by the name_search function. (the 'name' column is always searchable). 

.. i18n:     Order Description,Partner/Code 

    Order Description,Partner/Code 

.. i18n:     * Change the title of the column for all many2many or many2one fields. It's because you export the related resource and you import a link on the resource. Example from a sale order: Partner/Code should become partner_id and not partner_id/code. If you kept the @@/code@@, Tiny ERP will try to create those entries in the database instead of finding reference to existing ones. 
.. i18n: 
.. i18n:     * Many2many fields. If all the exported data contains 0 or 1 relation on each many2many fields, there will be no problem. Otherwise, the export will result in one line per many2many. The import function expect to get all many2many relations in one column, separated by a comma. So, you have to make to transformation. For example, if the categories "Customer" and "Supplier" already exists : 

    * Change the title of the column for all many2many or many2one fields. It's because you export the related resource and you import a link on the resource. Example from a sale order: Partner/Code should become partner_id and not partner_id/code. If you kept the @@/code@@, Tiny ERP will try to create those entries in the database instead of finding reference to existing ones. 

    * Many2many fields. If all the exported data contains 0 or 1 relation on each many2many fields, there will be no problem. Otherwise, the export will result in one line per many2many. The import function expect to get all many2many relations in one column, separated by a comma. So, you have to make to transformation. For example, if the categories "Customer" and "Supplier" already exists : 

.. i18n:     name,category_id 
.. i18n:     Smith, "Customer, Supplier" 

    name,category_id 
    Smith, "Customer, Supplier" 

.. i18n: If you want to create these two categories you can try :

If you want to create these two categories you can try :

.. i18n:     name,category_id/name 
.. i18n:     Smith, "Customer, Supplier" 

    name,category_id/name 
    Smith, "Customer, Supplier" 

.. i18n: This does not work as expected: a category "Customer, Supplier" is created. The solution is to create an empty line with only the second category:

This does not work as expected: a category "Customer, Supplier" is created. The solution is to create an empty line with only the second category:

.. i18n:     name,category_id/name 
.. i18n:     Smith, Customer 
.. i18n:     ,Supplier 

    name,category_id/name 
    Smith, Customer 
    ,Supplier 

.. i18n: (Note the comma before "Supplier").

(Note the comma before "Supplier").

.. i18n:     * Read only fields. Do not try to import read only fields like the amount receivable or payable for a partner. Otherwise, Tiny ERP will not accept to import your file. 
.. i18n: 
.. i18n:     * Exporting trees. You can export and import tree structures using the parent field. You just have to take care of the import order. The parent have to be created before his child's. 

    * Read only fields. Do not try to import read only fields like the amount receivable or payable for a partner. Otherwise, Tiny ERP will not accept to import your file. 

    * Exporting trees. You can export and import tree structures using the parent field. You just have to take care of the import order. The parent have to be created before his child's. 

.. i18n: Use record id like in xml file:
.. i18n: +++++++++++++++++++++++++++++++

Use record id like in xml file:
+++++++++++++++++++++++++++++++

.. i18n: It's possible to define an id for each line of the csv file. This allow to define references between records:

It's possible to define an id for each line of the csv file. This allow to define references between records:

.. i18n:     id, name, parent_id:id 
.. i18n:     record_one, Father, 
.. i18n:     record_two, Child, record_one 

    id, name, parent_id:id 
    record_one, Father, 
    record_two, Child, record_one 

.. i18n: If you do this, the line with the parent data must be before the child lines in the file. 

If you do this, the line with the parent data must be before the child lines in the file. 

.. i18n: Multiple CSV Files 
.. i18n: ------------------

Multiple CSV Files 
------------------

.. i18n: Importing from multiple CSV a full group of linked data
.. i18n: +++++++++++++++++++++++++++++++++++++++++++++++++++++++

Importing from multiple CSV a full group of linked data
+++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. i18n: It' possible to import a lot of data, with multiple CSV files imported as a single operation. Assume we have a database with books and authors with a relation many2many between book and author.

It' possible to import a lot of data, with multiple CSV files imported as a single operation. Assume we have a database with books and authors with a relation many2many between book and author.

.. i18n: And that you already have a file with a lot of books (like a library) and an other file with a lot of authors and a third file with the links between them.

And that you already have a file with a lot of books (like a library) and an other file with a lot of authors and a third file with the links between them.

.. i18n: How to import that easily in openERP ?

How to import that easily in openERP ?

.. i18n: Definition of an import module
.. i18n: ++++++++++++++++++++++++++++++

Definition of an import module
++++++++++++++++++++++++++++++

.. i18n: You can do this in the module you have defined to manage yours books and authors. but Sometimes, the tables to import can also be in several modules.

You can do this in the module you have defined to manage yours books and authors. but Sometimes, the tables to import can also be in several modules.

.. i18n: For this example, let's say that 'book' object is defined in a module called 'library_management' and that 'Author' object in a module called 'contact_name'.

For this example, let's say that 'book' object is defined in a module called 'library_management' and that 'Author' object in a module called 'contact_name'.

.. i18n: In this case, you can create a 'fake' module, just to import the data for all these multiples modules. Call this importation module : 'import_my_books'.

In this case, you can create a 'fake' module, just to import the data for all these multiples modules. Call this importation module : 'import_my_books'.

.. i18n: You create this module as others modules of OpenObject :

You create this module as others modules of OpenObject :

.. i18n:    1. create a folder 'import_my_books'
.. i18n:    2. inside, create a '__init__.py' file with only one line : import import_my_books
.. i18n:    3. again, in the same folder, create a '__terp__.py' file and in this file, write the following code : 

   1. create a folder 'import_my_books'
   2. inside, create a '__init__.py' file with only one line : import import_my_books
   3. again, in the same folder, create a '__terp__.py' file and in this file, write the following code : 

.. i18n: .. code-block :: python

.. code-block :: python

.. i18n: 	 # -*- encoding: utf-8 -*-
.. i18n: 	 {
.. i18n: 	   'name': 'My Book Import',
.. i18n: 	   'category': 'Data Module 1',
.. i18n: 	   'init_xml':[],
.. i18n: 	   'author': 'mySelf & I',
.. i18n: 	   'depends': ['base','library_management','contact_name'],
.. i18n: 	   'version': '1.0',
.. i18n: 	   'active': False,
.. i18n: 	   'demo_xml': [],
.. i18n: 	   'update_xml':['contact_name.author.csv','library.book.csv'],
.. i18n: 	   'installable': True
.. i18n: 	 }

	 # -*- encoding: utf-8 -*-
	 {
	   'name': 'My Book Import',
	   'category': 'Data Module 1',
	   'init_xml':[],
	   'author': 'mySelf & I',
	   'depends': ['base','library_management','contact_name'],
	   'version': '1.0',
	   'active': False,
	   'demo_xml': [],
	   'update_xml':['contact_name.author.csv','library.book.csv'],
	   'installable': True
	 }

.. i18n: Creation of CSV files
.. i18n: +++++++++++++++++++++

Creation of CSV files
+++++++++++++++++++++

.. i18n: For the CSV files, you'll import one the after, the other one.

For the CSV files, you'll import one the after, the other one.

.. i18n: So you have to choose, in which way you'll treat the many2many relation. For our example, we've choose to import all the authors, then all the books with the links to the authors.

So you have to choose, in which way you'll treat the many2many relation. For our example, we've choose to import all the authors, then all the books with the links to the authors.

.. i18n:    1. authors CSV file 

   1. authors CSV file 

.. i18n: You have to put your data in a CSV file without any link to books (because the book ids will be known only AFTERWARDS...) For example : ("contact_name.author.csv")

You have to put your data in a CSV file without any link to books (because the book ids will be known only AFTERWARDS...) For example : ("contact_name.author.csv")

.. i18n: ::
.. i18n: 
.. i18n: 	 id,last_name,first_name,type
.. i18n: 	 author_1,Bradley,Marion Zimmer,Book writer
.. i18n: 	 author_2,"Szu T'su",,Chinese philosopher
.. i18n: 	 author_3,Zelazny,Roger,Book writer
.. i18n: 	 author_4,Arleston,Scotch,Screen Writer
.. i18n: 	 author_5,Magnin,Florence,Comics Drawer
.. i18n: 	 ...

::

	 id,last_name,first_name,type
	 author_1,Bradley,Marion Zimmer,Book writer
	 author_2,"Szu T'su",,Chinese philosopher
	 author_3,Zelazny,Roger,Book writer
	 author_4,Arleston,Scotch,Screen Writer
	 author_5,Magnin,Florence,Comics Drawer
	 ...

.. i18n:    1. Books CSV file 

   1. Books CSV file 

.. i18n: Here, you can put the data about your books, but also, the links to the authors, using the same id as the column 'id' of the author CSV file. For example : ("library.book.csv" )

Here, you can put the data about your books, but also, the links to the authors, using the same id as the column 'id' of the author CSV file. For example : ("library.book.csv" )

.. i18n: ::
.. i18n: 
.. i18n: 	 id,title,isbn,pages,date,author_ids:id
.. i18n: 	 book_a,Les Cours du Chaos,1234567890123,268,1975-12-25,"author_3"
.. i18n: 	 book_b,"L'art de la Guerre, en 219 volumes",1234567890124,1978-01-01,"author_2"
.. i18n: 	 book_c,"new marvellous comics",1587459248579,2009-01-01,"author_5,author_4"
.. i18n: 	 ...

::

	 id,title,isbn,pages,date,author_ids:id
	 book_a,Les Cours du Chaos,1234567890123,268,1975-12-25,"author_3"
	 book_b,"L'art de la Guerre, en 219 volumes",1234567890124,1978-01-01,"author_2"
	 book_c,"new marvellous comics",1587459248579,2009-01-01,"author_5,author_4"
	 ...

.. i18n: Five remarks :

Five remarks :

.. i18n:    1. the field content must be enclosed in double quotes (") if there is a double quote or a comma in the field.
.. i18n:    2. the dates are in the format YYYY-MM-DD
.. i18n:    3. if you have many ids in the same column, you must separate them with a comma, and, by the way, you must enclosed the content of the column between double quotes...
.. i18n:    4. the name of the field is the same as the name of the field in the class definition AND must be followed by ':id' if the content is an ID that must be interpreted by the import module. In fact, "author_4" will be transformed by the import module in an integer id for the database module and this numercial id will be put also in the table between author and book, not the literal ID (author_4).
.. i18n:    5. the encoding to be used by the CSV file is the 'UTF-8' encoding 

   1. the field content must be enclosed in double quotes (") if there is a double quote or a comma in the field.
   2. the dates are in the format YYYY-MM-DD
   3. if you have many ids in the same column, you must separate them with a comma, and, by the way, you must enclosed the content of the column between double quotes...
   4. the name of the field is the same as the name of the field in the class definition AND must be followed by ':id' if the content is an ID that must be interpreted by the import module. In fact, "author_4" will be transformed by the import module in an integer id for the database module and this numercial id will be put also in the table between author and book, not the literal ID (author_4).
   5. the encoding to be used by the CSV file is the 'UTF-8' encoding 

.. i18n: Links between id if the CSV files
.. i18n: +++++++++++++++++++++++++++++++++

Links between id if the CSV files
+++++++++++++++++++++++++++++++++

.. i18n: Links to id already in the system 
.. i18n: +++++++++++++++++++++++++++++++++

Links to id already in the system 
+++++++++++++++++++++++++++++++++

.. i18n: XML data files convention
.. i18n: -------------------------

XML data files convention
-------------------------

.. i18n: Developers:Developper's Book/Data Loading/XMLFilesConventions

Developers:Developper's Book/Data Loading/XMLFilesConventions

.. i18n: Jump to: navigation, search

Jump to: navigation, search

.. i18n: The ressources are placed in different files according to their uses. By convention;

The ressources are placed in different files according to their uses. By convention;

.. i18n:  .. csv-table:: 
.. i18n:    :header: "Name","Description"
.. i18n:    :widths: 25, 25
.. i18n: 
.. i18n:    "modulename_workflow.xml","the definitions of workflows"
.. i18n:    "modulename_view.xml","the views"
.. i18n:    "modulename_data.xml","the important datas to download"
.. i18n:    "modulename_report.xml","the reports declarations"
.. i18n:    "modulename_demo.xml","the useful datas for the demo version"

 .. csv-table:: 
   :header: "Name","Description"
   :widths: 25, 25

   "modulename_workflow.xml","the definitions of workflows"
   "modulename_view.xml","the views"
   "modulename_data.xml","the important datas to download"
   "modulename_report.xml","the reports declarations"
   "modulename_demo.xml","the useful datas for the demo version"

.. i18n: The workflow files have to be loaded before the datas ! Otherwise, the ressource created won't be integrated inside the workflow because the later is not yet defined.

The workflow files have to be loaded before the datas ! Otherwise, the ressource created won't be integrated inside the workflow because the later is not yet defined.

.. i18n: Managing updates 
.. i18n: ----------------

Managing updates 
----------------

.. i18n: Managing updates and migrations
.. i18n: +++++++++++++++++++++++++++++++

Managing updates and migrations
+++++++++++++++++++++++++++++++

.. i18n: Open ERP has a built'in migration and upgrade system which allows updates to be nearly (or often) automatic. This system also allows to easily incorporate custom modules.

Open ERP has a built'in migration and upgrade system which allows updates to be nearly (or often) automatic. This system also allows to easily incorporate custom modules.

.. i18n: Table/Object structure
.. i18n: """"""""""""""""""""""

Table/Object structure
""""""""""""""""""""""

.. i18n: When you run tinyerp-server with option --init or --update, the table structure are updated to match the new description that is in .py files. Fields that are removed are not removed in the postgresql database not to lose data.

When you run tinyerp-server with option --init or --update, the table structure are updated to match the new description that is in .py files. Fields that are removed are not removed in the postgresql database not to lose data.

.. i18n: So, simply running --update or --init, will upgrade your table structure.

So, simply running --update or --init, will upgrade your table structure.

.. i18n: It's important to run --init=module the first time you install the module. Next time, you must use the --update=module argument instead of the init one. This is because init loads ressources that are loaded only once and never upgraded (eg: ressources with no id="" attribute or within a noupdate="1" <data> tag).

It's important to run --init=module the first time you install the module. Next time, you must use the --update=module argument instead of the init one. This is because init loads ressources that are loaded only once and never upgraded (eg: ressources with no id="" attribute or within a noupdate="1" <data> tag).

.. i18n: Data
.. i18n: """"
.. i18n: Some data is automatically loaded at the installation of Tiny ERP:

Data
""""
Some data is automatically loaded at the installation of Tiny ERP:

.. i18n:     * views, actions, menus,
.. i18n:     * workflows,
.. i18n:     * demo data 

    * views, actions, menus,
    * workflows,
    * demo data 

.. i18n: This data is also migrated to a new version if you run --update or --init.

This data is also migrated to a new version if you run --update or --init.

.. i18n: Workflows
.. i18n: """""""""

Workflows
"""""""""

.. i18n: Workflows are also upgraded automatically. If some activities are removed, the documents states evolves automatically to the preceding activities. That ensure that all documents are always in valid states.

Workflows are also upgraded automatically. If some activities are removed, the documents states evolves automatically to the preceding activities. That ensure that all documents are always in valid states.

.. i18n: You can freely remove activities in your XML files. If workitems are in this activity, they will evolve to the preceding unlinked activity. And after the activity will be removed.

You can freely remove activities in your XML files. If workitems are in this activity, they will evolve to the preceding unlinked activity. And after the activity will be removed.

.. i18n: Things to care about during development
.. i18n: """""""""""""""""""""""""""""""""""""""

Things to care about during development
"""""""""""""""""""""""""""""""""""""""

.. i18n: Since version 3.0.2 of Tiny ERP, you can not use twice the same 'id="..."' during resource creation in your XML files, unless they are in two different modules.

Since version 3.0.2 of Tiny ERP, you can not use twice the same 'id="..."' during resource creation in your XML files, unless they are in two different modules.

.. i18n: Resources which don't contain an id are created (and updated) only once; at the installation of the module or when you use the --init argument.

Resources which don't contain an id are created (and updated) only once; at the installation of the module or when you use the --init argument.

.. i18n: If a resource has an id and this resource is not present anymore in the next version of the XML file, Open ERP will automatically remove it from the database. If this resource is still present, Open ERP will update the modifications to this resource.

If a resource has an id and this resource is not present anymore in the next version of the XML file, Open ERP will automatically remove it from the database. If this resource is still present, Open ERP will update the modifications to this resource.

.. i18n: If you use a new id, the resource will be automatically created at the next update of this module.

If you use a new id, the resource will be automatically created at the next update of this module.

.. i18n: **Use explicit id declaration !**, Example:

**Use explicit id declaration !**, Example:

.. i18n:     * view_invoice_form,
.. i18n:     * view_move_line_tree,
.. i18n:     * action_invoice_form_open, ... 

    * view_invoice_form,
    * view_move_line_tree,
    * action_invoice_form_open, ... 

.. i18n: It is important to put id="...." to all record that are important for the next version migrations. For example, do not forget to put some id="..." on all workflows transitions. This will allows Open ERP to know which transition has been removed and which transition is new or updated.

It is important to put id="...." to all record that are important for the next version migrations. For example, do not forget to put some id="..." on all workflows transitions. This will allows Open ERP to know which transition has been removed and which transition is new or updated.

.. i18n: Custom modules
.. i18n: """"""""""""""

Custom modules
""""""""""""""

.. i18n: For example, if you want to override the view of an object named 'invoice_form' in your xml file (id="invoice_form"). All you have to do is redefine this view in your custom module with the same id. You can prefix ids with the name of the module to reference an id defined in another module.

For example, if you want to override the view of an object named 'invoice_form' in your xml file (id="invoice_form"). All you have to do is redefine this view in your custom module with the same id. You can prefix ids with the name of the module to reference an id defined in another module.

.. i18n: Example:

Example:

.. i18n:     <record model="ir.ui.view" id="account.invoice_form"> 
.. i18n:     ... 
.. i18n:     <record> 

    <record model="ir.ui.view" id="account.invoice_form"> 
    ... 
    <record> 

.. i18n: This will override the invoice form view. You do not have to delete the old view, like in 3.0 versions of Open ERP.

This will override the invoice form view. You do not have to delete the old view, like in 3.0 versions of Open ERP.

.. i18n: Note that it is often better to use view inherytancy instead of overwritting views.

Note that it is often better to use view inherytancy instead of overwritting views.

.. i18n: In this migration system, you do not have to delete any ressource. The migration system will detect if it is an update or a delete using id="..." attributes. This is important to preserve references duing migrations.

In this migration system, you do not have to delete any ressource. The migration system will detect if it is an update or a delete using id="..." attributes. This is important to preserve references duing migrations.

.. i18n: Demo datas
.. i18n: """"""""""

Demo datas
""""""""""

.. i18n: Demo datas do not have to be upgraded; because they are probably modified, deleted, ... by users. So, to avoid demo data to be upgraded, you can put a noupdate="1" attribute in the <data> tag of your .xml data files.

Demo datas do not have to be upgraded; because they are probably modified, deleted, ... by users. So, to avoid demo data to be upgraded, you can put a noupdate="1" attribute in the <data> tag of your .xml data files.

.. i18n: Summary of update and init process
.. i18n: ++++++++++++++++++++++++++++++++++

Summary of update and init process
++++++++++++++++++++++++++++++++++

.. i18n: init:

init:

.. i18n:     modify/add/delete demo data and builtin data 

    modify/add/delete demo data and builtin data 

.. i18n: update:

update:

.. i18n:     modifiy/add/delete non demo data 

    modifiy/add/delete non demo data 

.. i18n: Examples of builtin (non demo) data:

Examples of builtin (non demo) data:

.. i18n:     * Menu structure, 
.. i18n:     * View definition, 
.. i18n:     * Workflow description, ... 
.. i18n:       -> Everything that as an id="..." in the .XML data declaration (if no attr noupdate="1" in the header) 

    * Menu structure, 
    * View definition, 
    * Workflow description, ... 
      -> Everything that as an id="..." in the .XML data declaration (if no attr noupdate="1" in the header) 

.. i18n: What's going on on a update process:

What's going on on a update process:

.. i18n:    1. If you manually added data within the client:
.. i18n:           * the update process will not change them 
.. i18n:    2. If you dropped data:
.. i18n:           * if it was demo data, the update process will do nothing
.. i18n:           * it it was builtin data (like a view), the update process will recreate it 
.. i18n:    3. If you modified data (either in the .XML or the client):
.. i18n:           * if it's demo data: nothing
.. i18n:           * if it's builtin data, data are updated 
.. i18n:    4. If builtin data have been deleted in the .XML file:
.. i18n:           * this data will be deleted in the database. 

   1. If you manually added data within the client:
          * the update process will not change them 
   2. If you dropped data:
          * if it was demo data, the update process will do nothing
          * it it was builtin data (like a view), the update process will recreate it 
   3. If you modified data (either in the .XML or the client):
          * if it's demo data: nothing
          * if it's builtin data, data are updated 
   4. If builtin data have been deleted in the .XML file:
          * this data will be deleted in the database. 
