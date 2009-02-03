
.. module:: product_size
    :synopsis: Sizes of lots (width, length, thickness) 
    :noindex:
.. 

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

    <style>
      div.body p#module-product_size {
        display: none;
      }
    </style>

Sizes of lots (width, length, thickness) (*product_size*)
=========================================================
:Module: product_size
:Name: Sizes of lots (width, length, thickness)
:Version: 5.0.1.0
:Author: Tiny
:Directory: product_size
:Web: 
:Is certified: no

Description
-----------

::

  Manage 3 dimensions size on lots.
  Implements demo data for a complex workflow on steel.

Dependencies
------------

 * :mod:`base`
 * :mod:`account`
 * :mod:`product`
 * :mod:`stock`
 * :mod:`mrp`
 * :mod:`sale`

Reports
-------

None


Menus
-------


None


Views
-----

 * \* INHERIT stock.production.lot.form (form)
 * \* INHERIT stock.production.lot.tree (tree)
 * \* INHERIT product.normal.form (form)


Objects
-------

None
