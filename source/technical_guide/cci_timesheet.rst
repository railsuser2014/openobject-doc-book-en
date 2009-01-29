
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



:line_ids: Timesheet Lines, one2many





:affectation_ids: Affectation Lines, one2many





:name: Grant Name, char, required




Object: CCI Timesheet
#####################



:name: Name, char, required, readonly





:grant_id: Grant, many2one, required, readonly





:sending_date: Sending Date, date





:asked_amount: Asked Amount, float





:state: State, selection, required, readonly





:date_to: To Date, date, required





:line_ids: Timesheet Lines, one2many





:date_from: From Date, date, required





:accepted_amount: Accepted Amount, float




Object: CCI Timesheet Line
##########################



:suppl_cost: Supplementary Cost, float





:user_id: User, many2one, required





:name: Name, char, required





:diff_hours: Hour To - Hour From, float, readonly





:zip_id: Zip, many2one





:grant_id: Grant, many2one





:contact_id: Contact, many2one





:day_date: Date of the Day, date, required





:hour_from: Hour From, float, required





:hour_to: Hour To, float, required





:timesheet_id: Timesheet, many2one





:kms: Kilometers, integer





:partner_id: Partner, many2one





:description: Description, text




Object: Timesheet Affectation
#############################



:hours_per_week: Hours Per Week, float, required





:user_id: User, many2one, required





:name: Name, char, required





:grant_id: Grant, many2one, required





:rate: Rate, float, required





:date_to: To Date, date, required





:percentage: Percentage, float, required





:date_from: From Date, date, required




Object: Report on Timesheet and Affectation
###########################################



:hours_per_week: Hours Per Week, float





:name: Name, char





:diff_hours: Hours, float





:date_from: From Date, date





:th_percentage: Percentage, float





:affectation_name: Affectation, char





:day_date: Date of the Day, date





:rate: Rate, float





:hour_from: Hour From, float





:hour_to: Hour To, float





:date_to: To Date, date





:timesheet_id: Timesheet Ref, integer





:grant_name: Grant, char





:user_name: Employee, char





:description: Description, text


