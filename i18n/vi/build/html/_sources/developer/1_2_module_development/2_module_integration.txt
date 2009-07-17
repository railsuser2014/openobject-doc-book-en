
.. i18n: Module Integrations
.. i18n: ===================

Module Integrations
===================

.. i18n: The are many different modules available for Open ERP and suited for different business models. Nearly all of these are optional (except ModulesAdminBase), making it easy to customize Open ERP to serve specific business needs. All the modules are in a directory named addons/ on the server. You simply need to copy or delete a module directory in order to either install or delete the module on the Open ERP platform.

The are many different modules available for Open ERP and suited for different business models. Nearly all of these are optional (except ModulesAdminBase), making it easy to customize Open ERP to serve specific business needs. All the modules are in a directory named addons/ on the server. You simply need to copy or delete a module directory in order to either install or delete the module on the Open ERP platform.

.. i18n: Some modules depend on other modules. See the file addons/module/__terp__.py for more information on the dependencies.

Some modules depend on other modules. See the file addons/module/__terp__.py for more information on the dependencies.

.. i18n: Here is an example of __terp__.py:

Here is an example of __terp__.py:

.. i18n: .. code-block:: python
.. i18n: 
.. i18n: 	{
.. i18n: 	    "name" : "Open TERP Accounting",
.. i18n: 	    "version" : "1.0",
.. i18n: 	    "author" : "Bob Gates - Not So Tiny",
.. i18n: 	    "website" : "http://www.openerp.com/",
.. i18n: 	    "category" : "Generic Modules/Others",
.. i18n: 	    "depends" : ["base"],
.. i18n: 	    "description" : """A
.. i18n: 	    Multiline
.. i18n: 	    Description
.. i18n: 	    """,
.. i18n: 	    "init_xml" : ["account_workflow.xml", "account_data.xml", "account_demo.xml"],
.. i18n: 	    "demo_xml" : ["account_demo.xml"],
.. i18n: 	    "update_xml" : ["account_view.xml", "account_report.xml", "account_wizard.xml"],
.. i18n: 	    "active": False,
.. i18n: 	    "installable": True
.. i18n: 	}

.. code-block:: python

	{
	    "name" : "Open TERP Accounting",
	    "version" : "1.0",
	    "author" : "Bob Gates - Not So Tiny",
	    "website" : "http://www.openerp.com/",
	    "category" : "Generic Modules/Others",
	    "depends" : ["base"],
	    "description" : """A
	    Multiline
	    Description
	    """,
	    "init_xml" : ["account_workflow.xml", "account_data.xml", "account_demo.xml"],
	    "demo_xml" : ["account_demo.xml"],
	    "update_xml" : ["account_view.xml", "account_report.xml", "account_wizard.xml"],
	    "active": False,
	    "installable": True
	}

.. i18n: When initializing a module, the files in the init_xml list are evaluated in turn and then the files in the update_xml list are evaluated. When updating a module, only the files from the **update_xml** list are evaluated. 

When initializing a module, the files in the init_xml list are evaluated in turn and then the files in the update_xml list are evaluated. When updating a module, only the files from the **update_xml** list are evaluated. 
