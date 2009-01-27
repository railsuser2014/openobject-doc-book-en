
Module Pilot Human Resource Management (*md_hr_contract*)
=========================================================
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

.. index::
  single: HR Contract Availability object
.. 


:to_hour: To, time



.. index::
  single: to_hour field
.. 




:from_hour: From, time



.. index::
  single: from_hour field
.. 




:contract_id: Contract, many2one



.. index::
  single: contract_id field
.. 




:day: Day, selection



.. index::
  single: day field
.. 

