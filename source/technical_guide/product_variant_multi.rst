
.. module:: product_variant_multi
    :synopsis: Products with multi-level variants
    :noindex:
.. 

Products with multi-level variants (*product_variant_multi*)
============================================================
:Module: product_variant_multi
:Name: Products with multi-level variants
:Version: 5.0.1.0
:Directory: product_variant_multi
:Web: 
:Is certified: no

Description
-----------

::

  None

Dependencies
------------

 * product - installed

Reports
-------

None


Menus
-------

 * Books/Products/Product Templates
 * Books/Products/Product Variants

Views
-----


None



Objects
-------

Object: Dimension Type (product.variant.dimension.type)
#######################################################



:name: Dimension, char





:value_ids: Dimension Values, one2many





:sequence: Sequence, integer




Object: Dimension Type (product.variant.dimension.value)
########################################################



:dimension_id: Dimension, many2one, required





:price_extra: Dimension Values, float





:price_margin: Dimension Values, float





:name: Dimension Value, char





:sequence: Sequence, integer


