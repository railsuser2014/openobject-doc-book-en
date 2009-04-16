
.. i18n: Schema
.. i18n: ======

Schema
======

.. i18n: .. image::  images/Bi_arch.png

.. image::  images/Bi_arch.png

.. i18n: Components
.. i18n: ==========

Components
==========

.. i18n: The Cube
.. i18n: --------

The Cube
--------

.. i18n: The cube is based of the following component:

The cube is based of the following component:

.. i18n: * A MDX parser that will transform an MDX expression to RDBMs queries:
.. i18n:         - Computed using a mix of:
.. i18n:                 + Using star flow snake like in mondrian (based on joins)
.. i18n:                 + Using space hyerarchy cutting like in cubulus
.. i18n: * A memory cache system
.. i18n:         - On space hyerarchies (dimensions with space cutting)
.. i18n: * An aggregation system
.. i18n:         - Ability to create aggregated table to speed up all queries (automatic or user-defined)
.. i18n:         - Queries will be computed on fact tables or aggregated tables
.. i18n: * A MDX Output (or several) to output the result

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

.. i18n: The cube will use:

The cube will use:

.. i18n: * SQLAlchemy for all database communications
.. i18n: 
.. i18n: * XML-RPC for his external interfaces
.. i18n: 
.. i18n: * PyParser for MDX parsing

* SQLAlchemy for all database communications

* XML-RPC for his external interfaces

* PyParser for MDX parsing

.. i18n: The CLI interface
.. i18n: -----------------

The CLI interface
-----------------

.. i18n: Allows user to test MDX queries in this CLI command line interface. Simple script in python
.. i18n: that will send XML-RPC queries and print the result.

Allows user to test MDX queries in this CLI command line interface. Simple script in python
that will send XML-RPC queries and print the result.

.. i18n: The Cube Definition
.. i18n: -------------------

The Cube Definition
-------------------

.. i18n: The meta data of the cube definition will be stored in the Open ERP database. The user interface
.. i18n: to edit cubes is in Open  ERP. We will use the same concept of the one defined in the ... XML standard. So that we will be able, in a futur phase, to import such files.

The meta data of the cube definition will be stored in the Open ERP database. The user interface
to edit cubes is in Open  ERP. We will use the same concept of the one defined in the ... XML standard. So that we will be able, in a futur phase, to import such files.

.. i18n: This must not depend on any module of Open g ERP so that if you want to use the BI library independently, you may not use Open  ERP if cubes are defined. If cubes are not defined, you just install the minimal version of Open  ERP that includes: the olap module, user management, workflow managements, access rights management, ... (the base module)

This must not depend on any module of Open g ERP so that if you want to use the BI library independently, you may not use Open  ERP if cubes are defined. If cubes are not defined, you just install the minimal version of Open  ERP that includes: the olap module, user management, workflow managements, access rights management, ... (the base module)

.. i18n: The goal is that the user never have to create the cubes himself. We will create a wizard that 
.. i18n: will compute cubes based on introspection on the RDBM's. The steps of this wizard:

The goal is that the user never have to create the cubes himself. We will create a wizard that 
will compute cubes based on introspection on the RDBM's. The steps of this wizard:

.. i18n: * Selection of the database (type of db, then selection box like in the login of Open  ERP)
.. i18n: 
.. i18n: * Selection of the factable (selection box)
.. i18n: 
.. i18n: * Selection of the measures and their attributes (selection box, aggregation func)
.. i18n: 
.. i18n: * Selection of the dimensions (click on a tree structure)

* Selection of the database (type of db, then selection box like in the login of Open  ERP)

* Selection of the factable (selection box)

* Selection of the measures and their attributes (selection box, aggregation func)

* Selection of the dimensions (click on a tree structure)

.. i18n: Then it's done, the cube is computed. The aggrgated table may be also auto-matically computed by Open  ERP.

Then it's done, the cube is computed. The aggrgated table may be also auto-matically computed by Open  ERP.

.. i18n: The goal is to create new cube on the fly from the Open  ERP client on every object, on user demand. This will also server the online demo server.

The goal is to create new cube on the fly from the Open  ERP client on every object, on user demand. This will also server the online demo server.

.. i18n: The cube creation can be stored in the server of kept in memory for one time usage.

The cube creation can be stored in the server of kept in memory for one time usage.

.. i18n: The Web Client
.. i18n: --------------

The Web Client
--------------

.. i18n: The web client is a web-server that display cubes and provide tools to browse them, it must provide at least these operations:

The web client is a web-server that display cubes and provide tools to browse them, it must provide at least these operations:

.. i18n: * switch view
.. i18n: 
.. i18n: * different type of charts
.. i18n: 
.. i18n: * drill up/down
.. i18n: 
.. i18n: * slice
.. i18n: 
.. i18n: * dice

* switch view

* different type of charts

* drill up/down

* slice

* dice

.. i18n: The OpenOffice plugin
.. i18n: ---------------------

The OpenOffice plugin
---------------------

.. i18n: Similar to Palo but all operation of contruction and manipulation of cubes remains in Open  ERP to limit development on OOo. The development on OOo just contains functions to:

Similar to Palo but all operation of contruction and manipulation of cubes remains in Open  ERP to limit development on OOo. The development on OOo just contains functions to:

.. i18n: * Insert new data (based on selection of dimensions and filters)
.. i18n: 
.. i18n: * Drill up/down functions
.. i18n: 
.. i18n: * Slice function

* Insert new data (based on selection of dimensions and filters)

* Drill up/down functions

* Slice function

.. i18n: The Open  ERP interface
.. i18n: -----------------------

The Open  ERP interface
-----------------------

.. i18n: From Open  ERP, you should be able to right click/drag and drop any field to trigger the cube definition wizard to create your own cube on demand. For this, we will use the web client of the bi system.

From Open  ERP, you should be able to right click/drag and drop any field to trigger the cube definition wizard to create your own cube on demand. For this, we will use the web client of the bi system.

.. i18n: We will intergate this on the gtk and web client of Open  erp. For the GTK one, it will open the browser to browse the cube.

We will intergate this on the gtk and web client of Open  erp. For the GTK one, it will open the browser to browse the cube.

.. i18n: Extra libraries
.. i18n: ===============

Extra libraries
===============

.. i18n: Libraries we will use:

Libraries we will use:

.. i18n: * Turbogears for the web client to browse cube
.. i18n: 
.. i18n: * Mathplotlib for rendering graphs
.. i18n: 
.. i18n: * PyParsing to parse MDX Expressions
.. i18n: 
.. i18n: * SQLAlchemy to construct SQL queries and RDBMS connections
.. i18n: 
.. i18n: * XMLRPC lib for communication with the cube server
.. i18n: 
.. i18n: * PÿUNO for the OOo integration

* Turbogears for the web client to browse cube

* Mathplotlib for rendering graphs

* PyParsing to parse MDX Expressions

* SQLAlchemy to construct SQL queries and RDBMS connections

* XMLRPC lib for communication with the cube server

* PÿUNO for the OOo integration

.. i18n: We will use an object relationnal mapping system on all objects: dimensions, ...

We will use an object relationnal mapping system on all objects: dimensions, ...
