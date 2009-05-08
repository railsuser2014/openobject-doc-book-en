
Design Elements
===============

The common structure to all the XML files of Tiny ERP is described in the DataLoadXML "Data Loading Using XML Files" section

The files describing the views are also of the form:

:Example:

.. code-block:: xml

    <?xml version="1.0"?>
    <terp>
       <data>
           [view definitions]
       </data>
    </terp>

The view definitions contain mainly three types of tags:

    * **<record>** tags with the attribute model="ir.ui.view", which contain the view definitions themselves
    * **<record>** tags with the attribute model="ir.actions.act_window", which link actions to these views
    * **<menuitem>** tags, which create entries in the menu, and link them with actions

New : You can precise groups for whom the menu is accessible using the groups attribute in menuitem tag.

New : You can now add shortcut using the shortcut tag.

:Example:

.. code-block:: xml

    <shortcut name="Draft Purchase Order (Proposals)" model="purchase.order" logins="demo" menu="m"/>

Note that you should add an id attribute on the menuitem which is refered by menu attribute.

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

Default value for the priority field : 16. When not specified the system will use the view with the lower priority.

Grouping Elements
-----------------

Separator
+++++++++

Adds a separator line

:Example:

.. code-block:: xml

    <separator string="Links" colspan="4"/>

The string attribute defines its label and the colspan attribute defines his horizontal size (in number of columns).

Notebook
++++++++

<notebook>: With notebooks you can distribute the view fields on different tabs (each one defined by a page tag). You can use the tabpos properties to set tab at: up, down, left, right.

:Example:

.. code-block:: xml

    <notebook colspan="4">....</notebook>

Group
+++++

<group>: groups several columns and split the group in as many columns as desired.

    * **colspan**: the number of columns to use
    * **rowspan**: the number of rows to use
    * **expand**: if we should expand the group or not
    * **col**: the number of columns to provide (to its children)
    * **string**: (optional) If set, a frame will be drawn around the group of fields, with a label containing the string. Otherwise, the frame will be invisible.

:Example:

.. code-block:: xml

    <group col="3" colspan="2">
        <field name="invoiced" select="2"/>
        <button colspan="1" name="make_invoice" states="confirmed" string="Make Invoice"
            type="object"/>
    </group>

Page
++++

Defines a new notebook page for the view.

:Example:

.. code-block:: xml

    <page string="Order Line"> ... </page>:

* **string**: defines the name of the page.

Data Elements
-------------

Field
+++++

:guilabel:`attributes for the "field" tag`

    * **select="1"**: mark this field as being one of the research criteria for this resource search view.

    * **colspan="4"**: the number of columns on which a field must extend.

    * **readonly="1"**: set the widget as read only

    * **required="1"**: the field is marked as required. If a field is marked as required, a user has to fill it the system won't save the resource if the field is not filled. This attribute supersede the required field value defined in the object.

    * **nolabel="1"**: hides the label of the field (but the field is not hidden in the search view).

    * **invisible="True"**: hides both the label and the field.

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

        .. code-block:: xml

            <field digits="(14, 3)" name="volume" attrs="{'readonly':[('type','=','service')]}"/>

    * **eval**: evaluate the attribute content as if it was Python code (see :ref:`below <eval-attribute-link>` for example)

Example

Here's the source code of the view of a sale order object. This is the same object as the object shown on the screen shots of the presentation.

:Example:

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

.. _eval-attribute-link:

The eval attribute
""""""""""""""""""

The **eval** attribute evaluate its content as if it was Python code. This
allows you to define values that are not strings.

Normally, content inside *<field>* tags are always evaluated as strings.

.. describe:: Example 1:

.. code-block:: xml

    <field name="value">2.3</field>

This will evaluate to the string ``'2.3'`` and not the float ``2.3``

.. describe:: Example 2:

.. code-block:: xml

    <field name="value">False</field>

This will evaluate to the string ``'False'`` and not the boolean ``False``

If you want to evaluate the value to a float, a boolean or another type, except string, you need to use the **eval** attribute:

.. code-block:: xml

    <field name="value" eval="2.3" />
    <field name="value" eval="False" />

Button
++++++

<button/>: add a button using the string attribute as label. When clicked, it can trigger methods on the object, workflow transitions or actions (reports, wizards, ...).

    * string: define the button's label
    * confirm: the message for the confirmation window, if needed. Eg: confirm="Are you sure?"
    * name: the name of the function to call when the button is pressed. In the case it's an object function, it must take 4 arguments: cr, uid, ids,
          + cr is a database cursor
          + uid is the userID of the user who clicked the button
          + ids is the record ID list
          + \**args is a tuple of additional arguments
          .. **

    * states: a comma-separated list of states (from the state field or from the workflow) in which the button must appear. If the states attribute is not given, the button is always visible.
    * type: this attribute can have 3 values
          + "workflow" (value by default): the function to call is a function of workflow
          + "object": the function to call is a method of the object
          + "action": call an action instead of a function

:Example:

.. code-block:: xml

    <button name="order_confirm" states="draft" string="Confirm Order" icon="gtk-execute"/>

Label
+++++

Adds a simple label using the string attribute as caption.

:Example:

.. code-block:: xml

    <label string="Test"/>

New Line
++++++++

Force a return to the line even if all the columns of the view are not filled in.

:Example:

.. code-block:: xml

    <newline/>

