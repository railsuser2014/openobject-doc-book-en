
.. module:: esale_osc
    :synopsis: OScommerce Interface / ZenCart 
    :noindex:
.. 

.. raw:: html

      <br />
    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. tip:: This module is part of the Open ERP software, the leading Open Source 
  enterprise management system. If you want to discover Open ERP, check our 
  `screencasts <href="http://openerp.tv>`_ or download 
  `Open ERP <href="http://openerp.com>`_ directly.

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/esale_osc"></div>
    <script src="http://js-kit.com/ratings.js"></script>

OScommerce Interface / ZenCart (*esale_osc*)
============================================
:Module: esale_osc
:Name: OScommerce Interface / ZenCart
:Version: 5.0.1.0
:Author: Axelor/Zikzakmedia
:Directory: esale_osc
:Web: http://www.zikzakmedia.com
:Official module: no
:Quality certified: no

Description
-----------

::

  OSCommerce (Zencart) eCommerce interface synchronisation.
  Users can order on the website, orders are automatically imported in OpenERP.
  
  You can export products, stock level and create links between
  categories of products, taxes and languages.
  
  If you product has an image attached, it sends the image to the OScommerce website.
  
  Developed by Tiny, Axelor and Zikzakmedia

Download links
--------------

You can download this module as a zip file in the following version:

  * `trunk </download/modules/trunk/esale_osc.zip>`_


Dependencies
------------

 * :mod:`product`
 * :mod:`stock`
 * :mod:`sale`
 * :mod:`account_payment`

Reports
-------

None


Menus
-------

 * Sales Management/Internet Sales
 * Sales Management/Internet Sales/Websites
 * Sales Management/Internet Sales/Web sale orders
 * Sales Management/Internet Sales/Web sale orders/New order
 * Sales Management/Internet Sales/Web sale orders/Request for quotation
 * Sales Management/Internet Sales/Web sale orders/Waiting invoice
 * Sales Management/Internet Sales/Web sale orders/In progress
 * Sales Management/Internet Sales/Invoices
 * Sales Management/Internet Sales/Invoices/Draft
 * Sales Management/Internet Sales/Invoices/PRO-FORMA
 * Sales Management/Internet Sales/Invoices/Opened
 * Sales Management/Internet Sales/Synchronize products and stocks to all OScommerce web shops
 * Sales Management/Internet Sales/Update stocks to all OScommerce web shops
 * Sales Management/Internet Sales/Manufacturers

Views
-----

 * esale.oscom.web.form (form)
 * esale.oscom.web.form (tree)
 * esale.oscom.language.web.form (form)
 * esale.oscom.language.web.tree (tree)
 * esale.oscom.tax.web.form (form)
 * esale.oscom.tax.web.tree (tree)
 * esale.oscom.pay.typ.form (form)
 * esale.oscom.pay.typ.tree (tree)
 * esale.oscom.category.web.form (form)
 * esale.oscom.category.web.v (tree)
 * esale.oscom.product.web.form (form)
 * esale.oscom.saleorder.tree (tree)
 * esale.oscom.saleorder.form (form)
 * \* INHERIT esale.oscom.product.add.oscom.fields (form)
 * esale.oscom.product.maufacturer.view.form (form)
 * esale.oscom.product.maufacturer.view.tree (tree)


Objects
-------

Object: OScommerce Website (esale.oscom.web)
############################################



:pay_typ_ids: Payment types, one2many





:name: Name, char, required





:url: URL, char, required





:language_ids: Languages, one2many





:category_ids: Categories, one2many





:esale_account_id: Dest Account, many2one, required

    *Payment account for web invoices.*



:shop_id: Sale Shop, many2one, required





:product_ids: Web Products, one2many





:active: Active, boolean





:price_type: Price type, selection, required





:tax_ids: Taxes, one2many




Object: esale_oscom Tax (esale.oscom.tax)
#########################################



:web_id: Website, many2one





:name: Tax name, char, required, readonly





:esale_oscom_id: OScommerce Id, integer





:tax_id: OpenERP Tax, many2one




Object: esale_oscom Category (esale.oscom.category)
###################################################



:category_id: OpenERP Category, many2one





:web_id: Website, many2one





:name: Name, char, readonly





:esale_oscom_id: OScommerce Id, integer, required




Object: esale_oscom PayType (esale.oscom.paytype)
#################################################



:payment_id: OpenERP payment, many2one





:paytyp: Payment Type, selection





:web_id: Website, many2one





:name: Name, char, readonly





:esale_oscom_id: OScommerce Id, integer, required




Object: esale_oscom Product (esale.oscom.product)
#################################################



:web_id: Website, many2one





:esale_oscom_tax_id: OScommerce tax, many2one





:name: Name, char, required, readonly





:esale_oscom_id: OScommerce product Id, integer





:product_id: OpenERP Product, many2one




Object: esale_oscom Language (esale.oscom.lang)
###############################################



:web_id: Website, many2one





:name: Name, char, required, readonly





:esale_oscom_id: OScommerce Id, integer, required





:language_id: OpenERP Language, many2one




Object: Product Manufacturer that produces the product (product.manufacturer)
#############################################################################



:manufacturer_url: URL, char





:name: Name, char, required


