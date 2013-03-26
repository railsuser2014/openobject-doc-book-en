Business Example
================

In this example, you will configure a system that enables you to:

* buy products from a supplier,

* stock the products in a warehouse,

* sell these products to a customer.

The system should support all aspects of invoicing, payments to suppliers and receipts from
customers.

Basic Settings
==============

For this business case, you will have to model:

* the suppliers and a supplier category,

* the customers and a customer category,

* some products and a product category,

* an inventory,

* a purchase order,

* a sales order,

* invoices,

* payments.

To test the system, you will need at least one supplier, one customer, one product, a warehouse, a
minimal chart of accounts and a bank account.

Get your Database Up and Running without Demo Data
==================================================

Use the technique outlined in :ref:`sect-dbcreate` to create a new database, \ ``openerp_ch03``\  . This
database will be free of data and contain the least possible amount of functionality as a starting
point. You will need to know your super administrator password for this – or you will have to find
somebody who does have it to create this seed database. You will not be able to use the \
``openerp_ch01``\   or \ ``openerp_ch02``\   databases that you might have created so far in this book
because they both contain demonstration data.

Start the database creation process from the :guilabel:`Welcome` page by clicking
:guilabel:`Manage Databases` and then completing the following fields on the :guilabel:`Create Database` form, as shown in :ref:`fig-oech03`:

*  :guilabel:`Super admin password` : by default it is \ ``admin`` \, if you or your system
   administrator have not changed it,

*  :guilabel:`New database name` : \ ``openerp_ch03``\  ,

*  :guilabel:`Load Demonstration data` checkbox: \ ``not checked``\  (**this step is very important, but catches out many people**),

*  :guilabel:`Default Language` : \ ``English (US)``\  ,

*  :guilabel:`Administrator password` : \ ``admin``\  (because it is the easiest to remember at this stage, but obviously completely insecure),

*  :guilabel:`Confirm password` : \ ``admin``\  .

.. _fig-oech03:

.. figure::  images/openerp_ch03.png
   :scale: 50
   :align: center

   *Creating a blank database*

Then click :guilabel:`Create Database` to create the database and move to the Application screen :ref:`fig-oech03s1`.

.. _fig-oech03s1:

.. figure::  images/openerp_ch03_s1.png
   :scale: 50
   :align: center

   *Setting up a blank database - first screen*

You can have the screen as shown in above screenshot :ref:`fig-oech03s1`.


Fit your Needs
==============

Functional needs can be provided by core modules from OpenERP. You just have to decide which functionality
you want in your system. Click `Install` button of the corresponding application in the :ref:`fig-oech03cfsimp`.

.. index::
   single: module; product
   single: module; stock
   single: module; account
   single: module; purchase
   single: module; sale

For this instance, we need the following applications:

* Accounting & Finance (the :mod:`account` module),

* Warehouse Management (the :mod:`stock` module),

* Purchase Management (the :mod:`purchase` module),

* Sales Management (the :mod:`sale` module).

To get OpenERP to install these business applications,screens should look as follows:

.. _fig-oech03cfsimp:

.. figure:: images/openerp_feature.png
   :scale: 50
   :align: center

   *At the time of Installation*

:guilabel:`Skip` the step that asks you to configure your Accounting Chart. OpenERP will now display the opening screen with all selected business applications installed.

.. _fig-oech03cfgexample:

.. figure:: images/openerp_ch03_main.png
   :scale: 50
   :align: center

   *Database with all required functionality for this example*


.. Copyright © Open Object Press. All rights reserved.

.. You may take electronic copy of this publication and distribute it if you don't
.. change the content. You can also print a copy to be read by yourself only.

.. We have contracts with different publishers in different countries to sell and
.. distribute paper or electronic based versions of this book (translated or not)
.. in bookstores. This helps to distribute and promote the OpenERP product. It
.. also helps us to create incentives to pay contributors and authors using author
.. rights of these sales.

.. Due to this, grants to translate, modify or sell this book are strictly
.. forbidden, unless Tiny SPRL (representing Open Object Press) gives you a
.. written authorisation for this.

.. Many of the designations used by manufacturers and suppliers to distinguish their
.. products are claimed as trademarks. Where those designations appear in this book,
.. and Open Object Press was aware of a trademark claim, the designations have been
.. printed in initial capitals.

.. While every precaution has been taken in the preparation of this book, the publisher
.. and the authors assume no responsibility for errors or omissions, or for damages
.. resulting from the use of the information contained herein.

.. Published by Open Object Press, Grand Rosière, Belgium

