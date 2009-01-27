
Module OScommerce Interface / ZenCart (*esale_osc*)
===================================================
:Module: esale_osc
:Name: OScommerce Interface / ZenCart
:Version: 5.0.1.0
:Directory: esale_osc
:Web: http://www.tinyerp.com

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

 * product - installed
 * stock - installed
 * sale - installed

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

Object: OScommerce Website
##########################

.. index::
  single: OScommerce Website object
.. 


:partner_anonymous_id: Anonymous, many2one, required



.. index::
  single: partner_anonymous_id field
.. 




:name: Name, char, required



.. index::
  single: name field
.. 




:url: URL, char, required



.. index::
  single: url field
.. 




:language_ids: Languages, one2many



.. index::
  single: language_ids field
.. 




:category_ids: Categories, one2many



.. index::
  single: category_ids field
.. 




:shop_id: Sale Shop, many2one, required



.. index::
  single: shop_id field
.. 




:product_ids: Web Products, one2many



.. index::
  single: product_ids field
.. 




:active: Active, boolean



.. index::
  single: active field
.. 




:tax_ids: Taxes, one2many



.. index::
  single: tax_ids field
.. 



Object: esale_osc Tax
#####################

.. index::
  single: esale_osc Tax object
.. 


:web_id: Website, many2one



.. index::
  single: web_id field
.. 




:esale_osc_id: esale_osc ID, integer



.. index::
  single: esale_osc_id field
.. 




:name: Tax name, char, required



.. index::
  single: name field
.. 




:tax_id: Tax, many2one



.. index::
  single: tax_id field
.. 



Object: esale_osc Category
##########################

.. index::
  single: esale_osc Category object
.. 


:web_id: Website, many2one



.. index::
  single: web_id field
.. 




:category_id: Category, many2one



.. index::
  single: category_id field
.. 




:esale_osc_id: esale_osc ID, integer, required



.. index::
  single: esale_osc_id field
.. 




:name: Name, char



.. index::
  single: name field
.. 



Object: esale_osc Product
#########################

.. index::
  single: esale_osc Product object
.. 


:esale_osc_id: esale_osc product id, integer



.. index::
  single: esale_osc_id field
.. 




:web_id: Web Ref, many2one



.. index::
  single: web_id field
.. 




:name: Name, char, required



.. index::
  single: name field
.. 




:esale_osc_tax_id: esale_osc tax, many2one



.. index::
  single: esale_osc_tax_id field
.. 




:product_id: Product, many2one, required



.. index::
  single: product_id field
.. 



Object: esale_osc Language
##########################

.. index::
  single: esale_osc Language object
.. 


:web_id: Website, many2one



.. index::
  single: web_id field
.. 




:esale_osc_id: esale_osc ID, integer, required



.. index::
  single: esale_osc_id field
.. 




:name: Name, char, required



.. index::
  single: name field
.. 




:language_id: Language, many2one



.. index::
  single: language_id field
.. 

