
.. i18n: .. module:: product_variant_multi
.. i18n:     :synopsis: Products with multi-level variants 
.. i18n:     :noindex:
.. i18n: .. 

.. module:: product_variant_multi
    :synopsis: Products with multi-level variants 
    :noindex:
.. 

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. i18n: Products with multi-level variants (*product_variant_multi*)
.. i18n: ============================================================
.. i18n: :Module: product_variant_multi
.. i18n: :Name: Products with multi-level variants
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: product_variant_multi
.. i18n: :Web: 
.. i18n: :Official module: no
.. i18n: :Quality certified: no

Products with multi-level variants (*product_variant_multi*)
============================================================
:Module: product_variant_multi
:Name: Products with multi-level variants
:Version: 5.0.1.0
:Author: Tiny
:Directory: product_variant_multi
:Web: 
:Official module: no
:Quality certified: no

.. i18n: Description
.. i18n: -----------

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   None

::

  None

.. i18n: Dependencies
.. i18n: ------------

Dependencies
------------

.. i18n:  * :mod:`product`

 * :mod:`product`

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

.. i18n:  * Books/Products/Product Templates
.. i18n:  * Books/Products/Product Variants

 * Books/Products/Product Templates
 * Books/Products/Product Variants

.. i18n: Views
.. i18n: -----

Views
-----

.. i18n: None

None

.. i18n: Objects
.. i18n: -------

Objects
-------

.. i18n: Object: Dimension Type (product.variant.dimension.type)
.. i18n: #######################################################

Object: Dimension Type (product.variant.dimension.type)
#######################################################

.. i18n: :name: Dimension, char

:name: Dimension, char

.. i18n: :value_ids: Dimension Values, one2many

:value_ids: Dimension Values, one2many

.. i18n: :sequence: Sequence, integer

:sequence: Sequence, integer

.. i18n: Object: Dimension Type (product.variant.dimension.value)
.. i18n: ########################################################

Object: Dimension Type (product.variant.dimension.value)
########################################################

.. i18n: :dimension_id: Dimension, many2one, required

:dimension_id: Dimension, many2one, required

.. i18n: :price_extra: Dimension Values, float

:price_extra: Dimension Values, float

.. i18n: :price_margin: Dimension Values, float

:price_margin: Dimension Values, float

.. i18n: :name: Dimension Value, char

:name: Dimension Value, char

.. i18n: :sequence: Sequence, integer

:sequence: Sequence, integer
