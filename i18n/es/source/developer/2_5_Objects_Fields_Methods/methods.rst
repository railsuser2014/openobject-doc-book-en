
.. i18n: ORM methods
.. i18n: ===========

ORM methods
===========

.. i18n: .. describe:: create

.. describe:: create

.. i18n: :Description:

:Description:

.. i18n: Create a new resource 

Create a new resource 

.. i18n: **Signature:** def create(cr, uid, vals, context={}) 

**Signature:** def create(cr, uid, vals, context={}) 

.. i18n: **Parameters:**

**Parameters:**

.. i18n:     * vals: a dictionary of values for every field. This dictionary must use this form: **{'name_of_the_field': value, ...}**
.. i18n:     
.. i18n:     * context (optional): the actual context dictionary. 

    * vals: a dictionary of values for every field. This dictionary must use this form: **{'name_of_the_field': value, ...}**
    
    * context (optional): the actual context dictionary. 

.. i18n:     **Returns:** the id of the newly created resource. 

    **Returns:** the id of the newly created resource. 

.. i18n: Example::
.. i18n: 
.. i18n:         id = pooler.get_pool(cr.dbname).get('res.partner.event').create(cr, uid,
.. i18n:                 {'name': 'Email sent through mass mailing',
.. i18n:                  'partner_id': partner.id,
.. i18n:                  'description': 'The Description for Partner Event'})

Example::

        id = pooler.get_pool(cr.dbname).get('res.partner.event').create(cr, uid,
                {'name': 'Email sent through mass mailing',
                 'partner_id': partner.id,
                 'description': 'The Description for Partner Event'})

.. i18n: .. describe:: search

.. describe:: search

.. i18n: :Description:

:Description:

.. i18n: Search all the resources which satisfy certain criteria 

Search all the resources which satisfy certain criteria 

.. i18n: **Signature**: def search(self, cr, uid, args, offset=0, limit=2000,order=None,context=None, count=False) 

**Signature**: def search(self, cr, uid, args, offset=0, limit=2000,order=None,context=None, count=False) 

.. i18n: **Parameters**

**Parameters**

.. i18n:     * args: a list of tuples containing the search criteria. This list must be of the form: [('name_of_the_field', 'operator', value), ...]. The available operators are:
.. i18n:           - =, >, <, <=, >=
.. i18n:           - IN (sql)
.. i18n:           - LIKE, ILIKE (sql)
.. i18n:           - child_of 
.. i18n:     * offset (optional): do not return the "offset" first results.
.. i18n:     * limit (optional): maximum number of results to return. 

    * args: a list of tuples containing the search criteria. This list must be of the form: [('name_of_the_field', 'operator', value), ...]. The available operators are:
          - =, >, <, <=, >=
          - IN (sql)
          - LIKE, ILIKE (sql)
          - child_of 
    * offset (optional): do not return the "offset" first results.
    * limit (optional): maximum number of results to return. 

.. i18n: **Returns**: the list of ids of matching resources. 

**Returns**: the list of ids of matching resources. 

.. i18n: Example::
.. i18n: 
.. i18n:         ids = pooler.get_pool(cr.dbname).get('res.partner').search(cr, uid, [('category_id', '=', 'Customer')])

Example::

        ids = pooler.get_pool(cr.dbname).get('res.partner').search(cr, uid, [('category_id', '=', 'Customer')])

.. i18n: This example will return a list with all the partners that have the category 'Customer'.

This example will return a list with all the partners that have the category 'Customer'.

.. i18n: .. describe:: read

.. describe:: read

.. i18n: :Description:

:Description:

.. i18n: List of fields resources values. 

List of fields resources values. 

.. i18n:     **Signature**: def read(self, cr, uid, ids, fields=None, context={}) 
.. i18n:     
.. i18n:     **Parameters:**

    **Signature**: def read(self, cr, uid, ids, fields=None, context={}) 
    
    **Parameters:**

.. i18n:             * ids: list of the identifiers of the resources to read (list of integers).
.. i18n:             * fields (optional): the list of the interested fields. If a value is not provided for this parameter, the function will check all the fields.
.. i18n:             * context (optional): the actual context dictionary. 

            * ids: list of the identifiers of the resources to read (list of integers).
            * fields (optional): the list of the interested fields. If a value is not provided for this parameter, the function will check all the fields.
            * context (optional): the actual context dictionary. 

.. i18n:         **Returns**: A list of dictionaries (a dictionary per resource asked) of the form [{'name_of_the_field': value, ...}, ...] 

        **Returns**: A list of dictionaries (a dictionary per resource asked) of the form [{'name_of_the_field': value, ...}, ...] 

.. i18n: Example::
.. i18n: 
.. i18n:         values = pooler.get_pool(cr.dbname).get('res.partner').
.. i18n:                     read(cr, uid, ids, ['name','category_id'], context=context)

Example::

        values = pooler.get_pool(cr.dbname).get('res.partner').
                    read(cr, uid, ids, ['name','category_id'], context=context)

.. i18n: .. describe:: browse

.. describe:: browse

.. i18n: :Description:

:Description:

.. i18n: Return one or several resources with the objects form. These object fields can be reached directly with the pointed notation ("object.name_of_the_field"). The "relations" fields are also automatically evaluated to allow you to recover the values in the "neighbors" objects. 

Return one or several resources with the objects form. These object fields can be reached directly with the pointed notation ("object.name_of_the_field"). The "relations" fields are also automatically evaluated to allow you to recover the values in the "neighbors" objects. 

.. i18n:     **Signature**: def browse(self, cr, uid, select, offset=0, limit=2000) 
.. i18n:     
.. i18n:     **Parameters** 

    **Signature**: def browse(self, cr, uid, select, offset=0, limit=2000) 
    
    **Parameters** 

.. i18n:             * select: this parameter accept data of several types:
.. i18n:                   - an integer : identifier of a resource
.. i18n:                   - a list of integers (list of identifiers) 
.. i18n:             * offset (optional): the number of results to pass.
.. i18n:             * limit (optional): the maximum number of results to return. 

            * select: this parameter accept data of several types:
                  - an integer : identifier of a resource
                  - a list of integers (list of identifiers) 
            * offset (optional): the number of results to pass.
            * limit (optional): the maximum number of results to return. 

.. i18n:     **Returns**: 

    **Returns**: 

.. i18n:             * if an integer (identifier) has been passed as select parameter, return an object having the properties described here above.
.. i18n:             * if a list of integer (identifiers) has been passed, return the object list. 

            * if an integer (identifier) has been passed as select parameter, return an object having the properties described here above.
            * if a list of integer (identifiers) has been passed, return the object list. 

.. i18n: :Example:

:Example:

.. i18n: Let's consider the case of a partner (object 'res.partner') and of a partner contact (object 'res.partner.address'). Let's suppose that we know the identifier of a partner contact (name contact_id) and we want to recover his name and the account number of the company he works for. 

Let's consider the case of a partner (object 'res.partner') and of a partner contact (object 'res.partner.address'). Let's suppose that we know the identifier of a partner contact (name contact_id) and we want to recover his name and the account number of the company he works for. 

.. i18n: Knowing that the object res.partner contains the field::
.. i18n: 
.. i18n:         'bank':fields.char('Bank account',size=64),

Knowing that the object res.partner contains the field::

        'bank':fields.char('Bank account',size=64),

.. i18n: and the object res.partner.address contains the fields::
.. i18n: 
.. i18n:         'partner_id': fields.many2one('res.partner', 'Partner', required=True),
.. i18n:         'name': fields.char('Contact Name', size=64),

and the object res.partner.address contains the fields::

        'partner_id': fields.many2one('res.partner', 'Partner', required=True),
        'name': fields.char('Contact Name', size=64),

.. i18n: the most simple way to proceed is to use the browse method::
.. i18n: 
.. i18n:         addr_obj = self.pool.get('res.partner.address').browse(cr, uid, contact_id)

the most simple way to proceed is to use the browse method::

        addr_obj = self.pool.get('res.partner.address').browse(cr, uid, contact_id)

.. i18n: so, to recover the two fields that interest us, you have to write::
.. i18n: 
.. i18n:         name = addr_obj.name
.. i18n:         account_num = addr_obj.partner_id.bank

so, to recover the two fields that interest us, you have to write::

        name = addr_obj.name
        account_num = addr_obj.partner_id.bank

.. i18n: .. note::
.. i18n: 
.. i18n:         This method is only useful locally (on the server itself) and not with the other interfaces !!

.. note::

        This method is only useful locally (on the server itself) and not with the other interfaces !!

.. i18n: .. describe:: write

.. describe:: write

.. i18n: :Description:

:Description:

.. i18n: Writes values in one or several fields of one or several resources

Writes values in one or several fields of one or several resources

.. i18n:     **Signature:** def write(self, cr, uid, ids, vals, context={}) 
.. i18n:     
.. i18n:     **Parameters:**

    **Signature:** def write(self, cr, uid, ids, vals, context={}) 
    
    **Parameters:**

.. i18n:             * ids: the resources identifiers list to modify.
.. i18n:             * vals: a dictionary with values to write. This dictionary must be with the form: {'name_of_the_field': value, ...}.
.. i18n:             * context (optional): the actual context dictionary. 

            * ids: the resources identifiers list to modify.
            * vals: a dictionary with values to write. This dictionary must be with the form: {'name_of_the_field': value, ...}.
            * context (optional): the actual context dictionary. 

.. i18n:     **Returns:** True 

    **Returns:** True 

.. i18n: Example::
.. i18n: 
.. i18n:         self.pool.get('sale.order').write(cr, uid, ids, {'state':'cancel'})

Example::

        self.pool.get('sale.order').write(cr, uid, ids, {'state':'cancel'})

.. i18n: .. describe:: unlink

.. describe:: unlink

.. i18n: :Description:

:Description:

.. i18n: Delete one or several resources

Delete one or several resources

.. i18n:     **Signature:** def unlink(self, cr, uid, ids) 
.. i18n:     
.. i18n:     **Parameters:**

    **Signature:** def unlink(self, cr, uid, ids) 
    
    **Parameters:**

.. i18n:             * ids: the identifiers resources list to delete. 

            * ids: the identifiers resources list to delete. 

.. i18n:     **Returns:** True 

    **Returns:** True 

.. i18n: Example::
.. i18n: 
.. i18n:          self.pool.get('sale.order').unlink(cr,uid, ids)
.. i18n: 		

Example::

         self.pool.get('sale.order').unlink(cr,uid, ids)
		

.. i18n: Methods to manipulate the default values
.. i18n: ++++++++++++++++++++++++++++++++++++++++

Methods to manipulate the default values
++++++++++++++++++++++++++++++++++++++++

.. i18n: .. describe:: default_get

.. describe:: default_get

.. i18n: :Description:

:Description:

.. i18n: Get back the value by default for one or several fields. 

Get back the value by default for one or several fields. 

.. i18n:     **Signature:** def default_get(self, cr, uid, fields, form=None, reference=None) 
.. i18n:     
.. i18n:     **Parameters:**

    **Signature:** def default_get(self, cr, uid, fields, form=None, reference=None) 
    
    **Parameters:**

.. i18n:             * fields: the fields list which we want to recover the value by default.
.. i18n:             * form (optional): TODO
.. i18n:             * reference (optional): TODO 

            * fields: the fields list which we want to recover the value by default.
            * form (optional): TODO
            * reference (optional): TODO 

.. i18n:     **Returns:** dictionary of the default values of the form {'field_name': value, ... } 

    **Returns:** dictionary of the default values of the form {'field_name': value, ... } 

.. i18n: Example::
.. i18n: 
.. i18n:         self.pool.get('hr.analytic.timesheet').default_get(cr, uid, ['product_id','product_uom_id'])

Example::

        self.pool.get('hr.analytic.timesheet').default_get(cr, uid, ['product_id','product_uom_id'])

.. i18n: .. describe:: default_set

.. describe:: default_set

.. i18n: :Description:

:Description:

.. i18n: Change the default value for one or several fields.

Change the default value for one or several fields.

.. i18n:     **Signature:** def default_set(self, cr, uid, field, value, for_user=False) 
.. i18n:     
.. i18n:     **Parameters:**

    **Signature:** def default_set(self, cr, uid, field, value, for_user=False) 
    
    **Parameters:**

.. i18n:             * field: the name of the field that we want to change the value by default.
.. i18n:             * value: the value by default.
.. i18n:             * for_user (optional): boolean that determines if the new default value must be available only for the current user or for all users. 

            * field: the name of the field that we want to change the value by default.
            * value: the value by default.
            * for_user (optional): boolean that determines if the new default value must be available only for the current user or for all users. 

.. i18n:     **Returns:** True 

    **Returns:** True 

.. i18n: Example::
.. i18n: 
.. i18n:         TODO

Example::

        TODO

.. i18n: Methods to manipulate the permissions
.. i18n: +++++++++++++++++++++++++++++++++++++

Methods to manipulate the permissions
+++++++++++++++++++++++++++++++++++++

.. i18n: .. describe:: perm_read

.. describe:: perm_read

.. i18n: :Description:

:Description:

.. i18n:     **Signature:** def perm_read(self, cr, uid, ids) 
.. i18n:     
.. i18n:     **Parameters:**

    **Signature:** def perm_read(self, cr, uid, ids) 
    
    **Parameters:**

.. i18n:         * ids: an integer list 

        * ids: an integer list 

.. i18n:     **Returns:** a list of dictionaries with the following keys 

    **Returns:** a list of dictionaries with the following keys 

.. i18n:             * level : access level
.. i18n:             * uid : user id
.. i18n:             * gid : group id
.. i18n:             * create_uid: user who created the resource
.. i18n:             * create_date: date when the resource was created
.. i18n:             * write_uid: last user who changed the resource
.. i18n:             * write_date: date of the last change to the resource 

            * level : access level
            * uid : user id
            * gid : group id
            * create_uid: user who created the resource
            * create_date: date when the resource was created
            * write_uid: last user who changed the resource
            * write_date: date of the last change to the resource 

.. i18n: .. describe:: perm_write

.. describe:: perm_write

.. i18n: :Description:

:Description:

.. i18n:     **Signature:** def perm_write(self, cr, uid, ids, fields) 
.. i18n:     
.. i18n:     **Parameters:**
.. i18n:     
.. i18n:     **Returns:**

    **Signature:** def perm_write(self, cr, uid, ids, fields) 
    
    **Parameters:**
    
    **Returns:**

.. i18n: Example::
.. i18n: 
.. i18n:        self.pool.get('res.partner').perm_read(cr, uid, ids, context)

Example::

       self.pool.get('res.partner').perm_read(cr, uid, ids, context)

.. i18n: Methods to generate the fields and the views
.. i18n: ++++++++++++++++++++++++++++++++++++++++++++

Methods to generate the fields and the views
++++++++++++++++++++++++++++++++++++++++++++

.. i18n: .. describe:: fields_get

.. describe:: fields_get

.. i18n: :Description:

:Description:

.. i18n:     **Signature:** def fields_get(self, cr, uid, fields = None, context={}) 
.. i18n:    
.. i18n:     **Parameters:**

    **Signature:** def fields_get(self, cr, uid, fields = None, context={}) 
   
    **Parameters:**

.. i18n:             * fields: a list of fields that interest us, if None, all the fields
.. i18n:             * context: context['lang'] 

            * fields: a list of fields that interest us, if None, all the fields
            * context: context['lang'] 

.. i18n:     **Result:**

    **Result:**

.. i18n: Example:

Example:

.. i18n: In payment.line in account_payment module ::
.. i18n: 
.. i18n:      def fields_get(self, cr, uid, fields=None, context=None):
.. i18n:         res = super(payment_line, self).fields_get(cr, uid, fields, context)
.. i18n:         if 'communication2' in res:
.. i18n:             res['communication2'].setdefault('states', {})
.. i18n:             res['communication2']['states']['structured'] = [('readonly', True)]
.. i18n:             res['communication2']['states']['normal'] = [('readonly', False)]
.. i18n:         return res

In payment.line in account_payment module ::

     def fields_get(self, cr, uid, fields=None, context=None):
        res = super(payment_line, self).fields_get(cr, uid, fields, context)
        if 'communication2' in res:
            res['communication2'].setdefault('states', {})
            res['communication2']['states']['structured'] = [('readonly', True)]
            res['communication2']['states']['normal'] = [('readonly', False)]
        return res

.. i18n: .. describe:: fields_view_get

.. describe:: fields_view_get

.. i18n: :Description:

:Description:

.. i18n:     **Signature:** def fields_view_get(self, cr, uid, view_id=None, view_type='form', context={}, toolbar=False) 

    **Signature:** def fields_view_get(self, cr, uid, view_id=None, view_type='form', context={}, toolbar=False) 

.. i18n:     **Parameters:**
.. i18n:     
.. i18n:     **Result:**

    **Parameters:**
    
    **Result:**

.. i18n: Example:

Example:

.. i18n: In membership module [product.product]::
.. i18n: 
.. i18n:     def fields_view_get(self, cr, user, view_id=None, view_type='form', context=None, toolbar=False):
.. i18n:         if ('product' in context) and (context['product']=='membership_product'):
.. i18n:             model_data_ids_form = self.pool.get('ir.model.data').search(cr,user,[('model','=','ir.ui.view'),('name','in',
.. i18n:                                                                 ['membership_products_form','membership_products_tree'])])
.. i18n:             resource_id_form = self.pool.get('ir.model.data').
.. i18n:                                 read(cr,user,model_data_ids_form,fields=['res_id','name'])
.. i18n:             dict_model={}
.. i18n:             for i in resource_id_form:
.. i18n:                 dict_model[i['name']]=i['res_id']
.. i18n:             if view_type=='form':
.. i18n:                 view_id = dict_model['membership_products_form']
.. i18n:             else:
.. i18n:                 view_id = dict_model['membership_products_tree']
.. i18n:         return super(Product,self).fields_view_get(cr, user, view_id, view_type, context, toolbar)

In membership module [product.product]::

    def fields_view_get(self, cr, user, view_id=None, view_type='form', context=None, toolbar=False):
        if ('product' in context) and (context['product']=='membership_product'):
            model_data_ids_form = self.pool.get('ir.model.data').search(cr,user,[('model','=','ir.ui.view'),('name','in',
                                                                ['membership_products_form','membership_products_tree'])])
            resource_id_form = self.pool.get('ir.model.data').
                                read(cr,user,model_data_ids_form,fields=['res_id','name'])
            dict_model={}
            for i in resource_id_form:
                dict_model[i['name']]=i['res_id']
            if view_type=='form':
                view_id = dict_model['membership_products_form']
            else:
                view_id = dict_model['membership_products_tree']
        return super(Product,self).fields_view_get(cr, user, view_id, view_type, context, toolbar)

.. i18n: .. describe:: distinct_field_get

.. describe:: distinct_field_get

.. i18n: :Description:

:Description:

.. i18n:     **Signature:** def distinct_field_get(self, cr, uid, field, value, args=[], offset=0, limit=2000) 

    **Signature:** def distinct_field_get(self, cr, uid, field, value, args=[], offset=0, limit=2000) 

.. i18n:     **Parameters:**
.. i18n:     
.. i18n:     **Result:**

    **Parameters:**
    
    **Result:**

.. i18n: Example::
.. i18n: 
.. i18n:         TODO

Example::

        TODO

.. i18n: Methods concerning the name of the resources
.. i18n: ++++++++++++++++++++++++++++++++++++++++++++

Methods concerning the name of the resources
++++++++++++++++++++++++++++++++++++++++++++

.. i18n: .. describe:: name_get

.. describe:: name_get

.. i18n: :Description:

:Description:

.. i18n:     **Signature:** def name_get(self, cr, uid, ids, context={}) 
.. i18n:     
.. i18n:     **Parameters:**
.. i18n:     
.. i18n:     **Result:** a list of tuples of the form [(id, name), ...] 

    **Signature:** def name_get(self, cr, uid, ids, context={}) 
    
    **Parameters:**
    
    **Result:** a list of tuples of the form [(id, name), ...] 

.. i18n: Example:

Example:

.. i18n: In res.partner.address::
.. i18n: 
.. i18n:         def name_get(self, cr, user, ids, context={}):
.. i18n:             if not len(ids):
.. i18n:                 return []
.. i18n:             res = []
.. i18n:             for r in self.read(cr, user, ids, ['name','zip','city']):
.. i18n:                 addr = str(r['name'] or '')
.. i18n:                 if r['name'] and (r['zip'] or r['city']):
.. i18n:                     addr += ', '
.. i18n:                 addr += str(r['zip'] or '') + ' ' + str(r['city'] or '')
.. i18n:                 res.append((r['id'], addr))
.. i18n:             return res

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

.. i18n: .. describe:: name_search

.. describe:: name_search

.. i18n: :Description:

:Description:

.. i18n:     **Signature:** def name_search(self, cr, uid, name=, args=[], operator='ilike', context={}) 
.. i18n:     
.. i18n:     **'Parameters:**
.. i18n:     
.. i18n:     **Result:**

    **Signature:** def name_search(self, cr, uid, name=, args=[], operator='ilike', context={}) 
    
    **'Parameters:**
    
    **Result:**

.. i18n: Example:

Example:

.. i18n: In res.country::
.. i18n: 
.. i18n:       def name_search(self, cr, user, name='', args=None, operator='ilike',
.. i18n:             context=None, limit=80):
.. i18n:         if not args:
.. i18n:             args=[]
.. i18n:         if not context:
.. i18n:             context={}
.. i18n:         ids = False
.. i18n:         if len(name) == 2:
.. i18n:             ids = self.search(cr, user, [('code', '=', name)] + args,
.. i18n:                               limit=limit, context=context)
.. i18n:         if not ids:
.. i18n:             ids = self.search(cr, user, [('name', operator, name)] + args,
.. i18n:                               limit=limit, context=context)
.. i18n:         return self.name_get(cr, user, ids, context)

In res.country::

      def name_search(self, cr, user, name='', args=None, operator='ilike',
            context=None, limit=80):
        if not args:
            args=[]
        if not context:
            context={}
        ids = False
        if len(name) == 2:
            ids = self.search(cr, user, [('code', '=', name)] + args,
                              limit=limit, context=context)
        if not ids:
            ids = self.search(cr, user, [('name', operator, name)] + args,
                              limit=limit, context=context)
        return self.name_get(cr, user, ids, context)
