
.. i18n: Type of Fields
.. i18n: ==============

Type of Fields
==============

.. i18n: Basic Types
.. i18n: ------------

Basic Types
------------

.. i18n: :boolean:

:boolean:

.. i18n: A boolean (true, false).

A boolean (true, false).

.. i18n:         Syntax::
.. i18n: 
.. i18n:                 fields.boolean('Field Name' [, Optional Parameters]),

        Syntax::

                fields.boolean('Field Name' [, Optional Parameters]),

.. i18n: :integer:

:integer:

.. i18n: An integer.
.. i18n:         
.. i18n:         Syntax::
.. i18n: 
.. i18n:                 fields.integer('Field Name' [, Optional Parameters]),

An integer.
        
        Syntax::

                fields.integer('Field Name' [, Optional Parameters]),

.. i18n: :float:

:float:

.. i18n: A floating point number.

A floating point number.

.. i18n:         Syntax::
.. i18n: 
.. i18n:                 fields.float('Field Name' [, Optional Parameters]),

        Syntax::

                fields.float('Field Name' [, Optional Parameters]),

.. i18n:         .. note::
.. i18n: 
.. i18n:                 The optional parameter digits defines the precision and scale of the number. The scale being the number of digits after the decimal point whereas the precision is the total number of significant digits in the number (before and after the decimal point). If the parameter digits is not present, the number will be a double precision floating point number. Warning: these floating-point numbers are inexact (not any value can be converted to its binary representation) and this can lead to rounding errors. You should always use the digits parameter for monetary amounts.
.. i18n:         
.. i18n:         
.. i18n:         Example
.. i18n: 
.. i18n:         'rate' : fields.float('Relative Change rate', digits=(12,6) [, Optional Parameters]),

        .. note::

                The optional parameter digits defines the precision and scale of the number. The scale being the number of digits after the decimal point whereas the precision is the total number of significant digits in the number (before and after the decimal point). If the parameter digits is not present, the number will be a double precision floating point number. Warning: these floating-point numbers are inexact (not any value can be converted to its binary representation) and this can lead to rounding errors. You should always use the digits parameter for monetary amounts.
        
        
        Example

        'rate' : fields.float('Relative Change rate', digits=(12,6) [, Optional Parameters]),

.. i18n: :char:

:char:

.. i18n: A string of limited length. The required size parameter determines its size.

A string of limited length. The required size parameter determines its size.

.. i18n:         Syntax::
.. i18n: 
.. i18n:                 fields.char('Field Name', size=n [, Optional Parameters]), # where ''n'' is an integer.

        Syntax::

                fields.char('Field Name', size=n [, Optional Parameters]), # where ''n'' is an integer.

.. i18n: Example

Example

.. i18n: 'city' : fields.char('City Name', size=30, required=True),

'city' : fields.char('City Name', size=30, required=True),

.. i18n: :text:

:text:

.. i18n: A text field with no limit in length.

A text field with no limit in length.

.. i18n:         Syntax::
.. i18n: 
.. i18n:                 fields.text('Field Name' [, Optional Parameters]),

        Syntax::

                fields.text('Field Name' [, Optional Parameters]),

.. i18n: :date:

:date:

.. i18n: A date.

A date.

.. i18n:         Syntax::
.. i18n: 
.. i18n:                 fields.date('Field Name' [, Optional Parameters]),

        Syntax::

                fields.date('Field Name' [, Optional Parameters]),

.. i18n: :datetime:

:datetime:

.. i18n: Allows to store a date and the time of day in the same field.

Allows to store a date and the time of day in the same field.

.. i18n:         Syntax::
.. i18n: 
.. i18n:                 fields.datetime('Field Name' [, Optional Parameters]),

        Syntax::

                fields.datetime('Field Name' [, Optional Parameters]),

.. i18n: :binary:

:binary:

.. i18n: A binary chain

A binary chain

.. i18n: :selection:

:selection:

.. i18n: A field which allows the user to make a selection between various predefined values.

A field which allows the user to make a selection between various predefined values.

.. i18n:         Syntax::
.. i18n: 
.. i18n:                 fields.selection((('n','Unconfirmed'), ('c','Confirmed')), 
.. i18n:                                    'Field Name' [, Optional Parameters]),

        Syntax::

                fields.selection((('n','Unconfirmed'), ('c','Confirmed')), 
                                   'Field Name' [, Optional Parameters]),

.. i18n: .. note::
.. i18n: 
.. i18n:         Format of the selection parameter: tuple of tuples of strings of the form::
.. i18n: 
.. i18n:                 (('key_or_value', 'string_to_display'), ... )

.. note::

        Format of the selection parameter: tuple of tuples of strings of the form::

                (('key_or_value', 'string_to_display'), ... )

.. i18n: *Example*

*Example*

.. i18n: Using relation fields **many2one** with **selection**. In fields definitions add::
.. i18n: 
.. i18n:         ...,
.. i18n:         'my_field': fields.many2one('mymodule.relation.model', 'Title', selection=_sel_func), 
.. i18n:         ...,

Using relation fields **many2one** with **selection**. In fields definitions add::

        ...,
        'my_field': fields.many2one('mymodule.relation.model', 'Title', selection=_sel_func), 
        ...,

.. i18n: And then define the _sel_func like this (but before the fields definitions)::
.. i18n: 
.. i18n:         def _sel_func(self, cr, uid, context={}): 
.. i18n:             obj = self.pool.get('mymodule.relation.model') 
.. i18n:             ids = obj.search(cr, uid, []) 
.. i18n:             res = obj.read(cr, uid, ids, ['name', 'id'], context) 
.. i18n:             res = [(r['id'], r['name']) for r in res] 
.. i18n:             return res
.. i18n:             

And then define the _sel_func like this (but before the fields definitions)::

        def _sel_func(self, cr, uid, context={}): 
            obj = self.pool.get('mymodule.relation.model') 
            ids = obj.search(cr, uid, []) 
            res = obj.read(cr, uid, ids, ['name', 'id'], context) 
            res = [(r['id'], r['name']) for r in res] 
            return res
            

.. i18n: Relational Types
.. i18n: ----------------

Relational Types
----------------

.. i18n: :one2one:

:one2one:

.. i18n: A one2one field expresses a one:to:one relation between two objects. It is deprecated. Use many2one instead.
.. i18n:         
.. i18n:         syntax::
.. i18n: 
.. i18n:                 fields.one2one('other.object.name', 'Field Name')

A one2one field expresses a one:to:one relation between two objects. It is deprecated. Use many2one instead.
        
        syntax::

                fields.one2one('other.object.name', 'Field Name')

.. i18n: :many2one:

:many2one:

.. i18n: Associates this object to a parent object via this Field. For example Department an Employee belongs to would Many to one. i.e Many employees will belong to a Department

Associates this object to a parent object via this Field. For example Department an Employee belongs to would Many to one. i.e Many employees will belong to a Department

.. i18n:         syntax::
.. i18n: 
.. i18n:                 fields.many2one('other.object.name', 'Field Name', optional parameter)

        syntax::

                fields.many2one('other.object.name', 'Field Name', optional parameter)

.. i18n:         * Optional parameters:
.. i18n:                 - ondelete: What should happen when the resource this field points to is deleted.
.. i18n:                         + Predefined value: "cascade", "set null"
.. i18n:                         + Default value: "set null" 
.. i18n:                 - required: True
.. i18n:                 - readonly: True
.. i18n:                 - select: True - (creates an index on the Foreign Key field) 

        * Optional parameters:
                - ondelete: What should happen when the resource this field points to is deleted.
                        + Predefined value: "cascade", "set null"
                        + Default value: "set null" 
                - required: True
                - readonly: True
                - select: True - (creates an index on the Foreign Key field) 

.. i18n:         *Example*

        *Example*

.. i18n:                 'commercial': fields.many2one('res.users', 'Commercial', ondelete='cascade'),

                'commercial': fields.many2one('res.users', 'Commercial', ondelete='cascade'),

.. i18n: :one2many:

:one2many:

.. i18n: TODO

TODO

.. i18n:         syntax::
.. i18n: 
.. i18n:                 fields.one2many('other.object.name', 'Field relation id', 'Fieldname', optional parameter)

        syntax::

                fields.one2many('other.object.name', 'Field relation id', 'Fieldname', optional parameter)

.. i18n:         * Optional parameters:
.. i18n:                 - invisible: True/False
.. i18n:                 - states: ?
.. i18n:                 - readonly: True/False 

        * Optional parameters:
                - invisible: True/False
                - states: ?
                - readonly: True/False 

.. i18n:         *Example*

        *Example*

.. i18n:                 'address': fields.one2many('res.partner.address', 'partner_id', 'Contacts'),

                'address': fields.one2many('res.partner.address', 'partner_id', 'Contacts'),

.. i18n: :many2many:

:many2many:

.. i18n: TODO

TODO

.. i18n:         syntax::
.. i18n: 
.. i18n:                 fields.many2many('other.object.name', 
.. i18n:                                  'relation object', 
.. i18n:                                  'other.object.id', 
.. i18n:                                  'actual.object.id', 
.. i18n:                                  'Field Name')

        syntax::

                fields.many2many('other.object.name', 
                                 'relation object', 
                                 'other.object.id', 
                                 'actual.object.id', 
                                 'Field Name')

.. i18n:         * where
.. i18n:                 - other.object.name is the other object which belongs to the relation
.. i18n:                 - relation object is the table that makes the link
.. i18n:                 - other.object.id and actual.object.id are the fields' names used in the relation table 

        * where
                - other.object.name is the other object which belongs to the relation
                - relation object is the table that makes the link
                - other.object.id and actual.object.id are the fields' names used in the relation table 

.. i18n:         Example::
.. i18n: 
.. i18n:                 'category_id': 
.. i18n:                    fields.many2many(
.. i18n:                     'res.partner.category', 
.. i18n:                     'res_partner_category_rel', 
.. i18n:                     'partner_id', 
.. i18n:                     'category_id', 
.. i18n:                     'Categories'),

        Example::

                'category_id': 
                   fields.many2many(
                    'res.partner.category', 
                    'res_partner_category_rel', 
                    'partner_id', 
                    'category_id', 
                    'Categories'),

.. i18n: :related:

:related:

.. i18n: Sometimes you need to refer the relation of a relation. For example, supposing you have objects: City <- State <- Country, and you need to refer Country in a City, you can define a field as below in the City object::
.. i18n: 
.. i18n:         'country_id': fields.related('state_id', 'country_id', type="many2one", 
.. i18n: 				      relation="module.country", string="Country", store=False)

Sometimes you need to refer the relation of a relation. For example, supposing you have objects: City <- State <- Country, and you need to refer Country in a City, you can define a field as below in the City object::

        'country_id': fields.related('state_id', 'country_id', type="many2one", 
				      relation="module.country", string="Country", store=False)

.. i18n: Property Fields
.. i18n: +++++++++++++++

Property Fields
+++++++++++++++

.. i18n: .. describe:: Declaring a property

.. describe:: Declaring a property

.. i18n: A property is a special field: fields.property.

A property is a special field: fields.property.

.. i18n: .. code-block:: python
.. i18n: 
.. i18n:         class res_partner(osv.osv):
.. i18n:             _name = "res.partner"
.. i18n:             _inherit = "res.partner"
.. i18n:             _columns = {
.. i18n:                         'property_product_pricelist': fields.property( 
.. i18n:                         'product.pricelist', 
.. i18n:                         type='many2one',· 
.. i18n:                         relation='product.pricelist',· 
.. i18n:                         string="Sale Pricelist",· 
.. i18n:                         method=True, 
.. i18n:                         view_load=True, 
.. i18n:                         group_name="Pricelists Properties"), 
.. i18n:             }

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

.. i18n: Then you have to create the default value in a .XML file for this property:

Then you have to create the default value in a .XML file for this property:

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:         <record model="ir.property" id="property_product_pricelist">
.. i18n:             <field name="name">property_product_pricelist</field> 
.. i18n:             <field name="fields_id" search="[('model','=','res.partner'),
.. i18n:               ('name','=','property_product_pricelist')]"/> 
.. i18n:             <field name="value" eval="'product.pricelist,'+str(list0)"/> 
.. i18n:         </record>

.. code-block:: xml

        <record model="ir.property" id="property_product_pricelist">
            <field name="name">property_product_pricelist</field> 
            <field name="fields_id" search="[('model','=','res.partner'),
              ('name','=','property_product_pricelist')]"/> 
            <field name="value" eval="'product.pricelist,'+str(list0)"/> 
        </record>

.. i18n: ..

..

.. i18n: .. tip:: 
.. i18n:         
.. i18n:         if the default value points to a resource from another module, you can use the ref function like this:
.. i18n:         
.. i18n:         <field name="value" eval="'product.pricelist,'+str(ref('module.data_id'))"/> 

.. tip:: 
        
        if the default value points to a resource from another module, you can use the ref function like this:
        
        <field name="value" eval="'product.pricelist,'+str(ref('module.data_id'))"/> 

.. i18n: **Putting properties in forms**

**Putting properties in forms**

.. i18n: To add properties in forms, just put the <properties/> tag in your form. This will automatically add all properties fields that are related to this object. The system will add properties depending on your rights. (some people will be able to change a specific property, others won't).

To add properties in forms, just put the <properties/> tag in your form. This will automatically add all properties fields that are related to this object. The system will add properties depending on your rights. (some people will be able to change a specific property, others won't).

.. i18n: Properties are displayed by section, depending on the group_name attribute. (It is rendered in the client like a separator tag).

Properties are displayed by section, depending on the group_name attribute. (It is rendered in the client like a separator tag).

.. i18n: **How does this work ?**

**How does this work ?**

.. i18n: The fields.property class inherits from fields.function and overrides the read and write method. The type of this field is many2one, so in the form a property is represented like a many2one function.

The fields.property class inherits from fields.function and overrides the read and write method. The type of this field is many2one, so in the form a property is represented like a many2one function.

.. i18n: But the value of a property is stored in the ir.property class/table as a complete record. The stored value is a field of type reference (not many2one) because each property may point to a different object. If you edit properties values (from the administration menu), these are represented like a field of type reference.

But the value of a property is stored in the ir.property class/table as a complete record. The stored value is a field of type reference (not many2one) because each property may point to a different object. If you edit properties values (from the administration menu), these are represented like a field of type reference.

.. i18n: When you read a property, the program gives you the property attached to the instance of object you are reading. It this object has no value, the system will give you the default property.

When you read a property, the program gives you the property attached to the instance of object you are reading. It this object has no value, the system will give you the default property.

.. i18n: The definition of a property is stored in the ir.model.fields class like any other fields. In the definition of the property, you can add groups that are allowed to change to property.

The definition of a property is stored in the ir.model.fields class like any other fields. In the definition of the property, you can add groups that are allowed to change to property.

.. i18n: **Using properties or normal fields**

**Using properties or normal fields**

.. i18n: When you want to add a new feature, you will have to choose to implement it as a property or as normal field. Use a normal field when you inherit from an object and want to extend this object. Use a property when the new feature is not related to the object but to an external concept.

When you want to add a new feature, you will have to choose to implement it as a property or as normal field. Use a normal field when you inherit from an object and want to extend this object. Use a property when the new feature is not related to the object but to an external concept.

.. i18n: Here are a few tips to help you choose between a normal field or a property:

Here are a few tips to help you choose between a normal field or a property:

.. i18n: Normal fields extend the object, adding more features or data.

Normal fields extend the object, adding more features or data.

.. i18n: A property is a concept that is attached to an object and have special features:

A property is a concept that is attached to an object and have special features:

.. i18n: * Different value for the same property depending on the company
.. i18n: * Rights management per field
.. i18n: * It's a link between resources (many2one) 

* Different value for the same property depending on the company
* Rights management per field
* It's a link between resources (many2one) 

.. i18n: **Example 1: Account Receivable**

**Example 1: Account Receivable**

.. i18n: The default "Account Receivable" for a specific partner is implemented as a property because:

The default "Account Receivable" for a specific partner is implemented as a property because:

.. i18n:     * This is a concept related to the account chart and not to the partner, so it is an account property that is visible on a partner form. Rights have to be managed on this fields for accountants, these are not the same rights that are applied to partner objects. So you have specific rights just for this field of the partner form: only accountants may change the account receivable of a partner. 
.. i18n: 
.. i18n:     * This is a multi-company field: the same partner may have different account receivable values depending on the company the user belongs to. In a multi-company system, there is one account chart per company. The account receivable of a partner depends on the company it placed the sale order. 
.. i18n: 
.. i18n:     * The default account receivable is the same for all partners and is configured from the general property menu (in administration). 

    * This is a concept related to the account chart and not to the partner, so it is an account property that is visible on a partner form. Rights have to be managed on this fields for accountants, these are not the same rights that are applied to partner objects. So you have specific rights just for this field of the partner form: only accountants may change the account receivable of a partner. 

    * This is a multi-company field: the same partner may have different account receivable values depending on the company the user belongs to. In a multi-company system, there is one account chart per company. The account receivable of a partner depends on the company it placed the sale order. 

    * The default account receivable is the same for all partners and is configured from the general property menu (in administration). 

.. i18n: .. note::
.. i18n:         One interesting thing is that properties avoid "spaghetti" code. The account module depends on the partner (base) module. But you can install the partner (base) module without the accounting module. If you add a field that points to an account in the partner object, both objects will depend on each other. It's much more difficult to maintain and code (for instance, try to remove a table when both tables are pointing to each others.)

.. note::
        One interesting thing is that properties avoid "spaghetti" code. The account module depends on the partner (base) module. But you can install the partner (base) module without the accounting module. If you add a field that points to an account in the partner object, both objects will depend on each other. It's much more difficult to maintain and code (for instance, try to remove a table when both tables are pointing to each others.)

.. i18n: **Example 2: Product Times**

**Example 2: Product Times**

.. i18n: The product expiry module implements all delays related to products: removal date, product usetime, ... This module is very useful for food industries.

The product expiry module implements all delays related to products: removal date, product usetime, ... This module is very useful for food industries.

.. i18n: This module inherits from the product.product object and adds new fields to it:

This module inherits from the product.product object and adds new fields to it:

.. i18n: .. code-block:: python
.. i18n: 
.. i18n:         class product_product(osv.osv):
.. i18n: 
.. i18n:             _inherit = 'product.product' 
.. i18n:             _name = 'product.product' 
.. i18n:             _columns = {
.. i18n: 
.. i18n:                 'life_time': fields.integer('Product lifetime'), 
.. i18n:                 'use_time': fields.integer('Product usetime'), 
.. i18n:                 'removal_time': fields.integer('Product removal time'), 
.. i18n:                 'alert_time': fields.integer('Product alert time'), 
.. i18n:                 } 
.. i18n: 
.. i18n:         product_product()

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

.. i18n: ..

..

.. i18n: This module adds simple fields to the product.product object. We did not use properties because:

This module adds simple fields to the product.product object. We did not use properties because:

.. i18n:     * We extend a product, the life_time field is a concept related to a product, not to another object.
.. i18n:     * We do not need a right management per field, the different delays are managed by the same people that manage all products. 

    * We extend a product, the life_time field is a concept related to a product, not to another object.
    * We do not need a right management per field, the different delays are managed by the same people that manage all products. 
