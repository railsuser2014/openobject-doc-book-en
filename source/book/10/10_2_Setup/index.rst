******************************
Configuration and Installation
******************************

Setup a database
================

Explain how to start on Odoo.

* Subscribe on Odoo
* Connect to your database

Or install manually:

* Install manually
* Create a database

.. note:: Exercice 1 - Install a working Open ERP

    As to configure the system, you must start by preparing a new database for
    NotSoTiny. During the process, you must configure the header/footer of the
    NotSoTiny documents. Put them a logo and their address:

        NotSoTiny SARL
        Rue du Nid 1
        75000 Paris
        France

NotSoTiny plans to use Open ERP to manage all their activitities. The basic
requirements of NotSoTiny company have been defined above, so now you have the
responsibility to install and configure the database by selecting the modules
which will be used by NotSoTiny company.

You must take into account all the departments, but in order not to complicate
the system, you should not install the modules which won't be used by NotSoTiny
company. It's better to install too few modules, than too much modules.

.. note:: Exercice 2 - Install the required modules

    As to configure the system, you should install and configure modules required
    by the NotSoTiny company. Have a look at all their activities and department
    to select which module will fit best their needs.

Configure the system
====================

Then, we instruct a person in charge of the company to provide us with an
inventory of various users. The following simplified table has been provided
by NotSoTiny.

---------------------------------------------------
| Employee | Role | Login | Password | Activities |
---------------------------------------------------
|Fabien Dupont|CEO|fabien|fabien|Must access all features, except administration of the ERP|
|Luc Lecoq|CSO & CFO|luc|luc|Should access all financial and sales documents.|
|Eric Dubois|Worker|eric|eric|Do only production orders, must have the simplest menu possible|
---------------------------------------------------------------------------------------

.. note:: Exercice 3 - Create the different users and set their access rights

    Define the different users and assign them to the right groups. As this is
    just a prototype for the demonstration purpose, just assign existing groups,
    without creating specific rules.

Luc Lecoq, the founder and sales/financial director insisted to have a sales
dashboard that appears automatically when he logs into the system. Because each
morning, when he arrives at the office, the first things he needs is his sales
statistics.

.. note:: Exercice 4 - Assign a sales dashboard at Luc's connection

    Setup a sales manager dashboard to Luc. This dashboard must appear when
    he logs in.

Fabien thinks that one of the biggest value of their company is their customer
database. Since the beginning of the company, they have very strict rules on how
to keep and maintain their customer database. One of his requirement for his
ERP system is that noone should be able to delete a partner for the database.

Fabien must be the only user that have the ability to delete a user from 
the database.

.. note:: Exercice 5 - Modify security rules

   Create a new group for users that have the right to delete a partner. The
   others groups should not have the rights to delete a partner. Assign this
   newly created group to Fabien.


Setup the base data
===================

As to prepare your prototype, you requested NotSoTiny to give you files that
contains their main data. The goal is to import all their partners into the
database.

They exported three tables from their old Sage software:

* Categories of customers and suppliers
* List of customers
* List of suppliers

NotSoTiyn sent you three .CSV (Comma Separated Values) files containing these
data. Here is a copy of some of the records contained in these files.

  categories.csv
  Consummers
  Retailers
  Wood Suppliers
  Miscelleanous Suppliers

  customers.csv
  Name,Contact Name,City,Country,Category
  The Shelve House,Henry Chard,Paris,France,Retailers
  ZeroOne Inc,Geoff,Bruxelles,Belgium,Consummers

  suppliers.csv
  Name,Contact Name,City,Country,Category
  Wood y Wood Pecker,Roger Pecker,Kainuu,Finland,Wood Suppliers
  Vicking Direct,,Bruxelles,Belgium,Miscelleanous Suppliers

.. note:: Exercice 6 - Define categories of partners

   Define the categories of partners. As they are only a few categories,
   we suggest you to encode them manually. As to provide a good service
   to NotSoTiny, you can structure their categories in a hyerarchical tree.

.. note:: Exercice 7 - Import Partners

   NotSoTiny provided a file with about 1200 customers and 200 suppliers.
   So you will have to import these partners using the .CSV import tools
   of Open ERP. Create a .CSV file yourself with these few lines.

.. note:: Question 8 - What's the easiest way to list all wood suppliers ?

   How will you do to list all "Wood Suppliers" ?


Setup the products
==================

After a quick analysis of their products, Luc, the sales manager
gave you a list of all their products's categories. Here it is:

* Sellable Products

  * Services
  * Shelves

* Others Products

.. note:: Exercice 8 - Categories of products.

    Before setting up the products, you must define the available categories
    of products. Create the tree structure of the categories of products, using
    the data provided by Luc, the sales manager.


NotSoTiny did not provided their exportation of their products yet.
As to not take delay in the project, you decided to manually encode
a few products manually. You will encode only threee products at the
moment but encode much more when you will receive their full range
of products.

Here is a list of some products to encode, with their main characteristics:

| Code | Description | Type | Unit of Measure | Cust.Price | Cost | Method | Supplier | Delivery Delay |
-------------------------------------------------------------------------------------------------------
|ARM100|Shelf of 100cm| Product | Unit | 130€ | 50€ | Produce | / | / |
|ARM200|Shelf of 200cm| Product | Unit | 210€ | 80€ | Produce | / | / |
|WOOD002|Wood 2mm| Product | Meter | 10€ | 5€ | Buy | Wood y Wood Pecker | 2 Weeks |
|PROJ|Cooking Design Project| Service | Hour | 90€ | 20€ | Produce | / | / |

.. note:: Exercice 9 - Products.

    Setup the above products in the NotSoTiny database.


As to be able to sell some products, you will encode a starting inventory.
Currently, here is the stock level of the above products:

| Code | Stock |
----------------
|ARM100|50 Units|
|ARM200|20 Units|
|WOOD002|120 Meters|

.. note:: Exercice 10 - Create the initial stock inventory.

    Create the initial stock inventory. Once the inventory is confirmed you
    should see the real stock of each product on the product form.


.. note:: Exercice 11 - Test the system

    You should now be able to test the system. Perform the following operations:

    * Create a Quotation:
    
        * Customer : ZeroOne Inc
        * Products : 1 Cooking Design Project, 3 Shelves 100cm

    * Convert the quotation to a sale order
    * Deliver the shelves to the customer
    * Generate the draft invoice
    * Confirm the invoice and print it


.. note:: Exercice 12 - Check stock level

    You should now test the stock level of the ARM100 product. It should have
    47 Units in stock.


