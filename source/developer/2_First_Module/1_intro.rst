=============
Business case
=============

This chapter will give you a quick overview on how you can easily and quickly develop your own features within Open ERP. We will describe here the complete development of a small module for a travel agency company.

We describe in this chapter what we do but not "how" we do it. Having a first look at the different component will help you to better understand the following chapters that will go deeper in details of each part of a module development.

We suggest you to try to develop the proposed module while reading this chapter. This way, you will quickly see how simple it is to write a module in Open ERP. 

In this simple example, we would like to manage a travel agency which is responsible for one simple task, which is booking rooms in hostels. We show how to write a simple module that performs such a task in Open ERP. 


Development planning
====================

All the modules are located in the server/addons directory.

The following steps are necessary to create a new module:

    * create a subdirectory in the server/addons directory
    * create a module description file: __terp__.py
    * create the Python file containing the objects
    * create .xml files that download the data (views, menu entries, demo data, ...)
    * optionally create reports, wizards or workflows. 


The structure of a module should be like this::

 /module_name/
 /module_name/__init__.py
 /module_name/__terp__.py
 /module_name/module.py
 /module_name/module_view.xml
 /module_name/module_wizard.xml
 /module_name/module_report.xml
 /module_name/module_data.xml
 /module_name/module_demo.xml
 /module_name/module_security.xml
 /module_name/wizard/
 /module_name/wizard/__init__.py
 /module_name/wizard/wizard_name.py
 /module_name/wizard/wizard_name_view.xml
 /module_name/wizard/wizard_name_workflow.xml
 /module_name/report/
 /module_name/report/__init__.py
 /module_name/report/report_name.sxw
 /module_name/report/report_name.rml
 /module_name/report/report_name.py


..        Explain here the steps of the developments of the module, and what will be done
        in which chapter.


..        Final result
        ============

        At the end of this book, the developped module will cover...

        Here are a few screenshots with explanations...


