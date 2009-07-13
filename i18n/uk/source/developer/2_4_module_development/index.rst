
.. i18n: =======================
.. i18n: First Module to OpenERP
.. i18n: =======================

=======================
First Module to OpenERP
=======================

.. i18n: Open ERP is a Python based client/server program for Enterprise Resource
.. i18n: Planning. It consist of a client "openerp-client" and a server "openerp-server"
.. i18n: while the persistence is provided by Postgresql. Open ERP currently uses
.. i18n: XML-RPC for communication over a network. Once installed Open ERP has a
.. i18n: modular structure that allows modules to be added as needed. 

Open ERP is a Python based client/server program for Enterprise Resource
Planning. It consist of a client "openerp-client" and a server "openerp-server"
while the persistence is provided by Postgresql. Open ERP currently uses
XML-RPC for communication over a network. Once installed Open ERP has a
modular structure that allows modules to be added as needed. 

.. i18n: The Modules - Introduction
.. i18n: ==========================

The Modules - Introduction
==========================

.. i18n: The usage of the modules is the way to extend Tiny ERP functionality. The default Tiny ERP installation is organized as a kernel and various modules among which we can distinguish :

The usage of the modules is the way to extend Tiny ERP functionality. The default Tiny ERP installation is organized as a kernel and various modules among which we can distinguish :

.. i18n:     * base : The most basic module. Defines ir.property, res.company, res.request, res.currency, res.user, res.partner
.. i18n:     * crm : Customer & Supplier Relationship Management.
.. i18n:     * sale : Sales Management.
.. i18n:     * mrp : Manufacturing Resource Planning. 

    * base : The most basic module. Defines ir.property, res.company, res.request, res.currency, res.user, res.partner
    * crm : Customer & Supplier Relationship Management.
    * sale : Sales Management.
    * mrp : Manufacturing Resource Planning. 

.. i18n: New modules can be programed easily, and require a little practice of XML and Python.

New modules can be programed easily, and require a little practice of XML and Python.

.. i18n: ..  toctree::
.. i18n:     :maxdepth: 3
.. i18n: 
.. i18n:     4_1_module_structure
.. i18n:     4_2_module_descriptor
.. i18n:     4_3_create_module
.. i18n:     4_4_createing_action

..  toctree::
    :maxdepth: 3

    4_1_module_structure
    4_2_module_descriptor
    4_3_create_module
    4_4_createing_action
