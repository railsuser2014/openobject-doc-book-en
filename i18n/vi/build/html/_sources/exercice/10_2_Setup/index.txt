
.. i18n: ******************************
.. i18n: Configuration and Installation
.. i18n: ******************************

******************************
Configuration and Installation
******************************

.. i18n: Setup a database
.. i18n: ================

Setup a database
================

.. i18n: Explain how to start on Odoo.

Explain how to start on Odoo.

.. i18n: * Subscribe on Odoo
.. i18n: * Connect to your database

* Subscribe on Odoo
* Connect to your database

.. i18n: Or install manually:

Or install manually:

.. i18n: * Install manually
.. i18n: * Create a database

* Install manually
* Create a database

.. i18n: .. note:: Exercice 1 - Install a working Open ERP
.. i18n: 
.. i18n:     As to configure the system, you must start by preparing a new database for
.. i18n:     NotSoTiny. During the process, you must configure the header/footer of the
.. i18n:     NotSoTiny documents. Put them a logo and their address:
.. i18n: 
.. i18n:         NotSoTiny SARL
.. i18n:         Rue du Nid 1
.. i18n:         75000 Paris
.. i18n:         France

.. note:: Exercice 1 - Install a working Open ERP

    As to configure the system, you must start by preparing a new database for
    NotSoTiny. During the process, you must configure the header/footer of the
    NotSoTiny documents. Put them a logo and their address:

        NotSoTiny SARL
        Rue du Nid 1
        75000 Paris
        France

.. i18n: NotSoTiny plans to use Open ERP to manage all their activitities. The basic
.. i18n: requirements of NotSoTiny company have been defined above, so now you have the
.. i18n: responsibility to install and configure the database by selecting the modules
.. i18n: which will be used by NotSoTiny company.

NotSoTiny plans to use Open ERP to manage all their activitities. The basic
requirements of NotSoTiny company have been defined above, so now you have the
responsibility to install and configure the database by selecting the modules
which will be used by NotSoTiny company.

.. i18n: You must take into account all the departments, but in order not to complicate
.. i18n: the system, you should not install the modules which won't be used by NotSoTiny
.. i18n: company. It's better to install too few modules, than too much modules.

You must take into account all the departments, but in order not to complicate
the system, you should not install the modules which won't be used by NotSoTiny
company. It's better to install too few modules, than too much modules.

.. i18n: .. note:: Exercice 2 - Install the required modules
.. i18n: 
.. i18n:     As to configure the system, you should install and configure modules required
.. i18n:     by the NotSoTiny company. Have a look at all their activities and department
.. i18n:     to select which module will fit best their needs.

.. note:: Exercice 2 - Install the required modules

    As to configure the system, you should install and configure modules required
    by the NotSoTiny company. Have a look at all their activities and department
    to select which module will fit best their needs.

.. i18n: Configure the system
.. i18n: ====================

Configure the system
====================

.. i18n: Then, we instruct a person in charge of the company to provide us with an
.. i18n: inventory of various users. The following simplified table has been provided
.. i18n: by NotSoTiny.

Then, we instruct a person in charge of the company to provide us with an
inventory of various users. The following simplified table has been provided
by NotSoTiny.

.. i18n: +---------------+-----------+---------+------------+-----------------------------------------------------------------+
.. i18n: |  Employee     |  Role     |  Login  |  Password  |  Activities                                                     |
.. i18n: +===============+===========+=========+============+=================================================================+
.. i18n: | Fabien Dupont | CEO       | fabien  | fabien     | Must access all features, except administration of the ERP      |
.. i18n: +---------------+-----------+---------+------------+-----------------------------------------------------------------+
.. i18n: | Luc Lecoq     | CSO & CFO | luc     | luc        | Should access all financial and sales documents.                |
.. i18n: +---------------+-----------+---------+------------+-----------------------------------------------------------------+
.. i18n: | Eric Dubois   | Worker    | eric    | eric       | Do only production orders, must have the simplest menu possible |
.. i18n: +---------------+-----------+---------+------------+-----------------------------------------------------------------+

+---------------+-----------+---------+------------+-----------------------------------------------------------------+
|  Employee     |  Role     |  Login  |  Password  |  Activities                                                     |
+===============+===========+=========+============+=================================================================+
| Fabien Dupont | CEO       | fabien  | fabien     | Must access all features, except administration of the ERP      |
+---------------+-----------+---------+------------+-----------------------------------------------------------------+
| Luc Lecoq     | CSO & CFO | luc     | luc        | Should access all financial and sales documents.                |
+---------------+-----------+---------+------------+-----------------------------------------------------------------+
| Eric Dubois   | Worker    | eric    | eric       | Do only production orders, must have the simplest menu possible |
+---------------+-----------+---------+------------+-----------------------------------------------------------------+

.. i18n: .. note:: Exercice 3 - Create the different users and set their access rights
.. i18n: 
.. i18n:     Define the different users and assign them to the right groups. As this is
.. i18n:     just a prototype for the demonstration purpose, just assign existing groups,
.. i18n:     without creating specific rules.

.. note:: Exercice 3 - Create the different users and set their access rights

    Define the different users and assign them to the right groups. As this is
    just a prototype for the demonstration purpose, just assign existing groups,
    without creating specific rules.

.. i18n: Luc Lecoq, the founder and sales/financial director insisted to have a sales
.. i18n: dashboard that appears automatically when he logs into the system. Because each
.. i18n: morning, when he arrives at the office, the first things he needs is his sales
.. i18n: statistics.

Luc Lecoq, the founder and sales/financial director insisted to have a sales
dashboard that appears automatically when he logs into the system. Because each
morning, when he arrives at the office, the first things he needs is his sales
statistics.

.. i18n: .. note:: Exercice 4 - Assign a sales dashboard at Luc's connection
.. i18n: 
.. i18n:     Setup a sales manager dashboard to Luc. This dashboard must appear when
.. i18n:     he logs in.

.. note:: Exercice 4 - Assign a sales dashboard at Luc's connection

    Setup a sales manager dashboard to Luc. This dashboard must appear when
    he logs in.

.. i18n: Fabien thinks that one of the biggest value of their company is their customer
.. i18n: database. Since the beginning of the company, they have very strict rules on how
.. i18n: to keep and maintain their customer database. One of his requirement for his
.. i18n: ERP system is that noone should be able to delete a partner for the database.

Fabien thinks that one of the biggest value of their company is their customer
database. Since the beginning of the company, they have very strict rules on how
to keep and maintain their customer database. One of his requirement for his
ERP system is that noone should be able to delete a partner for the database.

.. i18n: Fabien must be the only user that have the ability to delete a user from 
.. i18n: the database.

Fabien must be the only user that have the ability to delete a user from 
the database.

.. i18n: .. note:: Exercice 5 - Modify security rules
.. i18n: 
.. i18n:    Create a new group for users that have the right to delete a partner. The
.. i18n:    others groups should not have the rights to delete a partner. Assign this
.. i18n:    newly created group to Fabien.

.. note:: Exercice 5 - Modify security rules

   Create a new group for users that have the right to delete a partner. The
   others groups should not have the rights to delete a partner. Assign this
   newly created group to Fabien.

.. i18n: Setup the base data
.. i18n: ===================

Setup the base data
===================

.. i18n: As to prepare your prototype, you requested NotSoTiny to give you files that
.. i18n: contains their main data. The goal is to import all their partners into the
.. i18n: database.

As to prepare your prototype, you requested NotSoTiny to give you files that
contains their main data. The goal is to import all their partners into the
database.

.. i18n: They exported three tables from their old Sage software:

They exported three tables from their old Sage software:

.. i18n: * Categories of customers and suppliers
.. i18n: * List of customers
.. i18n: * List of suppliers

* Categories of customers and suppliers
* List of customers
* List of suppliers

.. i18n: NotSoTiyn sent you three .CSV (Comma Separated Values) files containing these
.. i18n: data. Here is a copy of some of the records contained in these files.

NotSoTiyn sent you three .CSV (Comma Separated Values) files containing these
data. Here is a copy of some of the records contained in these files.

.. i18n:   categories.csv
.. i18n:   Consummers
.. i18n:   Retailers
.. i18n:   Wood Suppliers
.. i18n:   Miscelleanous Suppliers

  categories.csv
  Consummers
  Retailers
  Wood Suppliers
  Miscelleanous Suppliers

.. i18n:   customers.csv
.. i18n:   Name,Contact Name,City,Country,Category
.. i18n:   The Shelve House,Henry Chard,Paris,France,Retailers
.. i18n:   ZeroOne Inc,Geoff,Bruxelles,Belgium,Consummers

  customers.csv
  Name,Contact Name,City,Country,Category
  The Shelve House,Henry Chard,Paris,France,Retailers
  ZeroOne Inc,Geoff,Bruxelles,Belgium,Consummers

.. i18n:   suppliers.csv
.. i18n:   Name,Contact Name,City,Country,Category
.. i18n:   Wood y Wood Pecker,Roger Pecker,Kainuu,Finland,Wood Suppliers
.. i18n:   Vicking Direct,,Bruxelles,Belgium,Miscelleanous Suppliers

  suppliers.csv
  Name,Contact Name,City,Country,Category
  Wood y Wood Pecker,Roger Pecker,Kainuu,Finland,Wood Suppliers
  Vicking Direct,,Bruxelles,Belgium,Miscelleanous Suppliers

.. i18n: .. note:: Exercice 6 - Define categories of partners
.. i18n: 
.. i18n:    Define the categories of partners. As they are only a few categories,
.. i18n:    we suggest you to encode them manually. As to provide a good service
.. i18n:    to NotSoTiny, you can structure their categories in a hyerarchical tree.

.. note:: Exercice 6 - Define categories of partners

   Define the categories of partners. As they are only a few categories,
   we suggest you to encode them manually. As to provide a good service
   to NotSoTiny, you can structure their categories in a hyerarchical tree.

.. i18n: .. note:: Exercice 7 - Import Partners
.. i18n: 
.. i18n:    NotSoTiny provided a file with about 1200 customers and 200 suppliers.
.. i18n:    So you will have to import these partners using the .CSV import tools
.. i18n:    of Open ERP. Create a .CSV file yourself with these few lines.

.. note:: Exercice 7 - Import Partners

   NotSoTiny provided a file with about 1200 customers and 200 suppliers.
   So you will have to import these partners using the .CSV import tools
   of Open ERP. Create a .CSV file yourself with these few lines.

.. i18n: .. note:: Question 8 - What's the easiest way to list all wood suppliers ?
.. i18n: 
.. i18n:    How will you do to list all "Wood Suppliers" ?

.. note:: Question 8 - What's the easiest way to list all wood suppliers ?

   How will you do to list all "Wood Suppliers" ?

.. i18n: Setup the products
.. i18n: ==================

Setup the products
==================

.. i18n: After a quick analysis of their products, Luc, the sales manager
.. i18n: gave you a list of all their products's categories. Here it is:

After a quick analysis of their products, Luc, the sales manager
gave you a list of all their products's categories. Here it is:

.. i18n: * Sellable Products
.. i18n: 
.. i18n:   * Services
.. i18n:   * Shelves
.. i18n: 
.. i18n: * Others Products

* Sellable Products

  * Services
  * Shelves

* Others Products

.. i18n: .. note:: Exercice 8 - Categories of products.
.. i18n: 
.. i18n:     Before setting up the products, you must define the available categories
.. i18n:     of products. Create the tree structure of the categories of products, using
.. i18n:     the data provided by Luc, the sales manager.

.. note:: Exercice 8 - Categories of products.

    Before setting up the products, you must define the available categories
    of products. Create the tree structure of the categories of products, using
    the data provided by Luc, the sales manager.

.. i18n: NotSoTiny did not provided their exportation of their products yet.
.. i18n: As to not take delay in the project, you decided to manually encode
.. i18n: a few products manually. You will encode only threee products at the
.. i18n: moment but encode much more when you will receive their full range
.. i18n: of products.

NotSoTiny did not provided their exportation of their products yet.
As to not take delay in the project, you decided to manually encode
a few products manually. You will encode only threee products at the
moment but encode much more when you will receive their full range
of products.

.. i18n: Here is a list of some products to encode, with their main characteristics:

Here is a list of some products to encode, with their main characteristics:

.. i18n: +---------+------------------------+-----------+-------------------+--------------+---------+-----------+----------------------+------------------+
.. i18n: |  Code   |  Description           |  Type     |  Unit of Measure  |  Cust.Price  |  Cost   |  Method   |  Supplier            |  Delivery Delay  |
.. i18n: +=========+========================+===========+===================+==============+=========+===========+======================+==================+
.. i18n: | ARM100  | Shelf of 100cm         |  Product  |  Unit             |  130€        |  50€    |  Produce  |  /                   |  /               |
.. i18n: +---------+------------------------+-----------+-------------------+--------------+---------+-----------+----------------------+------------------+
.. i18n: | ARM200  | Shelf of 200cm         |  Product  |  Unit             |  210€        |  80€    |  Produce  |  /                   |  /               |
.. i18n: +---------+------------------------+-----------+-------------------+--------------+---------+-----------+----------------------+------------------+
.. i18n: | WOOD002 | Wood 2mm               |  Product  |  Meter            |  10€         |  5€     |  Buy      |  Wood y Wood Pecker  |  2 Weeks         |
.. i18n: +---------+------------------------+-----------+-------------------+--------------+---------+-----------+----------------------+------------------+
.. i18n: | PROJ    | Cooking Design Project |  Service  |  Hour             |  90€         |  20€    |  Produce  |  /                   |  /               |
.. i18n: +---------+------------------------+-----------+-------------------+--------------+---------+-----------+----------------------+------------------+

+---------+------------------------+-----------+-------------------+--------------+---------+-----------+----------------------+------------------+
|  Code   |  Description           |  Type     |  Unit of Measure  |  Cust.Price  |  Cost   |  Method   |  Supplier            |  Delivery Delay  |
+=========+========================+===========+===================+==============+=========+===========+======================+==================+
| ARM100  | Shelf of 100cm         |  Product  |  Unit             |  130€        |  50€    |  Produce  |  /                   |  /               |
+---------+------------------------+-----------+-------------------+--------------+---------+-----------+----------------------+------------------+
| ARM200  | Shelf of 200cm         |  Product  |  Unit             |  210€        |  80€    |  Produce  |  /                   |  /               |
+---------+------------------------+-----------+-------------------+--------------+---------+-----------+----------------------+------------------+
| WOOD002 | Wood 2mm               |  Product  |  Meter            |  10€         |  5€     |  Buy      |  Wood y Wood Pecker  |  2 Weeks         |
+---------+------------------------+-----------+-------------------+--------------+---------+-----------+----------------------+------------------+
| PROJ    | Cooking Design Project |  Service  |  Hour             |  90€         |  20€    |  Produce  |  /                   |  /               |
+---------+------------------------+-----------+-------------------+--------------+---------+-----------+----------------------+------------------+

.. i18n: .. note:: Exercice 9 - Products.
.. i18n: 
.. i18n:     Setup the above products in the NotSoTiny database.

.. note:: Exercice 9 - Products.

    Setup the above products in the NotSoTiny database.

.. i18n: As to be able to sell some products, you will encode a starting inventory.
.. i18n: Currently, here is the stock level of the above products:

As to be able to sell some products, you will encode a starting inventory.
Currently, here is the stock level of the above products:

.. i18n: +---------+------------+
.. i18n: |  Code   |  Stock     |
.. i18n: +=========+============+
.. i18n: | ARM100  | 50 Units   |
.. i18n: +---------+------------+
.. i18n: | ARM200  | 20 Units   |
.. i18n: +---------+------------+
.. i18n: | WOOD002 | 120 Meters |
.. i18n: +---------+------------+

+---------+------------+
|  Code   |  Stock     |
+=========+============+
| ARM100  | 50 Units   |
+---------+------------+
| ARM200  | 20 Units   |
+---------+------------+
| WOOD002 | 120 Meters |
+---------+------------+

.. i18n: .. note:: Exercice 10 - Create the initial stock inventory.
.. i18n: 
.. i18n:     Create the initial stock inventory. Once the inventory is confirmed you
.. i18n:     should see the real stock of each product on the product form.

.. note:: Exercice 10 - Create the initial stock inventory.

    Create the initial stock inventory. Once the inventory is confirmed you
    should see the real stock of each product on the product form.

.. i18n: .. note:: Exercice 11 - Test the system
.. i18n: 
.. i18n:     You should now be able to test the system. Perform the following operations:
.. i18n: 
.. i18n:     * Create a Quotation:
.. i18n:     
.. i18n:         * Customer : ZeroOne Inc
.. i18n:         * Products : 1 Cooking Design Project, 3 Shelves 100cm
.. i18n: 
.. i18n:     * Convert the quotation to a sale order
.. i18n:     * Deliver the shelves to the customer
.. i18n:     * Generate the draft invoice
.. i18n:     * Confirm the invoice and print it

.. note:: Exercice 11 - Test the system

    You should now be able to test the system. Perform the following operations:

    * Create a Quotation:
    
        * Customer : ZeroOne Inc
        * Products : 1 Cooking Design Project, 3 Shelves 100cm

    * Convert the quotation to a sale order
    * Deliver the shelves to the customer
    * Generate the draft invoice
    * Confirm the invoice and print it

.. i18n: .. note:: Exercice 12 - Check stock level
.. i18n: 
.. i18n:     You should now test the stock level of the ARM100 product. It should have
.. i18n:     47 Units in stock.

.. note:: Exercice 12 - Check stock level

    You should now test the stock level of the ARM100 product. It should have
    47 Units in stock.
