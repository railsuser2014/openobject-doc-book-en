
.. i18n: .. module:: product
.. i18n:     :synopsis: Products & Pricelists (Official, Quality Certified)
.. i18n:     :noindex:
.. i18n: .. 

.. module:: product
    :synopsis: Products & Pricelists (Official, Quality Certified)
    :noindex:
.. 

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. i18n: Products & Pricelists (*product*)
.. i18n: =================================
.. i18n: :Module: product
.. i18n: :Name: Products & Pricelists
.. i18n: :Version: 5.0.1.1
.. i18n: :Author: Tiny
.. i18n: :Directory: product
.. i18n: :Web: 
.. i18n: :Official module: yes
.. i18n: :Quality certified: yes

Products & Pricelists (*product*)
=================================
:Module: product
:Name: Products & Pricelists
:Version: 5.0.1.1
:Author: Tiny
:Directory: product
:Web: 
:Official module: yes
:Quality certified: yes

.. i18n: Description
.. i18n: -----------

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   This is the base module to manage products and pricelists in Open ERP.
.. i18n:   
.. i18n:       Products support variants, different pricing methods, suppliers
.. i18n:       information, make to stock/order, different unit of measures,
.. i18n:       packagings and properties.
.. i18n:   
.. i18n:       Pricelists supports:
.. i18n:       * Multiple-level of discount (by product, category, quantities)
.. i18n:       * Compute price based on different criteria:
.. i18n:           * Other pricelist,
.. i18n:           * Cost price,
.. i18n:           * List price,
.. i18n:           * Supplier price, ...
.. i18n:       Pricelists preferences by product and/or partners.
.. i18n:   
.. i18n:       Print product labels with barcode.

::

  This is the base module to manage products and pricelists in Open ERP.
  
      Products support variants, different pricing methods, suppliers
      information, make to stock/order, different unit of measures,
      packagings and properties.
  
      Pricelists supports:
      * Multiple-level of discount (by product, category, quantities)
      * Compute price based on different criteria:
          * Other pricelist,
          * Cost price,
          * List price,
          * Supplier price, ...
      Pricelists preferences by product and/or partners.
  
      Print product labels with barcode.

.. i18n: Dependencies
.. i18n: ------------

Dependencies
------------

.. i18n:  * :mod:`base`
.. i18n:  * :mod:`process`

 * :mod:`base`
 * :mod:`process`

.. i18n: Reports
.. i18n: -------

Reports
-------

.. i18n:  * Products Labels

 * Products Labels

.. i18n: Menus
.. i18n: -------

Menus
-------

.. i18n:  * Books
.. i18n:  * Books/Configuration
.. i18n:  * Books/Products
.. i18n:  * Books/Products by Category
.. i18n:  * Books/Configuration/Products Categories
.. i18n:  * Books/Configuration/Units of Measure
.. i18n:  * Books/Configuration/Units of Measure/Units of Measure
.. i18n:  * Books/Configuration/Units of Measure/Units of Measure Categories
.. i18n:  * Books/Configuration/Packagings
.. i18n:  * Books/Pricelists
.. i18n:  * Books/Pricelists/Pricelist Versions
.. i18n:  * Books/Pricelists/Pricelists
.. i18n:  * Books/Configuration/Prices Computations
.. i18n:  * Books/Configuration/Prices Computations/Prices Types
.. i18n:  * Books/Configuration/Prices Computations/Pricelists Types

 * Books
 * Books/Configuration
 * Books/Products
 * Books/Products by Category
 * Books/Configuration/Products Categories
 * Books/Configuration/Units of Measure
 * Books/Configuration/Units of Measure/Units of Measure
 * Books/Configuration/Units of Measure/Units of Measure Categories
 * Books/Configuration/Packagings
 * Books/Pricelists
 * Books/Pricelists/Pricelist Versions
 * Books/Pricelists/Pricelists
 * Books/Configuration/Prices Computations
 * Books/Configuration/Prices Computations/Prices Types
 * Books/Configuration/Prices Computations/Pricelists Types

.. i18n: Views
.. i18n: -----

Views
-----

.. i18n:  * product.product.tree (tree)
.. i18n:  * product.normal.form (form)
.. i18n:  * product.category.form (form)
.. i18n:  * product.category.list (tree)
.. i18n:  * product.category.tree (tree)
.. i18n:  * product.uom.tree (tree)
.. i18n:  * product.uom.form (form)
.. i18n:  * product.uom.categ.form (form)
.. i18n:  * product.ul.form.view (form)
.. i18n:  * product.ul.tree (tree)
.. i18n:  * product.packaging.tree.view (tree)
.. i18n:  * product.packaging.form.view (form)
.. i18n:  * product.supplierinfo.form.view (form)
.. i18n:  * product.supplierinfo.tree.view (tree)
.. i18n:  * product.variant.form (form)
.. i18n:  * product.variant.tree (tree)
.. i18n:  * product.template.product.tree (tree)
.. i18n:  * product.template.product.form (form)
.. i18n:  * product.pricelist.version.form (form)
.. i18n:  * product.pricelist.version.tree (tree)
.. i18n:  * product.pricelist.item.tree (tree)
.. i18n:  * product.pricelist.item.form (form)
.. i18n:  * product.pricelist.tree (tree)
.. i18n:  * product.pricelist.form (form)
.. i18n:  * product.price.type.form (form)
.. i18n:  * product.pricelist.type.form (form)
.. i18n:  * \* INHERIT res.partner.product.property.form.inherit (form)

 * product.product.tree (tree)
 * product.normal.form (form)
 * product.category.form (form)
 * product.category.list (tree)
 * product.category.tree (tree)
 * product.uom.tree (tree)
 * product.uom.form (form)
 * product.uom.categ.form (form)
 * product.ul.form.view (form)
 * product.ul.tree (tree)
 * product.packaging.tree.view (tree)
 * product.packaging.form.view (form)
 * product.supplierinfo.form.view (form)
 * product.supplierinfo.tree.view (tree)
 * product.variant.form (form)
 * product.variant.tree (tree)
 * product.template.product.tree (tree)
 * product.template.product.form (form)
 * product.pricelist.version.form (form)
 * product.pricelist.version.tree (tree)
 * product.pricelist.item.tree (tree)
 * product.pricelist.item.form (form)
 * product.pricelist.tree (tree)
 * product.pricelist.form (form)
 * product.price.type.form (form)
 * product.pricelist.type.form (form)
 * \* INHERIT res.partner.product.property.form.inherit (form)

.. i18n: Objects
.. i18n: -------

Objects
-------

.. i18n: Object: Product uom categ (product.uom.categ)
.. i18n: #############################################

Object: Product uom categ (product.uom.categ)
#############################################

.. i18n: :name: Name, char, required

:name: Name, char, required

.. i18n: Object: Product Unit of Measure (product.uom)
.. i18n: #############################################

Object: Product Unit of Measure (product.uom)
#############################################

.. i18n: :name: Name, char, required

:name: Name, char, required

.. i18n: :factor_inv: Factor, float

:factor_inv: Factor, float

.. i18n:     *The coefficient for the formula:
.. i18n:     coef (base unit) = 1 (this unit). Factor = 1 / Rate.*

    *The coefficient for the formula:
    coef (base unit) = 1 (this unit). Factor = 1 / Rate.*

.. i18n: :rounding: Rounding Precision, float, required

:rounding: Rounding Precision, float, required

.. i18n:     *The computed quantity will be a multiple of this value. Use 1.0 for products that can not be splitted.*

    *The computed quantity will be a multiple of this value. Use 1.0 for products that can not be splitted.*

.. i18n: :factor: Rate, float, required

:factor: Rate, float, required

.. i18n:     *The coefficient for the formula:
.. i18n:     1 (base unit) = coef (this unit). Rate = 1 / Factor.*

    *The coefficient for the formula:
    1 (base unit) = coef (this unit). Rate = 1 / Factor.*

.. i18n: :active: Active, boolean

:active: Active, boolean

.. i18n: :category_id: UoM Category, many2one, required

:category_id: UoM Category, many2one, required

.. i18n:     *Unit of Measure of the same category can be converted between each others.*

    *Unit of Measure of the same category can be converted between each others.*

.. i18n: :factor_inv_data: Factor, float

:factor_inv_data: Factor, float

.. i18n: Object: Shipping Unit (product.ul)
.. i18n: ##################################

Object: Shipping Unit (product.ul)
##################################

.. i18n: :type: Type, selection, required

:type: Type, selection, required

.. i18n: :name: Name, char, required

:name: Name, char, required

.. i18n: Object: Product Category (product.category)
.. i18n: ###########################################

Object: Product Category (product.category)
###########################################

.. i18n: :property_account_expense_categ: Expense Account, many2one

:property_account_expense_categ: Expense Account, many2one

.. i18n:     *This account will be used, instead of the default one, to value outgoing stock for the current product category*

    *This account will be used, instead of the default one, to value outgoing stock for the current product category*

.. i18n: :property_stock_journal: Stock journal, many2one

:property_stock_journal: Stock journal, many2one

.. i18n:     *This journal will be used for the accounting move generated by stock move*

    *This journal will be used for the accounting move generated by stock move*

.. i18n: :isamenitype: Is amenities Type, boolean

:isamenitype: Is amenities Type, boolean

.. i18n: :property_account_expense_world: Outside Europe Expense Account, many2one

:property_account_expense_world: Outside Europe Expense Account, many2one

.. i18n:     *This account will be used, instead of the default one, to value outgoing stock for the current product*

    *This account will be used, instead of the default one, to value outgoing stock for the current product*

.. i18n: :sequence: Sequence, integer

:sequence: Sequence, integer

.. i18n: :property_account_expense_europe: Expense Account for Europe, many2one

:property_account_expense_europe: Expense Account for Europe, many2one

.. i18n:     *This account will be used, instead of the default one, to value outgoing stock for the current product*

    *This account will be used, instead of the default one, to value outgoing stock for the current product*

.. i18n: :ismenutype: Is Menu Type, boolean

:ismenutype: Is Menu Type, boolean

.. i18n: :isservicetype: Is Service Type, boolean

:isservicetype: Is Service Type, boolean

.. i18n: :property_stock_account_input_categ: Stock Input Account, many2one

:property_stock_account_input_categ: Stock Input Account, many2one

.. i18n:     *This account will be used to value the input stock*

    *This account will be used to value the input stock*

.. i18n: :property_account_income_europe: Income Account for Europe, many2one

:property_account_income_europe: Income Account for Europe, many2one

.. i18n:     *This account will be used, instead of the default one, to value incoming stock for the current product*

    *This account will be used, instead of the default one, to value incoming stock for the current product*

.. i18n: :parent_id: Parent Category, many2one

:parent_id: Parent Category, many2one

.. i18n: :property_account_income_world: Outside Europe Income Account, many2one

:property_account_income_world: Outside Europe Income Account, many2one

.. i18n:     *This account will be used, instead of the default one, to value incoming stock for the current product*

    *This account will be used, instead of the default one, to value incoming stock for the current product*

.. i18n: :complete_name: Name, char, readonly

:complete_name: Name, char, readonly

.. i18n: :isactivitytype: Is Activity Type, boolean

:isactivitytype: Is Activity Type, boolean

.. i18n: :property_account_income_categ: Income Account, many2one

:property_account_income_categ: Income Account, many2one

.. i18n:     *This account will be used, instead of the default one, to value incoming stock for the current product category*

    *This account will be used, instead of the default one, to value incoming stock for the current product category*

.. i18n: :child_id: Childs Categories, one2many

:child_id: Childs Categories, one2many

.. i18n: :isroomtype: Is Room Type, boolean

:isroomtype: Is Room Type, boolean

.. i18n: :property_stock_account_output_categ: Stock Output Account, many2one

:property_stock_account_output_categ: Stock Output Account, many2one

.. i18n:     *This account will be used to value the output stock*

    *This account will be used to value the output stock*

.. i18n: :name: Name, char, required

:name: Name, char, required

.. i18n: Object: Product Template (product.template)
.. i18n: ###########################################

Object: Product Template (product.template)
###########################################

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

.. i18n: :standard_price: Cost Price, float, required

:standard_price: Cost Price, float, required

.. i18n:     *The cost of the product for accounting stock valorisation. It can serves as a base price for supplier price.*

    *The cost of the product for accounting stock valorisation. It can serves as a base price for supplier price.*

.. i18n: :member_price: Member Price, float

:member_price: Member Price, float

.. i18n: :mes_type: Measure Type, selection, required

:mes_type: Measure Type, selection, required

.. i18n: :uom_id: Default UoM, many2one, required

:uom_id: Default UoM, many2one, required

.. i18n:     *Default Unit of Measure used for all stock operation.*

    *Default Unit of Measure used for all stock operation.*

.. i18n: :description_purchase: Purchase Description, text

:description_purchase: Purchase Description, text

.. i18n: :property_account_income: Income Account, many2one

:property_account_income: Income Account, many2one

.. i18n:     *This account will be used, instead of the default one, to value incoming stock for the current product*

    *This account will be used, instead of the default one, to value incoming stock for the current product*

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

.. i18n: :sale_ok: Can be sold, boolean

:sale_ok: Can be sold, boolean

.. i18n:     *Determine if the product can be visible in the list of product within a selection from a sale order line.*

    *Determine if the product can be visible in the list of product within a selection from a sale order line.*

.. i18n: :auto_picking: Auto Picking for Production, boolean

:auto_picking: Auto Picking for Production, boolean

.. i18n: :purchase_ok: Can be Purchased, boolean

:purchase_ok: Can be Purchased, boolean

.. i18n:     *Determine if the product is visible in the list of products within a selection from a purchase order line.*

    *Determine if the product is visible in the list of products within a selection from a purchase order line.*

.. i18n: :product_manager: Product Manager, many2one

:product_manager: Product Manager, many2one

.. i18n: :company_id: Company, many2one

:company_id: Company, many2one

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

.. i18n: :uom_po_id: Purchase UoM, many2one, required

:uom_po_id: Purchase UoM, many2one, required

.. i18n:     *Default Unit of Measure used for purchase orders. It must in the same category than the default unit of measure.*

    *Default Unit of Measure used for purchase orders. It must in the same category than the default unit of measure.*

.. i18n: :intrastat_id: Intrastat code, many2one

:intrastat_id: Intrastat code, many2one

.. i18n: :type: Product Type, selection, required

:type: Product Type, selection, required

.. i18n:     *Will change the way procurements are processed, consumable are stockable products with infinite stock, or without a stock management in the system.*

    *Will change the way procurements are processed, consumable are stockable products with infinite stock, or without a stock management in the system.*

.. i18n: :property_stock_account_input: Stock Input Account, many2one

:property_stock_account_input: Stock Input Account, many2one

.. i18n:     *This account will be used, instead of the default one, to value input stock*

    *This account will be used, instead of the default one, to value input stock*

.. i18n: :property_account_income_europe: Income Account for Europe, many2one

:property_account_income_europe: Income Account for Europe, many2one

.. i18n:     *This account will be used, instead of the default one, to value incoming stock for the current product*

    *This account will be used, instead of the default one, to value incoming stock for the current product*

.. i18n: :loc_case: Case, char

:loc_case: Case, char

.. i18n: :description: Description, text

:description: Description, text

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

.. i18n: :supplier_taxes_id: Supplier Taxes, many2many

:supplier_taxes_id: Supplier Taxes, many2many

.. i18n: :volume: Volume, float

:volume: Volume, float

.. i18n:     *The volume in m3.*

    *The volume in m3.*

.. i18n: :y: Y of Product, float

:y: Y of Product, float

.. i18n: :cutting: Can be Cutted, boolean

:cutting: Can be Cutted, boolean

.. i18n: :description_sale: Sale Description, text

:description_sale: Sale Description, text

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

.. i18n: :loc_row: Row, char

:loc_row: Row, char

.. i18n: :seller_delay: Supplier Lead Time, integer, readonly

:seller_delay: Supplier Lead Time, integer, readonly

.. i18n:     *This is the average delay in days between the purchase order confirmation and the reception of goods for this product and for the default supplier. It is used by the scheduler to order requests based on reordering delays.*

    *This is the average delay in days between the purchase order confirmation and the reception of goods for this product and for the default supplier. It is used by the scheduler to order requests based on reordering delays.*

.. i18n: :rental: Rentable product, boolean

:rental: Rentable product, boolean

.. i18n: :sale_delay: Customer Lead Time, float

:sale_delay: Customer Lead Time, float

.. i18n:     *This is the average time between the confirmation of the customer order and the delivery of the finnished products. It's the time you promise to your customers.*

    *This is the average time between the confirmation of the customer order and the delivery of the finnished products. It's the time you promise to your customers.*

.. i18n: :name: Name, char, required

:name: Name, char, required

.. i18n: :property_stock_account_output: Stock Output Account, many2one

:property_stock_account_output: Stock Output Account, many2one

.. i18n:     *This account will be used, instead of the default one, to value output stock*

    *This account will be used, instead of the default one, to value output stock*

.. i18n: :property_account_expense: Expense Account, many2one

:property_account_expense: Expense Account, many2one

.. i18n:     *This account will be used, instead of the default one, to value outgoing stock for the current product*

    *This account will be used, instead of the default one, to value outgoing stock for the current product*

.. i18n: :categ_id: Category, many2one, required

:categ_id: Category, many2one, required

.. i18n: :taxes_id: Product Taxes, many2many

:taxes_id: Product Taxes, many2many

.. i18n: :produce_delay: Manufacturing Lead Time, float

:produce_delay: Manufacturing Lead Time, float

.. i18n:     *Average time to produce this product. This is only for the production order and, if it is a multi-level bill of material, it's only for the level of this product. Different delays will be summed for all levels and purchase orders.*

    *Average time to produce this product. This is only for the production order and, if it is a multi-level bill of material, it's only for the level of this product. Different delays will be summed for all levels and purchase orders.*

.. i18n: :seller_ids: Partners, one2many

:seller_ids: Partners, one2many

.. i18n: :x: X of Product, float

:x: X of Product, float

.. i18n: :z: Z of Product, float

:z: Z of Product, float

.. i18n: Object: Product (product.product)
.. i18n: #################################

Object: Product (product.product)
#################################

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

.. i18n: :isbn: Isbn code, char

:isbn: Isbn code, char

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

.. i18n: :packaging: Logistical Units, one2many

:packaging: Logistical Units, one2many

.. i18n:     *Gives the different ways to package the same product. This has no impact on the packing order and is mainly used if you use the EDI module.*

    *Gives the different ways to package the same product. This has no impact on the packing order and is mainly used if you use the EDI module.*

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

.. i18n: :manufacturer: Manufacturer, many2one

:manufacturer: Manufacturer, many2one

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

.. i18n: :unique_production_number: Unique Production Number, boolean

:unique_production_number: Unique Production Number, boolean

.. i18n: :life_time: Product lifetime, integer

:life_time: Product lifetime, integer

.. i18n: :price: Customer Price, float, readonly

:price: Customer Price, float, readonly

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

.. i18n: :expected_margin_rate: Expected Margin (%), float, readonly

:expected_margin_rate: Expected Margin (%), float, readonly

.. i18n:     *Expected margin * 100 / Expected Sale*

    *Expected margin * 100 / Expected Sale*

.. i18n: :seller_delay: Supplier Lead Time, integer, readonly

:seller_delay: Supplier Lead Time, integer, readonly

.. i18n:     *This is the average delay in days between the purchase order confirmation and the reception of goods for this product and for the default supplier. It is used by the scheduler to order requests based on reordering delays.*

    *This is the average delay in days between the purchase order confirmation and the reception of goods for this product and for the default supplier. It is used by the scheduler to order requests based on reordering delays.*

.. i18n: :index_purchase: Purchase indexes, many2many

:index_purchase: Purchase indexes, many2many

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

.. i18n: :list_price: Sale Price, float

:list_price: Sale Price, float

.. i18n:     *Base price for computing the customer price. Sometimes called the catalog price.*

    *Base price for computing the customer price. Sometimes called the catalog price.*

.. i18n: :purchase_line_warn_msg: Message for Purchase Order Line, text

:purchase_line_warn_msg: Message for Purchase Order Line, text

.. i18n: :member_price: Member Price, float

:member_price: Member Price, float

.. i18n: :sale_line_warn_msg: Message for Sale Order Line, text

:sale_line_warn_msg: Message for Sale Order Line, text

.. i18n: :mes_type: Measure Type, selection, required

:mes_type: Measure Type, selection, required

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

.. i18n: :sale_ok: Can be sold, boolean

:sale_ok: Can be sold, boolean

.. i18n:     *Determine if the product can be visible in the list of product within a selection from a sale order line.*

    *Determine if the product can be visible in the list of product within a selection from a sale order line.*

.. i18n: :buyer_price_index: Indexed buyer price, float, readonly

:buyer_price_index: Indexed buyer price, float, readonly

.. i18n: :categ_id: Category, many2one, required

:categ_id: Category, many2one, required

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

.. i18n: :author_ids: Authors, many2many

:author_ids: Authors, many2many

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

.. i18n: :nbpage: Number of pages, integer

:nbpage: Number of pages, integer

.. i18n: :pocket: Pocket, char

:pocket: Pocket, char

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

.. i18n: :weight_net: Net weight, float

:weight_net: Net weight, float

.. i18n:     *The net weight in Kg.*

    *The net weight in Kg.*

.. i18n: :index_date: Index price date, date, required

:index_date: Index price date, date, required

.. i18n: :collection: Collection, many2one

:collection: Collection, many2one

.. i18n: :membership: Membership, boolean

:membership: Membership, boolean

.. i18n:     *Specify if this product is a membership product*

    *Specify if this product is a membership product*

.. i18n: :manufacturer_pref: Manufacturer product code, char

:manufacturer_pref: Manufacturer product code, char

.. i18n: :lang: Language, many2many

:lang: Language, many2many

.. i18n: :volume: Volume, float

:volume: Volume, float

.. i18n:     *The volume in m3.*

    *The volume in m3.*

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

.. i18n: :turnover: Turnover, float, readonly

:turnover: Turnover, float, readonly

.. i18n:     *Sum of Multification of Invoice price and quantity of Customer Invoices*

    *Sum of Multification of Invoice price and quantity of Customer Invoices*

.. i18n: Object: Packaging (product.packaging)
.. i18n: #####################################

Object: Packaging (product.packaging)
#####################################

.. i18n: :rows: Number of Layer, integer, required

:rows: Number of Layer, integer, required

.. i18n:     *The number of layer on a palet or box*

    *The number of layer on a palet or box*

.. i18n: :name: Description, char

:name: Description, char

.. i18n: :weight: Total Package Weight, float

:weight: Total Package Weight, float

.. i18n:     *The weight of a full of products palet or box.*

    *The weight of a full of products palet or box.*

.. i18n: :ean: EAN, char

:ean: EAN, char

.. i18n:     *The EAN code of the package unit.*

    *The EAN code of the package unit.*

.. i18n: :ul_qty: Package by layer, integer

:ul_qty: Package by layer, integer

.. i18n: :sequence: Sequence, integer

:sequence: Sequence, integer

.. i18n: :qty: Quantity by Package, float

:qty: Quantity by Package, float

.. i18n:     *The total number of products you can put by palet or box.*

    *The total number of products you can put by palet or box.*

.. i18n: :ul: Type of Package, many2one, required

:ul: Type of Package, many2one, required

.. i18n: :length: Length, float

:length: Length, float

.. i18n:     *The length of the package*

    *The length of the package*

.. i18n: :code: Code, char

:code: Code, char

.. i18n:     *The code of the transport unit.*

    *The code of the transport unit.*

.. i18n: :width: Width, float

:width: Width, float

.. i18n:     *The width of the package*

    *The width of the package*

.. i18n: :height: Height, float

:height: Height, float

.. i18n:     *The height of the package*

    *The height of the package*

.. i18n: :weight_ul: Empty Package Weight, float

:weight_ul: Empty Package Weight, float

.. i18n:     *The weight of the empty UL*

    *The weight of the empty UL*

.. i18n: :product_id: Product, many2one, required

:product_id: Product, many2one, required

.. i18n: Object: Information about a product supplier (product.supplierinfo)
.. i18n: ###################################################################

Object: Information about a product supplier (product.supplierinfo)
###################################################################

.. i18n: :pricelist_ids: Supplier Pricelist, one2many

:pricelist_ids: Supplier Pricelist, one2many

.. i18n: :last_order_date: Last Order date, date, readonly

:last_order_date: Last Order date, date, readonly

.. i18n: :product_id: Product, many2one, required

:product_id: Product, many2one, required

.. i18n: :sequence: Priority, integer

:sequence: Priority, integer

.. i18n: :qty: Minimal Quantity, float, required

:qty: Minimal Quantity, float, required

.. i18n:     *The minimal quantity to purchase for this supplier, expressed in the default unit of measure.*

    *The minimal quantity to purchase for this supplier, expressed in the default unit of measure.*

.. i18n: :delay: Delivery Delay, integer, required

:delay: Delivery Delay, integer, required

.. i18n:     *Delay in days between the confirmation of the purchase order and the reception of the products in your warehouse. Used by the scheduler for automatic computation of the purchase order planning.*

    *Delay in days between the confirmation of the purchase order and the reception of the products in your warehouse. Used by the scheduler for automatic computation of the purchase order planning.*

.. i18n: :last_order: Last Order, many2one, readonly

:last_order: Last Order, many2one, readonly

.. i18n: :direct_delivery_flag: Direct delivery possible ?, boolean

:direct_delivery_flag: Direct delivery possible ?, boolean

.. i18n: :product_code: Partner Product Code, char

:product_code: Partner Product Code, char

.. i18n:     *Code of the product for this partner, will be used when printing a request for quotation. Keep empty to use the internal one.*

    *Code of the product for this partner, will be used when printing a request for quotation. Keep empty to use the internal one.*

.. i18n: :product_name: Partner Product Name, char

:product_name: Partner Product Name, char

.. i18n:     *Name of the product for this partner, will be used when printing a request for quotation. Keep empty to use the internal one.*

    *Name of the product for this partner, will be used when printing a request for quotation. Keep empty to use the internal one.*

.. i18n: :name: Partner, many2one, required

:name: Partner, many2one, required

.. i18n:     *Supplier of this product*

    *Supplier of this product*

.. i18n: Object: pricelist.partnerinfo (pricelist.partnerinfo)
.. i18n: #####################################################

Object: pricelist.partnerinfo (pricelist.partnerinfo)
#####################################################

.. i18n: :min_quantity: Quantity, float, required

:min_quantity: Quantity, float, required

.. i18n: :price: Unit Price, float, required

:price: Unit Price, float, required

.. i18n: :suppinfo_id: Partner Information, many2one, required

:suppinfo_id: Partner Information, many2one, required

.. i18n: :name: Description, char

:name: Description, char

.. i18n: Object: Price type (product.price.type)
.. i18n: #######################################

Object: Price type (product.price.type)
#######################################

.. i18n: :active: Active, boolean

:active: Active, boolean

.. i18n: :field: Product Field, selection, required

:field: Product Field, selection, required

.. i18n:     *Associated field in the product form.*

    *Associated field in the product form.*

.. i18n: :currency_id: Currency, many2one, required

:currency_id: Currency, many2one, required

.. i18n:     *The currency the field is expressed in.*

    *The currency the field is expressed in.*

.. i18n: :name: Price Name, char, required

:name: Price Name, char, required

.. i18n:     *Name of this kind of price.*

    *Name of this kind of price.*

.. i18n: Object: Pricelist Type (product.pricelist.type)
.. i18n: ###############################################

Object: Pricelist Type (product.pricelist.type)
###############################################

.. i18n: :name: Name, char, required

:name: Name, char, required

.. i18n: :key: Key, char, required

:key: Key, char, required

.. i18n:     *Used in the code to select specific prices based on the context. Keep unchanged.*

    *Used in the code to select specific prices based on the context. Keep unchanged.*

.. i18n: Object: Pricelist (product.pricelist)
.. i18n: #####################################

Object: Pricelist (product.pricelist)
#####################################

.. i18n: :visible_discount: Visible Discount, boolean

:visible_discount: Visible Discount, boolean

.. i18n: :name: Pricelist Name, char, required

:name: Pricelist Name, char, required

.. i18n: :version_id: Pricelist Versions, one2many

:version_id: Pricelist Versions, one2many

.. i18n: :currency_id: Currency, many2one, required

:currency_id: Currency, many2one, required

.. i18n: :active: Active, boolean

:active: Active, boolean

.. i18n: :type: Pricelist Type, selection, required

:type: Pricelist Type, selection, required

.. i18n: Object: Pricelist Version (product.pricelist.version)
.. i18n: #####################################################

Object: Pricelist Version (product.pricelist.version)
#####################################################

.. i18n: :items_id: Price List Items, one2many, required

:items_id: Price List Items, one2many, required

.. i18n: :name: Name, char, required

:name: Name, char, required

.. i18n: :date_end: End Date, date

:date_end: End Date, date

.. i18n:     *Ending date for validity of this pricelist version.*

    *Ending date for validity of this pricelist version.*

.. i18n: :date_start: Start Date, date

:date_start: Start Date, date

.. i18n:     *Starting date for validity of this pricelist version.*

    *Starting date for validity of this pricelist version.*

.. i18n: :active: Active, boolean

:active: Active, boolean

.. i18n: :pricelist_id: Price List, many2one, required

:pricelist_id: Price List, many2one, required

.. i18n: :offer_name: OfferName, char

:offer_name: OfferName, char

.. i18n: Object: Pricelist item (product.pricelist.item)
.. i18n: ###############################################

Object: Pricelist item (product.pricelist.item)
###############################################

.. i18n: :price_round: Price Rounding, float

:price_round: Price Rounding, float

.. i18n:     *Sets the price so that it is a multiple of this value.
.. i18n:     Rounding is applied after the discount and before the surcharge.
.. i18n:     To have prices that ends by 9.99, set rounding 10, surcharge -0.01*

    *Sets the price so that it is a multiple of this value.
    Rounding is applied after the discount and before the surcharge.
    To have prices that ends by 9.99, set rounding 10, surcharge -0.01*

.. i18n: :price_min_margin: Price Min. Margin, float

:price_min_margin: Price Min. Margin, float

.. i18n: :name: Rule Name, char

:name: Rule Name, char

.. i18n:     *Explicit rule name for this pricelist line.*

    *Explicit rule name for this pricelist line.*

.. i18n: :base_pricelist_id: If Other Pricelist, many2one

:base_pricelist_id: If Other Pricelist, many2one

.. i18n: :sequence: Sequence, integer, required

:sequence: Sequence, integer, required

.. i18n: :price_max_margin: Price Max. Margin, float

:price_max_margin: Price Max. Margin, float

.. i18n: :product_tmpl_id: Product Template, many2one

:product_tmpl_id: Product Template, many2one

.. i18n:     *Set a template if this rule only apply to a template of product. Keep empty for all products*

    *Set a template if this rule only apply to a template of product. Keep empty for all products*

.. i18n: :base: Based on, selection, required

:base: Based on, selection, required

.. i18n:     *The mode of computation of the price for this rule.*

    *The mode of computation of the price for this rule.*

.. i18n: :price_discount: Price Discount, float

:price_discount: Price Discount, float

.. i18n: :price_version_id: Price List Version, many2one, required

:price_version_id: Price List Version, many2one, required

.. i18n: :min_quantity: Min. Quantity, integer, required

:min_quantity: Min. Quantity, integer, required

.. i18n:     *The rule only apply if the partner buys/sells more than this quantity.*

    *The rule only apply if the partner buys/sells more than this quantity.*

.. i18n: :price_surcharge: Price Surcharge, float

:price_surcharge: Price Surcharge, float

.. i18n: :categ_id: Product Category, many2one

:categ_id: Product Category, many2one

.. i18n:     *Set a category of product if this rule only apply to products of a category and his childs. Keep empty for all products*

    *Set a category of product if this rule only apply to products of a category and his childs. Keep empty for all products*

.. i18n: :product_id: Product, many2one

:product_id: Product, many2one

.. i18n:     *Set a product if this rule only apply to one product. Keep empty for all products*

    *Set a product if this rule only apply to one product. Keep empty for all products*
