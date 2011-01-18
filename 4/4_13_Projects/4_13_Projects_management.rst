
Project Management
==================

In the previous chapter you dealt with the financial management of projects, which was based on
OpenERP's analytic accounts, structured into cases. This way of working enables you to analyze
time plans and budgets, to control invoicing, and to manage your different contracts.

In this chapter you can use operational project management to organize tasks and plan the work you
need to get the tasks completed. All of the necessary operations are carried out through the menu
:menuselection:`Project`.

.. index::
   single: project

.. note:: Project

	In OpenERP a project is represented by a set of tasks for completion.
	Projects have a tree structure that can be divided into phases and sub-phases.
	This structure is very useful to organise your work.

	Whereas analytic accounts look at the past activities of the company, project management's role is
	to plan the future.
	Even when there is a close link between the two (such as where a project has been planned and then
	completed through OpenERP)
	they are still two different concepts, each making its own contribution to a flexible workflow.

Most client projects are represented by:

* one or several analytic accounts in the accounts system for tracking the contract and its
  different phases,

* one or several projects in project management for tracking the project and the different tasks to
  be completed.

Creating Projects and Related Tasks
-----------------------------------

To define a new project, go to the menu :menuselection:`Project --> Project --> Projects`.
Select :guilabel:`New` and give your new project a :guilabel:`Project Name`.

You can put this project into a hierarchy, as a child of a :guilabel:`Parent Project`, and
give it a :guilabel:`Project Manager`.
You can also give it a general duration by completing :guilabel:`Start Date` and
:guilabel:`End Date`.

By checking the box :guilabel:`Warn Manager`, you configure the system to send the project manager
an Open ERP request every time that a task is closed.
You can also link to a :guilabel:`Working Time` category.
And you add :guilabel:`Members` as you need.

.. note:: Warn Partner setup

   If you check :guilabel:`Warn Partner`, you should define a page header and footer in the
   :guilabel:`Billing` tab for use in an email.
   Open ERP prepares an email that the user can send to the client
   each time that a task is completed. The contents of this email are based on details of the project
   task, and can be modified by the user before the email is sent.

The status of a project can take the following values:

* \ ``Open``\  : while the project is being carried out,

* \ ``Pending``\  : while the project is paused,

* \ ``Cancelled``\  : if the project has been cancelled and therefore aborted,

* \ ``Closed``\  : the project has been successfully completed.

.. note:: Study of client satisfaction

	Some companies run a system where emails are automatically sent at the end of a task requesting the
	client to complete an online survey.
	This survey enables them to ask different questions about the work carried out, to gauge client
	satisfaction as the project progresses.

	This function can be used by companies certified to ISO 9001, to rate client satisfaction.

Once a project has been defined you can code in the tasks to be done. You have two possibilities for
this:

* from the :guilabel:`ACTION` link button :guilabel:`Tasks` to the right of the project form, then select :guilabel:`New`,

* from the menu :menuselection:`Project --> Project --> Tasks`, create a new task and assign it
  to an existing project.

Managing tasks
--------------

Each task must adopt one of the following states:

* \ ``Draft``\  : the task has been entered but has not yet been validated by the person who will
  have to do it,

* \ ``Open``\

* \ ``Closed``\

* \ ``Cancelled``\

* \ ``Pending``\

A task can be assigned to a user, who then becomes responsible for closing it. But you could also
leave it unassigned so that nobody specific will be responsible: various team members instead are
made jointly responsible for taking on tasks that they have the skills for.

.. figure::  images/service_task.png
   :scale: 50
   :align: center

   *Tasks in project management*

Each user then manages his or her own task using the different available menus. To open the list of
unclosed tasks that you have been assigned specifically use the menu :menuselection:`Project --> Project --> Tasks`. Or to open the unassigned tasks, go to
:menuselection:`Project --> Project --> Tasks` and then click \ ``Clear``\ button
and then \ ``Unassigned``\   button.

.. tip:: Shortcuts

	Every user should create a link in their own shortcuts to the :menuselection:`Tasks` menu because they will
	have to consult this menu several times a day.

.. _sect-projroles:

Assigning Roles
---------------

In some companies two distinct responsibilities are defined for each important project:

* someone responsible for the client,

* someone responsible for managing the project technically.

The person responsible for the client, the client account manager, approves client requests, writes
sales proposals, and assures that these activities and the invoicing progress properly. He is
responsible for the functional definition of the client's needs. The account manager would have a
sales, technical sales or financial profile.

The person responsible for the technical tracking of the project is called the project manager. She
makes the project happen, organizing and sub-contracting the different project tasks. The project
manager would often be responsible for a development team to carry the project out, and generally
has a technical profile.

If you do not make any such distinction in the roles then put the same person in both fields.

.. index::
   single: invoicing; tasks

Invoicing Tasks
---------------

Several methods of invoicing have already been described:

* invoicing from a sales order,

* invoicing on the basis of analytic costs (service times, expenses),

* invoicing on the basis of deliveries,

* manual invoicing.

Although invoicing tasks might appear useful, in certain situations it is best to invoice from the
service or purchase orders instead. These methods of invoicing are more flexible, with various
pricing levels set out in the pricelist, and different products that can be invoiced. And it is
helpful to limit the number of invoicing methods in your company by extending the use of an
invoicing method that you already have.

If you want to connect your Sales Order with Project tasks you should create such
products as \ ``Consultant``\  , and \ ``Senior Developer``\ . These products should be configured
with :guilabel:`Product Type` \ ``Service``\ , a :guilabel:`Procurement Method` of \ ``Make to Order``\  ,
and a :guilabel:`Supply Method` of \ ``Produce``\  . Once you have set this up,
OpenERP automatically creates a task in project management when the order is approved.
You can even take this further by adding a default project to your product. In the Product form, on the `Procurement & Locations` tab, enter the default project to which the automatically created task (from the sales order) should be linked.

You can also change some of the order parameters, which affects the invoice:

*  :guilabel:`Shipping Policy` : \ ``Invoice on Order After Delivery``\ (when the task is closed),

*  :guilabel:`Invoice On` : \ ``Shipped Quantities``\   (actual hours in
   the task).

Create the `Sale Order` using the product :guilabel:`Consultant` with above configuration and confirm this sale order.
You can find the task created from this sale order using the menu :menuselection:`Project --> Project --> Tasks`.
Once you find that task, click on the :guilabel:`Start Task` button in order to start it.  You have to manually assign the
project for this task. When you complete the task enter the information regarding
this in the :guilabel:`Task Work` field. Then click on :guilabel:`Done` button in order to indicate to OpenERP that this task is finished.
As for example the new task `SO008:Create SRS` generated from sale order `SO0008` as shown in following figure.

.. figure::  images/project_task_from_sale_order.png
   :scale: 50
   :align: center

   *Task created from sale order*

After finishing this task go to the menu :menuselection:`Project --> Invoicing --> Invoice Tasks Work` in order to
find the list of uninvoiced task works. You need to configure carefully the analytic account related to this project.
Click on the action :guilabel:`Invoice analytic lines` when you want to create invoice for this task work.

.. figure::  images/project_invoice_from_task_work.png
   :scale: 50
   :align: center

   *Form to create invoice from tasks work*

Priority Management
-------------------

Several methods can be used for ordering tasks by their respective priorities. Open ERP orders
tasks based on a function of the following fields: :guilabel:`Sequence`, :guilabel:`Priority`, and
:guilabel:`Deadline`.

Use the :guilabel:`Sequence` field on the second tab, :guilabel:`Extra Info`, to plan a
project made up of several tasks. In the case of an IT project, for example, where development tasks
are done in a given order, the first task to do will be sequence number 1, then numbers 2, 3, 4 and
so on. When you first open the list of project tasks, they are listed in their sequence order.

You can use one of these three ordering methods, or combine several of them, depending on the
project.

.. index::
   single: module; scrum
   single: agile (method)

.. note:: Agile methods

	Open ERP implements the agile methodology Scrum for IT development projects in the :mod:`project_scrum`
	module.

	Scrum supplements the task system with the following concepts:
	long-term planning, sprints, iterative development, progress meetings, burndown chart, and product
	backlog.

	Look at the site: http://controlchaos.com for more information on the Scrum methodology.

.. figure::  images/service_project_gantt.png
   :scale: 50
   :align: center

   *Gantt plan, calculated for earliest delivery*

You can set the Working Time in the project file. If you do not specify
anything, Open ERP assumes by default that you work 8 hours a day from Monday to Sunday. Once the
time is specified you can call up a project Gantt chart from Tasks. The system then
calculates a project plan for earliest delivery using task ordering and the working time.

.. tip:: Calendar view

	Open ERP can give you a calendar view of the different tasks in both the web client and the GTK client.
	This is all based on the deadline data and displays only tasks that have a deadline.
	You can then delete, create or modify tasks using simple drag and drop (only in web).

	.. figure::  images/service_task_calendar.png
	   :scale: 50
	   :align: center

       *Calendar view of the system tasks*

.. index:: delegation (task)

Delegate your Tasks
-------------------

To delegate a task to another user you can just change the person responsible for that task. However
the system does not help you track tasks that you have delegated, such as monitoring of work done, if
you do it this way.

.. figure::  images/service_task_delegate.png
   :scale: 50
   :align: center

   *Form for delegating a task to another user*

Instead, you can use the button :guilabel:`Delegate` on a task.

.. *Delegate* \ ``Pending``\

.. \ ``Pending``\  \ ``Open``\

The system enables you to modify tasks at all levels in the chain of delegation, to add additional
information. A task can therefore start as a global objective and become more detailed as it is
delegated down in the hierarchy.

The second tab on the task form gives you a complete history of the chain of delegation for each
task. You can find a link to the parent task there, and the different tasks that have been
delegated.


.. Copyright © Open Object Press. All rights reserved.

.. You may take electronic copy of this publication and distribute it if you don't
.. change the content. You can also print a copy to be read by yourself only.

.. We have contracts with different publishers in different countries to sell and
.. distribute paper or electronic based versions of this book (translated or not)
.. in bookstores. This helps to distribute and promote the Open ERP product. It
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


