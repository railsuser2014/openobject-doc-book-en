ORM methods
===========

.. describe:: create

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

.. describe:: search

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

.. describe:: read

:Description:

List of fields resources values. 

    **Signature**: def read(self, cr, uid, ids, fields=None, context={}) 
    
    **Parameters:**

            * ids: list of the identifiers of the resources to read (list of integers).
            * fields (optional): the list of the interested fields. If a value is not provided for this parameter, the function will check all the fields.
            * context (optional): the actual context dictionary. 

        **Returns**: A list of dictionaries (a dictionary per resource asked) of the form [{'name_of_the_field': value, ...}, ...] 

Example::

        values = pooler.get_pool(cr.dbname).get('res.partner').
                    read(cr, uid, ids, ['name','category_id'], context=context)

.. describe:: browse

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

.. describe:: write

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

.. describe:: unlink

:Description:

Delete one or several resources

    **Signature:** def unlink(self, cr, uid, ids) 
    
    **Parameters:**

            * ids: the identifiers resources list to delete. 

    **Returns:** True 

Example::

         self.pool.get('sale.order').unlink(cr,uid, ids)
		


Methods to manipulate the default values
++++++++++++++++++++++++++++++++++++++++

.. describe:: default_get

:Description:

Get back the value by default for one or several fields. 

    **Signature:** def default_get(self, cr, uid, fields, form=None, reference=None) 
    
    **Parameters:**

            * fields: the fields list which we want to recover the value by default.
            * form (optional): TODO
            * reference (optional): TODO 

    **Returns:** dictionary of the default values of the form {'field_name': value, ... } 

Example::

        self.pool.get('hr.analytic.timesheet').default_get(cr, uid, ['product_id','product_uom_id'])

.. describe:: default_set

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

.. describe:: perm_read

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

.. describe:: perm_write

:Description:

    **Signature:** def perm_write(self, cr, uid, ids, fields) 
    
    **Parameters:**
    
    **Returns:**

Example::

       self.pool.get('res.partner').perm_read(cr, uid, ids, context)

Methods to generate the fields and the views
++++++++++++++++++++++++++++++++++++++++++++

.. describe:: fields_get

:Description:

    **Signature:** def fields_get(self, cr, uid, fields = None, context={}) 
   
    **Parameters:**

            * fields: a list of fields that interest us, if None, all the fields
            * context: context['lang'] 

    **Result:**

Example:

In payment.line in account_payment module ::

     def fields_get(self, cr, uid, fields=None, context=None):
        res = super(payment_line, self).fields_get(cr, uid, fields, context)
        if 'communication2' in res:
            res['communication2'].setdefault('states', {})
            res['communication2']['states']['structured'] = [('readonly', True)]
            res['communication2']['states']['normal'] = [('readonly', False)]
        return res

.. describe:: fields_view_get

:Description:

    **Signature:** def fields_view_get(self, cr, uid, view_id=None, view_type='form', context={}, toolbar=False) 

    **Parameters:**
    
    **Result:**

Example:

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

.. describe:: distinct_field_get

:Description:

    **Signature:** def distinct_field_get(self, cr, uid, field, value, args=[], offset=0, limit=2000) 

    **Parameters:**
    
    **Result:**

Example::

        TODO

Methods concerning the name of the resources
++++++++++++++++++++++++++++++++++++++++++++

.. describe:: name_get

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

.. describe:: name_search

:Description:

    **Signature:** def name_search(self, cr, uid, name=, args=[], operator='ilike', context={}) 
    
    **'Parameters:**
    
    **Result:**

Example:

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


