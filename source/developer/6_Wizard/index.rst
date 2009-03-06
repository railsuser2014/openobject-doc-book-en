===============================
Creating Wizard - (The Process)
===============================

Introduction
============
Wizards describe interaction sequences between the client and the server.

Here is, as an example, a typical process for a wizard:

   1. A window is sent to the client (a form to be completed)
   2. The client sends back the data from the fields which were filled in
   3. The server gets the result, usually execute a function and possibly sends another window/form to the client 

.. image:: images/Wizard.png

Here is a screenshot of the wizard used to reconcile transactions (when you click on the gear icon in an account chart):

.. image:: images/Wizard_screenshot.png 

Wizards - Principles
====================
A wizard is a succession of steps. A step is composed of several actions;

#. send a form to the client and some buttons
#. get the form result and the button pressed from the client
#. execute some actions
#. send a new action to the client (form, print, ...) 

To define a wizard, you have to create a class inheriting from **wizard.interface** and instantiate it. Each wizard must have a unique name, which can be chosen arbitrarily except for the fact it has to start with the module name (for example: account.move.line.reconcile). The wizard must define a dictionary named **states** which defines all its steps.

Here is an example of such a class:

.. code-block:: python

	class wiz_reconcile(wizard.interface):
	      states = {
		   'init': {
		        'actions': [_trans_rec_get],
		        'result': {'type': 'form', 
		                   'arch': _transaction_form, 
		                   'fields': _transaction_fields,  
		                   'state':[('reconcile','Reconcile'),('end','Cancel')]}
		  },
		   'reconcile': {
		        'actions': [_trans_rec_reconcile],
		        'result': {'type': 'state', 'state':'end'}
		  }
	     }
	wiz_reconcile('account.move.line.reconcile');

The 'states' dictionary define all the states of the wizard. In this example; **init** and **reconcile**. There is another state which is named end which is implicit.

A wizard always starts in the **init** state and ends in the **end** state.

A state define two things:

	#. a list of actions
	#. a result 

The list of actions
-------------------
Each step/state of a wizard defines a list of actions which are executed when the wizard enters the state. This list can be empty.

The function (actions) must have the following signatures:

.. code-block:: python

	def _trans_rec_get(self, uid, data, res_get=False):

Where:

    * **self** is the pointer to the wizard object
    * **uid** is the user ID of the user which is executing the wizard
    * **data** is a dictionary containing the following data:
           * **ids**: the list of ids of resources selected when the user executed the wizard
           * **id**: the id highlighted when the user executed the wizard
           * **form**: a dictionary containing all the values the user completed in the preceding forms. If you change values in this dictionary, the following forms will be pre-completed. 

The result

Here are some result examples:

Result: next step

.. code-block:: python

	'result': {'type': 'state', 
	           'state':'end'}

Indicate that the wizard has to continue to the next state: 'end'. If this is the 'end' state, the wizard stops.

Result: new dialog for the client

.. code-block:: python

	'result': {'type': 'form', 
	           'arch': _form, 
	           'fields': _fields, 
	           'state':[('reconcile','Reconcile'),('end','Cancel')]}

The type=form indicate that this step is a dialog to the client. The dialog is composed of:

#. a form : with fields description and a form description
#. some buttons : on wich the user press after completing the form 

The form description (arch) is like in the views objects. Here is an example of form:

.. code-block:: xml

	_form = """<?xml version="1.0"?>
		<form title="Reconciliation">
		  <separator string="Reconciliation transactions" colspan="4"/>
		  <field name="trans_nbr"/>
		  <newline/>
		  <field name="credit"/>
		  <field name="debit"/>
		  <separator string="Write-Off" colspan="4"/>
		  <field name="writeoff"/>
		  <newline/>
		  <field name="writeoff_acc_id" colspan="3"/>
		</form>
		"""

The fields description is similar to the fields described in the python ORM objects. Example:

.. code-block:: python

	_transaction_fields = {
	      'trans_nbr': {'string':'# of Transaction', 'type':'integer', 'readonly':True},
	      'credit': {'string':'Credit amount', 'type':'float', 'readonly':True},
	      'debit': {'string':'Debit amount', 'type':'float', 'readonly':True},
	      'writeoff': {'string':'Write-Off amount', 'type':'float', 'readonly':True},
	      'writeoff_acc_id': {'string':'Write-Off account', 
                                   'type':'many2one', 
                                   'relation':'account.account'
                                 },
	}

Each step/state of a wizard can have several buttons. Those are located on the bottom right of the dialog box. The list of buttons for each step of the wizard is declared in the state key of its result dictionary.

For example:

.. code-block:: python

	'state':[('end', 'Cancel', 'gtk-cancel'), ('reconcile', 'Reconcile', '', True)]

#. the next step name (determine which state will be next)
#. the button string (to display for the client)
#. the gtk stock item without the stock prefix (since 4.2)
#. a boolean, if true the button is set as the default action (since 4.2) 

Here is a screenshot of this form:

.. image:: images/Wizard_screenshot1.png

Result: call a method to determine which state is next

.. code-block:: python

	def _check_refund(self, cr, uid, data, context):
	    ...
	    return datas['form']['refund_id'] and 'wait_invoice' or 'end'
	 
	    ...
	 
	    'result': {'type':'choice', 'next_state':_check_refund}

Result: print a report

.. code-block:: python

	def _get_invoice_id(self, uid, datas):
	      ...
	      return {'ids': [...]}
	 
	      ...
	 
	      'actions': [_get_invoice_id],
	      'result': {'type':'print', 
		         'report':'account.invoice', 
		         'get_id_from_action': True, 
		         'state':'check_refund'}

Result: client run an action

.. code-block:: python

	def _makeInvoices(self, cr, uid, data, context):
	    ...
	    return {
			'domain': "[('id','in', ["+','.join(map(str,newinv))+"])]",
			'name': 'Invoices',
			'view_type': 'form',
			'view_mode': 'tree,form',
			'res_model': 'account.invoice',
			'view_id': False,
			'context': "{'type':'out_refund'}",
			'type': 'ir.actions.act_window'
		}
	 
		...
	 
		'result': {'type': 'action', 
		'action': _makeInvoices, 
		'state': 'end'}

The result of the function must be an all the fields of an ir.actions.* Here it is an ir.action.act_window, so the client will open an new tab for the objects account.invoice For more information about the fields used click here.

It is recommended to use the result of a read on the ir.actions object like this:

.. code-block:: python

	def _account_chart_open_window(self, cr, uid, data, context):
		mod_obj = pooler.get_pool(cr.dbname).get('ir.model.data')
		act_obj = pooler.get_pool(cr.dbname).get('ir.actions.act_window')
	 
		result = mod_obj._get_id(cr, uid, 'account', 'action_account_tree')
		id = mod_obj.read(cr, uid, [result], ['res_id'])[0]['res_id']
		result = act_obj.read(cr, uid, [id])[0]
		result['context'] = str({'fiscalyear': data['form']['fiscalyear']})
		return result
	 
		...
	 
		'result': {'type': 'action', 
		           'action': _account_chart_open_window, 
		           'state':'end'}

Specification
=============

Form
----

.. code-block:: xml


	_form = '''<?xml version="1.0"?>
	<form string="Your String">
	    <field name="Field 1"/>
	    <newline/>
	    <field name="Field 2"/>
	</form>'''

Fields
------

Standard
+++++++++

.. code-block:: python

	Field type: char, integer, boolean, float, date, datetime

	_fields = {
	      'str_field': {'string':'product name', 'type':'char', 'readonly':True},
	}

* **string**: Field label (required)
* **type**: (required)
* **readonly**: (optional) 

Relational
++++++++++

.. code-block:: python

	Field type: one2one,many2one,one2many,many2many

	_fields = {
	    'field_id': {'string':'Write-Off account', 'type':'many2one', 'relation':'account.account'}
	}

* **string**: Field label (required)
* **type**: (required)
* **relation**: name of the relation object 



Add A New Wizard
================

To create a new wizard, you must:

    * create the wizard definition in a .py file
          * wizards are usually defined in the wizard subdirectory of their module as in server/bin/addons/module_name/wizard/your_wizard_name.py 
    * add your wizard to the list of import statements in the __init__.py file of your module's wizard subdirectory.
    * declare your wizard in the database 

The declaration is needed to map the wizard with a key of the client; when to launch which client. To declare a new wizard, you need to add it to the module_name_wizard.xml file, which contains all the wizard declarations for the module. If that file does not exist, you need to create it first.

Here is an example of the account_wizard.xml file;

.. code-block:: python

	<?xml version="1.0"?>
	<terp>
	    <data>
		<delete model="ir.actions.wizard" search="[('wiz_name','like','account.')]" />
		<wizard string="Reconcile Transactions" model="account.move.line" 
                        name="account.move.line.reconcile" />
		<wizard string="Verify Transac steptions" model="account.move.line" 
                        name="account.move.line.check" keyword="tree_but_action" /> 
		<wizard string="Verify Transactions" model="account.move.line"  
                        name="account.move.line.check" />
		<wizard string="Print Journal" model="account.account" 
                        name="account.journal" />
		<wizard string="Split Invoice" model="account.invoice" 
                        name="account.invoice.split" />
		<wizard string="Refund Invoice" model="account.invoice" 
                        name="account.invoice.refund" />
	    </data>
	</terp>

Attributes for the wizard tag:

    * **id** (optional):
    * **string**: The string which will be displayed if there are several wizards for one resthe user will be presented a list with wizards names).
    * **model**: The name of the **model** where the data needed by the wizard is.
    * **name**: The name of the wizard. It is used internally and should be unique.
    * **replace** (optional): Whether or not the wizard should override **all** existing wizards for this model. Default value: False.
    * **menu** (optional): Whether or not (True|False) to link the wizard with the 'gears' button (i.e. show the button or not). Default value: True.
    * **keyword** (optional): Bind the wizard to another action (print icon, gear icon, ...). Possible values for the keyword attribute are:
          * **client_print_multi**: the print icon in a form
          * **client_action_multi**: the 'gears' icon in a form
          * **tree_but_action**: the 'gears' icon in a tree view (with the shortcuts on the left)
          * **tree_but_open**: the double click on a branch of a tree (with the shortcuts on the left). For example, this is used, to bind wizards in the menu. 

**__terp__.py**

If the wizard you created is the first one of its module, you probably had to create the modulename_wizard.xml file yourself. In that case, it should be added to the update_xml field of the __terp__.py file of the module.

Here is, for example, the **__terp__.py** file for the account module.

.. code-block:: python

	{
	    "name": Open ERP Accounting",
	    "version": "0.1",
	    "depends": ["base"],
	    "init_xml": ["account_workflow.xml", "account_data.xml"],
	    "update_xml": ["account_view.xml","account_report.xml", "account_wizard.xml"],
	}



osv_memory Wizard System
========================
To develop osv_memory wizard, just create a normal object, But instead of inheriting from osv.osv, Inherit from osv.osv_memory. Methods of "wizard" are in object and if the wizard is complex, You can define workflow on object. osv_memory object is managed in memory instead of storing in postgresql.

That's all, nothing more than just changing the inherit.

So what makes them looks like 'old' wizards?

    * In the action that opens the object, you can put 

.. code-block:: python

	<field name="target">new</field>

It means the object will open in a new window instead of the current one.

    * On a button, you can use <button special="cancel" .../> to close the window. 

Example : In project.py file.

.. code-block:: python

	class config_compute_remaining(osv.osv_memory):
	    _name='config.compute.remaining'
	    def _get_remaining(self,cr, uid, ctx):
		if 'active_id' in ctx:
		    return self.pool.get('project.task').browse(cr,uid,ctx['active_id']).remaining_hours
		return False
	    _columns = {
		'remaining_hours' : fields.float('Remaining Hours', digits=(16,2),),
		    }
	    _defaults = {
		'remaining_hours': _get_remaining
		}
	    def compute_hours(self, cr, uid, ids, context=None):
		if 'active_id' in context:
		    remaining_hrs=self.browse(cr,uid,ids)[0].remaining_hours
		    self.pool.get('project.task').write(cr,uid,context['active_id'],
                                                         {'remaining_hours' : remaining_hrs})
		return {
		        'type': 'ir.actions.act_window_close',
		 }
	config_compute_remaining()

* View is same as normal view (Note buttons). 

Example :

.. code-block:: xml

	<record id="view_config_compute_remaining" model="ir.ui.view">
		    <field name="name">Compute Remaining Hours </field>
		    <field name="model">config.compute.remaining</field>
		    <field name="type">form</field>
		    <field name="arch" type="xml">
		        <form string="Remaining Hours">
		            <separator colspan="4" string="Change Remaining Hours"/>
		            <newline/>
		            <field name="remaining_hours" widget="float_time"/>
		            <group col="4" colspan="4">
		                <button icon="gtk-cancel" special="cancel" string="Cancel"/>
		                <button icon="gtk-ok" name="compute_hours" string="Update" type="object"/>
		            </group>
		        </form>
		    </field>
		</record>

* Action is also same as normal action (don't forget to add target attribute) 

Example :

.. code-block:: xml

	<record id="action_config_compute_remaining" model="ir.actions.act_window">
	    <field name="name">Compute Remaining Hours</field>
	    <field name="type">ir.actions.act_window</field>
	    <field name="res_model">config.compute.remaining</field>
	    <field name="view_type">form</field>
	    <field name="view_mode">form</field>
	    <field name="target">new</field>
	</record>
