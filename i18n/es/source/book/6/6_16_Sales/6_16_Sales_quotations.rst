
.. i18n: Sales Quotations
.. i18n: ================

Sales Quotations
================

.. i18n: In Open ERP a quotation and an order are handled by the same underlying object, but in different states. You
.. i18n: can consider an order to be a quotation that has evolved because it has been confirmed by the
.. i18n: customer. Or, conversely, that a quotation is an order that hasn't yet been validated or cancelled.
.. i18n: All of the orders and quotations in the system can be reached using the menu :menuselection:`Sales
.. i18n: Management --> Orders`.

In Open ERP a quotation and an order are handled by the same underlying object, but in different states. You
can consider an order to be a quotation that has evolved because it has been confirmed by the
customer. Or, conversely, that a quotation is an order that hasn't yet been validated or cancelled.
All of the orders and quotations in the system can be reached using the menu :menuselection:`Sales
Management --> Orders`.

.. i18n: Entering Quotation details
.. i18n: --------------------------

Entering Quotation details
--------------------------

.. i18n: To enter details of a new quotations you can use the menu :menuselection:`Sales Management -->
.. i18n: Orders --> New Quotation`. Open ERP then opens a new window so that you can enter data into new
.. i18n: blank quotation form.

To enter details of a new quotations you can use the menu :menuselection:`Sales Management -->
Orders --> New Quotation`. Open ERP then opens a new window so that you can enter data into new
blank quotation form.

.. i18n: .. figure:: images/sale_quotation_new.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Data entry for a new quotation*

.. figure:: images/sale_quotation_new.png
   :scale: 75
   :align: center

   *Data entry for a new quotation*

.. i18n: Some information is automatically completed by the system:

Some information is automatically completed by the system:

.. i18n: * an internal reference for the quotation or order,
.. i18n: 
.. i18n: * the sale point that the order will be delivered from,
.. i18n: 
.. i18n: * the order date.

* an internal reference for the quotation or order,

* the sale point that the order will be delivered from,

* the order date.

.. i18n: You can modify any of that information before validating the quotation. The customer
.. i18n: reference is shown in the header of the order. This optional field if for the customer's own reference
.. i18n: number – if the customer doesn't supply one then just leave it empty.

You can modify any of that information before validating the quotation. The customer
reference is shown in the header of the order. This optional field if for the customer's own reference
number – if the customer doesn't supply one then just leave it empty.

.. i18n: You then enter all the data about the order in the :guilabel:`Sale Order` tab. Start by entering
.. i18n: the customer name, selecting the correct customer from the list of customers in the system. You can
.. i18n: create a new customer on the fly at this stage if necessary – press :kbd:`<F1>` in the empty
.. i18n: :guilabel:`Customer` field to do that.

You then enter all the data about the order in the :guilabel:`Sale Order` tab. Start by entering
the customer name, selecting the correct customer from the list of customers in the system. You can
create a new customer on the fly at this stage if necessary – press :kbd:`<F1>` in the empty
:guilabel:`Customer` field to do that.

.. i18n: Once the customer name has been selected, different fields of the order become completed
.. i18n: automatically, based on the configuration of the partner form for that customer:

Once the customer name has been selected, different fields of the order become completed
automatically, based on the configuration of the partner form for that customer:

.. i18n: * :guilabel:`Order Address` : person handling the order at the customer. By default, Open ERP
.. i18n:   proposes the Contact Address at the selected partner.
.. i18n: 
.. i18n: * :guilabel:`Delivery Address` : address used on the delivery order. By default, Open ERP proposes
.. i18n:   the Delivery address from the partner form. If nothing is defined in that slot, it uses the default
.. i18n:   address instead.
.. i18n: 
.. i18n: * :guilabel:`Invoice Address` : address used to send the invoice to the customer. By default, Open
.. i18n:   ERP proposes the address labelled :guilabel:`Invoice` from the partner form. If nothing is defined there,
.. i18n:   it uses the default address instead.
.. i18n: 
.. i18n: * :guilabel:`Price List` : will determine both the currency of the quotation and the price that will
.. i18n:   be used for each product.
.. i18n: 
.. i18n: * :guilabel:`Payment Conditions` : shows the payment method that the customer will follow, for example
.. i18n:   ``50% on order, 50% on delivery`` .
.. i18n: 
.. i18n: * :guilabel:`Delivery Method` : for example ``Post – Express Mail`` .

* :guilabel:`Order Address` : person handling the order at the customer. By default, Open ERP
  proposes the Contact Address at the selected partner.

* :guilabel:`Delivery Address` : address used on the delivery order. By default, Open ERP proposes
  the Delivery address from the partner form. If nothing is defined in that slot, it uses the default
  address instead.

* :guilabel:`Invoice Address` : address used to send the invoice to the customer. By default, Open
  ERP proposes the address labelled :guilabel:`Invoice` from the partner form. If nothing is defined there,
  it uses the default address instead.

* :guilabel:`Price List` : will determine both the currency of the quotation and the price that will
  be used for each product.

* :guilabel:`Payment Conditions` : shows the payment method that the customer will follow, for example
  ``50% on order, 50% on delivery`` .

* :guilabel:`Delivery Method` : for example ``Post – Express Mail`` .

.. i18n: You can modify any of these fields on the order as you go.

You can modify any of these fields on the order as you go.

.. i18n: You can also set an analytic account for your order. This account will be used during invoicing
.. i18n: to generate accounting entries corresponding to the invoice automatically. This is extremely useful
.. i18n: for assigning revenues to the project or case specified by this order.

You can also set an analytic account for your order. This account will be used during invoicing
to generate accounting entries corresponding to the invoice automatically. This is extremely useful
for assigning revenues to the project or case specified by this order.

.. i18n: .. tip::  Analytic Accounts
.. i18n: 
.. i18n:    If you're managing by task, the analytic account to be selected is the one that corresponds to
.. i18n:    the project for the order.
.. i18n:    The sale carried out by the order can be allocated to the project so that profitability
.. i18n:    calculations can be made.

.. tip::  Analytic Accounts

   If you're managing by task, the analytic account to be selected is the one that corresponds to
   the project for the order.
   The sale carried out by the order can be allocated to the project so that profitability
   calculations can be made.

.. i18n: Once the information has been entered, you can enter data for the order lines. To do that, create a
.. i18n: new order line as shown in the figure :ref:`fig-slinf`:

Once the information has been entered, you can enter data for the order lines. To do that, create a
new order line as shown in the figure :ref:`fig-slinf`:

.. i18n: .. _fig-slinf:
.. i18n: 
.. i18n: .. figure:: images/sale_line_form.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Entering a new customer order line*

.. _fig-slinf:

.. figure:: images/sale_line_form.png
   :scale: 75
   :align: center

   *Entering a new customer order line*

.. i18n: First of all select the product that is to be sold to the customer. Open ERP shows some
.. i18n: useful information in the list of products to help you during your sale:

First of all select the product that is to be sold to the customer. Open ERP shows some
useful information in the list of products to help you during your sale:

.. i18n: * :guilabel:`Real stock` : physically present in your warehouses. This value depends on the sale
.. i18n:   point selected in the order header. Different sale points can be linked to different warehouses,
.. i18n:   giving different stock levels, or can use the same warehouse.
.. i18n: 
.. i18n: * :guilabel:`Virtual stock` : shows a salesperson the quantity that can be sold, taking into account
.. i18n:   both stock reserved for other orders and amounts that could arrive in the short term.
.. i18n: 
.. i18n: * :guilabel:`Customer Price` : (May not be shown, depending on the installed modules). depends on the conditions attached to the customer, calculated on the
.. i18n:   list price. This is the price that's proposed by default in the customer quotation, unless it's been
.. i18n:   modified by the salesperson. 
.. i18n: 
.. i18n: * :guilabel:`List Price` : the base sale price for the given product. It provides a base for the
.. i18n:   salesperson to be able to judge whether to offer a discount to the customer, and how much any
.. i18n:   discount should be.
.. i18n: 
.. i18n: * :guilabel:`Cost Price` : shows the cost price of the product. If the salesperson sells at less
.. i18n:   than this amount, then the company loses money.

* :guilabel:`Real stock` : physically present in your warehouses. This value depends on the sale
  point selected in the order header. Different sale points can be linked to different warehouses,
  giving different stock levels, or can use the same warehouse.

* :guilabel:`Virtual stock` : shows a salesperson the quantity that can be sold, taking into account
  both stock reserved for other orders and amounts that could arrive in the short term.

* :guilabel:`Customer Price` : (May not be shown, depending on the installed modules). depends on the conditions attached to the customer, calculated on the
  list price. This is the price that's proposed by default in the customer quotation, unless it's been
  modified by the salesperson. 

* :guilabel:`List Price` : the base sale price for the given product. It provides a base for the
  salesperson to be able to judge whether to offer a discount to the customer, and how much any
  discount should be.

* :guilabel:`Cost Price` : shows the cost price of the product. If the salesperson sells at less
  than this amount, then the company loses money.

.. i18n: .. figure:: images/sale_product_list.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Selecting a product in a Sales Order*

.. figure:: images/sale_product_list.png
   :scale: 75
   :align: center

   *Selecting a product in a Sales Order*

.. i18n: When the product that's to be sold to the customer has been selected, Open ERP automatically
.. i18n: completes all the other required fields: price, unit of measure, description, discount, lead times,
.. i18n: applicable taxes, default packaging and the product description. All of this information comes from
.. i18n: the product form.

When the product that's to be sold to the customer has been selected, Open ERP automatically
completes all the other required fields: price, unit of measure, description, discount, lead times,
applicable taxes, default packaging and the product description. All of this information comes from
the product form.

.. i18n: .. index::
.. i18n:    single: module; product_visible_discount

.. index::
   single: module; product_visible_discount

.. i18n: .. tip:: Visible Discount
.. i18n: 
.. i18n:    If a discounted price is taken from a price list then by default that figure is shown as the 
.. i18n:    sale price to the customer. He'll see a discount of 0% along with unit price that is different 
.. i18n:    from the list price.
.. i18n:    If you install the module :mod:`product_visible_discount` from addons-extra
.. i18n:    you can configure whether you want to make the discount
.. i18n:    explicitly visible on an order form as a percentage difference from the list price, 
.. i18n:    or just show a reduced unit price as it does by default.

.. tip:: Visible Discount

   If a discounted price is taken from a price list then by default that figure is shown as the 
   sale price to the customer. He'll see a discount of 0% along with unit price that is different 
   from the list price.
   If you install the module :mod:`product_visible_discount` from addons-extra
   you can configure whether you want to make the discount
   explicitly visible on an order form as a percentage difference from the list price, 
   or just show a reduced unit price as it does by default.

.. i18n: In the form, the selected product is presented in the language of the user so that he can see
.. i18n: what he's selling. The description of the product sold can also be expressed in the customer's language. 
.. i18n: The translation to the customer's language is used on the quotation or order when it's printed.

In the form, the selected product is presented in the language of the user so that he can see
what he's selling. The description of the product sold can also be expressed in the customer's language. 
The translation to the customer's language is used on the quotation or order when it's printed.

.. i18n: .. figure:: images/sale_line_translation.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Sale of a product in a partner language that differs from the user language*

.. figure:: images/sale_line_translation.png
   :scale: 75
   :align: center

   *Sale of a product in a partner language that differs from the user language*

.. i18n: .. note:: One-off Sales
.. i18n: 
.. i18n:    If a product's only sold to a customer once, you don't have to enter data into a complete new
.. i18n:    product form just for that sale.
.. i18n:    You can manually complete all the information in the order without putting it into a product:
.. i18n:    description, price, quantity, lead time, taxes.
.. i18n:    In this case Open ERP won't generate a delivery note because the product isn't held in stock.

.. note:: One-off Sales

   If a product's only sold to a customer once, you don't have to enter data into a complete new
   product form just for that sale.
   You can manually complete all the information in the order without putting it into a product:
   description, price, quantity, lead time, taxes.
   In this case Open ERP won't generate a delivery note because the product isn't held in stock.

.. i18n: When all of the products are entered, you can print the quotation and send it to the customer. To do
.. i18n: this, click on the report :guilabel:`Quotation / Order` in the :guilabel:`REPORTS` links to the right. 
.. i18n: Open ERP opens the quotation in PDF to enable to you to see it before printing.

When all of the products are entered, you can print the quotation and send it to the customer. To do
this, click on the report :guilabel:`Quotation / Order` in the :guilabel:`REPORTS` links to the right. 
Open ERP opens the quotation in PDF to enable to you to see it before printing.

.. i18n: .. figure:: images/sale_print.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Printing a customer quotation*

.. figure:: images/sale_print.png
   :scale: 75
   :align: center

   *Printing a customer quotation*

.. i18n: You can then confirm the quotation to move it on to an order if the order is confirmed by the
.. i18n: customer, or just cancel the window without confirming the order to leave it in quotation state. To
.. i18n: find all of the current quotations, you can use the menu :menuselection:`Sales Management --> Orders
.. i18n: --> My Orders --> My Quotations`.

You can then confirm the quotation to move it on to an order if the order is confirmed by the
customer, or just cancel the window without confirming the order to leave it in quotation state. To
find all of the current quotations, you can use the menu :menuselection:`Sales Management --> Orders
--> My Orders --> My Quotations`.

.. i18n: To follow the process for your order, you can click on the process view from the order form. Open
.. i18n: ERP shows you an interactive process view of that order. For more information about its use,
.. i18n: look at :ref:`ch-process`.

To follow the process for your order, you can click on the process view from the order form. Open
ERP shows you an interactive process view of that order. For more information about its use,
look at :ref:`ch-process`.

.. i18n: .. figure:: images/sale_process.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Process view from following a customer order*

.. figure:: images/sale_process.png
   :scale: 75
   :align: center

   *Process view from following a customer order*

.. i18n: .. Copyright © Open Object Press. All rights reserved.

.. Copyright © Open Object Press. All rights reserved.

.. i18n: .. You may take electronic copy of this publication and distribute it if you don't
.. i18n: .. change the content. You can also print a copy to be read by yourself only.

.. You may take electronic copy of this publication and distribute it if you don't
.. change the content. You can also print a copy to be read by yourself only.

.. i18n: .. We have contracts with different publishers in different countries to sell and
.. i18n: .. distribute paper or electronic based versions of this book (translated or not)
.. i18n: .. in bookstores. This helps to distribute and promote the Open ERP product. It
.. i18n: .. also helps us to create incentives to pay contributors and authors using author
.. i18n: .. rights of these sales.

.. We have contracts with different publishers in different countries to sell and
.. distribute paper or electronic based versions of this book (translated or not)
.. in bookstores. This helps to distribute and promote the Open ERP product. It
.. also helps us to create incentives to pay contributors and authors using author
.. rights of these sales.

.. i18n: .. Due to this, grants to translate, modify or sell this book are strictly
.. i18n: .. forbidden, unless Tiny SPRL (representing Open Object Press) gives you a
.. i18n: .. written authorisation for this.

.. Due to this, grants to translate, modify or sell this book are strictly
.. forbidden, unless Tiny SPRL (representing Open Object Press) gives you a
.. written authorisation for this.

.. i18n: .. Many of the designations used by manufacturers and suppliers to distinguish their
.. i18n: .. products are claimed as trademarks. Where those designations appear in this book,
.. i18n: .. and Open Object Press was aware of a trademark claim, the designations have been
.. i18n: .. printed in initial capitals.

.. Many of the designations used by manufacturers and suppliers to distinguish their
.. products are claimed as trademarks. Where those designations appear in this book,
.. and Open Object Press was aware of a trademark claim, the designations have been
.. printed in initial capitals.

.. i18n: .. While every precaution has been taken in the preparation of this book, the publisher
.. i18n: .. and the authors assume no responsibility for errors or omissions, or for damages
.. i18n: .. resulting from the use of the information contained herein.

.. While every precaution has been taken in the preparation of this book, the publisher
.. and the authors assume no responsibility for errors or omissions, or for damages
.. resulting from the use of the information contained herein.

.. i18n: .. Published by Open Object Press, Grand Rosière, Belgium

.. Published by Open Object Press, Grand Rosière, Belgium
