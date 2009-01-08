Creating Cube Definition using XML file
=======================================

.. describe:: Things to know

Before going through XML details its good to have an idea of all :ref:`Terminolgies <terminologies-link>`  of OLAP.

**Lets understand XML file in details**


**Step: 1. The first step is to specify the database it will use with parameter like name, database name , database login and database password**

.. code-block:: xml

   <record model="olap.fact.database" id="fact_databases_BI">
  	<field name="name">Tiny ERP databases</field>
  	<field name="db_name">SalesBI</field>
  	<field name="db_login">postgres</field>
  	<field name="db_password">postgres</field>
   </record>

* This will create the connection parameters needed for connecting to the database.

**Step: 2. Defining Schema**

.. code-block:: xml

   <record model="olap.schema" id="schema_main_sales">
  	<field name="name">tinysales</field>
  	<field name="database_id" ref="fact_databases_BI"/>
   </record>

* This will create schema name tinysales for fact_database_BI made in step 1


**Step: 3. Defining fact table to be used (In this case, sale_order_line)**

.. code-block:: xml

   <record model="olap.cube.table" id="table_sales_order_line">
  	<field name="name">sale_order_line</field>
   </record>

**Step: 4. Making Cube on fact_table**

.. code-block:: xml

   <record model="olap.cube" id="cube_sales_order_line">
  	<field name="name">sale_order_line</field>
  	<field name="table_id" ref="table_sales_order_line"/>
  	<field name="schema_id" ref="schema_main_sales"/>
   </record>

* This will create cube name sale_order_line 

**Step: 5. Creating Dimension product**

* This will used to fetch and make MDX Query on all the product 

.. code-block:: xml

   <record model="olap.dimension" id="dimension_product_template">
  	<field name="name">product</field>
  	<field name="foreign_key">product_id</field>
  	<field name="foreign_key_table">sale_order_line</field>
  	<field name="cube_id" ref="cube_sales_order_line"/>
   </record>

   <record model="olap.cube.table" id="table_product_template">
  	<field name="name">product_product</field>
   </record>

**Step: 5a. Creating Hierarchy for the Dimension Product**

.. code-block:: xml

   <record model="olap.hierarchy" id="hierarchy_product_template">
  	<field name="name">product</field>
  	<field name="field_name">name</field>
  	<field name="dimension_id" ref="dimension_product_template"/>
  	<field name="type">many2one</field>
  	<field name="primary_key_table">product_product</field>
  	<field name="table_id" ref="table_product_template"/>
   </record>

**Step: 5b  Creating Level for the Dimension Product**

.. code-block:: xml

   <record model="olap.level" id="level_product_template">
  	<field name="name">default_code</field>
  	<field name="column_name">default_code</field>
  	<field name="hierarchy_id" ref="hierarchy_product_template"/>
   </record>

**Step: 6  Creating Dimension date_order up to the quarters**

.. code-block:: xml

    <record model="olap.dimension" id="dimension_sales_order">
  	<field name="name">date_order</field>
  	<field name="foreign_key">order_id</field>
  	<field name="foreign_key_table">sale_order_line</field>
  	<field name="cube_id" ref="cube_sales_order_line"/>
     </record>
     <record model="olap.cube.table" id="table_sales_order">
  	<field name="name">sale_order</field>
     </record>
     <record model="olap.hierarchy" id="hierarchy_sales_order">
  	<field name="name">date_order</field>
  	<field name="field_name">order_date</field>
  	<field name="dimension_id" ref="dimension_sales_order"/>
  	<field name="type">many2one</field>
  	<field name="primary_key_table">sale_order</field>
  	<field name="table_id" ref="table_sales_order"/>
     </record>

Making levels in data_order so to get details as per year,quarters and months. 

.. code-block:: xml

     <record model="olap.level" id="level_sales_order">
  	<field name="name">date_order</field>
  	<field name="column_name">date_order</field>
  	<field name="column_id_name">date_order</field>
  	<field name="type">date_year</field>
  	<field name="sequence">1</field>
  	<field name="hierarchy_id" ref="hierarchy_sales_order"/>
     </record>

     <record model="olap.level" id="level_sales_order_q">
  	<field name="name">date_order</field>
  	<field name="column_name">date_order</field>
  	<field name="column_id_name">date_order</field>
  	<field name="type">date_quarter</field>
  	<field name="sequence">2</field>
  	<field name="hierarchy_id" ref="hierarchy_sales_order"/>
     </record>
     <record model="olap.level" id="level_sales_order_m">
  	<field name="name">date_order</field>
  	<field name="column_name">date_order</field>
  	<field name="column_id_name">date_order</field>
  	<field name="type">date_month</field>
  	<field name="sequence">3</field>
  	<field name="hierarchy_id" ref="hierarchy_sales_order"/>
     </record>

**Step: 7  Creating Dimension res_country**

.. code-block:: xml

     <record model="olap.cube.table" id="table_sale_order">
  	<field name="name">sale_order</field>
     </record>

     <record model="olap.cube.table" id="table_partner_address_0">
  	<field name="name">res_partner_address</field>
     </record>
     <record model="olap.cube.table" id="table_partner_address_1">
  	<field name="name">res_country</field>
     </record>

     <record model="olap.cube.table" id="table_partner_address">
  	<field name="name">res_partner_address</field>
  	<field name="table_right_id" ref="table_partner_address_1"/>
  	<field name="key_right">id</field>
  	<field name="table_left_id" ref="table_partner_address_0"/>
  	<field name="key_left">country_id</field>
     </record>



     <record model="olap.cube.table" id="table_partner_country">
  	<field name="name">sale_order_country</field>
  	<field name="table_right_id" ref="table_sale_order"/>
  	<field name="key_right">partner_id</field>
  	<field name="table_left_id" ref="table_partner_address"/>
  	<field name="key_left">partner_id</field>
     </record>

     <record model="olap.dimension" id="dimension_partner_country">
  	<field name="name">Sales From Partners</field>
  	<field name="foreign_key">order_id</field>
  	<field name="foreign_key_table">sale_order_line</field>
  	<field name="cube_id" ref="cube_sales_order_line"/>
     </record>

     <record model="olap.hierarchy" id="hierarchy_partner_country">
  	<field name="name">partner_country</field>
  	<field name="field_name">partner_id</field>
  	<field name="dimension_id" ref="dimension_partner_country"/>
  	<field name="type">many2one</field>
  	<field name="primary_key_table">sale_order</field>
  	<field name="table_id" ref="table_partner_country"/>
     </record>

     <record model="olap.level" id="level_partner_country">
  	<field name="name">country_id</field>
  	<field name="column_name">name</field>
  	<field name="column_id_name">name</field>
  	<field name="table_name">res_country</field>
  	<field name="hierarchy_id" ref="hierarchy_partner_country"/>
     </record>

**Step: 8  Creating Dimension res_parnter_address**

.. code-block:: xml

     <record model="olap.cube.table" id="table_address">
  	<field name="name">res_partner_address</field>
     </record>

     <record model="olap.cube.table" id="table_address_country">
  	<field name="name">sale_order_country</field>
  	<field name="table_right_id" ref="table_sale_order"/>
  	<field name="key_right">partner_order_id</field>
  	<field name="table_left_id" ref="table_address"/>
  	<field name="key_left">id</field>
     </record>

     <record model="olap.dimension" id="dimension_partner_address_country">
  	<field name="name">Sales by Order Address</field>
  	<field name="foreign_key">order_id</field>
  	<field name="foreign_key_table">sale_order_line</field>
  	<field name="cube_id" ref="cube_sales_order_line"/>
     </record>

     <record model="olap.hierarchy" id="hierarchy_partner_address_country">
  	<field name="name">address_country</field>
  	<field name="field_name">partner_id</field>
  	<field name="dimension_id" ref="dimension_partner_address_country"/>
  	<field name="type">many2one</field>
  	<field name="primary_key_table">sale_order</field>
  	<field name="table_id" ref="table_address_country"/>
     </record>

     <record model="olap.level" id="level_address_country">
  	<field name="name">country_id</field>
  	<field name="sequence">1</field>
  	<field name="column_name">country_id</field>
  	<field name="column_id_name">country_id</field>
  	<field name="table_name">res_partner_address</field>
  	<field name="hierarchy_id" ref="hierarchy_partner_address_country"/>
     </record>

     <record model="olap.level" id="level_address_partner">
  	<field name="name">partner_id</field>
  	<field name="sequence">2</field>
  	<field name="column_name">partner_id</field>
  	<field name="column_id_name">partner_id</field>
  	<field name="table_name">res_partner_address</field>
  	<field name="hierarchy_id" ref="hierarchy_partner_address_country"/>
      </record>


**Step: 9  Creating Dimension res_user**

.. code-block:: xml

     <record model="olap.dimension" id="dimension_sales_user">
  	<field name="name">user</field>
  	<field name="foreign_key">create_uid</field>
  	<field name="foreign_key_table">sale_order_line</field>
  	<field name="cube_id" ref="cube_sales_order_line"/>
     </record>
     <record model="olap.cube.table" id="table_sales_res_users">
  	<field name="name">res_users</field>
     </record>
     <record model="olap.hierarchy" id="hierarchy_sales_user">
  	<field name="name">user</field>
  	<field name="field_name">name</field>
  	<field name="dimension_id" ref="dimension_sales_user"/>
  	<field name="type">many2one</field>
  	<field name="primary_key_table">res_users</field>
  	<field name="table_id" ref="table_sales_res_users"/>
     </record>
     <record model="olap.level" id="hierarchy_sales_user_level">
  	<field name="name">name</field>
  	<field name="column_name">name</field>
  	<field name="hierarchy_id" ref="hierarchy_sales_user"/>
     </record>

**Step: 10  Creating Measures Item Sold and Total Sold**

.. code-block:: xml

   <record model="olap.measure" id="measure_item_sold">
  	<field name="name">Items Sold</field>
  	<field name="cube_id" ref="cube_sales_order_line"/>
  	<field name="value_column">product_uom_qty</field>
  	<field name="agregator">sum</field>
   </record>
   <record model="olap.measure" id="measure_total_sales">
  	<field name="name">Total Sold</field>
  	<field name="value_column">price_unit</field>
  	<field name="agregator">sum</field>
   </record>

