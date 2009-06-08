
.. i18n: .. module:: product_variant_configurator
.. i18n:     :synopsis: Products with multi-level variants configurator 
.. i18n:     :noindex:
.. i18n: .. 

.. module:: product_variant_configurator
    :synopsis: Products with multi-level variants configurator 
    :noindex:
.. 

.. i18n: .. raw:: html
.. i18n: 
.. i18n:       <br />
.. i18n:     <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. raw:: html

      <br />
    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. i18n: .. tip:: This module is part of the Open ERP software, the leading Open Source 
.. i18n:   enterprise management system. If you want to discover Open ERP, check our 
.. i18n:   `screencasts <http://openerp.tv>`_ or download 
.. i18n:   `Open ERP <http://openerp.com>`_ directly.

.. tip:: This module is part of the Open ERP software, the leading Open Source 
  enterprise management system. If you want to discover Open ERP, check our 
  `screencasts <http://openerp.tv>`_ or download 
  `Open ERP <http://openerp.com>`_ directly.

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/product_variant_configurator"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/product_variant_configurator"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Products with multi-level variants configurator (*product_variant_configurator*)
.. i18n: ================================================================================
.. i18n: :Module: product_variant_configurator
.. i18n: :Name: Products with multi-level variants configurator
.. i18n: :Version: 5.0.0.5
.. i18n: :Author: Smile.fr
.. i18n: :Directory: product_variant_configurator
.. i18n: :Web: http://www.smile.fr
.. i18n: :Official module: no
.. i18n: :Quality certified: no

Products with multi-level variants configurator (*product_variant_configurator*)
================================================================================
:Module: product_variant_configurator
:Name: Products with multi-level variants configurator
:Version: 5.0.0.5
:Author: Smile.fr
:Directory: product_variant_configurator
:Web: http://www.smile.fr
:Official module: no
:Quality certified: no

.. i18n: Description
.. i18n: -----------

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   Product Configurator - WARNING WORK IN PROGRESS

::

  Product Configurator - WARNING WORK IN PROGRESS

.. i18n: Download links
.. i18n: --------------

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:

You can download this module as a zip file in the following version:

.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/product_variant_configurator.zip>`_

  * `trunk <http://www.openerp.com/download/modules/trunk/product_variant_configurator.zip>`_

.. i18n: Dependencies
.. i18n: ------------

Dependencies
------------

.. i18n:  * :mod:`product_variant_multi`
.. i18n:  * :mod:`sale`
.. i18n:  * :mod:`sale_product_multistep_configurator`

 * :mod:`product_variant_multi`
 * :mod:`sale`
 * :mod:`sale_product_multistep_configurator`

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

.. i18n:  * view_product_variant_configurator (form)
.. i18n:  * \* INHERIT product_variant_configurator.sale_order_form_view (form)
.. i18n:  * \* INHERIT product_variant_configurator.sale_order_line_form_view (form)

 * view_product_variant_configurator (form)
 * \* INHERIT product_variant_configurator.sale_order_form_view (form)
 * \* INHERIT product_variant_configurator.sale_order_line_form_view (form)

.. i18n: Objects
.. i18n: -------

Objects
-------

.. i18n: Object: sale.order.line.dimension_custom_values (sale.order.line.dimension_custom_values)
.. i18n: #########################################################################################

Object: sale.order.line.dimension_custom_values (sale.order.line.dimension_custom_values)
#########################################################################################

.. i18n: :mrp_production_id: Production Order, many2one

:mrp_production_id: Production Order, many2one

.. i18n: :sale_order_line_id: Sale Order Line, many2one

:sale_order_line_id: Sale Order Line, many2one

.. i18n: :custom_value: Custom Value, char

:custom_value: Custom Value, char

.. i18n: :dimension_type_id: Dimension Type, many2one

:dimension_type_id: Dimension Type, many2one

.. i18n: Object: product_variant_configurator.line (product_variant_configurator.line)
.. i18n: #############################################################################

Object: product_variant_configurator.line (product_variant_configurator.line)
#############################################################################

.. i18n: :dimension_type_id: Dimension Type, many2one

:dimension_type_id: Dimension Type, many2one

.. i18n: :dimension_custom_value: Custom Value, char

:dimension_custom_value: Custom Value, char

.. i18n: :allow_custom_value: Allow custom values ?, boolean

:allow_custom_value: Allow custom values ?, boolean

.. i18n: :dimension_type_value_id: Dimension Value, many2one

:dimension_type_value_id: Dimension Value, many2one

.. i18n: :configurator_id: product_variant_configurator Test, many2one

:configurator_id: product_variant_configurator Test, many2one

.. i18n: Object: product_variant_configurator.configurator (product_variant_configurator.configurator)
.. i18n: #############################################################################################

Object: product_variant_configurator.configurator (product_variant_configurator.configurator)
#############################################################################################

.. i18n: :product_tmpl_id: Product Template, many2one

:product_tmpl_id: Product Template, many2one

.. i18n: :dimension_configuration_line_ids: Configurator Lines, one2many

:dimension_configuration_line_ids: Configurator Lines, one2many

.. i18n: :product_variant_id: Product Variant, many2one

:product_variant_id: Product Variant, many2one
