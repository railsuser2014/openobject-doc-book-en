
.. module:: hr_holidays
    :synopsis: Human Resources: Holidays management (Quality Certified)
    :noindex:
.. 

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

    <style>
      div.body p#module-hr_holidays {
        display: none;
      }
    </style>

Human Resources: Holidays management (*hr_holidays*)
====================================================
:Module: hr_holidays
:Name: Human Resources: Holidays management
:Version: 5.0.1.1
:Author: Tiny & Axelor
:Directory: hr_holidays
:Web: http://www.openerp.com
:Is certified: yes

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

 * :mod:`hr`
 * :mod:`crm_configuration`
 * :mod:`process`

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

Object: Holidays Status (hr.holidays.status)
############################################



:active: Active, boolean





:color_name: Color of the status, selection, required





:limit: Allow to override Limit, boolean





:name: Holiday Status, char, required





:section_id: Section, many2one




Object: Holidays (hr.holidays)
##############################



:employee_id: Employee, many2one, required, readonly





:user_id: User_id, many2one, readonly





:name: Description, char, required, readonly





:date_to1: To, date, required, readonly





:date_from: Vacation start day, datetime





:state: State, selection, readonly





:contactno: Contact no, char, required, readonly





:total_hour: Total Hours, integer, readonly





:date_from1: From, date, required, readonly





:case_id: Case, many2one





:total_full: Total Full Leave, integer, readonly





:manager_id: Holiday manager, many2one, readonly





:holiday_id: Holiday's days list, one2many, readonly





:date_to: Vacation end day, datetime





:number_of_days: Number of Days in this Holiday Request, float





:total_half: Total Half Leave, integer, readonly





:notes: Notes, text, readonly





:holiday_status: Holiday's Status, many2one




Object: Holidays Per User (hr.holidays.per.user)
################################################



:employee_id: Employee, many2one, required





:user_id: User, many2one





:notes: Notes, text





:max_leaves: Maximum Leaves Allowed, float, required





:leaves_taken: Leaves Already Taken, float, readonly





:history: History, one2many





:active: Active, boolean





:remaining_leaves: Remaining Leaves, float, readonly





:holiday_status: Holiday's Status, many2one, required




Object: hr.holidays.log (hr.holidays.log)
#########################################



:holiday_req_id: Holiday Request ID, char





:employee_id: Employee, many2one, readonly





:name: Action, char, readonly





:nb_holidays: Number of Holidays Requested, float





:holiday_user_id: Holidays user, many2one





:date: Date, datetime





:holiday_status: Holiday's Status, many2one, readonly


