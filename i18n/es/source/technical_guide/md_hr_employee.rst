
.. i18n: .. module:: md_hr_employee
.. i18n:     :synopsis: Pilot Human Resources 
.. i18n:     :noindex:
.. i18n: .. 

.. module:: md_hr_employee
    :synopsis: Pilot Human Resources 
    :noindex:
.. 

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. i18n: Pilot Human Resources (*md_hr_employee*)
.. i18n: ========================================
.. i18n: :Module: md_hr_employee
.. i18n: :Name: Pilot Human Resources
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: md_hr_employee
.. i18n: :Web: http://www.openerp.com/
.. i18n: :Official module: no
.. i18n: :Quality certified: no

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

.. i18n: Description
.. i18n: -----------

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   None

::

  None

.. i18n: Dependencies
.. i18n: ------------

Dependencies
------------

.. i18n:  * :mod:`base`
.. i18n:  * :mod:`hr`
.. i18n:  * :mod:`hr_holidays_request`
.. i18n:  * :mod:`md_hr_contract`
.. i18n:  * :mod:`hr_evaluation`

 * :mod:`base`
 * :mod:`hr`
 * :mod:`hr_holidays_request`
 * :mod:`md_hr_contract`
 * :mod:`hr_evaluation`

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

.. i18n:  * Human Resources/Configuration/Maximun Travel allowance

 * Human Resources/Configuration/Maximun Travel allowance

.. i18n: Views
.. i18n: -----

Views
-----

.. i18n:  * \* INHERIT md.hr.employee.form (form)
.. i18n:  * \* INHERIT md.hr.employee.form (form)
.. i18n:  * \* INHERIT md.hr.employee.form (form)
.. i18n:  * \* INHERIT md.hr.employee.form (form)
.. i18n:  * \* INHERIT md.hr.employee.form (form)
.. i18n:  * \* INHERIT md.hr.employee.form (form)
.. i18n:  * \* INHERIT md.hr.employee.form (form)
.. i18n:  * \* INHERIT md.hr.employee.form (form)
.. i18n:  * \* INHERIT md.hr.employee.form (form)
.. i18n:  * \* INHERIT md.hr.employee.form (form)
.. i18n:  * \* INHERIT md.hr.employee.form (form)
.. i18n:  * \* INHERIT md.hr.employee.form (form)
.. i18n:  * \* INHERIT md.hr.employee.form (form)
.. i18n:  * \* INHERIT md.hr.employee.form (form)
.. i18n:  * md.hr.employee.tree (tree)
.. i18n:  * md.hr.employee.tree (tree)
.. i18n:  * md.hr.address.form (form)
.. i18n:  * md.hr.address.tree (tree)
.. i18n:  * hr.employee.max.travel.allow.form (form)
.. i18n:  * hr.employee.max.travel.allow.tree (tree)

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

.. i18n: Objects
.. i18n: -------

Objects
-------

.. i18n: Object: Street (md.hr.address.street)
.. i18n: #####################################

Object: Street (md.hr.address.street)
#####################################

.. i18n: :name: Street, char

:name: Street, char

.. i18n: Object: Zip (md.hr.address.zip)
.. i18n: ###############################

Object: Zip (md.hr.address.zip)
###############################

.. i18n: :name: Zip, char

:name: Zip, char

.. i18n: Object: Town (md.hr.address.town)
.. i18n: #################################

Object: Town (md.hr.address.town)
#################################

.. i18n: :name: Town, char

:name: Town, char

.. i18n: Object: Employee Address (md.hr.address)
.. i18n: ########################################

Object: Employee Address (md.hr.address)
########################################

.. i18n: :employee_id: Employee, many2one

:employee_id: Employee, many2one

.. i18n: :name: Name, char

:name: Name, char

.. i18n: :house_nbr: # House No, char

:house_nbr: # House No, char

.. i18n: :zip_id: Zip, many2one

:zip_id: Zip, many2one

.. i18n: :country_id: Country, many2one

:country_id: Country, many2one

.. i18n: :town_id: Town, many2one

:town_id: Town, many2one

.. i18n: :street_id: Street, many2one

:street_id: Street, many2one

.. i18n: :type: Address Type, selection

:type: Address Type, selection

.. i18n: Object: Maximun Travel allowance per year and per day (hr.employee.max.travel.allow)
.. i18n: ####################################################################################

Object: Maximun Travel allowance per year and per day (hr.employee.max.travel.allow)
####################################################################################

.. i18n: :amount_per_day: Maximun Amount Per Day, float, required

:amount_per_day: Maximun Amount Per Day, float, required

.. i18n: :amount_per_year: Maximum Amount Per Year, float, required

:amount_per_year: Maximum Amount Per Year, float, required
