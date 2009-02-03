
.. module:: sale_tax_include
    :synopsis: Invoices and prices with taxes included 
    :noindex:
.. 

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

    <style>
      div.body p#module-sale_tax_include {
        display: none;
      }
    </style>

Invoices and prices with taxes included (*sale_tax_include*)
============================================================
:Module: sale_tax_include
:Name: Invoices and prices with taxes included
:Version: 5.0.1.0
:Author: Tiny
:Directory: sale_tax_include
:Web: http://tinyerp.com/module_account.html
:Is certified: no

Description
-----------

::

  Allow the user to work tax included prices.
  Especially useful for b2c businesses.
      
  This module implement the modification on the sale order form.

Dependencies
------------

 * :mod:`sale`
 * :mod:`account_tax_include`

Reports
-------

None


Menus
-------


None


Views
-----

 * \* INHERIT sale.order.exlcuded.view.form (form)
 * \* INHERIT sale.order.exlcuded.view.form (form)


Objects
-------

None
