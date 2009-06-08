
.. i18n: OpenERP Module Descriptor File : __terp__.py
.. i18n: ============================================

OpenERP Module Descriptor File : __terp__.py
============================================

.. i18n: Normal Module
.. i18n: -------------

Normal Module
-------------

.. i18n: In the created module directory, you must add a **__terp__.py** file. This file, which must be in Python format, is responsible to

In the created module directory, you must add a **__terp__.py** file. This file, which must be in Python format, is responsible to

.. i18n:    1. determine the XML files that will be parsed during the initialization of the server, and also to
.. i18n:    2. determine the dependencies of the created module.

   1. determine the XML files that will be parsed during the initialization of the server, and also to
   2. determine the dependencies of the created module.

.. i18n: This file must contain a Python dictionary with the following values:

This file must contain a Python dictionary with the following values:

.. i18n: **name**

**name**

.. i18n:     The (Plain English) name of the module.

    The (Plain English) name of the module.

.. i18n: **version**

**version**

.. i18n:     The version of the module.

    The version of the module.

.. i18n: **description**

**description**

.. i18n:     The module description (text).

    The module description (text).

.. i18n: **author**

**author**

.. i18n:     The author of the module.

    The author of the module.

.. i18n: **website**

**website**

.. i18n:     The website of the module.

    The website of the module.

.. i18n: **license**

**license**

.. i18n:     The license of the module (default:GPL-2).

    The license of the module (default:GPL-2).

.. i18n: **depends**

**depends**

.. i18n:     List of modules on which this module depends. The base module must almost always be in the dependencies because some necessary data for the views, reports, ... are in the base module.

    List of modules on which this module depends. The base module must almost always be in the dependencies because some necessary data for the views, reports, ... are in the base module.

.. i18n: **init_xml**

**init_xml**

.. i18n:     List of .xml files to load when the server is launched with the "--init=module" argument. Filepaths must be relative to the directory where the module is. Open ERP XML File Format is detailed in this section.

    List of .xml files to load when the server is launched with the "--init=module" argument. Filepaths must be relative to the directory where the module is. Open ERP XML File Format is detailed in this section.

.. i18n: **update_xml**

**update_xml**

.. i18n:     List of .xml files to load when the server is launched with the "--update=module" launched. Filepaths must be relative to the directory where the module is. Open ERP XML File Format is detailed in this section.

    List of .xml files to load when the server is launched with the "--update=module" launched. Filepaths must be relative to the directory where the module is. Open ERP XML File Format is detailed in this section.

.. i18n: **installable**

**installable**

.. i18n:     True or False. Determines if the module is installable or not.

    True or False. Determines if the module is installable or not.

.. i18n: **active**

**active**

.. i18n:     True or False (default: False). Determines the modules that are installed on the database creation.

    True or False (default: False). Determines the modules that are installed on the database creation.

.. i18n: Example
.. i18n: +++++++

Example
+++++++

.. i18n: Here is an example of __terp__.py file for the *product* module:

Here is an example of __terp__.py file for the *product* module:

.. i18n: .. code-block:: python
.. i18n: 
.. i18n:     {
.. i18n:         "name" : "Products & Pricelists",
.. i18n:         "version" : "1.0",
.. i18n:         "author" : "Open",
.. i18n:         "category" : "Generic Modules/Inventory Control",
.. i18n:         "depends" : ["base", "account"],
.. i18n:         "init_xml" : [],
.. i18n:         "demo_xml" : ["product_demo.xml"],
.. i18n:         "update_xml" : ["product_data.xml","product_report.xml", "product_wizard.xml","product_view.xml", "pricelist_view.xml"],
.. i18n:         "installable": True,
.. i18n:         "active": True
.. i18n:     }

.. code-block:: python

    {
        "name" : "Products & Pricelists",
        "version" : "1.0",
        "author" : "Open",
        "category" : "Generic Modules/Inventory Control",
        "depends" : ["base", "account"],
        "init_xml" : [],
        "demo_xml" : ["product_demo.xml"],
        "update_xml" : ["product_data.xml","product_report.xml", "product_wizard.xml","product_view.xml", "pricelist_view.xml"],
        "installable": True,
        "active": True
    }

.. i18n: The files that must be placed in init_xml are the ones that relate to the workflow definition, data to load at the installation of the software and the data for the demonstrations.

The files that must be placed in init_xml are the ones that relate to the workflow definition, data to load at the installation of the software and the data for the demonstrations.

.. i18n: The files in **update_xml** concern: views, reports and wizards.

The files in **update_xml** concern: views, reports and wizards.

.. i18n: Profile Module
.. i18n: --------------

Profile Module
--------------

.. i18n: The purpose of a profile is to initialize Open ERP with a set of modules directly after the database has been created. A profile is a special kind of module that contains no code, only *dependencies on other modules*.

The purpose of a profile is to initialize Open ERP with a set of modules directly after the database has been created. A profile is a special kind of module that contains no code, only *dependencies on other modules*.

.. i18n: In order to create a profile, you only have to create a new directory in server/addons (you *should* call this folder profile_modulename), in which you put an *empty* __init__.py file (as every directory Python imports must contain an __init__.py file), and a __terp__.py whose structure is as follows :

In order to create a profile, you only have to create a new directory in server/addons (you *should* call this folder profile_modulename), in which you put an *empty* __init__.py file (as every directory Python imports must contain an __init__.py file), and a __terp__.py whose structure is as follows :

.. i18n: .. code-block:: python
.. i18n: 
.. i18n:     {
.. i18n:          "name":"''Name of the Profile'',
.. i18n:          "version":"''Version String''",
.. i18n:          "author":"''Author Name''",
.. i18n:          "category":"Profile",
.. i18n:          "depends":[''List of the modules to install with the profile''],
.. i18n:          "demo_xml":[],
.. i18n:          "update_xml":[],
.. i18n:          "active":False,
.. i18n:          "installable":True,
.. i18n:     }

.. code-block:: python

    {
         "name":"''Name of the Profile'',
         "version":"''Version String''",
         "author":"''Author Name''",
         "category":"Profile",
         "depends":[''List of the modules to install with the profile''],
         "demo_xml":[],
         "update_xml":[],
         "active":False,
         "installable":True,
    }

.. i18n: Example
.. i18n: +++++++

Example
+++++++

.. i18n: Here's the code of the file
.. i18n: server/bin/addons/profile_manufacturing/__terp__.py, which corresponds to the
.. i18n: manufacturing industry profile in Open ERP.

Here's the code of the file
server/bin/addons/profile_manufacturing/__terp__.py, which corresponds to the
manufacturing industry profile in Open ERP.

.. i18n: .. code-block:: python
.. i18n: 
.. i18n:     {
.. i18n:          "name":"Manufacturing industry profile",
.. i18n:          "version":"1.0",
.. i18n:          "author":"Open",
.. i18n:          "category":"Profile",
.. i18n:          "depends":["mrp", "crm", "sale", "delivery"],
.. i18n:          "demo_xml":[],
.. i18n:          "update_xml":[],
.. i18n:          "active":False,
.. i18n:          "installable":True,
.. i18n:     }

.. code-block:: python

    {
         "name":"Manufacturing industry profile",
         "version":"1.0",
         "author":"Open",
         "category":"Profile",
         "depends":["mrp", "crm", "sale", "delivery"],
         "demo_xml":[],
         "update_xml":[],
         "active":False,
         "installable":True,
    }
