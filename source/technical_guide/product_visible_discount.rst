
.. module:: product_visible_discount
    :synopsis: Visible Discount Module 
    :noindex:
.. 

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

Visible Discount Module (*product_visible_discount*)
====================================================
:Module: product_visible_discount
:Name: Visible Discount Module
:Version: 5.0.1.0
:Author: Tiny
:Directory: product_visible_discount
:Web: 
:Official module: no
:Quality certified: no

Description
-----------

::

  This module use for calculate discount amount on Sale order line and invoice line  base on partner's 
  pricelist
      For that,On the pricelists form, new check box called "Visible Discount" is added.
      Example:
          For product PC1, listprice=450, for partner Asustek, his pricelist calculated is 225 for PC1
          If the check box is ticked, we will have on the SO line (and so also on invoice line): 
          Unit price=450, Discount=50,00, Net price=225
          If the check box is NOT ticked, we will have on SO and Invoice lines: Unit price=225, 
          Discount=0,00, Net price=225

Dependencies
------------

 * :mod:`base`
 * :mod:`product`
 * :mod:`account`
 * :mod:`sale`

Reports
-------

None


Menus
-------


None


Views
-----

 * \* INHERIT product.pricelist.tree (form)
 * \* INHERIT product.pricelist.form (form)


Objects
-------

None
