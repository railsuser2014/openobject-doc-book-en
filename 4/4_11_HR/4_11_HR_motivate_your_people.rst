
.. index::
   single: motivation
..

Inspire your People
===================

A motivated workforce of people can give the best outcome for an organization. OpenERP
can maintain this motivational process by periodical evaluation of employees' performance and
efficient holiday management.

Assessments
-----------

The regular assessments of human resources can benefit your people as well organization.
For efficient periodical evaluation of employees' performance, you need to install the :mod:`hr_evaluation`
module. The configuration wizard to install this module is shown below:

.. figure::  images/config_wiz_evaluation.png
   :scale: 75
   :align: center

   *Configuration wizard to install hr_evaluation module*

To create and manage new evaluations, you can use the menu :menuselection:`Human Resources --> Evaluations --> Evaluations`.

.. figure::  images/employee_evaluation.png
   :scale: 75
   :align: center

   *Employee Evaluation form*

Each employee can be assigned an evaluation plan. These plans define the frequency and the
way you manage your periodic personal evaluation. You will be able to define steps and attach
interview forms to each step. OpenERP manages all kinds of evaluations: bottom-up, top-down,
self evaluation and final evaluation by the manager.

The main features of the evaluation process covered by OpenERP are as follows:

* Ability to create employees evaluation.
* An evaluation can be created by an employee for subordinates, juniors as well
  as his manager.
* The evaluation is done under a plan in which various surveys can be created,
  and which level of employee hierarchy fills what can be defined and
  the final review and evaluation is done by the manager.
* Every evaluation filled by employees can be viewed through a PDF form.
* Interview Requests are generated automatically by OpenERP according to employees
  evaluation plans. Each user receives automatic emails and requests to perform evaluation
  of their colleagues periodically.

You can analyse evaluation data through the menu :menuselection:`Human Resources --> Reporting --> Evaluations Analysis`.

Holiday Management
------------------

You can manage leaves taken by employees using the :mod:`hr_holidays`
module. The configuration wizard to install this module is shown below:

.. figure::  images/config_wiz_holidays.png
   :scale: 75
   :align: center

   *Configuration wizard to install hr_holidays module*

Using the menu :menuselection:`Human Resources --> Holidays --> Leave Requests` an employee can request a leave.

.. figure::  images/employee_leave_request_form.png
   :scale: 75
   :align: center

   *Leave Request form*

Leaves requests can be recorded by employees and validated by their managers.
Once a leave request is validated, it appears automatically in the agenda of the employee.
You can define several allowance types (paid holidays, sickness, etc.) and manage allowances
per type.

OpenERP can provide the following features for efficient holiday management process:

* It helps you to manage leaves and leave requests.
* Synchronisation with an internal agenda (use of :mod:`crm`) is possible:
  in order to automatically create a case when a holiday request is accepted,
  you have to link the holidays status to a case section.
* You can set up colour preferences according to your leave type, for example, `Sick Leave` should be red in reports.
* An employee can request for more days off, by making a new Allocation Request through :menuselection:`Human Resources --> Holidays --> Allocation Requests`.

The statistical report for leaves can be seen using the
:menuselection:`Human Resources --> Reporting --> Holidays --> Leaves Analysis` menu.

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
