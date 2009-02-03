
.. module:: lunch
    :synopsis: Lunch Module 
    :noindex:
.. 

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

    <style>
      div.body p#module-lunch {
        display: none;
      }
    </style>

Lunch Module (*lunch*)
======================
:Module: lunch
:Name: Lunch Module
:Version: 5.0.0.1
:Author: Tiny
:Directory: lunch
:Web: 
:Is certified: no

Description
-----------

::

  None

Dependencies
------------

 * :mod:`base`

Reports
-------

 * Print Order

Menus
-------

 * Tools
 * Tools/Lunch
 * Tools/Lunch/Configuration
 * Tools/Lunch/Make order
 * Tools/Lunch/Make order/Order of the day
 * Tools/Lunch/Configuration/CashBox
 * Tools/Lunch/Cash Moves
 * Tools/Lunch/Configuration/Products
 * Tools/Lunch/Configuration/Products/Category of product
 * Tools/Lunch/Box Amount by User

Views
-----

 * Order (form)
 * Order (tree)
 * CashBox (form)
 * CashBox (tree)
 * CashMove (form)
 * CashMove (tree)
 *  Category of product  (form)
 * Category (tree)
 * Products (form)
 * Products (tree)
 * Lunch amount (tree)
 * Lunch amount (form)


Objects
-------

Object: Category (lunch.category)
#################################



:name: Name, char, required




Object: lunch.product (lunch.product)
#####################################



:active: Active, boolean





:price: Price, float





:category_id: Category, selection





:name: Name, char, required





:description: Description, char




Object: lunch.cashbox (lunch.cashbox)
#####################################



:manager: Manager, many2one





:name: Name, char, required





:sum_remain: Remained Total, float, readonly




Object: lunch.cashmove (lunch.cashmove)
#######################################



:box: Box Name, many2one, required





:create_date: Created date, datetime, readonly





:name: Name, char





:user_cashmove: User Name, many2one, required





:amount: Amount, float





:active: Active, boolean




Object: lunch.order (lunch.order)
#################################



:product: Product, many2one, required, readonly





:user_id: User Name, many2one, required, readonly





:price: Price, float, readonly





:descript: Description Order, char, readonly





:state: State, selection, readonly





:date: Date, date, readonly





:cashmove: CashMove, many2one, readonly




Object: Amount available by user and box (report.lunch.amount)
##############################################################



:box: Box Name, many2one, readonly





:amount: Amount, float, readonly





:user_id: User Name, many2one, readonly


