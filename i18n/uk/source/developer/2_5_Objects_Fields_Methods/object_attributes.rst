
.. i18n: OpenERP Object Attributes
.. i18n: =========================

OpenERP Object Attributes
=========================

.. i18n: Objects Introduction
.. i18n: --------------------

Objects Introduction
--------------------

.. i18n: To define a new object, you have to define a new Python class then instantiate it. This class must inherit from the osv class in the osv module.

To define a new object, you have to define a new Python class then instantiate it. This class must inherit from the osv class in the osv module.

.. i18n: Object definition
.. i18n: -----------------

Object definition
-----------------

.. i18n: The first line of the object definition will always be of the form::
.. i18n: 
.. i18n:         class name_of_the_object(osv.osv):
.. i18n:                 _name = 'name.of.the.object'
.. i18n:                 _columns = { ... }
.. i18n:                 ...
.. i18n:         name_of_the_object()

The first line of the object definition will always be of the form::

        class name_of_the_object(osv.osv):
                _name = 'name.of.the.object'
                _columns = { ... }
                ...
        name_of_the_object()

.. i18n: An object is defined by declaring some fields with predefined names in the class. Two of them are required (_name and _columns), the rest is optional. The predefined fields are:

An object is defined by declaring some fields with predefined names in the class. Two of them are required (_name and _columns), the rest is optional. The predefined fields are:

.. i18n: Prefined names
.. i18n: ---------------

Prefined names
---------------

.. i18n: :_auto:

:_auto:

.. i18n: Determines whether a corresponding PostgreSQL table must be generated automatically from the object. Setting _auto to False can be useful in case of Open ERP objects generated from PostgreSQL views. See the "Reporting From PostgreSQL Views" section for more details.

Determines whether a corresponding PostgreSQL table must be generated automatically from the object. Setting _auto to False can be useful in case of Open ERP objects generated from PostgreSQL views. See the "Reporting From PostgreSQL Views" section for more details.

.. i18n: :_columns (required):

:_columns (required):

.. i18n: The object fields. See the fields section for details.

The object fields. See the fields section for details.

.. i18n: :_constraints:

:_constraints:

.. i18n: The constraints on the object. See the constraints section for details.

The constraints on the object. See the constraints section for details.

.. i18n: :_sql_constraints:

:_sql_constraints:

.. i18n: The SQL Constraint on the object. See theconstraints SQL section for more details.

The SQL Constraint on the object. See theconstraints SQL section for more details.

.. i18n: :_defaults:

:_defaults:

.. i18n: The default values for some of the object's fields. See the default value section for details.

The default values for some of the object's fields. See the default value section for details.

.. i18n: :_inherit:

:_inherit:

.. i18n: The name of the osv object which the current object inherits from. See the object inheritance section (first form) for details.

The name of the osv object which the current object inherits from. See the object inheritance section (first form) for details.

.. i18n: :_inherits:

:_inherits:

.. i18n: The list of osv objects the object inherits from. This list must be given in a python dictionary of the form: {'name_of_the_parent_object': 'name_of_the_field', ...}. See the object inheritance section (second form) for details. Default value: {}.

The list of osv objects the object inherits from. This list must be given in a python dictionary of the form: {'name_of_the_parent_object': 'name_of_the_field', ...}. See the object inheritance section (second form) for details. Default value: {}.

.. i18n: :_log_access:

:_log_access:

.. i18n: Determines whether or not the write access to the resource must be logged. If true, four fields will be created in the SQL table: create_uid, create_date, write_uid, write_date. Those fields represent respectively the id of the user who created the record, the creation date of record, the id of the user who last modified the record, and the date of that last modification. This data may be obtained by using the perm_read method.

Determines whether or not the write access to the resource must be logged. If true, four fields will be created in the SQL table: create_uid, create_date, write_uid, write_date. Those fields represent respectively the id of the user who created the record, the creation date of record, the id of the user who last modified the record, and the date of that last modification. This data may be obtained by using the perm_read method.

.. i18n: :_name (required):

:_name (required):

.. i18n: Name of the object. Default value: None.

Name of the object. Default value: None.

.. i18n: :_order:

:_order:

.. i18n: Name of the fields used to sort the results of the search and read methods.

Name of the fields used to sort the results of the search and read methods.

.. i18n: Default value: 'id'.

Default value: 'id'.

.. i18n:     Examples::
.. i18n: 
.. i18n:                 _order = "name"  
.. i18n:                 _order = "date_order desc"

    Examples::

                _order = "name"  
                _order = "date_order desc"

.. i18n: :_rec_name:

:_rec_name:

.. i18n: Name of the field in which the name of every resource is stored. Default value: 'name'. Note: by default, the name_get method simply returns the content of this field.

Name of the field in which the name of every resource is stored. Default value: 'name'. Note: by default, the name_get method simply returns the content of this field.

.. i18n: :_sequence:

:_sequence:

.. i18n: Name of the SQL sequence that manages the ids for this object. Default value: None.

Name of the SQL sequence that manages the ids for this object. Default value: None.

.. i18n: :_sql:

:_sql:

.. i18n: SQL code executed upon creation of the object (only if _auto is True)

SQL code executed upon creation of the object (only if _auto is True)

.. i18n: :_table:

:_table:

.. i18n: Name of the SQL table. Default value: the value of the _name field above with the dots ( . ) replaced by underscores ( _ ). 

Name of the SQL table. Default value: the value of the _name field above with the dots ( . ) replaced by underscores ( _ ). 
