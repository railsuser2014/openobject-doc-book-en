
Module HR Holiday Request (*hr_holidays_request*)
=================================================
:Module: hr_holidays_request
:Name: HR Holiday Request
:Version: 5.0.1.0
:Directory: hr_holidays_request
:Web: http://www.axelor.com

Description
-----------

::

  None

Dependencies
------------

 * base - installed
 * hr - installed
 * hr_holidays - installed

Reports
-------

 * Holidays Report

 * Holidays Report Form

Menus
-------

 * Human Resources/Holidays Request
 * Human Resources/Holidays Request/All Validated Holidays
 * Human Resources/Holidays Request/Public Holidays
 * Human Resources/Holidays Request/All Holidays Requests
 * Human Resources/Holidays Request/Holiday History
 * Human Resources/Holidays Request/My Holidays Request
 * Human Resources/Holidays Request/My Holidays Request/Draft
 * Human Resources/Holidays Request/My Holidays Request/Waiting confirmation
 * Human Resources/Holidays Request/My Holidays Request/Validated
 * Human Resources/Holidays Request/My Holidays Request/Refused
 * Human Resources/Holidays Request/My Holidays Request/Request waiting validation
 * Human Resources/Holidays Request/My Holidays Request/Holidays Report

Views
-----

 * \* INHERIT Holidays (form)
 * \* INHERIT hr.holidays.tree (tree)
 * holidays.days.list (tree)
 * Holidays_hr (form)
 * holidays.days.history.list (tree)
 * holidays.days.history.list (form)
 * holidays.days.list (form)
 * public.holidays.days.list (form)
 * hr.holidays.tree.2 (tree)
 * hr.holidays.tree.2.history (tree)
 * ask.holiday.history (form)


Objects
-------

Object: Holidays history
########################

.. index::
  single: Holidays history object
.. 


:employee_id: Employee, many2one, readonly



.. index::
  single: employee_id field
.. 




:user_id: Employee_id, many2one, readonly



.. index::
  single: user_id field
.. 




:name: Description, char, readonly



.. index::
  single: name field
.. 




:date_to1: To, date, readonly



.. index::
  single: date_to1 field
.. 




:notes: Notes, text, readonly



.. index::
  single: notes field
.. 




:date_from1: From, date, readonly



.. index::
  single: date_from1 field
.. 




:contactno: Contact no, char, readonly



.. index::
  single: contactno field
.. 




:state: State, selection, readonly



.. index::
  single: state field
.. 




:total_full: Total Full Leave, integer, readonly



.. index::
  single: total_full field
.. 




:manager_id: Holiday manager, many2one, readonly



.. index::
  single: manager_id field
.. 




:holiday_id: Holiday's days list, one2many, readonly



.. index::
  single: holiday_id field
.. 




:total_hour: Total Hours, integer, readonly



.. index::
  single: total_hour field
.. 




:total_half: Total Half Leave, integer, readonly



.. index::
  single: total_half field
.. 




:validated_id: Validated By, many2one, readonly



.. index::
  single: validated_id field
.. 



Object: Holidays history
########################

.. index::
  single: Holidays history object
.. 


:date1: Date, date, required, readonly



.. index::
  single: date1 field
.. 




:user_id: User_id, many2one, readonly



.. index::
  single: user_id field
.. 




:name: Date, char



.. index::
  single: name field
.. 




:public_h: Public Holiday, boolean, readonly



.. index::
  single: public_h field
.. 




:state: State, selection, readonly



.. index::
  single: state field
.. 




:hourly_leave: Hourly Leave, float, readonly



.. index::
  single: hourly_leave field
.. 




:holiday_id: Holiday Ref, many2one



.. index::
  single: holiday_id field
.. 




:half_day: Half Leave, boolean, readonly



.. index::
  single: half_day field
.. 




:full_day: Full Leave, boolean, readonly



.. index::
  single: full_day field
.. 




:holiday_status: Holiday's Status, many2one



.. index::
  single: holiday_status field
.. 



Object: Public Holidays
#######################

.. index::
  single: Public Holidays object
.. 


:reason: Reason, text, required



.. index::
  single: reason field
.. 




:name: Date, date, required



.. index::
  single: name field
.. 



Object: Holidays history
########################

.. index::
  single: Holidays history object
.. 


:date1: Date, date, readonly



.. index::
  single: date1 field
.. 




:user_id: User_id, many2one, readonly



.. index::
  single: user_id field
.. 




:name: Date, char, readonly



.. index::
  single: name field
.. 




:public_h: Public Holiday, boolean, readonly



.. index::
  single: public_h field
.. 




:state: State, selection, readonly



.. index::
  single: state field
.. 




:hourly_leave: Hourly Leave, float, readonly



.. index::
  single: hourly_leave field
.. 




:holiday_id: Holiday Ref, many2one, readonly



.. index::
  single: holiday_id field
.. 




:half_day: Half Leave, boolean, readonly



.. index::
  single: half_day field
.. 




:full_day: Full Leave, boolean, readonly



.. index::
  single: full_day field
.. 




:holiday_status: Holiday's Status, selection, readonly



.. index::
  single: holiday_status field
.. 

