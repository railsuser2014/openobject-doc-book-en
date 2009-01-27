
Module Ampco (*Ampco*)
======================
:Module: Ampco
:Name: Ampco
:Version: 5.0.1.0
:Directory: Ampco
:Web: 

Description
-----------

::

  Module for Quality information, Localisation

Dependencies
------------

 * base - installed
 * product - installed
 * sale - installed

Reports
-------

None


Menus
-------

 * Products/Configuration/Heatcode/Properties
 * Products/Configuration/Heatcode/Product Heatcode

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

Object: Properties
##################

.. index::
  single: Properties object
.. 


:property_type: Property Type, selection



.. index::
  single: property_type field
.. 




:code: Code, char, required



.. index::
  single: code field
.. 




:name: Name, char, required



.. index::
  single: name field
.. 




:description: Desciption, char



.. index::
  single: description field
.. 



Object: Product HeatCode
########################

.. index::
  single: Product HeatCode object
.. 


:product_property: Property Values, one2many



.. index::
  single: product_property field
.. 




:heatcode: HeatCode, char



.. index::
  single: heatcode field
.. 




:product_id: Product, many2one, required



.. index::
  single: product_id field
.. 



Object: Product's Properties
############################

.. index::
  single: Product's Properties object
.. 


:heatcode_id: HeatCode, many2one, required



.. index::
  single: heatcode_id field
.. 




:value: Value, float



.. index::
  single: value field
.. 




:property_id: Property, many2one, required



.. index::
  single: property_id field
.. 




:comments: Comments, char



.. index::
  single: comments field
.. 

