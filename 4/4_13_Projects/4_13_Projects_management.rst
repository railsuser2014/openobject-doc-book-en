
Project Management
==================

In the previous chapter you learned more about the financial management of projects, based on
OpenERP's analytic accounts, structured into cases. This way of working enables you to analyze
time plans and budgets, to control invoicing and to manage your different contracts.

Here we will explain operational project management to organize tasks and plan the work you
need to get the tasks completed. All the necessary operations are carried out from the
:menuselection:`Project` menu.

.. index::
   single: project

.. note:: Project

	In OpenERP, a project is represented by a set of tasks to be completed.
	Projects have a tree structure that can be divided into phases and sub-phases.
	This structure is very useful to organise your work.

	Whereas analytic accounts look at the past activities of the company, Project Management's role is
	to plan the future.
	Even though there is a close link between the two (such as where a project has been planned and then
	completed through OpenERP) they are still two different concepts, each making its own contribution to a flexible workflow.

Most customer projects are represented by:

* one or several analytic accounts in the Accounting System, to keep track of the contract and its
  different phases,

* one or several projects in Project Management, to track the project and the different tasks to
  be completed.

There is a direct link between the project and the analytic account, because for each new project created, OpenERP will automatically create the corresponding analytic account in the `Projects` analytic chart of accounts. Note that you have no access to the analytic account directly from a project.

Creating Projects and Related Tasks
-----------------------------------

To define a new project, go to the menu :menuselection:`Project --> Project --> Projects`.
Click :guilabel:`Create` and give your new project a :guilabel:`Project Name`.

You can assign a :guilabel:`Project Manager` and assign your project privacy with :guilabel:`Privacy / Visibility`.

The `Other Info` tab displays information about Planned Time and the Time Spent on the project according to the task work completed.
Enter the general duration by completing :guilabel:`End Date`.
You can put this project into a hierarchy, as a child of a :guilabel:`Parent` Analytic Account

In case a project takes too long, it can also be escalated to another project. This feature is available if you have installed the module :mod:`project_issue`, which can be done by selecting :guilabel:`Track issues and bugs` in the :menuselection:`Settings --> Configuration --> Project`. In :guilabel:`Project Escalation`, enter the project that will be used for escalated tasks.
You can also link to a :guilabel:`Working Time` category, which will be used to calculate the Project's time line, i.e. through a Gantt chart.

The status of a project can take the following values:

* \ ``In Progress``\: the project is being carried out,

* \ ``Pending``\: the project is paused,

* \ ``Cancelled``\: the project has been cancelled and therefore aborted,

* \ ``Closed``\: the project has been successfully completed,

* \ ``Template``\: the project can be used as a template to make projects based on this.


On the `Team` tab, add :guilabel:`Project Members` to the project; this is related to access rights too.

.. figure::  images/projects.png
   :scale: 60
   :align: center

   *Projects*

On the project form you find a customer field, which will also be used for invoice creation.
To generate invoices based on time spent on tasks, you need to install :mod:`project_timesheet`.Go to menu 
menu :menuselection:`Settings --> Configuration --> Project`.And in `Task`, tick Record timesheet lines per tasks.
Then Go to the menu :menuselection:`Project --> Invoicing --> Invoice Tasks`.Open its form view click on `More` and `Create Invoices`.

.. note:: Complete the invoicing data, such as Sale Pricelist and Customer on Analytic Account before creating the invoice.

.. note:: Study of Customer Satisfaction

	Some companies run a system where emails are automatically sent at the end of a task requesting the
	customer to complete an online survey.
	This survey enables a company to ask several questions about the work carried out, to gauge customer
	satisfaction as the project progresses.

	This function can also be used by ISO 9001-certified companies, to measure customer satisfaction.
	OpenERP also allows you to create your own surveys. 

The `Project Stages` tab allows you to define stages that help you divide your tasks. You can add a sequence number to set the stage order, allowing you to prioritize your task work, i.e. first you will have the Design stage and then Specification.

Managing Tasks
--------------

Once a project has been defined, you can enter the tasks to be executed. You have two possibilities for this:

* click the button :guilabel:`Tasks` to the right of the project form, then click :guilabel:`Create`,

* from the menu :menuselection:`Project --> Project --> Tasks`, create a new task and assign it
  to an existing project.

Each task has one of the following states:

* \ ``Draft``\: the task has been entered but has not yet been validated by the person who will
  have to do it,

* \ ``In Progress``\: you can start working on the task, hence the task is in progress,

* \ ``Done``\: task is completed,

* \ ``Cancelled``\: task work is no longer required,

* \ ``Pending``\: task is waiting for response of someone else (e.g. customer information).

A task can be assigned to a user, who then becomes responsible for closing it. But you could also
leave it unassigned so that nobody specific will be responsible: various team members instead are
made jointly responsible for working on tasks they have the skills for.

.. figure::  images/service_task.png
   :scale: 50
   :align: center

   *Tasks in Project Management*

Each user manages his or her own task using the various menus available. To open the list of
unclosed tasks that have been specifically assigned to you, go to the menu :menuselection:`Project --> Project --> Tasks`. Or to open the unassigned tasks, go to :menuselection:`Project --> Project --> Tasks` and then \ ``Clear``\ the search
and then click \ ``Unassigned Tasks``\ from search filter.

.. tip:: Shortcuts

	Every user should create a link in their own shortcuts to the :menuselection:`Tasks` menu, because they will
	have to consult this menu several times a day.

The `Delegation` tab allows you to define links between your tasks. From `Parent Tasks` set the tasks that are related to this task. Use this feature to define the order in which tasks need to be accomplished, i.e. task 2 may not be executed before task 1.

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

If you want to connect your Sales Order with Project tasks you should create
products such as \ ``On Site Assistance``\  and \ ``On Site Monitoring``\ . These products should be configured
with :guilabel:`Product Type` \ ``Service``\ , a :guilabel:`Procurement Method` of \ ``Make to Order``\  ,
and a :guilabel:`Supply Method` of \ ``Produce``\. Once you have set this up, OpenERP automatically creates a task in project management When the Quotation will be Converted to Sale Order.
You can even take this further by adding a default project to your product. In the Product form, on the `Information` tab, enter the default project to which the automatically created task (from the sales order) should be linked.

You can also change some of the order parameters, which affects the invoice:

*  :guilabel:`Shipping Policy` : \ ``Invoice on Order After Delivery`` \ (when the task is closed),

*  :guilabel:`Invoice On` : \ ``Shipped Quantities`` \ (actual hours in the task).

Create the `Sales Order` using the product :guilabel:`On Site Assistance` with the above configuration and confirm it.
You can find the task created from this sale order using the menu :menuselection:`Project --> Project --> Tasks`.
Once you find that task, click on the specific stage e.g.:guilabel:`Design`.  You have to manually assign the
project for this task, unless you specified a default project in the Product form. When you complete the task, enter the information in the :guilabel:`Task Work` field. Then click the :guilabel:`Done` button in order to indicate to OpenERP that this task is finished.
As an example, the new task `SO008:On Site Assistance` generated from sales order `SO008` is shown in following figure.

.. figure::  images/project_task_from_sale_order.png
   :scale: 60
   :align: center

   *Task created from Sales Order*

.. tip:: You need to carefully configure the analytic account related to this project. If you use the Billing tab of the project to do this, the analytic account linked to the project will automatically get the related settings.

After finishing this task, go to the menu :menuselection:`Project --> Invoicing --> Invoice Tasks` in order to
find the list of uninvoiced tasks.
Click the action :guilabel:`Create Invoice` from more button, when you want to create an invoice for this task work.

.. figure::  images/project_invoice_from_task_work.png
   :scale: 60
   :align: center

   *Create Invoice for Tasks Work*

Priority Management
-------------------

Several methods can be used for ordering tasks by their respective priorities. OpenERP orders
tasks based on a function of the following fields: :guilabel:`Sequence`, :guilabel:`Priority`, and
:guilabel:`Deadline`.

Use the :guilabel:`Sequence` field on the second tab, :guilabel:`Other Info`, to plan a
project made up of several tasks. In the case of an IT project, for example, where development tasks
are done in a given order, the first task to do will be sequence number 1, then numbers 2, 3, 4 and
so on. When you first open the list of project tasks, they are listed in their sequence order. You can simply drag and drop tasks to change their sequence.

You can use one of these three ordering methods, or combine several of them, depending on the
project.


.. figure::  images/service_project_gantt.png
   :scale: 60
   :align: center

   *Gantt chart, calculated for earliest delivery*

You can set the Working Time in the project file. If you do not specify
anything, OpenERP assumes by default that you work 8 hours a day from Monday to Sunday. Once the
time is specified you can call up a project Gantt chart from Tasks. The system then
calculates a project plan for earliest delivery using task ordering and the working time.

.. tip:: Calendar View

	OpenERP can give you a calendar view of the different tasks.
	This is all based on the deadline data and displays only tasks that have a deadline.
	You can then delete, create or modify tasks using drag and drop (only in web).

	.. figure::  images/service_task_calendar.png
	   :scale: 45
	   :align: center

	*Calendar View of the System Tasks*

.. index:: delegation (task)

Delegate your Tasks
-------------------

To delegate a task to another user, you can just change the person Assigned to for that task. However,
the system does not help you track tasks that you have delegated, such as monitoring of work done, if
you do it this way.

.. figure::  images/service_task_delegate.png
   :scale: 60
   :align: center

   *Form for Delegating a Task to Another User*

Instead, you can use the :guilabel:`Delegate` button on a task.

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


