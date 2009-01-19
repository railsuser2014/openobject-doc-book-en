
===============================
Creation of Objects (The Model)
===============================

Introduction
============

.. This chapter is dedicated to detailed objects definition:
    all fields
    all objects
    inheritancies

All the ERP's pieces of data are accessible through "objects". As an example, there is a res.partner object to access the data concerning the partners, an account.invoice object for the data concerning the invoices, etc...

Please note that there is an object for every type of resource, and not an object per resource. We have thus a res.partner object to manage all the partners and not a @@res.partner@@ object per partner. If we talk in "object oriented" terms, we could also say that there is an object per level.

The direct consequences is that all the methods of objects have a common parameter: the "ids" parameter. This specifies on which resources (for example, on which partner) the method must be applied. Precisely, this parameter contains a list of resource ids on which the method must be applied.

For example, if we have two partners with the identifiers 1 and 5, and we want to call the res_partner method "send_email", we will write something like::

        res_partner.send_email(... , [1, 5], ...)

We will see the exact syntax of object method calls further in this document.

In the following section, we will see how to define a new object. Then, we will check out the different methods of doing this.

For developers:

* Open ERP "objects" are usually called classes in object oriented programming.
* A Open ERP "resource" is usually called an object in OO programming, instance of a class. 

It's a bit confusing when you try to program inside Open ERP, because the language used is Python, and Python is a fully object oriented language, and has objects and instances ...

Luckily, an Open ERP "resource" can be converted magically into a nice Python object using the "browse" class method (Open ERP object method). 


Objects and fields
==================

Objects Introduction
--------------------

To define a new object, you have to define a new Python class then instantiate it. This class must inherit from the osv class in the osv module.

Object definition
-----------------

The first line of the object definition will always be of the form:

.. code-block:: python

        class name_of_the_object(osv.osv):
            _name = 'name.of.the.object'
            _columns = { ... }
            ...
        name_of_the_object()

An object is defined by declaring some fields with predefined names in the class. Two of them are required (_name and _columns), the rest is optional. The predefined fields are:

Prefined names
---------------

:_auto:

Determines whether a corresponding `PostgreSQL table must be generated automatically from the object. Setting _auto to False can be useful in case of Open ERP objects generated from `PostgreSQL views. See the "Reporting From PostgreSQL Views" section for more details.

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

    *Example*s::

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

Fields Introduction
-------------------

Objects may contain different types of fields. Those types can be divided into three categories: simple types, relation types and functional fields. The simple types are integers, floats, booleans, strings, etc ... ; the relation types are used to represent relations between objects (one2one, one2many, many2one). Functional fields are special fields because they are not stored in the database but calculated in real time given other fields of the view.

Here's the header of the initialization method of the class any field defined in Open ERP inherits (as you can see in server/bin/osv/fields.py)::

        def __init__(self, string='unknown', required=False, readonly=False, domain=[], context="", states={}, priority=0, change_default=False, size=None, ondelete="set null", translate=False, select=False, **args) :


Optional parameters to All Field Types
++++++++++++++++++++++++++++++++++++++

:change_default: 

Whether or not the user can define default values on other fields depending on the value of this field.

    Default value: False. 
    
*Example*: (in res.partner.address)
    
    'zip': fields.char('Zip', change_default=True, size=24),
    
    In this case, it means users will be able to set default values for any field of the contact form depending on the value of the 'zip' field. For example, the user could have the program automatically set the city field to 'Brussels' if the zip is 1200 and to 'Namur' if the zip is 5000. 

:help: 

Shows a helpmessage (tooltip) when mousecursor is over the field.

        Default value: . 
        
    *Example*:
        'name': fields.char('name', help='Your own name.'), 

:readonly: 

Whether the field is editable or not. 

        Default value: False. 

:required:

Whether the field is required or not. The program will refuse to save a resource if a required field is left blank. 
        
        Default value: False. 

:states:

This parameter permits to define attributes for this field that will only be available in some states of the resource. 
        
        Format: {'name_of_the_state': list_of_attributes}
        
        where list_of_attributes is a list of tuples of the form [('name_of_attribute', value), ...] 

        Default value: {}. 
        
    *Example*: (in account.transfer) 
        
        'partner_id': fields.many2one('res.partner', 'Partner', states={'posted':[('readonly',True)]}), 

:string:

The label of the field. 

        Default value: 'unknown'. 

    *Example*: 

        'tested': fields.boolean('Tested'), 

        Note: Strings containing non-ASCII characters must use python unicode objects. 

    *Example*: (in french) 

        'tested': fields.boolean(u'Testé'), 

:translate:

Whether or not the content of this field should be translated (ie. managed by the translation system). 

        Default value: False. 

        Optional Parameters specific to some Field types

:priority:

Default value: 0. 

:domain:

domain restriction on a relational field. 

        Default value: []. 

    *Example*: domain=[('field','=',value)]) 

:invisible:

Hide the field's value in forms (password...) 

        Default value: False 

:context:

Define a variable's value visible in the view's context (or an on-change function...) 

        Default value: . 

    *Example*: context={lang=’fr’} 


:selection:

select the default search level on views. 1 search field always appears. 2: appears only in advanced search mode.

    Default value: None. 

:on_change:

Launch a function (define on an ORM object) when the field's value is changed in a view. 

    *Example*: on_change="onchange_shop_id(shop_id)” 

Simple Fields
+++++++++++++

:boolean:

A boolean (true, false).

        Syntax::

                fields.boolean('Field Name' [, Optional Parameters]),

:integer:

An integer.
        
        Syntax::

                fields.integer('Field Name' [, Optional Parameters]),

:float:

A floating point number.

        Syntax::

                fields.float('Field Name' [, Optional Parameters]),

        .. note::

                The optional parameter digits defines the precision and scale of the number. The scale being the number of digits after the decimal point whereas the precision is the total number of significant digits in the number (before and after the decimal point). If the parameter digits is not present, the number will be a double precision floating point number. Warning: these floating-point numbers are inexact (not any value can be converted to its binary representation) and this can lead to rounding errors. You should always use the digits parameter for monetary amounts.
        
        
        Example

        'rate' : fields.float('Relative Change rate', digits=(12,6) [, Optional Parameters]),

:char:

A string of limited length. The required size parameter determines its size.

        Syntax::

                fields.char('Field Name', size=n [, Optional Parameters]), # where ''n'' is an integer.

Example

'city' : fields.char('City Name', size=30, required=True),

:text:

A text field with no limit in length.

        Syntax::

                fields.text('Field Name' [, Optional Parameters]),

:date:

A date.

        Syntax::

                fields.date('Field Name' [, Optional Parameters]),

:datetime:

Allows to store a date and the time of day in the same field.

        Syntax::

                fields.datetime('Field Name' [, Optional Parameters]),

:binary:

A binary chain

:selection:

A field which allows the user to make a selection between various predefined values.

        Syntax::

                fields.selection((('n','Unconfirmed'), ('c','Confirmed')), 'Field Name' [, Optional Parameters]),

.. note::

        Format of the selection parameter: tuple of tuples of strings of the form::

                (('key_or_value', 'string_to_display'), ... )

*Example*

Using relation fields **many2one** with **selection**. In fields definitions add::

        ...,
        'my_field': fields.many2one('mymodule.relation.model', 'Title', selection=_sel_func), 
        ...,

And then define the _sel_func like this (but before the fields definitions)::

        def _sel_func(self, cr, uid, context={}): 
            obj = self.pool.get('mymodule.relation.model') 
            ids = obj.search(cr, uid, []) 
            res = obj.read(cr, uid, ids, ['name', 'id'], context) 
            res = [(r['id'], r['name']) for r in res] 
            return res
            
Function Fields
+++++++++++++++

A functional field is a field whose value is calculated by a function (rather than being stored in the database).

**Parameters:** fnct, arg=None, fnct_inv=None, fnct_inv_arg=None, type="%green%float%black%", fnct_search=None, obj=None, method=False, store=True

where

* *type* is the field type name returned by the function. It can be any field type name except function.
* *store* If you want to store field in database or not. Default is False.
* *method* whether the field is computed by a method (of an object) or a global function
* *fnct* is the function or method that will compute the field value. It must have been declared before declaring the functional field. 

        If *method* is True, the signature of the method must be::

                def fnct(self, cr, uid, ids, field_name, arg, context)

        otherwise (if it is a global function), its signature must be::

                def fnct(cr, table, ids, field_name, arg, context)

        Either way, it must return a dictionary of values of the form {id'_1_': value'_1_', id'_2_': value'_2_',...}.::

                The values of the returned dictionary must be of the type specified by the type argument in the field declaration.

* *fnct_inv* is the function or method that will allow writing values in that field. 

        If *method* is true, the signature of the method must be::

                def fnct(self, cr, uid, ids, field_name, field_value, arg, context)

        otherwise (if it is a global function), it should be::

                def fnct(cr, table, ids, field_name, field_value, arg, context)

* *fnct_search* allows you to define the searching behaviour on that field. 

        If *method* is true, the signature of the method must be::

                def fnct(self, cr, uid, obj, name, args)

        otherwise (if it is a global function), it should be::

                def fnct(cr, uid, obj, name, args)

        The return value is a list countaining 3-part tuplets which are used in search funtion::

                return [('id','in',[1,3,5])]

Example Of Functional Field
"""""""""""""""""""""""""""

Suppose we create a contract object which is:

.. code-block:: python

        class hr_contract(osv.osv):
            _name = 'hr.contract'
            _description = 'Contract'
            _columns = {
                'name' : fields.char('Contract Name', size=30, required=True),
                'employee_id' : fields.many2one('hr.employee', 'Employee', required=True),
                'function' : fields.many2one('res.partner.function', 'Function'),
            }
        hr_contract()

If we want to add a field that retrieves the function of an employee by looking its current contract, we use a functional field. The object hr_employee is inherited this way:

.. code-block:: python

        class hr_employee(osv.osv):
            _name = "hr.employee"
            _description = "Employee"
            _inherit = "hr.employee"
            _columns = {
                'contract_ids' : fields.one2many('hr.contract', 'employee_id', 'Contracts'),
                'function' : fields.function(_get_cur_function_id, type='many2one', obj="res.partner.function",
                                             method=True, string='Contract Function'),
            }
        hr_employee()

Note three points:

* type='many2one' is because the function field must create a many2one field; function is declared as a many2one in hr_contract also.
* obj="res.partner.function" is used to specify that the object to use for the many2one field is res.partner.function.
* We called our method _get_cur_function_id because its role is to return a dictionary whose keys are ids of employees, and whose corresponding values are ids of the function of those employees. The code of this method is: 


.. code-block:: python

        def _get_cur_function_id(self, cr, uid, ids, field_name, arg, context):
            for i in ids:
                #get the id of the current function of the employee of identifier "i"
                sql_req= """
                SELECT f.id AS func_id
                FROM hr_contract c
                  LEFT JOIN res_partner_function f ON (f.id = c.function)
                WHERE
                  (c.employee_id = %d)
                """ % (i,)
         
                cr.execute(sql_req)
                sql_res = cr.dictfetchone()
         
                if sql_res: #The employee has one associated contract
                    res[i] = sql_res['func_id']
                else:
                    #res[i] must be set to False and not to None because of XML:RPC
                    # "cannot marshal None unless allow_none is enabled"
                    res[i] = False
                    return res

The id of the function is retrieved using a SQL query. Note that if the query returns no result, the value of sql_res['func_id'] will be None. We force the False value in this case value because XML:RPC (communication between the server and the client) doesn't allow to transmit this value.

**store={...} Enhancement**

It will compute the field depends on other objects.

**Syntex** store={'object_name':(function_name,['field_name1','field_name2'],priority)} It will call function function_name when any changes will be applied on field list ['field1','field2'] on object 'object_name' and output of the function will send as a parameter for main function of the field.

**Example** In membership module

.. code-block:: python

        'membership_state': fields.function(_membership_state, method=True, string='Current membership state', type='selection', selection=STATE, 
          store={'account.invoice':(_get_invoice_partner,['state'], 10),
          'membership.membership_line':(_get_partner_id,['state'], 10),
          'res.partner':(lambda self,cr,uid,ids,c={}:ids, ['free_member'], 10)}),

Inheritancies
=============

Introduction
------------

Extension of an object
----------------------

Describe here _inherit


A composite object
------------------

Describe here _inherits


Improvement of school management module
=======================================

Adding function fields
----------------------

Adding relate fields
--------------------

Inheriting from partners
------------------------

Inheriting from products
------------------------



