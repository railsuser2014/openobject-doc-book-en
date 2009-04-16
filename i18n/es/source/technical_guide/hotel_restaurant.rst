
.. i18n: .. module:: hotel_restaurant
.. i18n:     :synopsis: Hotel Restaurant 
.. i18n:     :noindex:
.. i18n: .. 

.. module:: hotel_restaurant
    :synopsis: Hotel Restaurant 
    :noindex:
.. 

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. i18n: Hotel Restaurant (*hotel_restaurant*)
.. i18n: =====================================
.. i18n: :Module: hotel_restaurant
.. i18n: :Name: Hotel Restaurant
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: hotel_restaurant
.. i18n: :Web: 
.. i18n: :Official module: no
.. i18n: :Quality certified: no

Hotel Restaurant (*hotel_restaurant*)
=====================================
:Module: hotel_restaurant
:Name: Hotel Restaurant
:Version: 5.0.1.0
:Author: Tiny
:Directory: hotel_restaurant
:Web: 
:Official module: no
:Quality certified: no

.. i18n: Description
.. i18n: -----------

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   Module for Hotel/Resort/Restaurant management. You can manage:
.. i18n:       * Configure Property
.. i18n:       * Restaurant Configuration
.. i18n:       * table reservation
.. i18n:       * Generate and process Kitchen Order ticket,
.. i18n:       * Payment
.. i18n:   
.. i18n:       Different reports are also provided, mainly for Restaurant.

::

  Module for Hotel/Resort/Restaurant management. You can manage:
      * Configure Property
      * Restaurant Configuration
      * table reservation
      * Generate and process Kitchen Order ticket,
      * Payment
  
      Different reports are also provided, mainly for Restaurant.

.. i18n: Dependencies
.. i18n: ------------

Dependencies
------------

.. i18n:  * :mod:`base`
.. i18n:  * :mod:`hotel`

 * :mod:`base`
 * :mod:`hotel`

.. i18n: Reports
.. i18n: -------

Reports
-------

.. i18n:  * Kitchen Order Tickets
.. i18n: 
.. i18n:  * Customer Bill
.. i18n: 
.. i18n:  * Table Reservation List

 * Kitchen Order Tickets

 * Customer Bill

 * Table Reservation List

.. i18n: Menus
.. i18n: -------

Menus
-------

.. i18n:  * Hotel Restaurant
.. i18n:  * Hotel Restaurant/Configuration
.. i18n:  * Hotel Restaurant/Configuration/Tables
.. i18n:  * Hotel Restaurant/Reservation
.. i18n:  * Hotel Restaurant/Reservation/Table Booking
.. i18n:  * Hotel Restaurant/Reservation/Orders
.. i18n:  * Hotel Restaurant/Table Order
.. i18n:  * Hotel Restaurant/KOT
.. i18n:  * Hotel Restaurant/Configuration/FoodItem Types
.. i18n:  * Hotel Restaurant/Configuration/Menucard
.. i18n:  * Hotel Restaurant/Reservation List

 * Hotel Restaurant
 * Hotel Restaurant/Configuration
 * Hotel Restaurant/Configuration/Tables
 * Hotel Restaurant/Reservation
 * Hotel Restaurant/Reservation/Table Booking
 * Hotel Restaurant/Reservation/Orders
 * Hotel Restaurant/Table Order
 * Hotel Restaurant/KOT
 * Hotel Restaurant/Configuration/FoodItem Types
 * Hotel Restaurant/Configuration/Menucard
 * Hotel Restaurant/Reservation List

.. i18n: Views
.. i18n: -----

Views
-----

.. i18n:  * hotel_restaurant_tables.form (form)
.. i18n:  * hotel_restaurant_tables.tree (tree)
.. i18n:  * hotel_restaurant_reservation.form (form)
.. i18n:  * hotel_restaurant_reservation.tree (tree)
.. i18n:  * hotel_reservation_order.form (form)
.. i18n:  * hotel_reservation_order.tree (tree)
.. i18n:  * hotel_restaurant_order.form (form)
.. i18n:  * hotel_restaurant_order.tree (tree)
.. i18n:  * hotel_restaurant_kitchen_order_tickets.form (form)
.. i18n:  * hotel_restaurant_kitchen_order_tickets.tree (tree)
.. i18n:  * hotel_menucard_type_form (form)
.. i18n:  * hotel_menucard_type_list (tree)
.. i18n:  * hotel.menucard.form (form)
.. i18n:  * hotel.menucard.tree (tree)

 * hotel_restaurant_tables.form (form)
 * hotel_restaurant_tables.tree (tree)
 * hotel_restaurant_reservation.form (form)
 * hotel_restaurant_reservation.tree (tree)
 * hotel_reservation_order.form (form)
 * hotel_reservation_order.tree (tree)
 * hotel_restaurant_order.form (form)
 * hotel_restaurant_order.tree (tree)
 * hotel_restaurant_kitchen_order_tickets.form (form)
 * hotel_restaurant_kitchen_order_tickets.tree (tree)
 * hotel_menucard_type_form (form)
 * hotel_menucard_type_list (tree)
 * hotel.menucard.form (form)
 * hotel.menucard.tree (tree)

.. i18n: Objects
.. i18n: -------

Objects
-------

.. i18n: Object: amenities Type (hotel.menucard.type)
.. i18n: ############################################

Object: amenities Type (hotel.menucard.type)
############################################

.. i18n: :menu_id: category, many2one, required

:menu_id: category, many2one, required

.. i18n: :property_account_expense_categ: Expense Account, many2one

:property_account_expense_categ: Expense Account, many2one

.. i18n:     *This account will be used, instead of the default one, to value outgoing stock for the current product category*

    *This account will be used, instead of the default one, to value outgoing stock for the current product category*

.. i18n: :property_stock_journal: Stock journal, many2one

:property_stock_journal: Stock journal, many2one

.. i18n:     *This journal will be used for the accounting move generated by stock move*

    *This journal will be used for the accounting move generated by stock move*

.. i18n: :sequence: Sequence, integer

:sequence: Sequence, integer

.. i18n: :property_account_expense_europe: Expense Account for Europe, many2one

:property_account_expense_europe: Expense Account for Europe, many2one

.. i18n:     *This account will be used, instead of the default one, to value outgoing stock for the current product*

    *This account will be used, instead of the default one, to value outgoing stock for the current product*

.. i18n: :property_stock_account_input_categ: Stock Input Account, many2one

:property_stock_account_input_categ: Stock Input Account, many2one

.. i18n:     *This account will be used to value the input stock*

    *This account will be used to value the input stock*

.. i18n: :property_account_income_categ: Income Account, many2one

:property_account_income_categ: Income Account, many2one

.. i18n:     *This account will be used, instead of the default one, to value incoming stock for the current product category*

    *This account will be used, instead of the default one, to value incoming stock for the current product category*

.. i18n: :child_id: Childs Categories, one2many

:child_id: Childs Categories, one2many

.. i18n: :property_stock_account_output_categ: Stock Output Account, many2one

:property_stock_account_output_categ: Stock Output Account, many2one

.. i18n:     *This account will be used to value the output stock*

    *This account will be used to value the output stock*

.. i18n: :name: Name, char, required

:name: Name, char, required

.. i18n: :isactivitytype: Is Activity Type, boolean

:isactivitytype: Is Activity Type, boolean

.. i18n: :isroomtype: Is Room Type, boolean

:isroomtype: Is Room Type, boolean

.. i18n: :property_account_expense_world: Outside Europe Expense Account, many2one

:property_account_expense_world: Outside Europe Expense Account, many2one

.. i18n:     *This account will be used, instead of the default one, to value outgoing stock for the current product*

    *This account will be used, instead of the default one, to value outgoing stock for the current product*

.. i18n: :ismenutype: Is Menu Type, boolean

:ismenutype: Is Menu Type, boolean

.. i18n: :isservicetype: Is Service Type, boolean

:isservicetype: Is Service Type, boolean

.. i18n: :parent_id: Parent Category, many2one

:parent_id: Parent Category, many2one

.. i18n: :property_account_income_world: Outside Europe Income Account, many2one

:property_account_income_world: Outside Europe Income Account, many2one

.. i18n:     *This account will be used, instead of the default one, to value incoming stock for the current product*

    *This account will be used, instead of the default one, to value incoming stock for the current product*

.. i18n: :complete_name: Name, char, readonly

:complete_name: Name, char, readonly

.. i18n: :isamenitype: Is amenities Type, boolean

:isamenitype: Is amenities Type, boolean

.. i18n: :property_account_income_europe: Income Account for Europe, many2one

:property_account_income_europe: Income Account for Europe, many2one

.. i18n:     *This account will be used, instead of the default one, to value incoming stock for the current product*

    *This account will be used, instead of the default one, to value incoming stock for the current product*

.. i18n: Object: Hotel Menucard (hotel.menucard)
.. i18n: #######################################

Object: Hotel Menucard (hotel.menucard)
#######################################

.. i18n: :ean13: EAN UPC JPC GTIN, char

:ean13: EAN UPC JPC GTIN, char

.. i18n: :code: Acronym, char, readonly

:code: Acronym, char, readonly

.. i18n: :pricelist_purchase: Purchase Pricelists, text, readonly

:pricelist_purchase: Purchase Pricelists, text, readonly

.. i18n: :incoming_qty: Incoming, float, readonly

:incoming_qty: Incoming, float, readonly

.. i18n:     *Quantities of products that are planned to arrive in selected locations or all internal if none have been selected.*

    *Quantities of products that are planned to arrive in selected locations or all internal if none have been selected.*

.. i18n: :standard_price: Cost Price, float, required

:standard_price: Cost Price, float, required

.. i18n:     *The cost of the product for accounting stock valorisation. It can serves as a base price for supplier price.*

    *The cost of the product for accounting stock valorisation. It can serves as a base price for supplier price.*

.. i18n: :membership_date_to: Date to, date

:membership_date_to: Date to, date

.. i18n: :size_x: Width, float

:size_x: Width, float

.. i18n: :size_y: Length, float

:size_y: Length, float

.. i18n: :size_z: Thickness, float

:size_z: Thickness, float

.. i18n: :property_account_income: Income Account, many2one

:property_account_income: Income Account, many2one

.. i18n:     *This account will be used, instead of the default one, to value incoming stock for the current product*

    *This account will be used, instead of the default one, to value incoming stock for the current product*

.. i18n: :list_price: Sale Price, float

:list_price: Sale Price, float

.. i18n:     *Base price for computing the customer price. Sometimes called the catalog price.*

    *Base price for computing the customer price. Sometimes called the catalog price.*

.. i18n: :author_om_ids: Authors, one2many

:author_om_ids: Authors, one2many

.. i18n: :company_id: Company, many2one

:company_id: Company, many2one

.. i18n: :use_time: Product usetime, integer

:use_time: Product usetime, integer

.. i18n: :loc_rack: Rack, char

:loc_rack: Rack, char

.. i18n: :ismenucard: Is Room, boolean

:ismenucard: Is Room, boolean

.. i18n: :price_margin: Variant Price Margin, float

:price_margin: Variant Price Margin, float

.. i18n: :property_stock_account_input: Stock Input Account, many2one

:property_stock_account_input: Stock Input Account, many2one

.. i18n:     *This account will be used, instead of the default one, to value input stock*

    *This account will be used, instead of the default one, to value input stock*

.. i18n: :format: Format, char

:format: Format, char

.. i18n: :finished_test: Finished Goods testing, one2many

:finished_test: Finished Goods testing, one2many

.. i18n:     *Quality Testing configuration for finished goods.*

    *Quality Testing configuration for finished goods.*

.. i18n: :is_direct_delivery_from_product: Is Supplier Direct Delivery Automatic?, boolean, readonly

:is_direct_delivery_from_product: Is Supplier Direct Delivery Automatic?, boolean, readonly

.. i18n: :cutting: Can be Cutted, boolean

:cutting: Can be Cutted, boolean

.. i18n: :sale_num_invoiced: # Invoiced, float, readonly

:sale_num_invoiced: # Invoiced, float, readonly

.. i18n:     *Sum of Quantity in Customer Invoices*

    *Sum of Quantity in Customer Invoices*

.. i18n: :variants: Variants, char

:variants: Variants, char

.. i18n: :partner_ref: Customer ref, char, readonly

:partner_ref: Customer ref, char, readonly

.. i18n: :rental: Rentable product, boolean

:rental: Rentable product, boolean

.. i18n: :purchase_num_invoiced: # Invoiced, float, readonly

:purchase_num_invoiced: # Invoiced, float, readonly

.. i18n:     *Sum of Quantity in Supplier Invoices*

    *Sum of Quantity in Supplier Invoices*

.. i18n: :path_ids: Location Paths, one2many

:path_ids: Location Paths, one2many

.. i18n:     *These rules set the right path of the product in the whole location tree.*

    *These rules set the right path of the product in the whole location tree.*

.. i18n: :mes_type: Measure Type, selection, required

:mes_type: Measure Type, selection, required

.. i18n: :name: Name, char, required

:name: Name, char, required

.. i18n: :qty_dispo: Stock available, float, readonly

:qty_dispo: Stock available, float, readonly

.. i18n: :sale_expected: Expected Sale, float, readonly

:sale_expected: Expected Sale, float, readonly

.. i18n:     *Sum of Multification of Sale Catalog price and quantity of Customer Invoices*

    *Sum of Multification of Sale Catalog price and quantity of Customer Invoices*

.. i18n: :seller_ids: Partners, one2many

:seller_ids: Partners, one2many

.. i18n: :x: X of Product, float

:x: X of Product, float

.. i18n: :rack: Rack, many2one

:rack: Rack, many2one

.. i18n: :isroom: Is Room, boolean

:isroom: Is Room, boolean

.. i18n: :supply_method: Supply method, selection, required

:supply_method: Supply method, selection, required

.. i18n:     *Produce will generate production order or tasks, according to the product type. Purchase will trigger purchase orders when requested.*

    *Produce will generate production order or tasks, according to the product type. Purchase will trigger purchase orders when requested.*

.. i18n: :orderpoint_ids: Orderpoints, one2many

:orderpoint_ids: Orderpoints, one2many

.. i18n: :weight: Gross weight, float

:weight: Gross weight, float

.. i18n:     *The gross weight in Kg.*

    *The gross weight in Kg.*

.. i18n: :back: Reliure, selection

:back: Reliure, selection

.. i18n: :creation_date: Creation date, datetime, readonly

:creation_date: Creation date, datetime, readonly

.. i18n: :total_margin_rate: Total Margin (%), float, readonly

:total_margin_rate: Total Margin (%), float, readonly

.. i18n:     *Total margin * 100 / Turnover*

    *Total margin * 100 / Turnover*

.. i18n: :description_purchase: Purchase Description, text

:description_purchase: Purchase Description, text

.. i18n: :sales_gap: Sales Gap, float, readonly

:sales_gap: Sales Gap, float, readonly

.. i18n:     *Excepted Sale - Turn Over*

    *Excepted Sale - Turn Over*

.. i18n: :virtual_available: Virtual Stock, float, readonly

:virtual_available: Virtual Stock, float, readonly

.. i18n:     *Futur stock for this product according to the selected location or all internal if none have been selected. Computed as: Real Stock - Outgoing + Incoming.*

    *Futur stock for this product according to the selected location or all internal if none have been selected. Computed as: Real Stock - Outgoing + Incoming.*

.. i18n: :date_retour: Return date, date

:date_retour: Return date, date

.. i18n: :total_cost: Total Cost, float, readonly

:total_cost: Total Cost, float, readonly

.. i18n:     *Sum of Multification of Invoice price and quantity of Supplier Invoices*

    *Sum of Multification of Invoice price and quantity of Supplier Invoices*

.. i18n: :thickness: Thickness, float

:thickness: Thickness, float

.. i18n: :product_tmpl_id: Product Template, many2one, required

:product_tmpl_id: Product Template, many2one, required

.. i18n: :state: State, selection

:state: State, selection

.. i18n: :life_time: Product lifetime, integer

:life_time: Product lifetime, integer

.. i18n: :weight_net: Net weight, float

:weight_net: Net weight, float

.. i18n:     *The net weight in Kg.*

    *The net weight in Kg.*

.. i18n: :sale_avg_price: Avg. Unit Price, float, readonly

:sale_avg_price: Avg. Unit Price, float, readonly

.. i18n:     *Avg. Price in Customer Invoices)*

    *Avg. Price in Customer Invoices)*

.. i18n: :manufacturer_pname: Manufacturer product name, char

:manufacturer_pname: Manufacturer product name, char

.. i18n: :partner_ref2: Customer ref, char, readonly

:partner_ref2: Customer ref, char, readonly

.. i18n: :active: Active, boolean

:active: Active, boolean

.. i18n: :loc_row: Row, char

:loc_row: Row, char

.. i18n: :manufacturer: Manufacturer, many2one

:manufacturer: Manufacturer, many2one

.. i18n: :loc_case: Case, char

:loc_case: Case, char

.. i18n: :property_stock_account_output: Stock Output Account, many2one

:property_stock_account_output: Stock Output Account, many2one

.. i18n:     *This account will be used, instead of the default one, to value output stock*

    *This account will be used, instead of the default one, to value output stock*

.. i18n: :lst_price: List Price, float, readonly

:lst_price: List Price, float, readonly

.. i18n: :purchase_ok: Can be Purchased, boolean

:purchase_ok: Can be Purchased, boolean

.. i18n:     *Determine if the product is visible in the list of products within a selection from a purchase order line.*

    *Determine if the product is visible in the list of products within a selection from a purchase order line.*

.. i18n: :catalog_num: Catalog number, char

:catalog_num: Catalog number, char

.. i18n: :tome: Tome, char

:tome: Tome, char

.. i18n: :warranty: Warranty (months), float

:warranty: Warranty (months), float

.. i18n: :property_stock_procurement: Procurement Location, many2one

:property_stock_procurement: Procurement Location, many2one

.. i18n:     *For the current product (template), this stock location will be used, instead of the default one, as the source location for stock moves generated by procurements*

    *For the current product (template), this stock location will be used, instead of the default one, as the source location for stock moves generated by procurements*

.. i18n: :uos_id: Unit of Sale, many2one

:uos_id: Unit of Sale, many2one

.. i18n:     *Used by companies that manages two unit of measure: invoicing and stock management. For example, in food industries, you will manage a stock of ham but invoice in Kg. Keep empty to use the default UOM.*

    *Used by companies that manages two unit of measure: invoicing and stock management. For example, in food industries, you will manage a stock of ham but invoice in Kg. Keep empty to use the default UOM.*

.. i18n: :isbn: Isbn code, char

:isbn: Isbn code, char

.. i18n: :purchase_line_warn_msg: Message for Purchase Order Line, text

:purchase_line_warn_msg: Message for Purchase Order Line, text

.. i18n: :member_price: Member Price, float

:member_price: Member Price, float

.. i18n: :sale_line_warn_msg: Message for Sale Order Line, text

:sale_line_warn_msg: Message for Sale Order Line, text

.. i18n: :packaging: Logistical Units, one2many

:packaging: Logistical Units, one2many

.. i18n:     *Gives the different ways to package the same product. This has no impact on the packing order and is mainly used if you use the EDI module.*

    *Gives the different ways to package the same product. This has no impact on the packing order and is mainly used if you use the EDI module.*

.. i18n: :purchase_avg_price: Avg. Unit Price, float, readonly

:purchase_avg_price: Avg. Unit Price, float, readonly

.. i18n:     *Avg. Price in Supplier Invoices*

    *Avg. Price in Supplier Invoices*

.. i18n: :production_test: During Production testing, one2many

:production_test: During Production testing, one2many

.. i18n:     *Quality Testing configuration during production.*

    *Quality Testing configuration during production.*

.. i18n: :qty_available: Real Stock, float, readonly

:qty_available: Real Stock, float, readonly

.. i18n:     *Current quantities of products in selected locations or all internal if none have been selected.*

    *Current quantities of products in selected locations or all internal if none have been selected.*

.. i18n: :num_pocket: Collection Num., char

:num_pocket: Collection Num., char

.. i18n: :property_account_expense_world1: Outside Europe Expense Account, many2one

:property_account_expense_world1: Outside Europe Expense Account, many2one

.. i18n:     *This account will be used, instead of the default one, to value outgoing stock for the current product*

    *This account will be used, instead of the default one, to value outgoing stock for the current product*

.. i18n: :uos_coeff: UOM -> UOS Coeff, float

:uos_coeff: UOM -> UOS Coeff, float

.. i18n:     *Coefficient to convert UOM to UOS
.. i18n:     uom = uos * coeff*

    *Coefficient to convert UOM to UOS
    uom = uos * coeff*

.. i18n: :auto_pick: Auto Picking, boolean

:auto_pick: Auto Picking, boolean

.. i18n:     *Auto picking for raw materials of production orders.*

    *Auto picking for raw materials of production orders.*

.. i18n: :expected_margin_rate: Expected Margin (%), float, readonly

:expected_margin_rate: Expected Margin (%), float, readonly

.. i18n:     *Expected margin * 100 / Expected Sale*

    *Expected margin * 100 / Expected Sale*

.. i18n: :buyer_price_index: Indexed buyer price, float, readonly

:buyer_price_index: Indexed buyer price, float, readonly

.. i18n: :index_purchase: Purchase indexes, many2many

:index_purchase: Purchase indexes, many2many

.. i18n: :product_manager: Product Manager, many2one

:product_manager: Product Manager, many2one

.. i18n: :width: Width, float

:width: Width, float

.. i18n: :pricelist_sale: Sale Pricelists, text, readonly

:pricelist_sale: Sale Pricelists, text, readonly

.. i18n: :normal_cost: Normal Cost, float, readonly

:normal_cost: Normal Cost, float, readonly

.. i18n:     *Sum of Multification of Cost price and quantity of Supplier Invoices*

    *Sum of Multification of Cost price and quantity of Supplier Invoices*

.. i18n: :raw_m_test: Raw material testing, one2many

:raw_m_test: Raw material testing, one2many

.. i18n:     *Quality Testing configuration for raw material.*

    *Quality Testing configuration for raw material.*

.. i18n: :type: Product Type, selection, required

:type: Product Type, selection, required

.. i18n:     *Will change the way procurements are processed, consumable are stockable products with infinite stock, or without a stock management in the system.*

    *Will change the way procurements are processed, consumable are stockable products with infinite stock, or without a stock management in the system.*

.. i18n: :property_account_income_europe: Income Account for Europe, many2one

:property_account_income_europe: Income Account for Europe, many2one

.. i18n:     *This account will be used, instead of the default one, to value incoming stock for the current product*

    *This account will be used, instead of the default one, to value incoming stock for the current product*

.. i18n: :editor: Editor, many2one

:editor: Editor, many2one

.. i18n: :lang: Language, many2many

:lang: Language, many2many

.. i18n: :price_cat: Price category, many2one

:price_cat: Price category, many2one

.. i18n: :num_edition: Num. edition, integer

:num_edition: Num. edition, integer

.. i18n: :track_incoming: Track Incomming Lots, boolean

:track_incoming: Track Incomming Lots, boolean

.. i18n:     *Force to use a Production Lot during receptions*

    *Force to use a Production Lot during receptions*

.. i18n: :property_stock_production: Production Location, many2one

:property_stock_production: Production Location, many2one

.. i18n:     *For the current product (template), this stock location will be used, instead of the default one, as the source location for stock moves generated by production orders*

    *For the current product (template), this stock location will be used, instead of the default one, as the source location for stock moves generated by production orders*

.. i18n: :supplier_taxes_id: Supplier Taxes, many2many

:supplier_taxes_id: Supplier Taxes, many2many

.. i18n: :removal_time: Product removal time, integer

:removal_time: Product removal time, integer

.. i18n: :package_weight: Package Weight, float

:package_weight: Package Weight, float

.. i18n: :membership_date_from: Date from, date

:membership_date_from: Date from, date

.. i18n: :date_to: To Date, date, readonly

:date_to: To Date, date, readonly

.. i18n: :procure_method: Procure Method, selection, required

:procure_method: Procure Method, selection, required

.. i18n:     *'Make to Stock': When needed, take from the stock or wait until refurnishing. 'Make to Order': When needed, purchase or produce for the procurement request.*

    *'Make to Stock': When needed, take from the stock or wait until refurnishing. 'Make to Order': When needed, purchase or produce for the procurement request.*

.. i18n: :property_stock_inventory: Inventory Location, many2one

:property_stock_inventory: Inventory Location, many2one

.. i18n:     *For the current product (template), this stock location will be used, instead of the default one, as the source location for stock moves generated when you do an inventory*

    *For the current product (template), this stock location will be used, instead of the default one, as the source location for stock moves generated when you do an inventory*

.. i18n: :cost_method: Costing Method, selection, required

:cost_method: Costing Method, selection, required

.. i18n:     *Standard Price: the cost price is fixed and recomputed periodically (usually at the end of the year), Average Price: the cost price is recomputed at each reception of products.*

    *Standard Price: the cost price is fixed and recomputed periodically (usually at the end of the year), Average Price: the cost price is recomputed at each reception of products.*

.. i18n: :product_id: Product_id, many2one

:product_id: Product_id, many2one

.. i18n: :volume: Volume, float

:volume: Volume, float

.. i18n:     *The volume in m3.*

    *The volume in m3.*

.. i18n: :sale_delay: Customer Lead Time, float

:sale_delay: Customer Lead Time, float

.. i18n:     *This is the average time between the confirmation of the customer order and the delivery of the finnished products. It's the time you promise to your customers.*

    *This is the average time between the confirmation of the customer order and the delivery of the finnished products. It's the time you promise to your customers.*

.. i18n: :description_sale: Sale Description, text

:description_sale: Sale Description, text

.. i18n: :purchase_line_warn: Purchase Order Line, boolean

:purchase_line_warn: Purchase Order Line, boolean

.. i18n: :dimension_ids: Dimensions, many2many

:dimension_ids: Dimensions, many2many

.. i18n: :lot_ids: Lots, one2many

:lot_ids: Lots, one2many

.. i18n: :z: Z of Product, float

:z: Z of Product, float

.. i18n: :purchase_gap: Purchase Gap, float, readonly

:purchase_gap: Purchase Gap, float, readonly

.. i18n:     *Normal Cost - Total Cost*

    *Normal Cost - Total Cost*

.. i18n: :sale_line_warn: Sale Order Line, boolean

:sale_line_warn: Sale Order Line, boolean

.. i18n: :isservice: Is Service id, boolean

:isservice: Is Service id, boolean

.. i18n: :track_production: Track Production Lots, boolean

:track_production: Track Production Lots, boolean

.. i18n:     *Force to use a Production Lot during production order*

    *Force to use a Production Lot during production order*

.. i18n: :sale_ok: Can be sold, boolean

:sale_ok: Can be sold, boolean

.. i18n:     *Determine if the product can be visible in the list of product within a selection from a sale order line.*

    *Determine if the product can be visible in the list of product within a selection from a sale order line.*

.. i18n: :nbpage: Number of pages, integer

:nbpage: Number of pages, integer

.. i18n: :price_extra: Variant Price Extra, float

:price_extra: Variant Price Extra, float

.. i18n: :uom_id: Default UoM, many2one, required

:uom_id: Default UoM, many2one, required

.. i18n:     *Default Unit of Measure used for all stock operation.*

    *Default Unit of Measure used for all stock operation.*

.. i18n: :default_code: Code, char

:default_code: Code, char

.. i18n: :attribute_ids: Attributes, one2many

:attribute_ids: Attributes, one2many

.. i18n: :iscategid: Is categ id, boolean

:iscategid: Is categ id, boolean

.. i18n: :expected_margin: Expected Margin, float, readonly

:expected_margin: Expected Margin, float, readonly

.. i18n:     *Excepted Sale - Normal Cost*

    *Excepted Sale - Normal Cost*

.. i18n: :standard_price_index: Indexed standard price, float, readonly

:standard_price_index: Indexed standard price, float, readonly

.. i18n: :product_logo: Product Logo, binary

:product_logo: Product Logo, binary

.. i18n: :auto_picking: Auto Picking for Production, boolean

:auto_picking: Auto Picking for Production, boolean

.. i18n: :date_from: From Date, date, readonly

:date_from: From Date, date, readonly

.. i18n: :track_outgoing: Track Outging Lots, boolean

:track_outgoing: Track Outging Lots, boolean

.. i18n:     *Force to use a Production Lot during deliveries*

    *Force to use a Production Lot during deliveries*

.. i18n: :length: Length, float

:length: Length, float

.. i18n: :turnover: Turnover, float, readonly

:turnover: Turnover, float, readonly

.. i18n:     *Sum of Multification of Invoice price and quantity of Customer Invoices*

    *Sum of Multification of Invoice price and quantity of Customer Invoices*

.. i18n: :property_account_income_world: Outside Europe Income Account, many2one

:property_account_income_world: Outside Europe Income Account, many2one

.. i18n:     *This account will be used, instead of the default one, to value incoming stock for the current product*

    *This account will be used, instead of the default one, to value incoming stock for the current product*

.. i18n: :is_maintenance: Is Maintenance?, boolean

:is_maintenance: Is Maintenance?, boolean

.. i18n: :online: Visible on website, boolean

:online: Visible on website, boolean

.. i18n: :uom_po_id: Purchase UoM, many2one, required

:uom_po_id: Purchase UoM, many2one, required

.. i18n:     *Default Unit of Measure used for purchase orders. It must in the same category than the default unit of measure.*

    *Default Unit of Measure used for purchase orders. It must in the same category than the default unit of measure.*

.. i18n: :intrastat_id: Intrastat code, many2one

:intrastat_id: Intrastat code, many2one

.. i18n: :description: Description, text

:description: Description, text

.. i18n: :list_price_index: Indexed list price, float, readonly

:list_price_index: Indexed list price, float, readonly

.. i18n: :property_account_expense_europe: Expense Account for Europe, many2one

:property_account_expense_europe: Expense Account for Europe, many2one

.. i18n:     *This account will be used, instead of the default one, to value outgoing stock for the current product*

    *This account will be used, instead of the default one, to value outgoing stock for the current product*

.. i18n: :price: Customer Price, float, readonly

:price: Customer Price, float, readonly

.. i18n: :index_date: Index price date, date, required

:index_date: Index price date, date, required

.. i18n: :collection: Collection, many2one

:collection: Collection, many2one

.. i18n: :membership: Membership, boolean

:membership: Membership, boolean

.. i18n:     *Specify if this product is a membership product*

    *Specify if this product is a membership product*

.. i18n: :seller_delay: Supplier Lead Time, integer, readonly

:seller_delay: Supplier Lead Time, integer, readonly

.. i18n:     *This is the average delay in days between the purchase order confirmation and the reception of goods for this product and for the default supplier. It is used by the scheduler to order requests based on reordering delays.*

    *This is the average delay in days between the purchase order confirmation and the reception of goods for this product and for the default supplier. It is used by the scheduler to order requests based on reordering delays.*

.. i18n: :manufacturer_pref: Manufacturer product code, char

:manufacturer_pref: Manufacturer product code, char

.. i18n: :categ_id: Category, many2one, required

:categ_id: Category, many2one, required

.. i18n: :author_ids: Authors, many2many

:author_ids: Authors, many2many

.. i18n: :pocket: Pocket, char

:pocket: Pocket, char

.. i18n: :link_ids: Related Books, many2many

:link_ids: Related Books, many2many

.. i18n: :equivalency_in_A4: A4 Equivalency, float

:equivalency_in_A4: A4 Equivalency, float

.. i18n: :url: Image URL, char

:url: Image URL, char

.. i18n:     *Add Product Image URL.*

    *Add Product Image URL.*

.. i18n: :produce_delay: Manufacturing Lead Time, float

:produce_delay: Manufacturing Lead Time, float

.. i18n:     *Average time to produce this product. This is only for the production order and, if it is a multi-level bill of material, it's only for the level of this product. Different delays will be summed for all levels and purchase orders.*

    *Average time to produce this product. This is only for the production order and, if it is a multi-level bill of material, it's only for the level of this product. Different delays will be summed for all levels and purchase orders.*

.. i18n: :property_account_expense: Expense Account, many2one

:property_account_expense: Expense Account, many2one

.. i18n:     *This account will be used, instead of the default one, to value outgoing stock for the current product*

    *This account will be used, instead of the default one, to value outgoing stock for the current product*

.. i18n: :calculate_price: Compute price, boolean

:calculate_price: Compute price, boolean

.. i18n: :invoice_state: Invoice State, selection, readonly

:invoice_state: Invoice State, selection, readonly

.. i18n: :outgoing_qty: Outgoing, float, readonly

:outgoing_qty: Outgoing, float, readonly

.. i18n:     *Quantities of products that are planned to leave in selected locations or all internal if none have been selected.*

    *Quantities of products that are planned to leave in selected locations or all internal if none have been selected.*

.. i18n: :alert_time: Product alert time, integer

:alert_time: Product alert time, integer

.. i18n: :taxes_id: Product Taxes, many2many

:taxes_id: Product Taxes, many2many

.. i18n: :y: Y of Product, float

:y: Y of Product, float

.. i18n: :date_parution: Release date, date

:date_parution: Release date, date

.. i18n: :total_margin: Total Margin, float, readonly

:total_margin: Total Margin, float, readonly

.. i18n:     *Turnorder - Total Cost*

    *Turnorder - Total Cost*

.. i18n: :index_sale: Sales indexes, many2many

:index_sale: Sales indexes, many2many

.. i18n: :buyer_price: Buyer price, float

:buyer_price: Buyer price, float

.. i18n: :unique_production_number: Unique Production Number, boolean

:unique_production_number: Unique Production Number, boolean

.. i18n: Object: Includes Hotel Restaurant Table (hotel.restaurant.tables)
.. i18n: #################################################################

Object: Includes Hotel Restaurant Table (hotel.restaurant.tables)
#################################################################

.. i18n: :capacity: Capacity, integer

:capacity: Capacity, integer

.. i18n: :name: Table number, char, required

:name: Table number, char, required

.. i18n: Object: Includes Hotel Restaurant Reservation (hotel.restaurant.reservation)
.. i18n: ############################################################################

Object: Includes Hotel Restaurant Reservation (hotel.restaurant.reservation)
############################################################################

.. i18n: :end_date: End Date, datetime, required

:end_date: End Date, datetime, required

.. i18n: :room_no: Room No, many2one

:room_no: Room No, many2one

.. i18n: :tableno: Table number, many2many

:tableno: Table number, many2many

.. i18n: :partner_address_id: Address, many2one

:partner_address_id: Address, many2one

.. i18n: :state: state, selection, required, readonly

:state: state, selection, required, readonly

.. i18n: :cname: Customer Name, many2one, required

:cname: Customer Name, many2one, required

.. i18n: :reservation_id: Reservation No, char, required

:reservation_id: Reservation No, char, required

.. i18n: :start_date: Start Date, datetime, required

:start_date: Start Date, datetime, required

.. i18n: Object: Includes Hotel Restaurant Order (hotel.restaurant.kitchen.order.tickets)
.. i18n: ################################################################################

Object: Includes Hotel Restaurant Order (hotel.restaurant.kitchen.order.tickets)
################################################################################

.. i18n: :tableno: Table number, many2many

:tableno: Table number, many2many

.. i18n: :room_no: Room No, char, readonly

:room_no: Room No, char, readonly

.. i18n: :w_name: Waiter Name, char, readonly

:w_name: Waiter Name, char, readonly

.. i18n: :kot_date: Date, datetime

:kot_date: Date, datetime

.. i18n: :orderno: Order Number, char, readonly

:orderno: Order Number, char, readonly

.. i18n: :resno: Reservation Number, char

:resno: Reservation Number, char

.. i18n: :kot_list: Order List, one2many

:kot_list: Order List, one2many

.. i18n: Object: Includes Hotel Restaurant Order (hotel.restaurant.order)
.. i18n: ################################################################

Object: Includes Hotel Restaurant Order (hotel.restaurant.order)
################################################################

.. i18n: :room_no: Room No, many2one

:room_no: Room No, many2one

.. i18n: :order_no: Order Number, char, required

:order_no: Order Number, char, required

.. i18n: :tax: Tax (%) , float

:tax: Tax (%) , float

.. i18n: :table_no: Table number, many2many

:table_no: Table number, many2many

.. i18n: :amount_subtotal: Subtotal, float, readonly

:amount_subtotal: Subtotal, float, readonly

.. i18n: :o_date: Date, datetime, required

:o_date: Date, datetime, required

.. i18n: :order_list: Order List, one2many

:order_list: Order List, one2many

.. i18n: :amount_total: Total, float, readonly

:amount_total: Total, float, readonly

.. i18n: :waiter_name: Waiter Name, many2one, required

:waiter_name: Waiter Name, many2one, required

.. i18n: Object: Reservation Order (hotel.reservation.order)
.. i18n: ###################################################

Object: Reservation Order (hotel.reservation.order)
###################################################

.. i18n: :date1: Date, datetime, required

:date1: Date, datetime, required

.. i18n: :order_list: Order List, one2many

:order_list: Order List, one2many

.. i18n: :amount_subtotal: Subtotal, float, readonly

:amount_subtotal: Subtotal, float, readonly

.. i18n: :reservationno: Reservation No, char

:reservationno: Reservation No, char

.. i18n: :tax: Tax (%) , float

:tax: Tax (%) , float

.. i18n: :waitername: Waiter Name, many2one

:waitername: Waiter Name, many2one

.. i18n: :order_number: Order No, char

:order_number: Order No, char

.. i18n: :table_no: Table number, many2many

:table_no: Table number, many2many

.. i18n: :amount_total: Total, float, readonly

:amount_total: Total, float, readonly

.. i18n: Object: Includes Hotel Restaurant Order (hotel.restaurant.order.list)
.. i18n: #####################################################################

Object: Includes Hotel Restaurant Order (hotel.restaurant.order.list)
#####################################################################

.. i18n: :o_list: unknown, many2one

:o_list: unknown, many2one

.. i18n: :item_qty: Qty, char, required

:item_qty: Qty, char, required

.. i18n: :name: Item Name, many2one, required

:name: Item Name, many2one, required

.. i18n: :kot_order_list: unknown, many2one

:kot_order_list: unknown, many2one

.. i18n: :price_subtotal: Subtotal, float, readonly

:price_subtotal: Subtotal, float, readonly

.. i18n: :o_l: unknown, many2one

:o_l: unknown, many2one

.. i18n: :item_rate: Rate, float

:item_rate: Rate, float
