
Module CCI Timesheet (*cci_timesheet*)
======================================
:Module: cci_timesheet
:Name: CCI Timesheet
:Version: 5.0.1.0
:Directory: cci_timesheet
:Web: http://www.openerp.com

Description
-----------

::

  A Customized timesheet module.

Dependencies
------------

 * base - installed
 * cci_partner - installed
 * cci_crm - installed
 * cci_base_contact - installed

Reports
-------

None


Menus
-------

 * Timesheet
 * Timesheet/Configuration
 * Timesheet/Timesheet
 * Timesheet/Configuration/Grant
 * Timesheet/Timesheet/Timesheet
 * Timesheet/Timesheet/Timesheet Lines
 * Timesheet/Timesheet/Timesheet Affectation
 * Timesheet/Reporting
 * Timesheet/Reporting/Timesheets per Employee
 * Timesheet/Create Timesheet Lines

Views
-----

 * cci_timesheet.grant.form (form)
 * cci_timesheet.grant.tree (tree)
 * cci_timesheet.form (form)
 * cci_timesheet.tree (tree)
 * cci_timesheet.line.form (form)
 * cci_timesheet.line.tree (tree)
 * cci_timesheet.affectation.form (form)
 * cci_timesheet.affectation.tree (tree)
 * Timesheets per Employee (Tree) (tree)
 * Timesheets per Employee (Form) (form)
 * Timesheets per Employee (Graph) (graph)
 * \* INHERIT crm.case.form.confidential2 (form)
 * \* INHERIT crm.case.form.confidential3 (form)
 * \* INHERIT project.task.work.form (form)
 * \* INHERIT project.task.work.form1 (form)
 * \* INHERIT project.task.work.tree (tree)


Objects
-------

Object: CCI Timesheet Grant
###########################

.. index::
  single: CCI Timesheet Grant object
.. 


:line_ids: Timesheet Lines, one2many



.. index::
  single: line_ids field
.. 




:affectation_ids: Affectation Lines, one2many



.. index::
  single: affectation_ids field
.. 




:name: Grant Name, char, required



.. index::
  single: name field
.. 



Object: CCI Timesheet
#####################

.. index::
  single: CCI Timesheet object
.. 


:name: Name, char, required, readonly



.. index::
  single: name field
.. 




:grant_id: Grant, many2one, required, readonly



.. index::
  single: grant_id field
.. 




:sending_date: Sending Date, date



.. index::
  single: sending_date field
.. 




:asked_amount: Asked Amount, float



.. index::
  single: asked_amount field
.. 




:state: State, selection, required, readonly



.. index::
  single: state field
.. 




:date_to: To Date, date, required



.. index::
  single: date_to field
.. 




:line_ids: Timesheet Lines, one2many



.. index::
  single: line_ids field
.. 




:date_from: From Date, date, required



.. index::
  single: date_from field
.. 




:accepted_amount: Accepted Amount, float



.. index::
  single: accepted_amount field
.. 



Object: CCI Timesheet Line
##########################

.. index::
  single: CCI Timesheet Line object
.. 


:suppl_cost: Supplementary Cost, float



.. index::
  single: suppl_cost field
.. 




:user_id: User, many2one, required



.. index::
  single: user_id field
.. 




:name: Name, char, required



.. index::
  single: name field
.. 




:diff_hours: Hour To - Hour From, float, readonly



.. index::
  single: diff_hours field
.. 




:zip_id: Zip, many2one



.. index::
  single: zip_id field
.. 




:grant_id: Grant, many2one



.. index::
  single: grant_id field
.. 




:contact_id: Contact, many2one



.. index::
  single: contact_id field
.. 




:day_date: Date of the Day, date, required



.. index::
  single: day_date field
.. 




:hour_from: Hour From, float, required



.. index::
  single: hour_from field
.. 




:hour_to: Hour To, float, required



.. index::
  single: hour_to field
.. 




:timesheet_id: Timesheet, many2one



.. index::
  single: timesheet_id field
.. 




:kms: Kilometers, integer



.. index::
  single: kms field
.. 




:partner_id: Partner, many2one



.. index::
  single: partner_id field
.. 




:description: Description, text



.. index::
  single: description field
.. 



Object: Timesheet Affectation
#############################

.. index::
  single: Timesheet Affectation object
.. 


:hours_per_week: Hours Per Week, float, required



.. index::
  single: hours_per_week field
.. 




:user_id: User, many2one, required



.. index::
  single: user_id field
.. 




:name: Name, char, required



.. index::
  single: name field
.. 




:grant_id: Grant, many2one, required



.. index::
  single: grant_id field
.. 




:rate: Rate, float, required



.. index::
  single: rate field
.. 




:date_to: To Date, date, required



.. index::
  single: date_to field
.. 




:percentage: Percentage, float, required



.. index::
  single: percentage field
.. 




:date_from: From Date, date, required



.. index::
  single: date_from field
.. 



Object: Report on Timesheet and Affectation
###########################################

.. index::
  single: Report on Timesheet and Affectation object
.. 


:hours_per_week: Hours Per Week, float



.. index::
  single: hours_per_week field
.. 




:name: Name, char



.. index::
  single: name field
.. 




:diff_hours: Hours, float



.. index::
  single: diff_hours field
.. 




:date_from: From Date, date



.. index::
  single: date_from field
.. 




:th_percentage: Percentage, float



.. index::
  single: th_percentage field
.. 




:affectation_name: Affectation, char



.. index::
  single: affectation_name field
.. 




:day_date: Date of the Day, date



.. index::
  single: day_date field
.. 




:rate: Rate, float



.. index::
  single: rate field
.. 




:hour_from: Hour From, float



.. index::
  single: hour_from field
.. 




:hour_to: Hour To, float



.. index::
  single: hour_to field
.. 




:date_to: To Date, date



.. index::
  single: date_to field
.. 




:timesheet_id: Timesheet Ref, integer



.. index::
  single: timesheet_id field
.. 




:grant_name: Grant, char



.. index::
  single: grant_name field
.. 




:user_name: Employee, char



.. index::
  single: user_name field
.. 




:description: Description, text



.. index::
  single: description field
.. 

