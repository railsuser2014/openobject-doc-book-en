
Pilot Human Resource Management (*md_hr_contract*)
==================================================
:Module: md_hr_contract
:Name: Pilot Human Resource Management
:Version: 5.0.1.0
:Directory: md_hr_contract
:Web: 

Description
-----------

::

  Contract Module for human resource management. You can manage:
      * Contract of the employee
      * Availability of the employee
      and many more.................

Dependencies
------------

 * base - installed
 * hr - installed
 * hr_contract - installed

Reports
-------

None


Menus
-------


None


Views
-----

 * \* INHERIT md.hr.contract.form1 (form)
 * \* INHERIT md.hr.contract.form2 (form)
 * \* INHERIT md.hr.contract.form3 (form)
 * \* INHERIT md.hr.contract.form4 (form)
 * \* INHERIT md.hr.contract.form5 (form)
 * \* INHERIT md.hr.employee.form1 (form)
 * md.hr.contract.availability.form (form)
 * md.hr.contract.availability.tree (tree)
 * \* INHERIT hr.department.form (form)


Objects
-------

Object: HR Contract Availability
################################



:to_hour: To, time





:from_hour: From, time





:contract_id: Contract, many2one





:day: Day, selection


