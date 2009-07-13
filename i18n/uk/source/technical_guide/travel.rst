
.. i18n: .. module:: travel
.. i18n:     :synopsis: Travel 
.. i18n:     :noindex:
.. i18n: .. 

.. module:: travel
    :synopsis: Travel 
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/travel"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/travel"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Travel (*travel*)
.. i18n: =================
.. i18n: :Module: travel
.. i18n: :Name: Travel
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: travel
.. i18n: :Web: 
.. i18n: :Official module: no
.. i18n: :Quality certified: no

Travel (*travel*)
=================
:Module: travel
:Name: Travel
:Version: 5.0.1.0
:Author: Tiny
:Directory: travel
:Web: 
:Official module: no
:Quality certified: no

.. i18n: Description
.. i18n: -----------

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   None

::

  None

.. i18n: Download links
.. i18n: --------------

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:

You can download this module as a zip file in the following version:

.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/travel.zip>`_

  * `trunk <http://www.openerp.com/download/modules/trunk/travel.zip>`_

.. i18n: Dependencies
.. i18n: ------------

Dependencies
------------

.. i18n:  * :mod:`base`
.. i18n:  * :mod:`product`

 * :mod:`base`
 * :mod:`product`

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

.. i18n:  * Travel Agency
.. i18n:  * Travel Agency/Hostels
.. i18n:  * Travel Agency/Rooms
.. i18n:  * Travel Agency/Rooms/Single Rooms
.. i18n:  * Travel Agency/Rooms/Double Rooms
.. i18n:  * Travel Agency/Airports
.. i18n:  * Travel Agency/Flights

 * Travel Agency
 * Travel Agency/Hostels
 * Travel Agency/Rooms
 * Travel Agency/Rooms/Single Rooms
 * Travel Agency/Rooms/Double Rooms
 * Travel Agency/Airports
 * Travel Agency/Flights

.. i18n: Views
.. i18n: -----

Views
-----

.. i18n:  * travel.flight (form)
.. i18n:  * travel.room (form)
.. i18n:  * travel.room (tree)
.. i18n:  * travel.hostel (form)

 * travel.flight (form)
 * travel.room (form)
 * travel.room (tree)
 * travel.hostel (form)

.. i18n: Objects
.. i18n: -------

Objects
-------

.. i18n: Object: Partner (travel.hostel)
.. i18n: ###############################

Object: Partner (travel.hostel)
###############################

.. i18n: :comment: Notes, text

:comment: Notes, text

.. i18n: :ean13: EAN, char

:ean13: EAN, char

.. i18n:     *Barcode number for EAN8 EAN13 UPC JPC GTIN*

    *Barcode number for EAN8 EAN13 UPC JPC GTIN*

.. i18n: :property_account_position: Fiscal Position, many2one

:property_account_position: Fiscal Position, many2one

.. i18n:     *The fiscal position will determine taxes and the accounts used for the the partner.*

    *The fiscal position will determine taxes and the accounts used for the the partner.*

.. i18n: :vat_no: VAT Number, char

:vat_no: VAT Number, char

.. i18n: :excise: Exices Number, char

:excise: Exices Number, char

.. i18n: :ref_companies: Companies that refers to partner, one2many

:ref_companies: Companies that refers to partner, one2many

.. i18n: :relation_ids: Relations, one2many

:relation_ids: Relations, one2many

.. i18n: :date: Date, date

:date: Date, date

.. i18n: :logo: Logo, binary

:logo: Logo, binary

.. i18n: :property_product_pricelist: Sale Pricelist, many2one

:property_product_pricelist: Sale Pricelist, many2one

.. i18n:     *This pricelist will be used, instead of the default one,                     for sales to the current partner*

    *This pricelist will be used, instead of the default one,                     for sales to the current partner*

.. i18n: :quality: Quality, char

:quality: Quality, char

.. i18n: :city: City, char

:city: City, char

.. i18n: :user_id: Dedicated Salesman, many2one

:user_id: Dedicated Salesman, many2one

.. i18n:     *The internal user that is in charge of communicating with this partner if any.*

    *The internal user that is in charge of communicating with this partner if any.*

.. i18n: :title: Title, selection

:title: Title, selection

.. i18n: :pan_no: PAN Number, char

:pan_no: PAN Number, char

.. i18n: :debit_limit: Payable Limit, float

:debit_limit: Payable Limit, float

.. i18n: :participation_ids: Participations, one2many

:participation_ids: Participations, one2many

.. i18n: :property_account_payable: Account Payable, many2one, required

:property_account_payable: Account Payable, many2one, required

.. i18n:     *This account will be used instead of the default one as the payable account for the current partner*

    *This account will be used instead of the default one as the payable account for the current partner*

.. i18n: :parent_id: Main Company, many2one

:parent_id: Main Company, many2one

.. i18n: :debit: Total Payable, float, readonly

:debit: Total Payable, float, readonly

.. i18n:     *Total amount you have to pay to this supplier.*

    *Total amount you have to pay to this supplier.*

.. i18n: :supplier: Supplier, boolean

:supplier: Supplier, boolean

.. i18n:     *Check this box if the partner is a supplier. If it's not checked, purchase people will not see it when encoding a purchase order.*

    *Check this box if the partner is a supplier. If it's not checked, purchase people will not see it when encoding a purchase order.*

.. i18n: :turnover_id: Turnover, one2many

:turnover_id: Turnover, one2many

.. i18n: :ref: Code, char, readonly

:ref: Code, char, readonly

.. i18n: :events: Events, one2many

:events: Events, one2many

.. i18n: :vat: VAT, char

:vat: VAT, char

.. i18n:     *Value Added Tax number. Check the box if the partner is subjected to the VAT. Used by the VAT legal statement.*

    *Value Added Tax number. Check the box if the partner is subjected to the VAT. Used by the VAT legal statement.*

.. i18n: :rooms_id: Rooms, one2many

:rooms_id: Rooms, one2many

.. i18n: :customer: Customer, boolean

:customer: Customer, boolean

.. i18n:     *Check this box if the partner is a customer.*

    *Check this box if the partner is a customer.*

.. i18n: :website: Website, char

:website: Website, char

.. i18n: :bank_ids: Banks, one2many

:bank_ids: Banks, one2many

.. i18n: :signature: Signature, binary

:signature: Signature, binary

.. i18n: :child_ids: Partner Ref., one2many

:child_ids: Partner Ref., one2many

.. i18n: :address: Contacts, one2many

:address: Contacts, one2many

.. i18n: :active: Active, boolean

:active: Active, boolean

.. i18n: :answers_ids: Answers, many2many

:answers_ids: Answers, many2many

.. i18n: :partner_ids: Parent Companies, one2many

:partner_ids: Parent Companies, one2many

.. i18n: :cst_no: CST Number, char

:cst_no: CST Number, char

.. i18n: :lang: Language, selection

:lang: Language, selection

.. i18n:     *If the selected language is loaded in the system, all documents related to this partner will be printed in this language. If not, it will be english.*

    *If the selected language is loaded in the system, all documents related to this partner will be printed in this language. If not, it will be english.*

.. i18n: :credit_limit: Credit Limit, float

:credit_limit: Credit Limit, float

.. i18n: :name: Name, char, required

:name: Name, char, required

.. i18n: :header: Header (.odt), binary

:header: Header (.odt), binary

.. i18n: :country: Country, many2one

:country: Country, many2one

.. i18n: :property_account_receivable: Account Receivable, many2one, required

:property_account_receivable: Account Receivable, many2one, required

.. i18n:     *This account will be used instead of the default one as the receivable account for the current partner*

    *This account will be used instead of the default one as the receivable account for the current partner*

.. i18n: :credit: Total Receivable, float, readonly

:credit: Total Receivable, float, readonly

.. i18n:     *Total amount this customer owes you.*

    *Total amount this customer owes you.*

.. i18n: :range: Range, char

:range: Range, char

.. i18n: :ser_tax: Service Tax Number, char

:ser_tax: Service Tax Number, char

.. i18n: :property_payment_term: Payment Term, many2one

:property_payment_term: Payment Term, many2one

.. i18n:     *This payment term will be used instead of the default one for the current partner*

    *This payment term will be used instead of the default one for the current partner*

.. i18n: :div: Division, char

:div: Division, char

.. i18n: :category_id: Categories, many2many

:category_id: Categories, many2many

.. i18n: Object: travel.airport (travel.airport)
.. i18n: #######################################

Object: travel.airport (travel.airport)
#######################################

.. i18n: :city: City, char

:city: City, char

.. i18n: :name: Airport name, char

:name: Airport name, char

.. i18n: :country: Country, many2one

:country: Country, many2one

.. i18n: Object: Product (travel.room)
.. i18n: #############################

Object: Product (travel.room)
#############################

.. i18n: :warranty: Warranty (months), float

:warranty: Warranty (months), float

.. i18n: :property_stock_procurement: Procurement Location, many2one

:property_stock_procurement: Procurement Location, many2one

.. i18n:     *For the current product (template), this stock location will be used, instead of the default one, as the source location for stock moves generated by procurements*

    *For the current product (template), this stock location will be used, instead of the default one, as the source location for stock moves generated by procurements*

.. i18n: :supply_method: Supply method, selection, required

:supply_method: Supply method, selection, required

.. i18n:     *Produce will generate production order or tasks, according to the product type. Purchase will trigger purchase orders when requested.*

    *Produce will generate production order or tasks, according to the product type. Purchase will trigger purchase orders when requested.*

.. i18n: :uos_id: Unit of Sale, many2one

:uos_id: Unit of Sale, many2one

.. i18n:     *Used by companies that manages two unit of measure: invoicing and stock management. For example, in food industries, you will manage a stock of ham but invoice in Kg. Keep empty to use the default UOM.*

    *Used by companies that manages two unit of measure: invoicing and stock management. For example, in food industries, you will manage a stock of ham but invoice in Kg. Keep empty to use the default UOM.*

.. i18n: :list_price: Sale Price, float

:list_price: Sale Price, float

.. i18n:     *Base price for computing the customer price. Sometimes called the catalog price.*

    *Base price for computing the customer price. Sometimes called the catalog price.*

.. i18n: :weight: Gross weight, float

:weight: Gross weight, float

.. i18n:     *The gross weight in Kg.*

    *The gross weight in Kg.*

.. i18n: :ean13: EAN, char

:ean13: EAN, char

.. i18n:     *Barcode number for EAN8 EAN13 UPC JPC GTIN http://de.wikipedia.org/wiki/Global_Trade_Item_Number*

    *Barcode number for EAN8 EAN13 UPC JPC GTIN http://de.wikipedia.org/wiki/Global_Trade_Item_Number*

.. i18n: :incoming_qty: Incoming, float, readonly

:incoming_qty: Incoming, float, readonly

.. i18n: :standard_price: Cost Price, float, required

:standard_price: Cost Price, float, required

.. i18n:     *The cost of the product for accounting stock valuation. It can serves as a base price for supplier price.*

    *The cost of the product for accounting stock valuation. It can serves as a base price for supplier price.*

.. i18n: :member_price: Member Price, float

:member_price: Member Price, float

.. i18n: :price_extra: Variant Price Extra, float

:price_extra: Variant Price Extra, float

.. i18n: :mes_type: Measure Type, selection, required

:mes_type: Measure Type, selection, required

.. i18n: :uom_id: Default UoM, many2one, required

:uom_id: Default UoM, many2one, required

.. i18n:     *Default Unit of Measure used for all stock operation.*

    *Default Unit of Measure used for all stock operation.*

.. i18n: :hostel_id: Hostel, many2one

:hostel_id: Hostel, many2one

.. i18n: :code: Code, char, readonly

:code: Code, char, readonly

.. i18n: :description_purchase: Purchase Description, text

:description_purchase: Purchase Description, text

.. i18n: :default_code: Code, char

:default_code: Code, char

.. i18n: :property_account_income: Income Account, many2one

:property_account_income: Income Account, many2one

.. i18n:     *This account will be used instead of the default one to value incoming stock for the current product*

    *This account will be used instead of the default one to value incoming stock for the current product*

.. i18n: :qty_available: Real Stock, float, readonly

:qty_available: Real Stock, float, readonly

.. i18n: :price: Customer Price, float, readonly

:price: Customer Price, float, readonly

.. i18n: :index_sale: Sales indexes, many2many

:index_sale: Sales indexes, many2many

.. i18n: :variants: Variants, char

:variants: Variants, char

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

.. i18n: :product_tmpl_id: Product Template, many2one, required

:product_tmpl_id: Product Template, many2one, required

.. i18n: :virtual_available: Virtual Stock, float, readonly

:virtual_available: Virtual Stock, float, readonly

.. i18n: :sale_ok: Can be sold, boolean

:sale_ok: Can be sold, boolean

.. i18n:     *Determine if the product can be visible in the list of product within a selection from a sale order line.*

    *Determine if the product can be visible in the list of product within a selection from a sale order line.*

.. i18n: :life_cycle: Life Cycle, selection

:life_cycle: Life Cycle, selection

.. i18n: :purchase_ok: Can be Purchased, boolean

:purchase_ok: Can be Purchased, boolean

.. i18n:     *Determine if the product is visible in the list of products within a selection from a purchase order line.*

    *Determine if the product is visible in the list of products within a selection from a purchase order line.*

.. i18n: :product_manager: Product Manager, many2one

:product_manager: Product Manager, many2one

.. i18n: :characteristic_group_ids: Characteristic groups, many2many

:characteristic_group_ids: Characteristic groups, many2many

.. i18n: :company_id: Company, many2one

:company_id: Company, many2one

.. i18n: :name: Name, char, required

:name: Name, char, required

.. i18n: :active: Active, boolean

:active: Active, boolean

.. i18n: :state: Status, selection

:state: Status, selection

.. i18n:     *Tells the user if he can use the product or not.*

    *Tells the user if he can use the product or not.*

.. i18n: :property_account_income_world: Outside Europe Income Account, many2one

:property_account_income_world: Outside Europe Income Account, many2one

.. i18n:     *This account will be used, instead of the default one, to value incoming stock for the current product*

    *This account will be used, instead of the default one, to value incoming stock for the current product*

.. i18n: :loc_rack: Rack, char

:loc_rack: Rack, char

.. i18n: :rough_drawing: rough drawing, binary

:rough_drawing: rough drawing, binary

.. i18n: :standard_price_index: Indexed standard price, float, readonly

:standard_price_index: Indexed standard price, float, readonly

.. i18n: :series: Series, many2one

:series: Series, many2one

.. i18n: :uom_po_id: Purchase UoM, many2one, required

:uom_po_id: Purchase UoM, many2one, required

.. i18n:     *Default Unit of Measure used for purchase orders. It must in the same category than the default unit of measure.*

    *Default Unit of Measure used for purchase orders. It must in the same category than the default unit of measure.*

.. i18n: :intrastat_id: Intrastat code, many2one

:intrastat_id: Intrastat code, many2one

.. i18n: :type: Product Type, selection, required

:type: Product Type, selection, required

.. i18n:     *Will change the way procurements are processed. Consumables are stockable products with infinite stock, or for use when you have no stock management in the system.*

    *Will change the way procurements are processed. Consumables are stockable products with infinite stock, or for use when you have no stock management in the system.*

.. i18n: :property_stock_account_input: Stock Input Account, many2one

:property_stock_account_input: Stock Input Account, many2one

.. i18n:     *This account will be used, instead of the default one, to value input stock*

    *This account will be used, instead of the default one, to value input stock*

.. i18n: :property_account_income_europe: Income Account for Europe, many2one

:property_account_income_europe: Income Account for Europe, many2one

.. i18n:     *This account will be used, instead of the default one, to value incoming stock for the current product*

    *This account will be used, instead of the default one, to value incoming stock for the current product*

.. i18n: :schema: schema, binary

:schema: schema, binary

.. i18n: :picture: Image, binary

:picture: Image, binary

.. i18n: :description: Description, text

:description: Description, text

.. i18n: :list_price_index: Indexed list price, float, readonly

:list_price_index: Indexed list price, float, readonly

.. i18n: :property_account_expense_europe: Expense Account for Europe, many2one

:property_account_expense_europe: Expense Account for Europe, many2one

.. i18n:     *This account will be used, instead of the default one, to value outgoing stock for the current product*

    *This account will be used, instead of the default one, to value outgoing stock for the current product*

.. i18n: :weight_net: Net weight, float

:weight_net: Net weight, float

.. i18n:     *The net weight in Kg.*

    *The net weight in Kg.*

.. i18n: :property_stock_production: Production Location, many2one

:property_stock_production: Production Location, many2one

.. i18n:     *For the current product (template), this stock location will be used, instead of the default one, as the source location for stock moves generated by production orders*

    *For the current product (template), this stock location will be used, instead of the default one, as the source location for stock moves generated by production orders*

.. i18n: :index_date: Index price date, date, required

:index_date: Index price date, date, required

.. i18n: :partner_ref2: Customer ref, char, readonly

:partner_ref2: Customer ref, char, readonly

.. i18n: :supplier_taxes_id: Supplier Taxes, many2many

:supplier_taxes_id: Supplier Taxes, many2many

.. i18n: :volume: Volume, float

:volume: Volume, float

.. i18n:     *The volume in m3.*

    *The volume in m3.*

.. i18n: :outgoing_qty: Outgoing, float, readonly

:outgoing_qty: Outgoing, float, readonly

.. i18n: :dimension_type_ids: Dimension Types, one2many

:dimension_type_ids: Dimension Types, one2many

.. i18n: :description_sale: Sale Description, text

:description_sale: Sale Description, text

.. i18n: :procure_method: Procure Method, selection, required

:procure_method: Procure Method, selection, required

.. i18n:     *'Make to Stock': When needed, take from the stock or wait until re-supplying. 'Make to Order': When needed, purchase or produce for the procurement request.*

    *'Make to Stock': When needed, take from the stock or wait until re-supplying. 'Make to Order': When needed, purchase or produce for the procurement request.*

.. i18n: :property_stock_inventory: Inventory Location, many2one

:property_stock_inventory: Inventory Location, many2one

.. i18n:     *For the current product (template), this stock location will be used, instead of the default one, as the source location for stock moves generated when you do an inventory*

    *For the current product (template), this stock location will be used, instead of the default one, as the source location for stock moves generated when you do an inventory*

.. i18n: :cost_method: Costing Method, selection, required

:cost_method: Costing Method, selection, required

.. i18n:     *Standard Price: the cost price is fixed and recomputed periodically (usually at the end of the year), Average Price: the cost price is recomputed at each reception of products.*

    *Standard Price: the cost price is fixed and recomputed periodically (usually at the end of the year), Average Price: the cost price is recomputed at each reception of products.*

.. i18n: :partner_ref: Customer ref, char, readonly

:partner_ref: Customer ref, char, readonly

.. i18n: :loc_row: Row, char

:loc_row: Row, char

.. i18n: :seller_delay: Supplier Lead Time, integer, readonly

:seller_delay: Supplier Lead Time, integer, readonly

.. i18n:     *This is the average delay in days between the purchase order confirmation and the reception of goods for this product and for the default supplier. It is used by the scheduler to order requests based on reordering delays.*

    *This is the average delay in days between the purchase order confirmation and the reception of goods for this product and for the default supplier. It is used by the scheduler to order requests based on reordering delays.*

.. i18n: :rental: Rentable Product, boolean

:rental: Rentable Product, boolean

.. i18n: :packaging: Logistical Units, one2many

:packaging: Logistical Units, one2many

.. i18n:     *Gives the different ways to package the same product. This has no impact on the packing order and is mainly used if you use the EDI module.*

    *Gives the different ways to package the same product. This has no impact on the packing order and is mainly used if you use the EDI module.*

.. i18n: :sale_delay: Customer Lead Time, float

:sale_delay: Customer Lead Time, float

.. i18n:     *This is the average time between the confirmation of the customer order and the delivery of the finished products. It's the time you promise to your customers.*

    *This is the average time between the confirmation of the customer order and the delivery of the finished products. It's the time you promise to your customers.*

.. i18n: :index_purchase: Purchase indexes, many2many

:index_purchase: Purchase indexes, many2many

.. i18n: :loc_case: Case, char

:loc_case: Case, char

.. i18n: :produce_delay: Manufacturing Lead Time, float

:produce_delay: Manufacturing Lead Time, float

.. i18n:     *Average time to produce this product. This is only for the production order and, if it is a multi-level bill of material, it's only for the level of this product. Different delays will be summed for all levels and purchase orders.*

    *Average time to produce this product. This is only for the production order and, if it is a multi-level bill of material, it's only for the level of this product. Different delays will be summed for all levels and purchase orders.*

.. i18n: :property_account_expense: Expense Account, many2one

:property_account_expense: Expense Account, many2one

.. i18n:     *This account will be used instead of the default one to value outgoing stock for the current product*

    *This account will be used instead of the default one to value outgoing stock for the current product*

.. i18n: :buyer_price_index: Indexed buyer price, float, readonly

:buyer_price_index: Indexed buyer price, float, readonly

.. i18n: :categ_id: Category, many2one, required

:categ_id: Category, many2one, required

.. i18n: :variant_ids: Variants, one2many

:variant_ids: Variants, one2many

.. i18n: :beds: Nbr of Beds, integer

:beds: Nbr of Beds, integer

.. i18n: :lst_price: List Price, float, readonly

:lst_price: List Price, float, readonly

.. i18n: :taxes_id: Product Taxes, many2many

:taxes_id: Product Taxes, many2many

.. i18n: :property_stock_account_output: Stock Output Account, many2one

:property_stock_account_output: Stock Output Account, many2one

.. i18n:     *This account will be used, instead of the default one, to value output stock*

    *This account will be used, instead of the default one, to value output stock*

.. i18n: :seller_ids: Partners, one2many

:seller_ids: Partners, one2many

.. i18n: :view: Room View, selection

:view: Room View, selection

.. i18n: :buyer_price: Buyer price, float

:buyer_price: Buyer price, float

.. i18n: :price_margin: Variant Price Margin, float

:price_margin: Variant Price Margin, float

.. i18n: Object: Product (travel.flight)
.. i18n: ###############################

Object: Product (travel.flight)
###############################

.. i18n: :warranty: Warranty (months), float

:warranty: Warranty (months), float

.. i18n: :property_stock_procurement: Procurement Location, many2one

:property_stock_procurement: Procurement Location, many2one

.. i18n:     *For the current product (template), this stock location will be used, instead of the default one, as the source location for stock moves generated by procurements*

    *For the current product (template), this stock location will be used, instead of the default one, as the source location for stock moves generated by procurements*

.. i18n: :supply_method: Supply method, selection, required

:supply_method: Supply method, selection, required

.. i18n:     *Produce will generate production order or tasks, according to the product type. Purchase will trigger purchase orders when requested.*

    *Produce will generate production order or tasks, according to the product type. Purchase will trigger purchase orders when requested.*

.. i18n: :uos_id: Unit of Sale, many2one

:uos_id: Unit of Sale, many2one

.. i18n:     *Used by companies that manages two unit of measure: invoicing and stock management. For example, in food industries, you will manage a stock of ham but invoice in Kg. Keep empty to use the default UOM.*

    *Used by companies that manages two unit of measure: invoicing and stock management. For example, in food industries, you will manage a stock of ham but invoice in Kg. Keep empty to use the default UOM.*

.. i18n: :list_price: Sale Price, float

:list_price: Sale Price, float

.. i18n:     *Base price for computing the customer price. Sometimes called the catalog price.*

    *Base price for computing the customer price. Sometimes called the catalog price.*

.. i18n: :weight: Gross weight, float

:weight: Gross weight, float

.. i18n:     *The gross weight in Kg.*

    *The gross weight in Kg.*

.. i18n: :ean13: EAN, char

:ean13: EAN, char

.. i18n:     *Barcode number for EAN8 EAN13 UPC JPC GTIN http://de.wikipedia.org/wiki/Global_Trade_Item_Number*

    *Barcode number for EAN8 EAN13 UPC JPC GTIN http://de.wikipedia.org/wiki/Global_Trade_Item_Number*

.. i18n: :incoming_qty: Incoming, float, readonly

:incoming_qty: Incoming, float, readonly

.. i18n: :standard_price: Cost Price, float, required

:standard_price: Cost Price, float, required

.. i18n:     *The cost of the product for accounting stock valuation. It can serves as a base price for supplier price.*

    *The cost of the product for accounting stock valuation. It can serves as a base price for supplier price.*

.. i18n: :member_price: Member Price, float

:member_price: Member Price, float

.. i18n: :price_extra: Variant Price Extra, float

:price_extra: Variant Price Extra, float

.. i18n: :mes_type: Measure Type, selection, required

:mes_type: Measure Type, selection, required

.. i18n: :uom_id: Default UoM, many2one, required

:uom_id: Default UoM, many2one, required

.. i18n:     *Default Unit of Measure used for all stock operation.*

    *Default Unit of Measure used for all stock operation.*

.. i18n: :code: Code, char, readonly

:code: Code, char, readonly

.. i18n: :description_purchase: Purchase Description, text

:description_purchase: Purchase Description, text

.. i18n: :default_code: Code, char

:default_code: Code, char

.. i18n: :property_account_income: Income Account, many2one

:property_account_income: Income Account, many2one

.. i18n:     *This account will be used instead of the default one to value incoming stock for the current product*

    *This account will be used instead of the default one to value incoming stock for the current product*

.. i18n: :qty_available: Real Stock, float, readonly

:qty_available: Real Stock, float, readonly

.. i18n: :price: Customer Price, float, readonly

:price: Customer Price, float, readonly

.. i18n: :partner_id: PArtner, many2one

:partner_id: PArtner, many2one

.. i18n: :variants: Variants, char

:variants: Variants, char

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

.. i18n: :product_tmpl_id: Product Template, many2one, required

:product_tmpl_id: Product Template, many2one, required

.. i18n: :date: Departure Date, datetime

:date: Departure Date, datetime

.. i18n: :sale_ok: Can be sold, boolean

:sale_ok: Can be sold, boolean

.. i18n:     *Determine if the product can be visible in the list of product within a selection from a sale order line.*

    *Determine if the product can be visible in the list of product within a selection from a sale order line.*

.. i18n: :life_cycle: Life Cycle, selection

:life_cycle: Life Cycle, selection

.. i18n: :purchase_ok: Can be Purchased, boolean

:purchase_ok: Can be Purchased, boolean

.. i18n:     *Determine if the product is visible in the list of products within a selection from a purchase order line.*

    *Determine if the product is visible in the list of products within a selection from a purchase order line.*

.. i18n: :product_manager: Product Manager, many2one

:product_manager: Product Manager, many2one

.. i18n: :characteristic_group_ids: Characteristic groups, many2many

:characteristic_group_ids: Characteristic groups, many2many

.. i18n: :company_id: Company, many2one

:company_id: Company, many2one

.. i18n: :name: Name, char, required

:name: Name, char, required

.. i18n: :active: Active, boolean

:active: Active, boolean

.. i18n: :state: Status, selection

:state: Status, selection

.. i18n:     *Tells the user if he can use the product or not.*

    *Tells the user if he can use the product or not.*

.. i18n: :property_account_income_world: Outside Europe Income Account, many2one

:property_account_income_world: Outside Europe Income Account, many2one

.. i18n:     *This account will be used, instead of the default one, to value incoming stock for the current product*

    *This account will be used, instead of the default one, to value incoming stock for the current product*

.. i18n: :loc_rack: Rack, char

:loc_rack: Rack, char

.. i18n: :rough_drawing: rough drawing, binary

:rough_drawing: rough drawing, binary

.. i18n: :standard_price_index: Indexed standard price, float, readonly

:standard_price_index: Indexed standard price, float, readonly

.. i18n: :series: Series, many2one

:series: Series, many2one

.. i18n: :uom_po_id: Purchase UoM, many2one, required

:uom_po_id: Purchase UoM, many2one, required

.. i18n:     *Default Unit of Measure used for purchase orders. It must in the same category than the default unit of measure.*

    *Default Unit of Measure used for purchase orders. It must in the same category than the default unit of measure.*

.. i18n: :intrastat_id: Intrastat code, many2one

:intrastat_id: Intrastat code, many2one

.. i18n: :type: Product Type, selection, required

:type: Product Type, selection, required

.. i18n:     *Will change the way procurements are processed. Consumables are stockable products with infinite stock, or for use when you have no stock management in the system.*

    *Will change the way procurements are processed. Consumables are stockable products with infinite stock, or for use when you have no stock management in the system.*

.. i18n: :property_stock_account_input: Stock Input Account, many2one

:property_stock_account_input: Stock Input Account, many2one

.. i18n:     *This account will be used, instead of the default one, to value input stock*

    *This account will be used, instead of the default one, to value input stock*

.. i18n: :property_account_income_europe: Income Account for Europe, many2one

:property_account_income_europe: Income Account for Europe, many2one

.. i18n:     *This account will be used, instead of the default one, to value incoming stock for the current product*

    *This account will be used, instead of the default one, to value incoming stock for the current product*

.. i18n: :schema: schema, binary

:schema: schema, binary

.. i18n: :picture: Image, binary

:picture: Image, binary

.. i18n: :virtual_available: Virtual Stock, float, readonly

:virtual_available: Virtual Stock, float, readonly

.. i18n: :description: Description, text

:description: Description, text

.. i18n: :list_price_index: Indexed list price, float, readonly

:list_price_index: Indexed list price, float, readonly

.. i18n: :property_account_expense_europe: Expense Account for Europe, many2one

:property_account_expense_europe: Expense Account for Europe, many2one

.. i18n:     *This account will be used, instead of the default one, to value outgoing stock for the current product*

    *This account will be used, instead of the default one, to value outgoing stock for the current product*

.. i18n: :weight_net: Net weight, float

:weight_net: Net weight, float

.. i18n:     *The net weight in Kg.*

    *The net weight in Kg.*

.. i18n: :property_stock_production: Production Location, many2one

:property_stock_production: Production Location, many2one

.. i18n:     *For the current product (template), this stock location will be used, instead of the default one, as the source location for stock moves generated by production orders*

    *For the current product (template), this stock location will be used, instead of the default one, as the source location for stock moves generated by production orders*

.. i18n: :index_date: Index price date, date, required

:index_date: Index price date, date, required

.. i18n: :partner_ref2: Customer ref, char, readonly

:partner_ref2: Customer ref, char, readonly

.. i18n: :supplier_taxes_id: Supplier Taxes, many2many

:supplier_taxes_id: Supplier Taxes, many2many

.. i18n: :volume: Volume, float

:volume: Volume, float

.. i18n:     *The volume in m3.*

    *The volume in m3.*

.. i18n: :airport_from: Airport Departure, many2one

:airport_from: Airport Departure, many2one

.. i18n: :outgoing_qty: Outgoing, float, readonly

:outgoing_qty: Outgoing, float, readonly

.. i18n: :dimension_type_ids: Dimension Types, one2many

:dimension_type_ids: Dimension Types, one2many

.. i18n: :description_sale: Sale Description, text

:description_sale: Sale Description, text

.. i18n: :procure_method: Procure Method, selection, required

:procure_method: Procure Method, selection, required

.. i18n:     *'Make to Stock': When needed, take from the stock or wait until re-supplying. 'Make to Order': When needed, purchase or produce for the procurement request.*

    *'Make to Stock': When needed, take from the stock or wait until re-supplying. 'Make to Order': When needed, purchase or produce for the procurement request.*

.. i18n: :property_stock_inventory: Inventory Location, many2one

:property_stock_inventory: Inventory Location, many2one

.. i18n:     *For the current product (template), this stock location will be used, instead of the default one, as the source location for stock moves generated when you do an inventory*

    *For the current product (template), this stock location will be used, instead of the default one, as the source location for stock moves generated when you do an inventory*

.. i18n: :cost_method: Costing Method, selection, required

:cost_method: Costing Method, selection, required

.. i18n:     *Standard Price: the cost price is fixed and recomputed periodically (usually at the end of the year), Average Price: the cost price is recomputed at each reception of products.*

    *Standard Price: the cost price is fixed and recomputed periodically (usually at the end of the year), Average Price: the cost price is recomputed at each reception of products.*

.. i18n: :partner_ref: Customer ref, char, readonly

:partner_ref: Customer ref, char, readonly

.. i18n: :loc_row: Row, char

:loc_row: Row, char

.. i18n: :seller_delay: Supplier Lead Time, integer, readonly

:seller_delay: Supplier Lead Time, integer, readonly

.. i18n:     *This is the average delay in days between the purchase order confirmation and the reception of goods for this product and for the default supplier. It is used by the scheduler to order requests based on reordering delays.*

    *This is the average delay in days between the purchase order confirmation and the reception of goods for this product and for the default supplier. It is used by the scheduler to order requests based on reordering delays.*

.. i18n: :rental: Rentable Product, boolean

:rental: Rentable Product, boolean

.. i18n: :packaging: Logistical Units, one2many

:packaging: Logistical Units, one2many

.. i18n:     *Gives the different ways to package the same product. This has no impact on the packing order and is mainly used if you use the EDI module.*

    *Gives the different ways to package the same product. This has no impact on the packing order and is mainly used if you use the EDI module.*

.. i18n: :sale_delay: Customer Lead Time, float

:sale_delay: Customer Lead Time, float

.. i18n:     *This is the average time between the confirmation of the customer order and the delivery of the finished products. It's the time you promise to your customers.*

    *This is the average time between the confirmation of the customer order and the delivery of the finished products. It's the time you promise to your customers.*

.. i18n: :index_purchase: Purchase indexes, many2many

:index_purchase: Purchase indexes, many2many

.. i18n: :loc_case: Case, char

:loc_case: Case, char

.. i18n: :produce_delay: Manufacturing Lead Time, float

:produce_delay: Manufacturing Lead Time, float

.. i18n:     *Average time to produce this product. This is only for the production order and, if it is a multi-level bill of material, it's only for the level of this product. Different delays will be summed for all levels and purchase orders.*

    *Average time to produce this product. This is only for the production order and, if it is a multi-level bill of material, it's only for the level of this product. Different delays will be summed for all levels and purchase orders.*

.. i18n: :property_account_expense: Expense Account, many2one

:property_account_expense: Expense Account, many2one

.. i18n:     *This account will be used instead of the default one to value outgoing stock for the current product*

    *This account will be used instead of the default one to value outgoing stock for the current product*

.. i18n: :buyer_price_index: Indexed buyer price, float, readonly

:buyer_price_index: Indexed buyer price, float, readonly

.. i18n: :categ_id: Category, many2one, required

:categ_id: Category, many2one, required

.. i18n: :variant_ids: Variants, one2many

:variant_ids: Variants, one2many

.. i18n: :lst_price: List Price, float, readonly

:lst_price: List Price, float, readonly

.. i18n: :taxes_id: Product Taxes, many2many

:taxes_id: Product Taxes, many2many

.. i18n: :property_stock_account_output: Stock Output Account, many2one

:property_stock_account_output: Stock Output Account, many2one

.. i18n:     *This account will be used, instead of the default one, to value output stock*

    *This account will be used, instead of the default one, to value output stock*

.. i18n: :seller_ids: Partners, one2many

:seller_ids: Partners, one2many

.. i18n: :airport_to: Airport Arrival, many2one

:airport_to: Airport Arrival, many2one

.. i18n: :index_sale: Sales indexes, many2many

:index_sale: Sales indexes, many2many

.. i18n: :buyer_price: Buyer price, float

:buyer_price: Buyer price, float

.. i18n: :price_margin: Variant Price Margin, float

:price_margin: Variant Price Margin, float
