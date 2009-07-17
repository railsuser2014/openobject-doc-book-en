
.. i18n: .. index::
.. i18n:    single: HR; management
.. i18n:    single: employee

.. index::
   single: HR; management
   single: employee

.. i18n: Managing Human Resources
.. i18n: ========================

Managing Human Resources
========================

.. i18n: To establish a system that's integrated into a company's management you need to start with a
.. i18n: current list of collaborators.

To establish a system that's integrated into a company's management you need to start with a
current list of collaborators.

.. i18n: .. note:: Don't confuse employees and users
.. i18n: 
.. i18n: 	For Open ERP, “employee” represents all of the physical people who have an work contract with
.. i18n: 	the company. This includes all types of contract: contracts with both fixed and indeterminate time
.. i18n: 	periods, and also independent and freelance service contracts.
.. i18n: 	
.. i18n: 	.. index::
.. i18n: 	   single: modules; portal_	
.. i18n: 
.. i18n: 	A “user” is a physical person who's given access to the company's systems. Most employees are
.. i18n: 	users but some users aren't employees: external partners can have access to parts of the system.
.. i18n: 	You can manage them through the :mod:`portal_` modules.

.. note:: Don't confuse employees and users

	For Open ERP, “employee” represents all of the physical people who have an work contract with
	the company. This includes all types of contract: contracts with both fixed and indeterminate time
	periods, and also independent and freelance service contracts.
	
	.. index::
	   single: modules; portal_	

	A “user” is a physical person who's given access to the company's systems. Most employees are
	users but some users aren't employees: external partners can have access to parts of the system.
	You can manage them through the :mod:`portal_` modules.

.. i18n: Here are some examples of functions which depend on the accuracy of the employee list:

Here are some examples of functions which depend on the accuracy of the employee list:

.. i18n: * the cost of a service, which depends on the employee's working contract,
.. i18n: 
.. i18n: * project planning, which depends on the work pattern of the project contributors,
.. i18n: 
.. i18n: * the client billing rate, which probably depends on the employee's job function,
.. i18n: 
.. i18n: * the chain of command, or responsibilities, which is related to the hierarchical structure of the
.. i18n:   company.

* the cost of a service, which depends on the employee's working contract,

* project planning, which depends on the work pattern of the project contributors,

* the client billing rate, which probably depends on the employee's job function,

* the chain of command, or responsibilities, which is related to the hierarchical structure of the
  company.

.. i18n: Management of staff
.. i18n: -------------------

Management of staff
-------------------

.. i18n: To define a new employee in Open ERP, use the menu :menuselection:`Human Resources --> Employees
.. i18n: --> New Employee`.

To define a new employee in Open ERP, use the menu :menuselection:`Human Resources --> Employees
--> New Employee`.

.. i18n: .. figure::  images/service_employee_form.png
.. i18n:    :scale: 50
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Form describing an employee*

.. figure::  images/service_employee_form.png
   :scale: 50
   :align: center

   *Form describing an employee*

.. i18n: Start by entering the employee's name in :guilabel:`Employee` and the company that this employee works for
.. i18n: in :guilabel:`Company`. You can then create a new user of the Open ERP system linked to this
.. i18n: employee by filling in a new :guilabel:`User` form through the :guilabel:`Related User` field. 

Start by entering the employee's name in :guilabel:`Employee` and the company that this employee works for
in :guilabel:`Company`. You can then create a new user of the Open ERP system linked to this
employee by filling in a new :guilabel:`User` form through the :guilabel:`Related User` field. 

.. i18n: Even if the employee isn't a user, it's best if you
.. i18n: create a system access for most of your staff just so that you can control their access rights from
.. i18n: the outset (and you can do that through this field if you need to).

Even if the employee isn't a user, it's best if you
create a system access for most of your staff just so that you can control their access rights from
the outset (and you can do that through this field if you need to).

.. i18n: .. tip:: Employee and User link.
.. i18n: 
.. i18n: 	If the employee has a user account on the system you always link his or her user
.. i18n: 	account to the employee form.
.. i18n: 
.. i18n: 	Creating this link enables automatic completion to be done on the :guilabel:`Employee` field in the
.. i18n: 	relevant forms, such as services and expense records.

.. tip:: Employee and User link.

	If the employee has a user account on the system you always link his or her user
	account to the employee form.

	Creating this link enables automatic completion to be done on the :guilabel:`Employee` field in the
	relevant forms, such as services and expense records.

.. i18n: Then enter the employee's address. 

Then enter the employee's address. 

.. i18n: .. todo:: We need to give better guidance about Partners vs Employees just here.

.. todo:: We need to give better guidance about Partners vs Employees just here.

.. i18n: This appears in the partner contact form in Open ERP. Since
.. i18n: employees are people that have contacts with your company, it's logical that they have entries
.. i18n: like any other partner in your database. So enter the name of the employee as a new partner Name and
.. i18n: the address in the Contact form. Then all of the functions that apply to a partner can also be
.. i18n: applied to an employee. This is particularly useful for tracking debits and credits in
.. i18n: the accounts – so you can track salary payments, for example.

This appears in the partner contact form in Open ERP. Since
employees are people that have contacts with your company, it's logical that they have entries
like any other partner in your database. So enter the name of the employee as a new partner Name and
the address in the Contact form. Then all of the functions that apply to a partner can also be
applied to an employee. This is particularly useful for tracking debits and credits in
the accounts – so you can track salary payments, for example.

.. i18n: You can then set both an analytic journal and a linked product to this employee
.. i18n: in the :guilabel:`Timesheets` tab. If
.. i18n: you do it that way, then this information can be used to track services. For now, just complete the
.. i18n: form with the following information:

You can then set both an analytic journal and a linked product to this employee
in the :guilabel:`Timesheets` tab. If
you do it that way, then this information can be used to track services. For now, just complete the
form with the following information:

.. i18n: *  :guilabel:`Analytic Journal` : usually a ``Timesheet Journal``,
.. i18n: 
.. i18n: *  :guilabel:`Product` : a service product that describes how this employee would be charged out,
.. i18n:    for example as ``Senior Consultant``.

*  :guilabel:`Analytic Journal` : usually a ``Timesheet Journal``,

*  :guilabel:`Product` : a service product that describes how this employee would be charged out,
   for example as ``Senior Consultant``.

.. i18n: Management of employment contracts
.. i18n: ----------------------------------

Management of employment contracts
----------------------------------

.. i18n: If you install the :mod:`hr_contract` module you can link contract details to the employee record.

If you install the :mod:`hr_contract` module you can link contract details to the employee record.

.. i18n: .. figure::  images/service_hr_contract.png
.. i18n:    :scale: 50
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Definition of a working contract for a given employee*

.. figure::  images/service_hr_contract.png
   :scale: 50
   :align: center

   *Definition of a working contract for a given employee*

.. i18n: You can enter information about the employment contract for the employee, such as:

You can enter information about the employment contract for the employee, such as:

.. i18n: *  :guilabel:`Contract Name`
.. i18n: 
.. i18n: *  :guilabel:`Function`
.. i18n: 
.. i18n: *  :guilabel:`Working hours per day`
.. i18n: 
.. i18n: *  :guilabel:`Start Date`
.. i18n: 
.. i18n: *  :guilabel:`End Date`
.. i18n: 
.. i18n: *  :guilabel:`Wage Type` either :guilabel:`Monthly Gross` or :guilabel:`Weekly Net`

*  :guilabel:`Contract Name`

*  :guilabel:`Function`

*  :guilabel:`Working hours per day`

*  :guilabel:`Start Date`

*  :guilabel:`End Date`

*  :guilabel:`Wage Type` either :guilabel:`Monthly Gross` or :guilabel:`Weekly Net`

.. i18n: .. index::
.. i18n:    single: employee; sign in / sign out

.. index::
   single: employee; sign in / sign out

.. i18n: Sign in and out
.. i18n: ---------------

Sign in and out
---------------

.. i18n: In some companies, staff have to sign in when they arrive at work and sign out again at the end of
.. i18n: the day. If each employee has been linked to a system user, then they can sign in on Open ERP by
.. i18n: using the menu :menuselection:`Human Resources --> Attendances --> Sign in / Sign out`.

In some companies, staff have to sign in when they arrive at work and sign out again at the end of
the day. If each employee has been linked to a system user, then they can sign in on Open ERP by
using the menu :menuselection:`Human Resources --> Attendances --> Sign in / Sign out`.

.. i18n: If an employee has forgotten to sign out on leaving, the system proposes that they sign out manually
.. i18n: and type in the time that they left when they come in again the next day. This gives you a simple way
.. i18n: of managing forgotten sign-outs.

If an employee has forgotten to sign out on leaving, the system proposes that they sign out manually
and type in the time that they left when they come in again the next day. This gives you a simple way
of managing forgotten sign-outs.

.. i18n: Find employee attendance details from their forms in 
.. i18n: :menuselection:`Human Resources --> Employees --> All Employees`.

Find employee attendance details from their forms in 
:menuselection:`Human Resources --> Employees --> All Employees`.

.. i18n: To get the detail of attendances from an employee's form in Open ERP you can use the three
.. i18n: available reports:

To get the detail of attendances from an employee's form in Open ERP you can use the three
available reports:

.. i18n: *  :guilabel:`Print Attendance Error Report`
.. i18n: 
.. i18n: *  :guilabel:`Print Timesheet by week`
.. i18n: 
.. i18n: *  :guilabel:`Print Timesheet by month`

*  :guilabel:`Print Attendance Error Report`

*  :guilabel:`Print Timesheet by week`

*  :guilabel:`Print Timesheet by month`

.. i18n: The first report highlights errors in attendance data entry. 
.. i18n: It shows you whether an employee has entered the time of
.. i18n: entry or exit manually and the differences between the actual and expected sign out time and the time.

The first report highlights errors in attendance data entry. 
It shows you whether an employee has entered the time of
entry or exit manually and the differences between the actual and expected sign out time and the time.

.. i18n: The others are reports using the data recorded.

The others are reports using the data recorded.

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
