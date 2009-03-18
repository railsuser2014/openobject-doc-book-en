Inheritance in Views 
-------------------- 

When you create and inherit objects in some custom or specific modules, it is better to inherit (than to replace) from an existing view to add/modify/delete some fields and preserve the others.

:Example:

.. code-block:: xml

	<record model="ir.ui.view" id="view_partner_form">
	    <field name="name">res.partner.form.inherit</field>
	    <field name="model">res.partner</field>
	    <field name="inherit_id" ref="base.view_partner_form"/>
	    <field name="arch" type="xml">
		 <notebook position="inside">
		     <page string="Relations">
		           <field name="relation_ids" colspan="4" nolabel="1"/>
		     </page>
		 </notebook>
	    </field>
	</record>


The inheritance engine will parse the existing view and search for the the root nodes of

.. code-block:: xml

	<field name="arch" type="xml">

It will append or edit the content of this tag. If this tag has some attributes, it will look for the matching node, including the same attributes (unless position).

This will add a page to the notebook of the res.partner.form view in the base module.

You can use these values in the position attribute:

    * inside (default): your values will be appended inside this tag
    * after: add the content after this tag
    * before: add the content before this tag
    * replace: replace the content of the tag. 

:Second Example:

.. code-block:: xml

	<record model="ir.ui.view" id="view_partner_form">
	    <field name="name">res.partner.form.inherit</field>
	    <field name="model">res.partner</field>
	    <field name="inherit_id" ref="base.view_partner_form"/>
	    <field name="arch" type="xml">
		 <page string="Extra Info" position="replace">
		     <field name="relation_ids" colspan="4" nolabel="1"/>
		 </page>
	    </field>
	</record>

Will replace the content of the Extra Info tab of the notebook by one 'relation_ids' field.

The parent and the inherited views are correctly updated with --update=all argument like any other views.

To delete a field from a form, an empty element with position="replace" atribute is used. Example:

.. code-block:: xml

	<record model="ir.ui.view" id="view_partner_form3">
	    <field name="name">res.partner.form.inherit</field>
	    <field name="model">res.partner</field>
	    <field name="inherit_id" ref="base.view_partner_form"/>
	    <field name="arch" type="xml">
		 <field name="lang" position="replace"/>
	   </field>
	</record>

Take into account that only one position="replace" attribute can be used per inherited view so multiple inherited views must be created to make multiple replacements. 
