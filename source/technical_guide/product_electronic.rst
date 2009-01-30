
.. module:: product_electronic
    :synopsis: Products Attributes & Manufacturers
    :noindex:
.. 

Products Attributes & Manufacturers (*product_electronic*)
==========================================================
:Module: product_electronic
:Name: Products Attributes & Manufacturers
:Version: 5.0.1.0
:Directory: product_electronic
:Web: 

Description
-----------

::

  A module that add manufacturers and attributes on the product form

Dependencies
------------

 * base - installed
 * account - installed
 * product - installed
 * stock - installed

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


