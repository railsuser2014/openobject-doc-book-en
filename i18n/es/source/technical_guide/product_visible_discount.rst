
.. i18n: .. module:: product_visible_discount
.. i18n:     :synopsis: Visible Discount Module 
.. i18n:     :noindex:
.. i18n: .. 

.. module:: product_visible_discount
    :synopsis: Visible Discount Module 
    :noindex:
.. 

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. i18n: Visible Discount Module (*product_visible_discount*)
.. i18n: ====================================================
.. i18n: :Module: product_visible_discount
.. i18n: :Name: Visible Discount Module
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: product_visible_discount
.. i18n: :Web: 
.. i18n: :Official module: no
.. i18n: :Quality certified: no

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

.. i18n: Description
.. i18n: -----------

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   This module use for calculate discount amount on Sale order line and invoice line  base on partner's 
.. i18n:   pricelist
.. i18n:       For that,On the pricelists form, new check box called "Visible Discount" is added.
.. i18n:       Example:
.. i18n:           For product PC1, listprice=450, for partner Asustek, his pricelist calculated is 225 for PC1
.. i18n:           If the check box is ticked, we will have on the SO line (and so also on invoice line): 
.. i18n:           Unit price=450, Discount=50,00, Net price=225
.. i18n:           If the check box is NOT ticked, we will have on SO and Invoice lines: Unit price=225, 
.. i18n:           Discount=0,00, Net price=225

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

.. i18n: Dependencies
.. i18n: ------------

Dependencies
------------

.. i18n:  * :mod:`base`
.. i18n:  * :mod:`product`
.. i18n:  * :mod:`account`
.. i18n:  * :mod:`sale`

 * :mod:`base`
 * :mod:`product`
 * :mod:`account`
 * :mod:`sale`

.. i18n: Reports
.. i18n: -------

Reports
-------

.. i18n: None

None

.. i18n: Menus
.. i18n: -------

Menus
-------

.. i18n: None

None

.. i18n: Views
.. i18n: -----

Views
-----

.. i18n:  * \* INHERIT product.pricelist.tree (form)
.. i18n:  * \* INHERIT product.pricelist.form (form)

 * \* INHERIT product.pricelist.tree (form)
 * \* INHERIT product.pricelist.form (form)

.. i18n: Objects
.. i18n: -------

Objects
-------

.. i18n: None

None
