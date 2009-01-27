
Module Tiny purchase (*tiny_purchase*)
======================================
:Module: tiny_purchase
:Name: Tiny purchase
:Version: 5.0.0.1
:Directory: tiny_purchase
:Web: 

Description
-----------

::

  Very simple purchase module.

Dependencies
------------

 * base - installed

Reports
-------

 * Print Order

Menus
-------

 * Tools
 * Tools/Tiny Purchase
 * Tools/Tiny Purchase/Purchase line
 * Tools/Tiny Purchase/Configuration
 * Tools/Tiny Purchase/Configuration/Purchase product
 * Tools/Tiny Purchase/Purchase Order

Views
-----

 * tiny_purchase.line.form (form)
 * tiny_purchase.product.form (form)
 * tiny_purchase.order.form (form)


Objects
-------

Object: tiny_purchase.product
#############################

.. index::
  single: tiny_purchase.product object
.. 


:price: Price, float



.. index::
  single: price field
.. 




:name: Name, char



.. index::
  single: name field
.. 



Object: tiny_purchase.order
###########################

.. index::
  single: tiny_purchase.order object
.. 


:line_ids: Lines, one2many



.. index::
  single: line_ids field
.. 




:state: State, selection



.. index::
  single: state field
.. 




:user_id: User, many2one, required



.. index::
  single: user_id field
.. 




:name: Date, date



.. index::
  single: name field
.. 



Object: tiny_purchase.line
##########################

.. index::
  single: tiny_purchase.line object
.. 


:order_id: Order, many2one, required



.. index::
  single: order_id field
.. 




:price: Price, float, readonly



.. index::
  single: price field
.. 




:product_id: Product, many2one, required



.. index::
  single: product_id field
.. 




:comments: Comments, text



.. index::
  single: comments field
.. 




:quantity: Quantity, integer



.. index::
  single: quantity field
.. 

