
.. i18n: Information Repository
.. i18n: ======================

Information Repository
======================

.. i18n: The information repository is a semantics tree in which the datas that are not the ressources are stocked. We find in this structure:

The information repository is a semantics tree in which the datas that are not the ressources are stocked. We find in this structure:

.. i18n:    1. the values by default
.. i18n:    2. the conditional values;
.. i18n:           * the state depends on the zip code,
.. i18n:           * the payment method depends of the partner, ... 
.. i18n:    3. the reactions to the events client;
.. i18n:           * click on the invoice menu,
.. i18n:           * print an invoice,
.. i18n:           * action on a partner, ... 

   1. the values by default
   2. the conditional values;
          * the state depends on the zip code,
          * the payment method depends of the partner, ... 
   3. the reactions to the events client;
          * click on the invoice menu,
          * print an invoice,
          * action on a partner, ... 

.. i18n: The IR has 3 methods;

The IR has 3 methods;

.. i18n:     * add a value in the tree
.. i18n:     * delete a value in the tree
.. i18n:     * obtain all the values of a selected sheet 

    * add a value in the tree
    * delete a value in the tree
    * obtain all the values of a selected sheet 

.. i18n: Setting Value
.. i18n: -------------

Setting Value
-------------

.. i18n: The ir_set tag allows you to insert new values in the  "Information Repository". This tag must contain several field tags.
.. i18n: field tags

The ir_set tag allows you to insert new values in the  "Information Repository". This tag must contain several field tags.
field tags

.. i18n:     attributes: name and eval 

    attributes: name and eval 

.. i18n: The attributes are those defined by the access methods to the information repository. We must provide him with several attributes: keys, args, name, value, // isobject, replace, meta. optional fields
.. i18n: Example

The attributes are those defined by the access methods to the information repository. We must provide him with several attributes: keys, args, name, value, // isobject, replace, meta. optional fields
Example

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n: 	<ir_set>
.. i18n: 		<field name="keys" eval="[('action','client_print_multi'),('res_model','account.invoice')]"/> 
.. i18n: 		<field name="args" eval="[]"/> 
.. i18n: 		<field name="name">Print Invoices</field> 
.. i18n: 		<field name="value" eval="'ir.actions.report.xml,'+str(l0)"/> 
.. i18n: 		<field name="isobject" eval="True"/> 
.. i18n: 		<field name="replace" eval="False"/> 
.. i18n: 	</ir_set> 

.. code-block:: xml

	<ir_set>
		<field name="keys" eval="[('action','client_print_multi'),('res_model','account.invoice')]"/> 
		<field name="args" eval="[]"/> 
		<field name="name">Print Invoices</field> 
		<field name="value" eval="'ir.actions.report.xml,'+str(l0)"/> 
		<field name="isobject" eval="True"/> 
		<field name="replace" eval="False"/> 
	</ir_set> 

.. i18n: IR Methods
.. i18n: -----------

IR Methods
-----------

.. i18n:     * def ir_set(cr, uid, key, key2, name, models, value, replace=True, isobject=False, meta=None) 
.. i18n: 
.. i18n:     * def ir_get(cr, uid, key, key2, models, meta=False, context={}, res_id_req=False) 
.. i18n: 
.. i18n:     * def ir_del(cr, uid, id): 

    * def ir_set(cr, uid, key, key2, name, models, value, replace=True, isobject=False, meta=None) 

    * def ir_get(cr, uid, key, key2, models, meta=False, context={}, res_id_req=False) 

    * def ir_del(cr, uid, id): 

.. i18n: :Description of the fields:

:Description of the fields:

.. i18n:    1. key:
.. i18n:    2. key2:
.. i18n:    3. name:
.. i18n:    4. models:
.. i18n:    5. value:
.. i18n:    6. isobject:
.. i18n:    7. replace: whether or not the action described should override an existing action or be appended to the list of actions.
.. i18n:    8. meta: 

   1. key:
   2. key2:
   3. name:
   4. models:
   5. value:
   6. isobject:
   7. replace: whether or not the action described should override an existing action or be appended to the list of actions.
   8. meta: 

.. i18n: :Using ir_set and ir_get:

:Using ir_set and ir_get:

.. i18n: ...

...

.. i18n:     res = ir.ir_set(cr, uid, key, key2, name, models, value, replace, isobject, meta) 

    res = ir.ir_set(cr, uid, key, key2, name, models, value, replace, isobject, meta) 

.. i18n: ...

...

.. i18n: ...

...

.. i18n:     if not report.menu_id:

    if not report.menu_id:

.. i18n:         ir.ir_set(cr, uid, 'action', 'client_print_multi', name, [(model, False)], action, False, True) 

        ir.ir_set(cr, uid, 'action', 'client_print_multi', name, [(model, False)], action, False, True) 

.. i18n:     else:

    else:

.. i18n:         ir.ir_set(cr, uid, 'action', 'tree_but_open', 'Menuitem', [('ir.ui.menu', int(m_id))], action, False, True) 

        ir.ir_set(cr, uid, 'action', 'tree_but_open', 'Menuitem', [('ir.ui.menu', int(m_id))], action, False, True) 

.. i18n: ...

...

.. i18n: ...

...

.. i18n:     res = ir.ir_get(cr, uid, [('default', self._name), ('field', False)], [('user_id',str(uid))]) 

    res = ir.ir_get(cr, uid, [('default', self._name), ('field', False)], [('user_id',str(uid))]) 

.. i18n: ...

...

.. i18n:     account_payable = ir.ir_get(cr, uid, [('meta','res.partner'), ('name','account.payable')], opt)[0][2] 

    account_payable = ir.ir_get(cr, uid, [('meta','res.partner'), ('name','account.payable')], opt)[0][2] 

.. i18n: ... 

... 
