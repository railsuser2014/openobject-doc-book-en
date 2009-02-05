
.. module:: esale_osc
    :synopsis: OScommerce Interface / ZenCart 
    :noindex:
.. 

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

OScommerce Interface / ZenCart (*esale_osc*)
============================================
:Module: esale_osc
:Name: OScommerce Interface / ZenCart
:Version: 5.0.1.0
:Author: Tiny / modified by Lucien Moerkamp
:Directory: esale_osc
:Web: http://www.tinyerp.com
:Official module: no
:Quality certified: no

Description
-----------

::

  OSCommerce (Zencart) eCommerce interface synchronisation.
  Users can order on the website, orders are automatically imported in Tiny
  ERP.
  
  You can export products, stock level and create links between
  categories of products, taxes and languages.
  
  If you product has an image attched, it send the image to the Joomla website.

Dependencies
------------

 * :mod:`product`
 * :mod:`stock`
 * :mod:`sale`

Reports
-------

None


Menus
-------

 * Sales Management/Internet Sales
 * Sales Management/Internet Sales/Websites
 * Sales Management/Internet Sales/Sale Orders

Views
-----

 * esale_osc.web.form (form)
 * esale_osc.language.web.form (form)
 * esale_osc.tax.web.form (form)
 * esale_osc.category.web.form (form)
 * esale_osc.product.web.form (form)
 * esale_osc.saleorder.tree (tree)
 * esale_osc.saleorder.form (form)


Objects
-------

Object: OScommerce Website (esale_osc.web)
##########################################



:partner_anonymous_id: Anonymous, many2one, required





:name: Name, char, required





:url: URL, char, required





:language_ids: Languages, one2many





:category_ids: Categories, one2many





:shop_id: Sale Shop, many2one, required





:product_ids: Web Products, one2many





:active: Active, boolean





:tax_ids: Taxes, one2many




Object: esale_osc Tax (esale_osc.tax)
#####################################



:web_id: Website, many2one





:esale_osc_id: esale_osc ID, integer





:name: Tax name, char, required





:tax_id: Tax, many2one




Object: esale_osc Category (esale_osc.category)
###############################################



:web_id: Website, many2one





:category_id: Category, many2one





:esale_osc_id: esale_osc ID, integer, required





:name: Name, char




Object: esale_osc Product (esale_osc.product)
#############################################



:esale_osc_id: esale_osc product id, integer





:web_id: Web Ref, many2one





:name: Name, char, required





:esale_osc_tax_id: esale_osc tax, many2one





:product_id: Product, many2one, required




Object: esale_osc Language (esale_osc.lang)
###########################################



:web_id: Website, many2one





:esale_osc_id: esale_osc ID, integer, required





:name: Name, char, required





:language_id: Language, many2one


