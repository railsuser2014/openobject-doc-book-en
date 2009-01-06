Connecting to an Existing Database
----------------------------------

One can very easily connect to the existing database. The details requiered are 


#. Fact Name : Logical Name of the database

#. Database Name: Pyhsical Database name to be used

#. Database type : Type of the database it can be PostgreSQL, MySQL, Oracle etc.

#. Connection type : Port or Socket

#. Database Host : Server name like localhost

#. Database Port : Port to be used for making connection to the database

#. Database Login: Login name for accessing a database

#. Database Password:Password for the user in login

------

Giving this detail will generate a string like ''postgres://postgres:postgres@localhost:5432/terp''

------

Strings so generated is a connection string for making connection to the database.

