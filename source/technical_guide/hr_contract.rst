
.. module:: hr_contract
    :synopsis: Human Resources Contracts
    :noindex:
.. 

Human Resources Contracts (*hr_contract*)
=========================================
:Module: hr_contract
:Name: Human Resources Contracts
:Version: 5.0.1.0
:Directory: hr_contract
:Web: http://www.openerp.com

Description
-----------

::

  Add all information on the employee form to manage contracts:
      * Martial status,
      * Security number,
      * Place of birth, birth date, ...
  
      You can assign several contracts per employee.

Dependencies
------------

 * hr - installed

Reports
-------

None


Menus
-------

 * Human Resources/Configuration/Contract
 * Human Resources/Configuration/Contract/Contract Wage Type
 * Human Resources/Configuration/Contract/Wage period
 * Human Resources/Configuration/Marital Status
 * Human Resources/Contract

Views
-----

 * hr.contract.wage.type.period.view.form (form)
 * hr.hr.employee.marital.status (form)
 * hr.contract.wage.type.view.form (form)
 * hr.contract.wage.type.view.tree (tree)
 * \* INHERIT hr.hr.employee.view.form2 (form)
 * hr.contract.type.view.form (form)
 * hr.contract.view.form (form)
 * hr.contract.type.view.tree (tree)
 * hr.contract.view.tree (tree)


Objects
-------

Object: Employee Marital Status (hr.employee.marital.status)
############################################################



:name: Marital Status, char, required





:description: Status Description, text




Object: Wage Period (hr.contract.wage.type.period)
##################################################



:name: Period Name, char, required





:factor_days: Hours in the period, float, required

    *This field is used by the timesheet system to compute the price of an hour of work wased on the contract of the employee*


Object: Wage Type (hr.contract.wage.type)
#########################################



:type: Type, selection, required





:period_id: Wage Period, many2one, required





:name: Wage Type Name, char, required





:factor_type: Factor for hour cost, float, required

    *This field is used by the timesheet system to compute the price of an hour of work wased on the contract of the employee*


Object: Contract (hr.contract)
##############################



:function: Position, many2one





:wage_type_id: Wage Type, many2one, required





:fulltime_salary: Full-time Salary, float, readonly





:code: code, char





:availability_per_week: Availability per week, one2many





:salary_level: Salary level, integer





:form_of_employment: Form of employment, selection





:date_end: Expire date, date





:date_start: Date of appointment, date, required





:trial_period_review: Trial period review, date





:employee_id: Employee, many2one, required





:fte_hrs: FTE in Hours, float, readonly





:bank_account_nbr: Bank account number, char





:extend_appointment_date: Extend appointment from, date





:wage: Base salary, float, required





:fte: FTE, float





:salary_grade: Salary grade, integer





:working_hours_per_day: Working hours per day, integer





:department_id: Department, many2one





:notes: Notes, text





:name: Contract Name, char, required


