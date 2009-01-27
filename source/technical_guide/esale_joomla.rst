
Module eSale Interface - Joomla (*esale_joomla*)
================================================
:Module: esale_joomla
:Name: eSale Interface - Joomla
:Version: 5.0.1.0
:Directory: esale_joomla
:Web: http://tinyerp.com

Description
-----------

::

  Joomla (Virtuemart) eCommerce interface synchronisation.
  Users can order on the website, orders are automatically imported in Tiny
  ERP.
  
  You can export products, product's categories, account taxes,  stock level and create links between
  categories of products, taxes and languages.
  
  If you product has an image attched, it send the image to the Joomla website.

Dependencies
------------

 * product - installed
 * stock - installed
 * sale - installed
 * account - installed
 * account_tax_include - installed

Reports
-------

None


Menus
-------


None


Views
-----


None



Objects
-------

Object: eCommerce Website
#########################

.. index::
  single: eCommerce Website object
.. 


:taxes_included_ids: Taxes included, many2many



.. index::
  single: taxes_included_ids field
.. 




:name: Name, char, required



.. index::
  single: name field
.. 




:url: URL, char, required



.. index::
  single: url field
.. 




:language_id: Language, many2one



.. index::
  single: language_id field
.. 




:category_ids: Categories, one2many



.. index::
  single: category_ids field
.. 




:shop_id: Sale Shop, many2one, required



.. index::
  single: shop_id field
.. 




:product_ids: Products, one2many



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



Object: eSale Tax
#################

.. index::
  single: eSale Tax object
.. 


:web_id: Website, many2one



.. index::
  single: web_id field
.. 




:name: Tax name, char, required



.. index::
  single: name field
.. 




:esale_joomla_id: eSale id, integer



.. index::
  single: esale_joomla_id field
.. 




:tax_id: Tax, many2one



.. index::
  single: tax_id field
.. 



Object: eSale Category
######################

.. index::
  single: eSale Category object
.. 


:include_childs: Include Childs, boolean

    *If checked, Tiny ERP will also export products from categories that are childs of this one.*

.. index::
  single: include_childs field
.. 




:category_id: Category, many2one



.. index::
  single: category_id field
.. 




:web_id: Website, many2one



.. index::
  single: web_id field
.. 




:name: Name, char, required



.. index::
  single: name field
.. 




:esale_joomla_id: Web ID, integer, required, readonly



.. index::
  single: esale_joomla_id field
.. 



Object: eSale Product
#####################

.. index::
  single: eSale Product object
.. 


:esale_joomla_tax_id: eSale tax, many2one



.. index::
  single: esale_joomla_tax_id field
.. 




:web_id: Web Ref, many2one



.. index::
  single: web_id field
.. 




:name: Name, char, required



.. index::
  single: name field
.. 




:esale_joomla_id: eSale product id, integer



.. index::
  single: esale_joomla_id field
.. 




:product_id: Product, many2one, required



.. index::
  single: product_id field
.. 



Object: eSale Language
######################

.. index::
  single: eSale Language object
.. 


:web_id: Website, many2one



.. index::
  single: web_id field
.. 




:name: Name, char, required



.. index::
  single: name field
.. 




:esale_joomla_id: Web ID, integer, required



.. index::
  single: esale_joomla_id field
.. 




:language_id: Language, many2one



.. index::
  single: language_id field
.. 



Object: eShop Partner
#####################

.. index::
  single: eShop Partner object
.. 


:city: City, char



.. index::
  single: city field
.. 




:address_id: Partner Address, many2one



.. index::
  single: address_id field
.. 




:name: Name, char, required



.. index::
  single: name field
.. 




:zip: Zip, char



.. index::
  single: zip field
.. 




:country: Country, char



.. index::
  single: country field
.. 




:state: State, char



.. index::
  single: state field
.. 




:esale_id: eSale ID, char



.. index::
  single: esale_id field
.. 




:address: Address, char



.. index::
  single: address field
.. 




:email: Mail, char



.. index::
  single: email field
.. 



Object: esale_joomla.order
##########################

.. index::
  single: esale_joomla.order object
.. 


:web_id: Web Shop, many2one, required



.. index::
  single: web_id field
.. 




:name: Order Description, char, required



.. index::
  single: name field
.. 




:epartner_shipping_id: Joomla Shipping Address, many2one, required



.. index::
  single: epartner_shipping_id field
.. 




:order_id: Sale Order, many2one



.. index::
  single: order_id field
.. 




:epartner_invoice_id: Joomla Invoice Address, many2one, required



.. index::
  single: epartner_invoice_id field
.. 




:web_ref: Web Ref, integer



.. index::
  single: web_ref field
.. 




:note: Notes, text



.. index::
  single: note field
.. 




:state: Order State, selection



.. index::
  single: state field
.. 




:partner_shipping_id: Shipping Address, many2one



.. index::
  single: partner_shipping_id field
.. 




:partner_invoice_id: Invoice Address, many2one



.. index::
  single: partner_invoice_id field
.. 




:date_order: Date Ordered, date, required



.. index::
  single: date_order field
.. 




:partner_id: Contact Address, many2one



.. index::
  single: partner_id field
.. 




:order_lines: Order Lines, one2many



.. index::
  single: order_lines field
.. 



Object: eSale Order line
########################

.. index::
  single: eSale Order line object
.. 


:product_id: Product, many2one



.. index::
  single: product_id field
.. 




:order_id: eOrder Ref, many2one



.. index::
  single: order_id field
.. 




:product_uom_id: Unit of Measure, many2one, required



.. index::
  single: product_uom_id field
.. 




:price_unit: Unit Price, float, required



.. index::
  single: price_unit field
.. 




:product_qty: Quantity, float, required



.. index::
  single: product_qty field
.. 




:name: Order Line, char, required



.. index::
  single: name field
.. 



Object: eSale webshop Synchronisation log
#########################################

.. index::
  single: eSale webshop Synchronisation log object
.. 


:log_date: Log date, datetime, required



.. index::
  single: log_date field
.. 




:user_id: Exported By, many2one, required



.. index::
  single: user_id field
.. 




:web_id: Web Ref, many2one



.. index::
  single: web_id field
.. 




:name: Synchronisation Log, char, required



.. index::
  single: name field
.. 




:log_type: Export type, selection, readonly



.. index::
  single: log_type field
.. 

