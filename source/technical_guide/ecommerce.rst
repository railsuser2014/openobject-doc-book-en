
E-Commerce (*ecommerce*)
========================
:Module: ecommerce
:Name: E-Commerce
:Version: 5.0.1.0
:Directory: ecommerce
:Web: http://www.etiny.com

Description
-----------

::

  eCommerce Users can order on the website, orders are automatically imported in TinyERP.
                        You can configure products, categories of products, language, currency, carrier, payment
                        and also configure row,column,images.

Dependencies
------------

 * delivery - installed
 * base - installed
 * product - installed
 * sale - installed

Reports
-------

 * Shipping Invoice

Menus
-------

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

Views
-----

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


Objects
-------

Object: ecommerce partner
#########################



:lang: Language, selection





:last_name: Last Name, char, required





:name: Name, char, required





:category_ids: Categories, many2many





:company_name: Company Name, char





:address: Contacts, one2many





:active: Active, boolean




Object: ecommerce partner address
#################################



:username: Contact Name, char, required





:city: City, char





:fax: Fax, char





:zip: Zip, char





:mobile: Mobile, char





:partner_id: Partner, many2one, required





:street2: Street2, char





:country_id: Country, many2one





:phone: Phone, char





:street: Street, char





:state_id: State, many2one





:type: Address Type, selection





:email: E-Mail, char




Object: search parameters
#########################



:code: Search Parameter Code, char





:name: Search Parameter Name, char




Object: Reviews about product
#############################



:rating: Rating, integer





:reviewdate: Review Date, date





:customer_id: Customer, many2one, required





:product_id: Product, many2one, required





:review: Review, text




Object: Credit Cards
####################



:code: Credit Card Code, char





:name: Credit Card Name, char




Object: ecommerce payment
#########################



:biz_account: Your Business E-mail Id, char

    *Paypal Business Account Id.*



:bank_name: Bank Name, char





:chequepay_to: Account Name, char





:name: Method, selection, required





:zip: Zip, char





:city: City, char





:street2: Street2, char





:country_id: Country, many2one





:bic: BIC number or SWIFT, char





:cancel_url: Cancel URL, char

    *Cancel url which is set at the paypal account.*



:street: Street, char





:iban: IBAN, char

    *for international bank transfers*



:return_url: Return URL, char

    *Return url which is set at the paypal account.*



:creditcards: Credit Cards, many2many





:state_id: State, many2one





:transaction_detail: Transaction History, one2many

    *Transaction detail with the uniq transaction id.*



:acc_number: Account Number, char

    *Bank account number*


Object: ecommerce payment received
##################################



:paypal_acc: Paypal Account, many2one, required





:saleorder_id: Sale Order, many2one, required





:invoice_id: Invoice, many2one, required





:transaction_date: Date, date, required





:partner: Partner, many2one, required





:transaction_id: Uniq Transaction Id, char, required




Object: ecommerce shop
######################



:column_configuration: No. of Columns, integer

    *Add No. of columns for products which u want to configure at website*



:name: Name, char, required

    *Name of the Shop which u want to configure for website.*



:payment_method: Payable method, many2many





:image_width: Width in Pixel, integer

    *Add product image width in pixels.*



:currency_ids: Currency, many2many

    *Add the currency options for the online customers.*



:company_id: Company, many2one





:shop_id: Sale Shop, many2one, required





:language_ids: Language, many2many

    *Add the Launguage options for the online customers.*



:row_configuration: No. of Row, integer

    *Add No. of row for products which u want to configure at website*



:search_ids: Search On, many2many

    *Add the Search Parameters which you are allow from the website.*



:image_height: Height in Pixel, integer

    *Add product image height in pixels.*



:category_ids: Categories, one2many

    *Add the product categories which you want to displayed on the website.*



:delivery_ids: Delivery, many2many

    *Add the carriers which we use for the shipping.*


Object: ecommerce category
##########################



:child_id: Child Categories, one2many





:category_id: Tiny Category, many2one

    *It display the product which are under the tiny category.*



:web_id: Webshop, many2one





:name: E-commerce Category, char, required

    *Add the Category name which you want to display on the website.*



:parent_category_id: Parent Category, many2one




Object: ecommerce sale order
############################



:note: Notes, text





:web_id: Web Shop, many2one, required





:name: Order Description, char, required





:epartner_shipping_id: Shipping Address, many2one





:order_id: Sale Order, many2one





:epartner_add_id: Contact Address, many2one





:epartner_id: Ecommerce Partner, many2one, required





:pricelist_id: Pricelist, many2one, required





:date_order: Date Ordered, date, required





:epartner_invoice_id: Invoice Address, many2one





:order_lines: Order Lines, one2many




Object: ecommerce order line
############################



:product_id: Product, many2one





:order_id: eOrder Ref, many2one





:product_uom_id: Unit of Measure, many2one, required





:price_unit: Unit Price, float, required





:product_qty: Quantity, float, required





:name: Order Line, char, required


