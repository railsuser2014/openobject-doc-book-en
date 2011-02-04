
Sales Quotations
================

In OpenERP, a quotation and an order are handled by the same underlying object, but in different states. You
can consider an order to be a quotation that has evolved because it has been confirmed by the
customer. Or, conversely, that a quotation is an order that has not yet been validated or cancelled.
All of the orders and quotations in the system can be reached using the menu :menuselection:`Sales
--> Sales --> Sales Orders`.

To enter details of a new quotation, you can use the menu :menuselection:`Sales -->
Sales --> Sales Orders` and then select :guilabel:`New`. OpenERP then opens a new window
so that you can enter data into a new blank quotation form.

.. figure:: images/sale_quotation_new.png
   :scale: 75
   :align: center

   *Data entry for a new quotation*

Some information is automatically specified by the system:

* an internal reference for the quotation or order,

* the sale point that the order will be delivered from,

* the order date,

* the pricelist for the current sales order.

You can modify any of that information before validating the quotation. The customer
reference is shown in the header of the order. This optional field is for the customer's own reference –
if the customer does not supply one then just leave it empty.

You then enter all the data about the order in the :guilabel:`Sales Order` tab. Start by entering
the customer name, selecting the correct customer from the list of customers in the system. You can
create a new customer on the fly at this stage if necessary – press :kbd:`<F1>` in the empty
:guilabel:`Customer` field to do that.

Once the customer name has been selected, different fields of the order are completed
automatically, based on the configuration of the partner form for that customer:

* :guilabel:`Ordering Contact` : person handling the order at the customer end. By default, OpenERP
  proposes the Ordering Contact at the selected partner.

* :guilabel:`Shipping Address` : address used on the delivery order. By default, OpenERP proposes
  the shipping address from the partner form. If nothing is defined in that slot, it uses the default
  address instead.

* :guilabel:`Invoice Address` : address used to send the invoice to the customer. By default, OpenERP
  proposes the address labelled :guilabel:`Invoice` from the partner form. If nothing is defined there,
  it uses the default address instead.

* :guilabel:`Pricelist` : will determine both the currency of the quotation and the price that will
  be used for each product.

* :guilabel:`Payment Term` : available in the :guilabel:`Other Information` tab, it shows the payment
  method that the customer will follow, for example ``30 Days End of Month``.

You can modify any of these fields on the order as you go.

You can also set an analytic account for your order. This account will be used during invoicing
to generate accounting entries corresponding to the invoice automatically. This is extremely useful
for assigning revenues to the project or case specified by this order.

.. tip::  Analytic Accounts

   If you are managing by task, the analytic account to be selected is the one that corresponds to
   the project for the order.
   The sale carried out by the order can be allocated to the project so that profitability
   calculations can be made.

Once the information has been entered, you can enter data for the order lines. To do that, create a
new order line as shown in the figure :ref:`fig-slinf`:

.. _fig-slinf:

.. figure:: images/sale_line_form.png
   :scale: 75
   :align: center

   *Entering a new sales order line*

First of all, select the product that is to be sold to the customer. OpenERP shows some
useful information in the list of products to help you during your sale:

* :guilabel:`Real Stock` : physically present in your warehouses. This value depends on the sale
  point selected in the order header. Different sale points can be linked to different warehouses,
  giving different stock levels, or can use the same warehouse.

* :guilabel:`Virtual Stock` : shows a salesperson the quantity that can be sold, taking into account
  both stock reserved for other orders and amounts that could arrive in the short term.

* :guilabel:`Pricelist` : (may not be shown, depending on the installed modules) depends on the conditions attached to the customer, calculated on the
  list price. This is the price that is proposed by default in the customer quotation, unless it has been
  modified by the salesperson.

* :guilabel:`Public Price` : the base sale price for the given product. It provides a base for the
  salesperson to be able to judge whether to offer a discount to the customer, and how much the
  discount should be.

* :guilabel:`Cost Price` : shows the cost price of the product. If the salesperson sells at less
  than this amount, then the company incurs a loss.

.. figure:: images/sale_product_list.png
   :scale: 75
   :align: center

   *Selecting a product in a Sales Order Line*

When the product that is to be sold to the customer has been selected, OpenERP automatically
completes all the other required fields: quantity, unit of measure, description, unit price,
discount, procurement method, lead times and applicable taxes. All of this information comes from
the product form.

.. index::
   single: module; product_visible_discount

.. tip:: Visible Discount

   If a discounted price is taken from a price list, then by default that figure is shown as the
   sale price to the customer. He will see a discount of 0% along with unit price that is different
   from the list price.
   If you install the module :mod:`product_visible_discount` from ``extra-addons``
   you can configure whether you want to make the discount
   explicitly visible on an order form as a percentage difference from the list price,
   or just show a reduced unit price as it does by default.

In the form, the selected product is presented in the language of the user so that he can see
what he is selling. The description of the product sold can also be expressed in the customer's language.
The translation to the customer's language is used on the quotation or order when it is printed.

.. figure:: images/sale_line_translation.png
   :scale: 75
   :align: center

   *Sale of a product in a partner language that differs from the user language*

.. note:: One-off Sales

   If a product is sold to a customer only once, you do not have to enter data into a complete new
   product form just for that sale.
   You can manually complete all the information in the order without putting it into a product:
   description, price, quantity, lead time, taxes.
   In this case OpenERP will not generate a delivery note because the product is not held in stock.

When all of the products are entered, you can print the quotation and send it to the customer. To do
this, click on the link :guilabel:`Quotation / Order` in the :guilabel:`Reports` section to the right.
OpenERP opens the quotation in PDF to enable to you to see it before printing.

.. figure:: images/sale_print.png
   :scale: 75
   :align: center

   *Printing a sales quotation*

You can then confirm the quotation to move it on to an order if the order is confirmed by the
customer, or just cancel the window without confirming the order to leave it in quotation state. To
find all of the current quotations, you can use the menu :menuselection:`Sales --> Sales
--> Sales Orders` and click the :guilabel:`Quotations` filter button.

To follow the process for your order, you can click on the process view from the order form. OpenERP
shows you an interactive process view of that order. For more information about its use,
look at :ref:`ch-process`.

.. figure:: images/sale_process.png
   :scale: 75
   :align: center

   *Process view from following a sales order*

.. Copyright © Open Object Press. All rights reserved.

.. You may take electronic copy of this publication and distribute it if you don't
.. change the content. You can also print a copy to be read by yourself only.

.. We have contracts with different publishers in different countries to sell and
.. distribute paper or electronic based versions of this book (translated or not)
.. in bookstores. This helps to distribute and promote the OpenERP product. It
.. also helps us to create incentives to pay contributors and authors using author
.. rights of these sales.

.. Due to this, grants to translate, modify or sell this book are strictly
.. forbidden, unless Tiny SPRL (representing Open Object Press) gives you a
.. written authorisation for this.

.. Many of the designations used by manufacturers and suppliers to distinguish their
.. products are claimed as trademarks. Where those designations appear in this book,
.. and Open Object Press was aware of a trademark claim, the designations have been
.. printed in initial capitals.

.. While every precaution has been taken in the preparation of this book, the publisher
.. and the authors assume no responsibility for errors or omissions, or for damages
.. resulting from the use of the information contained herein.

.. Published by Open Object Press, Grand Rosière, Belgium
