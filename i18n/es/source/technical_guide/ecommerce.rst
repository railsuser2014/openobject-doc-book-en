
.. i18n: .. module:: ecommerce
.. i18n:     :synopsis: E-Commerce 
.. i18n:     :noindex:
.. i18n: .. 

.. module:: ecommerce
    :synopsis: E-Commerce 
    :noindex:
.. 

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. i18n: E-Commerce (*ecommerce*)
.. i18n: ========================
.. i18n: :Module: ecommerce
.. i18n: :Name: E-Commerce
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: e-tiny
.. i18n: :Directory: ecommerce
.. i18n: :Web: http://www.etiny.com
.. i18n: :Official module: no
.. i18n: :Quality certified: no

E-Commerce (*ecommerce*)
========================
:Module: ecommerce
:Name: E-Commerce
:Version: 5.0.1.0
:Author: e-tiny
:Directory: ecommerce
:Web: http://www.etiny.com
:Official module: no
:Quality certified: no

.. i18n: Description
.. i18n: -----------

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   eCommerce Users can order on the website, orders are automatically imported in TinyERP.
.. i18n:   You can configure products, categories of products, language, currency, carrier, pay 
.. i18n: and also configure row,column,images.

::

  eCommerce Users can order on the website, orders are automatically imported in TinyERP.
  You can configure products, categories of products, language, currency, carrier, pay 
and also configure row,column,images.

.. i18n: Dependencies
.. i18n: ------------

Dependencies
------------

.. i18n:  * :mod:`delivery`
.. i18n:  * :mod:`base`
.. i18n:  * :mod:`product`
.. i18n:  * :mod:`sale`

 * :mod:`delivery`
 * :mod:`base`
 * :mod:`product`
 * :mod:`sale`

.. i18n: Reports
.. i18n: -------

Reports
-------

.. i18n:  * Shipping Invoice

 * Shipping Invoice

.. i18n: Menus
.. i18n: -------

Menus
-------

.. i18n:  * Ecommerce
.. i18n:  * Ecommerce/Configuration
.. i18n:  * Ecommerce/Configuration/Web Shop
.. i18n:  * Ecommerce/Products
.. i18n:  * Ecommerce/Products/Products by Category
.. i18n:  * Ecommerce/Payment Configuration
.. i18n:  * Ecommerce/Payment Configuration/Payment
.. i18n:  * Ecommerce/Configuration/Payment method
.. i18n:  * Ecommerce/Payment Configuration/Payment Received
.. i18n:  * Ecommerce/Payment Configuration/Credit Cards
.. i18n:  * Ecommerce/Partners
.. i18n:  * Ecommerce/Partners/Partners
.. i18n:  * Ecommerce/Partners/Partner Contacts
.. i18n:  * Ecommerce/Products/Product Reviews
.. i18n:  * Ecommerce/Products/Search Parameters
.. i18n:  * Ecommerce/Sales Orders
.. i18n:  * Ecommerce/Sales Orders/Sale order

 * Ecommerce
 * Ecommerce/Configuration
 * Ecommerce/Configuration/Web Shop
 * Ecommerce/Products
 * Ecommerce/Products/Products by Category
 * Ecommerce/Payment Configuration
 * Ecommerce/Payment Configuration/Payment
 * Ecommerce/Configuration/Payment method
 * Ecommerce/Payment Configuration/Payment Received
 * Ecommerce/Payment Configuration/Credit Cards
 * Ecommerce/Partners
 * Ecommerce/Partners/Partners
 * Ecommerce/Partners/Partner Contacts
 * Ecommerce/Products/Product Reviews
 * Ecommerce/Products/Search Parameters
 * Ecommerce/Sales Orders
 * Ecommerce/Sales Orders/Sale order

.. i18n: Views
.. i18n: -----

Views
-----

.. i18n:  * ecommerce.shop.tree (tree)
.. i18n:  * Ecommerce Shop Basic Info (form)
.. i18n:  * ecommerce.product.category.form (form)
.. i18n:  * ecommerce.product.category.tree (tree)
.. i18n:  * ecommerce.payment.tree (tree)
.. i18n:  * ecommerce.payment.form (form)
.. i18n:  * ecommerce.payment.method.tree (tree)
.. i18n:  * ecommerce.payment.method.form (form)
.. i18n:  * ecommerce.payment.received.tree (tree)
.. i18n:  * ecommerce.payment.received.form (form)
.. i18n:  * ecommerce.creditcard.tree (tree)
.. i18n:  * ecommerce.creditcard.form (form)
.. i18n:  * ecommerce.partner.tree (tree)
.. i18n:  * ecommerce.partner.form (form)
.. i18n:  * ecommerce.partner.address.tree (tree)
.. i18n:  * ecommerce.partner.address.form (form)
.. i18n:  * \* INHERIT product.form (form)
.. i18n:  * \* INHERIT ecommerce.pricelist.version (form)
.. i18n:  * ecommerce.reviews.tree (tree)
.. i18n:  * ecommerce.reviews.form (form)
.. i18n:  * ecommerce.search.tree (tree)
.. i18n:  * ecommerce.search.form (form)
.. i18n:  * saleorder.form (form)
.. i18n:  * saleorder.tree (tree)
.. i18n:  * orderline.form (form)
.. i18n:  * orderline.tree (tree)

 * ecommerce.shop.tree (tree)
 * Ecommerce Shop Basic Info (form)
 * ecommerce.product.category.form (form)
 * ecommerce.product.category.tree (tree)
 * ecommerce.payment.tree (tree)
 * ecommerce.payment.form (form)
 * ecommerce.payment.method.tree (tree)
 * ecommerce.payment.method.form (form)
 * ecommerce.payment.received.tree (tree)
 * ecommerce.payment.received.form (form)
 * ecommerce.creditcard.tree (tree)
 * ecommerce.creditcard.form (form)
 * ecommerce.partner.tree (tree)
 * ecommerce.partner.form (form)
 * ecommerce.partner.address.tree (tree)
 * ecommerce.partner.address.form (form)
 * \* INHERIT product.form (form)
 * \* INHERIT ecommerce.pricelist.version (form)
 * ecommerce.reviews.tree (tree)
 * ecommerce.reviews.form (form)
 * ecommerce.search.tree (tree)
 * ecommerce.search.form (form)
 * saleorder.form (form)
 * saleorder.tree (tree)
 * orderline.form (form)
 * orderline.tree (tree)

.. i18n: Objects
.. i18n: -------

Objects
-------

.. i18n: Object: ecommerce partner (ecommerce.partner)
.. i18n: #############################################

Object: ecommerce partner (ecommerce.partner)
#############################################

.. i18n: :lang: Language, selection

:lang: Language, selection

.. i18n: :last_name: Last Name, char, required

:last_name: Last Name, char, required

.. i18n: :name: Name, char, required

:name: Name, char, required

.. i18n: :category_ids: Categories, many2many

:category_ids: Categories, many2many

.. i18n: :company_name: Company Name, char

:company_name: Company Name, char

.. i18n: :address: Contacts, one2many

:address: Contacts, one2many

.. i18n: :active: Active, boolean

:active: Active, boolean

.. i18n: Object: ecommerce partner address (ecommerce.partner.address)
.. i18n: #############################################################

Object: ecommerce partner address (ecommerce.partner.address)
#############################################################

.. i18n: :username: Contact Name, char, required

:username: Contact Name, char, required

.. i18n: :city: City, char

:city: City, char

.. i18n: :fax: Fax, char

:fax: Fax, char

.. i18n: :zip: Zip, char

:zip: Zip, char

.. i18n: :mobile: Mobile, char

:mobile: Mobile, char

.. i18n: :partner_id: Partner, many2one, required

:partner_id: Partner, many2one, required

.. i18n: :street2: Street2, char

:street2: Street2, char

.. i18n: :country_id: Country, many2one

:country_id: Country, many2one

.. i18n: :phone: Phone, char

:phone: Phone, char

.. i18n: :street: Street, char

:street: Street, char

.. i18n: :state_id: State, many2one

:state_id: State, many2one

.. i18n: :type: Address Type, selection

:type: Address Type, selection

.. i18n: :email: E-Mail, char

:email: E-Mail, char

.. i18n: Object: search parameters (ecommerce.search)
.. i18n: ############################################

Object: search parameters (ecommerce.search)
############################################

.. i18n: :code: Search Parameter Code, char

:code: Search Parameter Code, char

.. i18n: :name: Search Parameter Name, char

:name: Search Parameter Name, char

.. i18n: Object: Reviews about product (ecommerce.product.reviews)
.. i18n: #########################################################

Object: Reviews about product (ecommerce.product.reviews)
#########################################################

.. i18n: :rating: Rating, integer

:rating: Rating, integer

.. i18n: :reviewdate: Review Date, date

:reviewdate: Review Date, date

.. i18n: :customer_id: Customer, many2one, required

:customer_id: Customer, many2one, required

.. i18n: :product_id: Product, many2one, required

:product_id: Product, many2one, required

.. i18n: :review: Review, text

:review: Review, text

.. i18n: Object: Credit Cards (ecommerce.creditcard)
.. i18n: ###########################################

Object: Credit Cards (ecommerce.creditcard)
###########################################

.. i18n: :code: Credit Card Code, char

:code: Credit Card Code, char

.. i18n: :name: Credit Card Name, char

:name: Credit Card Name, char

.. i18n: Object: ecommerce payment (ecommerce.payment)
.. i18n: #############################################

Object: ecommerce payment (ecommerce.payment)
#############################################

.. i18n: :biz_account: Your Business E-mail Id, char

:biz_account: Your Business E-mail Id, char

.. i18n:     *Paypal Business Account Id.*

    *Paypal Business Account Id.*

.. i18n: :bank_name: Bank Name, char

:bank_name: Bank Name, char

.. i18n: :chequepay_to: Account Name, char

:chequepay_to: Account Name, char

.. i18n: :name: Method, selection, required

:name: Method, selection, required

.. i18n: :zip: Zip, char

:zip: Zip, char

.. i18n: :city: City, char

:city: City, char

.. i18n: :street2: Street2, char

:street2: Street2, char

.. i18n: :country_id: Country, many2one

:country_id: Country, many2one

.. i18n: :bic: BIC number or SWIFT, char

:bic: BIC number or SWIFT, char

.. i18n: :cancel_url: Cancel URL, char

:cancel_url: Cancel URL, char

.. i18n:     *Cancel url which is set at the paypal account.*

    *Cancel url which is set at the paypal account.*

.. i18n: :street: Street, char

:street: Street, char

.. i18n: :iban: IBAN, char

:iban: IBAN, char

.. i18n:     *for international bank transfers*

    *for international bank transfers*

.. i18n: :return_url: Return URL, char

:return_url: Return URL, char

.. i18n:     *Return url which is set at the paypal account.*

    *Return url which is set at the paypal account.*

.. i18n: :creditcards: Credit Cards, many2many

:creditcards: Credit Cards, many2many

.. i18n: :state_id: State, many2one

:state_id: State, many2one

.. i18n: :transaction_detail: Transaction History, one2many

:transaction_detail: Transaction History, one2many

.. i18n:     *Transaction detail with the uniq transaction id.*

    *Transaction detail with the uniq transaction id.*

.. i18n: :acc_number: Account Number, char

:acc_number: Account Number, char

.. i18n:     *Bank account number*

    *Bank account number*

.. i18n: Object: ecommerce payment received (ecommerce.payment.received)
.. i18n: ###############################################################

Object: ecommerce payment received (ecommerce.payment.received)
###############################################################

.. i18n: :paypal_acc: Paypal Account, many2one, required

:paypal_acc: Paypal Account, many2one, required

.. i18n: :saleorder_id: Sale Order, many2one, required

:saleorder_id: Sale Order, many2one, required

.. i18n: :invoice_id: Invoice, many2one, required

:invoice_id: Invoice, many2one, required

.. i18n: :transaction_date: Date, date, required

:transaction_date: Date, date, required

.. i18n: :partner: Partner, many2one, required

:partner: Partner, many2one, required

.. i18n: :transaction_id: Uniq Transaction Id, char, required

:transaction_id: Uniq Transaction Id, char, required

.. i18n: Object: ecommerce shop (ecommerce.shop)
.. i18n: #######################################

Object: ecommerce shop (ecommerce.shop)
#######################################

.. i18n: :column_configuration: No. of Columns, integer

:column_configuration: No. of Columns, integer

.. i18n:     *Add No. of columns for products which u want to configure at website*

    *Add No. of columns for products which u want to configure at website*

.. i18n: :name: Name, char, required

:name: Name, char, required

.. i18n:     *Name of the Shop which u want to configure for website.*

    *Name of the Shop which u want to configure for website.*

.. i18n: :payment_method: Payable method, many2many

:payment_method: Payable method, many2many

.. i18n: :image_width: Width in Pixel, integer

:image_width: Width in Pixel, integer

.. i18n:     *Add product image width in pixels.*

    *Add product image width in pixels.*

.. i18n: :currency_ids: Currency, many2many

:currency_ids: Currency, many2many

.. i18n:     *Add the currency options for the online customers.*

    *Add the currency options for the online customers.*

.. i18n: :company_id: Company, many2one

:company_id: Company, many2one

.. i18n: :shop_id: Sale Shop, many2one, required

:shop_id: Sale Shop, many2one, required

.. i18n: :language_ids: Language, many2many

:language_ids: Language, many2many

.. i18n:     *Add the Launguage options for the online customers.*

    *Add the Launguage options for the online customers.*

.. i18n: :row_configuration: No. of Row, integer

:row_configuration: No. of Row, integer

.. i18n:     *Add No. of row for products which u want to configure at website*

    *Add No. of row for products which u want to configure at website*

.. i18n: :search_ids: Search On, many2many

:search_ids: Search On, many2many

.. i18n:     *Add the Search Parameters which you are allow from the website.*

    *Add the Search Parameters which you are allow from the website.*

.. i18n: :image_height: Height in Pixel, integer

:image_height: Height in Pixel, integer

.. i18n:     *Add product image height in pixels.*

    *Add product image height in pixels.*

.. i18n: :category_ids: Categories, one2many

:category_ids: Categories, one2many

.. i18n:     *Add the product categories which you want to displayed on the website.*

    *Add the product categories which you want to displayed on the website.*

.. i18n: :delivery_ids: Delivery, many2many

:delivery_ids: Delivery, many2many

.. i18n:     *Add the carriers which we use for the shipping.*

    *Add the carriers which we use for the shipping.*

.. i18n: Object: ecommerce category (ecommerce.category)
.. i18n: ###############################################

Object: ecommerce category (ecommerce.category)
###############################################

.. i18n: :child_id: Child Categories, one2many

:child_id: Child Categories, one2many

.. i18n: :category_id: Tiny Category, many2one

:category_id: Tiny Category, many2one

.. i18n:     *It display the product which are under the tiny category.*

    *It display the product which are under the tiny category.*

.. i18n: :web_id: Webshop, many2one

:web_id: Webshop, many2one

.. i18n: :name: E-commerce Category, char, required

:name: E-commerce Category, char, required

.. i18n:     *Add the Category name which you want to display on the website.*

    *Add the Category name which you want to display on the website.*

.. i18n: :parent_category_id: Parent Category, many2one

:parent_category_id: Parent Category, many2one

.. i18n: Object: ecommerce sale order (ecommerce.saleorder)
.. i18n: ##################################################

Object: ecommerce sale order (ecommerce.saleorder)
##################################################

.. i18n: :note: Notes, text

:note: Notes, text

.. i18n: :web_id: Web Shop, many2one, required

:web_id: Web Shop, many2one, required

.. i18n: :name: Order Description, char, required

:name: Order Description, char, required

.. i18n: :epartner_shipping_id: Shipping Address, many2one

:epartner_shipping_id: Shipping Address, many2one

.. i18n: :order_id: Sale Order, many2one

:order_id: Sale Order, many2one

.. i18n: :epartner_add_id: Contact Address, many2one

:epartner_add_id: Contact Address, many2one

.. i18n: :epartner_id: Ecommerce Partner, many2one, required

:epartner_id: Ecommerce Partner, many2one, required

.. i18n: :pricelist_id: Pricelist, many2one, required

:pricelist_id: Pricelist, many2one, required

.. i18n: :date_order: Date Ordered, date, required

:date_order: Date Ordered, date, required

.. i18n: :epartner_invoice_id: Invoice Address, many2one

:epartner_invoice_id: Invoice Address, many2one

.. i18n: :order_lines: Order Lines, one2many

:order_lines: Order Lines, one2many

.. i18n: Object: ecommerce order line (ecommerce.order.line)
.. i18n: ###################################################

Object: ecommerce order line (ecommerce.order.line)
###################################################

.. i18n: :product_id: Product, many2one

:product_id: Product, many2one

.. i18n: :order_id: eOrder Ref, many2one

:order_id: eOrder Ref, many2one

.. i18n: :product_uom_id: Unit of Measure, many2one, required

:product_uom_id: Unit of Measure, many2one, required

.. i18n: :price_unit: Unit Price, float, required

:price_unit: Unit Price, float, required

.. i18n: :product_qty: Quantity, float, required

:product_qty: Quantity, float, required

.. i18n: :name: Order Line, char, required

:name: Order Line, char, required
