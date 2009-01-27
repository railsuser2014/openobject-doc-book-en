
Module Human Resources: Holidays management (*hr_holidays*)
===========================================================
:Module: hr_holidays
:Name: Human Resources: Holidays management
:Version: 5.0.1.1
:Directory: hr_holidays
:Web: http://www.openerp.com

Description
-----------

::

  Human Ressources: Holidays tracking and workflow
  
      This module allows you to manage holidays and holidays requests. For each employee, you can also define a number of available holidays per holiday status.
  
      Note that:
      - A synchronisation with an internal agenda (use of the CRM module) is possible: in order to automatically create a case when an holiday request is accepted, you have to link the holidays status to a case section. You can set up this info and your colour preferences in
                  HR \ Configuration \ Holidays Status
      - An employee can make a negative holiday request (holiday request of -2 days for example), this is considered by the system as an ask for more off-days. It will increase his total of that holiday status available (if the request is accepted).
      - There are two ways to print the employee's holidays:
          * The first will allow to choose employees by department and is used by clicking the menu item located in
                  HR \ Holidays Request \ Print Summary of Holidays
          * The second will allow you to choose the holidays report for specific employees. Go on the list
                  HR \ Employees \ Employees
              then select the ones you want to choose, click on the print icon and select the option
                  'Print Summary of Employee's Holidays'
      - The wizard allows you to choose if you want to print either the Confirmed & Validated holidays or only the Validated ones. These states must be set up by a user from the group 'HR' and with the role 'holidays'. You can define these features in the security tab from the user data in
                  Administration \ Users \ Users
              for example, you maybe will do it for the user 'admin'.

Dependencies
------------

 * hr - installed
 * crm_configuration - installed
 * process - installed

Reports
-------

 * Summary Of Holidays

Menus
-------

 * Human Resources/Configuration/Holiday Status
 * Human Resources/Holidays Management
 * Human Resources/Holidays Management/New Holidays Request
 * Human Resources/Holidays Management/All Holidays Requests
 * Human Resources/Holidays Management/My Holidays Requests
 * Human Resources/Holidays Management/My Holidays Requests/My Draft Holidays Requests
 * Human Resources/Holidays Management/My Holidays Requests/My Awaiting Confirmation Holidays Requests
 * Human Resources/Holidays Management/My Holidays Requests/My Validated Holidays Requests
 * Human Resources/Holidays Management/My Holidays Requests/My Refused Holidays Requests
 * Human Resources/Holidays Management/All Holidays Requests/Holidays Requests Awaiting for Validation
 * Human Resources/Configuration/Holidays Per Employee
 * Human Resources/Reporting/My Available Holidays
 * Human Resources/Reporting/Print Summary of Holidays

Views
-----

 * hr.holidays.form (form)
 * hr.holidays.tree (tree)
 * hr.holidays.log.form (form)
 * >hr.holidays.log.tree (tree)
 * hr.holidays.status.form (form)
 * hr.holidays.status.tree (tree)
 * hr.holidays.per.user.form (form)
 * hr.holidays.per.user.tree (tree)
 * hr.holidays.per.user.graph (graph)


Objects
-------

Object: Holidays Status
#######################

.. index::
  single: Holidays Status object
.. 


:active: Active, boolean



.. index::
  single: active field
.. 




:color_name: Color of the status, selection, required



.. index::
  single: color_name field
.. 




:limit: Allow to override Limit, boolean



.. index::
  single: limit field
.. 




:name: Holiday Status, char, required



.. index::
  single: name field
.. 




:section_id: Section, many2one



.. index::
  single: section_id field
.. 



Object: Holidays
################

.. index::
  single: Holidays object
.. 


:employee_id: Employee, many2one, required, readonly



.. index::
  single: employee_id field
.. 




:user_id: User_id, many2one, readonly



.. index::
  single: user_id field
.. 




:name: Description, char, required, readonly



.. index::
  single: name field
.. 




:date_to1: To, date, required, readonly



.. index::
  single: date_to1 field
.. 




:date_from: Vacation start day, datetime



.. index::
  single: date_from field
.. 




:state: State, selection, readonly



.. index::
  single: state field
.. 




:contactno: Contact no, char, required, readonly



.. index::
  single: contactno field
.. 




:total_hour: Total Hours, integer, readonly



.. index::
  single: total_hour field
.. 




:date_from1: From, date, required, readonly



.. index::
  single: date_from1 field
.. 




:case_id: Case, many2one



.. index::
  single: case_id field
.. 




:total_full: Total Full Leave, integer, readonly



.. index::
  single: total_full field
.. 




:manager_id: Holiday manager, many2one, readonly



.. index::
  single: manager_id field
.. 




:holiday_id: Holiday's days list, one2many, readonly



.. index::
  single: holiday_id field
.. 




:date_to: Vacation end day, datetime



.. index::
  single: date_to field
.. 




:number_of_days: Number of Days in this Holiday Request, float



.. index::
  single: number_of_days field
.. 




:total_half: Total Half Leave, integer, readonly



.. index::
  single: total_half field
.. 




:notes: Notes, text, readonly



.. index::
  single: notes field
.. 




:holiday_status: Holiday's Status, many2one



.. index::
  single: holiday_status field
.. 



Object: Holidays Per User
#########################

.. index::
  single: Holidays Per User object
.. 


:employee_id: Employee, many2one, required



.. index::
  single: employee_id field
.. 




:user_id: User, many2one



.. index::
  single: user_id field
.. 




:notes: Notes, text



.. index::
  single: notes field
.. 




:max_leaves: Maximum Leaves Allowed, float, required



.. index::
  single: max_leaves field
.. 




:leaves_taken: Leaves Already Taken, float, readonly



.. index::
  single: leaves_taken field
.. 




:history: History, one2many



.. index::
  single: history field
.. 




:active: Active, boolean



.. index::
  single: active field
.. 




:remaining_leaves: Remaining Leaves, float, readonly



.. index::
  single: remaining_leaves field
.. 




:holiday_status: Holiday's Status, many2one, required



.. index::
  single: holiday_status field
.. 



Object: hr.holidays.log
#######################

.. index::
  single: hr.holidays.log object
.. 


:holiday_req_id: Holiday Request ID, char



.. index::
  single: holiday_req_id field
.. 




:employee_id: Employee, many2one, readonly



.. index::
  single: employee_id field
.. 




:name: Action, char, readonly



.. index::
  single: name field
.. 




:nb_holidays: Number of Holidays Requested, float



.. index::
  single: nb_holidays field
.. 




:holiday_user_id: Holidays user, many2one



.. index::
  single: holiday_user_id field
.. 




:date: Date, datetime



.. index::
  single: date field
.. 




:holiday_status: Holiday's Status, many2one, readonly



.. index::
  single: holiday_status field
.. 

