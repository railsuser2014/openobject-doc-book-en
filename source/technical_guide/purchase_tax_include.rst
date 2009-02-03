
.. module:: purchase_tax_include
    :synopsis: Purchases with taxes included 
    :noindex:
.. 

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

    <style>
      div.body p#module-purchase_tax_include {
        display: none;
      }
    </style>

Purchases with taxes included (*purchase_tax_include*)
======================================================
:Module: purchase_tax_include
:Name: Purchases with taxes included
:Version: 5.0.1.0
:Author: Tiny
:Directory: purchase_tax_include
:Web: http://tinyerp.com/module_account.html
:Is certified: no

Description
-----------

::

  This module allows you to use purchase order with prices including or excluding taxes.

Dependencies
------------

 * :mod:`purchase`
 * :mod:`account_tax_include`

Reports
-------

None


Menus
-------


None


Views
-----

 * \* INHERIT purchase.order.exlcuded.view.form (form)
 * \* INHERIT purchase.order.line.tree (tree)


Objects
-------

None
