
.. i18n: .. module:: hr_holidays
.. i18n:     :synopsis: Human Resources: Holidays management (Official, Quality Certified)
.. i18n:     :noindex:
.. i18n: .. 

.. module:: hr_holidays
    :synopsis: Human Resources: Holidays management (Official, Quality Certified)
    :noindex:
.. 

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. i18n: Human Resources: Holidays management (*hr_holidays*)
.. i18n: ====================================================
.. i18n: :Module: hr_holidays
.. i18n: :Name: Human Resources: Holidays management
.. i18n: :Version: 5.0.1.1
.. i18n: :Author: Tiny & Axelor
.. i18n: :Directory: hr_holidays
.. i18n: :Web: http://www.openerp.com
.. i18n: :Official module: yes
.. i18n: :Quality certified: yes

Human Resources: Holidays management (*hr_holidays*)
====================================================
:Module: hr_holidays
:Name: Human Resources: Holidays management
:Version: 5.0.1.1
:Author: Tiny & Axelor
:Directory: hr_holidays
:Web: http://www.openerp.com
:Official module: yes
:Quality certified: yes

.. i18n: Description
.. i18n: -----------

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   Human Resources: Holidays tracking and workflow
.. i18n:   
.. i18n:       This module allows you to manage holidays and holidays requests. For each employee, you can also 
.. i18n:       define a number of available holidays per holiday status.  
.. i18n:       Note that:
.. i18n:       - A synchronisation with an internal agenda (use of the CRM module) is possible: in order to 
.. i18n:         automatically create a case when an holiday request is accepted, you have to link the holidays 
.. i18n:         status to a case section. 
.. i18n:         You can set up this info and your colour preferences in
.. i18n:                   HR \ Configuration \ Holidays Status
.. i18n:       - An employee can make a negative holiday request (holiday request of -2 days for example), 
.. i18n:         this is considered by the system as an ask for more off-days. It will increase his total of that 
.. i18n:         holiday status available (if the request is accepted).
.. i18n:       - There are two ways to print the employee's holidays:
.. i18n:           * The first will allow to choose employees by department and is used by clicking the menu 
.. i18n:             item located in
.. i18n:                   HR \ Holidays Request \ Print Summary of Holidays
.. i18n:           * The second will allow you to choose the holidays report for specific employees. 
.. i18n:              Go on the list
.. i18n:                   HR \ Employees \ Employees
.. i18n:               then select the ones you want to choose, click on the print icon and select the option
.. i18n:                   'Print Summary of Employee's Holidays'
.. i18n:       - The wizard allows you to choose if you want to print either the Confirmed & Validated 
.. i18n: holidays or only the Validated ones. These states must be set up by a user from the group 'HR' 
.. i18n: and with the role 'holidays'. You can define these features in the security tab from the user 
.. i18n: data in *Administration \ Users \ Users* for example, you maybe will do it for the user 'admin'.

::

  Human Resources: Holidays tracking and workflow
  
      This module allows you to manage holidays and holidays requests. For each employee, you can also 
      define a number of available holidays per holiday status.  
      Note that:
      - A synchronisation with an internal agenda (use of the CRM module) is possible: in order to 
        automatically create a case when an holiday request is accepted, you have to link the holidays 
        status to a case section. 
        You can set up this info and your colour preferences in
                  HR \ Configuration \ Holidays Status
      - An employee can make a negative holiday request (holiday request of -2 days for example), 
        this is considered by the system as an ask for more off-days. It will increase his total of that 
        holiday status available (if the request is accepted).
      - There are two ways to print the employee's holidays:
          * The first will allow to choose employees by department and is used by clicking the menu 
            item located in
                  HR \ Holidays Request \ Print Summary of Holidays
          * The second will allow you to choose the holidays report for specific employees. 
             Go on the list
                  HR \ Employees \ Employees
              then select the ones you want to choose, click on the print icon and select the option
                  'Print Summary of Employee's Holidays'
      - The wizard allows you to choose if you want to print either the Confirmed & Validated 
holidays or only the Validated ones. These states must be set up by a user from the group 'HR' 
and with the role 'holidays'. You can define these features in the security tab from the user 
data in *Administration \ Users \ Users* for example, you maybe will do it for the user 'admin'.

.. i18n: Dependencies
.. i18n: ------------

Dependencies
------------

.. i18n:  * :mod:`hr`
.. i18n:  * :mod:`crm_configuration`
.. i18n:  * :mod:`process`

 * :mod:`hr`
 * :mod:`crm_configuration`
 * :mod:`process`

.. i18n: Reports
.. i18n: -------

Reports
-------

.. i18n:  * Summary Of Holidays

 * Summary Of Holidays

.. i18n: Menus
.. i18n: -------

Menus
-------

.. i18n:  * Human Resources/Configuration/Holiday Status
.. i18n:  * Human Resources/Holidays Management
.. i18n:  * Human Resources/Holidays Management/New Holidays Request
.. i18n:  * Human Resources/Holidays Management/All Holidays Requests
.. i18n:  * Human Resources/Holidays Management/My Holidays Requests
.. i18n:  * Human Resources/Holidays Management/My Holidays Requests/My Draft Holidays Requests
.. i18n:  * Human Resources/Holidays Management/My Holidays Requests/My Awaiting Confirmation Holidays Requests
.. i18n:  * Human Resources/Holidays Management/My Holidays Requests/My Validated Holidays Requests
.. i18n:  * Human Resources/Holidays Management/My Holidays Requests/My Refused Holidays Requests
.. i18n:  * Human Resources/Holidays Management/All Holidays Requests/Holidays Requests Awaiting for Validation
.. i18n:  * Human Resources/Configuration/Holidays Per Employee
.. i18n:  * Human Resources/Reporting/My Available Holidays
.. i18n:  * Human Resources/Reporting/Print Summary of Holidays

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

.. i18n: Views
.. i18n: -----

Views
-----

.. i18n:  * hr.holidays.form (form)
.. i18n:  * hr.holidays.tree (tree)
.. i18n:  * hr.holidays.log.form (form)
.. i18n:  * >hr.holidays.log.tree (tree)
.. i18n:  * hr.holidays.status.form (form)
.. i18n:  * hr.holidays.status.tree (tree)
.. i18n:  * hr.holidays.per.user.form (form)
.. i18n:  * hr.holidays.per.user.tree (tree)
.. i18n:  * hr.holidays.per.user.graph (graph)

 * hr.holidays.form (form)
 * hr.holidays.tree (tree)
 * hr.holidays.log.form (form)
 * >hr.holidays.log.tree (tree)
 * hr.holidays.status.form (form)
 * hr.holidays.status.tree (tree)
 * hr.holidays.per.user.form (form)
 * hr.holidays.per.user.tree (tree)
 * hr.holidays.per.user.graph (graph)

.. i18n: Objects
.. i18n: -------

Objects
-------

.. i18n: Object: Holidays Status (hr.holidays.status)
.. i18n: ############################################

Object: Holidays Status (hr.holidays.status)
############################################

.. i18n: :active: Active, boolean

:active: Active, boolean

.. i18n: :color_name: Color of the status, selection, required

:color_name: Color of the status, selection, required

.. i18n: :limit: Allow to override Limit, boolean

:limit: Allow to override Limit, boolean

.. i18n: :name: Holiday Status, char, required

:name: Holiday Status, char, required

.. i18n: :section_id: Section, many2one

:section_id: Section, many2one

.. i18n: Object: Holidays (hr.holidays)
.. i18n: ##############################

Object: Holidays (hr.holidays)
##############################

.. i18n: :employee_id: Employee, many2one, required, readonly

:employee_id: Employee, many2one, required, readonly

.. i18n: :user_id: User_id, many2one, readonly

:user_id: User_id, many2one, readonly

.. i18n: :name: Description, char, required, readonly

:name: Description, char, required, readonly

.. i18n: :date_to1: To, date, required, readonly

:date_to1: To, date, required, readonly

.. i18n: :date_from: Vacation start day, datetime

:date_from: Vacation start day, datetime

.. i18n: :state: State, selection, readonly

:state: State, selection, readonly

.. i18n: :contactno: Contact no, char, required, readonly

:contactno: Contact no, char, required, readonly

.. i18n: :total_hour: Total Hours, integer, readonly

:total_hour: Total Hours, integer, readonly

.. i18n: :date_from1: From, date, required, readonly

:date_from1: From, date, required, readonly

.. i18n: :case_id: Case, many2one

:case_id: Case, many2one

.. i18n: :total_full: Total Full Leave, integer, readonly

:total_full: Total Full Leave, integer, readonly

.. i18n: :manager_id: Holiday manager, many2one, readonly

:manager_id: Holiday manager, many2one, readonly

.. i18n: :holiday_id: Holiday's days list, one2many, readonly

:holiday_id: Holiday's days list, one2many, readonly

.. i18n: :date_to: Vacation end day, datetime

:date_to: Vacation end day, datetime

.. i18n: :number_of_days: Number of Days in this Holiday Request, float

:number_of_days: Number of Days in this Holiday Request, float

.. i18n: :total_half: Total Half Leave, integer, readonly

:total_half: Total Half Leave, integer, readonly

.. i18n: :notes: Notes, text, readonly

:notes: Notes, text, readonly

.. i18n: :holiday_status: Holiday's Status, many2one

:holiday_status: Holiday's Status, many2one

.. i18n: Object: Holidays Per User (hr.holidays.per.user)
.. i18n: ################################################

Object: Holidays Per User (hr.holidays.per.user)
################################################

.. i18n: :employee_id: Employee, many2one, required

:employee_id: Employee, many2one, required

.. i18n: :user_id: User, many2one

:user_id: User, many2one

.. i18n: :notes: Notes, text

:notes: Notes, text

.. i18n: :max_leaves: Maximum Leaves Allowed, float, required

:max_leaves: Maximum Leaves Allowed, float, required

.. i18n: :leaves_taken: Leaves Already Taken, float, readonly

:leaves_taken: Leaves Already Taken, float, readonly

.. i18n: :history: History, one2many

:history: History, one2many

.. i18n: :active: Active, boolean

:active: Active, boolean

.. i18n: :remaining_leaves: Remaining Leaves, float, readonly

:remaining_leaves: Remaining Leaves, float, readonly

.. i18n: :holiday_status: Holiday's Status, many2one, required

:holiday_status: Holiday's Status, many2one, required

.. i18n: Object: hr.holidays.log (hr.holidays.log)
.. i18n: #########################################

Object: hr.holidays.log (hr.holidays.log)
#########################################

.. i18n: :holiday_req_id: Holiday Request ID, char

:holiday_req_id: Holiday Request ID, char

.. i18n: :employee_id: Employee, many2one, readonly

:employee_id: Employee, many2one, readonly

.. i18n: :name: Action, char, readonly

:name: Action, char, readonly

.. i18n: :nb_holidays: Number of Holidays Requested, float

:nb_holidays: Number of Holidays Requested, float

.. i18n: :holiday_user_id: Holidays user, many2one

:holiday_user_id: Holidays user, many2one

.. i18n: :date: Date, datetime

:date: Date, datetime

.. i18n: :holiday_status: Holiday's Status, many2one, readonly

:holiday_status: Holiday's Status, many2one, readonly
