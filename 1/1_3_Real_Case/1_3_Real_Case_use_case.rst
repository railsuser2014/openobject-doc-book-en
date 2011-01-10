Business Example
================

Configure a system that enables you to:

* buy products from a supplier,

* stock the products in a warehouse,

* sell these products to a customer.

The system should support all aspects of invoicing, payments to suppliers and receipts from
customers.

Basic Settings
==============

For working out the business case you will have to model:

* the suppliers,

* the customers,

* some products,

* inventory for despatch,

* a purchase order,

* a sale order,

* invoices,

* payments.

To test the system you will need at least one supplier, one customer, one product, a warehouse, a
minimal chart of accounts and a bank account.

Get your Database Up and Running with Demo Data
===============================================

Use the technique outlined in :ref:`sect-dbcreate` to create a new database, \ ``openerp_ch03``\  . This
database will be free of data and contain the least possible amount of functionality as a starting
point. You will need to know your super administrator password for this – or you will have to find
somebody who does have it to create this seed database. You will not be able to use the \
``openerp_ch1``\   or \ ``openerp_ch2``\   databases that you might have created so far in this book
because they both contain demonstration data.

Start the database creation process from the :guilabel:`Welcome` page by clicking
:guilabel:`Databases` and then completing the following fields on the :guilabel:`Create new database` form, as shown in :ref:`fig-oech03`:

*  :guilabel:`Super admin password` : by default it's \ ``admin``\  , if you or your system
   administrator have not changed it,

*  :guilabel:`New database name` : \ ``openerp_ch03``\  ,

*  :guilabel:`Load Demonstration data` checkbox: \ ``not checked``\  (**this step is very important, but catches out many people**),

*  :guilabel:`Default Language` : \ ``English``\  ,

*  :guilabel:`Administrator password` : \ ``admin``\  (because it is easiest to remember at this stage, but obviously completely insecure),

*  :guilabel:`Confirm password` : \ ``admin``\  .

.. _fig-oech03:

.. figure::  images/openerp_ch03.png
   :scale: 50
   :align: center

   *Creating a blank database*

Then click :guilabel:`Create` to create the database and move to the setup screen :ref:`fig-oech03s1`.

.. _fig-oech03s1:

.. figure::  images/openerp_ch03_s1.png
   :scale: 50
   :align: center

   *Setting up a blank database - first screen*

After a short delay you are connected to the new \ ``openerp_ch03``\   database as user \ ``admin``\
with the password you gave it. You will have to go through the Setup wizard in steps:

When you click on the button `Skip Configuration Wizard`, you can have the following screen. Then you
can start working with this minimal database.

.. _fig-oech03st:

.. figure::  images/openerp_ch03_start.png
   :scale: 50
   :align: center

   *Starting the minimal database*

If you click on the `Start Configuration` button then OpenERP helps you to install various applications
with different functionality through the following wizard.

.. _fig-oech03cfg:

.. figure::  images/openerp_ch03_config.png
   :scale: 75
   :align: center

   *Configuring a database with other applications and functionality*



Fit your Needs
==============

All of the functional needs are provided by core modules from Open ERP:

.. index::
   single: module; product
   single: module; stock
   single: module; account
   single: module; purchase
   single: module; sale

* product management (the :mod:`product` module),

* inventory control (the :mod:`stock` module),

* accounting and finance (the :mod:`account` module),

* purchase management (the :mod:`purchase` module),

* sales management (the :mod:`sale` module).

Use the menu :menuselection:`Administration --> Modules Management --> Modules --> Uninstalled
modules` to show the list of all modules that are registered within Open ERP but as yet
uninstalled. Then:

#. Enter \ ``product``\  into the :guilabel:`Name` field and click :guilabel:`Filter` to list the
   :mod:`product` module.

#. Click the name \ ``product``\  in the list to display the product module in form view, rather
   than the list view that a search displays.

#. Click the :guilabel:`Schedule for Installation` button on the product module form.

#. Click the :guilabel:`Search` button at the top of the form to toggle back to the list view with
   search selection fields on it.

#. Search for the :mod:`sale` module then select it, too, as you did with product, to show it in form
   view.

#. Click the :guilabel:`Dependencies` tab to see that you'll automatically be loading the \
   :mod:`product`, :mod:`stock`, :mod:`mrp`, and :mod:`process` modules along with the
   :mod:`sale` module. :mod:`product` and :mod:`process` are both already marked for
   installation as a result of the first steps.

#. Return to the :guilabel:`Module` tab and then click its :guilabel:`Schedule for Installation` button.

#. Click :guilabel:`Apply Scheduled Upgrades` in the :guilabel:`Action` toolbar to the right.

#. When the :guilabel:`System Upgrade` form appears, review the list of Modules to update – it
   may be longer than you had expected, and now includes all the modules you need, because the
   dependencies themselves had their own dependencies.

#. Click :guilabel:`Start Upgrade`, wait for :guilabel:`System upgrade done` to be displayed, then
   click :guilabel:`Start Configuration` on that form.

Configuration is required for both the accounts setup and the sales defaults.

#. Accept the defaults for the :guilabel:`Fiscal Year` and choose the
   :guilabel:`Charts of Account` to be :guilabel:`None` then click
   :guilabel:`Continue`.

#. The sales defaults are shown in the screenshot :ref:`fig-oech03cfss`. The selections you make
   determine how Open ERP's processes work by setting its default behaviour
   (although you can override any of them for any sales order,
   so you are not strictly bound by these defaults).
   Accept the initial set by clicking :guilabel:`Set default behaviour`.

#. You've reached the end of this configuration stage so click :guilabel:`Continue` to continue using the
   system as the Administrator. You first reach a new tab :guilabel:`Features` that lists the new menus
   and views as shown in the figure :ref:`fig-oech03cf`. Each of the modules that were installed
   has its own new tab - it's not only the one you see displayed in front of you. Click :guilabel:`Next`
   and :guilabel:`Previous` to move between them.

#. The main menu now displays all of the menu items that were loaded by the modules you installed.
   Click :guilabel:`MAIN MENU` to see this, shown in the screenshot :ref:`fig-oech03mm`.

.. _fig-oech03cfss:

.. figure:: images/openerp_ch03_setsales.png
   :scale: 75
   :align: center

   *The module form once a module is installed*

.. _fig-oech03cf:

.. figure:: images/openerp_feature.png
   :scale: 65
   :align: center

   *The Features tab once a module is installed*

.. _fig-oech03mm:

.. figure:: images/openerp_ch03_main.png
   :scale: 75
   :align: center

   *Continuing with the database after installing new modules*

.. Copyright © Open Object Press. All rights reserved.

.. You may take electronic copy of this publication and distribute it if you don't
.. change the content. You can also print a copy to be read by yourself only.

.. We have contracts with different publishers in different countries to sell and
.. distribute paper or electronic based versions of this book (translated or not)
.. in bookstores. This helps to distribute and promote the Open ERP product. It
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

