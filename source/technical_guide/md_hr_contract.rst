
.. module:: md_hr_contract
    :synopsis: Pilot Human Resource Management 
    :noindex:
.. 

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

Pilot Human Resource Management (*md_hr_contract*)
==================================================
:Module: md_hr_contract
:Name: Pilot Human Resource Management
:Version: 5.0.1.0
:Author: Tiny
:Directory: md_hr_contract
:Web: 
:Official module: no
:Quality certified: no

Description
-----------

::

  Contract Module for human resource management. You can manage:
      * Contract of the employee
      * Availability of the employee
      and many more.................

Dependencies
------------

 * :mod:`base`
 * :mod:`hr`
 * :mod:`hr_contract`

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

Object: HR Contract Availability (md.hr.contract.availability)
##############################################################



:to_hour: To, time





:from_hour: From, time





:contract_id: Contract, many2one





:day: Day, selection


