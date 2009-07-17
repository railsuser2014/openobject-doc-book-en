
.. i18n: Graph views
.. i18n: --------------

Graph views
--------------

.. i18n: A graph is a new mode of view for all views of type form. If, for example, a sale order line must be visible as list or as graph, define it like this in the action that open this sale order line. Do not set the view mode as "tree,form,graph" or "form,graph" - it must be "graph,tree" to show the graph first or "tree,graph" to show the list first. (This view mode is extra to your "form,tree" view and should have a seperate menu item):

A graph is a new mode of view for all views of type form. If, for example, a sale order line must be visible as list or as graph, define it like this in the action that open this sale order line. Do not set the view mode as "tree,form,graph" or "form,graph" - it must be "graph,tree" to show the graph first or "tree,graph" to show the list first. (This view mode is extra to your "form,tree" view and should have a seperate menu item):

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n: 	 <field name="view_type">form</field>
.. i18n: 	 <field name="view_mode">tree,graph</field>

.. code-block:: xml

	 <field name="view_type">form</field>
	 <field name="view_mode">tree,graph</field>

.. i18n: Then, the user will be able to switch from one view to the other. Unlike forms and trees, Tiny ERP is not able to automatically create a view on demand for the graph type. So, you must define a view for this graph:

Then, the user will be able to switch from one view to the other. Unlike forms and trees, Tiny ERP is not able to automatically create a view on demand for the graph type. So, you must define a view for this graph:

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n: 	<record model="ir.ui.view" id="view_order_line_graph">
.. i18n: 	   <field name="name">sale.order.line.graph</field>
.. i18n: 	   <field name="model">sale.order.line</field>
.. i18n: 	   <field name="type">graph</field>
.. i18n: 	   <field name="arch" type="xml">
.. i18n: 		 <graph string="Sales Order Lines">
.. i18n: 		      <field name="product_id" group="True"/>
.. i18n: 		      <field name="price_unit" operator="*"/>
.. i18n: 		</graph>
.. i18n: 	    </field>
.. i18n: 	</record>

.. code-block:: xml

	<record model="ir.ui.view" id="view_order_line_graph">
	   <field name="name">sale.order.line.graph</field>
	   <field name="model">sale.order.line</field>
	   <field name="type">graph</field>
	   <field name="arch" type="xml">
		 <graph string="Sales Order Lines">
		      <field name="product_id" group="True"/>
		      <field name="price_unit" operator="*"/>
		</graph>
	    </field>
	</record>

.. i18n: The graph view

The graph view

.. i18n: A view of type graph is just a list of fields for the graph.

A view of type graph is just a list of fields for the graph.

.. i18n: Graph tag
.. i18n: ++++++++++

Graph tag
++++++++++

.. i18n: The default type of the graph is a pie chart - to change it to a barchart change **<graph string="Sales Order Lines">** to **<graph string="Sales Order Lines" type="bar">** You also may change the orientation.

The default type of the graph is a pie chart - to change it to a barchart change **<graph string="Sales Order Lines">** to **<graph string="Sales Order Lines" type="bar">** You also may change the orientation.

.. i18n: :Example : 

:Example : 

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n: 	<graph string="Sales Order Lines" orientation="horizontal" type="bar">

.. code-block:: xml

	<graph string="Sales Order Lines" orientation="horizontal" type="bar">

.. i18n: Field tag
.. i18n: +++++++++

Field tag
+++++++++

.. i18n: The first field is the X axis. The second one is the Y axis and the optionnal third one is the Z axis for 3 dimensional graphs. You can apply a few attributes to each field/axis:

The first field is the X axis. The second one is the Y axis and the optionnal third one is the Z axis for 3 dimensional graphs. You can apply a few attributes to each field/axis:

.. i18n:     * **group**: if set to true, the client will group all item of the same value for this field. For each other field, it will apply an operator
.. i18n:     * **operator**: the operator to apply is another field is grouped. By default it's '+'. Allowed values are:
.. i18n:           + +: addition
.. i18n:           + \*: multiply
.. i18n:           + \**: exponent
.. i18n:           + min: minimum of the list
.. i18n:           + max: maximum of the list 

    * **group**: if set to true, the client will group all item of the same value for this field. For each other field, it will apply an operator
    * **operator**: the operator to apply is another field is grouped. By default it's '+'. Allowed values are:
          + +: addition
          + \*: multiply
          + \**: exponent
          + min: minimum of the list
          + max: maximum of the list 

.. i18n: :Defining real statistics on objects:

:Defining real statistics on objects:

.. i18n: The easiest method to compute real statistics on objects is:

The easiest method to compute real statistics on objects is:

.. i18n:    1. Define a statistic object wich is a postgresql view
.. i18n:    2. Create a tree view and a graph view on this object 

   1. Define a statistic object wich is a postgresql view
   2. Create a tree view and a graph view on this object 

.. i18n: You can get en example in all modules of the form: report\_.... Example: report_crm. 

You can get en example in all modules of the form: report\_.... Example: report_crm. 
