==============
Business Logic
==============

Theory
======

On Change
---------

The on_change attribute defines a method that is called when the content of a view field has changed.

This method takes at least arguments: cr, uid, ids, which are the three classical arguments and also the context dictionary. You can add parameters to the method. They must correspond to other fields defined in the view, and must also be defined in the XML with fields defined this way::

        <field name="name_of_field" on_change="name_of_method(other_field'_1_', ..., other_field'_n_')"/> 

The example below is from the sale order view.

You can use the 'context' keyword to access data in the context that can be used as params of the function.::

        <field name="shop_id" select="1" on_change="onchange_shop_id(shop_id)"/>

.. code-block:: python

        def onchange_shop_id(self, cr, uid, ids, shop_id):

            v={} 
            if shop_id:

                shop=self.pool.get('sale.shop').browse(cr,uid,shop_id) 
                v['project_id']=shop.project_id.id 
                if shop.pricelist_id.id:

                    v['pricelist_id']=shop.pricelist_id.id 

                v['payment_default_id']=shop.payment_default_id.id 

            return {'value':v} 


When editing the shop_id form field, the onchange_shop_id method of the sale_order object is called and returns a dictionary where the 'value' key contains a dictionary of the new value to use in the 'project_id', 'pricelist_id' and 'payment_default_id' fields.

Note that it is possible to change more than just the values of fields. For example, it is possible to change the value of some fields and the domain of other fields by returning a value of the form: return {'domain': d, 'value': value}

:context: in *<record model="ir.actions.act_window" id="a">* you can add a context field, which will be pass to the action.

See the example below:

.. code-block:: xml

        <record model="ir.actions.act_window" id="a">
            <field name="name">account.account.tree1</field> 
            <field name="res_model">account.account</field> 
            <field name="view_type">tree</field> 
            <field name="view_mode">form,tree</field> 
            <field name="view_id" ref="v"/> 
            <field name="domain">[('code','=','0')]</field> 
            <field name="context">{'project_id': active_id}</field> 
        </record>


view_type::

        tree = (tree with shortcuts at the left), form = (switchaable view form/list) 

view_mode::

        tree,form : sequences of the views when switching 
        
        
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


Playing with context and domains
--------------------------------

Custom methods can be defined in any Open ERP object. Those methods have the following signature::

        def custom_method_name (self, cr, uid, ids, ..., context={})

The context dictionary is a Python dictionary visible in views where it has been declared. It can be declared in the view itself (in any of its fields) or in an action leading to the view.

    * Declaring the context for a field allows you to declare the context locally : only methods called because of an action on the field on which the context is declared receive the context dictionary (whether they are called directly or indirectly).
    * Declaring the context in an action allows you to declare the context for the whole view : when the action is activated, all the fields attached to the view receive the context declared in the action. 

A context dictionary is declared in a field of a view using the following syntax

.. code-block:: xml

        <field name="field_name" context="field_1_name=field_1_value, field_2_name=field_2_value, ..., field_n_name=field_n_value"/>

A context dictionary is declared in an action using the following syntax :

.. code-block:: xml

        <field name="context">{'field_1_name':'field_1_value', 'field_2_name':'field_2_value', ..., 'field_n_name':'field_n_value'} </field>

Examples The file server/bin/addons/stock/stock_view.xml declares context dictionaries in fields and in actions.

    * Here is a view that contains a field that define context dictionaries : 

        .. code-block:: xml

                <record model="ir.ui.view" id="view_inventory_line_form">
                        <field name="name">stock.inventory.line.form</field>
                            <field name="model">stock.inventory.line</field>
                            <field name="type">form</field>
                            <field name="arch" type="xml">
                            <form string="Stock Inventory Lines">
                                 <field name="location_id" colspan="3" select="1" domain="[('usage','=','internal')]"/>
                                 <field name="product_id" select="1"  
                                      on_change="on_change_product_id(location_id,product_id,product_uom)"
                                      context="location=location_id,uom=product_uom"/>
                                 <field name="product_uom"/>
                                 <field name="product_qty"/>
                            </form>
                        </field>
                   </record>

    * Here is an action that declares a context dictionary : 

        .. code-block:: xml

                <record model="ir.actions.act_window" id="action_picking_tree">
                        <field name="name">stock.picking</field>
                      <field name="res_model">stock.picking</field>
                      <field name="type">ir.actions.act_window</field>
                      <field name="view_type">form</field>
                      <field name="view_mode">tree,form</field>
                      <field name="domain">[('type','=','out')]</field>
                      <field name="context">{'contact_display': 'partner'}</field>
                  </record>

..        Server Actions
        --------------


Overriding default methods
--------------------------

All Open ERP objects define a set of methods as we will see in the section "Predefined Methods". Of course, you can also add your own methods to a particular object.

All methods defined on an object are accessible from the outside (other objects or RPC), but don't forget the Python convention that makes a method private, if it is prefixed with two underscores. 


The predefined methods may be classified into 5 categories: the basic methods, methods to manipulate default values, methods to get the permissions, methods to return the fields and views, and finally those naming the resource.


Basic methods
+++++++++++++

create
""""""

:Description:

Create a new resource 

**Signature:** def create(cr, uid, vals, context={}) 

**Parameters:**

    * vals: a dictionary of values for every field. This dictionary must use this form: **{'name_of_the_field': value, ...}**
    
    * context (optional): the actual context dictionary. 

    **Returns:** the id of the newly created resource. 

Example::

        id = pooler.get_pool(cr.dbname).get('res.partner.event').create(cr, uid,
                {'name': 'Email sent through mass mailing',
                 'partner_id': partner.id,
                 'description': 'The Description for Partner Event'})

search
""""""

:Description:

Search all the resources which satisfy certain criteria 

**Signature**: def search(self, cr, uid, args, offset=0, limit=2000,order=None,context=None, count=False) 

**Parameters**

    * args: a list of tuples containing the search criteria. This list must be of the form: [('name_of_the_field', 'operator', value), ...]. The available operators are:
          - =, >, <, <=, >=
          - IN (sql)
          - LIKE, ILIKE (sql)
          - child_of 
    * offset (optional): do not return the "offset" first results.
    * limit (optional): maximum number of results to return. 

**Returns**: the list of ids of matching resources. 

Example::

        ids = pooler.get_pool(cr.dbname).get('res.partner').search(cr, uid, [('category_id', '=', 'Customer')])

This example will return a list with all the partners that have the category 'Customer'.

read
""""

:Description:

List of fields resources values. 

    **Signature**: def read(self, cr, uid, ids, fields=None, context={}) 
    
    **Parameters:**

            * ids: list of the identifiers of the resources to read (list of integers).
            * fields (optional): the list of the interested fields. If a value is not provided for this parameter, the function will check all the fields.
            * context (optional): the actual context dictionary. 

        **Returns**: A list of dictionaries (a dictionary per resource asked) of the form [{'name_of_the_field': value, ...}, ...] 

Example::

        values = pooler.get_pool(cr.dbname).get('res.partner').read(cr, uid, ids, ['name','category_id'], context=context)

browse
"""""""

:Description:

Return one or several resources with the objects form. These object fields can be reached directly with the pointed notation ("object.name_of_the_field"). The "relations" fields are also automatically evaluated to allow you to recover the values in the "neighbors" objects. 

    **Signature**: def browse(self, cr, uid, select, offset=0, limit=2000) 
    
    **Parameters** 

            * select: this parameter accept data of several types:
                  - an integer : identifier of a resource
                  - a list of integers (list of identifiers) 
            * offset (optional): the number of results to pass.
            * limit (optional): the maximum number of results to return. 

    **Returns**: 

            * if an integer (identifier) has been passed as select parameter, return an object having the properties described here above.
            * if a list of integer (identifiers) has been passed, return the object list. 

:Example:

Let's consider the case of a partner (object 'res.partner') and of a partner contact (object 'res.partner.address'). Let's suppose that we know the identifier of a partner contact (name contact_id) and we want to recover his name and the account number of the company he works for. 

Knowing that the object res.partner contains the field::

        'bank':fields.char('Bank account',size=64),

and the object res.partner.address contains the fields::

        'partner_id': fields.many2one('res.partner', 'Partner', required=True),
        'name': fields.char('Contact Name', size=64),

the most simple way to proceed is to use the browse method::

        addr_obj = self.pool.get('res.partner.address').browse(cr, uid, contact_id)

so, to recover the two fields that interest us, you have to write::

        name = addr_obj.name
        account_num = addr_obj.partner_id.bank

.. note::

        This method is only useful locally (on the server itself) and not with the other interfaces !!


write
"""""

:Description:

Writes values in one or several fields of one or several resources

    **Signature:** def write(self, cr, uid, ids, vals, context={}) 
    
    **Parameters:**

            * ids: the resources identifiers list to modify.
            * vals: a dictionary with values to write. This dictionary must be with the form: {'name_of_the_field': value, ...}.
            * context (optional): the actual context dictionary. 

    **Returns:** True 

Example::

        self.pool.get('sale.order').write(cr, uid, ids, {'state':'cancel'})


unlink
""""""

:Description:

Delete one or several resources

    **Signature:** def unlink(self, cr, uid, ids) 
    
    **Parameters:**

            * ids: the identifiers resources list to delete. 

    **Returns:** True 

Example::

        TODO


Methods to manipulate the default values
++++++++++++++++++++++++++++++++++++++++

default_get
"""""""""""

:Description:

Get back the value by default for one or several fields. 

    **Signature:** def default_get(self, cr, uid, fields, form=None, reference=None) 
    
    **Parameters:**

            * fields: the fields list which we want to recover the value by default.
            * form (optional): TODO
            * reference (optional): TODO 

    **Returns:** dictionary of the default values of the form {'field_name': value, ... } 

Example::

        TODO

default_set
"""""""""""

:Description:

Change the default value for one or several fields.

    **Signature:** def default_set(self, cr, uid, field, value, for_user=False) 
    
    **Parameters:**

            * field: the name of the field that we want to change the value by default.
            * value: the value by default.
            * for_user (optional): boolean that determines if the new default value must be available only for the current user or for all users. 

    **Returns:** True 

Example::

        TODO

Methods to manipulate the permissions
+++++++++++++++++++++++++++++++++++++

perm_read
"""""""""

:Description:

    **Signature:** def perm_read(self, cr, uid, ids) 
    
    **Parameters:**

        * ids: an integer list 

    **Returns:** a list of dictionaries with the following keys 

            * level : access level
            * uid : user id
            * gid : group id
            * create_uid: user who created the resource
            * create_date: date when the resource was created
            * write_uid: last user who changed the resource
            * write_date: date of the last change to the resource 

perm_write
""""""""""

:Description:

    **Signature:** def perm_write(self, cr, uid, ids, fields) 
    
    **Parameters:**
    
    **Returns:**

Example::

        TODO

Methods to generate the fields and the views
++++++++++++++++++++++++++++++++++++++++++++

fields_get
""""""""""

:Description:

    **Signature:** def fields_get(self, cr, uid, fields = None, context={}) 
   
    **Parameters:**

            * fields: a list of fields that interest us, if None, all the fields
            * context: context['lang'] 

    **Result:**

Example::

        TODO

fields_view_get
"""""""""""""""

:Description:

    **Signature:** def fields_view_get(self, cr, uid, view_id=None, view_type='form', context={}, toolbar=False) 

    **Parameters:**
    
    **Result:**

Example::

        TODO

distinct_field_get
""""""""""""""""""

:Description:

    **Signature:** def distinct_field_get(self, cr, uid, field, value, args=[], offset=0, limit=2000) 

    **Parameters:**
    
    **Result:**

Example::

        TODO

Methods concerning the name of the resources
++++++++++++++++++++++++++++++++++++++++++++

name_get
""""""""""

:Description:

    **Signature:** def name_get(self, cr, uid, ids, context={}) 
    
    **Parameters:**
    
    **Result:** a list of tuples of the form [(id, name), ...] 

Example:

In res.partner.address::

        def name_get(self, cr, user, ids, context={}):
            if not len(ids):
                return []
            res = []
            for r in self.read(cr, user, ids, ['name','zip','city']):
                addr = str(r['name'] or '')
                if r['name'] and (r['zip'] or r['city']):
                    addr += ', '
                addr += str(r['zip'] or '') + ' ' + str(r['city'] or '')
                res.append((r['id'], addr))
            return res

name_search
"""""""""""

:Description:

    **Signature:** def name_search(self, cr, uid, name=, args=[], operator='ilike', context={}) 
    
    **'Parameters:**
    
    **Result:**

Example::

        TODO




..  Improvement of school management module
        =======================================

        Improvement 1
        -------------


        Improvement 2
        -------------


        Improvement 3
        -------------



