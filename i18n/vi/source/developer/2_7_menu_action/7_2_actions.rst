
.. i18n: Actions
.. i18n: =======

Actions
=======

.. i18n: Introduction
.. i18n: ------------

Introduction
------------

.. i18n: The actions define the behavior of the system in response to the actions of the users ; login of a new user, double-click on an invoice, click on the action button, ...

The actions define the behavior of the system in response to the actions of the users ; login of a new user, double-click on an invoice, click on the action button, ...

.. i18n: There are different types of simple actions:

There are different types of simple actions:

.. i18n:     * Window: Opening of a new window
.. i18n:     * Report: The printing of a report
.. i18n:           o Custom Report: The personalized reports
.. i18n:           o RML Report: The XSL:RML reports
.. i18n:     * Wizard: The beginning of a Wizard
.. i18n:     * Execute: The execution of a method on the server side
.. i18n:     * Group: Gather some actions in one group

    * Window: Opening of a new window
    * Report: The printing of a report
          o Custom Report: The personalized reports
          o RML Report: The XSL:RML reports
    * Wizard: The beginning of a Wizard
    * Execute: The execution of a method on the server side
    * Group: Gather some actions in one group

.. i18n: The actions are used for the following events;

The actions are used for the following events;

.. i18n:     * User connection,
.. i18n:     * The user double-clicks on the menu,
.. i18n:     * The user clicks on the icon 'print' or 'action'.

    * User connection,
    * The user double-clicks on the menu,
    * The user clicks on the icon 'print' or 'action'.

.. i18n: Example of events
.. i18n: -----------------

Example of events
-----------------

.. i18n: In Open ERP, all the actions are described and not configured. Two examples:

In Open ERP, all the actions are described and not configured. Two examples:

.. i18n:     * Opening of a window when double-clicking in the menu
.. i18n:     * User connection

    * Opening of a window when double-clicking in the menu
    * User connection

.. i18n: Opening of the menu
.. i18n: +++++++++++++++++++

Opening of the menu
+++++++++++++++++++

.. i18n: When the user open the option of the menu "Operations > Partners > Partners Contact", the next steps are done to give the user information on the action to undertake.

When the user open the option of the menu "Operations > Partners > Partners Contact", the next steps are done to give the user information on the action to undertake.

.. i18n:    1. Search the action in the IR.
.. i18n:    2. Execution of the action
.. i18n:          1. If the action is the type Opening the Window; it indicates to the user that a new window must be opened for a selected object and it gives you the view (form or list) and the filed to use (only the pro-forma invoice).
.. i18n:          2. The user asks the object and receives information necessary to trace a form; the fields description and the XML view.

   1. Search the action in the IR.
   2. Execution of the action
         1. If the action is the type Opening the Window; it indicates to the user that a new window must be opened for a selected object and it gives you the view (form or list) and the filed to use (only the pro-forma invoice).
         2. The user asks the object and receives information necessary to trace a form; the fields description and the XML view.

.. i18n: User connection
.. i18n: +++++++++++++++

User connection
+++++++++++++++

.. i18n: When a new user is connected to the server, the client must search the action to use for the first screen of this user. Generally, this action is: open the menu in the 'Operations' section.

When a new user is connected to the server, the client must search the action to use for the first screen of this user. Generally, this action is: open the menu in the 'Operations' section.

.. i18n: The steps are:

The steps are:

.. i18n:    1. Reading of a user file to obtain ACTION_ID
.. i18n:    2. Reading of the action and execution of this one

   1. Reading of a user file to obtain ACTION_ID
   2. Reading of the action and execution of this one

.. i18n: The fields
.. i18n: ++++++++++

The fields
++++++++++

.. i18n: **Action Name**
.. i18n: 	The action name
.. i18n: **Action Type**
.. i18n: 	Always 'ir.actions.act_window'
.. i18n: **View Ref**
.. i18n:     	The view used for showing the object
.. i18n: **Model**
.. i18n: 	The model of the object to post
.. i18n: **Type of View**
.. i18n:     	The type of view (Tree/Form)
.. i18n: **Domain Value**
.. i18n:     	The domain that decreases the visible data with this view

**Action Name**
	The action name
**Action Type**
	Always 'ir.actions.act_window'
**View Ref**
    	The view used for showing the object
**Model**
	The model of the object to post
**Type of View**
    	The type of view (Tree/Form)
**Domain Value**
    	The domain that decreases the visible data with this view

.. i18n: The view
.. i18n: --------
.. i18n: The view describes how the edition form or the data tree/list appear on screen. The views can be of 'Form' or 'Tree' type, according to whether they represent a form for the edition or a list/tree for global data viewing.

The view
--------
The view describes how the edition form or the data tree/list appear on screen. The views can be of 'Form' or 'Tree' type, according to whether they represent a form for the edition or a list/tree for global data viewing.

.. i18n: A form can be called by an action opening in 'Tree' mode. The form view is generally opened from the list mode (like if the user pushes on 'switch view').

A form can be called by an action opening in 'Tree' mode. The form view is generally opened from the list mode (like if the user pushes on 'switch view').

.. i18n: The domain
.. i18n: ----------

The domain
----------

.. i18n: This parameter allows you to regulate which resources are visible in a selected view.(restriction)

This parameter allows you to regulate which resources are visible in a selected view.(restriction)

.. i18n: For example, in the invoice case, you can define an action that opens a view that shows only invoices not paid.

For example, in the invoice case, you can define an action that opens a view that shows only invoices not paid.

.. i18n: The domains are written in python; list of tuples. The tuples have three elements;

The domains are written in python; list of tuples. The tuples have three elements;

.. i18n:     * the field on which the test must be done
.. i18n:     * the operator used for the test (<, >, =, like)
.. i18n:     * the tested value

    * the field on which the test must be done
    * the operator used for the test (<, >, =, like)
    * the tested value

.. i18n: For example, if you want to obtain only 'Draft' invoice, use the following domain; [('state','=','draft')]

For example, if you want to obtain only 'Draft' invoice, use the following domain; [('state','=','draft')]

.. i18n: In the case of a simple view, the domain define the resources which are the roots of the tree. The other resources, even if they are not from a part of the domain will be posted if the user develop the branches of the tree.

In the case of a simple view, the domain define the resources which are the roots of the tree. The other resources, even if they are not from a part of the domain will be posted if the user develop the branches of the tree.

.. i18n: Window Action
.. i18n: -------------

Window Action
-------------

.. i18n: Actions are explained in more detail in section "Administration Modules - Actions". Here's the template of an action XML record :
.. i18n: ::
.. i18n: 
.. i18n: 	<record model="ir.actions.act_window" id="action_id_1">
.. i18n: 	    <field name="name">action.name</field>
.. i18n: 	    <field name="view_id" ref="view_id_1"/>
.. i18n: 	    <field name="domain">["list of 3-tuples (max 250 characters)"]</field>
.. i18n: 	    <field name="context">{"context dictionary (max 250 characters)"}</field>
.. i18n: 	    <field name="res_model">Open.object</field>
.. i18n: 	    <field name="view_type">form|tree</field>
.. i18n: 	    <field name="view_mode">form,tree|tree,form|form|tree</field>
.. i18n: 	    <field name="usage">menu</field>
.. i18n: 	    <field name="target">new</field>
.. i18n: 	</record>

Actions are explained in more detail in section "Administration Modules - Actions". Here's the template of an action XML record :
::

	<record model="ir.actions.act_window" id="action_id_1">
	    <field name="name">action.name</field>
	    <field name="view_id" ref="view_id_1"/>
	    <field name="domain">["list of 3-tuples (max 250 characters)"]</field>
	    <field name="context">{"context dictionary (max 250 characters)"}</field>
	    <field name="res_model">Open.object</field>
	    <field name="view_type">form|tree</field>
	    <field name="view_mode">form,tree|tree,form|form|tree</field>
	    <field name="usage">menu</field>
	    <field name="target">new</field>
	</record>

.. i18n: **Where**

**Where**

.. i18n:     * **id** is the identifier of the action in the table "ir.actions.act_window". It must be unique.
.. i18n:     * **name** is the name of the action (mandatory).
.. i18n:     * **view_id** is the name of the view to display when the action is activated. If this field is not defined, the view of a kind (list or form) associated to the object res_model with the highest priority field is used (if two views have the same priority, the first defined view of a kind is used).
.. i18n:     * **domain** is a list of constraints used to refine the results of a selection, and hence to get less records displayed in the view. Constraints of the list are linked together with an AND clause : a record of the table will be displayed in the view only if all the constraints are satisfied.
.. i18n:     * **context** is the context dictionary which will be visible in the view that will be opened when the action is activated. Context dictionaries are declared with the same syntax as Python dictionaries in the XML file. For more information about context dictionaries, see section " The context Dictionary".
.. i18n:     * **res_model** is the name of the object on which the action operates.
.. i18n:     * **view_type** is set to form when the action must open a new form view, and is set to tree when the action must open a new tree view.
.. i18n:     * **view_mode** is only considered if view_type is form, and ignored otherwise. The four possibilities are :
.. i18n:           - **form,tree** : the view is first displayed as a form, the list view can be displayed by clicking the "alternate view button" ;
.. i18n:           - **tree,form** : the view is first displayed as a list, the form view can be displayed by clicking the "alternate view button" ;
.. i18n:           - **form** : the view is displayed as a form and there is no way to switch to list view ;
.. i18n:           - **tree** : the view is displayed as a list and there is no way to switch to form view.

    * **id** is the identifier of the action in the table "ir.actions.act_window". It must be unique.
    * **name** is the name of the action (mandatory).
    * **view_id** is the name of the view to display when the action is activated. If this field is not defined, the view of a kind (list or form) associated to the object res_model with the highest priority field is used (if two views have the same priority, the first defined view of a kind is used).
    * **domain** is a list of constraints used to refine the results of a selection, and hence to get less records displayed in the view. Constraints of the list are linked together with an AND clause : a record of the table will be displayed in the view only if all the constraints are satisfied.
    * **context** is the context dictionary which will be visible in the view that will be opened when the action is activated. Context dictionaries are declared with the same syntax as Python dictionaries in the XML file. For more information about context dictionaries, see section " The context Dictionary".
    * **res_model** is the name of the object on which the action operates.
    * **view_type** is set to form when the action must open a new form view, and is set to tree when the action must open a new tree view.
    * **view_mode** is only considered if view_type is form, and ignored otherwise. The four possibilities are :
          - **form,tree** : the view is first displayed as a form, the list view can be displayed by clicking the "alternate view button" ;
          - **tree,form** : the view is first displayed as a list, the form view can be displayed by clicking the "alternate view button" ;
          - **form** : the view is displayed as a form and there is no way to switch to list view ;
          - **tree** : the view is displayed as a list and there is no way to switch to form view.

.. i18n: (version 5 introduced **graph** and **calendar** views)

(version 5 introduced **graph** and **calendar** views)

.. i18n:     * **usage** is used [+ ***TODO*** +]
.. i18n:     * **target** the view will open in new window like wizard.

    * **usage** is used [+ ***TODO*** +]
    * **target** the view will open in new window like wizard.

.. i18n: They indicate at the user that he has to open a new window in a new 'tab'.

They indicate at the user that he has to open a new window in a new 'tab'.

.. i18n: Administration > Custom > Low Level > Base > Action > Window Actions

Administration > Custom > Low Level > Base > Action > Window Actions

.. i18n: .. figure::  images/module_base_action_window.png
.. i18n:    :scale: 85
.. i18n:    :align: center

.. figure::  images/module_base_action_window.png
   :scale: 85
   :align: center

.. i18n: Examples of actions
.. i18n: +++++++++++++++++++

Examples of actions
+++++++++++++++++++

.. i18n: This action is declared in server/bin/addons/project/project_view.xml.
.. i18n: ::
.. i18n: 
.. i18n:     <record model="ir.actions.act_window" id="open_view_my_project">
.. i18n:         <field name="name">project.project</field>
.. i18n:         <field name="res_model">project.project</field>
.. i18n:         <field name="view_type">tree</field>
.. i18n:         <field name="domain">[('parent_id','=',False), ('manager', '=', uid)]</field>
.. i18n:         <field name="view_id" ref="view_my_project" />
.. i18n:     </record>

This action is declared in server/bin/addons/project/project_view.xml.
::

    <record model="ir.actions.act_window" id="open_view_my_project">
        <field name="name">project.project</field>
        <field name="res_model">project.project</field>
        <field name="view_type">tree</field>
        <field name="domain">[('parent_id','=',False), ('manager', '=', uid)]</field>
        <field name="view_id" ref="view_my_project" />
    </record>

.. i18n: This action is declared in server/bin/addons/stock/stock_view.xml.
.. i18n: ::
.. i18n: 
.. i18n:     <record model="ir.actions.act_window" id="action_picking_form">
.. i18n:         <field name="name">stock.picking</field>
.. i18n:         <field name="res_model">stock.picking</field>
.. i18n:         <field name="type">ir.actions.act_window</field>
.. i18n:         <field name="view_type">form</field>
.. i18n:         <field name="view_id" ref="view_picking_form"/>
.. i18n:         <field name="context">{'contact_display': 'partner'}</field>
.. i18n:     </record>

This action is declared in server/bin/addons/stock/stock_view.xml.
::

    <record model="ir.actions.act_window" id="action_picking_form">
        <field name="name">stock.picking</field>
        <field name="res_model">stock.picking</field>
        <field name="type">ir.actions.act_window</field>
        <field name="view_type">form</field>
        <field name="view_id" ref="view_picking_form"/>
        <field name="context">{'contact_display': 'partner'}</field>
    </record>

.. i18n: Url Action
.. i18n: -----------

Url Action
-----------

.. i18n: Wizard Action
.. i18n: -------------

Wizard Action
-------------

.. i18n: Here's an example of a .XML file that declares a wizard.
.. i18n: ::
.. i18n: 
.. i18n: 	<?xml version="1.0"?>
.. i18n: 	<terp>
.. i18n: 	    <data>
.. i18n: 		 <wizard string="Employee Info"
.. i18n: 		         model="hr.employee"
.. i18n: 		         name="employee.info.wizard"
.. i18n: 		         id="wizard_employee_info"/>
.. i18n: 	    </data>
.. i18n: 	</terp>

Here's an example of a .XML file that declares a wizard.
::

	<?xml version="1.0"?>
	<terp>
	    <data>
		 <wizard string="Employee Info"
		         model="hr.employee"
		         name="employee.info.wizard"
		         id="wizard_employee_info"/>
	    </data>
	</terp>

.. i18n: A wizard is declared using a wizard tag. See "Add A New Wizard" for more information about wizard XML.

A wizard is declared using a wizard tag. See "Add A New Wizard" for more information about wizard XML.

.. i18n: also you can add wizard in menu using following xml entry
.. i18n: ::
.. i18n: 
.. i18n:     <?xml version="1.0"?>
.. i18n:     <terp>
.. i18n:          <data>
.. i18n:          <wizard string="Employee Info"
.. i18n:                  model="hr.employee"
.. i18n:                  name="employee.info.wizard"
.. i18n:                  id="wizard_employee_info"/>
.. i18n:          <menuitem
.. i18n:                  name="Human Resource/Employee Info"
.. i18n:                  action="wizard_employee_info"
.. i18n:                  type="wizard"
.. i18n:                  id="menu_wizard_employee_info"/>
.. i18n:          </data>
.. i18n:     </terp>

also you can add wizard in menu using following xml entry
::

    <?xml version="1.0"?>
    <terp>
         <data>
         <wizard string="Employee Info"
                 model="hr.employee"
                 name="employee.info.wizard"
                 id="wizard_employee_info"/>
         <menuitem
                 name="Human Resource/Employee Info"
                 action="wizard_employee_info"
                 type="wizard"
                 id="menu_wizard_employee_info"/>
         </data>
    </terp>

.. i18n: Report Action
.. i18n: -------------

Report Action
-------------

.. i18n: Report declaration
.. i18n: ++++++++++++++++++

Report declaration
++++++++++++++++++

.. i18n: Reports in Open ERP are explained in chapter "Reports Reporting". Here's an example of a XML file that declares a RML report :
.. i18n: ::
.. i18n: 
.. i18n:     <?xml version="1.0"?>
.. i18n:     <terp>
.. i18n:         <data>
.. i18n:         <report id="sale_category_print"
.. i18n:                 string="Sales Orders By Categories"
.. i18n:                 model="sale.order"
.. i18n:                 name="sale_category.print"
.. i18n:                 rml="sale_category/report/sale_category_report.rml"
.. i18n:                 menu="True"
.. i18n:                 auto="False"/>
.. i18n:          </data>
.. i18n:     </terp>

Reports in Open ERP are explained in chapter "Reports Reporting". Here's an example of a XML file that declares a RML report :
::

    <?xml version="1.0"?>
    <terp>
        <data>
        <report id="sale_category_print"
                string="Sales Orders By Categories"
                model="sale.order"
                name="sale_category.print"
                rml="sale_category/report/sale_category_report.rml"
                menu="True"
                auto="False"/>
         </data>
    </terp>

.. i18n: A report is declared using a **report tag** inside a "data" block. The different arguments of a report tag are :

A report is declared using a **report tag** inside a "data" block. The different arguments of a report tag are :

.. i18n:     * **id** : an identifier which must be unique.
.. i18n:     * **string** : the text of the menu that calls the report (if any, see below).
.. i18n:     * **model** : the Open ERP object on which the report will be rendered.
.. i18n:     * **rml** : the .RML report model. Important Note : Path is relative to addons/ directory.
.. i18n:     * **menu** : whether the report will be able to be called directly via the client or not. Setting menu to False is useful in case of reports called by wizards.
.. i18n:     * **auto** : determines if the .RML file must be parsed using the default parser or not. Using a custom parser allows you to define additional functions to your report.

    * **id** : an identifier which must be unique.
    * **string** : the text of the menu that calls the report (if any, see below).
    * **model** : the Open ERP object on which the report will be rendered.
    * **rml** : the .RML report model. Important Note : Path is relative to addons/ directory.
    * **menu** : whether the report will be able to be called directly via the client or not. Setting menu to False is useful in case of reports called by wizards.
    * **auto** : determines if the .RML file must be parsed using the default parser or not. Using a custom parser allows you to define additional functions to your report.
