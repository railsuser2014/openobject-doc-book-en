Management of repairs
======================

The management of repairs is carried out using the module *mrp_repair*. Once it's installed this module adds new menus to the Manufacturing menu:

* *Manufacturing > Repairs*

* *Manufacturing > Repairs > Repairs in quotation*

* *Manufacturing > Repairs > Repairs in progress*

* *Manufacturing > Repairs > Repairs Ready to Start*

* *Manufacturing > Repairs > Repairs to be invoiced*

* *Manufacturing > Repairs > New Repair*

In Open ERP a repair will have the following effects:

* Use of materials: items for replacement,

* Production of products: items replaced from reserved stock,

* Quality control: tracking the reasons for repair,

* Accounting entries: following stock moves,

* Receipt and delivery of product from and to the end user,

* Adding operations in the product traceability,

* Invoicing items used and/or free for repairs.

Entering data for a new repair
-------------------------------

Use the menu *Manufacturing > Repairs > New Repair* to enter a new repair into the system. You'll see a blank form for the repair data, as shown in the figure below.

    .. image:: images/mrp_repair_new.png
       :align: center

*Entering data for a new repair.*

Start by identifying the product that will be repaired using the product lot number. Open ERP then automatically completes fields from the selected lot – the partner fields, address, delivery location, and stock move.

If a warranty period has been defined in the product description, in months, Open ERP then completes the field 'Warranty limit' with the correct warranty date.

You must then specify the components that you'll be adding, replacing or removing in the operations part. On each line you must specify the following:

Add or remove a component of the finished product:

* Product Component,

* Quantity,

* Unit of Measure

* Price of Component,

* Possible lot number,

* Location where the component was found,

* To invoice or not.

Once the component has been selected, Open ERP automatically completes most of the fields:

* Quantity: 1,

* Unit of Measure: unit for managing stock defined in the product form,

* Component Price: calculated from the customer list price,

* Source location: given by the stock management,

* To invoice or not: depends on the actual date and the quarantee period.

This information is automatically proposed by the system but you can modify it all yourself.

You can also encode additional charges in the second tab of the repair: applicable list price, address and type of invoice, as well as additional line items that need to be added to the repair bill.

    .. image:: images/mrp_repair_tab2.png
       :align: center

*Second tab.*

The third tab, Quality, is for encoding information about the quality: internal notes, notes for the quotation, corrective actions and preventative actions for example.

Repair workflow
----------------

A defined process handles a repair order – both the repair itself and invoicing the client. The figure below shows this repair process.

    .. image:: images/mrp_repair_workflow.png
       :align: center

*Process for handling a repair.*

Once a repair has been entered onto the system, it is in the 'draft' state. In this state it has no impact on the rest of the system. You can print a quotation from it using the action 'Print Quotation'. The repair quotation can then be sent to the customer.

Once the customer approves the repair, use the menu *Manufacturing > Repairs > Repairs in quotation* to find the draft repair. Click to confirm the draft repair and put it into the running state. You can specify the invoicing mode in the second tab:

* no invoicing,

* invoicing before repair,

* invoicing after repair.

You can confirm the repair operation or create an invoice for the customer depending on this state.

Invoicing the repair
---------------------

When the repair is to be invoiced, an invoice is generated in the draft state by the system. This invoice contains the raw materials used (replaced components) and any other costs such as the time used for the repair. These other costs are entered on the second tab of the repair form.

If the product to be repaired is still under guarantee, Open ERP automatically suggests that the components themselves are not invoiced, but will still use any other defined costs. You can override any of these default values when you're entering the data.

The link to the generated invoice is shown on the second tab of the repair document.

Stock movements and repair
---------------------------

When the repair has been carried out, Open ERP automatically carries out stock movements for components that have been removed, added or replaced on the finished product.

The move operations are carried out using the locations shown on the first tab of the repair document. If a destination location has been specified, Open ERP automatically handles the final customer delivery order when the repair has been completed. This also lets you manage the delivery of the repaired products.

For example, take the case of the cabinet that was produced at the start of this chapter. If you have to replace the shelf PANLAT, you must enter data for the repair as in the figure below.

    .. image:: images/mrp_repair_panlat.png
       :align: center

*Repair of a shelf in a cabinet.*

In this example, you'd carry out the following operations:

* Removal of a PANLAT shelf in the cabinet and put the faulty shelf in the location: *Defective Products*,

* Placement of a new PANLAT shelf that has been taken from stock.

When the repair is ready to be confirmed, Open ERP will generate the following stock moves:

* Put faulty PANLAT into suitable stock location: *Default Production > Defective Products*,

* Consume PANLAT:*Stock > Default production*.

If you analyze the traceability of this lot number you'll see all the repair operations in the upstream and downstream traceability lists of the products concerned.

