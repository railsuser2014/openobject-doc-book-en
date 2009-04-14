
.. i18n: .. module:: hr_contract
.. i18n:     :synopsis: Human Resources Contracts (Official, Quality Certified)
.. i18n:     :noindex:
.. i18n: .. 

.. module:: hr_contract
    :synopsis: Human Resources Contracts (Official, Quality Certified)
    :noindex:
.. 

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. i18n: Human Resources Contracts (*hr_contract*)
.. i18n: =========================================
.. i18n: :Module: hr_contract
.. i18n: :Name: Human Resources Contracts
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: hr_contract
.. i18n: :Web: http://www.openerp.com
.. i18n: :Official module: yes
.. i18n: :Quality certified: yes

Human Resources Contracts (*hr_contract*)
=========================================
:Module: hr_contract
:Name: Human Resources Contracts
:Version: 5.0.1.0
:Author: Tiny
:Directory: hr_contract
:Web: http://www.openerp.com
:Official module: yes
:Quality certified: yes

.. i18n: Description
.. i18n: -----------

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   Add all information on the employee form to manage contracts:
.. i18n:       * Martial status,
.. i18n:       * Security number,
.. i18n:       * Place of birth, birth date, ...
.. i18n:   
.. i18n:       You can assign several contracts per employee.

::

  Add all information on the employee form to manage contracts:
      * Martial status,
      * Security number,
      * Place of birth, birth date, ...
  
      You can assign several contracts per employee.

.. i18n: Dependencies
.. i18n: ------------

Dependencies
------------

.. i18n:  * :mod:`hr`

 * :mod:`hr`

.. i18n: Reports
.. i18n: -------

Reports
-------

.. i18n: None

None

.. i18n: Menus
.. i18n: -------

Menus
-------

.. i18n:  * Human Resources/Configuration/Contract
.. i18n:  * Human Resources/Configuration/Contract/Contract Wage Type
.. i18n:  * Human Resources/Configuration/Contract/Wage period
.. i18n:  * Human Resources/Configuration/Marital Status
.. i18n:  * Human Resources/Contract

 * Human Resources/Configuration/Contract
 * Human Resources/Configuration/Contract/Contract Wage Type
 * Human Resources/Configuration/Contract/Wage period
 * Human Resources/Configuration/Marital Status
 * Human Resources/Contract

.. i18n: Views
.. i18n: -----

Views
-----

.. i18n:  * hr.contract.wage.type.period.view.form (form)
.. i18n:  * hr.hr.employee.marital.status (form)
.. i18n:  * hr.contract.wage.type.view.form (form)
.. i18n:  * hr.contract.wage.type.view.tree (tree)
.. i18n:  * \* INHERIT hr.hr.employee.view.form2 (form)
.. i18n:  * hr.contract.type.view.form (form)
.. i18n:  * hr.contract.view.form (form)
.. i18n:  * hr.contract.type.view.tree (tree)
.. i18n:  * hr.contract.view.tree (tree)

 * hr.contract.wage.type.period.view.form (form)
 * hr.hr.employee.marital.status (form)
 * hr.contract.wage.type.view.form (form)
 * hr.contract.wage.type.view.tree (tree)
 * \* INHERIT hr.hr.employee.view.form2 (form)
 * hr.contract.type.view.form (form)
 * hr.contract.view.form (form)
 * hr.contract.type.view.tree (tree)
 * hr.contract.view.tree (tree)

.. i18n: Objects
.. i18n: -------

Objects
-------

.. i18n: Object: Employee Marital Status (hr.employee.marital.status)
.. i18n: ############################################################

Object: Employee Marital Status (hr.employee.marital.status)
############################################################

.. i18n: :name: Marital Status, char, required

:name: Marital Status, char, required

.. i18n: :description: Status Description, text

:description: Status Description, text

.. i18n: Object: Wage Period (hr.contract.wage.type.period)
.. i18n: ##################################################

Object: Wage Period (hr.contract.wage.type.period)
##################################################

.. i18n: :name: Period Name, char, required

:name: Period Name, char, required

.. i18n: :factor_days: Hours in the period, float, required

:factor_days: Hours in the period, float, required

.. i18n:     *This field is used by the timesheet system to compute the price of an hour of work wased on the contract of the employee*

    *This field is used by the timesheet system to compute the price of an hour of work wased on the contract of the employee*

.. i18n: Object: Wage Type (hr.contract.wage.type)
.. i18n: #########################################

Object: Wage Type (hr.contract.wage.type)
#########################################

.. i18n: :type: Type, selection, required

:type: Type, selection, required

.. i18n: :period_id: Wage Period, many2one, required

:period_id: Wage Period, many2one, required

.. i18n: :name: Wage Type Name, char, required

:name: Wage Type Name, char, required

.. i18n: :factor_type: Factor for hour cost, float, required

:factor_type: Factor for hour cost, float, required

.. i18n:     *This field is used by the timesheet system to compute the price of an hour of work wased on the contract of the employee*

    *This field is used by the timesheet system to compute the price of an hour of work wased on the contract of the employee*

.. i18n: Object: Contract (hr.contract)
.. i18n: ##############################

Object: Contract (hr.contract)
##############################

.. i18n: :function: Position, many2one

:function: Position, many2one

.. i18n: :wage_type_id: Wage Type, many2one, required

:wage_type_id: Wage Type, many2one, required

.. i18n: :fulltime_salary: Full-time Salary, float, readonly

:fulltime_salary: Full-time Salary, float, readonly

.. i18n: :code: code, char

:code: code, char

.. i18n: :availability_per_week: Availability per week, one2many

:availability_per_week: Availability per week, one2many

.. i18n: :salary_level: Salary level, integer

:salary_level: Salary level, integer

.. i18n: :form_of_employment: Form of employment, selection

:form_of_employment: Form of employment, selection

.. i18n: :date_end: Expire date, date

:date_end: Expire date, date

.. i18n: :date_start: Date of appointment, date, required

:date_start: Date of appointment, date, required

.. i18n: :trial_period_review: Trial period review, date

:trial_period_review: Trial period review, date

.. i18n: :employee_id: Employee, many2one, required

:employee_id: Employee, many2one, required

.. i18n: :fte_hrs: FTE in Hours, float, readonly

:fte_hrs: FTE in Hours, float, readonly

.. i18n: :bank_account_nbr: Bank account number, char

:bank_account_nbr: Bank account number, char

.. i18n: :extend_appointment_date: Extend appointment from, date

:extend_appointment_date: Extend appointment from, date

.. i18n: :wage: Base salary, float, required

:wage: Base salary, float, required

.. i18n: :fte: FTE, float

:fte: FTE, float

.. i18n: :salary_grade: Salary grade, integer

:salary_grade: Salary grade, integer

.. i18n: :working_hours_per_day: Working hours per day, integer

:working_hours_per_day: Working hours per day, integer

.. i18n: :department_id: Department, many2one

:department_id: Department, many2one

.. i18n: :notes: Notes, text

:notes: Notes, text

.. i18n: :name: Contract Name, char, required

:name: Contract Name, char, required
