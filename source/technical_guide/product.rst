
.. module:: product
    :synopsis: Products & Pricelists (Official, Quality Certified)
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/product"></div>
    <script src="http://js-kit.com/ratings.js"></script>

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

Description
-----------

::

  This is the base module for managing products and pricelists in Open ERP.
  
      Products support variants, different pricing methods, suppliers
      information, make to stock/order, different unit of measures,
      packaging and properties.
  
      Pricelists support:
      * Multiple-level of discount (by product, category, quantities)
      * Compute price based on different criteria:
          * Other pricelist,
          * Cost price,
          * List price,
          * Supplier price, ...
      Pricelists preferences by product and/or partners.
  
      Print product labels with barcode.

Download links
--------------

You can download this module as a zip file in the following version:

  * `4.2 <http://www.openerp.com/download/modules/4.2/product.zip>`_
  * `5.0 <http://www.openerp.com/download/modules/5.0/product.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/product.zip>`_


Dependencies
------------

 * :mod:`base`
 * :mod:`process`

Reports
-------

 * Products Labels

Menus
-------

 * Products
 * Products/Configuration
 * Products/Products
 * Products/Products by Category
 * Products/Configuration/Products Categories
 * Products/Configuration/Units of Measure
 * Products/Configuration/Units of Measure/Units of Measure
 * Products/Configuration/Units of Measure/Units of Measure Categories
 * Products/Configuration/Packaging
 * Products/Pricelists
 * Products/Pricelists/Pricelist Versions
 * Products/Pricelists/Pricelists
 * Products/Configuration/Prices Computations
 * Products/Configuration/Prices Computations/Prices Types
 * Products/Configuration/Prices Computations/Pricelists Types

Views
-----

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


Objects
-------

Object: Product uom categ (product.uom.categ)
#############################################



:name: Name, char, required




Object: Product Unit of Measure (product.uom)
#############################################



:name: Name, char, required





:factor_inv: Factor, float, readonly

    *The coefficient for the formula:
    coeff (base unit) = 1 (this unit). Factor = 1 / Rate.*



:rounding: Rounding Precision, float, required

    *The computed quantity will be a multiple of this value. Use 1.0 for products that can not be split.*



:factor: Rate, float, required

    *The coefficient for the formula:
    1 (base unit) = coeff (this unit). Rate = 1 / Factor.*



:active: Active, boolean





:category_id: UoM Category, many2one, required

    *Unit of Measure of a category can be converted between each others in the same category.*



:factor_inv_data: Factor, float




Object: Shipping Unit (product.ul)
##################################



:type: Type, selection, required





:name: Name, char, required




Object: Product Category (product.category)
###########################################



:sequence: Sequence, integer





:updated: Category updated on Magento, boolean





:child_id: Child Categories, one2many





:property_stock_account_input_categ: Stock Input Account, many2one

    *This account will be used to value the input stock*



:property_stock_account_output_categ: Stock Output Account, many2one

    *This account will be used to value the output stock*



:isactivitytype: Is Activity Type, boolean





:exportable: Export to website, boolean





:ismenutype: Is Menu Type, boolean





:isservicetype: Is Service Type, boolean





:parent_id: Parent Category, many2one





:property_account_income_world: Outside Europe Income Account, many2one

    *This account will be used, instead of the default one, to value incoming stock for the current product*



:complete_name: Name, char, readonly





:magento_product_type: Magento product type, integer





:isamenitype: Is amenities Type, boolean





:property_account_income_europe: Income Account for Europe, many2one

    *This account will be used, instead of the default one, to value incoming stock for the current product*



:property_account_expense_categ: Expense Account, many2one

    *This account will be used to value outgoing stock for the current product category*



:property_stock_journal: Stock journal, many2one

    *This journal will be used for the accounting move generated by stock move*



:magento_product_attribute_set_id: Magento product attribute set id, integer





:property_account_expense_europe: Expense Account for Europe, many2one

    *This account will be used, instead of the default one, to value outgoing stock for the current product*



:property_account_income_categ: Income Account, many2one

    *This account will be used to value incoming stock for the current product category*



:property_account_expense_world: Outside Europe Expense Account, many2one

    *This account will be used, instead of the default one, to value outgoing stock for the current product*



:isroomtype: Is Room Type, boolean





:name: Name, char, required





:magento_id: Magento category id, integer




Object: Product Template (product.template)
###########################################



:warranty: Warranty (months), float





:property_stock_procurement: Procurement Location, many2one

    *For the current product (template), this stock location will be used, instead of the default one, as the source location for stock moves generated by procurements*



:supply_method: Supply method, selection, required

    *Produce will generate production order or tasks, according to the product type. Purchase will trigger purchase orders when requested.*



:uos_id: Unit of Sale, many2one

    *Used by companies that manages two unit of measure: invoicing and stock management. For example, in food industries, you will manage a stock of ham but invoice in Kg. Keep empty to use the default UOM.*



:list_price: Sale Price, float

    *Base price for computing the customer price. Sometimes called the catalog price.*



:weight: Gross weight, float

    *The gross weight in Kg.*



:standard_price: Cost Price, float, required

    *The cost of the product for accounting stock valuation. It can serves as a base price for supplier price.*



:member_price: Member Price, float





:mes_type: Measure Type, selection, required





:uom_id: Default UoM, many2one, required

    *Default Unit of Measure used for all stock operation.*



:description_purchase: Purchase Description, text





:property_account_income: Income Account, many2one

    *This account will be used instead of the default one to value incoming stock for the current product*



:property_account_expense_world1: Outside Europe Expense Account, many2one

    *This account will be used, instead of the default one, to value outgoing stock for the current product*



:uos_coeff: UOM -> UOS Coeff, float

    *Coefficient to convert UOM to UOS
    uom = uos * coeff*



:sale_ok: Can be sold, boolean

    *Determine if the product can be visible in the list of product within a selection from a sale order line.*



:life_cycle: Life Cycle, selection





:purchase_ok: Can be Purchased, boolean

    *Determine if the product is visible in the list of products within a selection from a purchase order line.*



:product_manager: Product Manager, many2one





:characteristic_group_ids: Characteristic groups, many2many





:company_id: Company, many2one





:produce_delay: Manufacturing Lead Time, float

    *Average time to produce this product. This is only for the production order and, if it is a multi-level bill of material, it's only for the level of this product. Different delays will be summed for all levels and purchase orders.*



:state: Status, selection

    *Tells the user if he can use the product or not.*



:property_account_income_world: Outside Europe Income Account, many2one

    *This account will be used, instead of the default one, to value incoming stock for the current product*



:loc_rack: Rack, char





:rough_drawing: rough drawing, binary





:uom_po_id: Purchase UoM, many2one, required

    *Default Unit of Measure used for purchase orders. It must in the same category than the default unit of measure.*



:intrastat_id: Intrastat code, many2one





:type: Product Type, selection, required

    *Will change the way procurements are processed. Consumables are stockable products with infinite stock, or for use when you have no stock management in the system.*



:property_stock_account_input: Stock Input Account, many2one

    *This account will be used, instead of the default one, to value input stock*



:property_account_income_europe: Income Account for Europe, many2one

    *This account will be used, instead of the default one, to value incoming stock for the current product*



:schema: schema, binary





:picture: picture, binary





:loc_case: Case, char





:description: Description, text





:property_account_expense_europe: Expense Account for Europe, many2one

    *This account will be used, instead of the default one, to value outgoing stock for the current product*



:weight_net: Net weight, float

    *The net weight in Kg.*



:property_stock_production: Production Location, many2one

    *For the current product (template), this stock location will be used, instead of the default one, as the source location for stock moves generated by production orders*



:supplier_taxes_id: Supplier Taxes, many2many





:volume: Volume, float

    *The volume in m3.*



:dimension_type_ids: Dimension Types, one2many





:procure_method: Procure Method, selection, required

    *'Make to Stock': When needed, take from the stock or wait until re-supplying. 'Make to Order': When needed, purchase or produce for the procurement request.*



:property_stock_inventory: Inventory Location, many2one

    *For the current product (template), this stock location will be used, instead of the default one, as the source location for stock moves generated when you do an inventory*



:cost_method: Costing Method, selection, required

    *Standard Price: the cost price is fixed and recomputed periodically (usually at the end of the year), Average Price: the cost price is recomputed at each reception of products.*



:loc_row: Row, char





:seller_delay: Supplier Lead Time, integer, readonly

    *This is the average delay in days between the purchase order confirmation and the reception of goods for this product and for the default supplier. It is used by the scheduler to order requests based on reordering delays.*



:rental: Rentable Product, boolean





:sale_delay: Customer Lead Time, float

    *This is the average time between the confirmation of the customer order and the delivery of the finished products. It's the time you promise to your customers.*



:name: Name, char, required





:description_sale: Sale Description, text





:property_account_expense: Expense Account, many2one

    *This account will be used instead of the default one to value outgoing stock for the current product*



:categ_id: Category, many2one, required





:variant_ids: Variants, one2many





:taxes_id: Product Taxes, many2many





:property_stock_account_output: Stock Output Account, many2one

    *This account will be used, instead of the default one, to value output stock*



:seller_ids: Partners, one2many




Object: Product (product.product)
#################################



:ean13: EAN, char

    *Barcode number for EAN8 EAN13 UPC JPC GTIN http://de.wikipedia.org/wiki/Global_Trade_Item_Number*



:characteristic_ids: Characteristics, many2many





:code: Acronym, char, readonly





:pricelist_purchase: Purchase Pricelists, text, readonly





:incoming_qty: Incoming, float, readonly

    *Quantities of products that are planned to arrive in selected locations or all internal if none have been selected.*



:standard_price: Cost Price, float, required

    *The cost of the product for accounting stock valuation. It can serves as a base price for supplier price.*



:membership_date_to: Date to, date





:size_x: Width, float





:size_y: Length, float





:size_z: Thickness, float





:property_account_income: Income Account, many2one

    *This account will be used instead of the default one to value incoming stock for the current product*



:isbn: Isbn code, char





:index_sale: Sales indexes, many2many





:author_om_ids: Authors, one2many





:company_id: Company, many2one





:num_pocket: Collection Num., char





:loc_rack: Rack, char





:ismenucard: Is Room, boolean





:manufacturer_id:  Manufacturer, many2one





:price_margin: Variant Price Margin, float





:property_stock_account_input: Stock Input Account, many2one

    *This account will be used, instead of the default one, to value input stock*



:updated: Product updated on Magento, boolean





:pricelist_sale: Sale Pricelists, text, readonly





:format: Format, char





:pocket: Pocket, char





:is_direct_delivery_from_product: Is Supplier Direct Delivery Automatic?, boolean, readonly





:outgoing_qty: Outgoing, float, readonly

    *Quantities of products that are planned to leave in selected locations or all internal if none have been selected.*



:sale_num_invoiced: # Invoiced, float, readonly

    *Sum of Quantity in Customer Invoices*



:variants: Variants, char, readonly





:partner_ref: Customer ref, char, readonly





:rental: Rentable Product, boolean





:purchase_num_invoiced: # Invoiced, float, readonly

    *Sum of Quantity in Supplier Invoices*



:path_ids: Location Paths, one2many

    *These rules set the right path of the product in the whole location tree.*



:packaging: Logistical Units, one2many

    *Gives the different ways to package the same product. This has no impact on the packing order and is mainly used if you use the EDI module.*



:name: Name, char, required





:qty_dispo: Stock available, float, readonly





:sale_expected: Expected Sale, float, readonly

    *Sum of Multification of Sale Catalog price and quantity of Customer Invoices*



:editor: Editor, many2one





:dimension_value_ids: Dimensions, many2many





:seller_ids: Partners, one2many





:date_available: Available Date, date





:rack: Rack, many2one





:isroom: Is Room, boolean





:supply_method: Supply method, selection, required

    *Produce will generate production order or tasks, according to the product type. Purchase will trigger purchase orders when requested.*



:orderpoint_ids: Orderpoints, one2many





:weight: Gross weight, float

    *The gross weight in Kg.*



:series: Series, many2one





:lot_ids: Lots, one2many





:back: Reliure, selection





:creation_date: Creation date, datetime, readonly





:product_url: URL, char





:total_margin_rate: Total Margin (%), float, readonly

    *Total margin * 100 / Turnover*



:description_purchase: Purchase Description, text





:sales_gap: Sales Gap, float, readonly

    *Excepted Sale - Turn Over*



:virtual_available: Virtual Stock, float, readonly

    *Futur stock for this product according to the selected location or all internal if none have been selected. Computed as: Real Stock - Outgoing + Incoming.*



:date_retour: Return date, date





:total_cost: Total Cost, float, readonly

    *Sum of Multification of Invoice price and quantity of Supplier Invoices*



:language_id: Language, many2one





:thickness: Thickness, float





:product_tmpl_id: Product Template, many2one, required





:state: State, selection





:unique_production_number: Unique Production Number, boolean





:life_time: Product lifetime, integer





:price: Customer Price, float, readonly





:magento_tax_class_id: Magento tax class id, integer





:sale_avg_price: Avg. Unit Price, float, readonly

    *Avg. Price in Customer Invoices)*



:manufacturer_pname: Manufacturer product name, char





:country_ids: Allowed Countries, many2many





:image_name: Image name, char

    *Image name created by Magento*



:partner_ref2: Customer ref, char, readonly





:dimension_type_ids: Dimension Types, one2many





:hr_expense_ok: Can be Expensed, boolean

    *Determine if the product can be visible in the list of product within a selection from an HR expense sheet line.*



:active: Active, boolean





:loc_row: Row, char





:expected_margin_rate: Expected Margin (%), float, readonly

    *Expected margin * 100 / Expected Sale*



:seller_delay: Supplier Lead Time, integer, readonly

    *This is the average delay in days between the purchase order confirmation and the reception of goods for this product and for the default supplier. It is used by the scheduler to order requests based on reordering delays.*



:spe_price: Special price, char





:index_purchase: Purchase indexes, many2many





:loc_case: Case, char





:property_stock_account_output: Stock Output Account, many2one

    *This account will be used, instead of the default one, to value output stock*



:danger_ids: Dangers products, many2many





:securite_ids: Security, many2many





:length: Length, float





:catalog_num: Catalog number, char





:tome: Tome, char





:magento_id: Magento product id, integer





:warranty: Warranty (months), float





:property_stock_procurement: Procurement Location, many2one

    *For the current product (template), this stock location will be used, instead of the default one, as the source location for stock moves generated by procurements*



:uos_id: Unit of Sale, many2one

    *Used by companies that manages two unit of measure: invoicing and stock management. For example, in food industries, you will manage a stock of ham but invoice in Kg. Keep empty to use the default UOM.*



:list_price: Sale Price, float

    *Base price for computing the customer price. Sometimes called the catalog price.*



:purchase_line_warn_msg: Message for Purchase Order Line, text





:image: Image, binary

    *Image of the product (jpg or png). The same image will be set as thumbnail, small image and normal image. To change the product image, first delete the old one and save the product and then add the new one and save the product. Note that this image is optional, it can be left empty and manage the product images from Magento.*



:member_price: Member Price, float





:sale_line_warn_msg: Message for Sale Order Line, text





:mes_type: Measure Type, selection, required





:purchase_avg_price: Avg. Unit Price, float, readonly

    *Avg. Price in Supplier Invoices*



:exp_date: Expiry date, datetime





:risque_ids: Risk products, many2many





:qty_available: Real Stock, float, readonly

    *Current quantities of products in selected locations or all internal if none have been selected.*



:use_time: Product usetime, integer





:property_account_expense_world1: Outside Europe Expense Account, many2one

    *This account will be used, instead of the default one, to value outgoing stock for the current product*



:uos_coeff: UOM -> UOS Coeff, float

    *Coefficient to convert UOM to UOS
    uom = uos * coeff*



:auto_pick: Auto Picking, boolean

    *Auto picking for raw materials of production orders.*



:sale_ok: Can be sold, boolean

    *Determine if the product can be visible in the list of product within a selection from a sale order line.*



:buyer_price_index: Indexed buyer price, float, readonly





:purchase_ok: Can be Purchased, boolean

    *Determine if the product is visible in the list of products within a selection from a purchase order line.*



:product_manager: Product Manager, many2one





:characteristic_group_ids: Characteristic groups, many2many





:width: Width, float





:rough_drawing: rough drawing, binary





:normal_cost: Normal Cost, float, readonly

    *Sum of Multification of Cost price and quantity of Supplier Invoices*



:manufacturer: Manufacturer, many2one





:type: Product Type, selection, required

    *Will change the way procurements are processed. Consumables are stockable products with infinite stock, or for use when you have no stock management in the system.*



:property_account_income_europe: Income Account for Europe, many2one

    *This account will be used, instead of the default one, to value incoming stock for the current product*



:schema: schema, binary





:author_ids: Authors, many2many





:price_cat: Price category, many2one





:num_edition: Num. edition, integer





:track_incoming: Track Incomming Lots, boolean

    *Force to use a Production Lot during receptions*



:property_stock_production: Production Location, many2one

    *For the current product (template), this stock location will be used, instead of the default one, as the source location for stock moves generated by production orders*



:supplier_taxes_id: Supplier Taxes, many2many





:volume: Volume, float

    *The volume in m3.*



:package_weight: Package Weight, float





:membership_date_from: Date from, date





:date_to: To Date, date, readonly





:procure_method: Procure Method, selection, required

    *'Make to Stock': When needed, take from the stock or wait until re-supplying. 'Make to Order': When needed, purchase or produce for the procurement request.*



:property_stock_inventory: Inventory Location, many2one

    *For the current product (template), this stock location will be used, instead of the default one, as the source location for stock moves generated when you do an inventory*



:cost_method: Costing Method, selection, required

    *Standard Price: the cost price is fixed and recomputed periodically (usually at the end of the year), Average Price: the cost price is recomputed at each reception of products.*



:sale_delay: Customer Lead Time, float

    *This is the average time between the confirmation of the customer order and the delivery of the finished products. It's the time you promise to your customers.*



:description_sale: Sale Description, text





:purchase_line_warn: Purchase Order Line, selection

    *Selecting the "Warning" option will notify user with the message, Selecting "Blocking Message" will throw an exception with the message and block the flow. The Message has to be written in the next field.*



:state_ids: Allowed States, many2many





:product_picture: Product Picture, char





:purchase_gap: Purchase Gap, float, readonly

    *Normal Cost - Total Cost*



:sale_line_warn: Sale Order Line, selection

    *Selecting the "Warning" option will notify user with the message, Selecting "Blocking Message" will throw an exception with the message and block the flow. The Message has to be written in the next field.*



:isservice: Is Service id, boolean





:track_production: Track Production Lots, boolean

    *Force to use a Production Lot during production order*



:oscom_url: URL to OScommerce, char, readonly





:nbpage: Number of pages, integer





:spe_price_status: Status, selection





:price_extra: Variant Price Extra, float





:uom_id: Default UoM, many2one, required

    *Default Unit of Measure used for all stock operation.*



:default_code: Code, char





:attribute_ids: Attributes, one2many





:iscategid: Is categ id, boolean





:expected_margin: Expected Margin, float, readonly

    *Excepted Sale - Normal Cost*



:standard_price_index: Indexed standard price, float, readonly





:product_logo: Product Logo, binary





:image_label: Image label, char

    *Image label in the website. Left empty to take the product name as image label.*



:exportable: Export to website, boolean





:life_cycle: Life Cycle, selection





:auto_picking: Auto Picking for Production, boolean





:date_from: From Date, date, readonly





:track_outgoing: Track Outging Lots, boolean

    *Force to use a Production Lot during deliveries*



:lst_price: List Price, float, readonly





:property_account_income_world: Outside Europe Income Account, many2one

    *This account will be used, instead of the default one, to value incoming stock for the current product*



:is_maintenance: Is Maintenance?, boolean





:online: Visible on website, boolean





:uom_po_id: Purchase UoM, many2one, required

    *Default Unit of Measure used for purchase orders. It must in the same category than the default unit of measure.*



:intrastat_id: Intrastat code, many2one





:picture: Image, binary





:maintenance_analytic_id: Maintenance Analytic Account, many2one





:description: Description, text





:list_price_index: Indexed list price, float, readonly





:property_account_expense_europe: Expense Account for Europe, many2one

    *This account will be used, instead of the default one, to value outgoing stock for the current product*



:weight_net: Net weight, float

    *The net weight in Kg.*



:index_date: Index price date, date, required





:collection: Collection, many2one





:membership: Membership, boolean

    *Specify if this product is a membership product*



:manufacturer_pref: Manufacturer product code, char





:in_out_stock: In/Out Stock, selection





:categ_id: Category, many2one, required





:lang: Language, many2many





:removal_time: Product removal time, integer





:link_ids: Related Books, many2many





:equivalency_in_A4: A4 Equivalency, float





:produce_delay: Manufacturing Lead Time, float

    *Average time to produce this product. This is only for the production order and, if it is a multi-level bill of material, it's only for the level of this product. Different delays will be summed for all levels and purchase orders.*



:property_account_expense: Expense Account, many2one

    *This account will be used instead of the default one to value outgoing stock for the current product*



:calculate_price: Compute price, boolean





:invoice_state: Invoice State, selection, readonly





:variant_ids: Variants, one2many





:cutting: Can be Cutted, boolean





:alert_time: Product alert time, integer





:taxes_id: Product Taxes, many2many





:date_parution: Release date, date





:total_margin: Total Margin, float, readonly

    *Turnorder - Total Cost*



:buyer_price: Buyer price, float





:turnover: Turnover, float, readonly

    *Sum of Multification of Invoice price and quantity of Customer Invoices*


Object: Packaging (product.packaging)
#####################################



:rows: Number of Layer, integer, required

    *The number of layer on a palet or box*



:name: Description, char





:weight: Total Package Weight, float

    *The weight of a full of products palet or box.*



:ean: EAN, char

    *The EAN code of the package unit.*



:ul_qty: Package by layer, integer





:sequence: Sequence, integer





:qty: Quantity by Package, float

    *The total number of products you can put by palet or box.*



:ul: Type of Package, many2one, required





:length: Length, float

    *The length of the package*



:code: Code, char

    *The code of the transport unit.*



:width: Width, float

    *The width of the package*



:height: Height, float

    *The height of the package*



:weight_ul: Empty Package Weight, float

    *The weight of the empty UL*



:product_id: Product, many2one, required




Object: Information about a product supplier (product.supplierinfo)
###################################################################



:pricelist_ids: Supplier Pricelist, one2many





:last_order_date: Last Order date, date, readonly





:product_id: Product, many2one, required





:sequence: Priority, integer





:qty: Minimal Quantity, float, required

    *The minimal quantity to purchase for this supplier, expressed in the default unit of measure.*



:delay: Delivery Delay, integer, required

    *Delay in days between the confirmation of the purchase order and the reception of the products in your warehouse. Used by the scheduler for automatic computation of the purchase order planning.*



:last_order: Last Order, many2one, readonly





:direct_delivery_flag: Direct delivery possible ?, boolean





:product_code: Partner Product Code, char

    *Code of the product for this partner, will be used when printing a request for quotation. Keep empty to use the internal one.*



:product_name: Partner Product Name, char

    *Name of the product for this partner, will be used when printing a request for quotation. Keep empty to use the internal one.*



:name: Partner, many2one, required

    *Supplier of this product*


Object: pricelist.partnerinfo (pricelist.partnerinfo)
#####################################################



:min_quantity: Quantity, float, required





:price: Unit Price, float, required





:suppinfo_id: Partner Information, many2one, required





:name: Description, char




Object: Price type (product.price.type)
#######################################



:active: Active, boolean





:field: Product Field, selection, required

    *Associated field in the product form.*



:currency_id: Currency, many2one, required

    *The currency the field is expressed in.*



:name: Price Name, char, required

    *Name of this kind of price.*


Object: Pricelist Type (product.pricelist.type)
###############################################



:name: Name, char, required





:key: Key, char, required

    *Used in the code to select specific prices based on the context. Keep unchanged.*


Object: Pricelist (product.pricelist)
#####################################



:currency_id: Currency, many2one, required





:name: Pricelist Name, char, required





:magento_default: Default Magento price list, boolean

    *The price list with this box checked will be used to compute the Magento general prices (the standard prices of each product).*



:version_id: Pricelist Versions, one2many





:visible_discount: Visible Discount, boolean





:active: Active, boolean





:type: Pricelist Type, selection, required





:magento_id: Magento client group id, integer

    *You must create a client group in Magento and put its id in this field. Left 0 if you don't want to synchronize this price list.*


Object: Pricelist Version (product.pricelist.version)
#####################################################



:items_id: Price List Items, one2many, required





:name: Name, char, required





:date_end: End Date, date

    *Ending date for this pricelist version to be valid.*



:date_start: Start Date, date

    *Starting date for this pricelist version to be valid.*



:active: Active, boolean





:pricelist_id: Price List, many2one, required





:offer_name: Offer Name, char




Object: Pricelist item (product.pricelist.item)
###############################################



:price_round: Price Rounding, float

    *Sets the price so that it is a multiple of this value.
    Rounding is applied after the discount and before the surcharge.
    To have prices that end in 9.99, set rounding 10, surcharge -0.01*



:price_min_margin: Min. Price Margin, float





:name: Rule Name, char

    *Explicit rule name for this pricelist line.*



:base_pricelist_id: If Other Pricelist, many2one





:sequence: Sequence, integer, required





:price_max_margin: Max. Price Margin, float





:product_tmpl_id: Product Template, many2one

    *Set a template if this rule only apply to a template of product. Keep empty for all products*



:base: Based on, selection, required

    *The mode for computing the price for this rule.*



:price_discount: Price Discount, float





:price_version_id: Price List Version, many2one, required





:min_quantity: Min. Quantity, integer, required

    *The rule only applies if the partner buys/sells more than this quantity.*



:price_surcharge: Price Surcharge, float





:categ_id: Product Category, many2one

    *Set a category of product if this rule only apply to products of a category and his childs. Keep empty for all products*



:product_id: Product, many2one

    *Set a product if this rule only apply to one product. Keep empty for all products*
