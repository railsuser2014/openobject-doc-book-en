
.. i18n: .. module:: esale_osc
.. i18n:     :synopsis: OScommerce Interface / ZenCart 
.. i18n:     :noindex:
.. i18n: .. 

.. module:: esale_osc
    :synopsis: OScommerce Interface / ZenCart 
    :noindex:
.. 

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. i18n: OScommerce Interface / ZenCart (*esale_osc*)
.. i18n: ============================================
.. i18n: :Module: esale_osc
.. i18n: :Name: OScommerce Interface / ZenCart
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny / modified by Lucien Moerkamp
.. i18n: :Directory: esale_osc
.. i18n: :Web: http://www.openerp.com/
.. i18n: :Official module: no
.. i18n: :Quality certified: no

OScommerce Interface / ZenCart (*esale_osc*)
============================================
:Module: esale_osc
:Name: OScommerce Interface / ZenCart
:Version: 5.0.1.0
:Author: Tiny / modified by Lucien Moerkamp
:Directory: esale_osc
:Web: http://www.openerp.com/
:Official module: no
:Quality certified: no

.. i18n: Description
.. i18n: -----------

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   OSCommerce (Zencart) eCommerce interface synchronisation.
.. i18n:   Users can order on the website, orders are automatically imported in Tiny ERP.
.. i18n:   
.. i18n:   You can export products, stock level and create links between categories of products, 
.. i18n: taxes and languages.
.. i18n:   
.. i18n:   If you product has an image attched, it send the image to the Joomla website.

::

  OSCommerce (Zencart) eCommerce interface synchronisation.
  Users can order on the website, orders are automatically imported in Tiny ERP.
  
  You can export products, stock level and create links between categories of products, 
taxes and languages.
  
  If you product has an image attched, it send the image to the Joomla website.

.. i18n: Dependencies
.. i18n: ------------

Dependencies
------------

.. i18n:  * :mod:`product`
.. i18n:  * :mod:`stock`
.. i18n:  * :mod:`sale`

 * :mod:`product`
 * :mod:`stock`
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

.. i18n:  * Sales Management/Internet Sales
.. i18n:  * Sales Management/Internet Sales/Websites
.. i18n:  * Sales Management/Internet Sales/Sale Orders

 * Sales Management/Internet Sales
 * Sales Management/Internet Sales/Websites
 * Sales Management/Internet Sales/Sale Orders

.. i18n: Views
.. i18n: -----

Views
-----

.. i18n:  * esale_osc.web.form (form)
.. i18n:  * esale_osc.language.web.form (form)
.. i18n:  * esale_osc.tax.web.form (form)
.. i18n:  * esale_osc.category.web.form (form)
.. i18n:  * esale_osc.product.web.form (form)
.. i18n:  * esale_osc.saleorder.tree (tree)
.. i18n:  * esale_osc.saleorder.form (form)

 * esale_osc.web.form (form)
 * esale_osc.language.web.form (form)
 * esale_osc.tax.web.form (form)
 * esale_osc.category.web.form (form)
 * esale_osc.product.web.form (form)
 * esale_osc.saleorder.tree (tree)
 * esale_osc.saleorder.form (form)

.. i18n: Objects
.. i18n: -------

Objects
-------

.. i18n: Object: OScommerce Website (esale_osc.web)
.. i18n: ##########################################

Object: OScommerce Website (esale_osc.web)
##########################################

.. i18n: :partner_anonymous_id: Anonymous, many2one, required

:partner_anonymous_id: Anonymous, many2one, required

.. i18n: :name: Name, char, required

:name: Name, char, required

.. i18n: :url: URL, char, required

:url: URL, char, required

.. i18n: :language_ids: Languages, one2many

:language_ids: Languages, one2many

.. i18n: :category_ids: Categories, one2many

:category_ids: Categories, one2many

.. i18n: :shop_id: Sale Shop, many2one, required

:shop_id: Sale Shop, many2one, required

.. i18n: :product_ids: Web Products, one2many

:product_ids: Web Products, one2many

.. i18n: :active: Active, boolean

:active: Active, boolean

.. i18n: :tax_ids: Taxes, one2many

:tax_ids: Taxes, one2many

.. i18n: Object: esale_osc Tax (esale_osc.tax)
.. i18n: #####################################

Object: esale_osc Tax (esale_osc.tax)
#####################################

.. i18n: :web_id: Website, many2one

:web_id: Website, many2one

.. i18n: :esale_osc_id: esale_osc ID, integer

:esale_osc_id: esale_osc ID, integer

.. i18n: :name: Tax name, char, required

:name: Tax name, char, required

.. i18n: :tax_id: Tax, many2one

:tax_id: Tax, many2one

.. i18n: Object: esale_osc Category (esale_osc.category)
.. i18n: ###############################################

Object: esale_osc Category (esale_osc.category)
###############################################

.. i18n: :web_id: Website, many2one

:web_id: Website, many2one

.. i18n: :category_id: Category, many2one

:category_id: Category, many2one

.. i18n: :esale_osc_id: esale_osc ID, integer, required

:esale_osc_id: esale_osc ID, integer, required

.. i18n: :name: Name, char

:name: Name, char

.. i18n: Object: esale_osc Product (esale_osc.product)
.. i18n: #############################################

Object: esale_osc Product (esale_osc.product)
#############################################

.. i18n: :esale_osc_id: esale_osc product id, integer

:esale_osc_id: esale_osc product id, integer

.. i18n: :web_id: Web Ref, many2one

:web_id: Web Ref, many2one

.. i18n: :name: Name, char, required

:name: Name, char, required

.. i18n: :esale_osc_tax_id: esale_osc tax, many2one

:esale_osc_tax_id: esale_osc tax, many2one

.. i18n: :product_id: Product, many2one, required

:product_id: Product, many2one, required

.. i18n: Object: esale_osc Language (esale_osc.lang)
.. i18n: ###########################################

Object: esale_osc Language (esale_osc.lang)
###########################################

.. i18n: :web_id: Website, many2one

:web_id: Website, many2one

.. i18n: :esale_osc_id: esale_osc ID, integer, required

:esale_osc_id: esale_osc ID, integer, required

.. i18n: :name: Name, char, required

:name: Name, char, required

.. i18n: :language_id: Language, many2one

:language_id: Language, many2one
