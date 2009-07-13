
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/product"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/product"></div>
    <script src="http://js-kit.com/ratings.js"></script>

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
.. i18n:   This is the base module for managing products and pricelists in Open ERP.
.. i18n:   
.. i18n:       Products support variants, different pricing methods, suppliers
.. i18n:       information, make to stock/order, different unit of measures,
.. i18n:       packaging and properties.
.. i18n:   
.. i18n:       Pricelists support:
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

.. i18n: Download links
.. i18n: --------------

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:

You can download this module as a zip file in the following version:

.. i18n:   * `4.2 <http://www.openerp.com/download/modules/4.2/product.zip>`_
.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/product.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/product.zip>`_

  * `4.2 <http://www.openerp.com/download/modules/4.2/product.zip>`_
  * `5.0 <http://www.openerp.com/download/modules/5.0/product.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/product.zip>`_

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

.. i18n:  * Products
.. i18n:  * Products/Configuration
.. i18n:  * Products/Products
.. i18n:  * Products/Products by Category
.. i18n:  * Products/Configuration/Products Categories
.. i18n:  * Products/Configuration/Units of Measure
.. i18n:  * Products/Configuration/Units of Measure/Units of Measure
.. i18n:  * Products/Configuration/Units of Measure/Units of Measure Categories
.. i18n:  * Products/Configuration/Packaging
.. i18n:  * Products/Pricelists
.. i18n:  * Products/Pricelists/Pricelist Versions
.. i18n:  * Products/Pricelists/Pricelists
.. i18n:  * Products/Configuration/Prices Computations
.. i18n:  * Products/Configuration/Prices Computations/Prices Types
.. i18n:  * Products/Configuration/Prices Computations/Pricelists Types

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

.. i18n: :factor_inv: Factor, float, readonly

:factor_inv: Factor, float, readonly

.. i18n:     *The coefficient for the formula:
.. i18n:     coeff (base unit) = 1 (this unit). Factor = 1 / Rate.*

    *The coefficient for the formula:
    coeff (base unit) = 1 (this unit). Factor = 1 / Rate.*

.. i18n: :rounding: Rounding Precision, float, required

:rounding: Rounding Precision, float, required

.. i18n:     *The computed quantity will be a multiple of this value. Use 1.0 for products that can not be split.*

    *The computed quantity will be a multiple of this value. Use 1.0 for products that can not be split.*

.. i18n: :factor: Rate, float, required

:factor: Rate, float, required

.. i18n:     *The coefficient for the formula:
.. i18n:     1 (base unit) = coeff (this unit). Rate = 1 / Factor.*

    *The coefficient for the formula:
    1 (base unit) = coeff (this unit). Rate = 1 / Factor.*

.. i18n: :active: Active, boolean

:active: Active, boolean

.. i18n: :category_id: UoM Category, many2one, required

:category_id: UoM Category, many2one, required

.. i18n:     *Unit of Measure of a category can be converted between each others in the same category.*

    *Unit of Measure of a category can be converted between each others in the same category.*

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

.. i18n: :sequence: Sequence, integer

:sequence: Sequence, integer

.. i18n: :updated: Category updated on Magento, boolean

:updated: Category updated on Magento, boolean

.. i18n: :child_id: Child Categories, one2many

:child_id: Child Categories, one2many

.. i18n: :property_stock_account_input_categ: Stock Input Account, many2one

:property_stock_account_input_categ: Stock Input Account, many2one

.. i18n:     *This account will be used to value the input stock*

    *This account will be used to value the input stock*

.. i18n: :property_stock_account_output_categ: Stock Output Account, many2one

:property_stock_account_output_categ: Stock Output Account, many2one

.. i18n:     *This account will be used to value the output stock*

    *This account will be used to value the output stock*

.. i18n: :isactivitytype: Is Activity Type, boolean

:isactivitytype: Is Activity Type, boolean

.. i18n: :exportable: Export to website, boolean

:exportable: Export to website, boolean

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

.. i18n: :magento_product_type: Magento product type, integer

:magento_product_type: Magento product type, integer

.. i18n: :isamenitype: Is amenities Type, boolean

:isamenitype: Is amenities Type, boolean

.. i18n: :property_account_income_europe: Income Account for Europe, many2one

:property_account_income_europe: Income Account for Europe, many2one

.. i18n:     *This account will be used, instead of the default one, to value incoming stock for the current product*

    *This account will be used, instead of the default one, to value incoming stock for the current product*

.. i18n: :property_account_expense_categ: Expense Account, many2one

:property_account_expense_categ: Expense Account, many2one

.. i18n:     *This account will be used to value outgoing stock for the current product category*

    *This account will be used to value outgoing stock for the current product category*

.. i18n: :property_stock_journal: Stock journal, many2one

:property_stock_journal: Stock journal, many2one

.. i18n:     *This journal will be used for the accounting move generated by stock move*

    *This journal will be used for the accounting move generated by stock move*

.. i18n: :magento_product_attribute_set_id: Magento product attribute set id, integer

:magento_product_attribute_set_id: Magento product attribute set id, integer

.. i18n: :property_account_expense_europe: Expense Account for Europe, many2one

:property_account_expense_europe: Expense Account for Europe, many2one

.. i18n:     *This account will be used, instead of the default one, to value outgoing stock for the current product*

    *This account will be used, instead of the default one, to value outgoing stock for the current product*

.. i18n: :property_account_income_categ: Income Account, many2one

:property_account_income_categ: Income Account, many2one

.. i18n:     *This account will be used to value incoming stock for the current product category*

    *This account will be used to value incoming stock for the current product category*

.. i18n: :property_account_expense_world: Outside Europe Expense Account, many2one

:property_account_expense_world: Outside Europe Expense Account, many2one

.. i18n:     *This account will be used, instead of the default one, to value outgoing stock for the current product*

    *This account will be used, instead of the default one, to value outgoing stock for the current product*

.. i18n: :isroomtype: Is Room Type, boolean

:isroomtype: Is Room Type, boolean

.. i18n: :name: Name, char, required

:name: Name, char, required

.. i18n: :magento_id: Magento category id, integer

:magento_id: Magento category id, integer

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

.. i18n:     *The cost of the product for accounting stock valuation. It can serves as a base price for supplier price.*

    *The cost of the product for accounting stock valuation. It can serves as a base price for supplier price.*

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

.. i18n:     *This account will be used instead of the default one to value incoming stock for the current product*

    *This account will be used instead of the default one to value incoming stock for the current product*

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

.. i18n: :produce_delay: Manufacturing Lead Time, float

:produce_delay: Manufacturing Lead Time, float

.. i18n:     *Average time to produce this product. This is only for the production order and, if it is a multi-level bill of material, it's only for the level of this product. Different delays will be summed for all levels and purchase orders.*

    *Average time to produce this product. This is only for the production order and, if it is a multi-level bill of material, it's only for the level of this product. Different delays will be summed for all levels and purchase orders.*

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

.. i18n: :picture: picture, binary

:picture: picture, binary

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

.. i18n: :dimension_type_ids: Dimension Types, one2many

:dimension_type_ids: Dimension Types, one2many

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

.. i18n: :loc_row: Row, char

:loc_row: Row, char

.. i18n: :seller_delay: Supplier Lead Time, integer, readonly

:seller_delay: Supplier Lead Time, integer, readonly

.. i18n:     *This is the average delay in days between the purchase order confirmation and the reception of goods for this product and for the default supplier. It is used by the scheduler to order requests based on reordering delays.*

    *This is the average delay in days between the purchase order confirmation and the reception of goods for this product and for the default supplier. It is used by the scheduler to order requests based on reordering delays.*

.. i18n: :rental: Rentable Product, boolean

:rental: Rentable Product, boolean

.. i18n: :sale_delay: Customer Lead Time, float

:sale_delay: Customer Lead Time, float

.. i18n:     *This is the average time between the confirmation of the customer order and the delivery of the finished products. It's the time you promise to your customers.*

    *This is the average time between the confirmation of the customer order and the delivery of the finished products. It's the time you promise to your customers.*

.. i18n: :name: Name, char, required

:name: Name, char, required

.. i18n: :description_sale: Sale Description, text

:description_sale: Sale Description, text

.. i18n: :property_account_expense: Expense Account, many2one

:property_account_expense: Expense Account, many2one

.. i18n:     *This account will be used instead of the default one to value outgoing stock for the current product*

    *This account will be used instead of the default one to value outgoing stock for the current product*

.. i18n: :categ_id: Category, many2one, required

:categ_id: Category, many2one, required

.. i18n: :variant_ids: Variants, one2many

:variant_ids: Variants, one2many

.. i18n: :taxes_id: Product Taxes, many2many

:taxes_id: Product Taxes, many2many

.. i18n: :property_stock_account_output: Stock Output Account, many2one

:property_stock_account_output: Stock Output Account, many2one

.. i18n:     *This account will be used, instead of the default one, to value output stock*

    *This account will be used, instead of the default one, to value output stock*

.. i18n: :seller_ids: Partners, one2many

:seller_ids: Partners, one2many

.. i18n: Object: Product (product.product)
.. i18n: #################################

Object: Product (product.product)
#################################

.. i18n: :ean13: EAN, char

:ean13: EAN, char

.. i18n:     *Barcode number for EAN8 EAN13 UPC JPC GTIN http://de.wikipedia.org/wiki/Global_Trade_Item_Number*

    *Barcode number for EAN8 EAN13 UPC JPC GTIN http://de.wikipedia.org/wiki/Global_Trade_Item_Number*

.. i18n: :characteristic_ids: Characteristics, many2many

:characteristic_ids: Characteristics, many2many

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

.. i18n:     *The cost of the product for accounting stock valuation. It can serves as a base price for supplier price.*

    *The cost of the product for accounting stock valuation. It can serves as a base price for supplier price.*

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

.. i18n:     *This account will be used instead of the default one to value incoming stock for the current product*

    *This account will be used instead of the default one to value incoming stock for the current product*

.. i18n: :isbn: Isbn code, char

:isbn: Isbn code, char

.. i18n: :index_sale: Sales indexes, many2many

:index_sale: Sales indexes, many2many

.. i18n: :author_om_ids: Authors, one2many

:author_om_ids: Authors, one2many

.. i18n: :company_id: Company, many2one

:company_id: Company, many2one

.. i18n: :num_pocket: Collection Num., char

:num_pocket: Collection Num., char

.. i18n: :loc_rack: Rack, char

:loc_rack: Rack, char

.. i18n: :ismenucard: Is Room, boolean

:ismenucard: Is Room, boolean

.. i18n: :manufacturer_id:  Manufacturer, many2one

:manufacturer_id:  Manufacturer, many2one

.. i18n: :price_margin: Variant Price Margin, float

:price_margin: Variant Price Margin, float

.. i18n: :property_stock_account_input: Stock Input Account, many2one

:property_stock_account_input: Stock Input Account, many2one

.. i18n:     *This account will be used, instead of the default one, to value input stock*

    *This account will be used, instead of the default one, to value input stock*

.. i18n: :updated: Product updated on Magento, boolean

:updated: Product updated on Magento, boolean

.. i18n: :pricelist_sale: Sale Pricelists, text, readonly

:pricelist_sale: Sale Pricelists, text, readonly

.. i18n: :format: Format, char

:format: Format, char

.. i18n: :pocket: Pocket, char

:pocket: Pocket, char

.. i18n: :is_direct_delivery_from_product: Is Supplier Direct Delivery Automatic?, boolean, readonly

:is_direct_delivery_from_product: Is Supplier Direct Delivery Automatic?, boolean, readonly

.. i18n: :outgoing_qty: Outgoing, float, readonly

:outgoing_qty: Outgoing, float, readonly

.. i18n:     *Quantities of products that are planned to leave in selected locations or all internal if none have been selected.*

    *Quantities of products that are planned to leave in selected locations or all internal if none have been selected.*

.. i18n: :sale_num_invoiced: # Invoiced, float, readonly

:sale_num_invoiced: # Invoiced, float, readonly

.. i18n:     *Sum of Quantity in Customer Invoices*

    *Sum of Quantity in Customer Invoices*

.. i18n: :variants: Variants, char, readonly

:variants: Variants, char, readonly

.. i18n: :partner_ref: Customer ref, char, readonly

:partner_ref: Customer ref, char, readonly

.. i18n: :rental: Rentable Product, boolean

:rental: Rentable Product, boolean

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

.. i18n: :editor: Editor, many2one

:editor: Editor, many2one

.. i18n: :dimension_value_ids: Dimensions, many2many

:dimension_value_ids: Dimensions, many2many

.. i18n: :seller_ids: Partners, one2many

:seller_ids: Partners, one2many

.. i18n: :date_available: Available Date, date

:date_available: Available Date, date

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

.. i18n: :series: Series, many2one

:series: Series, many2one

.. i18n: :lot_ids: Lots, one2many

:lot_ids: Lots, one2many

.. i18n: :back: Reliure, selection

:back: Reliure, selection

.. i18n: :creation_date: Creation date, datetime, readonly

:creation_date: Creation date, datetime, readonly

.. i18n: :product_url: URL, char

:product_url: URL, char

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

.. i18n: :language_id: Language, many2one

:language_id: Language, many2one

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

.. i18n: :magento_tax_class_id: Magento tax class id, integer

:magento_tax_class_id: Magento tax class id, integer

.. i18n: :sale_avg_price: Avg. Unit Price, float, readonly

:sale_avg_price: Avg. Unit Price, float, readonly

.. i18n:     *Avg. Price in Customer Invoices)*

    *Avg. Price in Customer Invoices)*

.. i18n: :manufacturer_pname: Manufacturer product name, char

:manufacturer_pname: Manufacturer product name, char

.. i18n: :country_ids: Allowed Countries, many2many

:country_ids: Allowed Countries, many2many

.. i18n: :image_name: Image name, char

:image_name: Image name, char

.. i18n:     *Image name created by Magento*

    *Image name created by Magento*

.. i18n: :partner_ref2: Customer ref, char, readonly

:partner_ref2: Customer ref, char, readonly

.. i18n: :dimension_type_ids: Dimension Types, one2many

:dimension_type_ids: Dimension Types, one2many

.. i18n: :hr_expense_ok: Can be Expensed, boolean

:hr_expense_ok: Can be Expensed, boolean

.. i18n:     *Determine if the product can be visible in the list of product within a selection from an HR expense sheet line.*

    *Determine if the product can be visible in the list of product within a selection from an HR expense sheet line.*

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

.. i18n: :spe_price: Special price, char

:spe_price: Special price, char

.. i18n: :index_purchase: Purchase indexes, many2many

:index_purchase: Purchase indexes, many2many

.. i18n: :loc_case: Case, char

:loc_case: Case, char

.. i18n: :property_stock_account_output: Stock Output Account, many2one

:property_stock_account_output: Stock Output Account, many2one

.. i18n:     *This account will be used, instead of the default one, to value output stock*

    *This account will be used, instead of the default one, to value output stock*

.. i18n: :danger_ids: Dangers products, many2many

:danger_ids: Dangers products, many2many

.. i18n: :securite_ids: Security, many2many

:securite_ids: Security, many2many

.. i18n: :length: Length, float

:length: Length, float

.. i18n: :catalog_num: Catalog number, char

:catalog_num: Catalog number, char

.. i18n: :tome: Tome, char

:tome: Tome, char

.. i18n: :magento_id: Magento product id, integer

:magento_id: Magento product id, integer

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

.. i18n: :image: Image, binary

:image: Image, binary

.. i18n:     *Image of the product (jpg or png). The same image will be set as thumbnail, small image and normal image. To change the product image, first delete the old one and save the product and then add the new one and save the product. Note that this image is optional, it can be left empty and manage the product images from Magento.*

    *Image of the product (jpg or png). The same image will be set as thumbnail, small image and normal image. To change the product image, first delete the old one and save the product and then add the new one and save the product. Note that this image is optional, it can be left empty and manage the product images from Magento.*

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

.. i18n: :exp_date: Expiry date, datetime

:exp_date: Expiry date, datetime

.. i18n: :risque_ids: Risk products, many2many

:risque_ids: Risk products, many2many

.. i18n: :qty_available: Real Stock, float, readonly

:qty_available: Real Stock, float, readonly

.. i18n:     *Current quantities of products in selected locations or all internal if none have been selected.*

    *Current quantities of products in selected locations or all internal if none have been selected.*

.. i18n: :use_time: Product usetime, integer

:use_time: Product usetime, integer

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

.. i18n: :purchase_ok: Can be Purchased, boolean

:purchase_ok: Can be Purchased, boolean

.. i18n:     *Determine if the product is visible in the list of products within a selection from a purchase order line.*

    *Determine if the product is visible in the list of products within a selection from a purchase order line.*

.. i18n: :product_manager: Product Manager, many2one

:product_manager: Product Manager, many2one

.. i18n: :characteristic_group_ids: Characteristic groups, many2many

:characteristic_group_ids: Characteristic groups, many2many

.. i18n: :width: Width, float

:width: Width, float

.. i18n: :rough_drawing: rough drawing, binary

:rough_drawing: rough drawing, binary

.. i18n: :normal_cost: Normal Cost, float, readonly

:normal_cost: Normal Cost, float, readonly

.. i18n:     *Sum of Multification of Cost price and quantity of Supplier Invoices*

    *Sum of Multification of Cost price and quantity of Supplier Invoices*

.. i18n: :manufacturer: Manufacturer, many2one

:manufacturer: Manufacturer, many2one

.. i18n: :type: Product Type, selection, required

:type: Product Type, selection, required

.. i18n:     *Will change the way procurements are processed. Consumables are stockable products with infinite stock, or for use when you have no stock management in the system.*

    *Will change the way procurements are processed. Consumables are stockable products with infinite stock, or for use when you have no stock management in the system.*

.. i18n: :property_account_income_europe: Income Account for Europe, many2one

:property_account_income_europe: Income Account for Europe, many2one

.. i18n:     *This account will be used, instead of the default one, to value incoming stock for the current product*

    *This account will be used, instead of the default one, to value incoming stock for the current product*

.. i18n: :schema: schema, binary

:schema: schema, binary

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

.. i18n: :volume: Volume, float

:volume: Volume, float

.. i18n:     *The volume in m3.*

    *The volume in m3.*

.. i18n: :package_weight: Package Weight, float

:package_weight: Package Weight, float

.. i18n: :membership_date_from: Date from, date

:membership_date_from: Date from, date

.. i18n: :date_to: To Date, date, readonly

:date_to: To Date, date, readonly

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

.. i18n: :sale_delay: Customer Lead Time, float

:sale_delay: Customer Lead Time, float

.. i18n:     *This is the average time between the confirmation of the customer order and the delivery of the finished products. It's the time you promise to your customers.*

    *This is the average time between the confirmation of the customer order and the delivery of the finished products. It's the time you promise to your customers.*

.. i18n: :description_sale: Sale Description, text

:description_sale: Sale Description, text

.. i18n: :purchase_line_warn: Purchase Order Line, selection

:purchase_line_warn: Purchase Order Line, selection

.. i18n:     *Selecting the "Warning" option will notify user with the message, Selecting "Blocking Message" will throw an exception with the message and block the flow. The Message has to be written in the next field.*

    *Selecting the "Warning" option will notify user with the message, Selecting "Blocking Message" will throw an exception with the message and block the flow. The Message has to be written in the next field.*

.. i18n: :state_ids: Allowed States, many2many

:state_ids: Allowed States, many2many

.. i18n: :product_picture: Product Picture, char

:product_picture: Product Picture, char

.. i18n: :purchase_gap: Purchase Gap, float, readonly

:purchase_gap: Purchase Gap, float, readonly

.. i18n:     *Normal Cost - Total Cost*

    *Normal Cost - Total Cost*

.. i18n: :sale_line_warn: Sale Order Line, selection

:sale_line_warn: Sale Order Line, selection

.. i18n:     *Selecting the "Warning" option will notify user with the message, Selecting "Blocking Message" will throw an exception with the message and block the flow. The Message has to be written in the next field.*

    *Selecting the "Warning" option will notify user with the message, Selecting "Blocking Message" will throw an exception with the message and block the flow. The Message has to be written in the next field.*

.. i18n: :isservice: Is Service id, boolean

:isservice: Is Service id, boolean

.. i18n: :track_production: Track Production Lots, boolean

:track_production: Track Production Lots, boolean

.. i18n:     *Force to use a Production Lot during production order*

    *Force to use a Production Lot during production order*

.. i18n: :oscom_url: URL to OScommerce, char, readonly

:oscom_url: URL to OScommerce, char, readonly

.. i18n: :nbpage: Number of pages, integer

:nbpage: Number of pages, integer

.. i18n: :spe_price_status: Status, selection

:spe_price_status: Status, selection

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

.. i18n: :image_label: Image label, char

:image_label: Image label, char

.. i18n:     *Image label in the website. Left empty to take the product name as image label.*

    *Image label in the website. Left empty to take the product name as image label.*

.. i18n: :exportable: Export to website, boolean

:exportable: Export to website, boolean

.. i18n: :life_cycle: Life Cycle, selection

:life_cycle: Life Cycle, selection

.. i18n: :auto_picking: Auto Picking for Production, boolean

:auto_picking: Auto Picking for Production, boolean

.. i18n: :date_from: From Date, date, readonly

:date_from: From Date, date, readonly

.. i18n: :track_outgoing: Track Outging Lots, boolean

:track_outgoing: Track Outging Lots, boolean

.. i18n:     *Force to use a Production Lot during deliveries*

    *Force to use a Production Lot during deliveries*

.. i18n: :lst_price: List Price, float, readonly

:lst_price: List Price, float, readonly

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

.. i18n: :picture: Image, binary

:picture: Image, binary

.. i18n: :maintenance_analytic_id: Maintenance Analytic Account, many2one

:maintenance_analytic_id: Maintenance Analytic Account, many2one

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

.. i18n: :in_out_stock: In/Out Stock, selection

:in_out_stock: In/Out Stock, selection

.. i18n: :categ_id: Category, many2one, required

:categ_id: Category, many2one, required

.. i18n: :lang: Language, many2many

:lang: Language, many2many

.. i18n: :removal_time: Product removal time, integer

:removal_time: Product removal time, integer

.. i18n: :link_ids: Related Books, many2many

:link_ids: Related Books, many2many

.. i18n: :equivalency_in_A4: A4 Equivalency, float

:equivalency_in_A4: A4 Equivalency, float

.. i18n: :produce_delay: Manufacturing Lead Time, float

:produce_delay: Manufacturing Lead Time, float

.. i18n:     *Average time to produce this product. This is only for the production order and, if it is a multi-level bill of material, it's only for the level of this product. Different delays will be summed for all levels and purchase orders.*

    *Average time to produce this product. This is only for the production order and, if it is a multi-level bill of material, it's only for the level of this product. Different delays will be summed for all levels and purchase orders.*

.. i18n: :property_account_expense: Expense Account, many2one

:property_account_expense: Expense Account, many2one

.. i18n:     *This account will be used instead of the default one to value outgoing stock for the current product*

    *This account will be used instead of the default one to value outgoing stock for the current product*

.. i18n: :calculate_price: Compute price, boolean

:calculate_price: Compute price, boolean

.. i18n: :invoice_state: Invoice State, selection, readonly

:invoice_state: Invoice State, selection, readonly

.. i18n: :variant_ids: Variants, one2many

:variant_ids: Variants, one2many

.. i18n: :cutting: Can be Cutted, boolean

:cutting: Can be Cutted, boolean

.. i18n: :alert_time: Product alert time, integer

:alert_time: Product alert time, integer

.. i18n: :taxes_id: Product Taxes, many2many

:taxes_id: Product Taxes, many2many

.. i18n: :date_parution: Release date, date

:date_parution: Release date, date

.. i18n: :total_margin: Total Margin, float, readonly

:total_margin: Total Margin, float, readonly

.. i18n:     *Turnorder - Total Cost*

    *Turnorder - Total Cost*

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

.. i18n: :currency_id: Currency, many2one, required

:currency_id: Currency, many2one, required

.. i18n: :name: Pricelist Name, char, required

:name: Pricelist Name, char, required

.. i18n: :magento_default: Default Magento price list, boolean

:magento_default: Default Magento price list, boolean

.. i18n:     *The price list with this box checked will be used to compute the Magento general prices (the standard prices of each product).*

    *The price list with this box checked will be used to compute the Magento general prices (the standard prices of each product).*

.. i18n: :version_id: Pricelist Versions, one2many

:version_id: Pricelist Versions, one2many

.. i18n: :visible_discount: Visible Discount, boolean

:visible_discount: Visible Discount, boolean

.. i18n: :active: Active, boolean

:active: Active, boolean

.. i18n: :type: Pricelist Type, selection, required

:type: Pricelist Type, selection, required

.. i18n: :magento_id: Magento client group id, integer

:magento_id: Magento client group id, integer

.. i18n:     *You must create a client group in Magento and put its id in this field. Left 0 if you don't want to synchronize this price list.*

    *You must create a client group in Magento and put its id in this field. Left 0 if you don't want to synchronize this price list.*

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

.. i18n:     *Ending date for this pricelist version to be valid.*

    *Ending date for this pricelist version to be valid.*

.. i18n: :date_start: Start Date, date

:date_start: Start Date, date

.. i18n:     *Starting date for this pricelist version to be valid.*

    *Starting date for this pricelist version to be valid.*

.. i18n: :active: Active, boolean

:active: Active, boolean

.. i18n: :pricelist_id: Price List, many2one, required

:pricelist_id: Price List, many2one, required

.. i18n: :offer_name: Offer Name, char

:offer_name: Offer Name, char

.. i18n: Object: Pricelist item (product.pricelist.item)
.. i18n: ###############################################

Object: Pricelist item (product.pricelist.item)
###############################################

.. i18n: :price_round: Price Rounding, float

:price_round: Price Rounding, float

.. i18n:     *Sets the price so that it is a multiple of this value.
.. i18n:     Rounding is applied after the discount and before the surcharge.
.. i18n:     To have prices that end in 9.99, set rounding 10, surcharge -0.01*

    *Sets the price so that it is a multiple of this value.
    Rounding is applied after the discount and before the surcharge.
    To have prices that end in 9.99, set rounding 10, surcharge -0.01*

.. i18n: :price_min_margin: Min. Price Margin, float

:price_min_margin: Min. Price Margin, float

.. i18n: :name: Rule Name, char

:name: Rule Name, char

.. i18n:     *Explicit rule name for this pricelist line.*

    *Explicit rule name for this pricelist line.*

.. i18n: :base_pricelist_id: If Other Pricelist, many2one

:base_pricelist_id: If Other Pricelist, many2one

.. i18n: :sequence: Sequence, integer, required

:sequence: Sequence, integer, required

.. i18n: :price_max_margin: Max. Price Margin, float

:price_max_margin: Max. Price Margin, float

.. i18n: :product_tmpl_id: Product Template, many2one

:product_tmpl_id: Product Template, many2one

.. i18n:     *Set a template if this rule only apply to a template of product. Keep empty for all products*

    *Set a template if this rule only apply to a template of product. Keep empty for all products*

.. i18n: :base: Based on, selection, required

:base: Based on, selection, required

.. i18n:     *The mode for computing the price for this rule.*

    *The mode for computing the price for this rule.*

.. i18n: :price_discount: Price Discount, float

:price_discount: Price Discount, float

.. i18n: :price_version_id: Price List Version, many2one, required

:price_version_id: Price List Version, many2one, required

.. i18n: :min_quantity: Min. Quantity, integer, required

:min_quantity: Min. Quantity, integer, required

.. i18n:     *The rule only applies if the partner buys/sells more than this quantity.*

    *The rule only applies if the partner buys/sells more than this quantity.*

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
