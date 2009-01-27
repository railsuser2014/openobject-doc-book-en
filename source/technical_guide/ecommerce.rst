
Module E-Commerce (*ecommerce*)
===============================
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

.. index::
  single: ecommerce partner object
.. 


:lang: Language, selection



.. index::
  single: lang field
.. 




:last_name: Last Name, char, required



.. index::
  single: last_name field
.. 




:name: Name, char, required



.. index::
  single: name field
.. 




:category_ids: Categories, many2many



.. index::
  single: category_ids field
.. 




:company_name: Company Name, char



.. index::
  single: company_name field
.. 




:address: Contacts, one2many



.. index::
  single: address field
.. 




:active: Active, boolean



.. index::
  single: active field
.. 



Object: ecommerce partner address
#################################

.. index::
  single: ecommerce partner address object
.. 


:username: Contact Name, char, required



.. index::
  single: username field
.. 




:city: City, char



.. index::
  single: city field
.. 




:fax: Fax, char



.. index::
  single: fax field
.. 




:zip: Zip, char



.. index::
  single: zip field
.. 




:mobile: Mobile, char



.. index::
  single: mobile field
.. 




:partner_id: Partner, many2one, required



.. index::
  single: partner_id field
.. 




:street2: Street2, char



.. index::
  single: street2 field
.. 




:country_id: Country, many2one



.. index::
  single: country_id field
.. 




:phone: Phone, char



.. index::
  single: phone field
.. 




:street: Street, char



.. index::
  single: street field
.. 




:state_id: State, many2one



.. index::
  single: state_id field
.. 




:type: Address Type, selection



.. index::
  single: type field
.. 




:email: E-Mail, char



.. index::
  single: email field
.. 



Object: search parameters
#########################

.. index::
  single: search parameters object
.. 


:code: Search Parameter Code, char



.. index::
  single: code field
.. 




:name: Search Parameter Name, char



.. index::
  single: name field
.. 



Object: Reviews about product
#############################

.. index::
  single: Reviews about product object
.. 


:rating: Rating, integer



.. index::
  single: rating field
.. 




:reviewdate: Review Date, date



.. index::
  single: reviewdate field
.. 




:customer_id: Customer, many2one, required



.. index::
  single: customer_id field
.. 




:product_id: Product, many2one, required



.. index::
  single: product_id field
.. 




:review: Review, text



.. index::
  single: review field
.. 



Object: Credit Cards
####################

.. index::
  single: Credit Cards object
.. 


:code: Credit Card Code, char



.. index::
  single: code field
.. 




:name: Credit Card Name, char



.. index::
  single: name field
.. 



Object: ecommerce payment
#########################

.. index::
  single: ecommerce payment object
.. 


:biz_account: Your Business E-mail Id, char

    *Paypal Business Account Id.*

.. index::
  single: biz_account field
.. 




:bank_name: Bank Name, char



.. index::
  single: bank_name field
.. 




:chequepay_to: Account Name, char



.. index::
  single: chequepay_to field
.. 




:name: Method, selection, required



.. index::
  single: name field
.. 




:zip: Zip, char



.. index::
  single: zip field
.. 




:city: City, char



.. index::
  single: city field
.. 




:street2: Street2, char



.. index::
  single: street2 field
.. 




:country_id: Country, many2one



.. index::
  single: country_id field
.. 




:bic: BIC number or SWIFT, char



.. index::
  single: bic field
.. 




:cancel_url: Cancel URL, char

    *Cancel url which is set at the paypal account.*

.. index::
  single: cancel_url field
.. 




:street: Street, char



.. index::
  single: street field
.. 




:iban: IBAN, char

    *for international bank transfers*

.. index::
  single: iban field
.. 




:return_url: Return URL, char

    *Return url which is set at the paypal account.*

.. index::
  single: return_url field
.. 




:creditcards: Credit Cards, many2many



.. index::
  single: creditcards field
.. 




:state_id: State, many2one



.. index::
  single: state_id field
.. 




:transaction_detail: Transaction History, one2many

    *Transaction detail with the uniq transaction id.*

.. index::
  single: transaction_detail field
.. 




:acc_number: Account Number, char

    *Bank account number*

.. index::
  single: acc_number field
.. 



Object: ecommerce payment received
##################################

.. index::
  single: ecommerce payment received object
.. 


:paypal_acc: Paypal Account, many2one, required



.. index::
  single: paypal_acc field
.. 




:saleorder_id: Sale Order, many2one, required



.. index::
  single: saleorder_id field
.. 




:invoice_id: Invoice, many2one, required



.. index::
  single: invoice_id field
.. 




:transaction_date: Date, date, required



.. index::
  single: transaction_date field
.. 




:partner: Partner, many2one, required



.. index::
  single: partner field
.. 




:transaction_id: Uniq Transaction Id, char, required



.. index::
  single: transaction_id field
.. 



Object: ecommerce shop
######################

.. index::
  single: ecommerce shop object
.. 


:column_configuration: No. of Columns, integer

    *Add No. of columns for products which u want to configure at website*

.. index::
  single: column_configuration field
.. 




:name: Name, char, required

    *Name of the Shop which u want to configure for website.*

.. index::
  single: name field
.. 




:payment_method: Payable method, many2many



.. index::
  single: payment_method field
.. 




:image_width: Width in Pixel, integer

    *Add product image width in pixels.*

.. index::
  single: image_width field
.. 




:currency_ids: Currency, many2many

    *Add the currency options for the online customers.*

.. index::
  single: currency_ids field
.. 




:company_id: Company, many2one



.. index::
  single: company_id field
.. 




:shop_id: Sale Shop, many2one, required



.. index::
  single: shop_id field
.. 




:language_ids: Language, many2many

    *Add the Launguage options for the online customers.*

.. index::
  single: language_ids field
.. 




:row_configuration: No. of Row, integer

    *Add No. of row for products which u want to configure at website*

.. index::
  single: row_configuration field
.. 




:search_ids: Search On, many2many

    *Add the Search Parameters which you are allow from the website.*

.. index::
  single: search_ids field
.. 




:image_height: Height in Pixel, integer

    *Add product image height in pixels.*

.. index::
  single: image_height field
.. 




:category_ids: Categories, one2many

    *Add the product categories which you want to displayed on the website.*

.. index::
  single: category_ids field
.. 




:delivery_ids: Delivery, many2many

    *Add the carriers which we use for the shipping.*

.. index::
  single: delivery_ids field
.. 



Object: ecommerce category
##########################

.. index::
  single: ecommerce category object
.. 


:child_id: Child Categories, one2many



.. index::
  single: child_id field
.. 




:category_id: Tiny Category, many2one

    *It display the product which are under the tiny category.*

.. index::
  single: category_id field
.. 




:web_id: Webshop, many2one



.. index::
  single: web_id field
.. 




:name: E-commerce Category, char, required

    *Add the Category name which you want to display on the website.*

.. index::
  single: name field
.. 




:parent_category_id: Parent Category, many2one



.. index::
  single: parent_category_id field
.. 



Object: ecommerce sale order
############################

.. index::
  single: ecommerce sale order object
.. 


:note: Notes, text



.. index::
  single: note field
.. 




:web_id: Web Shop, many2one, required



.. index::
  single: web_id field
.. 




:name: Order Description, char, required



.. index::
  single: name field
.. 




:epartner_shipping_id: Shipping Address, many2one



.. index::
  single: epartner_shipping_id field
.. 




:order_id: Sale Order, many2one



.. index::
  single: order_id field
.. 




:epartner_add_id: Contact Address, many2one



.. index::
  single: epartner_add_id field
.. 




:epartner_id: Ecommerce Partner, many2one, required



.. index::
  single: epartner_id field
.. 




:pricelist_id: Pricelist, many2one, required



.. index::
  single: pricelist_id field
.. 




:date_order: Date Ordered, date, required



.. index::
  single: date_order field
.. 




:epartner_invoice_id: Invoice Address, many2one



.. index::
  single: epartner_invoice_id field
.. 




:order_lines: Order Lines, one2many



.. index::
  single: order_lines field
.. 



Object: ecommerce order line
############################

.. index::
  single: ecommerce order line object
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

