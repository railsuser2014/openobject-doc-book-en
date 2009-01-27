
Module Visible Discount Module (*product_visible_discount*)
===========================================================
:Module: product_visible_discount
:Name: Visible Discount Module
:Version: 5.0.1.0
:Directory: product_visible_discount
:Web: 

Description
-----------

::

  This module use for calculate discount amount on Sale order line and invoice line  base on partner's pricelist
      For that,On the pricelists form, new check box called "Visible Discount" is added.
      Example:
          For product PC1, listprice=450, for partner Asustek, his pricelist calculated is 225 for PC1
          If the check box is ticked, we will have on the SO line (and so also on invoice line): Unit price=450, Discount=50,00, Net price=225
          If the check box is NOT ticked, we will have on SO and Invoice lines: Unit price=225, Discount=0,00, Net price=225

Dependencies
------------

 * base - installed
 * product - installed
 * account - installed
 * sale - installed

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
