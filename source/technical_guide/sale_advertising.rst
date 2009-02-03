
.. module:: sale_advertising
    :synopsis: Sales: Avertising Sales 
    :noindex:
.. 

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

    <style>
      div.body p#module-sale_advertising {
        display: none;
      }
    </style>

Sales: Avertising Sales (*sale_advertising*)
============================================
:Module: sale_advertising
:Name: Sales: Avertising Sales
:Version: 5.0.0.1
:Author: Tiny
:Directory: sale_advertising
:Web: http://tinyerp.com/
:Is certified: no

Description
-----------

::

  This module allow you to use the Sale Management to encode your advertising sales ... TODO

Dependencies
------------

 * :mod:`sale`

Reports
-------

None


Menus
-------

 * Sales Management/Advertising
 * Sales Management/Advertising/Advertising Issue
 * Sales Management/Advertising/Advertising Proof
 * Sales Management/Advertising/All Advertising Sale Orders

Views
-----

 * \* INHERIT sale.order.form.inherit (form)
 * \* INHERIT sale.order.form.inherit.line (form)
 * \* INHERIT sale.order.line.form.inherit.line2 (form)
 * sale.advertising.issue.form (form)
 * sale.advertising.issue.tree (tree)
 * sale.advertising.proof.form (form)
 * sale.advertising.proof.tree (tree)
 * \* INHERIT product.product.form.inherit (form)


Objects
-------

Object: Sale Advertising Issue (sale.advertising.issue)
#######################################################



:issue_date: Issue Date, date, required





:medium: Medium, many2one, required





:name: Name, char, required





:default_note: Default Note, text





:state: State, selection




Object: Sale Advertising Proof (sale.advertising.proof)
#######################################################



:address_id: Delivery Address, many2one, required





:target_id: Target, many2one, required





:name: Name, char, required





:number: Number of Copies, integer, required


