Appendices A : Coding Conventions
=================================

Python coding
-------------

Use tabs: will be replaced by spaces soon...

Take care with default values for arguments: they are only evaluated once when the module is loaded and then used at each call. This means that if you use a mutable object as default value, and then modify that object, at the next call you will receive the modified object as default argument value. This applies to dict and list objects which are very often used as default values. If you want to use such objects as default value, you must either ensure that they won't be modified or use another default value (such as None) and test it. For example:

.. code-block:: python

    def foo(a=None):

        if a is None:

            a=[] 

        # ... 

This is what is [in the Python documentation]. In addition it is good practice to avoid modifying objects that you receive as arguments if it is not specified. If you want to do so, prefer to copy the object first. A list can easily be copied with the syntax

        copy = original[:] 

A lot of other objects, such as dict, define a copy method.

File names
-----------

The structure of a module should be like this::

    /module/

        /__init__.py 
        /__terp__.py 
        /module.py 
        /module_other.py 
        /module_view.xml 
        /module_wizard.xml 
        /module_report.xml 
        /module_data.xml 
        /module_demo.xml 
        /wizard/ 
        /__init__.py 
        /wizard_name.py 

    /report/

        /__init__.py 
        /report_name.sxw 
        /report_name.rml 
        /report_name.py 

Naming conventions
------------------

    * modules: modules must be written in lower case, with underscores. The name of the module is the name of the directory in the addons path of the server. If the module depends on other modules, you can write several module names separated by underscores, starting by the most important name. Example:
          + sale
          + sale_commission 

    * objects: the name of an object must be of the form name_of_module.name1.name2.name3.... The namei part of the object must go from the most important name to the least important one, from left to right, in lower case. Try not to use plurals in object names and to avoid shortcuts in the names. Example:
          + sale.order
          + sale.order.line
          + sale.shop
          + sale_commission.commission.rate 

    * fields: field must be in lowercase, separated by underscores. Try to use commonly used names for fields: name, state, active, partner_id, eso. Conventions for the field name depends on the field type:
          + many2one: must end by '_id' (eg: partner_id, order_line_id)
          + many2many: must end by '_ids' (eg: category_ids)
          + one2many: must end by '_ids' (eg: line_ids
