.. index::
   single: workflow
   single: process

Configuring workflows and processes
===================================

Workflows represent the company's different document flows. They're completely configurable and
define the path that any individual Open ERP object (such as an order) must follow depending on the conditions
(for example an order over a certain value must be approved by a sales director, otherwise by any
sales person, before the delivery can be triggered).

The figure :ref:`fig-sflow` shows the standard workflow for an order. You can show it from the GTK client
starting with :menuselection:`Sales Management --> Sales Order --> All Sales Order`. Select an
order, then go to the top menu :menuselection:`Plugins --> Execute a plugin --> Print Workflow` to
show the menu below. 

In the web client you can reach a workflow from the associated cross-company process
(the process itself is reached by going to the sales document and then clicking the 
:guilabel:`Process` button above it), 
Chapter :ref:`ch-process` provides all of the information
needed to create and modify technical workflows and cross-company processes.

.. _fig-sflow:

.. figure::  images/sales_workflow.png
   :scale: 75
   :align: center

   *Workflow for order SO005*

.. index::
   single: workflow; role

Assigning roles
---------------

Users can be linked to several roles specifying their duties in certain phases of different
workflows accompanying the various documents. For example, if a user has taken the role of services
manager he takes on the task of approving holiday requests from his staff. So his role will be
integrated in the holiday request workflow.

Role definition is done in :menuselection:`Administration --> Users --> Roles Structure -->
Roles`, the same way you define groups, except that roles can be hierarchical: a parent role has the
same influence as all of its child roles (for example, the sales director would be able to do all of
the things that have been defined for a sales person, as well as anything defined specifically for
the sales director group, if the sales director has been made a parent of the sales group).

Once the roles have been defined, you can add them into the workflow transitions using the
:guilabel:`Role` field. This means that users who have the required role can make the transitions in
the workflow, which enable them to pass from one activity to another (for example confirming an
order or an invoice).

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
