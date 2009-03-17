=======================
First Module to OpenERP
=======================

Open ERP is a Python based client/server program for Enterprise Resource Planning. It consist of a client "tinyerp-client" and a server "tinyerp-server" while the persistence is provided by Postgresql. Open ERP currently uses XML-RPC for communication over a network. Once installed Open ERP has a modular structure that allows modules to be added as needed. 

The Modules - Introduction
==========================

The usage of the modules is the way to extend Tiny ERP functionality. The default Tiny ERP installation is organized as a kernel and various modules among which we can distinguish :

    * base : The most basic module. Defines ir.property, res.company, res.request, res.currency, res.user, res.partner
    * crm : Customer & Supplier Relationship Management.
    * sale : Sales Management.
    * mrp : Manufacturing Resource Planning. 

New modules can be programed easily, and require a little practice of XML and Python. 

..  toctree::
    :maxdepth: 3

    4_1_module_structure
    4_2_module_descriptor
    4_3_create_module
    4_4_createing_action  
