
.. module:: Ampco
    :synopsis: Ampco 
    :noindex:
.. 

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

    <style>
      div.body p#module-Ampco {
        display: none;
      }
    </style>

Ampco (*Ampco*)
===============
:Module: Ampco
:Name: Ampco
:Version: 5.0.1.0
:Author: Tiny
:Directory: Ampco
:Web: 
:Is certified: no

Description
-----------

::

  Module for Quality information, Localisation

Dependencies
------------

 * :mod:`base`
 * :mod:`product`
 * :mod:`sale`

Reports
-------

None


Menus
-------

 * Books/Configuration/Heatcode/Properties
 * Books/Configuration/Heatcode/Product Heatcode

Views
-----

 * \* INHERIT sale.order.inherit.form (form)
 * \* INHERIT sale.inherit.order.line.form2 (form)
 * \* INHERIT sale.inherit.order.line.form2_weight (form)
 * \* INHERIT product.normal.inherit.form (form)
 * \* INHERIT inherit_product.template.product.form (form)
 * properties.details (form)
 * properties.details (tree)
 * product.heatcode (tree)
 * product.heatcode (form)
 * \* INHERIT stock.production.lot.inherit.form (form)


Objects
-------

Object: Properties (properties.details)
#######################################



:property_type: Property Type, selection





:code: Code, char, required





:name: Name, char, required





:description: Desciption, char




Object: Product HeatCode (product.heatcode)
###########################################



:product_property: Property Values, one2many





:heatcode: HeatCode, char





:product_id: Product, many2one, required




Object: Product's Properties (product.properties)
#################################################



:heatcode_id: HeatCode, many2one, required





:value: Value, float





:property_id: Property, many2one, required





:comments: Comments, char


