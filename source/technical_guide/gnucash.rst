
Module gnucash (*gnucash*)
==========================
:Module: gnucash
:Name: gnucash
:Version: 5.0.0.1
:Directory: gnucash
:Web: 

Description
-----------

::

  Gnucash Import from file

Dependencies
------------

 * base - installed
 * account - installed
 * product - installed

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

Object: gnucash.index
#####################

.. index::
  single: gnucash.index object
.. 


:noupdate: Non Updatable, boolean



.. index::
  single: noupdate field
.. 




:parent_book: Parent book, many2one



.. index::
  single: parent_book field
.. 




:date_init: Init Date, datetime



.. index::
  single: date_init field
.. 




:date_update: Update Date, datetime



.. index::
  single: date_update field
.. 




:module: Module, char, required



.. index::
  single: module field
.. 




:to_delete: Should be deleted, boolean, required



.. index::
  single: to_delete field
.. 




:model: Object, char, required



.. index::
  single: model field
.. 




:guid: Gnucash UID, char, required



.. index::
  single: guid field
.. 




:res_id: Resource ID, integer



.. index::
  single: res_id field
.. 

