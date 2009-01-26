Schema
======

.. image::  images/Bi_arch.png




Components
==========



The Cube
--------

The cube is based of the following component:

* A MDX parser that will transform an MDX expression to RDBMs queries:
        - Computed using a mix of:
                + Using star flow snake like in mondrian (based on joins)
                + Using space hyerarchy cutting like in cubulus
* A memory cache system
        - On space hyerarchies (dimensions with space cutting)
* An aggregation system
        - Ability to create aggregated table to speed up all queries (automatic or user-defined)
        - Queries will be computed on fact tables or aggregated tables
* A MDX Output (or several) to output the result

The cube will use:

* SQLAlchemy for all database communications

* XML-RPC for his external interfaces

* PyParser for MDX parsing

The CLI interface
-----------------

Allows user to test MDX queries in this CLI command line interface. Simple script in python
that will send XML-RPC queries and print the result.


The Cube Definition
-------------------

The meta data of the cube definition will be stored in the Open ERP database. The user interface
to edit cubes is in Open  ERP. We will use the same concept of the one defined in the ... XML standard. So that we will be able, in a futur phase, to import such files.

This must not depend on any module of Open g ERP so that if you want to use the BI library independently, you may not use Open  ERP if cubes are defined. If cubes are not defined, you just install the minimal version of Open  ERP that includes: the olap module, user management, workflow managements, access rights management, ... (the base module)

The goal is that the user never have to create the cubes himself. We will create a wizard that 
will compute cubes based on introspection on the RDBM's. The steps of this wizard:

* Selection of the database (type of db, then selection box like in the login of Open  ERP)

* Selection of the factable (selection box)

* Selection of the measures and their attributes (selection box, aggregation func)

* Selection of the dimensions (click on a tree structure)

Then it's done, the cube is computed. The aggrgated table may be also auto-matically computed by Open  ERP.

The goal is to create new cube on the fly from the Open  ERP client on every object, on user demand. This will also server the online demo server.

The cube creation can be stored in the server of kept in memory for one time usage.


The Web Client
--------------

The web client is a web-server that display cubes and provide tools to browse them, it must provide at least these operations:

* switch view

* different type of charts

* drill up/down

* slice

* dice



The OpenOffice plugin
---------------------

Similar to Palo but all operation of contruction and manipulation of cubes remains in Open  ERP to limit development on OOo. The development on OOo just contains functions to:

* Insert new data (based on selection of dimensions and filters)

* Drill up/down functions

* Slice function

The Open  ERP interface
-----------------------

From Open  ERP, you should be able to right click/drag and drop any field to trigger the cube definition wizard to create your own cube on demand. For this, we will use the web client of the bi system.

We will intergate this on the gtk and web client of Open  erp. For the GTK one, it will open the browser to browse the cube.


Extra libraries
===============

Libraries we will use:

* Turbogears for the web client to browse cube

* Mathplotlib for rendering graphs

* PyParsing to parse MDX Expressions

* SQLAlchemy to construct SQL queries and RDBMS connections

* XMLRPC lib for communication with the cube server

* PÿUNO for the OOo integration

We will use an object relationnal mapping system on all objects: dimensions, ...

