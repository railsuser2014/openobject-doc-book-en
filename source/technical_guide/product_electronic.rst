
.. module:: product_electronic
    :synopsis: Products Attributes & Manufacturers 
    :noindex:
.. 

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

    <style>
      div.body p#module-product_electronic {
        display: none;
      }
    </style>

Products Attributes & Manufacturers (*product_electronic*)
==========================================================
:Module: product_electronic
:Name: Products Attributes & Manufacturers
:Version: 5.0.1.0
:Author: Tiny
:Directory: product_electronic
:Web: 
:Is certified: no

Description
-----------

::

  A module that add manufacturers and attributes on the product form

Dependencies
------------

 * :mod:`base`
 * :mod:`account`
 * :mod:`product`
 * :mod:`stock`

Reports
-------

None


Menus
-------


None


Views
-----

 * \* INHERIT product.normal.form (form)
 * product.electronic.attribute.tree (tree)
 * product.electronic.attribute.form (form)


Objects
-------

Object: Product attributes (product.electronic.attribute)
#########################################################



:name: Attribute, char, required





:value: Value, char





:product_id: Product, many2one


