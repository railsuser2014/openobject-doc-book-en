
.. i18n: .. module:: md_hr_contract
.. i18n:     :synopsis: Pilot Human Resource Management 
.. i18n:     :noindex:
.. i18n: .. 

.. module:: md_hr_contract
    :synopsis: Pilot Human Resource Management 
    :noindex:
.. 

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. i18n: Pilot Human Resource Management (*md_hr_contract*)
.. i18n: ==================================================
.. i18n: :Module: md_hr_contract
.. i18n: :Name: Pilot Human Resource Management
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: md_hr_contract
.. i18n: :Web: 
.. i18n: :Official module: no
.. i18n: :Quality certified: no

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

.. i18n: Description
.. i18n: -----------

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   Contract Module for human resource management. You can manage:
.. i18n:       * Contract of the employee
.. i18n:       * Availability of the employee
.. i18n:       and many more.................

::

  Contract Module for human resource management. You can manage:
      * Contract of the employee
      * Availability of the employee
      and many more.................

.. i18n: Dependencies
.. i18n: ------------

Dependencies
------------

.. i18n:  * :mod:`base`
.. i18n:  * :mod:`hr`
.. i18n:  * :mod:`hr_contract`

 * :mod:`base`
 * :mod:`hr`
 * :mod:`hr_contract`

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

.. i18n: None

None

.. i18n: Views
.. i18n: -----

Views
-----

.. i18n:  * \* INHERIT md.hr.contract.form1 (form)
.. i18n:  * \* INHERIT md.hr.contract.form2 (form)
.. i18n:  * \* INHERIT md.hr.contract.form3 (form)
.. i18n:  * \* INHERIT md.hr.contract.form4 (form)
.. i18n:  * \* INHERIT md.hr.contract.form5 (form)
.. i18n:  * \* INHERIT md.hr.employee.form1 (form)
.. i18n:  * md.hr.contract.availability.form (form)
.. i18n:  * md.hr.contract.availability.tree (tree)
.. i18n:  * \* INHERIT hr.department.form (form)

 * \* INHERIT md.hr.contract.form1 (form)
 * \* INHERIT md.hr.contract.form2 (form)
 * \* INHERIT md.hr.contract.form3 (form)
 * \* INHERIT md.hr.contract.form4 (form)
 * \* INHERIT md.hr.contract.form5 (form)
 * \* INHERIT md.hr.employee.form1 (form)
 * md.hr.contract.availability.form (form)
 * md.hr.contract.availability.tree (tree)
 * \* INHERIT hr.department.form (form)

.. i18n: Objects
.. i18n: -------

Objects
-------

.. i18n: Object: HR Contract Availability (md.hr.contract.availability)
.. i18n: ##############################################################

Object: HR Contract Availability (md.hr.contract.availability)
##############################################################

.. i18n: :to_hour: To, time

:to_hour: To, time

.. i18n: :from_hour: From, time

:from_hour: From, time

.. i18n: :contract_id: Contract, many2one

:contract_id: Contract, many2one

.. i18n: :day: Day, selection

:day: Day, selection
