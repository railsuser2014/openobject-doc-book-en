
Module Human Resources (*hr*)
=============================
:Module: hr
:Name: Human Resources
:Version: 5.0.1.1
:Directory: hr
:Web: http://www.openerp.com

Description
-----------

::

  Module for human resource management. You can manage:
      * Employees and hierarchies
      * Work hours sheets
      * Attendances and sign in/out system
  
      Different reports are also provided, mainly for attendance statistics.

Dependencies
------------

 * base - installed
 * process - installed

Reports
-------

None


Menus
-------

 * Human Resources
 * Human Resources/Reporting
 * Human Resources/Configuration
 * Human Resources/Employees
 * Human Resources/Employees/Employees Structure
 * Human Resources/Employees/All Employees
 * Human Resources/Employees/New Employee
 * Human Resources/Configuration/Working Time Categories
 * Human Resources/Configuration/Categories of Employee
 * Human Resources/Configuration/Categories of Employee/Categories structure
 * Administration/Users/Departments
 * Administration/Users/Departments/Departments

Views
-----

 * hr.employee.form (form)
 * hr.employee.tree (tree)
 * hr.employee.tree (tree)
 * hr.timesheet.group.form (form)
 * hr.timesheet.tree (tree)
 * hr.timesheet.form (form)
 * hr.employee.category.form (form)
 * hr.employee.category.list (tree)
 * hr.employee.category.tree (tree)
 * hr.department.form (form)
 * hr.department.tree (tree)


Objects
-------

Object: Working Time
####################

.. index::
  single: Working Time object
.. 


:timesheet_id: Working Time, one2many



.. index::
  single: timesheet_id field
.. 




:manager: Workgroup manager, many2one



.. index::
  single: manager field
.. 




:name: Group name, char, required



.. index::
  single: name field
.. 



Object: Employee Category
#########################

.. index::
  single: Employee Category object
.. 


:parent_id: Parent category, many2one



.. index::
  single: parent_id field
.. 




:child_ids: Childs Categories, one2many



.. index::
  single: child_ids field
.. 




:name: Category, char, required



.. index::
  single: name field
.. 



Object: Employee
################

.. index::
  single: Employee object
.. 


:address_id: Working Address, many2one



.. index::
  single: address_id field
.. 




:code: Personal Number, char



.. index::
  single: code field
.. 




:ssnid: SSN No, char



.. index::
  single: ssnid field
.. 




:address_number: Number, char



.. index::
  single: address_number field
.. 




:zip_id: Zip, many2one



.. index::
  single: zip_id field
.. 




:holidays_id: unknown, one2many



.. index::
  single: holidays_id field
.. 




:audiens_num: AUDIENS Number, char



.. index::
  single: audiens_num field
.. 




:partner_prefix: Partner's prefix, char



.. index::
  single: partner_prefix field
.. 




:sinid: SIN No, char



.. index::
  single: sinid field
.. 




:manager: Manager, boolean



.. index::
  single: manager field
.. 




:partner_initials: Partner's initials, char



.. index::
  single: partner_initials field
.. 




:waowiaww_dep_id: If yes, which department, many2one



.. index::
  single: waowiaww_dep_id field
.. 




:lang_id: Languages Known, one2many



.. index::
  single: lang_id field
.. 




:partner_lastname: Partner's name, char



.. index::
  single: partner_lastname field
.. 




:education: Education, char



.. index::
  single: education field
.. 




:nationality_id: Nationality, many2one



.. index::
  single: nationality_id field
.. 




:children: Number of children, integer



.. index::
  single: children field
.. 




:place_of_birth: Place of Birth, char



.. index::
  single: place_of_birth field
.. 




:maiden_name: Maiden Name, char



.. index::
  single: maiden_name field
.. 




:user_id: Related User, many2one



.. index::
  single: user_id field
.. 




:earings_order_beneficier: In name of, char



.. index::
  single: earings_order_beneficier field
.. 




:work_phone: Work Phone, char



.. index::
  single: work_phone field
.. 




:dist_home_work: Dist. between home and workplace (km), integer



.. index::
  single: dist_home_work field
.. 




:country_id: Country, many2one



.. index::
  single: country_id field
.. 




:company_id: Company, many2one



.. index::
  single: company_id field
.. 




:medic_exam: Medical examination date, date



.. index::
  single: medic_exam field
.. 




:parent_id: Manager, many2one



.. index::
  single: parent_id field
.. 




:state: Attendance, selection, readonly



.. index::
  single: state field
.. 




:nbr_of_children: # of children, integer



.. index::
  single: nbr_of_children field
.. 




:payscale: Scale, many2one



.. index::
  single: payscale field
.. 




:town_id: Town, many2one



.. index::
  single: town_id field
.. 




:pension: Pension, boolean



.. index::
  single: pension field
.. 




:evaluation_id: unknown, one2many



.. index::
  single: evaluation_id field
.. 




:email: Email, char



.. index::
  single: email field
.. 




:contract_ids: Contracts, one2many



.. index::
  single: contract_ids field
.. 




:status: Employee Status, selection



.. index::
  single: status field
.. 




:earings_order_account: Account Number, char



.. index::
  single: earings_order_account field
.. 




:otherid: Other ID, char



.. index::
  single: otherid field
.. 




:nin: National Insurance Number, char



.. index::
  single: nin field
.. 




:firstname: Surname, char



.. index::
  single: firstname field
.. 




:spaarloonregeling_account: A/C number spaarloonregeling, char



.. index::
  single: spaarloonregeling_account field
.. 




:partner_firstname: Partner's surname, char



.. index::
  single: partner_firstname field
.. 




:child_ids: Subordinates, one2many



.. index::
  single: child_ids field
.. 




:waowiaww: Disability/unemployment benefit, boolean



.. index::
  single: waowiaww field
.. 




:phone: Phone Number, char



.. index::
  single: phone field
.. 




:birthday: Birthday, date



.. index::
  single: birthday field
.. 




:levensloopregeling_account: A/C number levensloonregeling, char



.. index::
  single: levensloopregeling_account field
.. 




:birth_date: Birth Date, date



.. index::
  single: birth_date field
.. 




:active: Active, boolean



.. index::
  single: active field
.. 




:field_of_education: Field of education, char



.. index::
  single: field_of_education field
.. 




:nationality: Nationality, many2one



.. index::
  single: nationality field
.. 




:marital: Marital Status, selection



.. index::
  single: marital field
.. 




:work_email: Work Email, char



.. index::
  single: work_email field
.. 




:product_id: Product, many2one



.. index::
  single: product_id field
.. 




:leavedate: Leaved on, date



.. index::
  single: leavedate field
.. 




:work_location: Office Location, char



.. index::
  single: work_location field
.. 




:partner_dob: Partner's DOB, date



.. index::
  single: partner_dob field
.. 




:name: Employee, char, required



.. index::
  single: name field
.. 




:pension_waiver: Pension waiver, boolean



.. index::
  single: pension_waiver field
.. 




:mobile: Mobile Phone Number, char



.. index::
  single: mobile field
.. 




:gender: Gender, selection



.. index::
  single: gender field
.. 




:notes: Notes, text



.. index::
  single: notes field
.. 




:amount_travel_allowance: Travel allowance(per year), float, readonly



.. index::
  single: amount_travel_allowance field
.. 




:attachment_earings_order: Attachment of earings order, boolean



.. index::
  single: attachment_earings_order field
.. 




:prefix: Prefix, char



.. index::
  single: prefix field
.. 




:birthdate: Date of Birthday, date



.. index::
  single: birthdate field
.. 




:earings_order_amount: Amount, float



.. index::
  single: earings_order_amount field
.. 




:journal_id: Analytic Journal, many2one



.. index::
  single: journal_id field
.. 




:travel_allowance: Travel Allowande, boolean



.. index::
  single: travel_allowance field
.. 




:marital_status: Marital Status, selection



.. index::
  single: marital_status field
.. 




:spaarloonregeling: Spaarloonregeling, float



.. index::
  single: spaarloonregeling field
.. 




:partner_gender: Partner's gender, selection



.. index::
  single: partner_gender field
.. 




:levensloopregeling: Levensloopregeling, float



.. index::
  single: levensloopregeling field
.. 




:addres_id: Address, many2one



.. index::
  single: addres_id field
.. 




:category_id: Category, many2one



.. index::
  single: category_id field
.. 




:soc_security: Social security number, char



.. index::
  single: soc_security field
.. 



Object: Timesheet Line
######################

.. index::
  single: Timesheet Line object
.. 


:dayofweek: Day of week, selection



.. index::
  single: dayofweek field
.. 




:name: Name, char, required



.. index::
  single: name field
.. 




:tgroup_id: Employee's timesheet group, many2one



.. index::
  single: tgroup_id field
.. 




:date_from: Starting date, date



.. index::
  single: date_from field
.. 




:hour_from: Work from, float, required



.. index::
  single: hour_from field
.. 




:hour_to: Work to, float, required



.. index::
  single: hour_to field
.. 



Object: hr.department
#####################

.. index::
  single: hr.department object
.. 


:member_ids: Members, many2many



.. index::
  single: member_ids field
.. 




:name: Department Name, char, required



.. index::
  single: name field
.. 




:child_ids: Childs Departments, one2many



.. index::
  single: child_ids field
.. 




:company_id: Company, many2one, required



.. index::
  single: company_id field
.. 




:note: Note, text



.. index::
  single: note field
.. 




:parent_id: Parent Department, many2one



.. index::
  single: parent_id field
.. 




:max_temp_contract: Maximum temporary contracts, integer



.. index::
  single: max_temp_contract field
.. 




:manager_id: Manager, many2one, required



.. index::
  single: manager_id field
.. 

