
Module Pilot Human Resources (*md_hr_employee*)
===============================================
:Module: md_hr_employee
:Name: Pilot Human Resources
:Version: 5.0.1.0
:Directory: md_hr_employee
:Web: http://tinyerp.com/module_hr.html

Description
-----------

::

  None

Dependencies
------------

 * base - installed
 * hr - installed
 * hr_holidays_request - installed
 * md_hr_contract - installed
 * hr_evaluation - installed

Reports
-------

None


Menus
-------

 * Human Resources/Configuration/Maximun Travel allowance

Views
-----

 * \* INHERIT md.hr.employee.form (form)
 * \* INHERIT md.hr.employee.form (form)
 * \* INHERIT md.hr.employee.form (form)
 * \* INHERIT md.hr.employee.form (form)
 * \* INHERIT md.hr.employee.form (form)
 * \* INHERIT md.hr.employee.form (form)
 * \* INHERIT md.hr.employee.form (form)
 * \* INHERIT md.hr.employee.form (form)
 * \* INHERIT md.hr.employee.form (form)
 * \* INHERIT md.hr.employee.form (form)
 * \* INHERIT md.hr.employee.form (form)
 * \* INHERIT md.hr.employee.form (form)
 * \* INHERIT md.hr.employee.form (form)
 * \* INHERIT md.hr.employee.form (form)
 * md.hr.employee.tree (tree)
 * md.hr.employee.tree (tree)
 * md.hr.address.form (form)
 * md.hr.address.tree (tree)
 * hr.employee.max.travel.allow.form (form)
 * hr.employee.max.travel.allow.tree (tree)


Objects
-------

Object: Street
##############



:name: Street, char




Object: Zip
###########



:name: Zip, char




Object: Town
############



:name: Town, char




Object: Employee Address
########################



:employee_id: Employee, many2one





:name: Name, char





:house_nbr: # House No, char





:zip_id: Zip, many2one





:country_id: Country, many2one





:town_id: Town, many2one





:street_id: Street, many2one





:type: Address Type, selection




Object: Maximun Travel allowance per year and per day
#####################################################



:amount_per_day: Maximun Amount Per Day, float, required





:amount_per_year: Maximum Amount Per Year, float, required


