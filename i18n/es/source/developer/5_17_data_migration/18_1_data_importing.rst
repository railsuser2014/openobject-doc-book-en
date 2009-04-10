
.. i18n: Data Importation
.. i18n: ================

Data Importation
================

.. i18n: Introduction
.. i18n: ------------

Introduction
------------

.. i18n: There are different methods to import your data into Open ERP:

There are different methods to import your data into Open ERP:

.. i18n: * Through the web-service interface
.. i18n: * Using CSV files through the client interface
.. i18n: * Building a module with .XML or .CSV files with the content
.. i18n: * Directly into the SQL database, using an ETL

* Through the web-service interface
* Using CSV files through the client interface
* Building a module with .XML or .CSV files with the content
* Directly into the SQL database, using an ETL

.. i18n: Importing data through a module
.. i18n: -------------------------------

Importing data through a module
-------------------------------

.. i18n: The best way to import data in Open ERP is to build a module that
.. i18n: integrates all the data you want to import. So, when you want to
.. i18n: import all the data, you just have to install the module and Open ERP
.. i18n: manages the different creation operations. When you have lots of different
.. i18n: data to import, we sometimes create different modules.

The best way to import data in Open ERP is to build a module that
integrates all the data you want to import. So, when you want to
import all the data, you just have to install the module and Open ERP
manages the different creation operations. When you have lots of different
data to import, we sometimes create different modules.

.. i18n: So, let's create a new module where we will store all our datas. To do
.. i18n: this, from the addons directory, create a new module called data_yourcompany.

So, let's create a new module where we will store all our datas. To do
this, from the addons directory, create a new module called data_yourcompany.

.. i18n: * mkdir data_yourcompany
.. i18n: * cd data_yourcompany
.. i18n: * touch __init__.py

* mkdir data_yourcompany
* cd data_yourcompany
* touch __init__.py

.. i18n: You must also create a file called __terp__.py in this new module.
.. i18n: Write the following content in this module file description.

You must also create a file called __terp__.py in this new module.
Write the following content in this module file description.

.. i18n: .. code-block:: python
.. i18n: 
.. i18n:   {
.. i18n:     'name': 'Module for Data Importation',
.. i18n:     'version': '1.0',
.. i18n:     'category': 'Generic Modules/Others',
.. i18n:     'description': "Sample module for data importation.",
.. i18n:     'author': 'Tiny',
.. i18n:     'website': 'http://www.openerp.com',
.. i18n:     'depends': ['base'],
.. i18n:     'init_xml': [
.. i18n:         'res.partner.csv',
.. i18n:         'res.partner.address.csv'
.. i18n:     ],
.. i18n:     'update_xml': [],
.. i18n:     'installable': True,
.. i18n:     'active': False,
.. i18n:   }

.. code-block:: python

  {
    'name': 'Module for Data Importation',
    'version': '1.0',
    'category': 'Generic Modules/Others',
    'description': "Sample module for data importation.",
    'author': 'Tiny',
    'website': 'http://www.openerp.com',
    'depends': ['base'],
    'init_xml': [
        'res.partner.csv',
        'res.partner.address.csv'
    ],
    'update_xml': [],
    'installable': True,
    'active': False,
  }

.. i18n: The following module will import two different files:

The following module will import two different files:

.. i18n: * res.partner.csv : a CSV file containing records of the res.partner object
.. i18n: * res.partner.address.csv : a CSV file containing records of the res.partner.address object

* res.partner.csv : a CSV file containing records of the res.partner object
* res.partner.address.csv : a CSV file containing records of the res.partner.address object

.. i18n: Once this module is created, you must load data from your old application to
.. i18n: .CSV file that will be loaded in Open ERP. Open ERP has a builtin system to
.. i18n: manage identifications columns of the original software.

Once this module is created, you must load data from your old application to
.CSV file that will be loaded in Open ERP. Open ERP has a builtin system to
manage identifications columns of the original software.

.. i18n: For this exercice, we will load data from another Open ERP database called old.
.. i18n: As this database is in SQL, it's quite easy to export the data using the command
.. i18n: line postgresql client: psql. As to get a result that looks like a .CSV fiel,
.. i18n: we will use the following arguments of psql:

For this exercice, we will load data from another Open ERP database called old.
As this database is in SQL, it's quite easy to export the data using the command
line postgresql client: psql. As to get a result that looks like a .CSV fiel,
we will use the following arguments of psql:

.. i18n: * -A : display records without space for the row separators
.. i18n: * -F , : set the separator character as ','
.. i18n: * --pset footer : don't write the latest line that looks like "(21 rows)"

* -A : display records without space for the row separators
* -F , : set the separator character as ','
* --pset footer : don't write the latest line that looks like "(21 rows)"

.. i18n: When you import a .CSV file in Open ERP, you can provide a 'id' column that
.. i18n: contains a uniq identification number or string for the record. We will use
.. i18n: this 'id' column to refer to the ID of the record in the original application.
.. i18n: As to refer to this record from a many2one field, you can use 'FIELD_NAME:id'.
.. i18n: Open ERP will re-create the relationship between the record using this uniq
.. i18n: ID.

When you import a .CSV file in Open ERP, you can provide a 'id' column that
contains a uniq identification number or string for the record. We will use
this 'id' column to refer to the ID of the record in the original application.
As to refer to this record from a many2one field, you can use 'FIELD_NAME:id'.
Open ERP will re-create the relationship between the record using this uniq
ID.

.. i18n: So let's start to export the partners from our database using psql: ::
.. i18n: ::
.. i18n: 
.. i18n: 	  psql trunk -c "select 'partner_'||id as id,name from res_partner" 
.. i18n: 	             -A -F , --pset footer > res.partner.csv

So let's start to export the partners from our database using psql: ::
::

	  psql trunk -c "select 'partner_'||id as id,name from res_partner" 
	             -A -F , --pset footer > res.partner.csv

.. i18n: This creates a res.partner.csv file containing a structure that looks like this:

This creates a res.partner.csv file containing a structure that looks like this:

.. i18n: ::
.. i18n: 
.. i18n: 	  id,name
.. i18n: 	  partner_2,ASUStek
.. i18n: 	  partner_3,Agrolait
.. i18n: 	  partner_4,Camptocamp
.. i18n: 	  partner_5,Syleam

::

	  id,name
	  partner_2,ASUStek
	  partner_3,Agrolait
	  partner_4,Camptocamp
	  partner_5,Syleam

.. i18n: By doing this, we generated data from the res.partner object, by creating a uniq
.. i18n: identification string for each record, which is related to the old application's
.. i18n: ID.

By doing this, we generated data from the res.partner object, by creating a uniq
identification string for each record, which is related to the old application's
ID.

.. i18n: Now, we will export the table with addresses (or contacts) that are linked to
.. i18n: partners through the relation field: partner_id. We will proceed in the same
.. i18n: way to export the data and put them into our module:

Now, we will export the table with addresses (or contacts) that are linked to
partners through the relation field: partner_id. We will proceed in the same
way to export the data and put them into our module:

.. i18n: ::
.. i18n: 
.. i18n:   psql trunk -c "select 'partner_address'||id as id,name,'partner_'||
.. i18n:                 partner_id as \"partner_id:id\" from res_partner_address" 
.. i18n:                 -A -F , --pset footer > res.partner.address.csv

::

  psql trunk -c "select 'partner_address'||id as id,name,'partner_'||
                partner_id as \"partner_id:id\" from res_partner_address" 
                -A -F , --pset footer > res.partner.address.csv

.. i18n: This should create a file called res.partner.address with the following data:

This should create a file called res.partner.address with the following data:

.. i18n:   id,name,partner_id:id
.. i18n:   partner_address2,Benoit Mortier,partner_2
.. i18n:   partner_address3,Laurent Jacot,partner_3
.. i18n:   partner_address4,Laith Jubair,partner_4
.. i18n:   partner_address5,Fabien Pinckaers,partner_4

  id,name,partner_id:id
  partner_address2,Benoit Mortier,partner_2
  partner_address3,Laurent Jacot,partner_3
  partner_address4,Laith Jubair,partner_4
  partner_address5,Fabien Pinckaers,partner_4

.. i18n: When you will install this module, Open ERP will automatically import the partners
.. i18n: and then the address and recreate efficiently the link between the two records.
.. i18n: When installing a module, Open ERP will test and apply the constraints for consistency
.. i18n: of the data. So, when you install this module, it may crash, for example, because
.. i18n: you may have different partners with the same name in the system. (due to the uniq
.. i18n: constraint on the name of a partner). So, you have to clean your data before importing
.. i18n: them.

When you will install this module, Open ERP will automatically import the partners
and then the address and recreate efficiently the link between the two records.
When installing a module, Open ERP will test and apply the constraints for consistency
of the data. So, when you install this module, it may crash, for example, because
you may have different partners with the same name in the system. (due to the uniq
constraint on the name of a partner). So, you have to clean your data before importing
them.

.. i18n: If you plan to upload thousands of records through this technique, you should consider
.. i18n: using the argument '-P' when running the server.

If you plan to upload thousands of records through this technique, you should consider
using the argument '-P' when running the server.

.. i18n:   openerp_server.py -P status.pickle --init=data_yourcompany

  openerp_server.py -P status.pickle --init=data_yourcompany

.. i18n: This method provides a faster importation of the data and, if it crashes in the middle
.. i18n: of the import, it will continue at the same line after rerunning the server. This may
.. i18n: preserves hours of testing when importing big files.

This method provides a faster importation of the data and, if it crashes in the middle
of the import, it will continue at the same line after rerunning the server. This may
preserves hours of testing when importing big files.

.. i18n: Using Open ERP's ETL
.. i18n: --------------------

Using Open ERP's ETL
--------------------

.. i18n: The next version of Open ERP will include an ETL module to allow you
.. i18n: to easily manages complex import jobs. If you are interrested in this
.. i18n: system, you can check the complete specifications and the available
.. i18n: prototype at this location:

The next version of Open ERP will include an ETL module to allow you
to easily manages complex import jobs. If you are interrested in this
system, you can check the complete specifications and the available
prototype at this location:

.. i18n:   bzr branch lp:~openerp-commiter/openobject-addons/trunk-extra-addons/etl

  bzr branch lp:~openerp-commiter/openobject-addons/trunk-extra-addons/etl

.. i18n: ... to be continued ...

... to be continued ...
