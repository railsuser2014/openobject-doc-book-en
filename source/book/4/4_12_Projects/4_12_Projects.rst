

Internal organization and project management
#############################################

Summary

* Project Management

* The art of productivity without stress

Keywords

* project

* task

* role

* plan

* delegation

* organization

* productivity

* GTD

 *If you have good systems for managing tasks, then your whole company will benefit. Open ERP's project management modules enable you to manage and track tasks efficiently, work on them effectively, delegate them quickly, and track the delegated tasks closely. Open ERP also helps handle staff's personal time in the organization, and this chapter proposes a methodology aimed at improving the productivity of executives.* 

Project management
===================

In the previous chapter you dealt with the financial management of projects, which was based on Open ERP's analytic accounts, structured into cases. This way of working enables you to analyze time plans and budgets, to control invoicing, and to manage your different contracts.

In this chapter you can use operational project management to organize tasks and plan the work you need to get the tasks completed. All of the necessary operations are carried out through the menu  *Project Management* 

.. tip::   **Terminology**  *Project* 

	In Open ERP a project is represented by a set of tasks for completion. Projects have a tree structure that can be divided into phases and sub-phases. This structure is very useful for work organization

	Whereas analytic accounts look at the past activities of the company, project management's role is to plan the future. Even when there's a close link between the two (such as where a project has been planned and then completed through Open ERP) they are still two different concepts, each making its own contribution to a flexible workflow.

Most client projects are represented by:

* one or several analytic accounts in the accounts system for tracking the contract and its different phases,

* one or several projects in project management for tracking the project and the different tasks to be completed.

Defining a project and its tasks
---------------------------------

To define a new project, go to the menu  *Project Management > Configuration > Projects*  and click  *New* .

 *Project Management > All projects* 

By checking the box  *Warn manager* , you configure the system to send the project manager an Open ERP request every time that a task is closed.

The status of a project can take the following values:

* \ ``Open``\  : while the project is being carried out,

* \ ``Pending``\  : while the project is paused,

* \ ``Canceled``\  : if the project has been canceled and therefore aborted,

* \ ``Done``\  : the project has been successfully completed.

 *Partner Info* 

If you check the box  *Warn customer* , you should define a page header and footer in that same tab for use in an email. Open ERP then prepares an email that the user can send to the client each time that a task is completed. The contents of this email are based on details of the project task, and can be modified by the user before the email is sent. 

.. tip::   **Note**  *Study of client satisfaction* 

	Some companies run a system where emails are automatically sent at the end of a task requesting the client to complete an online survey. This survey enables them to ask different questions about the work carried out, to gauge client satisfaction as the project progresses.

	This function can be used by companies certified to ISO 9001, to rate client satisfaction.

Once a project has been defined you can code in the tasks to be done. You've two possibilities for this:

*  *Tasks* 

* from the menu  *Project Management > All Tasks* , create a new task and assign it to an existing project.

Managing tasks
---------------

Each task contains one of the following statuses, depending on the state:

* \ ``Draft``\  : the task has been entered but hasn't yet been validated by the person who will have to do it,

* \ ``Open``\  

* \ ``Closed``\  

* \ ``Cancelled``\  

* \ ``Pending``\  

A task can be assigned to a user, who then becomes responsible for closing it. But you could also leave it unassigned so that nobody specific will be responsible: various team members instead are made jointly responsible for taking on tasks that they have the skills for.


	.. image::  images/service_task.png
	   :align: center

*Tasks in project management*

Each user then manages his or her own task using the different available menus. To open the list of unclosed tasks that you have been assigned specifically use the menu  *Project Management > My Tasks > My Open Tasks* . Or to open the unassigned tasks, go to  *Project Management > All Tasks > Unassigned Tasks*  and then select \ ``Draft``\   and \ ``Open``\   tasks from that list.

.. tip::   **Advice**  *Shortcuts* 

	Every user should create a link in their own shortcuts to the My Open Tasks menu because they'll have to consult this menu several times a day.

 *Task Work*  *Effective hours* 

.. tip::   **Note**  *Tasks and timesheet* 

	The module hr_timesheet_project gives you a way of creating the day's timesheet automatically from the effective work done for each of the different tasks. This way you don't have to encode service times twice – once for the project task and once for the timesheet.

	When you want to complete your timesheet, use the menu Human Resources > Timesheets > My Timesheets > Import projects.

Assigning roles: account manager and project manager
-----------------------------------------------------

In some companies two distinct responsibilities are defined for each important project:

* someone responsible for the client,

* someone responsible for manging the project technically.

The person responsible for the client, the client account manager, approves client requests, writes sales proposals, and assures that these activities and the invoicing progress properly. He is responsible for the functional definition of the client's needs. The account manager would have a sales, technical sales or financial profile.

The person responsible for the technical tracking of the project is called the project manager. She makes the project happen, organizing and sub-contracting the different project tasks. The project manager would often be responsible for a development team to carry the project out, and generally has a technical profile.

 *Account Manager*  *Project manager*  *Partner Info* 

If you don't make any such distinction in the roles then put the same person in both fields.

Invoicing tasks
-----------------

Several methods of invoicing have already been reviewed:

* invoicing from a sales order,

* invoicing on the basis of analytic costs (service times, expenses),

* invoicing on the basis of deliveries,

* manual invoicing.

Yet another method exists, however: invoicing the client from tasks as they're closed.

 *Pricelist*  *Price setting mode* 

To do this, first configure the project with a Pricelist whose details will be printed out on the invoice. The different modes of invoicing in the field Price setting mode are

*  *By project* 

*  *By hour* 

*  *By effective hour* : an hourly rate is established, and Open ERP uses the field  *Effective hours*  to create the invoice amount when the task is completed.

The partner to be invoiced should be specified in the project definition. But if you have a multi-client project you can code a different client in each individual task. This means that you can set up generic Support projects and invoice each task to a different client.

 *Project Management > All Tasks > Billable Tasks*  *Bill tasks* 

To be invoiced, the task must have been marked as such. Check the box  *To be invoiced*  in the tab  *Other info*  in the task definition form.

.. tip::   **Note**  *Invoicing by project (TODO)* 

	If your invoicing is based on tasks at an agreed rate for each project, you can specify tasks at the start of a project or a phase. Then for each phase in a project that is to be invoiced you create a task receipt or delivery note.

	When the task has been closed the account manager can automatically invoice all the projects or project phases showing on the list of tasks to invoice.

Although invoicing tasks might appear useful in certain situations, it's best to invoice from the service or purchase orders instead. These methods of invoicing are more flexible, with various pricing levels set out in the pricelist, and different products that can be invoiced. And it's helpful to limit the number of invoicing methods in your company by extending the use of an invoicing method that you already have.

If you want to connect your Sales Order with Project Management tasks you should create such products as \ ``Consultant``\  , and \ ``Senior Developer``\  . These products should be configured with  *Product Type* \ ``Service``\  , a  *Procurement Method*  of \ ``Make to Order``\  , and a  *Supply Method*  (on the second tab,  *Procurement* ) of \ ``Produce``\  . Once you've set this up, Open ERP automatically creates a task in the project management when the order is approved.

You can also change some of the order parameters, which affects the invoice:

*  *Shipping Policy* : \ ``Payment before delivery``\   or \ ``Invoice automatically after delivery``\   (at the closure of the task),

*  *Invoice On: * \ ``Ordered Quantities``\   or \ ``Delivered quantities``\   (effective hours in the task).

Planning and managing priorities
---------------------------------

Several methods can be used for ordering tasks by their respective priorities. Open ERP orders tasks based on a function of the following fields:  *Sequence* ,  *Priority*  and  *Deadline* .

Use the  *Sequence*  field on the second tab,  *Other Information* , to plan a project made up of several tasks. In the case of an IT project, for example, where development tasks are done in a given order, the first task to do will be sequence number 1, then numbers 2, 3, 4 and so on. When you first open the list of project tasks, they're listed in their sequence order.

 *Priority*  *Very low*  *Low*  *Medium*  *Urgent*  *Very Urgent* 

 *Deadline* 

You can use one of these three ordering methods, or combine several of them, depending on the project.

.. tip::   **A step further**  *Agile methods* 

	Open ERP implements the agile methodology Scrum for IT development projects in the scrum module.

	Scrum completes the task system by adding the following concepts: long-term planning, sprints, iterative development, progress meetings, burndown chart, and product backlog.

	Look at the site: http://controlchaos.com for more information on the Scrum methodology.


	.. image::  images/service_project_gantt.png
	   :align: center

*Gantt plan, calculated for earliest delivery*

You can set an attendance grid (or the timesheets) in the project file. If you don't specify anything, Open ERP assumes by default that you work 8 hours a day from Monday to Sunday. Once a grid is specified you can call up a project Gantt chart using the Print button. The system then calculates a project plan for earliest delivery using task ordering and the attendance grid.

.. tip::   **Point**  *Calendar view* 

	Open ERP's web client can give you a calendar view of the different tasks. This is all based on the deadline data and displays only tasks that have a deadline. You can then delete, create or modify tasks using simple drag and drop.

	This view isn't available in Open ERP's GTK client.


	.. image::  images/service_task_calendar.png
	   :align: center

*Calendar view of the system tasks*

Efficient delegation
---------------------

To delegate a task to another user you can just change the person responsible for that task. However the system doesn't help you track tasks that you've delegated, such as monitoring of work done, if you do it this way.


	.. image::  images/service_task_delegate.png
	   :align: center

*Form for delegating a task to another user*

Instead, you can use the button  *Delegate*  on a task from version 4.3.x of Open ERP.

 *Delegate* \ ``Pending``\  

\ ``Pending``\  \ ``Open``\  

The system enables you to modify tasks at all levels in the chain of delegation, to add additional information. A task can therefore start as a global objective and become more detailed as it is delegated down in the hierarchy.

The second tab on the task form gives you a complete history of the chain of delegation for each task. You can find a link to the parent task there, and the different tasks that have been delegated.

The art of productivity without stress
=======================================

Now take a slight detour away from pure enterprise management by looking at some tools offered by Open ERP to improve your own personal time management. It's not much of a detour because good organization is the key to better productivity in your daily work.

\ ``project_gtd``\  

* Getting Things Done – The Art of Stress-Free Productivity, by David Allen (2001), most often referred to by its initials GTD (trademark registered since 2005). This book is built around the principle that people should clearly write down all their outstanding tasks and store the details about these tasks in a trustworthy system. They then don't have to worry about holding all of this stuff in their head. Since they can be quite sure that it's recorded safely, they can allow themselves to relax and so have the energy and time to concentrate on handling the tasks themselves systematically. 

.. tip::   **References**  *Efficiently managing time* 

David Allen, Getting Things Done, Penguin Books, New York, 2001, 267 pages. (ISBN : 978-0142000281). Also see the site: http://davidco.com

	Stephen R. Covey, The 7 Habits of Highly Effective People, Free Press, 1989, 15th Anniversary Edition : 2004, 384 pages. (ISBN : 978-0743269513).

.. tip::   **Note**  *De-stress yourself !* 

	Clear the tasks that clutter your thoughts by registering them in an organized system. This immediately helps you to de-stress yourself and organize your work in the best possible way.

	If you feel stressed by too much work, do the following exercise to convince yourself about the benefits. Take some sheets of blank paper and write down everything that passes through your head about the things you need to do. For each task, note the next action to do on an adjacent line, and rank it by the date that you'll commit yourself to doing it.

	At the end of the exercise you'll feel better organized, considerably de-stressed and remarkably free of worries !

* The 7 Habits of Highly Effective People

Our objective in this detour is not to detail the whole methodology but to describe the supporting tools provided by Open ERP's \ ``project_gtd``\   module.

Not everything that is urgent is necessarily important
-------------------------------------------------------

The first modification brought to the basic Open ERP system by the module is a separation of the concepts of urgency and importance. Tasks are no longer classified by a single criterion but by the product of the two criteria, enabling you to prioritize matters that are both urgent and important in a single list

Many managers with a heavy workload use urgency as their sole method of prioritization. The difficulty is then in working out how to plan for substantive tasks (like medium term objectives). These aren't urgent but are nevertheless very important.

	.. note::  *Example Distinction between urgency and importance* 

			If you're very well organized, urgent tasks can (and should often) be given lower precedence than important tasks. Take an example from daily life as an illustration: the case of having some time with your children.

			For most people this task is important. But if you have a busy professional life, the days and weeks flow on with endless urgent tasks to be resolved. Even if you manage your time well, you could let several months pass without spending time with your children because the task of seeing them is never as urgent as your other work, despite its importance.

In Open ERP urgency is given by the  *Deadline*  of the task and importance by the  *Priority* . The classification of the tasks then results from the product of the two factors. The most important tasks and the most urgent both appear at the top of the list.

Organizing your life systematically
-------------------------------------

A methodology of organizing yourself using the concepts of context and timebox is presented in this section.

Context
^^^^^^^^^

The context is determined by the work environment you must be in to deal with certain tasks. For example you could define the following contexts:

*  *Office* : for tasks which have to be dealt with at your workplace (such as telephone a customer, or write a document).

*  *House* : for tasks which have to happen at your private address (such as finding a cleaning contractor, or mowing the lawn).

*  *On the move* : for tasks that you need to do on the move (such as going shopping, or going to the post office).

*  *Traveling* : for tasks that you can handle on the plane or in the train while you're doing traveling on business (tasks such as writing an article, or analyzing a new product). 

An employee / system user can create his or her own contexts using the menu  *Project Management > Configuration > Time Management > Contexts* .

Timebox
^^^^^^^^^

You then have to define the timeboxes. You have to complete the tasks in the time interval specified by a timebox. You usually define timeboxes with the following periods:

*  *Day* : for tasks which must be handled today,

*  *Week* : for tasks that have to be dealt with this week,

*  *Month* : for tasks which have to be completed within the month,

*  *Long term* : for tasks that can be dealt with in more than one month.

A task can be put in one and only one timebox at a time. 

You should distinguish between a timebox and the deadline for completing a task because the deadline is usually fixed by the requirements of the project manager. A timebox, by contrast, is selected with reference to what an individual can do.

To define timeboxes for your company, use the menu  *Project Management > Configuration > Time Management > Timeboxes > My timeboxes* .

Methodology and iterative process
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To organize your tasks efficiently, Open ERP uses a method based on the following systematic and iterative process:

	.. note::  *Method Iterative Process* 

		#. Identify all the tasks that you have to deal with, including everything that keeps you awake at night, and enter them in your Inbox, which you'll find in the menu Project Management > Time Management > Inbox.

		#. Classify the tasks in your Inbox periodically, assigning them a context and a timebox. This indicates both when and where the task should be handled. If a task takes less than 10 minutes then maybe it could be handled immediately.

		#. Every day, carry out the following process:

			* First thing in the morning, select those tasks contained in the current week's timebox that you want to deal with today. These are presented in order of importance and urgency, so you should select the tasks closest to the top of the list.

			* Carry out each task, that's to say either work on the task yourself or delegate it to another user,

			* Last thing at the end of the day's work, empty that day's timebox and return all unclosed tasks into the week's timebox.

		#. Repeat the same process each week and each month for the respective timeboxes.

.. tip::   **Don't confuse**  **  *Agenda*  *and timebox* 

	The idea of timebox is independent from that of an agenda. Certain tasks, such as meetings, must be done on a precise date. So they can't be managed by the timebox system but by an agenda.

	The ideal is to put the minimum of things on the agenda and to put only tasks there that have a fixed date. The timebox system is more flexible and more efficient for dealing with multiple tasks.

So start by entering all the tasks required by project management. These could have been entered by another user and assigned to you. It's important to code in all of the tasks that are buzzing around in your head, just to get them off your mind. A task could be:

* work to be done,

* a short objective, medium or long term,

* a complex project that hasn't yet been broken into tasks.

A project or an objective over several days can be summarized in a single task. You don't have to detail each operation if the actions to be done are sufficiently clear to you.

You have to empty your Inbox periodically. To do that, use the menu  *Project Management > Time Management > My Inbox* . Assign a timebox and a context to each task. This operation shouldn't take more than a few minutes because you aren't dealing with the tasks themselves, just classifying them.


	.. image::  images/service_timebox_day.png
	   :align: center

*Timebox for tasks to be done today*

 *Project Management > Time Management > My timebox for the day* 

Then click on the button at the top right:  *Plan the timebox* . This procedure lets you select the tasks for the day from those in the timebox for the week. This operation gives you an overview of the medium term tasks and objectives and makes you review them there at least once a day. It's then that you'd decide to allocate a part of your time that day to certain tasks based on your priorities.

Since the tasks are sorted by priority, it's sufficient to take the first from the list, up to the number of hours in your day. That'll only take a minute, because the selection isn't taken from every task you know about in the future, but just from those selected for the current week. 

Once the timebox has been completed you can start your daily work on the tasks. For each task you can start work on it, delegate it, close it, or cancel it.

At the end of the day you empty the timebox using the button at the top right. All the tasks that haven't been done are sent back to the weekly timebox to sit in amongst the tasks that will be planned next morning.

Do the same each week and each month using the same principles, but just using the appropriate timeboxes for those periods.

Shortcuts to the right of the timebox help you use the system efficiently with:

* a direct link to the Inbox,

* the list of all of your open tasks,

* the list of your waiting tasks,

* your deadlines,

* a link to all of the tasks in the timebox.

Some convincing results
^^^^^^^^^^^^^^^^^^^^^^^^^

After a few days of carefully practicing this method, users have reported the following improvements:

* a reduction in the number of tasks and objectives that were forgotten,

* a reduction in stress because people felt more in control of their situation,

* a change of the priorities in the types of tasks carried out daily,

* more notice taken of the urgency and importance of tasks and objectives in the long-term organization of time,

* better management of task delegation and the selection of which tasks were better to delegate,


Finally, it's important to note this system is totally integrated with Open ERP's project management function. Staff can use the system or not depending on their own needs. The system is complementary to the project management function that handles team organization and company-wide planning.



.. Copyright © Open Object Press. All rights reserved.

.. You may take electronic copy of this publication and distribute it if you don't
.. change the content. You can also print a copy to be read by yourself only.

.. We have contracts with different publishers in different countries to sell and
.. distribute paper or electronic based versions of this book (translated or not)
.. in bookstores. This helps to distribute and promote the Open ERP product. It
.. also helps us to create incentives to pay contributors and authors using author
.. rights of these sales.

.. Due to this, grants to translate, modify or sell this book are strictly
.. forbidden, unless Tiny SPRL (representing Open Object Presses) gives you a
.. written authorisation for this.

.. Many of the designations used by manufacturers and suppliers to distinguish their
.. products are claimed as trademarks. Where those designations appear in this book,
.. and Open ERP Press was aware of a trademark claim, the designations have been
.. printed in initial capitals.

.. While every precaution has been taken in the preparation of this book, the publisher
.. and the authors assume no responsibility for errors or omissions, or for damages
.. resulting from the use of the information contained herein.

.. Published by Open ERP Press, Grand Rosière, Belgium

