
.. i18n: .. index::
.. i18n:    single: process integration
.. i18n:    
.. i18n: The integration of processes into the management system
.. i18n: =======================================================

.. index::
   single: process integration
   
The integration of processes into the management system
=======================================================

.. i18n: Processes are at the heart of a company: they form a structure for all
.. i18n: activities that enable the company to function effectively. A company's human
.. i18n: dimension is often disconnected from its processes at the moment, preventing
.. i18n: individual employees' aspirations from being directed towards a collective
.. i18n: objective.

Processes are at the heart of a company: they form a structure for all
activities that enable the company to function effectively. A company's human
dimension is often disconnected from its processes at the moment, preventing
individual employees' aspirations from being directed towards a collective
objective.

.. i18n: From a mapping process, integrating management and the changing needs of each
.. i18n: employee becomes very useful for the fulfillment of each. Based on that, each
.. i18n: employee becomes aware of his own personal contribution to the company's value
.. i18n: chain. This representation also helps an employee's own personal management
.. i18n: because it shows his place and his role in the overall process, very often over
.. i18n: several departments.

From a mapping process, integrating management and the changing needs of each
employee becomes very useful for the fulfillment of each. Based on that, each
employee becomes aware of his own personal contribution to the company's value
chain. This representation also helps an employee's own personal management
because it shows his place and his role in the overall process, very often over
several departments.

.. i18n: The system of 'Corporate Intelligence' will also be highly useful to system
.. i18n: implementers who, after studying the requirements, have to formalize a
.. i18n: company's processes to put them into operation in Open ERP.

The system of 'Corporate Intelligence' will also be highly useful to system
implementers who, after studying the requirements, have to formalize a
company's processes to put them into operation in Open ERP.

.. i18n: Examples of process
.. i18n: -------------------

Examples of process
-------------------

.. i18n: To understand the aims of the system of Corporate Intelligence (process)
.. i18n: better, you'll now see an overview of the functions available to you in a the study of
.. i18n: two processes:

To understand the aims of the system of Corporate Intelligence (process)
better, you'll now see an overview of the functions available to you in a the study of
two processes:

.. i18n: * A customer order quotation,
.. i18n: 
.. i18n: * The engagement of a new employee.

* A customer order quotation,

* The engagement of a new employee.

.. i18n: .. index::
.. i18n:    single: process; customer order

.. index::
   single: process; customer order

.. i18n: Following a customer sales order
.. i18n: ----------------------------------

Following a customer sales order
----------------------------------

.. i18n: The example :ref:`fig-procquot` shows the process for handling a customer sales order. Use
.. i18n: the menu :menuselection:`Sales Management --> Sales Orders` to list all orders, then choose
.. i18n: Order SO001 – you can either check the checkbox to its left, or you can open
.. i18n: the order itself by clicking the order date to the left of its name in the
.. i18n: list.

The example :ref:`fig-procquot` shows the process for handling a customer sales order. Use
the menu :menuselection:`Sales Management --> Sales Orders` to list all orders, then choose
Order SO001 – you can either check the checkbox to its left, or you can open
the order itself by clicking the order date to the left of its name in the
list.

.. i18n: To view the process for that specific order, click the :guilabel:`Process` button at the
.. i18n: top right of the list or form. The process for this order is shown in the
.. i18n: window, and the current state of this document can be seen by looking for the
.. i18n: node whose left edge is colored maroon rather than grey.

To view the process for that specific order, click the :guilabel:`Process` button at the
top right of the list or form. The process for this order is shown in the
window, and the current state of this document can be seen by looking for the
node whose left edge is colored maroon rather than grey.

.. i18n: .. _fig-procquot:
.. i18n: 
.. i18n: .. figure:: images/process_quotation_flow.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Example of a process handling a customer order quotation*

.. _fig-procquot:

.. figure:: images/process_quotation_flow.png
   :scale: 75
   :align: center

   *Example of a process handling a customer order quotation*

.. i18n: This order is in the Quotation state. The whole of some nodes is greyed out
.. i18n: because the selected document will never enter into that state, such as
.. i18n: invoicing based on deliveries (the order is in an invoicing mode that's based
.. i18n: on orders, not deliveries).

This order is in the Quotation state. The whole of some nodes is greyed out
because the selected document will never enter into that state, such as
invoicing based on deliveries (the order is in an invoicing mode that's based
on orders, not deliveries).

.. i18n: The process is completely dynamic and based on that specific sale order
.. i18n: document. You can click each of the process nodes (:guilabel:`Quotation`, :guilabel:`Sale Order`,
.. i18n: :guilabel:`Procurement`, :guilabel:`Draft Invoice`, :guilabel:`Outgoing Products`) using one of the
.. i18n: links or icons
.. i18n: on it:

The process is completely dynamic and based on that specific sale order
document. You can click each of the process nodes (:guilabel:`Quotation`, :guilabel:`Sale Order`,
:guilabel:`Procurement`, :guilabel:`Draft Invoice`, :guilabel:`Outgoing Products`) using one of the
links or icons
on it:

.. i18n: * Obtaining the documentation and the corresponding process in the quality manual, using the
.. i18n:   :guilabel:`Help` (or :guilabel:`Information`) icon,
.. i18n: 
.. i18n: * Opening the corresponding Open ERP document, using the :guilabel:`Open` icon,
.. i18n: 
.. i18n: * Printing the document, using the :guilabel:`Print` icon,
.. i18n: 
.. i18n: * Printing the technical workflow by using the Gears (or :guilabel:`Print Workflow`) icon.
.. i18n: 
.. i18n: * Obtaining the documents that an employee needs to carry out the process by clicking the green
.. i18n:   arrow icon,
.. i18n: 
.. i18n: * Seeing the menu that Open ERP uses to get the document by hovering over the green arrow icon.

* Obtaining the documentation and the corresponding process in the quality manual, using the
  :guilabel:`Help` (or :guilabel:`Information`) icon,

* Opening the corresponding Open ERP document, using the :guilabel:`Open` icon,

* Printing the document, using the :guilabel:`Print` icon,

* Printing the technical workflow by using the Gears (or :guilabel:`Print Workflow`) icon.

* Obtaining the documents that an employee needs to carry out the process by clicking the green
  arrow icon,

* Seeing the menu that Open ERP uses to get the document by hovering over the green arrow icon.

.. i18n: Returning to the process diagram, note that you can also get more information
.. i18n: about the transitions between nodes by hovering the mouse cursor over a
.. i18n: transition:

Returning to the process diagram, note that you can also get more information
about the transitions between nodes by hovering the mouse cursor over a
transition:

.. i18n: * A description of the transition,
.. i18n: 
.. i18n: * A list of the roles that can carry out the transition,
.. i18n: 
.. i18n: * The actions available to you from the state.

* A description of the transition,

* A list of the roles that can carry out the transition,

* The actions available to you from the state.

.. i18n: .. figure:: images/process_transition_zoom.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Detail of a transition in the process*

.. figure:: images/process_transition_zoom.png
   :scale: 75
   :align: center

   *Detail of a transition in the process*

.. i18n: Confirm quotation SO001 by clicking on the icon of a person beside the
.. i18n: maroon-colored transition that takes the document from quotation to order.
.. i18n: Then click the :guilabel:`Confirm` button. The process automatically moves on to the next
.. i18n: state and updates its references to some new delivery reservations that you've
.. i18n: just created (see the third tab :guilabel:`History` for a reference to the Packing List
.. i18n: PACK13).

Confirm quotation SO001 by clicking on the icon of a person beside the
maroon-colored transition that takes the document from quotation to order.
Then click the :guilabel:`Confirm` button. The process automatically moves on to the next
state and updates its references to some new delivery reservations that you've
just created (see the third tab :guilabel:`History` for a reference to the Packing List
PACK13).

.. i18n: This dynamic response is extremely useful for learning about the software. It
.. i18n: gives you a high-level view of the different actions carried out and their
.. i18n: results.

This dynamic response is extremely useful for learning about the software. It
gives you a high-level view of the different actions carried out and their
results.

.. i18n: .. figure:: images/process_sale_flow.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *The process after confirming a process into an order*

.. figure:: images/process_sale_flow.png
   :scale: 75
   :align: center

   *The process after confirming a process into an order*

.. i18n: During order processing, the salesperson can quickly:

During order processing, the salesperson can quickly:

.. i18n: * Print the corresponding delivery note,
.. i18n: 
.. i18n: * Zoom into the invoice to see payment details,
.. i18n: 
.. i18n: * Get examples of the necessary documents (such as quotation types, export documents, and fax
.. i18n:   to confirm the order with the customer).

* Print the corresponding delivery note,

* Zoom into the invoice to see payment details,

* Get examples of the necessary documents (such as quotation types, export documents, and fax
  to confirm the order with the customer).

.. i18n: Create a draft invoice by starting the next step on your own.

Create a draft invoice by starting the next step on your own.

.. i18n: It should be clear that this system of user processes gives you great
.. i18n: visibility of the company's overall functions. Each process individually
.. i18n: reflects the specific situation of the company and its documents.

It should be clear that this system of user processes gives you great
visibility of the company's overall functions. Each process individually
reflects the specific situation of the company and its documents.

.. i18n: .. index::
.. i18n:    single: process; new employee

.. index::
   single: process; new employee

.. i18n: New employee induction
.. i18n: -----------------------

New employee induction
-----------------------

.. i18n: Open the employee form for Fabien Pinckaers from the menu
.. i18n: :menuselection:`Human Resources --> Employees --> All Employees`.
.. i18n: Click the :guilabel:`Process` button to open the detailed
.. i18n: process of engagement.

Open the employee form for Fabien Pinckaers from the menu
:menuselection:`Human Resources --> Employees --> All Employees`.
Click the :guilabel:`Process` button to open the detailed
process of engagement.

.. i18n: .. figure:: images/process_employee_flow.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Example of a process engaging a new employee*

.. figure:: images/process_employee_flow.png
   :scale: 75
   :align: center

   *Example of a process engaging a new employee*

.. i18n: You can immediately see things that might interest the HR manager. On a single
.. i18n: screen she has all of the documents about the selected employee. She can then
.. i18n: zoom into each document to look at employee holidays, associated documents, or
.. i18n: the user account in the system.

You can immediately see things that might interest the HR manager. On a single
screen she has all of the documents about the selected employee. She can then
zoom into each document to look at employee holidays, associated documents, or
the user account in the system.

.. i18n: It's also a great help for day-to-day management. When a new employee is
.. i18n: engaged, an HR manager - or anyone else with a suitable role - can complete each
.. i18n: node in the corresponding process, such as:

It's also a great help for day-to-day management. When a new employee is
engaged, an HR manager - or anyone else with a suitable role - can complete each
node in the corresponding process, such as:

.. i18n: * Entering his address,
.. i18n: 
.. i18n: * Creating his user account in the system,
.. i18n: 
.. i18n: * Sending any mandatory employment documents to the relevant government departments,
.. i18n: 
.. i18n: * Declaring the required insurance documents,
.. i18n: 
.. i18n: * Setting meal preferences, perhaps,
.. i18n: 
.. i18n: * Entering statutory public holidays into the system.

* Entering his address,

* Creating his user account in the system,

* Sending any mandatory employment documents to the relevant government departments,

* Declaring the required insurance documents,

* Setting meal preferences, perhaps,

* Entering statutory public holidays into the system.

.. i18n: You can click on each node to open the corresponding form in Open ERP. Some
.. i18n: actions aren't owned by Open ERP, such as contacts with government offices and
.. i18n: insurance companies. In this case click on the document icon to get the
.. i18n: documents to be completed and posted or faxed to the institutions:

You can click on each node to open the corresponding form in Open ERP. Some
actions aren't owned by Open ERP, such as contacts with government offices and
insurance companies. In this case click on the document icon to get the
documents to be completed and posted or faxed to the institutions:

.. i18n: * Fax for insurance declarations,
.. i18n: 
.. i18n: * Statutary forms for government departments.

* Fax for insurance declarations,

* Statutary forms for government departments.

.. i18n: .. figure:: images/process_document.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Example of a process required for the declarations for a new employee*

.. figure:: images/process_document.png
   :scale: 75
   :align: center

   *Example of a process required for the declarations for a new employee*

.. i18n: The system of *Corporate Intelligence* gives you a complete overview of all the
.. i18n: company's processes. So if you click on the node to the left it will start the
.. i18n: recruitment process of selecting and interviewing new employees if the
.. i18n: necessary modules have been installed.

The system of *Corporate Intelligence* gives you a complete overview of all the
company's processes. So if you click on the node to the left it will start the
recruitment process of selecting and interviewing new employees if the
necessary modules have been installed.

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
