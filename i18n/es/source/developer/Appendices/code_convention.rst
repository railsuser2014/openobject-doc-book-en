
.. i18n: Appendices A : Coding Conventions
.. i18n: =================================

Appendices A : Coding Conventions
=================================

.. i18n: Python coding
.. i18n: -------------

Python coding
-------------

.. i18n: Use tabs: will be replaced by spaces soon...

Use tabs: will be replaced by spaces soon...

.. i18n: Take care with default values for arguments: they are only evaluated once when the module is loaded and then used at each call. This means that if you use a mutable object as default value, and then modify that object, at the next call you will receive the modified object as default argument value. This applies to dict and list objects which are very often used as default values. If you want to use such objects as default value, you must either ensure that they won't be modified or use another default value (such as None) and test it. For example:

Take care with default values for arguments: they are only evaluated once when the module is loaded and then used at each call. This means that if you use a mutable object as default value, and then modify that object, at the next call you will receive the modified object as default argument value. This applies to dict and list objects which are very often used as default values. If you want to use such objects as default value, you must either ensure that they won't be modified or use another default value (such as None) and test it. For example:

.. i18n: .. code-block:: python
.. i18n: 
.. i18n:     def foo(a=None):
.. i18n: 
.. i18n:         if a is None:
.. i18n: 
.. i18n:             a=[] 
.. i18n: 
.. i18n:         # ... 

.. code-block:: python

    def foo(a=None):

        if a is None:

            a=[] 

        # ... 

.. i18n: This is what is [in the Python documentation]. In addition it is good practice to avoid modifying objects that you receive as arguments if it is not specified. If you want to do so, prefer to copy the object first. A list can easily be copied with the syntax

This is what is [in the Python documentation]. In addition it is good practice to avoid modifying objects that you receive as arguments if it is not specified. If you want to do so, prefer to copy the object first. A list can easily be copied with the syntax

.. i18n:         copy = original[:] 

        copy = original[:] 

.. i18n: A lot of other objects, such as dict, define a copy method.

A lot of other objects, such as dict, define a copy method.

.. i18n: File names
.. i18n: -----------

File names
-----------

.. i18n: The structure of a module should be like this::
.. i18n: 
.. i18n:     /module/

The structure of a module should be like this::

    /module/

.. i18n:         /__init__.py 
.. i18n:         /__terp__.py 
.. i18n:         /module.py 
.. i18n:         /module_other.py 
.. i18n:         /module_view.xml 
.. i18n:         /module_wizard.xml 
.. i18n:         /module_report.xml 
.. i18n:         /module_data.xml 
.. i18n:         /module_demo.xml 
.. i18n:         /wizard/ 
.. i18n:         /__init__.py 
.. i18n:         /wizard_name.py 

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

.. i18n:     /report/

    /report/

.. i18n:         /__init__.py 
.. i18n:         /report_name.sxw 
.. i18n:         /report_name.rml 
.. i18n:         /report_name.py 

        /__init__.py 
        /report_name.sxw 
        /report_name.rml 
        /report_name.py 

.. i18n: Naming conventions
.. i18n: ------------------

Naming conventions
------------------

.. i18n:     * modules: modules must be written in lower case, with underscores. The name of the module is the name of the directory in the addons path of the server. If the module depends on other modules, you can write several module names separated by underscores, starting by the most important name. Example:
.. i18n:           + sale
.. i18n:           + sale_commission 
.. i18n: 
.. i18n:     * objects: the name of an object must be of the form name_of_module.name1.name2.name3.... The namei part of the object must go from the most important name to the least important one, from left to right, in lower case. Try not to use plurals in object names and to avoid shortcuts in the names. Example:
.. i18n:           + sale.order
.. i18n:           + sale.order.line
.. i18n:           + sale.shop
.. i18n:           + sale_commission.commission.rate 
.. i18n: 
.. i18n:     * fields: field must be in lowercase, separated by underscores. Try to use commonly used names for fields: name, state, active, partner_id, eso. Conventions for the field name depends on the field type:
.. i18n:           + many2one: must end by '_id' (eg: partner_id, order_line_id)
.. i18n:           + many2many: must end by '_ids' (eg: category_ids)
.. i18n:           + one2many: must end by '_ids' (eg: line_ids

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
