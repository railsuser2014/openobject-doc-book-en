
.. i18n: .. index::
.. i18n:    single: workflow
.. i18n:    single: process

.. index::
   single: workflow
   single: process

.. i18n: Configuring workflows and processes
.. i18n: ===================================

Configuring workflows and processes
===================================

.. i18n: Workflows represent the company's different document flows. They're completely configurable and
.. i18n: define the path that any individual Open ERP object (such as an order) must follow depending on the conditions
.. i18n: (for example an order over a certain value must be approved by a sales director, otherwise by any
.. i18n: sales person, before the delivery can be triggered).

Workflows represent the company's different document flows. They're completely configurable and
define the path that any individual Open ERP object (such as an order) must follow depending on the conditions
(for example an order over a certain value must be approved by a sales director, otherwise by any
sales person, before the delivery can be triggered).

.. i18n: The figure :ref:`fig-sflow` shows the standard workflow for an order. You can show it from the GTK client
.. i18n: starting with :menuselection:`Sales Management --> Sales Order --> All Sales Order`. Select an
.. i18n: order, then go to the top menu :menuselection:`Plugins --> Execute a plugin --> Print Workflow` to
.. i18n: show the menu below. 

The figure :ref:`fig-sflow` shows the standard workflow for an order. You can show it from the GTK client
starting with :menuselection:`Sales Management --> Sales Order --> All Sales Order`. Select an
order, then go to the top menu :menuselection:`Plugins --> Execute a plugin --> Print Workflow` to
show the menu below. 

.. i18n: In the web client you can reach a workflow from the associated cross-company process
.. i18n: (the process itself is reached by going to the sales document and then clicking the 
.. i18n: :guilabel:`Process` button above it), 
.. i18n: Chapter :ref:`ch-process` provides all of the information
.. i18n: needed to create and modify technical workflows and cross-company processes.

In the web client you can reach a workflow from the associated cross-company process
(the process itself is reached by going to the sales document and then clicking the 
:guilabel:`Process` button above it), 
Chapter :ref:`ch-process` provides all of the information
needed to create and modify technical workflows and cross-company processes.

.. i18n: .. _fig-sflow:
.. i18n: 
.. i18n: .. figure::  images/sales_workflow.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Workflow for order SO005*

.. _fig-sflow:

.. figure::  images/sales_workflow.png
   :scale: 75
   :align: center

   *Workflow for order SO005*

.. i18n: .. index::
.. i18n:    single: workflow; role

.. index::
   single: workflow; role

.. i18n: Assigning roles
.. i18n: ---------------

Assigning roles
---------------

.. i18n: Users can be linked to several roles specifying their duties in certain phases of different
.. i18n: workflows accompanying the various documents. For example, if a user has taken the role of services
.. i18n: manager he takes on the task of approving holiday requests from his staff. So his role will be
.. i18n: integrated in the holiday request workflow.

Users can be linked to several roles specifying their duties in certain phases of different
workflows accompanying the various documents. For example, if a user has taken the role of services
manager he takes on the task of approving holiday requests from his staff. So his role will be
integrated in the holiday request workflow.

.. i18n: Role definition is done in :menuselection:`Administration --> Users --> Roles Structure -->
.. i18n: Roles`, the same way you define groups, except that roles can be hierarchical: a parent role has the
.. i18n: same influence as all of its child roles (for example, the sales director would be able to do all of
.. i18n: the things that have been defined for a sales person, as well as anything defined specifically for
.. i18n: the sales director group, if the sales director has been made a parent of the sales group).

Role definition is done in :menuselection:`Administration --> Users --> Roles Structure -->
Roles`, the same way you define groups, except that roles can be hierarchical: a parent role has the
same influence as all of its child roles (for example, the sales director would be able to do all of
the things that have been defined for a sales person, as well as anything defined specifically for
the sales director group, if the sales director has been made a parent of the sales group).

.. i18n: Once the roles have been defined, you can add them into the workflow transitions using the
.. i18n: :guilabel:`Role` field. This means that users who have the required role can make the transitions in
.. i18n: the workflow, which enable them to pass from one activity to another (for example confirming an
.. i18n: order or an invoice).

Once the roles have been defined, you can add them into the workflow transitions using the
:guilabel:`Role` field. This means that users who have the required role can make the transitions in
the workflow, which enable them to pass from one activity to another (for example confirming an
order or an invoice).

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
