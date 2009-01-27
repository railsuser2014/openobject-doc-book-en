Workflow for complete production
=================================

To understand the usefulness and the functioning of the system you should test a complete workflow on the new database installed with the demonstration data. In the order you can see:

* The creation of a customer order,

* The manufacturing workflow for an intermediate product,

* The manufacture of an ordered product,

* The delivery of products to a customer,

* Invoicing at the end of the month,

* Traceability for after-sales service.

.. tip:: **Attention**  *Demonstration data*

    To follow the workflow shown below well, it's important to keep the same quantities as in the example and start from a new database so that you don't run into exceptions from a lack of stock.

This case, more advanced, of handling problems of procurement, will be sorted out later in the chapter.

The customer order
-------------------

Begin by encoding a customer order. To do this, use the menu *Sales Management > Orders > New Quotation*. Enter the following information:

* Customer: Agrolait,

* Shipping Policy: Invoice from picklist (second tab),

* Order Line:

  * Product: PC2 – Basic PC (assemble on demand),

  * Quantity (UoM): 1,

  * Product UoM: PCE,

  * Procure method: Make To Order.

Once the quotation has been entered you can confirm it immediately by clicking the button at the bottom to the right *Confirm Order*. Keep note of the order reference because this follows all through the process. Usually, in a new database, this will be “SO007”. At this stage you can look at the process linked to your order using the 'Process' button above and to the right of the form.

    .. image:: images/mrp_sale_process.png
       :align: center

*Process for handling Sales Order SO007.*

Start the requirements calculation using the menu *Manufacturing > Compute All Schedulers*.

Producing an Intermediate Product
-----------------------------------

To understand the implications of requirements calculation, you must know the configuration of the sold product. To do this, go to the form for product PC2 and click on the link to the right: Bill of Materials. You get the scheme show below which is the composition of the selected product.

    .. image:: images/mrp_product_bom_tree.png
       :align: center

*Composition of product PC2 in the demonstration data.*

You can see that manufacturing the PC2 computer must be done in two steps:

1: Manufacture of the intermediate product: CPU_GEN

2: Manufacture of the finished product using that intermediate product: PC2

The manufacturing supervisor can then consult the product orders using the menu Manufacturing > Production Orders > Production Orders to start. You then get a list of orders to start and the estimated start date if the customer order date is not to be missed.

    .. image:: images/mrp_production_list.png
       :align: center

*List of production orders.*

You'll see the production order for CPU_GEN but not that for PC2 because that one depends on an intermediate product. Return to the production order for CPU_GEN and click below it. If there are several of them, select the one corresponding to your order using the reference that contains your order number (in this example SO007).

    .. image:: images/mrp_production_form.png
       :align: center

*The detail of a production order.*

The system shows you that you must manufacture product CPU_GEN using the components: MB1, CPU1, FAN, RAM. You can then confirm the production twice:

Start of production: consumption of raw materials,

End of production: manufacture of finished product.

At this stage, you should click to edit the line for the product MB1 to encode a lot number for it. The lot number is usually shown the parent chart, so you should just copy that over. To do that put the cursor in the field Production Lot and press <F1> to create a new lot. Set a lot reference, for example: MB1345678. The system may then show you a warning because this lot is not in stock, but you can ignore this message.

The production order must be in the closed state as shown in the figure below.

    .. image:: images/mrp_production_form_end.png
       :align: center

*Production order at the end of the different steps.*

Manufacture of finished product
--------------------------------

Having manufactured the intermediate product CPU_GEN, Open ERP then automatically suggests the manufacture of the computer PC2 using the order created earlier. So return to the menu for production orders to start *Manufacturing > Production Orders > Production Orders to start*.

You'll now find the computer PC2 which has been sold to the customer, as shown in the figure below.

    .. image:: images/mrp_production_list_end.png
       :align: center

*List of production orders.*

Just as for product CPU_GEN, confirm the production order on two dates: start of production and end of production.

At this stage the product sold to the customer has been manufactured and the raw materials have been consumed and taken out of stock.

.. tip:: **Point**  *Automatic Actions*

    As well as managing the use of materials and the production of stocks, manufacturing can have the following effects which are detailed further on in the chapter:

    * adding value to stock,

    * managing operations for assembly staff,

    * automatically creating analytical accounting entries.

Delivery of product to the customer
--------------------------------------

When the products have been manufactured, the storesperson automaticallys finds the order in his list of items to do. To see the items waiting for delivery, use the menu Stock Management > Outgoing Products > Available Packings. You'll find there the lists of packing to do, as shown in the figure below.

    .. image:: images/mrp_packing_out.png
       :align: center

*List of packings to do.*

The packing orders are treated by priority of leaving so the storesperson must begin with the orders at the top of the list. Confirm that your packing list has been create by looking for the customer name (Agrolait) or by its reference (SO007). Click on it and then click the button “Approve”.

.. tip::   **Point** *Packings and Delivery*

    Depending on whether you work in the simplified or extended mode you may have to do a further operation to make a delivery to your customer and so carry out the two steps:

    * pick lists,

    * delivery order.

Invoicing at delivery
----------------------

Periodically the administrator or an accountant can send invoices based on the deliveries that have been carried out. To do that, you can use the menu *Stock Management > Outgoing Products > Items to Invoice*. You then get a list of all the deliveries that have been made but haven't yet been invoiced. 

So select some or all of the deliveries. Click on the action “Invoice pickings”. Open ERP asks if you want to group the deliveries from the same partner into a single invoice or if you prefer to invoice for each delivery individually.

    .. image:: images/mrp_picking_invoice_form.png
       :align: center

*Invoicing of deliveries.*

Invoices are then produced automatically in the draft state by Open ERP and the orders of deliveries are eventually added if they were configured on the order. You can also modify the invoice before approving them finally.

    .. image:: images/mrp_invoice_list.png
       :align: center

*List of invoices generated by the system based on deliveries.*

Once you have reviewed the different invoices that were generated, you can confirm them one by one or all at once from the actions available to you. Then print the invoices using the multiple print option and send them to your customers by post.

Traceability
-------------

Now suppose that the customer phones you to tell you about a production fault in a delivered product. You can then consult the traceability through the whole manufacturing chain using the serial number indicate on the product MB1. To consult the detailed history, use the menu *Stock Management > Traceability > Production Lots*.

So find the product corresponding to the product or lot number. Once it's been found you can use the following actions:
* Upstream traceability: go back through the entire production chain to various suppliers of the final customer.

* Downstream traceability: follow the production chain to find the final customer of specified components.

Examples of the two traceability types are given in the by the following figures:

    .. image:: images/mrp_tracability_upstream.png
       :align: center

*Upstream traceability from customer to suppliers.*

    .. image:: images/mrp_tracability_downstream.png
       :align: center

*Downstream traceability from supplier to customers.*


