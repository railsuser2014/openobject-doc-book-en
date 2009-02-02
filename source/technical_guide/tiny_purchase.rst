
.. module:: tiny_purchase
    :synopsis: Tiny purchase
    :noindex:
.. 

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

Tiny purchase (*tiny_purchase*)
===============================
:Module: tiny_purchase
:Name: Tiny purchase
:Version: 5.0.0.1
:Directory: tiny_purchase
:Web: 
:Is certified: no

Description
-----------

::

  Very simple purchase module.

Dependencies
------------

 * :mod:`base`

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

Object: tiny_purchase.product (tiny_purchase.product)
#####################################################



:price: Price, float





:name: Name, char




Object: tiny_purchase.order (tiny_purchase.order)
#################################################



:line_ids: Lines, one2many





:state: State, selection





:user_id: User, many2one, required





:name: Date, date




Object: tiny_purchase.line (tiny_purchase.line)
###############################################



:order_id: Order, many2one, required





:price: Price, float, readonly





:product_id: Product, many2one, required





:comments: Comments, text





:quantity: Quantity, integer


