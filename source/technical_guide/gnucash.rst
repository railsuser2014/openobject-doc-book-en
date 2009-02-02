
.. module:: gnucash
    :synopsis: gnucash
    :noindex:
.. 

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

gnucash (*gnucash*)
===================
:Module: gnucash
:Name: gnucash
:Version: 5.0.0.1
:Directory: gnucash
:Web: 
:Is certified: no

Description
-----------

::

  Gnucash Import from file

Dependencies
------------

 * :mod:`base`
 * :mod:`account`
 * :mod:`product`

Reports
-------

None


Menus
-------

 * Administration/GnuCash
 * Administration/GnuCash/Gnucash Mappings
 * Administration/GnuCash/Import GnuCash File

Views
-----

 * gnucash.index.form (form)
 * gnucash.index.tree (tree)


Objects
-------

Object: gnucash.index (gnucash.index)
#####################################



:noupdate: Non Updatable, boolean





:parent_book: Parent book, many2one





:date_init: Init Date, datetime





:date_update: Update Date, datetime





:module: Module, char, required





:to_delete: Should be deleted, boolean, required





:model: Object, char, required





:guid: Gnucash UID, char, required





:res_id: Resource ID, integer


