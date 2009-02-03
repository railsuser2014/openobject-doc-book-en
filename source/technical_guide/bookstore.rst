
.. module:: bookstore
    :synopsis: Bookstore Verticalisation 
    :noindex:
.. 

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

    <style>
      div.body p#module-bookstore {
        display: none;
      }
    </style>

Bookstore Verticalisation (*bookstore*)
=======================================
:Module: bookstore
:Name: Bookstore Verticalisation
:Version: 5.0.1.0
:Author: Tiny
:Directory: bookstore
:Web: 
:Is certified: no

Description
-----------

::

  Module to manage book store.
      Add book Information, 
      Author Information, 
      Books Category,
      Related books,
      Available Languages,

Dependencies
------------

 * :mod:`library`
 * :mod:`delivery`
 * :mod:`sale`

Reports
-------

None


Menus
-------


None


Views
-----

 * \* INHERIT Company (form)
 * \* INHERIT Partner (form)
 * \* INHERIT Partner (form)
 * \* INHERIT Partner Address (form)
 * Partners (tree)
 * \* INHERIT Sale lines replace uom by mode (form)
 * \* INHERIT  (form)


Objects
-------

None
