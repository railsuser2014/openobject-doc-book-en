
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/esale_osc"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/esale_osc"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: OScommerce Interface / ZenCart (*esale_osc*)
.. i18n: ============================================
.. i18n: :Module: esale_osc
.. i18n: :Name: OScommerce Interface / ZenCart
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Axelor/Zikzakmedia
.. i18n: :Directory: esale_osc
.. i18n: :Web: http://www.zikzakmedia.com
.. i18n: :Official module: no
.. i18n: :Quality certified: no

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

.. i18n: Description
.. i18n: -----------

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   OSCommerce (Zencart) eCommerce interface synchronisation.
.. i18n:   Users can order on the website, orders are automatically imported in OpenERP.
.. i18n:   
.. i18n:   You can export products, stock level and create links between
.. i18n:   categories of products, taxes and languages.
.. i18n:   
.. i18n:   If you product has an image attached, it sends the image to the OScommerce website.
.. i18n:   
.. i18n:   Developed by Tiny, Axelor and Zikzakmedia

::

  OSCommerce (Zencart) eCommerce interface synchronisation.
  Users can order on the website, orders are automatically imported in OpenERP.
  
  You can export products, stock level and create links between
  categories of products, taxes and languages.
  
  If you product has an image attached, it sends the image to the OScommerce website.
  
  Developed by Tiny, Axelor and Zikzakmedia

.. i18n: Download links
.. i18n: --------------

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:

You can download this module as a zip file in the following version:

.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/esale_osc.zip>`_

  * `trunk <http://www.openerp.com/download/modules/trunk/esale_osc.zip>`_

.. i18n: Dependencies
.. i18n: ------------

Dependencies
------------

.. i18n:  * :mod:`product`
.. i18n:  * :mod:`stock`
.. i18n:  * :mod:`sale`
.. i18n:  * :mod:`account_payment`

 * :mod:`product`
 * :mod:`stock`
 * :mod:`sale`
 * :mod:`account_payment`

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
.. i18n:  * Sales Management/Internet Sales/Web sale orders
.. i18n:  * Sales Management/Internet Sales/Web sale orders/New order
.. i18n:  * Sales Management/Internet Sales/Web sale orders/Request for quotation
.. i18n:  * Sales Management/Internet Sales/Web sale orders/Waiting invoice
.. i18n:  * Sales Management/Internet Sales/Web sale orders/In progress
.. i18n:  * Sales Management/Internet Sales/Invoices
.. i18n:  * Sales Management/Internet Sales/Invoices/Draft
.. i18n:  * Sales Management/Internet Sales/Invoices/PRO-FORMA
.. i18n:  * Sales Management/Internet Sales/Invoices/Opened
.. i18n:  * Sales Management/Internet Sales/Synchronize products and stocks to all OScommerce web shops
.. i18n:  * Sales Management/Internet Sales/Update stocks to all OScommerce web shops
.. i18n:  * Sales Management/Internet Sales/Manufacturers

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

.. i18n: Views
.. i18n: -----

Views
-----

.. i18n:  * esale.oscom.web.form (form)
.. i18n:  * esale.oscom.web.form (tree)
.. i18n:  * esale.oscom.language.web.form (form)
.. i18n:  * esale.oscom.language.web.tree (tree)
.. i18n:  * esale.oscom.tax.web.form (form)
.. i18n:  * esale.oscom.tax.web.tree (tree)
.. i18n:  * esale.oscom.pay.typ.form (form)
.. i18n:  * esale.oscom.pay.typ.tree (tree)
.. i18n:  * esale.oscom.category.web.form (form)
.. i18n:  * esale.oscom.category.web.v (tree)
.. i18n:  * esale.oscom.product.web.form (form)
.. i18n:  * esale.oscom.saleorder.tree (tree)
.. i18n:  * esale.oscom.saleorder.form (form)
.. i18n:  * \* INHERIT esale.oscom.product.add.oscom.fields (form)
.. i18n:  * esale.oscom.product.maufacturer.view.form (form)
.. i18n:  * esale.oscom.product.maufacturer.view.tree (tree)

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

.. i18n: Objects
.. i18n: -------

Objects
-------

.. i18n: Object: OScommerce Website (esale.oscom.web)
.. i18n: ############################################

Object: OScommerce Website (esale.oscom.web)
############################################

.. i18n: :pay_typ_ids: Payment types, one2many

:pay_typ_ids: Payment types, one2many

.. i18n: :name: Name, char, required

:name: Name, char, required

.. i18n: :url: URL, char, required

:url: URL, char, required

.. i18n: :language_ids: Languages, one2many

:language_ids: Languages, one2many

.. i18n: :category_ids: Categories, one2many

:category_ids: Categories, one2many

.. i18n: :esale_account_id: Dest Account, many2one, required

:esale_account_id: Dest Account, many2one, required

.. i18n:     *Payment account for web invoices.*

    *Payment account for web invoices.*

.. i18n: :shop_id: Sale Shop, many2one, required

:shop_id: Sale Shop, many2one, required

.. i18n: :product_ids: Web Products, one2many

:product_ids: Web Products, one2many

.. i18n: :active: Active, boolean

:active: Active, boolean

.. i18n: :price_type: Price type, selection, required

:price_type: Price type, selection, required

.. i18n: :tax_ids: Taxes, one2many

:tax_ids: Taxes, one2many

.. i18n: Object: esale_oscom Tax (esale.oscom.tax)
.. i18n: #########################################

Object: esale_oscom Tax (esale.oscom.tax)
#########################################

.. i18n: :web_id: Website, many2one

:web_id: Website, many2one

.. i18n: :name: Tax name, char, required, readonly

:name: Tax name, char, required, readonly

.. i18n: :esale_oscom_id: OScommerce Id, integer

:esale_oscom_id: OScommerce Id, integer

.. i18n: :tax_id: OpenERP Tax, many2one

:tax_id: OpenERP Tax, many2one

.. i18n: Object: esale_oscom Category (esale.oscom.category)
.. i18n: ###################################################

Object: esale_oscom Category (esale.oscom.category)
###################################################

.. i18n: :category_id: OpenERP Category, many2one

:category_id: OpenERP Category, many2one

.. i18n: :web_id: Website, many2one

:web_id: Website, many2one

.. i18n: :name: Name, char, readonly

:name: Name, char, readonly

.. i18n: :esale_oscom_id: OScommerce Id, integer, required

:esale_oscom_id: OScommerce Id, integer, required

.. i18n: Object: esale_oscom PayType (esale.oscom.paytype)
.. i18n: #################################################

Object: esale_oscom PayType (esale.oscom.paytype)
#################################################

.. i18n: :payment_id: OpenERP payment, many2one

:payment_id: OpenERP payment, many2one

.. i18n: :paytyp: Payment Type, selection

:paytyp: Payment Type, selection

.. i18n: :web_id: Website, many2one

:web_id: Website, many2one

.. i18n: :name: Name, char, readonly

:name: Name, char, readonly

.. i18n: :esale_oscom_id: OScommerce Id, integer, required

:esale_oscom_id: OScommerce Id, integer, required

.. i18n: Object: esale_oscom Product (esale.oscom.product)
.. i18n: #################################################

Object: esale_oscom Product (esale.oscom.product)
#################################################

.. i18n: :web_id: Website, many2one

:web_id: Website, many2one

.. i18n: :esale_oscom_tax_id: OScommerce tax, many2one

:esale_oscom_tax_id: OScommerce tax, many2one

.. i18n: :name: Name, char, required, readonly

:name: Name, char, required, readonly

.. i18n: :esale_oscom_id: OScommerce product Id, integer

:esale_oscom_id: OScommerce product Id, integer

.. i18n: :product_id: OpenERP Product, many2one

:product_id: OpenERP Product, many2one

.. i18n: Object: esale_oscom Language (esale.oscom.lang)
.. i18n: ###############################################

Object: esale_oscom Language (esale.oscom.lang)
###############################################

.. i18n: :web_id: Website, many2one

:web_id: Website, many2one

.. i18n: :name: Name, char, required, readonly

:name: Name, char, required, readonly

.. i18n: :esale_oscom_id: OScommerce Id, integer, required

:esale_oscom_id: OScommerce Id, integer, required

.. i18n: :language_id: OpenERP Language, many2one

:language_id: OpenERP Language, many2one

.. i18n: Object: Product Manufacturer that produces the product (product.manufacturer)
.. i18n: #############################################################################

Object: Product Manufacturer that produces the product (product.manufacturer)
#############################################################################

.. i18n: :manufacturer_url: URL, char

:manufacturer_url: URL, char

.. i18n: :name: Name, char, required

:name: Name, char, required
