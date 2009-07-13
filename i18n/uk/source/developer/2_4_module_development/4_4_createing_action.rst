
.. i18n: Creating Action
.. i18n: ===============
.. i18n:   
.. i18n: Linking events to action
.. i18n: -------------------------

Creating Action
===============
  
Linking events to action
-------------------------

.. i18n: The available type of events are:

The available type of events are:

.. i18n:     * **client_print_multi** (print from a list or form)
.. i18n:     * **client_action_multi** (action from a list or form)
.. i18n:     * **tree_but_open** (double click on the item of a tree, like the menu)
.. i18n:     * **tree_but_action** (action on the items of a tree) 

    * **client_print_multi** (print from a list or form)
    * **client_action_multi** (action from a list or form)
    * **tree_but_open** (double click on the item of a tree, like the menu)
    * **tree_but_action** (action on the items of a tree) 

.. i18n: To map an events to an action:

To map an events to an action:

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:     <record model="ir.values" id="ir_open_journal_period">
.. i18n:         <field name="key2">tree_but_open</field>
.. i18n:         <field name="model">account.journal.period</field>
.. i18n:         <field name="name">Open Journal</field>
.. i18n:         <field name="value" eval="'ir.actions.wizard,%d'%action_move_journal_line_form_select"/>
.. i18n:         <field name="object" eval="True"/>
.. i18n:     </record>

.. code-block:: xml

    <record model="ir.values" id="ir_open_journal_period">
        <field name="key2">tree_but_open</field>
        <field name="model">account.journal.period</field>
        <field name="name">Open Journal</field>
        <field name="value" eval="'ir.actions.wizard,%d'%action_move_journal_line_form_select"/>
        <field name="object" eval="True"/>
    </record>

.. i18n: If you double click on a journal/period (object: account.journal.period), this will open the selected wizard. (id="action_move_journal_line_form_select").

If you double click on a journal/period (object: account.journal.period), this will open the selected wizard. (id="action_move_journal_line_form_select").

.. i18n: You can use a res_id field to allow this action only if the user click on a specific object.

You can use a res_id field to allow this action only if the user click on a specific object.

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:     <record model="ir.values" id="ir_open_journal_period">
.. i18n:         <field name="key2">tree_but_open</field>
.. i18n:         <field name="model">account.journal.period</field>
.. i18n:         <field name="name">Open Journal</field>
.. i18n:         <field name="value" eval="'ir.actions.wizard,%d'%action_move_journal_line_form_select"/>
.. i18n:         <field name="res_id" eval="3"/>
.. i18n:         <field name="object" eval="True"/>
.. i18n:     </record>

.. code-block:: xml

    <record model="ir.values" id="ir_open_journal_period">
        <field name="key2">tree_but_open</field>
        <field name="model">account.journal.period</field>
        <field name="name">Open Journal</field>
        <field name="value" eval="'ir.actions.wizard,%d'%action_move_journal_line_form_select"/>
        <field name="res_id" eval="3"/>
        <field name="object" eval="True"/>
    </record>

.. i18n: The action will be triggered if the user clicks on the account.journal.period n°3.

The action will be triggered if the user clicks on the account.journal.period n°3.

.. i18n: When you declare wizard, report or menus, the ir.values creation is automatically made with these tags:

When you declare wizard, report or menus, the ir.values creation is automatically made with these tags:

.. i18n:   * <wizard... />
.. i18n:   * <menuitem... />
.. i18n:   * <report... /> 

  * <wizard... />
  * <menuitem... />
  * <report... /> 

.. i18n: So you usually do not need to add the mapping by yourself. 

So you usually do not need to add the mapping by yourself. 
