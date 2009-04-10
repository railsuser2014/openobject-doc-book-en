
.. i18n: Inheritance in Views 
.. i18n: -------------------- 

Inheritance in Views 
-------------------- 

.. i18n: When you create and inherit objects in some custom or specific modules, it is better to inherit (than to replace) from an existing view to add/modify/delete some fields and preserve the others.

When you create and inherit objects in some custom or specific modules, it is better to inherit (than to replace) from an existing view to add/modify/delete some fields and preserve the others.

.. i18n: :Example:

:Example:

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n: 	<record model="ir.ui.view" id="view_partner_form">
.. i18n: 	    <field name="name">res.partner.form.inherit</field>
.. i18n: 	    <field name="model">res.partner</field>
.. i18n: 	    <field name="inherit_id" ref="base.view_partner_form"/>
.. i18n: 	    <field name="arch" type="xml">
.. i18n: 		 <notebook position="inside">
.. i18n: 		     <page string="Relations">
.. i18n: 		           <field name="relation_ids" colspan="4" nolabel="1"/>
.. i18n: 		     </page>
.. i18n: 		 </notebook>
.. i18n: 	    </field>
.. i18n: 	</record>

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

.. i18n: The inheritance engine will parse the existing view and search for the the root nodes of

The inheritance engine will parse the existing view and search for the the root nodes of

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n: 	<field name="arch" type="xml">

.. code-block:: xml

	<field name="arch" type="xml">

.. i18n: It will append or edit the content of this tag. If this tag has some attributes, it will look for the matching node, including the same attributes (unless position).

It will append or edit the content of this tag. If this tag has some attributes, it will look for the matching node, including the same attributes (unless position).

.. i18n: This will add a page to the notebook of the res.partner.form view in the base module.

This will add a page to the notebook of the res.partner.form view in the base module.

.. i18n: You can use these values in the position attribute:

You can use these values in the position attribute:

.. i18n:     * inside (default): your values will be appended inside this tag
.. i18n:     * after: add the content after this tag
.. i18n:     * before: add the content before this tag
.. i18n:     * replace: replace the content of the tag. 

    * inside (default): your values will be appended inside this tag
    * after: add the content after this tag
    * before: add the content before this tag
    * replace: replace the content of the tag. 

.. i18n: :Second Example:

:Second Example:

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n: 	<record model="ir.ui.view" id="view_partner_form">
.. i18n: 	    <field name="name">res.partner.form.inherit</field>
.. i18n: 	    <field name="model">res.partner</field>
.. i18n: 	    <field name="inherit_id" ref="base.view_partner_form"/>
.. i18n: 	    <field name="arch" type="xml">
.. i18n: 		 <page string="Extra Info" position="replace">
.. i18n: 		     <field name="relation_ids" colspan="4" nolabel="1"/>
.. i18n: 		 </page>
.. i18n: 	    </field>
.. i18n: 	</record>

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

.. i18n: Will replace the content of the Extra Info tab of the notebook by one 'relation_ids' field.

Will replace the content of the Extra Info tab of the notebook by one 'relation_ids' field.

.. i18n: The parent and the inherited views are correctly updated with --update=all argument like any other views.

The parent and the inherited views are correctly updated with --update=all argument like any other views.

.. i18n: To delete a field from a form, an empty element with position="replace" atribute is used. Example:

To delete a field from a form, an empty element with position="replace" atribute is used. Example:

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n: 	<record model="ir.ui.view" id="view_partner_form3">
.. i18n: 	    <field name="name">res.partner.form.inherit</field>
.. i18n: 	    <field name="model">res.partner</field>
.. i18n: 	    <field name="inherit_id" ref="base.view_partner_form"/>
.. i18n: 	    <field name="arch" type="xml">
.. i18n: 		 <field name="lang" position="replace"/>
.. i18n: 	   </field>
.. i18n: 	</record>

.. code-block:: xml

	<record model="ir.ui.view" id="view_partner_form3">
	    <field name="name">res.partner.form.inherit</field>
	    <field name="model">res.partner</field>
	    <field name="inherit_id" ref="base.view_partner_form"/>
	    <field name="arch" type="xml">
		 <field name="lang" position="replace"/>
	   </field>
	</record>

.. i18n: Take into account that only one position="replace" attribute can be used per inherited view so multiple inherited views must be created to make multiple replacements. 

Take into account that only one position="replace" attribute can be used per inherited view so multiple inherited views must be created to make multiple replacements. 
