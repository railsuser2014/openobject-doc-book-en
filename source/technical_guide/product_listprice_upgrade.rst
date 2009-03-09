
.. module:: product_listprice_upgrade
    :synopsis: Product listprice upgrade 
    :noindex:
.. 

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

Product listprice upgrade (*product_listprice_upgrade*)
=======================================================
:Module: product_listprice_upgrade
:Name: Product listprice upgrade
:Version: 5.0.1.0
:Author: Tiny
:Directory: product_listprice_upgrade
:Web: 
:Official module: no
:Quality certified: no

Description
-----------

::

  The aim of this module is to allow the automatic upgrade of the field 'List Price' on each product.
      * added a new price type called 'Internal Pricelist' (currently, we have only 2 price types: 
        Sale and Purchase Pricelist)
      * Created a wizard button in the menu Products>Pricelist called 'Upgrade Product List Price'
      * When we have completed the wizard and click on 'Upgrade', it will change the field 
  'List Price' for all products contained in the categories that we have selected in the wizard

Dependencies
------------

 * :mod:`base`
 * :mod:`product`

Reports
-------

None


Menus
-------

 * Books/Pricelists
 * Books/Pricelists/Upgrade Product List price

Views
-----


None



Objects
-------

None
