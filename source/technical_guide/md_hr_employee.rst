
.. module:: md_hr_employee
    :synopsis: Pilot Human Resources 
    :noindex:
.. 

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

Pilot Human Resources (*md_hr_employee*)
========================================
:Module: md_hr_employee
:Name: Pilot Human Resources
:Version: 5.0.1.0
:Author: Tiny
:Directory: md_hr_employee
:Web: http://www.openerp.com/
:Official module: no
:Quality certified: no

Description
-----------

::

  None

Dependencies
------------

 * :mod:`base`
 * :mod:`hr`
 * :mod:`hr_holidays_request`
 * :mod:`md_hr_contract`
 * :mod:`hr_evaluation`

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

Object: Street (md.hr.address.street)
#####################################



:name: Street, char




Object: Zip (md.hr.address.zip)
###############################



:name: Zip, char




Object: Town (md.hr.address.town)
#################################



:name: Town, char




Object: Employee Address (md.hr.address)
########################################



:employee_id: Employee, many2one





:name: Name, char





:house_nbr: # House No, char





:zip_id: Zip, many2one





:country_id: Country, many2one





:town_id: Town, many2one





:street_id: Street, many2one





:type: Address Type, selection




Object: Maximun Travel allowance per year and per day (hr.employee.max.travel.allow)
####################################################################################



:amount_per_day: Maximun Amount Per Day, float, required





:amount_per_year: Maximum Amount Per Year, float, required


