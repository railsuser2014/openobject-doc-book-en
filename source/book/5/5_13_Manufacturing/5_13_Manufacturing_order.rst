Production order in detail
===========================

In this section production orders are detailed. To open a production order, use the menu Manufacturing > Production Orders > New Product Order. You get a blank for for encoding a new production order as shown in the figure below.

    .. image:: images/mrp_production_new.png
       :align: center

*New production order.*

The production order follows the process given by the figure below.

    .. image:: images/mrp_production_processus.png
       :align: center

*Process for handling a production order.*

The date fields, priority and reference, are automatically completed when the form is first opened. Enter the product that you want to produce, and the quantity required. The Unit of Measure by default is completed automatically by Open ERP when the product is first created.

You then have to set two locations:

The location where the required raw materials should be looked for, and

The location for depositing the finished products.

You can put the Stock location in both places for simplicilty. The field Bill of Materials will automatically be completed by Open ERP when you click the button 'Calculate the Requirements'. You can then overwrite it with another BoM to specify something else to use for this specific manufacture.

The tabs 'Planned Products' and 'Works Orders' are also completed automatically when you click 'Calculate the requirements'. You'll find the raw materials there that are required for the production and the operations needed by the assembly staff.

If you want to start production, click the button 'Confirm production', and Open ERP then automatically completes the field 'Products planned'. The information in the first tab can be changed for example if:

* you want to encode a serial number for raw materials,

* you want to change the quantities consumed (lost during production).

For traceability you can take the lot numbers from the raw materials used or from the finished products. To do this click on one of the lines of the first or the third tab. Note the Lot Number.

Once the order is confirmed, you should force the reservation of materials. This means that you're not waiting for the scheduler to assign and reserve the raw materials from your stock for this production. This shortcuts the procurement process. If you don't want to change the priorities, just leave the production order in this state and the scheduler will create a plan based on the priority and your planned date.

To start the production of products, click 'Start Production'. The raw materials are then consumed automatically from stock, which means that the draft movements become 'Done'.

Once the production is complete, click 'Production Finished'. The finished product are then put into stock.


