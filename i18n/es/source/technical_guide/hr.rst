
.. i18n: .. module:: hr
.. i18n:     :synopsis: Human Resources (Official, Quality Certified)
.. i18n:     :noindex:
.. i18n: .. 

.. module:: hr
    :synopsis: Human Resources (Official, Quality Certified)
    :noindex:
.. 

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. i18n: Human Resources (*hr*)
.. i18n: ======================
.. i18n: :Module: hr
.. i18n: :Name: Human Resources
.. i18n: :Version: 5.0.1.1
.. i18n: :Author: Tiny
.. i18n: :Directory: hr
.. i18n: :Web: http://www.openerp.com
.. i18n: :Official module: yes
.. i18n: :Quality certified: yes

Human Resources (*hr*)
======================
:Module: hr
:Name: Human Resources
:Version: 5.0.1.1
:Author: Tiny
:Directory: hr
:Web: http://www.openerp.com
:Official module: yes
:Quality certified: yes

.. i18n: Description
.. i18n: -----------

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   Module for human resource management. You can manage:
.. i18n:       * Employees and hierarchies
.. i18n:       * Work hours sheets
.. i18n:       * Attendances and sign in/out system
.. i18n:   
.. i18n:       Different reports are also provided, mainly for attendance statistics.

::

  Module for human resource management. You can manage:
      * Employees and hierarchies
      * Work hours sheets
      * Attendances and sign in/out system
  
      Different reports are also provided, mainly for attendance statistics.

.. i18n: Dependencies
.. i18n: ------------

Dependencies
------------

.. i18n:  * :mod:`base`
.. i18n:  * :mod:`process`

 * :mod:`base`
 * :mod:`process`

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

.. i18n:  * Human Resources
.. i18n:  * Human Resources/Reporting
.. i18n:  * Human Resources/Configuration
.. i18n:  * Human Resources/Employees
.. i18n:  * Human Resources/Employees/Employees Structure
.. i18n:  * Human Resources/Employees/All Employees
.. i18n:  * Human Resources/Employees/New Employee
.. i18n:  * Human Resources/Configuration/Working Time Categories
.. i18n:  * Human Resources/Configuration/Categories of Employee
.. i18n:  * Human Resources/Configuration/Categories of Employee/Categories structure
.. i18n:  * Administration/Users/Departments
.. i18n:  * Administration/Users/Departments/Departments

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

.. i18n: Views
.. i18n: -----

Views
-----

.. i18n:  * hr.employee.form (form)
.. i18n:  * hr.employee.tree (tree)
.. i18n:  * hr.employee.tree (tree)
.. i18n:  * hr.timesheet.group.form (form)
.. i18n:  * hr.timesheet.tree (tree)
.. i18n:  * hr.timesheet.form (form)
.. i18n:  * hr.employee.category.form (form)
.. i18n:  * hr.employee.category.list (tree)
.. i18n:  * hr.employee.category.tree (tree)
.. i18n:  * hr.department.form (form)
.. i18n:  * hr.department.tree (tree)

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

.. i18n: Objects
.. i18n: -------

Objects
-------

.. i18n: Object: Working Time (hr.timesheet.group)
.. i18n: #########################################

Object: Working Time (hr.timesheet.group)
#########################################

.. i18n: :timesheet_id: Working Time, one2many

:timesheet_id: Working Time, one2many

.. i18n: :manager: Workgroup manager, many2one

:manager: Workgroup manager, many2one

.. i18n: :name: Group name, char, required

:name: Group name, char, required

.. i18n: Object: Employee Category (hr.employee.category)
.. i18n: ################################################

Object: Employee Category (hr.employee.category)
################################################

.. i18n: :parent_id: Parent category, many2one

:parent_id: Parent category, many2one

.. i18n: :child_ids: Childs Categories, one2many

:child_ids: Childs Categories, one2many

.. i18n: :name: Category, char, required

:name: Category, char, required

.. i18n: Object: Employee (hr.employee)
.. i18n: ##############################

Object: Employee (hr.employee)
##############################

.. i18n: :address_id: Working Address, many2one

:address_id: Working Address, many2one

.. i18n: :code: Personal Number, char

:code: Personal Number, char

.. i18n: :ssnid: SSN No, char

:ssnid: SSN No, char

.. i18n: :address_number: Number, char

:address_number: Number, char

.. i18n: :zip_id: Zip, many2one

:zip_id: Zip, many2one

.. i18n: :holidays_id: unknown, one2many

:holidays_id: unknown, one2many

.. i18n: :audiens_num: AUDIENS Number, char

:audiens_num: AUDIENS Number, char

.. i18n: :partner_prefix: Partner's prefix, char

:partner_prefix: Partner's prefix, char

.. i18n: :sinid: SIN No, char

:sinid: SIN No, char

.. i18n: :manager: Manager, boolean

:manager: Manager, boolean

.. i18n: :partner_initials: Partner's initials, char

:partner_initials: Partner's initials, char

.. i18n: :waowiaww_dep_id: If yes, which department, many2one

:waowiaww_dep_id: If yes, which department, many2one

.. i18n: :lang_id: Languages Known, one2many

:lang_id: Languages Known, one2many

.. i18n: :partner_lastname: Partner's name, char

:partner_lastname: Partner's name, char

.. i18n: :education: Education, char

:education: Education, char

.. i18n: :nationality_id: Nationality, many2one

:nationality_id: Nationality, many2one

.. i18n: :children: Number of children, integer

:children: Number of children, integer

.. i18n: :place_of_birth: Place of Birth, char

:place_of_birth: Place of Birth, char

.. i18n: :maiden_name: Maiden Name, char

:maiden_name: Maiden Name, char

.. i18n: :user_id: Related User, many2one

:user_id: Related User, many2one

.. i18n: :earings_order_beneficier: In name of, char

:earings_order_beneficier: In name of, char

.. i18n: :work_phone: Work Phone, char

:work_phone: Work Phone, char

.. i18n: :dist_home_work: Dist. between home and workplace (km), integer

:dist_home_work: Dist. between home and workplace (km), integer

.. i18n: :country_id: Country, many2one

:country_id: Country, many2one

.. i18n: :company_id: Company, many2one

:company_id: Company, many2one

.. i18n: :medic_exam: Medical examination date, date

:medic_exam: Medical examination date, date

.. i18n: :parent_id: Manager, many2one

:parent_id: Manager, many2one

.. i18n: :state: Attendance, selection, readonly

:state: Attendance, selection, readonly

.. i18n: :nbr_of_children: # of children, integer

:nbr_of_children: # of children, integer

.. i18n: :payscale: Scale, many2one

:payscale: Scale, many2one

.. i18n: :town_id: Town, many2one

:town_id: Town, many2one

.. i18n: :pension: Pension, boolean

:pension: Pension, boolean

.. i18n: :evaluation_id: unknown, one2many

:evaluation_id: unknown, one2many

.. i18n: :email: Email, char

:email: Email, char

.. i18n: :contract_ids: Contracts, one2many

:contract_ids: Contracts, one2many

.. i18n: :status: Employee Status, selection

:status: Employee Status, selection

.. i18n: :earings_order_account: Account Number, char

:earings_order_account: Account Number, char

.. i18n: :otherid: Other ID, char

:otherid: Other ID, char

.. i18n: :nin: National Insurance Number, char

:nin: National Insurance Number, char

.. i18n: :firstname: Surname, char

:firstname: Surname, char

.. i18n: :spaarloonregeling_account: A/C number spaarloonregeling, char

:spaarloonregeling_account: A/C number spaarloonregeling, char

.. i18n: :partner_firstname: Partner's surname, char

:partner_firstname: Partner's surname, char

.. i18n: :child_ids: Subordinates, one2many

:child_ids: Subordinates, one2many

.. i18n: :waowiaww: Disability/unemployment benefit, boolean

:waowiaww: Disability/unemployment benefit, boolean

.. i18n: :phone: Phone Number, char

:phone: Phone Number, char

.. i18n: :birthday: Birthday, date

:birthday: Birthday, date

.. i18n: :levensloopregeling_account: A/C number levensloonregeling, char

:levensloopregeling_account: A/C number levensloonregeling, char

.. i18n: :birth_date: Birth Date, date

:birth_date: Birth Date, date

.. i18n: :active: Active, boolean

:active: Active, boolean

.. i18n: :field_of_education: Field of education, char

:field_of_education: Field of education, char

.. i18n: :nationality: Nationality, many2one

:nationality: Nationality, many2one

.. i18n: :marital: Marital Status, selection

:marital: Marital Status, selection

.. i18n: :work_email: Work Email, char

:work_email: Work Email, char

.. i18n: :product_id: Product, many2one

:product_id: Product, many2one

.. i18n: :leavedate: Leaved on, date

:leavedate: Leaved on, date

.. i18n: :work_location: Office Location, char

:work_location: Office Location, char

.. i18n: :partner_dob: Partner's DOB, date

:partner_dob: Partner's DOB, date

.. i18n: :name: Employee, char, required

:name: Employee, char, required

.. i18n: :pension_waiver: Pension waiver, boolean

:pension_waiver: Pension waiver, boolean

.. i18n: :mobile: Mobile Phone Number, char

:mobile: Mobile Phone Number, char

.. i18n: :gender: Gender, selection

:gender: Gender, selection

.. i18n: :notes: Notes, text

:notes: Notes, text

.. i18n: :amount_travel_allowance: Travel allowance(per year), float, readonly

:amount_travel_allowance: Travel allowance(per year), float, readonly

.. i18n: :attachment_earings_order: Attachment of earings order, boolean

:attachment_earings_order: Attachment of earings order, boolean

.. i18n: :prefix: Prefix, char

:prefix: Prefix, char

.. i18n: :birthdate: Date of Birthday, date

:birthdate: Date of Birthday, date

.. i18n: :earings_order_amount: Amount, float

:earings_order_amount: Amount, float

.. i18n: :journal_id: Analytic Journal, many2one

:journal_id: Analytic Journal, many2one

.. i18n: :travel_allowance: Travel Allowande, boolean

:travel_allowance: Travel Allowande, boolean

.. i18n: :marital_status: Marital Status, selection

:marital_status: Marital Status, selection

.. i18n: :spaarloonregeling: Spaarloonregeling, float

:spaarloonregeling: Spaarloonregeling, float

.. i18n: :partner_gender: Partner's gender, selection

:partner_gender: Partner's gender, selection

.. i18n: :levensloopregeling: Levensloopregeling, float

:levensloopregeling: Levensloopregeling, float

.. i18n: :addres_id: Address, many2one

:addres_id: Address, many2one

.. i18n: :category_id: Category, many2one

:category_id: Category, many2one

.. i18n: :soc_security: Social security number, char

:soc_security: Social security number, char

.. i18n: Object: Timesheet Line (hr.timesheet)
.. i18n: #####################################

Object: Timesheet Line (hr.timesheet)
#####################################

.. i18n: :dayofweek: Day of week, selection

:dayofweek: Day of week, selection

.. i18n: :name: Name, char, required

:name: Name, char, required

.. i18n: :tgroup_id: Employee's timesheet group, many2one

:tgroup_id: Employee's timesheet group, many2one

.. i18n: :date_from: Starting date, date

:date_from: Starting date, date

.. i18n: :hour_from: Work from, float, required

:hour_from: Work from, float, required

.. i18n: :hour_to: Work to, float, required

:hour_to: Work to, float, required

.. i18n: Object: hr.department (hr.department)
.. i18n: #####################################

Object: hr.department (hr.department)
#####################################

.. i18n: :member_ids: Members, many2many

:member_ids: Members, many2many

.. i18n: :name: Department Name, char, required

:name: Department Name, char, required

.. i18n: :child_ids: Childs Departments, one2many

:child_ids: Childs Departments, one2many

.. i18n: :company_id: Company, many2one, required

:company_id: Company, many2one, required

.. i18n: :note: Note, text

:note: Note, text

.. i18n: :parent_id: Parent Department, many2one

:parent_id: Parent Department, many2one

.. i18n: :max_temp_contract: Maximum temporary contracts, integer

:max_temp_contract: Maximum temporary contracts, integer

.. i18n: :manager_id: Manager, many2one, required

:manager_id: Manager, many2one, required
