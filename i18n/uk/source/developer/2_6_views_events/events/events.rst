
.. i18n: Events
.. i18n: ======

Events
======

.. i18n: On Change
.. i18n: ------------

On Change
------------

.. i18n: The on_change attribute defines a method that is called when the content of a view field has changed.

The on_change attribute defines a method that is called when the content of a view field has changed.

.. i18n: This method takes at least arguments: cr, uid, ids, which are the three classical arguments and also the context dictionary. You can add parameters to the method. They must correspond to other fields defined in the view, and must also be defined in the XML with fields defined this way::
.. i18n: 
.. i18n:         <field name="name_of_field" on_change="name_of_method(other_field'_1_', ..., other_field'_n_')"/> 

This method takes at least arguments: cr, uid, ids, which are the three classical arguments and also the context dictionary. You can add parameters to the method. They must correspond to other fields defined in the view, and must also be defined in the XML with fields defined this way::

        <field name="name_of_field" on_change="name_of_method(other_field'_1_', ..., other_field'_n_')"/> 

.. i18n: The example below is from the sale order view.

The example below is from the sale order view.

.. i18n: You can use the 'context' keyword to access data in the context that can be used as params of the function.::
.. i18n: 
.. i18n:         <field name="shop_id" select="1" on_change="onchange_shop_id(shop_id)"/>

You can use the 'context' keyword to access data in the context that can be used as params of the function.::

        <field name="shop_id" select="1" on_change="onchange_shop_id(shop_id)"/>

.. i18n: .. code-block:: python
.. i18n: 
.. i18n:         def onchange_shop_id(self, cr, uid, ids, shop_id):
.. i18n: 
.. i18n:             v={} 
.. i18n:             if shop_id:
.. i18n: 
.. i18n:                 shop=self.pool.get('sale.shop').browse(cr,uid,shop_id) 
.. i18n:                 v['project_id']=shop.project_id.id 
.. i18n:                 if shop.pricelist_id.id:
.. i18n: 
.. i18n:                     v['pricelist_id']=shop.pricelist_id.id 
.. i18n: 
.. i18n:                 v['payment_default_id']=shop.payment_default_id.id 
.. i18n: 
.. i18n:             return {'value':v} 

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

.. i18n: When editing the shop_id form field, the onchange_shop_id method of the sale_order object is called and returns a dictionary where the 'value' key contains a dictionary of the new value to use in the 'project_id', 'pricelist_id' and 'payment_default_id' fields.

When editing the shop_id form field, the onchange_shop_id method of the sale_order object is called and returns a dictionary where the 'value' key contains a dictionary of the new value to use in the 'project_id', 'pricelist_id' and 'payment_default_id' fields.

.. i18n: Note that it is possible to change more than just the values of fields. For example, it is possible to change the value of some fields and the domain of other fields by returning a value of the form: return {'domain': d, 'value': value}

Note that it is possible to change more than just the values of fields. For example, it is possible to change the value of some fields and the domain of other fields by returning a value of the form: return {'domain': d, 'value': value}

.. i18n: :context: in *<record model="ir.actions.act_window" id="a">* you can add a context field, which will be pass to the action.

:context: in *<record model="ir.actions.act_window" id="a">* you can add a context field, which will be pass to the action.

.. i18n: See the example below:

See the example below:

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:         <record model="ir.actions.act_window" id="a">
.. i18n:             <field name="name">account.account.tree1</field> 
.. i18n:             <field name="res_model">account.account</field> 
.. i18n:             <field name="view_type">tree</field> 
.. i18n:             <field name="view_mode">form,tree</field> 
.. i18n:             <field name="view_id" ref="v"/> 
.. i18n:             <field name="domain">[('code','=','0')]</field> 
.. i18n:             <field name="context">{'project_id': active_id}</field> 
.. i18n:         </record>

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

.. i18n: view_type::
.. i18n: 
.. i18n:         tree = (tree with shortcuts at the left), form = (switchaable view form/list) 

view_type::

        tree = (tree with shortcuts at the left), form = (switchaable view form/list) 

.. i18n: view_mode::
.. i18n: 
.. i18n:         tree,form : sequences of the views when switching 

view_mode::

        tree,form : sequences of the views when switching 

.. i18n: Getting Defaults
.. i18n: ----------------

Getting Defaults
----------------

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
