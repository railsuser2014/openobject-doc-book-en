
.. module:: olap
    :synopsis: olap 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/olap"></div>
    <script src="http://js-kit.com/ratings.js"></script>

olap (*olap*)
=============
:Module: olap
:Name: olap
:Version: 5.0.0.1
:Author: Tiny
:Directory: olap
:Web: http://www.openerp.com
:Official module: no
:Quality certified: no

Description
-----------

::

  Base module to manage Olap schemas. Cube designer.

Download links
--------------

You can download this module as a zip file in the following version:

  * `trunk </download/modules/trunk/olap.zip>`_


Dependencies
------------

 * :mod:`base`

Reports
-------

None


Menus
-------

 * Businesss Intelligence
 * Businesss Intelligence/Configuration
 * Businesss Intelligence/Configuration/Fact Databases
 * Businesss Intelligence/Configuration/Known Application
 * Businesss Intelligence/Configuration/Olap Cubes
 * Businesss Intelligence/Configuration/Tools
 * Businesss Intelligence/Cube Browser
 * Businesss Intelligence/Cube Designer
 * Businesss Intelligence/Configuration/Tools/Clear Logs
 * Businesss Intelligence/Server Parameters
 * Businesss Intelligence/Configuration/Olap Cubes/Olap Schema
 * Businesss Intelligence/Configuration/Olap Cubes/Olap Cubes Table
 * Businesss Intelligence/Configuration/Olap Cubes/Olap Cubes
 * Businesss Intelligence/Configuration/Olap Cubes/Olap Dimension
 * Businesss Intelligence/Configuration/Olap Cubes/Olap Hierarchy
 * Businesss Intelligence/Configuration/Olap Cubes/Olap Level
 * Businesss Intelligence/Configuration/Olap Cubes/Olap Measures
 * Businesss Intelligence/Configuration/Tools/Olap Saved Query
 * Businesss Intelligence/Configuration/Tools/All Logs
 * Businesss Intelligence/Configuration/Tools/All Logs/My Logs
 * Businesss Intelligence/Configuration/Fact Databases/Databases
 * Businesss Intelligence/Configuration/Fact Databases/Tables
 * Businesss Intelligence/Configuration/Fact Databases/Columns
 * Businesss Intelligence/Configuration/Known Application/Application
 * Businesss Intelligence/Configuration/Known Application/Application Table
 * Businesss Intelligence/Configuration/Known Application/Application Field

Views
-----

 * bi.load.db.form (form)
 * Parameters Configuration (form)
 * bi.auto.configure.form (form)
 * olap.schema.tree (tree)
 * olap.schema.form (form)
 * olap.cube.table.form (form)
 * olap.cube.tree (tree)
 * olap.cube.form (form)
 * olap.dimension.tree (tree)
 * olap.dimension.form (form)
 * olap.hierarchy.tree (tree)
 * olap.hierarchy.form (form)
 * olap.level.tree (tree)
 * olap.level.form (form)
 * olap.measure.tree (tree)
 * olap.measure.form (form)
 * olap.saved.query.tree (tree)
 * olap.saved.query.mdx (mdx)
 * olap.saved.query.form (form)
 * olap.query.logs (tree)
 * olap.query.logs.form (form)
 * olap.query.logs (mdx)
 * olap.query.logs.form (form)
 * olap.fact.database.tree (tree)
 * olap.fact.database.form (form)
 * olap.database.tables.tree (tree)
 * olap.database.tables.form (form)
 * olap.database.columns.tree (tree)
 * olap.database.columns.tree.m20 (tree)
 * olap.database.columns.form (form)
 * olap.application.tree (tree)
 * olap.application.form (form)
 * olap.application.table.tree (tree)
 * olap.application.table.form (form)
 * olap.application.field.tree (tree)
 * olap.application.field.form (form)


Objects
-------

Object: Olap Fact Database (olap.fact.database)
###############################################



:connection_type: Connection type, selection, required





:connection_url: Connection URL, char, readonly





:name: Fact name, char, required





:db_password: Database password, char, required





:table_ids: Tables, one2many





:db_port: Database port, integer, required





:db_name: Database name, char, required





:db_login: Database login, char, required





:loaded: Loaded, boolean, readonly





:db_host: Database host, char, required





:type: Database type, selection, required




Object: Olap Schema (olap.schema)
#################################



:name: Schema name, char, required





:app_detect: Connection URL, char, readonly





:state: Schema State, selection, readonly





:note: Schema description, text





:ready: Ready, boolean, readonly





:database_id: Database Connection, many2one, required





:cube_ids: Cubes, one2many





:loaded: Loading Datastructure, boolean, readonly





:configure: Configuring Datastructure, boolean, readonly




Object: Olap Database Tables (olap.database.tables)
###################################################



:hide: Hidden, boolean





:name: End-User Name, char, required





:fact_database_id: Database Id, many2one, required, readonly





:table_db_name: Table Name, char, required, readonly





:active: Active, boolean





:columns: Columns, one2many




Object: Olap Database Columns (olap.database.columns)
#####################################################



:hide: Hidden, boolean





:primary_key: Primary Key, boolean





:related_to: Related To, many2one, readonly





:table_id: Table Id, many2one, required, readonly





:active: Active, boolean





:type: Type, selection, required, readonly





:column_db_name: Column DBName, char, required, readonly





:name: Column Name, char, required




Object: Olap cube table (olap.cube.table)
#########################################



:available_table_ids: Available Tables, many2many, readonly





:line_ids: Database Tables, one2many, required





:schema_id: Schema id, many2one





:name: Table name, char, required





:column_link_id: Relational Column, many2one, required




Object: Olap cube table (olap.cube.table.line)
##############################################



:field_id: Link Field, many2one





:cube_table_id: Cube Table, many2one, required





:table_id: Database Table, many2one, required




Object: Olap cube (olap.cube)
#############################



:measure_ids: Measures, one2many





:name: Cube name, char, required





:dimension_ids: Dimensions, one2many





:query_ids: Queries, one2many





:schema_id: Schema, many2one, readonly





:table_id: Fact table, many2one, required





:query_log: Query Logging, boolean




Object: Olap query logs (olap.query.logs)
#########################################



:query: Query, text, required





:result_size: Result Size, integer, readonly





:user_id: Tiny ERP User, many2one





:cube_id: Cube, many2one, required





:time: Time, datetime, required




Object: Olap dimension (olap.dimension)
#######################################



:name: Dimension name, char, required





:cube_id: Cube, many2one, required





:hierarchy_ids: Hierarchies, one2many




Object: Olap hierarchy (olap.hierarchy)
#######################################



:name: Hierarchy name, char, required





:sequence: Sequence, integer, required





:dimension_id: Dimension, many2one, required





:primary_key_table: Primary key table, char





:table_id: Fact table(s), many2one, required





:level_ids: Levels, one2many





:primary_key: Primary key, char




Object: Olap level (olap.level)
###############################



:column_id_name: Column ID, char, required





:name: Level name, char, required





:sequence: Sequence, integer, required





:table_name: Table name, char, required

    *The name of the table on which the column is defined. If False, take the table from the hierarchy.*



:hierarchy_id: Hierarchy, many2one, required





:type: Level class, selection, required





:column_name: Columns Name, many2one, required




Object: Olap measure (olap.measure)
###################################



:value_sql: SQL Expression, char

    *You can provide valid sql expression. Make sure it have function with fully qualified column name like (sum,avg ...)(tablename.columnname (+,- ...) tablename.columnname)*



:name: Measure name, char, required





:cube_id: Cube, many2one, required





:datatype: Datatype, selection, required





:formatstring: Format string, selection, required





:table_name: Table name, char

    *The name of the table on which the column is defined. If False, take the table from the cube.*



:agregator: Agregator, selection, required





:value_column: Fact Table Column, many2one





:measure_type: Measure Type, selection, required

    *Select between auto column or sql expression for the measures*



:value_column_id_name: Column ID, char




Object: Olap application (olap.application)
###########################################



:query: Application Query, text





:field_ids: Fields, one2many





:name: Application name, char, required





:table_ids: Tables, one2many




Object: Olap application table (olap.application.table)
#######################################################



:application_id: Application Id, many2one, required





:is_hidden: Hidden, boolean





:table_name: Table name, char, required





:name: Application table name, char, required




Object: Olap application field (olap.application.field)
#######################################################



:field_name: Field name, char





:table_name: Application table name, char





:is_hidden: Hidden, boolean





:application_id: Application Id, many2one, required





:name: Application field name, char, required




Object: olap.saved.query (olap.saved.query)
###########################################



:user_id: User, many2one





:name: Query Name, text





:cube_id: Cube, many2one, required





:schema_id: Schema, many2one, required





:time: Time, datetime, required





:query: Query, text, required




Object: bi.load.db.wizard (bi.load.db.wizard)
#############################################



:db_name: Database Name, char, readonly





:fact_table: Fact Name, char, readonly




Object: bi.auto.configure.wizard (bi.auto.configure.wizard)
###########################################################



:name: Fact Name, char, readonly




Object: Olap Server Parameters (olap.parameters.config.wizard)
##############################################################



:host_port: Port, char, required

    *Put the port for the server. Put 8080 if                 its not clear.*



:host_name: Server Name, char, required

    *Put here the server address or IP                 Put localhost if its not clear.*
