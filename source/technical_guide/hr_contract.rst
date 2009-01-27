
Module Human Resources Contracts (*hr_contract*)
================================================
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

Object: Employee Marital Status
###############################

.. index::
  single: Employee Marital Status object
.. 


:name: Marital Status, char, required



.. index::
  single: name field
.. 




:description: Status Description, text



.. index::
  single: description field
.. 



Object: Wage Period
###################

.. index::
  single: Wage Period object
.. 


:name: Period Name, char, required



.. index::
  single: name field
.. 




:factor_days: Hours in the period, float, required

    *This field is used by the timesheet system to compute the price of an hour of work wased on the contract of the employee*

.. index::
  single: factor_days field
.. 



Object: Wage Type
#################

.. index::
  single: Wage Type object
.. 


:type: Type, selection, required



.. index::
  single: type field
.. 




:period_id: Wage Period, many2one, required



.. index::
  single: period_id field
.. 




:name: Wage Type Name, char, required



.. index::
  single: name field
.. 




:factor_type: Factor for hour cost, float, required

    *This field is used by the timesheet system to compute the price of an hour of work wased on the contract of the employee*

.. index::
  single: factor_type field
.. 



Object: Contract
################

.. index::
  single: Contract object
.. 


:function: Position, many2one



.. index::
  single: function field
.. 




:wage_type_id: Wage Type, many2one, required



.. index::
  single: wage_type_id field
.. 




:fulltime_salary: Full-time Salary, float, readonly



.. index::
  single: fulltime_salary field
.. 




:code: code, char



.. index::
  single: code field
.. 




:availability_per_week: Availability per week, one2many



.. index::
  single: availability_per_week field
.. 




:salary_level: Salary level, integer



.. index::
  single: salary_level field
.. 




:form_of_employment: Form of employment, selection



.. index::
  single: form_of_employment field
.. 




:date_end: Expire date, date



.. index::
  single: date_end field
.. 




:date_start: Date of appointment, date, required



.. index::
  single: date_start field
.. 




:trial_period_review: Trial period review, date



.. index::
  single: trial_period_review field
.. 




:employee_id: Employee, many2one, required



.. index::
  single: employee_id field
.. 




:fte_hrs: FTE in Hours, float, readonly



.. index::
  single: fte_hrs field
.. 




:bank_account_nbr: Bank account number, char



.. index::
  single: bank_account_nbr field
.. 




:extend_appointment_date: Extend appointment from, date



.. index::
  single: extend_appointment_date field
.. 




:wage: Base salary, float, required



.. index::
  single: wage field
.. 




:fte: FTE, float



.. index::
  single: fte field
.. 




:salary_grade: Salary grade, integer



.. index::
  single: salary_grade field
.. 




:working_hours_per_day: Working hours per day, integer



.. index::
  single: working_hours_per_day field
.. 




:department_id: Department, many2one



.. index::
  single: department_id field
.. 




:notes: Notes, text



.. index::
  single: notes field
.. 




:name: Contract Name, char, required



.. index::
  single: name field
.. 

