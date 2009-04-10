
.. i18n: .. module:: tiny_purchase
.. i18n:     :synopsis: Tiny purchase 
.. i18n:     :noindex:
.. i18n: .. 

.. module:: tiny_purchase
    :synopsis: Tiny purchase 
    :noindex:
.. 

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. i18n: Tiny purchase (*tiny_purchase*)
.. i18n: ===============================
.. i18n: :Module: tiny_purchase
.. i18n: :Name: Tiny purchase
.. i18n: :Version: 5.0.0.1
.. i18n: :Author: Tiny
.. i18n: :Directory: tiny_purchase
.. i18n: :Web: 
.. i18n: :Official module: no
.. i18n: :Quality certified: no

Tiny purchase (*tiny_purchase*)
===============================
:Module: tiny_purchase
:Name: Tiny purchase
:Version: 5.0.0.1
:Author: Tiny
:Directory: tiny_purchase
:Web: 
:Official module: no
:Quality certified: no

.. i18n: Description
.. i18n: -----------

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   Very simple purchase module.

::

  Very simple purchase module.

.. i18n: Dependencies
.. i18n: ------------

Dependencies
------------

.. i18n:  * :mod:`base`

 * :mod:`base`

.. i18n: Reports
.. i18n: -------

Reports
-------

.. i18n:  * Print Order

 * Print Order

.. i18n: Menus
.. i18n: -------

Menus
-------

.. i18n:  * Tools
.. i18n:  * Tools/Tiny Purchase
.. i18n:  * Tools/Tiny Purchase/Purchase line
.. i18n:  * Tools/Tiny Purchase/Configuration
.. i18n:  * Tools/Tiny Purchase/Configuration/Purchase product
.. i18n:  * Tools/Tiny Purchase/Purchase Order

 * Tools
 * Tools/Tiny Purchase
 * Tools/Tiny Purchase/Purchase line
 * Tools/Tiny Purchase/Configuration
 * Tools/Tiny Purchase/Configuration/Purchase product
 * Tools/Tiny Purchase/Purchase Order

.. i18n: Views
.. i18n: -----

Views
-----

.. i18n:  * tiny_purchase.line.form (form)
.. i18n:  * tiny_purchase.product.form (form)
.. i18n:  * tiny_purchase.order.form (form)

 * tiny_purchase.line.form (form)
 * tiny_purchase.product.form (form)
 * tiny_purchase.order.form (form)

.. i18n: Objects
.. i18n: -------

Objects
-------

.. i18n: Object: tiny_purchase.product (tiny_purchase.product)
.. i18n: #####################################################

Object: tiny_purchase.product (tiny_purchase.product)
#####################################################

.. i18n: :price: Price, float

:price: Price, float

.. i18n: :name: Name, char

:name: Name, char

.. i18n: Object: tiny_purchase.order (tiny_purchase.order)
.. i18n: #################################################

Object: tiny_purchase.order (tiny_purchase.order)
#################################################

.. i18n: :line_ids: Lines, one2many

:line_ids: Lines, one2many

.. i18n: :state: State, selection

:state: State, selection

.. i18n: :user_id: User, many2one, required

:user_id: User, many2one, required

.. i18n: :name: Date, date

:name: Date, date

.. i18n: Object: tiny_purchase.line (tiny_purchase.line)
.. i18n: ###############################################

Object: tiny_purchase.line (tiny_purchase.line)
###############################################

.. i18n: :order_id: Order, many2one, required

:order_id: Order, many2one, required

.. i18n: :price: Price, float, readonly

:price: Price, float, readonly

.. i18n: :product_id: Product, many2one, required

:product_id: Product, many2one, required

.. i18n: :comments: Comments, text

:comments: Comments, text

.. i18n: :quantity: Quantity, integer

:quantity: Quantity, integer
