
Module Sandwich Module (*sandwich*)
===================================
:Module: sandwich
:Name: Sandwich Module
:Version: 5.0.1.0
:Directory: sandwich
:Web: 

Description
-----------

::

  None

Dependencies
------------

 * base - installed
 * product - installed

Reports
-------

 * Sandwichs order

Menus
-------

 * Tools
 * Tools/Sandwich
 * Tools/Sandwich/Configuration
 * Tools/Sandwich/Configuration/Type of Product
 * Tools/Sandwich/Configuration/Product
 * Tools/Sandwich/Order Lines
 * Tools/Sandwich/Order Lines/My Order Lines
 * Tools/Sandwich/Order Lines/My Order Lines/My Order Lines of the Day
 * Tools/Sandwich/Order Lines/Order Lines of the Day
 * Tools/Sandwich/Today's Orders
 * Tools/Sandwich/Create Order

Views
-----

 * sandwich.product.type (form)
 * sandwich.product.type (tree)
 * sandwich.product (tree)
 * sandwich.product (form)
 * sandwich.order.line.tree (tree)
 * sandwich.order.line.form (form)
 * sandwich.order.tree (tree)
 * sandwich.order.form (form)


Objects
-------

Object: sandwich.product.type
#############################

.. index::
  single: sandwich.product.type object
.. 


:name: Name of the type, char, required



.. index::
  single: name field
.. 




:description: Type's description, char



.. index::
  single: description field
.. 



Object: sandwich.product
########################

.. index::
  single: sandwich.product object
.. 


:price: Product price, float



.. index::
  single: price field
.. 




:name: Product name, char, required



.. index::
  single: name field
.. 




:product_type_id: Type of product, many2one



.. index::
  single: product_type_id field
.. 



Object: sandwich.order
######################

.. index::
  single: sandwich.order object
.. 


:date: Order date, date



.. index::
  single: date field
.. 




:note: Notes, text



.. index::
  single: note field
.. 




:partner: Partner, many2one, required



.. index::
  single: partner field
.. 




:name: Name, char, required



.. index::
  single: name field
.. 




:order_lines: Order lines, one2many



.. index::
  single: order_lines field
.. 



Object: sandwich.order.line
###########################

.. index::
  single: sandwich.order.line object
.. 


:user_id: User id, many2one, required



.. index::
  single: user_id field
.. 




:name: Description, char, required



.. index::
  single: name field
.. 




:order_id: Order, many2one



.. index::
  single: order_id field
.. 




:product_id: Product, many2one



.. index::
  single: product_id field
.. 




:date: Date, date



.. index::
  single: date field
.. 




:quantity: Quantity, integer, required



.. index::
  single: quantity field
.. 




:product_type_id: Product type, many2one



.. index::
  single: product_type_id field
.. 

