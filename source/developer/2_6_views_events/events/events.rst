Events
======

On Change
------------

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

Getting Defaults
----------------

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
