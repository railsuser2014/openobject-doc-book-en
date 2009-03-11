
.. index::
   single: database; create
   single: database

.. _sect-dbcreate:

Database creation
=================

Use the technique outlined in this section to create a new database, \ ``openerp_ch01``\  . This
database will contain the demonstration data provided with Open ERP and a large proportion of the
core Open ERP functionality. You'll need to know your super administrator password for this – or
you'll have to find somebody who does have it to create this seed database.

.. index::
   single: password; super-administrator
   single: password; superadmin

.. note :: The super-administrator password

   Anyone who knows the super-administrator password has complete access to the data on the server
   – able to read, change and delete any of the data in any of the databases there.

   After first installation, the password is ``admin``. You can change it through the GTK client
   from the menu :menuselection:`File --> Databases --> Administrator Password`, or through the
   web client by logging out (click the :guilabel:`Logout` link), clicking :guilabel:`Databases` on the
   login screen, and then clicking the :guilabel:`Password` button on the Management screen. This
   password is stored in a configuration file outside the database, so a server systems
   administrator can change it if you forget it.

.. figure:: images/change_superadmin_pwd.png
   :scale: 75
   :align: center

   *Changing the super-administrator password through the web client*

.. _sect-creatingdb:

Creating the database
---------------------

If you're using the GTK client, choose :menuselection:`Files --> Databases --> New database`  in
the menu at the top left. Enter the super-administrator password, then the name of the new database
you're creating.

.. figure:: images/create_new_db_GTK.png
   :scale: 75
   :align: center

   *Creating a new database through the GTK client*  

If you're using the web client, click :guilabel:`Databases` on the login screen, then
:guilabel:`Create` on the database management page. Enter the super-administrator password, and the
name of the new database you're creating.
  
In both cases you'll see a checkbox that determines whether you load demonstration data or not.
The consequences of checking this box or not affect the **whole use** of this database.

In both cases you'll also see that you can choose the Administrator password. This makes your 
database quite secure because you can ensure that it is unique from the outset.
(In fact many people find it hard to resist ``admin`` as their password!)

Database openerp_ch01
---------------------

.. index::
   pair: account; user

Wait for the message showing that the database has been successfully created, along with the user
accounts and passwords (\ ``admin/XXXX``\   and \ ``demo/demo``\  ). Now you've created this seed
database you can extend it without having to know the super-administrator password.

.. index::
   single: access; LDAP
   single: LDAP
   pair: password; username
   single: access; user

.. tip::   User Access

	The combination of username/password is specific to a single database. If you have administrative
	rights to a database you can modify all users.

 	.. index::
	   single: module; users_ldap

	Alternatively you can install the :mod:`users_ldap` module, which manages the authentication of users
	in LDAP (the Lightweight Directory Access Protocol, a standard system), and connect it to several
	Open ERP databases. Using this, many databases can share the same user account details.

.. note::  Failure to create a database

	How do you know if you've successfully created your new database?
	You're told if the database creation has been unsuccessful.
	If you have entered a database name using prohibited characters (or no name, or too short a name)
	you will be alerted by the dialog box :guilabel:`Bad database name!` explaining how to correct the error.
	If you've entered the wrong super-administrator password or a name already in use
	(some names can be reserved without your knowledge), you'll be alerted by the dialog box
	:guilabel:`Error during database creation!`.

Connect to the database \ ``openerp_ch01``\   that you just created, using the default administrator
account.

If this is the first time you've connected to this database you'll be asked a series of questions to
define the database parameters:

	#.  :guilabel:`Select a profile` : select \ ``Minimal Profile``\  and click :guilabel:`Next`.

	#.  :guilabel:`Company Details` : replace the proposed default of \ ``Tiny sprl``\  by your own
	    company name, complete as much of your address as you like, and add some lines about your company,
	    such as a slogan and any statutory requirements, to the header and footer fields. Click
	    :guilabel:`Next`.

	#.  :guilabel:`Summary` : check the information and go back to make any modifications you need
	    before installation. Then click :guilabel:`Install`.

	#.  :guilabel:`Installation Completed` : click :guilabel:`Ok`.

Once configuration is complete you're connected to your Open ERP system. Its functionality is very
limited because you've selected a minimal installation, but this is sufficient to demonstrate that
your installation is working.

.. figure:: images/define_main_co_dlg.png
   :align: center
   :scale: 80

   *Defining your company during initial database configuration*

.. index::
   single: database; manage

Managing databases
------------------

As a super-administrator you've not only got rights to create new databases, but also to:

* delete databases,

* backup databases,

* restore databases.

All of these operations can be carried out from the menu :menuselection:`File --> Databases... -->
Backup databases` in the GTK client, or from the :guilabel:`Database` button in the web client's 
:guilabel:`Login` screen.

.. index::
   single: database; duplicate

.. tip::   Duplicating a database

	To duplicate a database you can:

        #. make a backup file on your PC from this database.

        #. restore this database from the backup file on your PC, giving it a new name as you do so.

	This can be a useful way of making a test database from a production database. You can try out the
	operation of a new configuration, new modules, or just the import of new data.

.. index::
   single: access

A system administrator can configure Open ERP to restrict access to some of these database functions
so that your security is enhanced in normal production use.

You are now ready to use databases from your installation to familiarize yourself with the
administration and use of Open ERP.

New Open ERP functionality
==========================

The database you've created and managed so far is based on the core Open ERP functionality that you
installed. The core system is installed in the file system of your Open ERP application server, but
only installed into an Open ERP database as you require it, as is described in the next chapter, :ref:`ch-guided`.

What if want to update what's there, or extend what's there with additional modules?

* To update what you have, you'd install a new instance of Open ERP using the same techniques as
  described earlier in this section, :ref:`sect-dbcreate`.

* To extend what you have, you'd install new modules in the ``addons`` directory of your current
  Open ERP installation. There are several ways of doing that.

.. index::
   pair:  system; administrator

In both cases you'll need briefly to be a \ ``root``\   user or \ ``Administrator``\   of your
Open ERP application server.

Extending Open ERP
------------------

To extend Open ERP you'll need to copy modules into the \ ``addons``\   directory. That's in
your server's \ ``openerp-server``\   directory (which differs between Windows, Mac and some of the
various Linux distributions and not available at all in the Windows all-in-one installer).

.. index::
   single: module; product
   single: module; purchase

If you look there you'll see existing modules such as :mod:`product` and :mod:`purchase`. A
module can be provided in the form of files within a directory or a a zip-format file containing
that same directory structure.

You can add modules in two main ways – through the server, or through the client.

.. index::
   pair:  system; administration

To add new modules through the server is a conventional systems administration task. As \ ``root``\
user or other suitable user, you'd put the module in the \ ``addons``\   directory and change its
permissions to match those of the other modules.

To add new modules through the client you must first change the permissions of the \ ``addons``\
directory of the server, so that it is writable by the server. That will enable you to install
Open ERP modules using the Open ERP client (a task ultimately carried out on the application
server by the server software).

.. index::
   pair:  filesystem; permissions

.. tip:: Changing permissions

	A very simple way of changing permissions on the Linux system you're using to develop an Open ERP
	application is to execute the command sudo chmod 777 <path_to_addons> (where <path_to_addons> is
	the full path to the addons directory, a location like /usr/lib/python2.5/site-packages/openerp-
	server/addons).

Any user of Open ERP who has access to the relevant administration menus can then upload any new
functionality, so you'd certainly disable this capability for production use. You'll see examples of
this uploading as you make your way through this book.


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

