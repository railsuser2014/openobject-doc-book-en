
.. i18n: .. module:: Ampco
.. i18n:     :synopsis: Ampco 
.. i18n:     :noindex:
.. i18n: .. 

.. module:: Ampco
    :synopsis: Ampco 
    :noindex:
.. 

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. i18n: Ampco (*Ampco*)
.. i18n: ===============
.. i18n: :Module: Ampco
.. i18n: :Name: Ampco
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: Ampco
.. i18n: :Web: 
.. i18n: :Official module: no
.. i18n: :Quality certified: no

Ampco (*Ampco*)
===============
:Module: Ampco
:Name: Ampco
:Version: 5.0.1.0
:Author: Tiny
:Directory: Ampco
:Web: 
:Official module: no
:Quality certified: no

.. i18n: Description
.. i18n: -----------

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   Module for Quality information, Localisation

::

  Module for Quality information, Localisation

.. i18n: Dependencies
.. i18n: ------------

Dependencies
------------

.. i18n:  * :mod:`base`
.. i18n:  * :mod:`product`
.. i18n:  * :mod:`sale`

 * :mod:`base`
 * :mod:`product`
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

.. i18n:  * Books/Configuration/Heatcode/Properties
.. i18n:  * Books/Configuration/Heatcode/Product Heatcode

 * Books/Configuration/Heatcode/Properties
 * Books/Configuration/Heatcode/Product Heatcode

.. i18n: Views
.. i18n: -----

Views
-----

.. i18n:  * \* INHERIT sale.order.inherit.form (form)
.. i18n:  * \* INHERIT sale.inherit.order.line.form2 (form)
.. i18n:  * \* INHERIT sale.inherit.order.line.form2_weight (form)
.. i18n:  * \* INHERIT product.normal.inherit.form (form)
.. i18n:  * \* INHERIT inherit_product.template.product.form (form)
.. i18n:  * properties.details (form)
.. i18n:  * properties.details (tree)
.. i18n:  * product.heatcode (tree)
.. i18n:  * product.heatcode (form)
.. i18n:  * \* INHERIT stock.production.lot.inherit.form (form)

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

.. i18n: Objects
.. i18n: -------

Objects
-------

.. i18n: Object: Properties (properties.details)
.. i18n: #######################################

Object: Properties (properties.details)
#######################################

.. i18n: :property_type: Property Type, selection

:property_type: Property Type, selection

.. i18n: :code: Code, char, required

:code: Code, char, required

.. i18n: :name: Name, char, required

:name: Name, char, required

.. i18n: :description: Desciption, char

:description: Desciption, char

.. i18n: Object: Product HeatCode (product.heatcode)
.. i18n: ###########################################

Object: Product HeatCode (product.heatcode)
###########################################

.. i18n: :product_property: Property Values, one2many

:product_property: Property Values, one2many

.. i18n: :heatcode: HeatCode, char

:heatcode: HeatCode, char

.. i18n: :product_id: Product, many2one, required

:product_id: Product, many2one, required

.. i18n: Object: Product's Properties (product.properties)
.. i18n: #################################################

Object: Product's Properties (product.properties)
#################################################

.. i18n: :heatcode_id: HeatCode, many2one, required

:heatcode_id: HeatCode, many2one, required

.. i18n: :value: Value, float

:value: Value, float

.. i18n: :property_id: Property, many2one, required

:property_id: Property, many2one, required

.. i18n: :comments: Comments, char

:comments: Comments, char
