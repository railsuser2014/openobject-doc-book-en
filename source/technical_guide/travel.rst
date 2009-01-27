
Module Travel (*travel*)
========================
:Module: travel
:Name: Travel
:Version: 5.0.1.0
:Directory: travel
:Web: 

Description
-----------

::

  None

Dependencies
------------

 * base - installed
 * product - installed

Reports
-------

None


Menus
-------

 * Travel Agency
 * Travel Agency/Hostels
 * Travel Agency/Rooms
 * Travel Agency/Rooms/Single Rooms
 * Travel Agency/Rooms/Double Rooms
 * Travel Agency/Airports
 * Travel Agency/Flights

Views
-----

 * travel.flight (form)
 * travel.room (form)
 * travel.room (tree)
 * travel.hostel (form)


Objects
-------

Object: Partner
###############

.. index::
  single: Partner object
.. 


:comment: Notes, text



.. index::
  single: comment field
.. 




:ean13: EAN13, char



.. index::
  single: ean13 field
.. 




:property_account_position: Fiscal Position, many2one

    *The fiscal position will determine taxes and the accounts used for the the partner.*

.. index::
  single: property_account_position field
.. 




:ref_companies: Companies that refers to partner, one2many



.. index::
  single: ref_companies field
.. 




:relation_ids: Relations, one2many



.. index::
  single: relation_ids field
.. 




:rooms_id: Rooms, one2many



.. index::
  single: rooms_id field
.. 




:date: Date, date



.. index::
  single: date field
.. 




:logo: Logo, binary



.. index::
  single: logo field
.. 




:property_product_pricelist: Sale Pricelist, many2one

    *This pricelist will be used, instead of the default one,                     for sales to the current partner*

.. index::
  single: property_product_pricelist field
.. 




:quality: Quality, char



.. index::
  single: quality field
.. 




:city: City, char



.. index::
  single: city field
.. 




:user_id: Dedicated Salesman, many2one

    *The internal user that is in charge of communicating with this partner if any.*

.. index::
  single: user_id field
.. 




:title: Title, selection



.. index::
  single: title field
.. 




:property_account_payable: Account Payable, many2one, required

    *This account will be used, instead of the default one, as the payable account for the current partner*

.. index::
  single: property_account_payable field
.. 




:parent_id: Main Company, many2one



.. index::
  single: parent_id field
.. 




:debit: Total Payable, float, readonly

    *Total amount you have to pay to this supplier.*

.. index::
  single: debit field
.. 




:supplier: Supplier, boolean

    *Check this box if the partner is a supplier. If it's not checked, purchase people will not see it when encoding a purchase order.*

.. index::
  single: supplier field
.. 




:ref: Code, char, readonly



.. index::
  single: ref field
.. 




:events: Events, one2many



.. index::
  single: events field
.. 




:vat: VAT, char

    *Value Added Tax number. Check the box if the partner is subjected to the VAT. Used by the VAT legal statement.*

.. index::
  single: vat field
.. 




:website: Website, char



.. index::
  single: website field
.. 




:customer: Customer, boolean

    *Check this box if the partner is a customer.*

.. index::
  single: customer field
.. 




:bank_ids: Banks, one2many



.. index::
  single: bank_ids field
.. 




:child_ids: Partner Ref., one2many



.. index::
  single: child_ids field
.. 




:address: Contacts, one2many



.. index::
  single: address field
.. 




:active: Active, boolean



.. index::
  single: active field
.. 




:answers_ids: Answers, many2many



.. index::
  single: answers_ids field
.. 




:category_id: Categories, many2many



.. index::
  single: category_id field
.. 




:lang: Language, selection

    *If the selected language is loaded in the system, all documents related to this partner will be printed in this language. If not, it will be english.*

.. index::
  single: lang field
.. 




:credit_limit: Credit Limit, float



.. index::
  single: credit_limit field
.. 




:name: Name, char, required



.. index::
  single: name field
.. 




:header: Header (.odt), binary



.. index::
  single: header field
.. 




:debit_limit: Payable Limit, float



.. index::
  single: debit_limit field
.. 




:property_account_receivable: Account Receivable, many2one, required

    *This account will be used, instead of the default one, as the receivable account for the current partner*

.. index::
  single: property_account_receivable field
.. 




:credit: Total Receivable, float, readonly

    *Total amount this customer owns you.*

.. index::
  single: credit field
.. 




:signature: Signature, binary



.. index::
  single: signature field
.. 




:property_payment_term: Payment Term, many2one

    *This payment term will be used, instead of the default one, for the current partner*

.. index::
  single: property_payment_term field
.. 




:country: Country, many2one



.. index::
  single: country field
.. 



Object: travel.airport
######################

.. index::
  single: travel.airport object
.. 


:city: City, char



.. index::
  single: city field
.. 




:name: Airport name, char



.. index::
  single: name field
.. 




:country: Country, many2one



.. index::
  single: country field
.. 



Object: Product
###############

.. index::
  single: Product object
.. 


:warranty: Warranty (months), float



.. index::
  single: warranty field
.. 




:property_stock_procurement: Procurement Location, many2one

    *For the current product (template), this stock location will be used, instead of the default one, as the source location for stock moves generated by procurements*

.. index::
  single: property_stock_procurement field
.. 




:supply_method: Supply method, selection, required

    *Produce will generate production order or tasks, according to the product type. Purchase will trigger purchase orders when requested.*

.. index::
  single: supply_method field
.. 




:uos_id: Unit of Sale, many2one

    *Used by companies that manages two unit of measure: invoicing and stock management. For example, in food industries, you will manage a stock of ham but invoice in Kg. Keep empty to use the default UOM.*

.. index::
  single: uos_id field
.. 




:list_price: Sale Price, float

    *Base price for computing the customer price. Sometimes called the catalog price.*

.. index::
  single: list_price field
.. 




:weight: Gross weight, float

    *The gross weight in Kg.*

.. index::
  single: weight field
.. 




:ean13: EAN UPC JPC GTIN, char



.. index::
  single: ean13 field
.. 




:incoming_qty: Incoming, float, readonly



.. index::
  single: incoming_qty field
.. 




:standard_price: Cost Price, float, required

    *The cost of the product for accounting stock valorisation. It can serves as a base price for supplier price.*

.. index::
  single: standard_price field
.. 




:member_price: Member Price, float



.. index::
  single: member_price field
.. 




:price_extra: Variant Price Extra, float



.. index::
  single: price_extra field
.. 




:mes_type: Measure Type, selection, required



.. index::
  single: mes_type field
.. 




:uom_id: Default UoM, many2one, required

    *Default Unit of Measure used for all stock operation.*

.. index::
  single: uom_id field
.. 




:hostel_id: Hostel, many2one



.. index::
  single: hostel_id field
.. 




:code: Code, char, readonly



.. index::
  single: code field
.. 




:description_purchase: Purchase Description, text



.. index::
  single: description_purchase field
.. 




:default_code: Code, char



.. index::
  single: default_code field
.. 




:property_account_income: Income Account, many2one

    *This account will be used, instead of the default one, to value incoming stock for the current product*

.. index::
  single: property_account_income field
.. 




:qty_available: Real Stock, float, readonly



.. index::
  single: qty_available field
.. 




:price: Customer Price, float, readonly



.. index::
  single: price field
.. 




:index_sale: Sales indexes, many2many



.. index::
  single: index_sale field
.. 




:variants: Variants, char



.. index::
  single: variants field
.. 




:property_account_expense_world1: Outside Europe Expense Account, many2one

    *This account will be used, instead of the default one, to value outgoing stock for the current product*

.. index::
  single: property_account_expense_world1 field
.. 




:uos_coeff: UOM -> UOS Coeff, float

    *Coefficient to convert UOM to UOS
    uom = uos * coeff*

.. index::
  single: uos_coeff field
.. 




:product_tmpl_id: Product Template, many2one, required



.. index::
  single: product_tmpl_id field
.. 




:virtual_available: Virtual Stock, float, readonly



.. index::
  single: virtual_available field
.. 




:sale_ok: Can be sold, boolean

    *Determine if the product can be visible in the list of product within a selection from a sale order line.*

.. index::
  single: sale_ok field
.. 




:buyer_price_index: Indexed buyer price, float, readonly



.. index::
  single: buyer_price_index field
.. 




:auto_picking: Auto Picking for Production, boolean



.. index::
  single: auto_picking field
.. 




:product_manager: Product Manager, many2one



.. index::
  single: product_manager field
.. 




:property_stock_account_output: Stock Output Account, many2one

    *This account will be used, instead of the default one, to value output stock*

.. index::
  single: property_stock_account_output field
.. 




:company_id: Company, many2one



.. index::
  single: company_id field
.. 




:name: Name, char, required



.. index::
  single: name field
.. 




:active: Active, boolean



.. index::
  single: active field
.. 




:produce_delay: Manufacturing Lead Time, float

    *Average time to produce this product. This is only for the production order and, if it is a multi-level bill of material, it's only for the level of this product. Different delays will be summed for all levels and purchase orders.*

.. index::
  single: produce_delay field
.. 




:state: Status, selection

    *Tells the user if he can use the product or not.*

.. index::
  single: state field
.. 




:property_account_income_world: Outside Europe Income Account, many2one

    *This account will be used, instead of the default one, to value incoming stock for the current product*

.. index::
  single: property_account_income_world field
.. 




:loc_rack: Rack, char



.. index::
  single: loc_rack field
.. 




:view: Room View, selection



.. index::
  single: view field
.. 




:uom_po_id: Purchase UoM, many2one, required

    *Default Unit of Measure used for purchase orders. It must in the same category than the default unit of measure.*

.. index::
  single: uom_po_id field
.. 




:intrastat_id: Intrastat code, many2one



.. index::
  single: intrastat_id field
.. 




:type: Product Type, selection, required

    *Will change the way procurements are processed, consumable are stockable products with infinite stock, or without a stock management in the system.*

.. index::
  single: type field
.. 




:property_stock_account_input: Stock Input Account, many2one

    *This account will be used, instead of the default one, to value input stock*

.. index::
  single: property_stock_account_input field
.. 




:property_account_income_europe: Income Account for Europe, many2one

    *This account will be used, instead of the default one, to value incoming stock for the current product*

.. index::
  single: property_account_income_europe field
.. 




:standard_price_index: Indexed standard price, float, readonly



.. index::
  single: standard_price_index field
.. 




:description: Description, text



.. index::
  single: description field
.. 




:list_price_index: Indexed list price, float, readonly



.. index::
  single: list_price_index field
.. 




:property_account_expense_europe: Expense Account for Europe, many2one

    *This account will be used, instead of the default one, to value outgoing stock for the current product*

.. index::
  single: property_account_expense_europe field
.. 




:weight_net: Net weight, float

    *The net weight in Kg.*

.. index::
  single: weight_net field
.. 




:property_stock_production: Production Location, many2one

    *For the current product (template), this stock location will be used, instead of the default one, as the source location for stock moves generated by production orders*

.. index::
  single: property_stock_production field
.. 




:index_date: Index price date, date, required



.. index::
  single: index_date field
.. 




:partner_ref2: Customer ref, char, readonly



.. index::
  single: partner_ref2 field
.. 




:supplier_taxes_id: Supplier Taxes, many2many



.. index::
  single: supplier_taxes_id field
.. 




:volume: Volume, float

    *The volume in m3.*

.. index::
  single: volume field
.. 




:seller_ids: Partners, one2many



.. index::
  single: seller_ids field
.. 




:cutting: Can be Cutted, boolean



.. index::
  single: cutting field
.. 




:procure_method: Procure Method, selection, required

    *'Make to Stock': When needed, take from the stock or wait until refurnishing. 'Make to Order': When needed, purchase or produce for the procurement request.*

.. index::
  single: procure_method field
.. 




:property_stock_inventory: Inventory Location, many2one

    *For the current product (template), this stock location will be used, instead of the default one, as the source location for stock moves generated when you do an inventory*

.. index::
  single: property_stock_inventory field
.. 




:cost_method: Costing Method, selection, required

    *Standard Price: the cost price is fixed and recomputed periodically (usually at the end of the year), Average Price: the cost price is recomputed at each reception of products.*

.. index::
  single: cost_method field
.. 




:partner_ref: Customer ref, char, readonly



.. index::
  single: partner_ref field
.. 




:loc_row: Row, char



.. index::
  single: loc_row field
.. 




:seller_delay: Supplier Lead Time, integer, readonly

    *This is the average delay in days between the purchase order confirmation and the reception of goods for this product and for the default supplier. It is used by the scheduler to order requests based on reordering delays.*

.. index::
  single: seller_delay field
.. 




:rental: Rentable product, boolean



.. index::
  single: rental field
.. 




:packaging: Logistical Units, one2many

    *Gives the different ways to package the same product. This has no impact on the packing order and is mainly used if you use the EDI module.*

.. index::
  single: packaging field
.. 




:sale_delay: Customer Lead Time, float

    *This is the average time between the confirmation of the customer order and the delivery of the finnished products. It's the time you promise to your customers.*

.. index::
  single: sale_delay field
.. 




:index_purchase: Purchase indexes, many2many



.. index::
  single: index_purchase field
.. 




:loc_case: Case, char



.. index::
  single: loc_case field
.. 




:description_sale: Sale Description, text



.. index::
  single: description_sale field
.. 




:property_account_expense: Expense Account, many2one

    *This account will be used, instead of the default one, to value outgoing stock for the current product*

.. index::
  single: property_account_expense field
.. 




:categ_id: Category, many2one, required



.. index::
  single: categ_id field
.. 




:beds: Nbr of Beds, integer



.. index::
  single: beds field
.. 




:lst_price: List Price, float, readonly



.. index::
  single: lst_price field
.. 




:outgoing_qty: Outgoing, float, readonly



.. index::
  single: outgoing_qty field
.. 




:taxes_id: Product Taxes, many2many



.. index::
  single: taxes_id field
.. 




:purchase_ok: Can be Purchased, boolean

    *Determine if the product is visible in the list of products within a selection from a purchase order line.*

.. index::
  single: purchase_ok field
.. 




:y: Y of Product, float



.. index::
  single: y field
.. 




:x: X of Product, float



.. index::
  single: x field
.. 




:z: Z of Product, float



.. index::
  single: z field
.. 




:buyer_price: Buyer price, float



.. index::
  single: buyer_price field
.. 




:dimension_ids: Dimensions, many2many



.. index::
  single: dimension_ids field
.. 




:price_margin: Variant Price Margin, float



.. index::
  single: price_margin field
.. 



Object: Product
###############

.. index::
  single: Product object
.. 


:warranty: Warranty (months), float



.. index::
  single: warranty field
.. 




:property_stock_procurement: Procurement Location, many2one

    *For the current product (template), this stock location will be used, instead of the default one, as the source location for stock moves generated by procurements*

.. index::
  single: property_stock_procurement field
.. 




:supply_method: Supply method, selection, required

    *Produce will generate production order or tasks, according to the product type. Purchase will trigger purchase orders when requested.*

.. index::
  single: supply_method field
.. 




:uos_id: Unit of Sale, many2one

    *Used by companies that manages two unit of measure: invoicing and stock management. For example, in food industries, you will manage a stock of ham but invoice in Kg. Keep empty to use the default UOM.*

.. index::
  single: uos_id field
.. 




:list_price: Sale Price, float

    *Base price for computing the customer price. Sometimes called the catalog price.*

.. index::
  single: list_price field
.. 




:weight: Gross weight, float

    *The gross weight in Kg.*

.. index::
  single: weight field
.. 




:ean13: EAN UPC JPC GTIN, char



.. index::
  single: ean13 field
.. 




:incoming_qty: Incoming, float, readonly



.. index::
  single: incoming_qty field
.. 




:airport_from: Airport Departure, many2one



.. index::
  single: airport_from field
.. 




:standard_price: Cost Price, float, required

    *The cost of the product for accounting stock valorisation. It can serves as a base price for supplier price.*

.. index::
  single: standard_price field
.. 




:member_price: Member Price, float



.. index::
  single: member_price field
.. 




:price_extra: Variant Price Extra, float



.. index::
  single: price_extra field
.. 




:mes_type: Measure Type, selection, required



.. index::
  single: mes_type field
.. 




:uom_id: Default UoM, many2one, required

    *Default Unit of Measure used for all stock operation.*

.. index::
  single: uom_id field
.. 




:code: Code, char, readonly



.. index::
  single: code field
.. 




:description_purchase: Purchase Description, text



.. index::
  single: description_purchase field
.. 




:default_code: Code, char



.. index::
  single: default_code field
.. 




:property_account_income: Income Account, many2one

    *This account will be used, instead of the default one, to value incoming stock for the current product*

.. index::
  single: property_account_income field
.. 




:qty_available: Real Stock, float, readonly



.. index::
  single: qty_available field
.. 




:price: Customer Price, float, readonly



.. index::
  single: price field
.. 




:partner_id: PArtner, many2one



.. index::
  single: partner_id field
.. 




:variants: Variants, char



.. index::
  single: variants field
.. 




:property_account_expense_world1: Outside Europe Expense Account, many2one

    *This account will be used, instead of the default one, to value outgoing stock for the current product*

.. index::
  single: property_account_expense_world1 field
.. 




:uos_coeff: UOM -> UOS Coeff, float

    *Coefficient to convert UOM to UOS
    uom = uos * coeff*

.. index::
  single: uos_coeff field
.. 




:product_tmpl_id: Product Template, many2one, required



.. index::
  single: product_tmpl_id field
.. 




:date: Departure Date, datetime



.. index::
  single: date field
.. 




:sale_ok: Can be sold, boolean

    *Determine if the product can be visible in the list of product within a selection from a sale order line.*

.. index::
  single: sale_ok field
.. 




:buyer_price_index: Indexed buyer price, float, readonly



.. index::
  single: buyer_price_index field
.. 




:auto_picking: Auto Picking for Production, boolean



.. index::
  single: auto_picking field
.. 




:product_manager: Product Manager, many2one



.. index::
  single: product_manager field
.. 




:property_stock_account_output: Stock Output Account, many2one

    *This account will be used, instead of the default one, to value output stock*

.. index::
  single: property_stock_account_output field
.. 




:company_id: Company, many2one



.. index::
  single: company_id field
.. 




:name: Name, char, required



.. index::
  single: name field
.. 




:active: Active, boolean



.. index::
  single: active field
.. 




:produce_delay: Manufacturing Lead Time, float

    *Average time to produce this product. This is only for the production order and, if it is a multi-level bill of material, it's only for the level of this product. Different delays will be summed for all levels and purchase orders.*

.. index::
  single: produce_delay field
.. 




:state: Status, selection

    *Tells the user if he can use the product or not.*

.. index::
  single: state field
.. 




:property_account_income_world: Outside Europe Income Account, many2one

    *This account will be used, instead of the default one, to value incoming stock for the current product*

.. index::
  single: property_account_income_world field
.. 




:loc_rack: Rack, char



.. index::
  single: loc_rack field
.. 




:uom_po_id: Purchase UoM, many2one, required

    *Default Unit of Measure used for purchase orders. It must in the same category than the default unit of measure.*

.. index::
  single: uom_po_id field
.. 




:intrastat_id: Intrastat code, many2one



.. index::
  single: intrastat_id field
.. 




:type: Product Type, selection, required

    *Will change the way procurements are processed, consumable are stockable products with infinite stock, or without a stock management in the system.*

.. index::
  single: type field
.. 




:property_stock_account_input: Stock Input Account, many2one

    *This account will be used, instead of the default one, to value input stock*

.. index::
  single: property_stock_account_input field
.. 




:property_account_income_europe: Income Account for Europe, many2one

    *This account will be used, instead of the default one, to value incoming stock for the current product*

.. index::
  single: property_account_income_europe field
.. 




:standard_price_index: Indexed standard price, float, readonly



.. index::
  single: standard_price_index field
.. 




:virtual_available: Virtual Stock, float, readonly



.. index::
  single: virtual_available field
.. 




:description: Description, text



.. index::
  single: description field
.. 




:list_price_index: Indexed list price, float, readonly



.. index::
  single: list_price_index field
.. 




:property_account_expense_europe: Expense Account for Europe, many2one

    *This account will be used, instead of the default one, to value outgoing stock for the current product*

.. index::
  single: property_account_expense_europe field
.. 




:weight_net: Net weight, float

    *The net weight in Kg.*

.. index::
  single: weight_net field
.. 




:property_stock_production: Production Location, many2one

    *For the current product (template), this stock location will be used, instead of the default one, as the source location for stock moves generated by production orders*

.. index::
  single: property_stock_production field
.. 




:index_date: Index price date, date, required



.. index::
  single: index_date field
.. 




:partner_ref2: Customer ref, char, readonly



.. index::
  single: partner_ref2 field
.. 




:supplier_taxes_id: Supplier Taxes, many2many



.. index::
  single: supplier_taxes_id field
.. 




:volume: Volume, float

    *The volume in m3.*

.. index::
  single: volume field
.. 




:seller_ids: Partners, one2many



.. index::
  single: seller_ids field
.. 




:cutting: Can be Cutted, boolean



.. index::
  single: cutting field
.. 




:airport_to: Airport Arrival, many2one



.. index::
  single: airport_to field
.. 




:procure_method: Procure Method, selection, required

    *'Make to Stock': When needed, take from the stock or wait until refurnishing. 'Make to Order': When needed, purchase or produce for the procurement request.*

.. index::
  single: procure_method field
.. 




:property_stock_inventory: Inventory Location, many2one

    *For the current product (template), this stock location will be used, instead of the default one, as the source location for stock moves generated when you do an inventory*

.. index::
  single: property_stock_inventory field
.. 




:cost_method: Costing Method, selection, required

    *Standard Price: the cost price is fixed and recomputed periodically (usually at the end of the year), Average Price: the cost price is recomputed at each reception of products.*

.. index::
  single: cost_method field
.. 




:partner_ref: Customer ref, char, readonly



.. index::
  single: partner_ref field
.. 




:loc_row: Row, char



.. index::
  single: loc_row field
.. 




:seller_delay: Supplier Lead Time, integer, readonly

    *This is the average delay in days between the purchase order confirmation and the reception of goods for this product and for the default supplier. It is used by the scheduler to order requests based on reordering delays.*

.. index::
  single: seller_delay field
.. 




:rental: Rentable product, boolean



.. index::
  single: rental field
.. 




:packaging: Logistical Units, one2many

    *Gives the different ways to package the same product. This has no impact on the packing order and is mainly used if you use the EDI module.*

.. index::
  single: packaging field
.. 




:sale_delay: Customer Lead Time, float

    *This is the average time between the confirmation of the customer order and the delivery of the finnished products. It's the time you promise to your customers.*

.. index::
  single: sale_delay field
.. 




:index_purchase: Purchase indexes, many2many



.. index::
  single: index_purchase field
.. 




:loc_case: Case, char



.. index::
  single: loc_case field
.. 




:description_sale: Sale Description, text



.. index::
  single: description_sale field
.. 




:property_account_expense: Expense Account, many2one

    *This account will be used, instead of the default one, to value outgoing stock for the current product*

.. index::
  single: property_account_expense field
.. 




:buyer_price: Buyer price, float



.. index::
  single: buyer_price field
.. 




:categ_id: Category, many2one, required



.. index::
  single: categ_id field
.. 




:lst_price: List Price, float, readonly



.. index::
  single: lst_price field
.. 




:outgoing_qty: Outgoing, float, readonly



.. index::
  single: outgoing_qty field
.. 




:taxes_id: Product Taxes, many2many



.. index::
  single: taxes_id field
.. 




:purchase_ok: Can be Purchased, boolean

    *Determine if the product is visible in the list of products within a selection from a purchase order line.*

.. index::
  single: purchase_ok field
.. 




:y: Y of Product, float



.. index::
  single: y field
.. 




:x: X of Product, float



.. index::
  single: x field
.. 




:z: Z of Product, float



.. index::
  single: z field
.. 




:index_sale: Sales indexes, many2many



.. index::
  single: index_sale field
.. 




:dimension_ids: Dimensions, many2many



.. index::
  single: dimension_ids field
.. 




:price_margin: Variant Price Margin, float



.. index::
  single: price_margin field
.. 

