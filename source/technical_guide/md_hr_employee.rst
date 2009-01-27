
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

.. index::
  single: Street object
.. 


:name: Street, char



.. index::
  single: name field
.. 



Object: Zip
###########

.. index::
  single: Zip object
.. 


:name: Zip, char



.. index::
  single: name field
.. 



Object: Town
############

.. index::
  single: Town object
.. 


:name: Town, char



.. index::
  single: name field
.. 



Object: Employee Address
########################

.. index::
  single: Employee Address object
.. 


:employee_id: Employee, many2one



.. index::
  single: employee_id field
.. 




:name: Name, char



.. index::
  single: name field
.. 




:house_nbr: # House No, char



.. index::
  single: house_nbr field
.. 




:zip_id: Zip, many2one



.. index::
  single: zip_id field
.. 




:country_id: Country, many2one



.. index::
  single: country_id field
.. 




:town_id: Town, many2one



.. index::
  single: town_id field
.. 




:street_id: Street, many2one



.. index::
  single: street_id field
.. 




:type: Address Type, selection



.. index::
  single: type field
.. 



Object: Maximun Travel allowance per year and per day
#####################################################

.. index::
  single: Maximun Travel allowance per year and per day object
.. 


:amount_per_day: Maximun Amount Per Day, float, required



.. index::
  single: amount_per_day field
.. 




:amount_per_year: Maximum Amount Per Year, float, required



.. index::
  single: amount_per_year field
.. 

