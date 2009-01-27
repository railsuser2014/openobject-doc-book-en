
Module Lunch Module (*lunch*)
=============================
:Module: lunch
:Name: Lunch Module
:Version: 5.0.0.1
:Directory: lunch
:Web: 

Description
-----------

::

  None

Dependencies
------------

 * base - installed

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

Object: Category
################

.. index::
  single: Category object
.. 


:name: Name, char, required



.. index::
  single: name field
.. 



Object: lunch.product
#####################

.. index::
  single: lunch.product object
.. 


:active: Active, boolean



.. index::
  single: active field
.. 




:price: Price, float



.. index::
  single: price field
.. 




:category_id: Category, selection



.. index::
  single: category_id field
.. 




:name: Name, char, required



.. index::
  single: name field
.. 




:description: Description, char



.. index::
  single: description field
.. 



Object: lunch.cashbox
#####################

.. index::
  single: lunch.cashbox object
.. 


:manager: Manager, many2one



.. index::
  single: manager field
.. 




:name: Name, char, required



.. index::
  single: name field
.. 




:sum_remain: Remained Total, float, readonly



.. index::
  single: sum_remain field
.. 



Object: lunch.cashmove
######################

.. index::
  single: lunch.cashmove object
.. 


:box: Box Name, many2one, required



.. index::
  single: box field
.. 




:create_date: Created date, datetime, readonly



.. index::
  single: create_date field
.. 




:name: Name, char



.. index::
  single: name field
.. 




:user_cashmove: User Name, many2one, required



.. index::
  single: user_cashmove field
.. 




:amount: Amount, float



.. index::
  single: amount field
.. 




:active: Active, boolean



.. index::
  single: active field
.. 



Object: lunch.order
###################

.. index::
  single: lunch.order object
.. 


:product: Product, many2one, required, readonly



.. index::
  single: product field
.. 




:user_id: User Name, many2one, required, readonly



.. index::
  single: user_id field
.. 




:price: Price, float, readonly



.. index::
  single: price field
.. 




:descript: Description Order, char, readonly



.. index::
  single: descript field
.. 




:state: State, selection, readonly



.. index::
  single: state field
.. 




:date: Date, date, readonly



.. index::
  single: date field
.. 




:cashmove: CashMove, many2one, readonly



.. index::
  single: cashmove field
.. 



Object: Amount available by user and box
########################################

.. index::
  single: Amount available by user and box object
.. 


:box: Box Name, many2one, readonly



.. index::
  single: box field
.. 




:amount: Amount, float, readonly



.. index::
  single: amount field
.. 




:user_id: User Name, many2one, readonly



.. index::
  single: user_id field
.. 

