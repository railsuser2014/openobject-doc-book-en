
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

**Example** In membership module::

        'membership_state': fields.function(_membership_state, method=True, string='Current membership state', type='selection', selection=STATE, 
          store={'account.invoice':(_get_invoice_partner,['state'], 10),
          'membership.membership_line':(_get_partner_id,['state'], 10),
          'res.partner':(lambda self,cr,uid,ids,c={}:ids, ['free_member'], 10)}),

Relational Fields
+++++++++++++++++

:one2one:

A one2one field expresses a one:to:one relation between two objects. It is deprecated. Use many2one instead.
        
        syntax::

                fields.one2one('other.object.name', 'Field Name')

:many2one:

Associates this object to a parent object via this Field. For example Department an Employee belongs to would Many to one. i.e Many employees will belong to a Department

        syntax::

                fields.many2one('other.object.name', 'Field Name', optional parameter)

        * Optional parameters:
                - ondelete: What should happen when the resource this field points to is deleted.
                        + Predefined value: "cascade", "set null"
                        + Default value: "set null" 
                - required: True
                - readonly: True
                - select: True - (creates an index on the Foreign Key field) 

        *Example*

                'commercial': fields.many2one('res.users', 'Commercial', ondelete='cascade'),

:one2many:

TODO

        syntax::

                fields.one2many('other.object.name', 'Field relation id', 'Fieldname', optional parameter)

        * Optional parameters:
                - invisible: True/False
                - states: ?
                - readonly: True/False 

        *Example*

                'address': fields.one2many('res.partner.address', 'partner_id', 'Contacts'),

:many2many:

TODO

        syntax::

                fields.many2many('other.object.name', 'relation object', 'other.object.id', 'actual.object.id', 'Field Name')

        * where
                - other.object.name is the other object which belongs to the relation
                - relation object is the table that makes the link
                - other.object.id and actual.object.id are the fields' names used in the relation table 

        Example::

                'category_id': 
                   fields.many2many(
                    'res.partner.category', 
                    'res_partner_category_rel', 
                    'partner_id', 
                    'category_id', 
                    'Categories'),

:related:

Sometimes you need to refer the relation of a relation. For example, supposing you have objects: City <- State <- Country, and you need to refer Country in a City, you can define a field as below in the City object::

        'country_id': fields.related('state_id', 'country_id', type="many2one", relation="module.country", string="Country", store=False)

Property Fields
+++++++++++++++

Declaring a property
""""""""""""""""""""

A property is a special field: fields.property.

.. code-block:: python

        class res_partner(osv.osv):
            _name = "res.partner"
            _inherit = "res.partner"
            _columns = {
                        'property_product_pricelist': fields.property( 
                        'product.pricelist', 
                        type='many2one',· 
                        relation='product.pricelist',· 
                        string="Sale Pricelist",· 
                        method=True, 
                        view_load=True, 
                        group_name="Pricelists Properties"), 
            }


Then you have to create the default value in a .XML file for this property:

.. code-block:: xml

        <record model="ir.property" id="property_product_pricelist">
            <field name="name">property_product_pricelist</field> 
            <field name="fields_id" search="[('model','=','res.partner'),('name','=','property_product_pricelist')]"/> 
            <field name="value" eval="'product.pricelist,'+str(list0)"/> 
        </record>

..

.. tip:: 
        
        if the default value points to a resource from another module, you can use the ref function like this:
        
        <field name="value" eval="'product.pricelist,'+str(ref('module.data_id'))"/> 

**Putting properties in forms**

To add properties in forms, just put the <properties/> tag in your form. This will automatically add all properties fields that are related to this object. The system will add properties depending on your rights. (some people will be able to change a specific property, others won't).

Properties are displayed by section, depending on the group_name attribute. (It is rendered in the client like a separator tag).

**How does this work ?**

The fields.property class inherits from fields.function and overrides the read and write method. The type of this field is many2one, so in the form a property is represented like a many2one function.

But the value of a property is stored in the ir.property class/table as a complete record. The stored value is a field of type reference (not many2one) because each property may point to a different object. If you edit properties values (from the administration menu), these are represented like a field of type reference.

When you read a property, the program gives you the property attached to the instance of object you are reading. It this object has no value, the system will give you the default property.

The definition of a property is stored in the ir.model.fields class like any other fields. In the definition of the property, you can add groups that are allowed to change to property.

**Using properties or normal fields**

When you want to add a new feature, you will have to choose to implement it as a property or as normal field. Use a normal field when you inherit from an object and want to extend this object. Use a property when the new feature is not related to the object but to an external concept.


Here are a few tips to help you choose between a normal field or a property:

Normal fields extend the object, adding more features or data.

A property is a concept that is attached to an object and have special features:

* Different value for the same property depending on the company
* Rights management per field
* It's a link between resources (many2one) 

**Example 1: Account Receivable**

The default "Account Receivable" for a specific partner is implemented as a property because:

    * This is a concept related to the account chart and not to the partner, so it is an account property that is visible on a partner form. Rights have to be managed on this fields for accountants, these are not the same rights that are applied to partner objects. So you have specific rights just for this field of the partner form: only accountants may change the account receivable of a partner. 

    * This is a multi-company field: the same partner may have different account receivable values depending on the company the user belongs to. In a multi-company system, there is one account chart per company. The account receivable of a partner depends on the company it placed the sale order. 

    * The default account receivable is the same for all partners and is configured from the general property menu (in administration). 

.. note::
        One interesting thing is that properties avoid "spaghetti" code. The account module depends on the partner (base) module. But you can install the partner (base) module without the accounting module. If you add a field that points to an account in the partner object, both objects will depend on each other. It's much more difficult to maintain and code (for instance, try to remove a table when both tables are pointing to each others.)

**Example 2: Product Times**

The product expiry module implements all delays related to products: removal date, product usetime, ... This module is very useful for food industries.

This module inherits from the product.product object and adds new fields to it:

.. code-block:: python

        class product_product(osv.osv):

            _inherit = 'product.product' 
            _name = 'product.product' 
            _columns = {

                'life_time': fields.integer('Product lifetime'), 
                'use_time': fields.integer('Product usetime'), 
                'removal_time': fields.integer('Product removal time'), 
                'alert_time': fields.integer('Product alert time'), 
                } 

        product_product()

..

This module adds simple fields to the product.product object. We did not use properties because:

    * We extend a product, the life_time field is a concept related to a product, not to another object.
    * We do not need a right management per field, the different delays are managed by the same people that manage all products. 


Predefined and special fields
+++++++++++++++++++++++++++++

:Predefined:

* **id** Remember that any resource in OpenERP is an object: id is an IDentification number field, managing the principle of identity of the object (two objects are distinct even if they have identical fields values).

* **create_uid** ID of the user that created the resource **create_date** Date of the creation of the record **write_uid** ID of the user that last modified the records **write_date** date of the latest modification

:Special fields:

* **company_id** if present in an object model, allow the data visibility by company (of the user). Note: this special field will have no effect and become a convention since version 4.2.0. This effect is managed through the rule system since 4.2.0.

* **state** object's state, used to show/hide buttons

* **active** is used to automatically show/hide some objects.

:Conventions:

These names are not required and have no special effect in Open ERP but are usually used as a convention:

* **name** name of the record. If you do not provide such a name in a record, you must override the name_search and name_get functions of your object. So it's easier to always put a name field.

* **sequence** is used for ordering different records 

Default values
--------------

:Definition:

The special attribute _defaults allows you to define default values for one or several simple fields of an object.

Because default values do not have to be static (they could, for example, depend on the values of resources already created), you have to define '"default values functions"' and not simple '"scalar"' default values.

To define default values for an object fields, you have to define a dictionary of the form: {'name_of_the_field': function, ...}

These functions take 4 parameters (obj, cr, uid, context) and can return any simple type (boolean, integer, string, etc.).

    * obj: the osv object corresponding to the type of resource being created
    * cr: a database cursor
    * uid: the user ID of the person creating the record
    * context: the current context (given by the client) 

Default values are usually declared by using Python's anonymous functions (also known as lambda functions). If you want more information about lambda functions, please refer to the Python tutorial or Python manual.

*Example:*

        Here is the declaration of default values for the "sale.order" object::

                _defaults = {
                    'date_order': lambda *a: time.strftime('%Y-%m-%d'),
                    'state': lambda *a: 'draft',
                    'user_id': lambda obj, cr, uid, context: uid
                }

Constraints
-----------

Tiny ERP objects can optionally have custom integrity/validity constraints. In case such a constraint is transgressed, the data modification which broke the constraint is canceled and an error message appears on the screen.

Python constraints
++++++++++++++++++

Constraints can be defined by using the _constraints attribute. If defined, it should be a list of tuples (one tuple per constraint) of the form::

        _constraints = [
            (method, 'error message', list_of_field_names), 
            ...
        ]

where:

    * method is an object method used to check the constraint. This method must have the following signature::

                def _name_of_the_method(self, cr, uid, ids): 
                        ...
                        return True|False

    * error message is the error message displayed to the user if the constraint check fails. 

    * list_of_field_names is the list of the names of the fields that will be added to the error message. It should help the user understand why the constraint check failed. 

Example:

        Here is the definition of the integrity constraint for the object "account.move"::

                def _constraint_sum(self, cr, uid, ids):
                        cr.execute('SELECT a.currency_id 
                                    FROM account_move m, account_move_line l, account_account a 
                                    WHERE m.id=l.move_id AND l.account_id=a.id AND m.id IN ('+','.join(map(str, ids))+') 
                                    GROUP BY a.currency_id')
                        if len(cr.fetchall())>=2:
                            return True
                        cr.execute('SELECT abs(SUM(l.amount)) 
                                    FROM account_move m LEFT JOIN account_move_line l ON (m.id=l.move_id) 
                                    WHERE m.id IN ('+','.join(map(str, ids))+')')
                        res = cr.fetchone()[0]
                        return res<0.01
                 
                    _constraints = [
                        (_constraint_sum, 'Error: the sum of all amounts should be zero.', ['name'])
                    ]

SQL Constraints
+++++++++++++++

TODO

Example::

        _sql_constraints = [
                ('code', 'UNIQUE (code)',  'The code must be unique !'),
            ]

:Test:
        
This is for test
        
Example
-------
Here is an example of the definition of an object. More particulary, here is the definition of the object res.partner.

.. code-block:: python

        class res_partner(osv.osv):
            def _credit_get(self, cr, uid, ids, prop, unknow_none, unknow_dict):
                res={}
                for id in ids:
                    acc = ir.ir_get(cr, uid, [('meta','res.partner'),('name','account.receivable')],[('id',str(id))])[0][2]
                    cr.execute('select sum(amount) from account_move_line 
                                where account_id=%d and partner_id=%d', (acc, id))
                    res[id]=cr.fetchone()[0] or 0.0
                return res
         
            def _credit_search(self, cr, uid, obj, name, args):
                if not len(args):
                    return []
                where = ' and '.join(map(lambda x: '(sum(amount)'+x[1]+str(x[2])+')',args))
                cr.execute('select partner_id from account_move_line 
                            where account_id in (select id from account_account where type=%s) 
                            group by partner_id having '+where, ('receivable',) )
                res = cr.fetchall()
                if not len(res):
                    return [('id','=','0')]
                return [('id','in',map(lambda x:x[0], res))]
         
            def _debit_get(self, cr, uid, ids, prop, unknow_none, unknow_dict):
                res={}
                for id in ids:
                    acc = ir.ir_get(cr, uid, [('meta','res.partner'),('name','account.payable')],[('id',str(id))])[0][2]
                    cr.execute('select sum(amount) from account_move_line 
                                where account_id=%d and partner_id=%d', (acc, id))
                    res[id]=cr.fetchone()[0] or 0.0
                return res
         
            def _debit_search(self, cr, uid, obj, name, args):
                if not len(args):
                    return []
                where = ' and '.join(map(lambda x: '(sum(amount)'+x[1]+str(x[2])+')',args))
                cr.execute('select partner_id from account_move_line 
                            where account_id in (select id from account_account where type=%s) 
                            group by partner_id having '+where, ('payable',) )
                res = cr.fetchall()
                if not len(res):
                    return [('id','=','0')]
                return [('id','in',map(lambda x:x[0], res))]
         
            _name = "res.partner"
            _auto=True
            _columns = {
                'name': fields.char('Name', size=64, required=True),
                'name2': fields.char('Corporation Type', size=64),
                'parent_id': fields.many2one('res.partner','Main Company'),
                'commercial': fields.many2one('res.users','Commercial'),
                'child_ids': fields.one2many('res.partner', 'parent_id', 'Partner Ref.'),
                'ref': fields.char('Identifiant', size=64),
                'lang':fields.char('Langage',size=2),
                'vat':fields.char('VAT',size=32),
                'bank':fields.char('Bank account',size=64),
                'website':fields.char('Website',size=64),
                'comment':fields.text('Notes'),
                'address': fields.one2many('res.partner.address', 'partner_id', 'Contacts'),
                'category_id': fields.many2many('res.partner.category', 'res_partner_category_rel', 'partner_id', 'category_id', 'Categories'),
                'events': fields.one2many('res.partner.event', 'partner_id', 'events'),
                'credit': fields.function(_credit_get, fnct_search=_credit_search, method=True, string='Credit'),
                'debit': fields.function(_debit_get, fnct_search=_debit_search, method=True, string='Debit'),
            }
         
            def name_search(self, cr, user, name, args=[], operator='ilike'):
                ids = self.search(cr, user, [('name',operator,name)]+ args)
                ids += self.search(cr, user, [('ref','=',name)]+ args)
                return self.name_get(cr, user, ids)
         
            def _email_send(self, cr, uid, ids, email_from, subject, body, on_error=None):
                emails = self.read(cr, uid, ids, ['email'])
                for email in emails:
                    if email['email']:
                        tools.email_send(email_from, email['email'], subject, body, on_error)
                return True
         
            def email_send(self, cr, uid, ids, email_from, subject, body, on_error=''):
                while len(ids):
                    self.pool.get('ir.cron').create(cr, uid, {
                        'uid':uid, 
                        'name':'Send Partner Emails', 
                        'date':False, 
                        'model':'res.partner', 
                        'function':'_email_send', 
                        'args':pickle.dumps((ids[:16], 
                        email_from, subject, body, on_error))
                        }
                    )
                    ids = ids[16:]
                return True
         
            def address_get(self, cr, uid, ids, adr_pref=['default']):
                cr.execute('select type,id from res_partner_address where partner_id in ('+','.join(map(str,ids))+')')
                res = cr.fetchall()
                adr = dict(res)
                result = {}
                for a in adr_pref:
                    result[a] = adr.get(a, adr.get('default', res[0][1]))
                return result
        res_partner()

Inheritancies
=============

Introduction
------------

Objects may be inherited in some custom or specific modules. It is better to inherit an object to add/modify some fields.

It is done with::

        _inherit='object.name'
        
Extension of an object
----------------------

There are two possible ways to do this kind of inheritance. Both ways result in a new class of data, which holds parent fields and behaviour as well as additional fielda and behaviour, but they differ in heavy programatical consequences. 

While Example 1 creates a new subclass "custom_material" that may be "seen" or "used" by any view or tree which handles "network.material", this will not be the case for Example 2. 

This is due to the table (other.material) the new subclass is operating on, which will never be recognized by previous "network.material" views or trees.

Example 1::

        class custom_material(osv.osv):
	        _name = 'network.material'
	        _inherit = 'network.material'
	        _columns = {
		        'manuf_warranty': fields.boolean('Manufacturer warranty?'),
	        }
	        _defaults = {
		        'manuf_warranty': lambda *a: False,
               }
        custom_material()

.. tip:: Notice
        
        _name == _inherit

In this example, the 'custom_material' will add a new field 'manuf_warranty' to the object 'network.material'. New instances of this class will be visible by views or trees operating on the superclasses table 'network.material'.

This inheritancy is usually called "class inheritance" in Object oriented design. The child inherits data (fields) and behavior (functions) of his parent.


Example 2::

        class other_material(osv.osv):
	        _name = 'other.material'
	        _inherit = 'network.material'
	        _columns = {
		        'manuf_warranty': fields.boolean('Manufacturer warranty?'),
	        }
	        _defaults = {
		        'manuf_warranty': lambda *a: False,
               }
        other_material()

.. tip:: Notice

        _name != _inherit

In this example, the 'other_material' will hold all fields specified by 'network.material' and it will additionally hold a new field 'manuf_warranty'. All those fields will be part of the table 'other.material'. New instances of this class will therefore never been seen by views or trees operating on the superclasses table 'network.material'.

This type of inheritancy is known as "inheritance by prototyping" (e.g. Javascript), because the newly created subclass "copies" all fields from the specified superclass (prototype). The child inherits data (fields) and behavior (functions) of his parent. 


A composite object
------------------

The second form of inheritance in Tiny ERP is used to extend an object from one or more other objects.

        Syntax::

                 class tiny_object(osv.osv)
                     _name = 'tiny.object'
                     _table = 'tiny_object'
                     _inherits = { 'tiny.object'_1_ : name_col'_1_', 'tiny.object'_2_ : name_col'_2_', ..., 'tiny.object'_n_ : name_col'_n_' }
                     (...)

The object 'tiny.object' inherits from all the *columns* and all the *methods* from the **n** objects *'tiny.object'_1_, ..., 'tiny.object'_n_.*

To inherit from multiple tables, the technique consists in adding one column to the table tiny_object per inherited object. This column will store a foreign key (an id from another table). The values *name_col'_1_' name_col'_2_' ... name_col'_n_'* are of type string and determine the title of the columns in which the foreign keys from 'tiny.object'_1_, ..., 'tiny.object'_n_ are stored.

This inheritance mechanism is usually called "instance inheritance" or "value inheritance". A resource (instance) has the VALUES of its parents.
	

..  Improvement of school management module
        =======================================

        Adding function fields
        ----------------------

        Adding relate fields
        --------------------

        Inheriting from partners
        ------------------------

        Inheriting from products
        ------------------------



