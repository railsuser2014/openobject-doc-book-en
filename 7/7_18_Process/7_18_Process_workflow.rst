

.. index:: 
   single: process
   single: workflow

Workflows and User Processes
=============================

Workflows are used to define the behaviour of a given document. They are used
by developers and system implementers to determine which object should execute
which actions and at which moments. These are principally technical processes
defined in a vertical way on the lifecycle of a complete object (represented by
a document). Changing a workflow will have a direct impact on the behaviour of
the software in response to user actions. You handle all possible exceptions
there so that the software is robust.

.. figure:: images/process_sale_workflow.png
   :scale: 75
   :align: center

   *Example of a workflow handling a customer order*

Unlike workflows, user processes represent workflows across all of a company
and its documents. They are used by end users to locate an action for more
complete handling. A change of user process won't have any effect on the
software but will show the user another way of working on a given problem.

.. figure:: images/process_sale_process.png
   :scale: 75
   :align: center

   *Example of a process handling a customer order*

Processes are used by end users to help them understand the problems which
haven't been handled in OpenERP. You can find actions that have no influence
on the software, such as “Telephone customer to thank him”, and “Send a fax to
reassure him”. As well as providing user help, processes provide functions such
as:

* integration with OpenERP help and the company's quality manual,

* showing the user menu for finding a specific document.

.. figure:: images/process_cross_worfklow_process.png
   :scale: 75
   :align: center

   *Relationship between workflow and user process*

User processes are thus connected to technical workflows. If you modify the
software's behaviour with a workflow, the changes will be directly visible in
the user processes that are based on the modified document. So if you add new
required roles for certain transitions on a workflow they will automatically be
shown in the process corresponding to the modified document.

To get maximum benefit from the power of user processes and the workflow
engine, OpenERP provides an integrated workflow editor and user process
editor. This enable you to modify them through the client interface.

You'll only work with the process editor in this chapter. If you want to test the
workflow editor click on the link to the bottom left of a document and select
the menu :menuselection:`Customize --> Manage Workflows`. OpenERP opens a graphical editor to
modify the workflow for the selected document type.

.. figure:: images/process_workflow_editor.png
   :scale: 75
   :align: center

   *Workflow editor modifying the behaviour of invoices*

The workflow editor is only available in OpenERP's web client at the time of writing. 
If you have the GTK client you can use the menus in
:menuselection:`Administration --> Low Level Objects --> Workflow Items`.
These are text-based not graphical.

Using processes effectively
----------------------------

Regardless of which OpenERP screen you're in you can call up a process on the
current document by clicking the :guilabel:`Process` icon. Depending on the document you
can have several processes defined using it, OpenERP then asks you to choose
which one of them you want.

For example if you are in a meeting form, OpenERP will ask you to choose from
the processes it knows about that involve such forms:

* processes for selecting and inducting new employees,

* tracing customer orders in pre-sales,

* processes for visiting customers and handling expenses.

.. figure:: images/process_screen.png
   :scale: 75
   :align: center

   *Button for entering a user process from a form*

The element colored red shows the active process for the selected document.
Elements in grey are the states that the selected document won't go through
because of its configuration. You can use the different icons to open the
document, print it, or get its documentation.

Some states have an image inside of arrows formed into a circle. These show
that the state refers to another process. To go to this other process you can
click on the title of the state. For example you can click on the invoice in
the customer order management workflow to see in detail how that invoice is
handled.

.. figure:: images/process_subflow_icon.png
   :scale: 75
   :align: center

   *A state that refers to another workflow*

Finally, you can place your mouse for a second over a transition (hover over a
transition) to get a help balloon appearing about this transition. OpenERP
then shows you:

* A description of the transition,

* The actions you can take at this step,

* The roles you need to make anything happen from this step.

.. figure:: images/process_transition.png
   :scale: 75
   :align: center

   *Detail of a transition in a workflow*

If you click on the transition, OpenERP opens a dialog box with buttons that
enable you to change the document state. These are the same buttons that you
see on the active document form. They enable you to confirm an order directly
from the process and then see the consequences in real time at a macro level.

.. index::
   single: process; defining

Defining your own user processes
---------------------------------

Use the menus under :menuselection:`Administration --> Customization --> Enterprise Processes` to
define new processes or modify existing processes. When entering a process,
OpenERP shows you the list of states available for that process.

.. figure:: images/process_form.png
   :scale: 75
   :align: center

   *Form for defining a process*

You can add a new state or modify an existing state. A state can be associated
with an object (whose instances are represented by documents). If that is the
case, choose it in the case object. You can set an expression that shows if the
object can be found in that state or not. Expressions are in Python format. For
example for the quotation state choose the object ``sale.order`` and set the
following expression ``object.state == 'draft'`` .

You can also link to a menu so that users can learn which menu to use to access
objects in a state. You can set the conditions in which this object is in a
greyed-out state in the second tab :guilabel:`Conditions`. These expressions, too, are
encoded in Python format.

Once the node has been defined you should set the transitions leaving this
object. For each transition you can:

* Give the leaving and destination states,

* Set up a list of buttons that start various transitions in the process,

* Map between workflow transitions and the document that's selected,

* Put an explanatory notice in different languages.

.. figure:: images/process_transition_form.png
   :scale: 75
   :align: center

   *Screen for defining a process transition*

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
