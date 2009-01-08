MDXOverview
===========

MDX stands for Multidimensional Expressions. You use it to query OLAP databases. In a nutshell, MDX is to OLAP databases as SQL queries are to relational databases. 

OLAP databases primarily consist of OLAP cubes, which store fact tables, measures (such as sales, purchase, etc.) and dimensions/hierarchies. An OLAP database is often an aggregation of a relational database; as a result, you can write MDX queries to retrieve key calculations that measure company performance, often with less code than standard SQL. 

Because of the nature of OLAP databases, we need to write MDX code to retrieve data in far fewer lines of code than would be required using SQL. This is a segue into the role that OLAP databases and MDX play in the world of business intelligence. 

MDXAlchemy is developed taking care of all the aspects of becoming a complete OLAP Engine, to execute MDX query and fetch data efficiently. MDXAlchemy is a complete MDX engine that provides your database with full MDX capabilities. 

MDXAlchemy use the services of SQLAlchemy to provide few of important feature that makes MDXAlchemy a full capable MDX Engine. The major is removing the clause of database dependency. 

The dimensional meta data facility addresses the issue that although this application store dimensional data in relational tables (usually in the form of fact and dimension tables), the user doesnot have to worry for database not aware of the dimensionality, or OLAP semantics, of this data. It provides a comprehensive meta data facility to define these semantics and an XML capability to enable meta data interchange with other external OLAP products.


