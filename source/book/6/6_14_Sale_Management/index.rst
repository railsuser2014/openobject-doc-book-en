Management of Sales
^^^^^^^^^^^^^^^^^^^^

*This chapter is for sales management in Open ERP, handling the complete order process from quotation to customer order, including control of deliveries and invoicing.*

*It doesn't look at customer relations and pre-sales. These functions are handled by the CRM (Customer Relationship Management) modules.*

Estimation of the order
-----------------------

In Open ERP a quotation and an order are handled by the same object, but in different states. You can consider an order to be a quotation that has evolved because it has been confirmed by the customer. Or, conversely, that a quotation is an order that hasn't yet been validated or cancelled. All of the orders and quotations in the system can be reached using the menu *Sales Management > Orders*.

Entering Quotation details
-------------------------------

To enter details of a new quotations you can use the menu *Sales Management > Orders > New Quotation*. Open ERP then opens a new window so that you can enter data into new blank quotation form.

    .. image:: images/sale_quotation_new.png
       :align: center

*Data entry for a new quotation.*

Some information is automatically completed by the system:

* an internal reference for the quotation or order,

* the point of sale that the order will be expedited from,

* the order date.

You can modify any of that information before validating the quotation. You can see the customer reference in the header of the order. This optional field represent's the customer's own reference number – if the customer doesn't supply one then just leave it empty.

You then enter all the data about the order in the tab 'Customer Order'. Start by entering the customer name, selecting the correct customer from the list of customers in the system. You can create a new customer on the fly at this stage if necessary – press <F1> in the corresponding field.

Once the customer name has been selected, different fields of the order become completed automatically, based on the configuration of the partner form for the selected customer:

* Order Address: person handling the order at the customer. By default, Open ERP proposes the Contact Address at the selected partner.

* Delivery Address: address used on the delivery order. By default, Open ERP proposes the Delivery address from the partner form. If nothing is defined in that slot, it uses the default address instead.

* Invoice Address: address used to send the invoice to the customer. By default, Open ERP proposes the address labelled “Invoice” from the partner form. If nothing is defined there, it uses the default address instead.

* Price List: will determine both the currency of the quotation and the price that will be used for each product

* Payment Conditions: shows the payment mode that the customer will follow, for example “50% on order, 50% on delivery”

* Delivery Method: for example “Post – Express Mail”

You can modify any of these fields on the order as you go.

You can also indicate an analytic account for your order. This account will be used during invoicing to automatically generate accounting entries corresponding to the invoice. This is extremely useful for assigning revenues to the project or case specified by this order.

  .. tip::   *Point*   Analytic Accounts

        If you're managing by task, the analytic account to be selected is the one that corresponds to the project for the order. The sale carried out by the order can be allotted to the project so that profitability calculations can be made.

Once the information has been entered, you can enter data for the order lines. To do that, create a new order line as shown in the figure below:

    .. image:: images/sale_line_form.png
       :align: center

*Entering an new customer order line.*

First of all select the product that is to be sold to the customer. Open ERP gives you all the useful information for your sale in the list of products it provides:

* Real stock: physically present in your warehouses. This value depends on the sale point selected in the order header. Different sale points can be linked to different warehouses, giving different stock levels, or can use the same warehouse.

* Virtual stock: shows a salesperson the quantity that can be sold, taking into account both stock reserved for other orders and quantities that could arrive in the short term.

* The Customer Price: depends on the conditions attached to the customer, calculated on the list price. This is the price that's proposed by default in the customer quotation, unless it's been modified by the salesperson.

* The List Price: the base sale price for the given product. It provides a base for the salesperson to be able to judge whether to offer a discount to the customer, and how much any discount should be.

* The Standard Cost: shows the cost price of the product. If the salesperson sells at less than this figure, then the company loses money.

    .. image:: images/sale_product_list.png
       :align: center

*Selecting a product in a Sales Order.*

When the product that's to be sold to the customer has been selected, Open ERP automatically completes all the other required fields: price, unit of measure, description, discount, lead times, applicable taxes, default packaging and the product description. All of this information comes from the product form.

  .. tip::   *Point*   Visible Discount

    By default, the customer discount is directly included in the sale price to the customer. He'll then see a discount of 0% but a reduced unit procie. If you install the module *product_visible_discount* you can configure whether you want to make the discount explicitly visible on the order form, or just reduce the unit price.

In the form, the selected product is presented in the language of the user so that he can understand what he's selling. The description of the product sold is presented in the customer's language. This language is used on the quotation or order when it's printed for the customer.

    .. image:: images/sale_line_translation.png
       :align: center

*Sale of a product in a partner language that differs from the user language.*

  .. tip::   *Point*   Exceptional Sales

    If a product's only sold to a customer once, you don't have to enter data into a complete new product form just for that sale. You can manually complete all the information in the order without putting it into a product: description, price, quantity, lead time, taxes. In that case Open ERP won't generate a delivery note because the product isn't held in stock.

When all of the products are entered, you can print the quotation and send it to the customer. To do this, click on the report to the right *Quotation / Order*. Open ERP then opens the quotation in PDF to enable to you to see it before printing.

    .. image:: images/sale_print.png
       :align: center

*Printing a customer quotation.*

You can then confirm the quotation to move it on to an order if the order is confirmed by the customer, or just cancel the window without confirming the order to leave it in quotation state. To find all of the current quotations, you can use the menu *Sales Management > Orders > My Orders > My Quotations*.

To follow the process for your order, you can click on the process view from the order form. Open ERP then shows you an interactive process view of that order. For more information about its use, look at the chapter on Process.

    .. image:: images/sale_process.png
       :align: center

*Process view from following a customer order.*

Management of Packaging
========================

Certain products can be managed in several different packaged forms. For example if you sell batteries you can define the following packages for a given battery product:

* by Piece: a battery

* Blister: a pack of 4 batteries

* Pack of 100 blisters: 400 batteries

* Palette, containing 40 packs for a total of 16,000 batteries.

Open ERP's packaging management enables you to sell the same product in several different forms. The salesperson could sell, independently, one battery or a palette of batteries. In the order, you can select the default packaging type as a function of the quantities ordered.

For example, if the customer wants to buy 30,000 batteries, the salesperson will select the packaing “palette”. Open ERP will then propose the sale of 32,000 batteries, which corresponds to two palettes, or of 75 packs.

The available packages are defined in the product form, in the *Packaging* tab. The first one on the list is the one that will be used by default.

Once a package has been defined on the order, Open ERP will throw up an alert if the ordered quantities don't correspond to the proposed packages. The quantity must be a multiple of the field *Quantity of items* defined on the packaging form.

    .. image:: images/sale_warning_packaging.png
       :align: center

*Alert on the quantities sold compared with the packaging.*

Don't confuse the management of packaging with the management of multiple units of measure. The Units of Measure are used to manage the stock in different units. In the case of packages, the stock is always managed by individual battery but information about the package to use is supplied along with the item for the storesperson.

Even if the effects are the same, the printed documents will be different. The two following operations will have the same effect on the levels of stock movement but will be printed differently on the sales order and the packing order:

* 32,000 batteries, delivered on two palettes,

* 2 palettes of batteries, with no information about packaging.

If the customer wants to order a palette and 10 packs, the salesperson can always put two order lines on the sales order using the same product but different units of measure.

Example Packing and different products
---------------------------------------

It's sometimes more useful to define different product than to define several possible packages for the same product. A case of beer in a supermarket is a good example. A case holds 24 bottles, plus the empty case itself. The customer can buy bottles by the piece or a case of 24 bottles at one go.

You could define two packages for the product *Bottle of beer*: *PCE* and *case*. But this representation doesn't let you manage the stock and price of empty cases. So you might instead prefer a Bill of Materials for the sale defining and using three different products:

* the empty case for the beer,

* the bottle of beer,

* the case of 24 bottles of beer.

You also define the bill of materials below which determines the make-up of the case of 24 beers:

* Case of 24 bottles of beer: 1 unit,

* Bottle of beer: 24 units,

* Empty case of beer: 1 unit.

Each of these three products has a different price. The products *Bottle of beer* and *Empty case of beer* have a stock to be managed. The *Case of 24 bottles of beer* has no stock because, if you sell the product, Open ERP automatically moves the stock in two lines, one for the empty case and the other for the 24 individual bottles of beer. For more information on bills of material for sale, look at the chapter on manufacturing management.

Management of Alerts
=====================

To manage alerts on products or partners, you can install the *warning* module. Once that is installed, it will enable you to configure a series of alerts on the partners or products.

    .. image:: images/warning_partner.png
       :align: center

*Management of alerts on partners.*

    .. image:: images/warning_product.png
       :align: center

*Management of alerts on products.*

You can activate alerts for a series of events. For each alert you should enter a message that will be attached to the person setting off the event. The different available events on the partner form are:

* Entering a customer order for the partner,

* Entering a supplier order for the partner,

* Sending a delivery to the partner (or receiving an item),

* Invoicing a partner.

The alerts that can be configured on a product form are:

* The sale of that product to a customer,

For example, if you enter an alert for the invoicing of a customer, for an accountant entering an invoice for that customer, the alert message will be attached as shown in the figure below:

    .. image:: images/warning_sample.png
       :align: center

*Alert from invoicing a customer.*

Control of deliveries and invoicing
====================================

Configuration of orders
------------------------

Depending on the configuration of the order, several different possible consequences might follow. Three fields will determine the behaviour of the order:

* Packing Policy : partial delivery, or complete delivery

* Invoicing : based on the order, or based on delivery

* Shipping Policy: invoicing based on order items, delivery and manual invoice, automatic invoicing after delivery.

  .. tip::   *Note*   Simplified view

    If you work in the simplified view mode, only the *Shipping Policy* field is visible in the second tab on the order. To get to the Extended View mode, assign the group *Usability – Extended View* to the current user.

Packing mode
--------------

The packing mode determines the way that the storesperson will do the packing. If the order is put into *Partial Delivery* mode, the packing order will appear in the list of things for the storesperson to do as soon as one of the products on the order is available. To get the list of items to be done you can use the menu *Stock Management > Outgoing Products > Available Packings*.

The storesperson will then be able to make a partial delivery of the quantities actually available and do a second packing later when the remaining products are available in stock.

If the packing mode is *Complete Delivery*, the packing list won't appear in the list of packings to do until all of the products are available in stock. In this case there will only be a single delivery for a given order.

If the storesperson wants, the delivery mode can be modified on each packing list even after the order has been confirmed.

In the case of invoicing on the basis of packing, the cost of delivering the products will be calculated on the basis of multiple deliveries. This risks a higher cost for the customer because of each delivery. If the invoicing is on the basis of the orders, the customer will only be invoiced once for the whole delivery, even if the delivery of several items has already been made.

Management of Carriers
========================

To manage deliveries in Open ERP, install the *delivery* module. If you have installed the *industry* profile this is installed by default during configuration of the database. This module enables you to manage:

* the different carriers with whom you work,

* the different possible modes of transport,

* cost calculation and invoicing of each delivery,

* the modes of transport and their tariffs.

Once the delivery module has been installed, the first thing to do is to configure the different modes of delivery accepted by your company. To do that use the menu *Stock Management > Configuration > Deliveries > Methods of Delivery*.

For each delivery mode, you should define the following elements:

* Name of the delivery mode,

* The partner associated with the transport (which can be yourselves),

* The associated product.

For example you can create the following modes:

================    ===========   ==========================
Delivery Mode       Partner       Associated Product
================    ===========   ==========================
Express Track       Mail Office   Express Track Delivery
Priority Courier    Mail Office   Courier Express Delivery
EFG Standard        EFG Inc       Delivery EFG
EFG Express         EFG Inc       Delivery EFG Express
================    ===========   ==========================

Information about the invoicing of transport (such as accounts, applicable taxes) are entered in the product linked to the delivery mode. Ideally the product should be configured as type 'service' and 'from stock'.

It's also possible to use the same product for several delivery modes. This simplifies the configuration but in this case your sales figures won't be be your delivery mode but globalized.

Tariff grids
=============

Unlike classical products, delivery prices aren't given by pricelists but by delivery grids, designed specifically for this purpose. For each delivery mode, you must enter several tariff grids. Each grid will be used for a given region/destination.

For example, for the postal tariffs for Priority Courier, you generally define the three taiff grids for Mail Office:

* Courier National,

* Courier Europe,

* Courier Outside Europe.

To define a new delivery grid, use the menu *Stock Management > Configuration > Deliveries > Delivery List Price*. You must then give a name to your delivery grid and define the region for which the tariffs in the grid will be applicable. To do this, use the second tab *Destination*. There you can set:

* A list of countries (for UK or Europe, for example),

* A list of states,

* A range of post codes (for Paris you might have 75000 – 75900).

You must then set the rules for calculating the price of transport in the first tab *Transprt Grid*. A rule must first of all have a name. Then set the condition for which this rule is applicable, for example Weight < 0.5kg.

  .. tip::   *Note*   Weights

    Weights are expressed in kilograms. You can define a number with a decimal point or comma, so that to set 500g you'd put 0.5 in the weight rule.

Then give the sale price and the cost price. The price can be expressed in different ways:

* a fixed price,

* a variable price, as a function of weight, or volume, or weight x volume or price.

For example, the rules for defining 

==========  =============  =====   =============
Rule Title  Condition      Price   Type of Price
==========  =============  =====   =============
S           Weight < 3 kg   6.9    Fixed
M           Weight < 5 kg  7.82    Fixed
L           Weight < 6 kg  8.53    Fixed
XL          Weight < 7 kg  9.87    Fixed
==========  =============  =====   =============

You can also define rules that depend on the total amount on the order. For example to offer the delivery if the order is more than 150 USD, add the following rule:

================= ===============  ======   =============
Rule Title        Condition        Price    Type of Price
================= ===============  ======   =============
Franked > 150 USD Price > 150 USD   10      Fixed
================= ===============  ======   =============

Using delivery modes
--------------------

Once the delivery modes and their tariffs have been defined you can use them in an order. To do that, two methods exist in Open ERP.

* Delivery based on order quantities,

* Delivery based on sent items.

Delivery based on the order
---------------------------

To add the delivery charges on the quotation, use the action *Delivery Costs* available to the right of the form. A dialog box opens, asking you to select a delivery mode from one of the available ones.

    .. image:: images/sale_delivery.png
       :align: center

*Adding a delivery charge to an order.*

Once the delivery mode has been selected, Open ERP automatically adds a line on the draft oder with the amount calculated by the delivery function. This technique will then enable you to calculate the delivery charge based on the order and then independently how the products will really be delivered to the customer.

If you want to calculate the exact delivery charges depending on the actual deliveries you must use invoicing based on deliveries.

Delivery based on the packed items
----------------------------------

To invoice the delivery on the basis of items packed you must indicate the delivery mode in the field 'carrier' on the <TODO>

Margin Control
----------------

<TODO>

Margins on sales orders
------------------------------

<TODO>

    .. image:: images/sale_margin.png
       :align: center

*An order with the module sale_margin.*

<TODO>

Margins by products
====================

<TODO>

    .. image:: images/product_margin_tree.png
       :align: center

*Screen following product margins.*

<TODO>

    .. image:: images/service_pricelist_line.png
       :align: center

*Detail of a rule in a version of the pricelist.*

<TODO>

    .. image:: images/product_pricelist_default.png
       :align: center

*Default pricelist after installing Open ERP.*

<TODO>

    .. image:: images/discount_campaign_RFA.png
       :align: center

*Configuring an end-of-year discount.*

<TODO>

    .. image:: images/discount_campaign.png
       :align: center

*Configuring a campaign of discounting on computers.*

<TODO>

    .. image:: images/sale_delivery.png
       :align: center

*Managing open orders, planning forecasts.*

In the order lines, Open ERP indicates the quantity planned <TODO>

Order templates
===============

At the time of writing, Tiny's development team was preparing a new module called *sale_layout*. This enables you to have a more elaborate template than the standard order forms.

For example you could put the follwing in the order lines:

* a horizontal separator line,

* titles and subtitles,

* subtotals at the end of the section,

* comments,

* a page break.

This enables you to lay out a more elaborate professional-looking quotation page. There's also the module *account_invoice_layout* which gives you the same functionality for invoice templates.

The two following figures show an invoice template in Open ERP and the resulting printed invoice.

    .. image:: images/invoice_layout_form.png
       :align: center

*Template for an invoice in Open ERP using the account_invoice_layout module.*

    .. image:: images/invoice_layout_print.png
       :align: center

*The resulting printed invoice.*

<incomplete chapter>
