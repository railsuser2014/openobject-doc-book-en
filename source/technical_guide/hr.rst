
Human Resources (*hr*)
======================
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



:timesheet_id: Working Time, one2many





:manager: Workgroup manager, many2one





:name: Group name, char, required




Object: Employee Category
#########################



:parent_id: Parent category, many2one





:child_ids: Childs Categories, one2many





:name: Category, char, required




Object: Employee
################



:address_id: Working Address, many2one





:code: Personal Number, char





:ssnid: SSN No, char





:address_number: Number, char





:zip_id: Zip, many2one





:holidays_id: unknown, one2many





:audiens_num: AUDIENS Number, char





:partner_prefix: Partner's prefix, char





:sinid: SIN No, char





:manager: Manager, boolean





:partner_initials: Partner's initials, char





:waowiaww_dep_id: If yes, which department, many2one





:lang_id: Languages Known, one2many





:partner_lastname: Partner's name, char





:education: Education, char





:nationality_id: Nationality, many2one





:children: Number of children, integer





:place_of_birth: Place of Birth, char





:maiden_name: Maiden Name, char





:user_id: Related User, many2one





:earings_order_beneficier: In name of, char





:work_phone: Work Phone, char





:dist_home_work: Dist. between home and workplace (km), integer





:country_id: Country, many2one





:company_id: Company, many2one





:medic_exam: Medical examination date, date





:parent_id: Manager, many2one





:state: Attendance, selection, readonly





:nbr_of_children: # of children, integer





:payscale: Scale, many2one





:town_id: Town, many2one





:pension: Pension, boolean





:evaluation_id: unknown, one2many





:email: Email, char





:contract_ids: Contracts, one2many





:status: Employee Status, selection





:earings_order_account: Account Number, char





:otherid: Other ID, char





:nin: National Insurance Number, char





:firstname: Surname, char





:spaarloonregeling_account: A/C number spaarloonregeling, char





:partner_firstname: Partner's surname, char





:child_ids: Subordinates, one2many





:waowiaww: Disability/unemployment benefit, boolean





:phone: Phone Number, char





:birthday: Birthday, date





:levensloopregeling_account: A/C number levensloonregeling, char





:birth_date: Birth Date, date





:active: Active, boolean





:field_of_education: Field of education, char





:nationality: Nationality, many2one





:marital: Marital Status, selection





:work_email: Work Email, char





:product_id: Product, many2one





:leavedate: Leaved on, date





:work_location: Office Location, char





:partner_dob: Partner's DOB, date





:name: Employee, char, required





:pension_waiver: Pension waiver, boolean





:mobile: Mobile Phone Number, char





:gender: Gender, selection





:notes: Notes, text





:amount_travel_allowance: Travel allowance(per year), float, readonly





:attachment_earings_order: Attachment of earings order, boolean





:prefix: Prefix, char





:birthdate: Date of Birthday, date





:earings_order_amount: Amount, float





:journal_id: Analytic Journal, many2one





:travel_allowance: Travel Allowande, boolean





:marital_status: Marital Status, selection





:spaarloonregeling: Spaarloonregeling, float





:partner_gender: Partner's gender, selection





:levensloopregeling: Levensloopregeling, float





:addres_id: Address, many2one





:category_id: Category, many2one





:soc_security: Social security number, char




Object: Timesheet Line
######################



:dayofweek: Day of week, selection





:name: Name, char, required





:tgroup_id: Employee's timesheet group, many2one





:date_from: Starting date, date





:hour_from: Work from, float, required





:hour_to: Work to, float, required




Object: hr.department
#####################



:member_ids: Members, many2many





:name: Department Name, char, required





:child_ids: Childs Departments, one2many





:company_id: Company, many2one, required





:note: Note, text





:parent_id: Parent Department, many2one





:max_temp_contract: Maximum temporary contracts, integer





:manager_id: Manager, many2one, required


