
.. i18n: Design Elements
.. i18n: ===============

Design Elements
===============

.. i18n: The common structure to all the XML files of Tiny ERP is described in the DataLoadXML "Data Loading Using XML Files" section

The common structure to all the XML files of Tiny ERP is described in the DataLoadXML "Data Loading Using XML Files" section

.. i18n: The files describing the views are also of the form:

The files describing the views are also of the form:

.. i18n: :Example:

:Example:

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:     <?xml version="1.0"?>
.. i18n:     <terp>
.. i18n:        <data>
.. i18n:            [view definitions]
.. i18n:        </data>
.. i18n:     </terp>

.. code-block:: xml

    <?xml version="1.0"?>
    <terp>
       <data>
           [view definitions]
       </data>
    </terp>

.. i18n: The view definitions contain mainly three types of tags:

The view definitions contain mainly three types of tags:

.. i18n:     * **<record>** tags with the attribute model="ir.ui.view", which contain the view definitions themselves
.. i18n:     * **<record>** tags with the attribute model="ir.actions.act_window", which link actions to these views
.. i18n:     * **<menuitem>** tags, which create entries in the menu, and link them with actions

    * **<record>** tags with the attribute model="ir.ui.view", which contain the view definitions themselves
    * **<record>** tags with the attribute model="ir.actions.act_window", which link actions to these views
    * **<menuitem>** tags, which create entries in the menu, and link them with actions

.. i18n: New : You can precise groups for whom the menu is accessible using the groups attribute in menuitem tag.

New : You can precise groups for whom the menu is accessible using the groups attribute in menuitem tag.

.. i18n: New : You can now add shortcut using the shortcut tag.

New : You can now add shortcut using the shortcut tag.

.. i18n: :Example:

:Example:

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:     <shortcut name="Draft Purchase Order (Proposals)" model="purchase.order" logins="demo" menu="m"/>

.. code-block:: xml

    <shortcut name="Draft Purchase Order (Proposals)" model="purchase.order" logins="demo" menu="m"/>

.. i18n: Note that you should add an id attribute on the menuitem which is refered by menu attribute.

Note that you should add an id attribute on the menuitem which is refered by menu attribute.

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:     <record model="ir.ui.view" id="v">
.. i18n:         <field name="name">sale.order.form</field>
.. i18n:         <field name="model">sale.order</field>
.. i18n:         <field name="priority" eval="2"/>
.. i18n:         <field name="arch" type="xml">
.. i18n:         <form string="Sale Order">
.. i18n:             .........
.. i18n:         </form>
.. i18n:         </field>
.. i18n:     </record>

.. code-block:: xml

    <record model="ir.ui.view" id="v">
        <field name="name">sale.order.form</field>
        <field name="model">sale.order</field>
        <field name="priority" eval="2"/>
        <field name="arch" type="xml">
        <form string="Sale Order">
            .........
        </form>
        </field>
    </record>

.. i18n: Default value for the priority field : 16. When not specified the system will use the view with the lower priority.

Default value for the priority field : 16. When not specified the system will use the view with the lower priority.

.. i18n: Grouping Elements
.. i18n: -----------------

Grouping Elements
-----------------

.. i18n: Separator
.. i18n: +++++++++

Separator
+++++++++

.. i18n: Adds a separator line

Adds a separator line

.. i18n: :Example:

:Example:

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:     <separator string="Links" colspan="4"/>

.. code-block:: xml

    <separator string="Links" colspan="4"/>

.. i18n: The string attribute defines its label and the colspan attribute defines his horizontal size (in number of columns).

The string attribute defines its label and the colspan attribute defines his horizontal size (in number of columns).

.. i18n: Notebook
.. i18n: ++++++++

Notebook
++++++++

.. i18n: <notebook>: With notebooks you can distribute the view fields on different tabs (each one defined by a page tag). You can use the tabpos properties to set tab at: up, down, left, right.

<notebook>: With notebooks you can distribute the view fields on different tabs (each one defined by a page tag). You can use the tabpos properties to set tab at: up, down, left, right.

.. i18n: :Example:

:Example:

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:     <notebook colspan="4">....</notebook>

.. code-block:: xml

    <notebook colspan="4">....</notebook>

.. i18n: Group
.. i18n: +++++

Group
+++++

.. i18n: <group>: groups several columns and split the group in as many columns as desired.

<group>: groups several columns and split the group in as many columns as desired.

.. i18n:     * **colspan**: the number of columns to use
.. i18n:     * **rowspan**: the number of rows to use
.. i18n:     * **expand**: if we should expand the group or not
.. i18n:     * **col**: the number of columns to provide (to its children)
.. i18n:     * **string**: (optional) If set, a frame will be drawn around the group of fields, with a label containing the string. Otherwise, the frame will be invisible.

    * **colspan**: the number of columns to use
    * **rowspan**: the number of rows to use
    * **expand**: if we should expand the group or not
    * **col**: the number of columns to provide (to its children)
    * **string**: (optional) If set, a frame will be drawn around the group of fields, with a label containing the string. Otherwise, the frame will be invisible.

.. i18n: :Example:

:Example:

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:     <group col="3" colspan="2">
.. i18n:         <field name="invoiced" select="2"/>
.. i18n:         <button colspan="1" name="make_invoice" states="confirmed" string="Make Invoice"
.. i18n:             type="object"/>
.. i18n:     </group>

.. code-block:: xml

    <group col="3" colspan="2">
        <field name="invoiced" select="2"/>
        <button colspan="1" name="make_invoice" states="confirmed" string="Make Invoice"
            type="object"/>
    </group>

.. i18n: Page
.. i18n: ++++

Page
++++

.. i18n: Defines a new notebook page for the view.

Defines a new notebook page for the view.

.. i18n: :Example:

:Example:

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:     <page string="Order Line"> ... </page>:

.. code-block:: xml

    <page string="Order Line"> ... </page>:

.. i18n: * **string**: defines the name of the page.

* **string**: defines the name of the page.

.. i18n: Data Elements
.. i18n: -------------

Data Elements
-------------

.. i18n: Field
.. i18n: +++++

Field
+++++

.. i18n: :guilabel:`attributes for the "field" tag`

:guilabel:`attributes for the "field" tag`

.. i18n:     * **select="1"**: mark this field as being one of the research criteria for this resource search view.
.. i18n: 
.. i18n:     * **colspan="4"**: the number of columns on which a field must extend.
.. i18n: 
.. i18n:     * **readonly="1"**: set the widget as read only
.. i18n: 
.. i18n:     * **required="1"**: the field is marked as required. If a field is marked as required, a user has to fill it the system won't save the resource if the field is not filled. This attribute supersede the required field value defined in the object.
.. i18n: 
.. i18n:     * **nolabel="1"**: hides the label of the field (but the field is not hidden in the search view).
.. i18n: 
.. i18n:     * **invisible="True"**: hides both the label and the field.
.. i18n: 
.. i18n:     * **password="True"**: replace field entry by asterisk, "*".
.. i18n: 
.. i18n:     * **string=""**: change the field label. Note that this label is also used in the search view: see select attribute above).
.. i18n: 
.. i18n:     * **domain**: can restrict the domain.
.. i18n:           + Example: domain="[('partner_id','=',partner_id)]"
.. i18n: 
.. i18n:     * **widget**: can change the widget.
.. i18n:           + Example: widget="one2many_list"
.. i18n:                 - one2one_list
.. i18n:                 - one2many_list
.. i18n:                 - many2one_list
.. i18n:                 - many2many
.. i18n:                 - url
.. i18n:                 - email
.. i18n:                 - image
.. i18n:                 - float_time
.. i18n:                 - reference
.. i18n: 
.. i18n:     * **on_change**: define a function that is called when the content of the field changes.
.. i18n:           + Example: on_change="onchange_partner(type,partner_id)"
.. i18n:           + See ViewsSpecialProperties for details
.. i18n: 
.. i18n:     * **attrs**: Permits to define attributes of a field depends on other fields of the same window. (It can be use on     page, group, button and notebook tag also)
.. i18n:           + Format: "{'attribute':[('field_name','operator','value'),('field_name','operator','value')],'attribute2':[('field_name','operator','value'),]}"
.. i18n:           + where attribute will be readonly, invisible, required
.. i18n:           + Default value: {}.
.. i18n:           + Example: (in product.product)

    * **select="1"**: mark this field as being one of the research criteria for this resource search view.

    * **colspan="4"**: the number of columns on which a field must extend.

    * **readonly="1"**: set the widget as read only

    * **required="1"**: the field is marked as required. If a field is marked as required, a user has to fill it the system won't save the resource if the field is not filled. This attribute supersede the required field value defined in the object.

    * **nolabel="1"**: hides the label of the field (but the field is not hidden in the search view).

    * **invisible="True"**: hides both the label and the field.

    * **password="True"**: replace field entry by asterisk, "*".

    * **string=""**: change the field label. Note that this label is also used in the search view: see select attribute above).

    * **domain**: can restrict the domain.
          + Example: domain="[('partner_id','=',partner_id)]"

    * **widget**: can change the widget.
          + Example: widget="one2many_list"
                - one2one_list
                - one2many_list
                - many2one_list
                - many2many
                - url
                - email
                - image
                - float_time
                - reference

    * **on_change**: define a function that is called when the content of the field changes.
          + Example: on_change="onchange_partner(type,partner_id)"
          + See ViewsSpecialProperties for details

    * **attrs**: Permits to define attributes of a field depends on other fields of the same window. (It can be use on     page, group, button and notebook tag also)
          + Format: "{'attribute':[('field_name','operator','value'),('field_name','operator','value')],'attribute2':[('field_name','operator','value'),]}"
          + where attribute will be readonly, invisible, required
          + Default value: {}.
          + Example: (in product.product)

.. i18n:         .. code-block:: xml
.. i18n: 
.. i18n:             <field digits="(14, 3)" name="volume" attrs="{'readonly':[('type','=','service')]}"/>
.. i18n: 
.. i18n:     * **eval**: evaluate the attribute content as if it was Python code (see :ref:`below <eval-attribute-link>` for example)

        .. code-block:: xml

            <field digits="(14, 3)" name="volume" attrs="{'readonly':[('type','=','service')]}"/>

    * **eval**: evaluate the attribute content as if it was Python code (see :ref:`below <eval-attribute-link>` for example)

.. i18n: Example

Example

.. i18n: Here's the source code of the view of a sale order object. This is the same object as the object shown on the screen shots of the presentation.

Here's the source code of the view of a sale order object. This is the same object as the object shown on the screen shots of the presentation.

.. i18n: :Example:

:Example:

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:     <?xml version="1.0"?>
.. i18n:     <terp>
.. i18n:         <data>
.. i18n:         <record id="view_partner_form" model="ir.ui.view">
.. i18n:                 <field name="name">res.partner.form</field>
.. i18n:                 <field name="model">res.partner</field>
.. i18n:                 <field name="type">form</field>
.. i18n:                 <field name="arch" type="xml">
.. i18n:                 <form string="Partners">
.. i18n:                     <group colspan="4" col="6">
.. i18n:                         <field name="name" select="1"/>
.. i18n:                         <field name="ref" select="1"/>
.. i18n:                         <field name="customer" select="1"/>
.. i18n:                         <field domain="[('domain', '=', 'partner')]" name="title"/>
.. i18n:                         <field name="lang" select="2"/>
.. i18n:                         <field name="supplier" select="2"/>
.. i18n:                     </group>
.. i18n:                     <notebook colspan="4">
.. i18n:                         <page string="General">
.. i18n:                             <field colspan="4" mode="form,tree" name="address"
.. i18n:                              nolabel="1" select="1">
.. i18n:                                 <form string="Partner Contacts">
.. i18n:                                     <field name="name" select="2"/>
.. i18n:                                     <field domain="[('domain', '=', 'contact')]" name="title"/>
.. i18n:                                     <field name="function"/>
.. i18n:                                     <field name="type" select="2"/>
.. i18n:                                     <field name="street" select="2"/>
.. i18n:                                     <field name="street2"/>
.. i18n:                                     <newline/>
.. i18n:                                     <field name="zip" select="2"/>
.. i18n:                                     <field name="city" select="2"/>
.. i18n:                                     <newline/>
.. i18n:                                     <field completion="1" name="country_id" select="2"/>
.. i18n:                                     <field name="state_id" select="2"/>
.. i18n:                                     <newline/>
.. i18n:                                     <field name="phone"/>
.. i18n:                                     <field name="fax"/>
.. i18n:                                     <newline/>
.. i18n:                                     <field name="mobile"/>
.. i18n:                                     <field name="email" select="2" widget="email"/>
.. i18n:                                 </form>
.. i18n:                                 <tree string="Partner Contacts">
.. i18n:                                     <field name="name"/>
.. i18n:                                     <field name="zip"/>
.. i18n:                                     <field name="city"/>
.. i18n:                                     <field name="country_id"/>
.. i18n:                                     <field name="phone"/>
.. i18n:                                     <field name="email"/>
.. i18n:                                 </tree>
.. i18n:                             </field>
.. i18n:                             <separator colspan="4" string="Categories"/>
.. i18n:                             <field colspan="4" name="category_id" nolabel="1" select="2"/>
.. i18n:                         </page>
.. i18n:                         <page string="Sales &amp; Purchases">
.. i18n:                             <separator string="General Information" colspan="4"/>
.. i18n:                             <field name="user_id" select="2"/>
.. i18n:                             <field name="active" select="2"/>
.. i18n:                             <field name="website" widget="url"/>
.. i18n:                             <field name="date" select="2"/>
.. i18n:                             <field name="parent_id"/>
.. i18n:                             <newline/>
.. i18n:                         </page>
.. i18n:                         <page string="History">
.. i18n:                             <field colspan="4" name="events" nolabel="1" widget="one2many_list"/>
.. i18n:                         </page>
.. i18n:                         <page string="Notes">
.. i18n:                             <field colspan="4" name="comment" nolabel="1"/>
.. i18n:                         </page>
.. i18n:                     </notebook>
.. i18n:                 </form>
.. i18n:                 </field>
.. i18n:             </record>
.. i18n:         <menuitem
.. i18n:                 action="action_partner_form"
.. i18n:                 id="menu_partner_form"
.. i18n:                 parent="base.menu_base_partner"
.. i18n:                 sequence="2"/>
.. i18n:         </data>
.. i18n:      </terp>

.. code-block:: xml

    <?xml version="1.0"?>
    <terp>
        <data>
        <record id="view_partner_form" model="ir.ui.view">
                <field name="name">res.partner.form</field>
                <field name="model">res.partner</field>
                <field name="type">form</field>
                <field name="arch" type="xml">
                <form string="Partners">
                    <group colspan="4" col="6">
                        <field name="name" select="1"/>
                        <field name="ref" select="1"/>
                        <field name="customer" select="1"/>
                        <field domain="[('domain', '=', 'partner')]" name="title"/>
                        <field name="lang" select="2"/>
                        <field name="supplier" select="2"/>
                    </group>
                    <notebook colspan="4">
                        <page string="General">
                            <field colspan="4" mode="form,tree" name="address"
                             nolabel="1" select="1">
                                <form string="Partner Contacts">
                                    <field name="name" select="2"/>
                                    <field domain="[('domain', '=', 'contact')]" name="title"/>
                                    <field name="function"/>
                                    <field name="type" select="2"/>
                                    <field name="street" select="2"/>
                                    <field name="street2"/>
                                    <newline/>
                                    <field name="zip" select="2"/>
                                    <field name="city" select="2"/>
                                    <newline/>
                                    <field completion="1" name="country_id" select="2"/>
                                    <field name="state_id" select="2"/>
                                    <newline/>
                                    <field name="phone"/>
                                    <field name="fax"/>
                                    <newline/>
                                    <field name="mobile"/>
                                    <field name="email" select="2" widget="email"/>
                                </form>
                                <tree string="Partner Contacts">
                                    <field name="name"/>
                                    <field name="zip"/>
                                    <field name="city"/>
                                    <field name="country_id"/>
                                    <field name="phone"/>
                                    <field name="email"/>
                                </tree>
                            </field>
                            <separator colspan="4" string="Categories"/>
                            <field colspan="4" name="category_id" nolabel="1" select="2"/>
                        </page>
                        <page string="Sales &amp; Purchases">
                            <separator string="General Information" colspan="4"/>
                            <field name="user_id" select="2"/>
                            <field name="active" select="2"/>
                            <field name="website" widget="url"/>
                            <field name="date" select="2"/>
                            <field name="parent_id"/>
                            <newline/>
                        </page>
                        <page string="History">
                            <field colspan="4" name="events" nolabel="1" widget="one2many_list"/>
                        </page>
                        <page string="Notes">
                            <field colspan="4" name="comment" nolabel="1"/>
                        </page>
                    </notebook>
                </form>
                </field>
            </record>
        <menuitem
                action="action_partner_form"
                id="menu_partner_form"
                parent="base.menu_base_partner"
                sequence="2"/>
        </data>
     </terp>

.. i18n: .. _eval-attribute-link:
.. i18n: 
.. i18n: The eval attribute
.. i18n: """"""""""""""""""

.. _eval-attribute-link:

The eval attribute
""""""""""""""""""

.. i18n: The **eval** attribute evaluate its content as if it was Python code. This
.. i18n: allows you to define values that are not strings.

The **eval** attribute evaluate its content as if it was Python code. This
allows you to define values that are not strings.

.. i18n: Normally, content inside *<field>* tags are always evaluated as strings.

Normally, content inside *<field>* tags are always evaluated as strings.

.. i18n: .. describe:: Example 1:

.. describe:: Example 1:

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:     <field name="value">2.3</field>

.. code-block:: xml

    <field name="value">2.3</field>

.. i18n: This will evaluate to the string ``'2.3'`` and not the float ``2.3``

This will evaluate to the string ``'2.3'`` and not the float ``2.3``

.. i18n: .. describe:: Example 2:

.. describe:: Example 2:

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:     <field name="value">False</field>

.. code-block:: xml

    <field name="value">False</field>

.. i18n: This will evaluate to the string ``'False'`` and not the boolean ``False``

This will evaluate to the string ``'False'`` and not the boolean ``False``

.. i18n: If you want to evaluate the value to a float, a boolean or another type, except string, you need to use the **eval** attribute:

If you want to evaluate the value to a float, a boolean or another type, except string, you need to use the **eval** attribute:

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:     <field name="value" eval="2.3" />
.. i18n:     <field name="value" eval="False" />

.. code-block:: xml

    <field name="value" eval="2.3" />
    <field name="value" eval="False" />

.. i18n: Button
.. i18n: ++++++

Button
++++++

.. i18n: <button/>: add a button using the string attribute as label. When clicked, it can trigger methods on the object, workflow transitions or actions (reports, wizards, ...).

<button/>: add a button using the string attribute as label. When clicked, it can trigger methods on the object, workflow transitions or actions (reports, wizards, ...).

.. i18n:     * string: define the button's label
.. i18n:     * confirm: the message for the confirmation window, if needed. Eg: confirm="Are you sure?"
.. i18n:     * name: the name of the function to call when the button is pressed. In the case it's an object function, it must take 4 arguments: cr, uid, ids,
.. i18n:           + cr is a database cursor
.. i18n:           + uid is the userID of the user who clicked the button
.. i18n:           + ids is the record ID list
.. i18n:           + \**args is a tuple of additional arguments

    * string: define the button's label
    * confirm: the message for the confirmation window, if needed. Eg: confirm="Are you sure?"
    * name: the name of the function to call when the button is pressed. In the case it's an object function, it must take 4 arguments: cr, uid, ids,
          + cr is a database cursor
          + uid is the userID of the user who clicked the button
          + ids is the record ID list
          + \**args is a tuple of additional arguments

.. i18n:           .. **

          .. **

.. i18n:     * states: a comma-separated list of states (from the state field or from the workflow) in which the button must appear. If the states attribute is not given, the button is always visible.
.. i18n:     * type: this attribute can have 3 values
.. i18n:           + "workflow" (value by default): the function to call is a function of workflow
.. i18n:           + "object": the function to call is a method of the object
.. i18n:           + "action": call an action instead of a function

    * states: a comma-separated list of states (from the state field or from the workflow) in which the button must appear. If the states attribute is not given, the button is always visible.
    * type: this attribute can have 3 values
          + "workflow" (value by default): the function to call is a function of workflow
          + "object": the function to call is a method of the object
          + "action": call an action instead of a function

.. i18n: :Example:

:Example:

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:     <button name="order_confirm" states="draft" string="Confirm Order" icon="gtk-execute"/>

.. code-block:: xml

    <button name="order_confirm" states="draft" string="Confirm Order" icon="gtk-execute"/>

.. i18n: Label
.. i18n: +++++

Label
+++++

.. i18n: Adds a simple label using the string attribute as caption.

Adds a simple label using the string attribute as caption.

.. i18n: :Example:

:Example:

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:     <label string="Test"/>

.. code-block:: xml

    <label string="Test"/>

.. i18n: New Line
.. i18n: ++++++++

New Line
++++++++

.. i18n: Force a return to the line even if all the columns of the view are not filled in.

Force a return to the line even if all the columns of the view are not filled in.

.. i18n: :Example:

:Example:

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:     <newline/>

.. code-block:: xml

    <newline/>
