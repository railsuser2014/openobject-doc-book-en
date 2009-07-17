
.. i18n: Server Action
.. i18n: =============

Server Action
=============

.. i18n: Introduction
.. i18n: ------------
.. i18n: Server action is an new feature to the OpenERP available since the version 5.0 beta, This is the
.. i18n: interesting features for the customizer, to full fill the customers requirements, This features enables
.. i18n: to provides the quick and easy configuration some process which is day to day requirements. Like
.. i18n: send email on confirmation of the sale order, or confirmation of the Invoice, log the operation of
.. i18n: the invoice (confirm, cancel, etc..). or need to develope some system which runs wizard / report on
.. i18n: the confirmation of the sales, purchase, or invoice. So Server action is the only one answer to solve
.. i18n: all this kind of problems without doing any development, just a few configuration and the system is
.. i18n: ready to answer few of above questions.

Introduction
------------
Server action is an new feature to the OpenERP available since the version 5.0 beta, This is the
interesting features for the customizer, to full fill the customers requirements, This features enables
to provides the quick and easy configuration some process which is day to day requirements. Like
send email on confirmation of the sale order, or confirmation of the Invoice, log the operation of
the invoice (confirm, cancel, etc..). or need to develope some system which runs wizard / report on
the confirmation of the sales, purchase, or invoice. So Server action is the only one answer to solve
all this kind of problems without doing any development, just a few configuration and the system is
ready to answer few of above questions.

.. i18n: Following are the list of action types which are supplied under the Server Action.

Following are the list of action types which are supplied under the Server Action.

.. i18n:        * Client Action
.. i18n:        * Trigger
.. i18n:        * Email
.. i18n:        * SMS
.. i18n:        * Create Object
.. i18n:        * Write Object
.. i18n:        * Multi Action

       * Client Action
       * Trigger
       * Email
       * SMS
       * Create Object
       * Write Object
       * Multi Action

.. i18n: Each type of action have the special features and different configuration parameters. We will see
.. i18n: one by one all type of action how to configure and list of parameters that affect the system

Each type of action have the special features and different configuration parameters. We will see
one by one all type of action how to configure and list of parameters that affect the system

.. i18n: Client Action
.. i18n: -------------

Client Action
-------------

.. i18n: This action executes at client side, this is a good idea to run the wizard or report at client side.
.. i18n: Using this type of action we can make the system like ERP will print the invoice after confirmation
.. i18n: of the Invoice. Like it will run the payment wizard after confirmation of the invoice. Technically we
.. i18n: can run all client action which execute at client side. We can execute ir.actions.report.custom,
.. i18n: ir.actions.report.xml, ir.actions.act_window, ir.actions.wizard, or ir.actions.url. Here is an example
.. i18n: to show how we can configuration Client action to print the invoice after confirmation of the
.. i18n: invoice.

This action executes at client side, this is a good idea to run the wizard or report at client side.
Using this type of action we can make the system like ERP will print the invoice after confirmation
of the Invoice. Like it will run the payment wizard after confirmation of the invoice. Technically we
can run all client action which execute at client side. We can execute ir.actions.report.custom,
ir.actions.report.xml, ir.actions.act_window, ir.actions.wizard, or ir.actions.url. Here is an example
to show how we can configuration Client action to print the invoice after confirmation of the
invoice.

.. i18n: .. image:: images/client_action.png

.. image:: images/client_action.png

.. i18n: This is an good and seems easy to configure the action.

This is an good and seems easy to configure the action.

.. i18n: Important fields are

Important fields are

.. i18n: :Object: Select the object on which we want to implement the Server Action when work flow will execute on this object
.. i18n: :Client Action: Select the client action that is to execute at client side. Any of the following types.

:Object: Select the object on which we want to implement the Server Action when work flow will execute on this object
:Client Action: Select the client action that is to execute at client side. Any of the following types.

.. i18n: * ir.actions.report.custom
.. i18n: * ir.actions.report.xml
.. i18n: * ir.actions.act_window
.. i18n: * ir.actions.wizard
.. i18n: * ir.actions.url

* ir.actions.report.custom
* ir.actions.report.xml
* ir.actions.act_window
* ir.actions.wizard
* ir.actions.url

.. i18n: Trigger
.. i18n: -------

Trigger
-------

.. i18n: Trigger is an really excellent when we want to deal with the work flow of the other object which
.. i18n: working the work flow of the first object. For example we want to configure the system like when
.. i18n: we confirm the purchase order and create the invoice that newly created invoice should confirm it
.. i18n: self automatically by the server action.

Trigger is an really excellent when we want to deal with the work flow of the other object which
working the work flow of the first object. For example we want to configure the system like when
we confirm the purchase order and create the invoice that newly created invoice should confirm it
self automatically by the server action.

.. i18n: .. image:: images/trigger_action.png

.. image:: images/trigger_action.png

.. i18n: This is the easy configuration for the trigger to have the system where the created invoice will
.. i18n: confirm it self.

This is the easy configuration for the trigger to have the system where the created invoice will
confirm it self.

.. i18n: Important fields are

Important fields are

.. i18n: :Object: Select the object on which we want to implement the Server Action when work flow will execute on this object

:Object: Select the object on which we want to implement the Server Action when work flow will execute on this object

.. i18n: :Work-flow on: Here we select invoice, need to select the model on which the automatic workflow will be called by the action system

:Work-flow on: Here we select invoice, need to select the model on which the automatic workflow will be called by the action system

.. i18n: :Trigger On: We need to provide the id of the newly record, here in this case, Purchase order store the id of the Invoice after creating of the invoice in invoice_id field.

:Trigger On: We need to provide the id of the newly record, here in this case, Purchase order store the id of the Invoice after creating of the invoice in invoice_id field.

.. i18n: :Trigger Name: This is the signal name which we want to generate on the newly created object.

:Trigger Name: This is the signal name which we want to generate on the newly created object.

.. i18n: Email Action
.. i18n: ------------

Email Action
------------

.. i18n: This is the common requirement for all business process, like send the confirmation by the email
.. i18n: when sales order, purchase order, invoice, payment, shipping of goods will takes place. For that we
.. i18n: need only few things to configure and tiny will send the email very quickly and in easy way. Even
.. i18n: not need to setting up the your own email server, you can use your exciting email server and
.. i18n: account, of you not have your email server you can use from the free email account by Gmail,
.. i18n: Yahoo !, etc..

This is the common requirement for all business process, like send the confirmation by the email
when sales order, purchase order, invoice, payment, shipping of goods will takes place. For that we
need only few things to configure and tiny will send the email very quickly and in easy way. Even
not need to setting up the your own email server, you can use your exciting email server and
account, of you not have your email server you can use from the free email account by Gmail,
Yahoo !, etc..

.. i18n: *Server Configuration*

*Server Configuration*

.. i18n: supply the following parameters when we run OpenERP Server.

supply the following parameters when we run OpenERP Server.

.. i18n: ::
.. i18n: 
.. i18n:   --email-from=gajjarmantavya@yahoo.co.in user email address
.. i18n:   --smtp=smtp.mail.yahoo.co.in smtp server name or ip
.. i18n:   --smtp-port=587 smtp port
.. i18n:   --smtp-user=gajjarmantavya user name usually same as the email address name without domain name
.. i18n:   --smtp-password=************* password to the user account
.. i18n:   --smtp-ssl=False use in case if the server required ssl for sending email

::

  --email-from=gajjarmantavya@yahoo.co.in user email address
  --smtp=smtp.mail.yahoo.co.in smtp server name or ip
  --smtp-port=587 smtp port
  --smtp-user=gajjarmantavya user name usually same as the email address name without domain name
  --smtp-password=************* password to the user account
  --smtp-ssl=False use in case if the server required ssl for sending email

.. i18n: .. **

.. **

.. i18n: Email Action Configuration

Email Action Configuration

.. i18n: .. image:: images/email_action.png

.. image:: images/email_action.png

.. i18n: Important Fields are:

Important Fields are:

.. i18n: :Object: Select the object on which we want to implement the Server Action when work flow will execute on this object
.. i18n: :Contact: We need to select the fields from which action will select the email address to whom we would like to send the email, system will display all the fields related to the current object selected in the Object field
.. i18n: :Message: You can provide the message template with the fields that relate to the current object. And it will be merged when it is going to send the email. This is the same language than the rml which is used to design the report here we can use the [[ ]] + html tags to design in the html format Working with You can select the any fields from the current object, like here we select the [[ ]] invoice in the object.

:Object: Select the object on which we want to implement the Server Action when work flow will execute on this object
:Contact: We need to select the fields from which action will select the email address to whom we would like to send the email, system will display all the fields related to the current object selected in the Object field
:Message: You can provide the message template with the fields that relate to the current object. And it will be merged when it is going to send the email. This is the same language than the rml which is used to design the report here we can use the [[ ]] + html tags to design in the html format Working with You can select the any fields from the current object, like here we select the [[ ]] invoice in the object.

.. i18n: For example to get the partner name we can use [[ object.partner_id.name ]]like the same, object refers to the current object and we can access any fields which exist in the model.

For example to get the partner name we can use [[ object.partner_id.name ]]like the same, object refers to the current object and we can access any fields which exist in the model.

.. i18n: After confirmation the invoice we get the confirmation email from the action.

After confirmation the invoice we get the confirmation email from the action.

.. i18n: .. image:: images/email_confirm.png

.. image:: images/email_confirm.png

.. i18n: Create Object
.. i18n: -------------

Create Object
-------------

.. i18n: This is an interesting feature for the tiny partners those who want to track the transaction in the
.. i18n: OpenERP, like currently in the ERP you can get the Event history on the Partners which logs the
.. i18n: only the sales order events. But if we want to start logging the invoice like the same we can easily
.. i18n: do like that using the Create object Actions.

This is an interesting feature for the tiny partners those who want to track the transaction in the
OpenERP, like currently in the ERP you can get the Event history on the Partners which logs the
only the sales order events. But if we want to start logging the invoice like the same we can easily
do like that using the Create object Actions.

.. i18n: .. image:: images/create_object.png

.. image:: images/create_object.png

.. i18n: Create Object action have the easy but tricky configuration, for the movement you have to
.. i18n: remember the fields name or check it out from the code it self, in future we will develop the
.. i18n: expression builder inside OpenERP so you can build the complex expression.

Create Object action have the easy but tricky configuration, for the movement you have to
remember the fields name or check it out from the code it self, in future we will develop the
expression builder inside OpenERP so you can build the complex expression.

.. i18n: Important fields are

Important fields are

.. i18n: :Object: Select the object on which we want to implement the Server Action when work flow will execute on this object
.. i18n: :Model: This is the target model where the new object is to be created, if its empty it refers to the current object and allow to select the fields from the same, but its advisable to provide the model in all case if different or if the same.
.. i18n: :Fields Mapping: Need to provide the 3 values

:Object: Select the object on which we want to implement the Server Action when work flow will execute on this object
:Model: This is the target model where the new object is to be created, if its empty it refers to the current object and allow to select the fields from the same, but its advisable to provide the model in all case if different or if the same.
:Fields Mapping: Need to provide the 3 values

.. i18n: 1. Field: any of the fields from the target model
.. i18n: 2. type of the value you can give either value or expression
.. i18n: 3. provide the value or expression the expression again start with the 'object' keyword and its refers to the current object which selected in to the Object field.

1. Field: any of the fields from the target model
2. type of the value you can give either value or expression
3. provide the value or expression the expression again start with the 'object' keyword and its refers to the current object which selected in to the Object field.

.. i18n: *You must select the all required fields from the object*

*You must select the all required fields from the object*

.. i18n: :Record Id: After creating the new record where the id of the new record if going to store. So in future we can refer the same for the other operations.

:Record Id: After creating the new record where the id of the new record if going to store. So in future we can refer the same for the other operations.

.. i18n: Write Object
.. i18n: ------------

Write Object
------------

.. i18n: The same configuration as defined for the Create Object, here we take an example that it will write the
.. i18n: 'Additional Information' on the same object

The same configuration as defined for the Create Object, here we take an example that it will write the
'Additional Information' on the same object

.. i18n: .. image:: images/write_object.png

.. image:: images/write_object.png

.. i18n: Important Fields are

Important Fields are

.. i18n:   **same as the Create Object**

  **same as the Create Object**

.. i18n: Multi Action
.. i18n: ------------

Multi Action
------------

.. i18n: This is the most interesting action, which allows to execute the multiple server action on the same
.. i18n: business operations. Like if you want to print and send the email on confirmation of the invoice. We
.. i18n: need to create the 3 Server Actions for that.

This is the most interesting action, which allows to execute the multiple server action on the same
business operations. Like if you want to print and send the email on confirmation of the invoice. We
need to create the 3 Server Actions for that.

.. i18n:   * Print Invoice
.. i18n:   * Invoice Confirmation Email !!
.. i18n:   * Multi Action

  * Print Invoice
  * Invoice Confirmation Email !!
  * Multi Action

.. i18n: The only problem with the Multi Action is that it will execute many actions at the server side, but only
.. i18n: one client action will be executed.

The only problem with the Multi Action is that it will execute many actions at the server side, but only
one client action will be executed.

.. i18n: For example we would like to print report + execute the wizard this 2 operation is not allowd in the
.. i18n: one multi action.

For example we would like to print report + execute the wizard this 2 operation is not allowd in the
one multi action.

.. i18n: .. image:: images/multi_action.png

.. image:: images/multi_action.png

.. i18n: Important Fields are

Important Fields are

.. i18n: :Object: Select the object on which we want to implement the Server Action when work flow will execute on this object
.. i18n: :Other Actions: We need to select the server action in this fields, we are free to select the as many as actions as we can. Just we need to take care for the problem of the multi action, other things is very easy.

:Object: Select the object on which we want to implement the Server Action when work flow will execute on this object
:Other Actions: We need to select the server action in this fields, we are free to select the as many as actions as we can. Just we need to take care for the problem of the multi action, other things is very easy.

.. i18n: **Link it up with the Work flow**

**Link it up with the Work flow**

.. i18n: The important things is to link the server action with the work flow, its bit easy to link with action
.. i18n: with the work flow. Open the work flow editor in GTK, select the work flow and go to the start and
.. i18n: select the Sever Action. This will automatically be called when the object comes to that state.

The important things is to link the server action with the work flow, its bit easy to link with action
with the work flow. Open the work flow editor in GTK, select the work flow and go to the start and
select the Sever Action. This will automatically be called when the object comes to that state.

.. i18n: .. image:: images/link_workflow.png

.. image:: images/link_workflow.png

.. i18n: Here in this example I added the Action to print the Invoice, when the Invoice will be confirmed.

Here in this example I added the Action to print the Invoice, when the Invoice will be confirmed.
