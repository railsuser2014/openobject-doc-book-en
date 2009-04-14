
.. i18n: .. module:: hotel
.. i18n:     :synopsis: Hotel Management 
.. i18n:     :noindex:
.. i18n: .. 

.. module:: hotel
    :synopsis: Hotel Management 
    :noindex:
.. 

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. i18n: Hotel Management (*hotel*)
.. i18n: ==========================
.. i18n: :Module: hotel
.. i18n: :Name: Hotel Management
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: hotel
.. i18n: :Web: 
.. i18n: :Official module: no
.. i18n: :Quality certified: no

Hotel Management (*hotel*)
==========================
:Module: hotel
:Name: Hotel Management
:Version: 5.0.1.0
:Author: Tiny
:Directory: hotel
:Web: 
:Official module: no
:Quality certified: no

.. i18n: Description
.. i18n: -----------

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   Module for Hotel/Resort/Property management. You can manage:
.. i18n:       * Configure Property
.. i18n:       * Hotel Configuration
.. i18n:       * Check In, Check out
.. i18n:       * Manage Folio
.. i18n:       * Payment
.. i18n:   
.. i18n:       Different reports are also provided, mainly for hotel statistics.

::

  Module for Hotel/Resort/Property management. You can manage:
      * Configure Property
      * Hotel Configuration
      * Check In, Check out
      * Manage Folio
      * Payment
  
      Different reports are also provided, mainly for hotel statistics.

.. i18n: Dependencies
.. i18n: ------------

Dependencies
------------

.. i18n:  * :mod:`base`
.. i18n:  * :mod:`product`
.. i18n:  * :mod:`sale`

 * :mod:`base`
 * :mod:`product`
 * :mod:`sale`

.. i18n: Reports
.. i18n: -------

Reports
-------

.. i18n:  * Folio Total

 * Folio Total

.. i18n: Menus
.. i18n: -------

Menus
-------

.. i18n:  * Hotel Management
.. i18n:  * Hotel Management/Configuration
.. i18n:  * Hotel Management/Configuration/Floor
.. i18n:  * Hotel Management/Configuration/Amenities Types
.. i18n:  * Hotel Management/Amenities
.. i18n:  * Hotel Management/Configuration/Room Type
.. i18n:  * Hotel Management/Rooms
.. i18n:  * Hotel Management/Configuration/Services Type
.. i18n:  * Hotel Management/Services
.. i18n:  * Hotel Management/Generate Folio
.. i18n:  * Hotel Management/Generate Folio/All Folio
.. i18n:  * Hotel Management/Configuration/Room Type
.. i18n:  * Hotel Management/Configuration/Room Type/Room by Category
.. i18n:  * Hotel Management/Configuration/Amenities Types
.. i18n:  * Hotel Management/Configuration/Amenities Types/Amenities by Category
.. i18n:  * Hotel Management/Configuration/Services Type/Services by Category
.. i18n:  * Hotel Management/Reports

 * Hotel Management
 * Hotel Management/Configuration
 * Hotel Management/Configuration/Floor
 * Hotel Management/Configuration/Amenities Types
 * Hotel Management/Amenities
 * Hotel Management/Configuration/Room Type
 * Hotel Management/Rooms
 * Hotel Management/Configuration/Services Type
 * Hotel Management/Services
 * Hotel Management/Generate Folio
 * Hotel Management/Generate Folio/All Folio
 * Hotel Management/Configuration/Room Type
 * Hotel Management/Configuration/Room Type/Room by Category
 * Hotel Management/Configuration/Amenities Types
 * Hotel Management/Configuration/Amenities Types/Amenities by Category
 * Hotel Management/Configuration/Services Type/Services by Category
 * Hotel Management/Reports

.. i18n: Views
.. i18n: -----

Views
-----

.. i18n:  * hotel.floor.form (form)
.. i18n:  * hotel.floor.tree (tree)
.. i18n:  * hotel.room_amenities_type_form (form)
.. i18n:  * hotel.room_amenities_type_list (tree)
.. i18n:  * hotel.room_amenities_form (form)
.. i18n:  * hotel.room_amenities_list (tree)
.. i18n:  * hotel.room_type.form (form)
.. i18n:  * hotel.room_type.tree (tree)
.. i18n:  * hotel.room.form (form)
.. i18n:  * hotel.room.tree (tree)
.. i18n:  * hotel.service_type.form (form)
.. i18n:  * hotel.service_type.tree (tree)
.. i18n:  * .hotel.services.form (form)
.. i18n:  * hotel.services.tree (tree)
.. i18n:  * hotel.folio.form (form)
.. i18n:  * hotel.folio.tree (tree)

 * hotel.floor.form (form)
 * hotel.floor.tree (tree)
 * hotel.room_amenities_type_form (form)
 * hotel.room_amenities_type_list (tree)
 * hotel.room_amenities_form (form)
 * hotel.room_amenities_list (tree)
 * hotel.room_type.form (form)
 * hotel.room_type.tree (tree)
 * hotel.room.form (form)
 * hotel.room.tree (tree)
 * hotel.service_type.form (form)
 * hotel.service_type.tree (tree)
 * .hotel.services.form (form)
 * hotel.services.tree (tree)
 * hotel.folio.form (form)
 * hotel.folio.tree (tree)

.. i18n: Objects
.. i18n: -------

Objects
-------

.. i18n: Object: Floor (hotel.floor)
.. i18n: ###########################

Object: Floor (hotel.floor)
###########################

.. i18n: :name: Floor Name, char, required

:name: Floor Name, char, required

.. i18n: :sequence: Sequence, integer

:sequence: Sequence, integer

.. i18n: Object: Room Type (hotel.room_type)
.. i18n: ###################################

Object: Room Type (hotel.room_type)
###################################

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

.. i18n: :cat_id: category, many2one, required

:cat_id: category, many2one, required

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

.. i18n: Object: amenities Type (hotel.room_amenities_type)
.. i18n: ##################################################

Object: amenities Type (hotel.room_amenities_type)
##################################################

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

.. i18n: :cat_id: category, many2one, required

:cat_id: category, many2one, required

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

.. i18n: Object: Room amenities (hotel.room_amenities)
.. i18n: #############################################

Object: Room amenities (hotel.room_amenities)
#############################################

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

.. i18n: :rcateg_id: Amenity Catagory, many2one

:rcateg_id: Amenity Catagory, many2one

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

.. i18n: :room_categ_id: Product Category, many2one, required

:room_categ_id: Product Category, many2one, required

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

.. i18n: :amenity_rate: Amenity Rate, integer

:amenity_rate: Amenity Rate, integer

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

.. i18n: Object: Hotel Room (hotel.room)
.. i18n: ###############################

Object: Hotel Room (hotel.room)
###############################

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

.. i18n: :room_amenities: Room Amenities, many2many

:room_amenities: Room Amenities, many2many

.. i18n: :maxChild: Max Child, integer

:maxChild: Max Child, integer

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

.. i18n: :avail_status: Room Status, selection

:avail_status: Room Status, selection

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

.. i18n: :maxAdult: Max Adult, integer

:maxAdult: Max Adult, integer

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

.. i18n: :floor_id: Floor No, many2one

:floor_id: Floor No, many2one

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

.. i18n: Object: hotel folio new (hotel.folio)
.. i18n: #####################################

Object: hotel folio new (hotel.folio)
#####################################

.. i18n: :origin: Origin, char

:origin: Origin, char

.. i18n: :topnotes: Top Notes, text

:topnotes: Top Notes, text

.. i18n: :checkin_date: Check In, datetime, required, readonly

:checkin_date: Check In, datetime, required, readonly

.. i18n: :order_line: Order Lines, one2many, readonly

:order_line: Order Lines, one2many, readonly

.. i18n: :picking_policy: Packing Policy, selection, required

:picking_policy: Packing Policy, selection, required

.. i18n:     *If you don't have enough stock available to deliver all at once, do you accept partial shippings or not.*

    *If you don't have enough stock available to deliver all at once, do you accept partial shippings or not.*

.. i18n: :order_policy: Shipping Policy, selection, required, readonly

:order_policy: Shipping Policy, selection, required, readonly

.. i18n:     *The Shipping Policy is used to synchronise invoice and delivery operations.
.. i18n:     - The 'Pay before delivery' choice will first generate the invoice and then generate the packing order after the payment of this invoice.
.. i18n:     - The 'Shipping & Manual Invoice' will create the packing order directly and wait for the user to manually click on the 'Invoice' button to generate the draft invoice.
.. i18n:     - The 'Invoice on Order Ater Delivery' choice will generate the draft invoice based on sale order after all packing lists have been finished.
.. i18n:     - The 'Invoice from the packings' choice is used to create an invoice during the packing process.*

    *The Shipping Policy is used to synchronise invoice and delivery operations.
    - The 'Pay before delivery' choice will first generate the invoice and then generate the packing order after the payment of this invoice.
    - The 'Shipping & Manual Invoice' will create the packing order directly and wait for the user to manually click on the 'Invoice' button to generate the draft invoice.
    - The 'Invoice on Order Ater Delivery' choice will generate the draft invoice based on sale order after all packing lists have been finished.
    - The 'Invoice from the packings' choice is used to create an invoice during the packing process.*

.. i18n: :carrier_id: Delivery method, many2one

:carrier_id: Delivery method, many2one

.. i18n:     *Complete this field if you plan to invoice the shipping based on packings made.*

    *Complete this field if you plan to invoice the shipping based on packings made.*

.. i18n: :invoice_ids: Invoice, many2many

:invoice_ids: Invoice, many2many

.. i18n:     *This is the list of invoices that have been generated for this sale order. The same sale order may have been invoiced in several times (by line for example).*

    *This is the list of invoices that have been generated for this sale order. The same sale order may have been invoiced in several times (by line for example).*

.. i18n: :shop_id: Shop, many2one, required, readonly

:shop_id: Shop, many2one, required, readonly

.. i18n: :fleet_id: Default Sub Fleet, many2one

:fleet_id: Default Sub Fleet, many2one

.. i18n: :partner_shipping_id: Shipping Address, many2one, required, readonly

:partner_shipping_id: Shipping Address, many2one, required, readonly

.. i18n: :client_order_ref: Customer Ref., char

:client_order_ref: Customer Ref., char

.. i18n: :date_order: Date Ordered, date, required, readonly

:date_order: Date Ordered, date, required, readonly

.. i18n: :esale_osc_id: esale_osc Id, integer

:esale_osc_id: esale_osc Id, integer

.. i18n: :id: ID, integer, readonly

:id: ID, integer, readonly

.. i18n: :invoiced: Paid, boolean, readonly

:invoiced: Paid, boolean, readonly

.. i18n: :delivery_line: Delivery Lines, one2many, readonly

:delivery_line: Delivery Lines, one2many, readonly

.. i18n: :note: Notes, text

:note: Notes, text

.. i18n: :fiscal_position: Fiscal Position, many2one

:fiscal_position: Fiscal Position, many2one

.. i18n: :user_id: Salesman, many2one

:user_id: Salesman, many2one

.. i18n: :partner_id: Customer, many2one, readonly

:partner_id: Customer, many2one, readonly

.. i18n: :payment_term: Payment Term, many2one

:payment_term: Payment Term, many2one

.. i18n: :parent_so: Parent Sales Order, many2one

:parent_so: Parent Sales Order, many2one

.. i18n: :journal_id: Journal, many2one

:journal_id: Journal, many2one

.. i18n: :amount_tax: Taxes, float, readonly

:amount_tax: Taxes, float, readonly

.. i18n: :state: Order State, selection, readonly

:state: Order State, selection, readonly

.. i18n:     *Gives the state of the quotation or sale order. The exception state is automatically set when a cancel operation occurs in the invoice validation (Invoice Exception) or in the packing list process (Shipping Exception). The 'Waiting Schedule' state is set when the invoice is confirmed but waiting for the scheduler to be on the date 'Date Ordered'.*

    *Gives the state of the quotation or sale order. The exception state is automatically set when a cancel operation occurs in the invoice validation (Invoice Exception) or in the packing list process (Shipping Exception). The 'Waiting Schedule' state is set when the invoice is confirmed but waiting for the scheduler to be on the date 'Date Ordered'.*

.. i18n: :partner_bank: Bank Account, many2one

:partner_bank: Bank Account, many2one

.. i18n:     *The bank account to pay to or to be paid from. It will be transferred to the invoice*

    *The bank account to pay to or to be paid from. It will be transferred to the invoice*

.. i18n: :abstract_line_ids: Order Lines, one2many, readonly

:abstract_line_ids: Order Lines, one2many, readonly

.. i18n: :invoiced_rate: Invoiced, float, readonly

:invoiced_rate: Invoiced, float, readonly

.. i18n: :service_lines: unknown, one2many

:service_lines: unknown, one2many

.. i18n: :pricelist_id: Pricelist, many2one, required, readonly

:pricelist_id: Pricelist, many2one, required, readonly

.. i18n: :advertising_agency: Advertising Agency, many2one

:advertising_agency: Advertising Agency, many2one

.. i18n: :project_id: Analytic Account, many2one, readonly

:project_id: Analytic Account, many2one, readonly

.. i18n: :has_supplier_direct_delivery: Has Supplier Direct Delivery, boolean, readonly

:has_supplier_direct_delivery: Has Supplier Direct Delivery, boolean, readonly

.. i18n: :child_so: Child Sales Order, one2many

:child_so: Child Sales Order, one2many

.. i18n: :incoterm: Incoterm, selection

:incoterm: Incoterm, selection

.. i18n: :checkout_date: Check Out, datetime, required, readonly

:checkout_date: Check Out, datetime, required, readonly

.. i18n: :order_id: order_id, many2one, required

:order_id: order_id, many2one, required

.. i18n: :published_customer: Published Customer, many2one

:published_customer: Published Customer, many2one

.. i18n: :partner_order_id: Ordering Contact, many2one, required, readonly

:partner_order_id: Ordering Contact, many2one, required, readonly

.. i18n:     *The name and address of the contact that requested the order or quotation.*

    *The name and address of the contact that requested the order or quotation.*

.. i18n: :picked_rate: Picked, float, readonly

:picked_rate: Picked, float, readonly

.. i18n: :partner_invoice_id: Invoice Address, many2one, required, readonly

:partner_invoice_id: Invoice Address, many2one, required, readonly

.. i18n: :amount_untaxed: Untaxed Amount, float, readonly

:amount_untaxed: Untaxed Amount, float, readonly

.. i18n: :invoice_type_id: Invoice Type, many2one

:invoice_type_id: Invoice Type, many2one

.. i18n: :picking_ids: Related Packings, one2many, readonly

:picking_ids: Related Packings, one2many, readonly

.. i18n:     *This is the list of picking list that have been generated for this invoice*

    *This is the list of picking list that have been generated for this invoice*

.. i18n: :amount_total: Total, float, readonly

:amount_total: Total, float, readonly

.. i18n: :name: Order Reference, char, required

:name: Order Reference, char, required

.. i18n: :esale_osc_web: Website, many2one

:esale_osc_web: Website, many2one

.. i18n: :customer_pricelist_id: Customer Pricelist, many2one

:customer_pricelist_id: Customer Pricelist, many2one

.. i18n: :price_type: Price method, selection, required

:price_type: Price method, selection, required

.. i18n: :case_ids: Related Cases, one2many

:case_ids: Related Cases, one2many

.. i18n: :dept: Department, many2one

:dept: Department, many2one

.. i18n: :shipped: Picked, boolean, readonly

:shipped: Picked, boolean, readonly

.. i18n: :invoice_quantity: Invoice on, selection, required

:invoice_quantity: Invoice on, selection, required

.. i18n:     *The sale order will automatically create the invoice proposition (draft invoice). Ordered and delivered quantities may not be the same. You have to choose if you invoice based on ordered or shipped quantities. If the product is a service, shipped quantities means hours spent on the associated tasks.*

    *The sale order will automatically create the invoice proposition (draft invoice). Ordered and delivered quantities may not be the same. You have to choose if you invoice based on ordered or shipped quantities. If the product is a service, shipped quantities means hours spent on the associated tasks.*

.. i18n: :payment_type: Payment type, many2one

:payment_type: Payment type, many2one

.. i18n:     *The type of payment. It will be transferred to the invoice*

    *The type of payment. It will be transferred to the invoice*

.. i18n: :discount_campaign: Discount Campaign, many2one

:discount_campaign: Discount Campaign, many2one

.. i18n: :margin: Margin, float, readonly

:margin: Margin, float, readonly

.. i18n: :room_lines: unknown, one2many

:room_lines: unknown, one2many

.. i18n: Object: hotel folio1 room line (hotel_folio.line)
.. i18n: #################################################

Object: hotel folio1 room line (hotel_folio.line)
#################################################

.. i18n: :property_ids: Properties, many2many

:property_ids: Properties, many2many

.. i18n: :product_uos_qty: Quantity (UOS), float

:product_uos_qty: Quantity (UOS), float

.. i18n: :adv_issue: Advertising Issue, many2one

:adv_issue: Advertising Issue, many2one

.. i18n: :product_uom: Product UoM, many2one, required

:product_uom: Product UoM, many2one, required

.. i18n: :sequence: Sequence Number, integer

:sequence: Sequence Number, integer

.. i18n: :parent_fleet_id: Fleet, many2one

:parent_fleet_id: Fleet, many2one

.. i18n: :price_unit: Unit Price, float, required

:price_unit: Unit Price, float, required

.. i18n: :product_uom_qty: Quantity (UoM), float, required

:product_uom_qty: Quantity (UoM), float, required

.. i18n: :price_subtotal: Subtotal w/o tax, float, readonly

:price_subtotal: Subtotal w/o tax, float, readonly

.. i18n: :maintenance_month_qty: Maintenance Month Quantity, integer, readonly

:maintenance_month_qty: Maintenance Month Quantity, integer, readonly

.. i18n: :deliveries: Planned Deliveries, float, readonly

:deliveries: Planned Deliveries, float, readonly

.. i18n: :is_supplier_direct_delivery_advised: Is Supplier Direct Delivery Advised?, boolean, readonly

:is_supplier_direct_delivery_advised: Is Supplier Direct Delivery Advised?, boolean, readonly

.. i18n: :size_x: Width, float

:size_x: Width, float

.. i18n: :size_y: Height, float

:size_y: Height, float

.. i18n: :size_z: Thickness, float

:size_z: Thickness, float

.. i18n: :product_uos: Product UOS, many2one

:product_uos: Product UOS, many2one

.. i18n: :purchase_order_line: Related Purchase Order Line, many2one

:purchase_order_line: Related Purchase Order Line, many2one

.. i18n: :address_allotment_id: Allotment Partner, many2one

:address_allotment_id: Allotment Partner, many2one

.. i18n: :production_lot_id: Production Lot, many2one

:production_lot_id: Production Lot, many2one

.. i18n: :number_packages: Number packages, integer, readonly

:number_packages: Number packages, integer, readonly

.. i18n: :invoiced: Invoiced, boolean, readonly

:invoiced: Invoiced, boolean, readonly

.. i18n: :delay: Delivery Delay, float, required

:delay: Delivery Delay, float, required

.. i18n: :folio_id: folio_id, many2one

:folio_id: folio_id, many2one

.. i18n: :analytics_id: Analytic Distribution, many2one

:analytics_id: Analytic Distribution, many2one

.. i18n: :state: Status, selection, required, readonly

:state: Status, selection, required, readonly

.. i18n: :name: Description, char, required

:name: Description, char, required

.. i18n: :move_ids: Inventory Moves, one2many, readonly

:move_ids: Inventory Moves, one2many, readonly

.. i18n: :order_id: Order Ref, many2one, required

:order_id: Order Ref, many2one, required

.. i18n: :from_date: Start of Validity, datetime

:from_date: Start of Validity, datetime

.. i18n: :maintenance_product_qty: Maintenance Product Quantity, integer

:maintenance_product_qty: Maintenance Product Quantity, integer

.. i18n: :order_partner_id: Customer, many2one

:order_partner_id: Customer, many2one

.. i18n: :is_supplier_direct_delivery: Is Direct Delivery?, boolean

:is_supplier_direct_delivery: Is Direct Delivery?, boolean

.. i18n: :product_packaging: Packaging, many2one

:product_packaging: Packaging, many2one

.. i18n: :maintenance_start_date: Maintenance Start Date, date

:maintenance_start_date: Maintenance Start Date, date

.. i18n: :checkout_date: Check Out, datetime, required

:checkout_date: Check Out, datetime, required

.. i18n: :type: Procure Method, selection, required

:type: Procure Method, selection, required

.. i18n: :maintenance_end_date: Maintenance End Date, date

:maintenance_end_date: Maintenance End Date, date

.. i18n: :procurement_id: Procurement, many2one

:procurement_id: Procurement, many2one

.. i18n: :order_fleet_id: Default Sale Order Sub Fleet, many2one

:order_fleet_id: Default Sale Order Sub Fleet, many2one

.. i18n: :price_unit_customer: Customer Unit Price, float

:price_unit_customer: Customer Unit Price, float

.. i18n: :layout_remark: Layout Remark, text

:layout_remark: Layout Remark, text

.. i18n: :price_subtotal_incl: Subtotal, float, readonly

:price_subtotal_incl: Subtotal, float, readonly

.. i18n: :discount: Discount (%), float

:discount: Discount (%), float

.. i18n: :prodlot_id: Production lot, many2one

:prodlot_id: Production lot, many2one

.. i18n:     *Production lot is used to put a serial number on the production*

    *Production lot is used to put a serial number on the production*

.. i18n: :x: X of Product, float

:x: X of Product, float

.. i18n: :checkin_date: Check In, datetime, required

:checkin_date: Check In, datetime, required

.. i18n: :price_net: Net Price, float, readonly

:price_net: Net Price, float, readonly

.. i18n: :layout_type: Layout Type, selection, required

:layout_type: Layout Type, selection, required

.. i18n: :tax_id: Taxes, many2many

:tax_id: Taxes, many2many

.. i18n: :is_maintenance: Is Maintenance, boolean

:is_maintenance: Is Maintenance, boolean

.. i18n: :page_reference: Reference of the Page, char

:page_reference: Reference of the Page, char

.. i18n: :expected_invoice_date: Expected Invoice Date, datetime

:expected_invoice_date: Expected Invoice Date, datetime

.. i18n: :invoice_lines: Invoice Lines, many2many, readonly

:invoice_lines: Invoice Lines, many2many, readonly

.. i18n: :notes: Notes, text

:notes: Notes, text

.. i18n: :purchase_order_state: Purchase Order State, char

:purchase_order_state: Purchase Order State, char

.. i18n: :purchase_order: Related Purchase Order, many2one

:purchase_order: Related Purchase Order, many2one

.. i18n: :prodlot_ids: Lots Assignation, one2many

:prodlot_ids: Lots Assignation, one2many

.. i18n:     *Production lot is used to put a serial number on the production*

    *Production lot is used to put a serial number on the production*

.. i18n: :product_id: Product, many2one

:product_id: Product, many2one

.. i18n: :th_weight: Weight, float

:th_weight: Weight, float

.. i18n: :y: Y of Product, float

:y: Y of Product, float

.. i18n: :fleet_id: Sub Fleet, many2one

:fleet_id: Sub Fleet, many2one

.. i18n: :customer_ref: Customer reference, char

:customer_ref: Customer reference, char

.. i18n: :z: Z of Product, float

:z: Z of Product, float

.. i18n: :margin: Margin, float, readonly

:margin: Margin, float, readonly

.. i18n: :order_line_id: order_line_id, many2one, required

:order_line_id: order_line_id, many2one, required

.. i18n: :to_date: End of Validity, datetime

:to_date: End of Validity, datetime

.. i18n: Object: hotel Service line (hotel_service.line)
.. i18n: ###############################################

Object: hotel Service line (hotel_service.line)
###############################################

.. i18n: :property_ids: Properties, many2many

:property_ids: Properties, many2many

.. i18n: :product_uos_qty: Quantity (UOS), float

:product_uos_qty: Quantity (UOS), float

.. i18n: :adv_issue: Advertising Issue, many2one

:adv_issue: Advertising Issue, many2one

.. i18n: :product_uom: Product UoM, many2one, required

:product_uom: Product UoM, many2one, required

.. i18n: :sequence: Sequence Number, integer

:sequence: Sequence Number, integer

.. i18n: :parent_fleet_id: Fleet, many2one

:parent_fleet_id: Fleet, many2one

.. i18n: :price_unit: Unit Price, float, required

:price_unit: Unit Price, float, required

.. i18n: :product_uom_qty: Quantity (UoM), float, required

:product_uom_qty: Quantity (UoM), float, required

.. i18n: :price_subtotal: Subtotal w/o tax, float, readonly

:price_subtotal: Subtotal w/o tax, float, readonly

.. i18n: :maintenance_month_qty: Maintenance Month Quantity, integer, readonly

:maintenance_month_qty: Maintenance Month Quantity, integer, readonly

.. i18n: :deliveries: Planned Deliveries, float, readonly

:deliveries: Planned Deliveries, float, readonly

.. i18n: :is_supplier_direct_delivery_advised: Is Supplier Direct Delivery Advised?, boolean, readonly

:is_supplier_direct_delivery_advised: Is Supplier Direct Delivery Advised?, boolean, readonly

.. i18n: :size_x: Width, float

:size_x: Width, float

.. i18n: :size_y: Height, float

:size_y: Height, float

.. i18n: :size_z: Thickness, float

:size_z: Thickness, float

.. i18n: :product_uos: Product UOS, many2one

:product_uos: Product UOS, many2one

.. i18n: :purchase_order_line: Related Purchase Order Line, many2one

:purchase_order_line: Related Purchase Order Line, many2one

.. i18n: :address_allotment_id: Allotment Partner, many2one

:address_allotment_id: Allotment Partner, many2one

.. i18n: :production_lot_id: Production Lot, many2one

:production_lot_id: Production Lot, many2one

.. i18n: :number_packages: Number packages, integer, readonly

:number_packages: Number packages, integer, readonly

.. i18n: :invoiced: Invoiced, boolean, readonly

:invoiced: Invoiced, boolean, readonly

.. i18n: :delay: Delivery Delay, float, required

:delay: Delivery Delay, float, required

.. i18n: :folio_id: folio_id, many2one

:folio_id: folio_id, many2one

.. i18n: :analytics_id: Analytic Distribution, many2one

:analytics_id: Analytic Distribution, many2one

.. i18n: :state: Status, selection, required, readonly

:state: Status, selection, required, readonly

.. i18n: :name: Description, char, required

:name: Description, char, required

.. i18n: :move_ids: Inventory Moves, one2many, readonly

:move_ids: Inventory Moves, one2many, readonly

.. i18n: :order_id: Order Ref, many2one, required

:order_id: Order Ref, many2one, required

.. i18n: :from_date: Start of Validity, datetime

:from_date: Start of Validity, datetime

.. i18n: :maintenance_product_qty: Maintenance Product Quantity, integer

:maintenance_product_qty: Maintenance Product Quantity, integer

.. i18n: :order_partner_id: Customer, many2one

:order_partner_id: Customer, many2one

.. i18n: :is_supplier_direct_delivery: Is Direct Delivery?, boolean

:is_supplier_direct_delivery: Is Direct Delivery?, boolean

.. i18n: :product_packaging: Packaging, many2one

:product_packaging: Packaging, many2one

.. i18n: :maintenance_start_date: Maintenance Start Date, date

:maintenance_start_date: Maintenance Start Date, date

.. i18n: :type: Procure Method, selection, required

:type: Procure Method, selection, required

.. i18n: :maintenance_end_date: Maintenance End Date, date

:maintenance_end_date: Maintenance End Date, date

.. i18n: :procurement_id: Procurement, many2one

:procurement_id: Procurement, many2one

.. i18n: :order_fleet_id: Default Sale Order Sub Fleet, many2one

:order_fleet_id: Default Sale Order Sub Fleet, many2one

.. i18n: :price_unit_customer: Customer Unit Price, float

:price_unit_customer: Customer Unit Price, float

.. i18n: :layout_remark: Layout Remark, text

:layout_remark: Layout Remark, text

.. i18n: :service_line_id: service_line_id, many2one, required

:service_line_id: service_line_id, many2one, required

.. i18n: :price_subtotal_incl: Subtotal, float, readonly

:price_subtotal_incl: Subtotal, float, readonly

.. i18n: :discount: Discount (%), float

:discount: Discount (%), float

.. i18n: :prodlot_id: Production lot, many2one

:prodlot_id: Production lot, many2one

.. i18n:     *Production lot is used to put a serial number on the production*

    *Production lot is used to put a serial number on the production*

.. i18n: :x: X of Product, float

:x: X of Product, float

.. i18n: :price_net: Net Price, float, readonly

:price_net: Net Price, float, readonly

.. i18n: :layout_type: Layout Type, selection, required

:layout_type: Layout Type, selection, required

.. i18n: :tax_id: Taxes, many2many

:tax_id: Taxes, many2many

.. i18n: :is_maintenance: Is Maintenance, boolean

:is_maintenance: Is Maintenance, boolean

.. i18n: :page_reference: Reference of the Page, char

:page_reference: Reference of the Page, char

.. i18n: :expected_invoice_date: Expected Invoice Date, datetime

:expected_invoice_date: Expected Invoice Date, datetime

.. i18n: :invoice_lines: Invoice Lines, many2many, readonly

:invoice_lines: Invoice Lines, many2many, readonly

.. i18n: :notes: Notes, text

:notes: Notes, text

.. i18n: :purchase_order_state: Purchase Order State, char

:purchase_order_state: Purchase Order State, char

.. i18n: :purchase_order: Related Purchase Order, many2one

:purchase_order: Related Purchase Order, many2one

.. i18n: :prodlot_ids: Lots Assignation, one2many

:prodlot_ids: Lots Assignation, one2many

.. i18n:     *Production lot is used to put a serial number on the production*

    *Production lot is used to put a serial number on the production*

.. i18n: :product_id: Product, many2one

:product_id: Product, many2one

.. i18n: :th_weight: Weight, float

:th_weight: Weight, float

.. i18n: :y: Y of Product, float

:y: Y of Product, float

.. i18n: :fleet_id: Sub Fleet, many2one

:fleet_id: Sub Fleet, many2one

.. i18n: :customer_ref: Customer reference, char

:customer_ref: Customer reference, char

.. i18n: :z: Z of Product, float

:z: Z of Product, float

.. i18n: :margin: Margin, float, readonly

:margin: Margin, float, readonly

.. i18n: :to_date: End of Validity, datetime

:to_date: End of Validity, datetime

.. i18n: Object: Service Type (hotel.service_type)
.. i18n: #########################################

Object: Service Type (hotel.service_type)
#########################################

.. i18n: :property_account_expense_categ: Expense Account, many2one

:property_account_expense_categ: Expense Account, many2one

.. i18n:     *This account will be used, instead of the default one, to value outgoing stock for the current product category*

    *This account will be used, instead of the default one, to value outgoing stock for the current product category*

.. i18n: :property_stock_journal: Stock journal, many2one

:property_stock_journal: Stock journal, many2one

.. i18n:     *This journal will be used for the accounting move generated by stock move*

    *This journal will be used for the accounting move generated by stock move*

.. i18n: :ser_id: category, many2one, required

:ser_id: category, many2one, required

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

.. i18n: Object: Hotel Services and its charges (hotel.services)
.. i18n: #######################################################

Object: Hotel Services and its charges (hotel.services)
#######################################################

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

.. i18n: :service_id: Service_id, many2one

:service_id: Service_id, many2one

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
