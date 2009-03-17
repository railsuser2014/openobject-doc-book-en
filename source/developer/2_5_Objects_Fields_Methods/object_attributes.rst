OpenERP Object Attributes
=========================

Objects Introduction
--------------------

To define a new object, you have to define a new Python class then instantiate it. This class must inherit from the osv class in the osv module.

Object definition
-----------------

The first line of the object definition will always be of the form::

        class name_of_the_object(osv.osv):
                _name = 'name.of.the.object'
                _columns = { ... }
                ...
        name_of_the_object()

An object is defined by declaring some fields with predefined names in the class. Two of them are required (_name and _columns), the rest is optional. The predefined fields are:

Prefined names
---------------

:_auto:

Determines whether a corresponding PostgreSQL table must be generated automatically from the object. Setting _auto to False can be useful in case of Open ERP objects generated from PostgreSQL views. See the "Reporting From PostgreSQL Views" section for more details.

:_columns (required):

The object fields. See the fields section for details.

:_constraints:

The constraints on the object. See the constraints section for details.

:_sql_constraints:

The SQL Constraint on the object. See theconstraints SQL section for more details.

:_defaults:

The default values for some of the object's fields. See the default value section for details.

:_inherit:

The name of the osv object which the current object inherits from. See the object inheritance section (first form) for details.

:_inherits:

The list of osv objects the object inherits from. This list must be given in a python dictionary of the form: {'name_of_the_parent_object': 'name_of_the_field', ...}. See the object inheritance section (second form) for details. Default value: {}.

:_log_access:

Determines whether or not the write access to the resource must be logged. If true, four fields will be created in the SQL table: create_uid, create_date, write_uid, write_date. Those fields represent respectively the id of the user who created the record, the creation date of record, the id of the user who last modified the record, and the date of that last modification. This data may be obtained by using the perm_read method.

:_name (required):

Name of the object. Default value: None.

:_order:

Name of the fields used to sort the results of the search and read methods.

Default value: 'id'.

    Examples::

                _order = "name"  
                _order = "date_order desc"


:_rec_name:

Name of the field in which the name of every resource is stored. Default value: 'name'. Note: by default, the name_get method simply returns the content of this field.

:_sequence:

Name of the SQL sequence that manages the ids for this object. Default value: None.

:_sql:

SQL code executed upon creation of the object (only if _auto is True)

:_table:

Name of the SQL table. Default value: the value of the _name field above with the dots ( . ) replaced by underscores ( _ ). 

