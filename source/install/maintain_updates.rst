
.. _maintaining-updates:

Maintaining updates
-------------------

Upgrading between versions
++++++++++++++++++++++++++

It is strongly recommended that you **back up your data** before attempting any updates or upgrades.

Server tools
++++++++++++

The server has some tools for maintaining updates:

The server program is located at /usr/lib/tinyerp-server by default.

  * --init=all (or module for just one module) - This initialises the database
  * --update=all (or module for just one module) - This updates the database 

If you want to do an update or init on a selection of modules, you can specify
more than one module name as a parameter separated by commas, for example: ``--update=hr,mrp``

The ``--init=all`` option recreates all databases specified and ERASES ALL
CURRENT DATA previously entered for the specified module. This option should
only be used by developers.

For more information take a look at: ::

  tinyerp_server --help

Minor release updates
+++++++++++++++++++++

The ``--update=all`` updates all database descriptions of all fields and
objects, preserving your data. This option is used to automatically update the
database when you install new versions. To be more precise, ``--update`` does:

  * create new tables
  * create new fields in tables
  * change field type if needed
  * recreate all views and menus
  * recreate all new reports 

So, when you change the description of a module or if you install a new
version, run the server with ``--update=all`` and it will auto-adapt the database
to your new version. This is useful for small releases: 2.0, 2.1.0, 2.1.1, 2.2,
... all that has to be done to upgrade your new server and run it (one time)
with ``--update=all``.

This works nearly all the time, but you will have trouble in some circumstances:

  * rename of a field is not detected: the program will drop the old field and
    create the new one. It will work, but you will lose one column of all records
    in this table.
  * field name conflict: you should not have any conflict, as
    all names are normalised but never say never ... 

We try to avoid these cases in small releases. So, when you install a new minor
release, feel free to run ``--update=all`` and it will adapt the database
preserving your data.

These 2 options are very useful because you never have to create a line of SQL.
Every table, row ... are automatically created from the descriptions of
objects, reports, views ... It is very easy to maintain.

Major release upgrades
++++++++++++++++++++++

Major releases (3.x.x - 4.x.x) may have major database alterations between
them. For this purpose, scripts are provided with new major versions to manage
the database changes. These can be found in doc/migrate. It is strongly
recommended that your database is backed up prior to any attempt at running the
upgrade scripts.

   1. Stop the old version server
   2. Backup your database
   3. Run pre.py
   4. Start the new version server with --update=all
   5. Stop the new version server
   6. Run post.py
   7. Start the new version server and connect 

You may also notice pre-tiny.py and post-tiny.py. In later versions (> 4.2)
they have been moved to doc/migrate/tiny. These are examples of customised
upgrade scripts and should not be used for a standard upgrade unless this has
been advised for your particular case.

Adding new modules
++++++++++++++++++

1. IMPORT MODULES

Go to Administration - Modules management - IMPORT NEW MODULE

Import the new .zip module or copy the file to addons directory


2. UPDATE MODULE LIST

Go to Administration - Modules Management - Update Module List and check what you may want to upgrade and install.


3. APPLY UPGRADES

Go to Administration - Modules Management - Apply Upgrades


If there is a File is not a zip file error then try this:

http://www.openerp.com/forum/topic4214.html?highlight=file%20zip%20file 

