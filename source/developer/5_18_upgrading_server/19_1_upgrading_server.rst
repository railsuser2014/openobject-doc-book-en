Data Loading
============

During Open ERP installation, two steps are necessary to create and feed the database:

   1. Create the SQL tables
   2. Insert the different data into the tables 

The creation (or modification in the case of an upgrade) of SQL tables is automated thanks to the description of objects in the server.

Into Open ERP, all the logic of the application is stored in the database. We find for example:

    * the definitions of the reports,
    * the object default values,
    * the form description of the interface client,
    * the relations between the menu and the client buttons, ... 


There must be a mechanism to describe, modify and reload the different data. These data are represented into a set of XML files that can possibly be loaded during start of the program in order to fill in the tables. 


Files: .XML
-----------
::

	%define=lightblue color=#27adfb%

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

Fields content are strings that must be encoded as UTF-8 in XML files.

Let's review an example taken from the TinyERP source (base_demo.xml in the base module):
::

	   <record model="res.company" id="main_company">
	       <field name="name">Tiny sprl</field>
	       <field name="partner_id" ref="main_partner"/>
	       <field name="currency_id" ref="EUR"/>
	   </record>

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

This last record defines the admin user :

    * The fields login, password, etc are straightforward.
    * The **ref** attribute allows to fill relations between the records : 

::
	
	<field name="company_id" ref="main_company"/>

->The field @@company_id@@ is a many-to-one relation from the user object to the company object, and **main_company** is the id of to associate.

    * The **eval** attribute allows to put some python code in the xml: here the groups_id field is a many2many. For such a field, "[(6,0,[group_admin])]" means : Remove all the groups associated with the current user and use the list [group_admin] as the new associated groups (and group_admin is the id of another record). 

    * The **search** attribute allows to find the record to associate when you do not know its xml id. You can thus specify a search criteria to find the wanted record. The criteria is a list of tuples of the same form than for the predefined search method. If there are several results, an arbitrary one will be chosen (the first one): 

	<field name="partner_id" search="[]" model="res.partner"/>

->This is a classical example of the use of @@search@@ in demo data: here we do not really care about which partner we want to use for the test, so we give an empty list. Notice the **model** attribute is currently mandatory. 

The Data
++++++++

Record Tag
""""""""""

Description
~~~~~~~~~~~

The addition of new data is made with the **record** tag. This one takes a mandatory attribute : **model**. Model is the object name where the insertion has to be done. The tag record can also take an optional attribute: **id**. If this attribute is given, a variable of this name can be used later on, in the same file, to make reference to the newly created resource ID.

A **record** tag may contain field tags. They indicate the record's **fields** value. If a field is not specified the default value will be used.

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

field tag
~~~~~~~~~

The attributes for the field tag are the following:

    * **name**
          o mandatory attribute indicating the field name 
    * **eval**
          o python expression that indicating the value to add 
    * **ref**
          o reference to an id defined in this file 

function tag
~~~~~~~~~~~~

    * model:
    * name:
    * eval
          o should evaluate to the list of parameters of the method to be called, excluding cr and uid 

Example
~~~~~~~
::

	<function model="ir.ui.menu" name="search" eval="[[('name','=','Operations')]]"/>

getitem tag

Takes a subset of the evaluation of the last child node of the tag.

    * type
          - int or list 
    * index
    * int or string (a key of a dictionary) 

Example
~~~~~~~

Evaluates to the first element of the list of ids returned by the function node

.. code-block :: python

	<getitem index="0" type="list">
	    <function model="ir.ui.menu" name="search" eval="[[('name','=','Operations')]]"/>
	</getitem>

CSV Files 
---------

Importing from a CSV
++++++++++++++++++++

Instead of using .XML file, you can import .CSV files. It is simpler but the migration system does not migrate the data imported from the .CSV files. It's like the noupdate attribute in .XML files. It's also more difficult to keep track of relations between ressources and it is more slower at the installation of the server.

Use this only for demo data that will never been upgraded from one version of Tiny ERP to another.

The name of the object is the name of the file before the first '-'. You must use one file per object to import. For example, to import a file with partners (including their multiple contacts and events), the file must be named like one of the following example:

    * res.partner.csv
    * res.partner-tiny_demo.csv
    * res.partner-tiny.demo.csv 

Structure of the CSV file
+++++++++++++++++++++++++

Have a look at the user manual for a complete description on how to construct your .CSV file.

Usefull info:

    * Separator of field: ,
    * Quote of fields: "
    * Encoding to use: UTF-8 

Export demo data and import it from a module
++++++++++++++++++++++++++++++++++++++++++++

You can import .CSV file that have been exported from the Tiny ERP client. This is interesting to create your own demo module. But both formats are not exactly the same, mainly due to the conversion: Structured Data -> Flat Data -> Structured Data.

    * The name of the column (first line of the .CSV file) use the end user term in his own language when you export from the client. If you want to import from a module, you must convert the first column using the fields names. Example, from the partner form: 

    Name,Code,Contacts/Contact Name,Contacts/Street,Contacts/Zip

        becomes 

    name,ref,address/name,address/street,address/zip 

    * When you export from the Tiny ERP client, you can select any many2one fields and their child's relation. When you import from a module, Tiny ERP tries to recreate the relation between the two resources. For example, do not export something like this from a sale order form - otherwise Tiny ERP will not be able to import your file: 

    Order Description,Partner/Name,Partner/Payable,Partner/Address/Name 

    * To find the link for a many2one or many2many field, the server use the name_search function when importing. So, for a many2one field, it is better to export the field 'name' or 'code' of the related resource only. Use the more unique one. Be sure that the field you export is searchable by the name_search function. (the 'name' column is always searchable). 

    Order Description,Partner/Code 

    * Change the title of the column for all many2many or many2one fields. It's because you export the related resource and you import a link on the resource. Example from a sale order: Partner/Code should become partner_id and not partner_id/code. If you kept the @@/code@@, Tiny ERP will try to create those entries in the database instead of finding reference to existing ones. 

    * Many2many fields. If all the exported data contains 0 or 1 relation on each many2many fields, there will be no problem. Otherwise, the export will result in one line per many2many. The import function expect to get all many2many relations in one column, separated by a comma. So, you have to make to transformation. For example, if the categories "Customer" and "Supplier" already exists : 

    name,category_id 
    Smith, "Customer, Supplier" 

If you want to create these two categories you can try :

    name,category_id/name 
    Smith, "Customer, Supplier" 

This does not work as expected: a category "Customer, Supplier" is created. The solution is to create an empty line with only the second category:


    name,category_id/name 
    Smith, Customer 
    ,Supplier 

(Note the comma before "Supplier").


    * Read only fields. Do not try to import read only fields like the amount receivable or payable for a partner. Otherwise, Tiny ERP will not accept to import your file. 

    * Exporting trees. You can export and import tree structures using the parent field. You just have to take care of the import order. The parent have to be created before his child's. 

Use record id like in xml file:
+++++++++++++++++++++++++++++++

It's possible to define an id for each line of the csv file. This allow to define references between records:

    id, name, parent_id:id 
    record_one, Father, 
    record_two, Child, record_one 

If you do this, the line with the parent data must be before the child lines in the file. 

Multiple CSV Files 
------------------

Importing from multiple CSV a full group of linked data
+++++++++++++++++++++++++++++++++++++++++++++++++++++++

It' possible to import a lot of data, with multiple CSV files imported as a single operation. Assume we have a database with books and authors with a relation many2many between book and author.

And that you already have a file with a lot of books (like a library) and an other file with a lot of authors and a third file with the links between them.

How to import that easily in openERP ?

Definition of an import module
++++++++++++++++++++++++++++++

You can do this in the module you have defined to manage yours books and authors. but Sometimes, the tables to import can also be in several modules.

For this example, let's say that 'book' object is defined in a module called 'library_management' and that 'Author' object in a module called 'contact_name'.

In this case, you can create a 'fake' module, just to import the data for all these multiples modules. Call this importation module : 'import_my_books'.

You create this module as others modules of OpenObject :

   1. create a folder 'import_my_books'
   2. inside, create a '__init__.py' file with only one line : import import_my_books
   3. again, in the same folder, create a '__terp__.py' file and in this file, write the following code : 

.. code-block :: python


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


Creation of CSV files
+++++++++++++++++++++

For the CSV files, you'll import one the after, the other one.

So you have to choose, in which way you'll treat the many2many relation. For our example, we've choose to import all the authors, then all the books with the links to the authors.

   1. authors CSV file 

You have to put your data in a CSV file without any link to books (because the book ids will be known only AFTERWARDS...) For example : ("contact_name.author.csv")

::

	 id,last_name,first_name,type
	 author_1,Bradley,Marion Zimmer,Book writer
	 author_2,"Szu T'su",,Chinese philosopher
	 author_3,Zelazny,Roger,Book writer
	 author_4,Arleston,Scotch,Screen Writer
	 author_5,Magnin,Florence,Comics Drawer
	 ...

   1. Books CSV file 

Here, you can put the data about your books, but also, the links to the authors, using the same id as the column 'id' of the author CSV file. For example : ("library.book.csv" )

::

	 id,title,isbn,pages,date,author_ids:id
	 book_a,Les Cours du Chaos,1234567890123,268,1975-12-25,"author_3"
	 book_b,"L'art de la Guerre, en 219 volumes",1234567890124,1978-01-01,"author_2"
	 book_c,"new marvellous comics",1587459248579,2009-01-01,"author_5,author_4"
	 ...

Five remarks :

   1. the field content must be enclosed in double quotes (") if there is a double quote or a comma in the field.
   2. the dates are in the format YYYY-MM-DD
   3. if you have many ids in the same column, you must separate them with a comma, and, by the way, you must enclosed the content of the column between double quotes...
   4. the name of the field is the same as the name of the field in the class definition AND must be followed by ':id' if the content is an ID that must be interpreted by the import module. In fact, "author_4" will be transformed by the import module in an integer id for the database module and this numercial id will be put also in the table between author and book, not the literal ID (author_4).
   5. the encoding to be used by the CSV file is the 'UTF-8' encoding 

Links between id if the CSV files
+++++++++++++++++++++++++++++++++

Links to id already in the system 
+++++++++++++++++++++++++++++++++


XML data files convention
-------------------------


Developers:Developper's Book/Data Loading/XMLFilesConventions


Jump to: navigation, search

The ressources are placed in different files according to their uses. By convention;

 .. csv-table:: 
   :header: "Name","Description"
   :widths: 25, 25

   "modulename_workflow.xml","the definitions of workflows"
   "modulename_view.xml","the views"
   "modulename_data.xml","the important datas to download"
   "modulename_report.xml","the reports declarations"
   "modulename_demo.xml","the useful datas for the demo version"



The workflow files have to be loaded before the datas ! Otherwise, the ressource created won't be integrated inside the workflow because the later is not yet defined.


Managing updates 
----------------

Managing updates and migrations
+++++++++++++++++++++++++++++++

Open ERP has a built'in migration and upgrade system which allows updates to be nearly (or often) automatic. This system also allows to easily incorporate custom modules.

Table/Object structure
""""""""""""""""""""""

When you run openerp-server with option --init or --update, the table structure are updated to match the new description that is in .py files. Fields that are removed are not removed in the postgresql database not to lose data.

So, simply running --update or --init, will upgrade your table structure.

It's important to run --init=module the first time you install the module. Next time, you must use the --update=module argument instead of the init one. This is because init loads ressources that are loaded only once and never upgraded (eg: ressources with no id="" attribute or within a noupdate="1" <data> tag).


Data
""""
Some data is automatically loaded at the installation of Tiny ERP:

    * views, actions, menus,
    * workflows,
    * demo data 

This data is also migrated to a new version if you run --update or --init.

Workflows
"""""""""

Workflows are also upgraded automatically. If some activities are removed, the documents states evolves automatically to the preceding activities. That ensure that all documents are always in valid states.

You can freely remove activities in your XML files. If workitems are in this activity, they will evolve to the preceding unlinked activity. And after the activity will be removed.

Things to care about during development
"""""""""""""""""""""""""""""""""""""""

Since version 3.0.2 of Tiny ERP, you can not use twice the same 'id="..."' during resource creation in your XML files, unless they are in two different modules.

Resources which don't contain an id are created (and updated) only once; at the installation of the module or when you use the --init argument.

If a resource has an id and this resource is not present anymore in the next version of the XML file, Open ERP will automatically remove it from the database. If this resource is still present, Open ERP will update the modifications to this resource.

If you use a new id, the resource will be automatically created at the next update of this module.

**Use explicit id declaration !**, Example:

    * view_invoice_form,
    * view_move_line_tree,
    * action_invoice_form_open, ... 

It is important to put id="...." to all record that are important for the next version migrations. For example, do not forget to put some id="..." on all workflows transitions. This will allows Open ERP to know which transition has been removed and which transition is new or updated.

Custom modules
""""""""""""""

For example, if you want to override the view of an object named 'invoice_form' in your xml file (id="invoice_form"). All you have to do is redefine this view in your custom module with the same id. You can prefix ids with the name of the module to reference an id defined in another module.

Example:

    <record model="ir.ui.view" id="account.invoice_form"> 
    ... 
    <record> 

This will override the invoice form view. You do not have to delete the old view, like in 3.0 versions of Open ERP.

Note that it is often better to use view inherytancy instead of overwritting views.

In this migration system, you do not have to delete any ressource. The migration system will detect if it is an update or a delete using id="..." attributes. This is important to preserve references duing migrations.

Demo datas
""""""""""

Demo datas do not have to be upgraded; because they are probably modified, deleted, ... by users. So, to avoid demo data to be upgraded, you can put a noupdate="1" attribute in the <data> tag of your .xml data files.

Summary of update and init process
++++++++++++++++++++++++++++++++++

init:

    modify/add/delete demo data and builtin data 

update:

    modifiy/add/delete non demo data 

Examples of builtin (non demo) data:

    * Menu structure, 
    * View definition, 
    * Workflow description, ... 
      -> Everything that as an id="..." in the .XML data declaration (if no attr noupdate="1" in the header) 

What's going on on a update process:

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


