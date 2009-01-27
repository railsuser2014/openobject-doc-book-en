
Module Customer Relationship Management (*crm_configuration*)
=============================================================
:Module: crm_configuration
:Name: Customer Relationship Management
:Version: 5.0.1.0
:Directory: crm_configuration
:Web: http://www.openerp.com

Description
-----------

::

  The Open ERP case and request tracker enables a group of
  people to intelligently and efficiently manage tasks, issues,
  and requests. It manages key tasks such as communication, 
  identification, prioritization, assignment, resolution and notification.
  
  This module provide screens like: jobs hiring process, leads, business
  opportunities, fund raising trackings, support & helpdesk, calendar of
  meetings, eso.

Dependencies
------------

 * crm - installed
 * report_crm - installed
 * process - installed

Reports
-------

None


Menus
-------

 * CRM & SRM/Configuration/Cases/Stages
 * CRM & SRM/Reporting/This Month/Cases by Section and Category2
 * CRM & SRM/Reporting/All Months/Cases by Section and Category2
 * CRM & SRM/Reporting/This Month/Cases by Section and Stage
 * CRM & SRM/Reporting/All Months/Cases by Section and Stage
 * CRM & SRM/Reporting/This Month/Cases by Section, Category and Stage
 * CRM & SRM/Reporting/All Months/Cases by Section, Category and Stage
 * CRM & SRM/Reporting/This Month/Cases by Section, Category and Category2
 * CRM & SRM/Reporting/All Months/Cases by Section, Category and Category2

Views
-----

 * Configure Menu for Sections (form)
 * CRM -Graph (graph)
 * crm.case.stage.tree (tree)
 * crm.case.stage.form (form)
 * CRM - Bug Tracker Form (form)
 * CRM - Bug Tracker Tree (tree)
 * CRM - Bug Tracker Calendar (calendar)
 * CRM - Jobs Requests Tree (tree)
 * CRM - Jobs Requests Form (form)
 * CRM - Jobs Requests Calendar (calendar)
 * CRM - Leads Form (form)
 * CRM - Leads Tree (tree)
 * CRM - Leads Calendar (calendar)
 * CRM - Meetings Form (form)
 * CRM - Meetings Tree (tree)
 * CRM - Meetings Calendar (calendar)
 * CRM - Opportunities Form (form)
 * CRM - Opportunities Tree (tree)
 * CRM - Opportunities Calendar (calendar)
 * CRM - Funds Tree (tree)
 * CRM - Funds Form (form)
 * CRM - Funds Calendar (calendar)
 * CRM - Funds Graph (graph)
 * CRM - Claims Tree (tree)
 * CRM - Claims Form (form)
 * CRM - Claims Calendar (calendar)
 * CRM - Phone Calls Tree (tree)
 * CRM - Phone Call Form (form)
 * CRM - Phone Calls Calendar (calendar)
 * CRM Report - Sections and Category2(Tree) (tree)
 * CRM Report - Sections and Category2(Form) (form)
 * CRM Report - Sections and Category2(Graph) (graph)
 * CRM Report - Sections and Stage(Tree) (tree)
 * CRM Report - Sections and Stage(Form) (form)
 * CRM Report - Sections and Stage(Graph) (graph)
 * CRM Report - Section, Category and Stage(Tree) (tree)
 * CRM Report - Section, Category and Stage(Form) (form)
 * CRM Report - Section, Category and Category2(Tree) (tree)
 * CRM Report - Section, Category and Category2(Form) (form)


Objects
-------

Object: Category2 of case
#########################

.. index::
  single: Category2 of case object
.. 


:name: Case Category2 Name, char, required



.. index::
  single: name field
.. 




:section_id: Case Section, many2one



.. index::
  single: section_id field
.. 



Object: Stage of case
#####################

.. index::
  single: Stage of case object
.. 


:name: Stage Name, char, required



.. index::
  single: name field
.. 




:section_id: Case Section, many2one



.. index::
  single: section_id field
.. 



Object: crm.menu.config_wizard
##############################

.. index::
  single: crm.menu.config_wizard object
.. 


:jobs: Jobs Hiring Process, boolean

    *Help you to organise the jobs hiring process: evaluation, meetings, email integration...*

.. index::
  single: jobs field
.. 




:name: Name, char



.. index::
  single: name field
.. 




:lead: Leads, boolean

    *Allows you to track and manage leads which are pre-sales requests or contacts, the very first contact with a customer request.*

.. index::
  single: lead field
.. 




:document_ics: Shared Calendar, boolean

    *Will allow you to synchronise your Open ERP calendars with your phone, outlook, Sunbird, ical, ...*

.. index::
  single: document_ics field
.. 




:helpdesk: Helpdesk, boolean

    *Manages an Helpdesk service.*

.. index::
  single: helpdesk field
.. 




:bugs: Bug Tracking, boolean

    *Used by companies to track bugs and support requests on softwares*

.. index::
  single: bugs field
.. 




:phonecall: Phone Calls, boolean

    *Help you to encode the result of a phone call or to planify a list of phone calls to process.*

.. index::
  single: phonecall field
.. 




:fund: Fund Raising Operations, boolean

    *This may help associations in their fund raising process and tracking.*

.. index::
  single: fund field
.. 




:claims: Claims, boolean

    *Manages the supplier and customers claims, including your corrective or preventive actions.*

.. index::
  single: claims field
.. 




:meeting: Calendar of Meetings, boolean

    *Manages the calendar of meetings of the users.*

.. index::
  single: meeting field
.. 




:opportunity: Business Opportunities, boolean

    *Tracks identified business opportunities for your sales pipeline.*

.. index::
  single: opportunity field
.. 



Object: Cases by section and category2
######################################

.. index::
  single: Cases by section and category2 object
.. 


:stage_id: Stage, many2one, readonly



.. index::
  single: stage_id field
.. 




:user_id: User, many2one, readonly



.. index::
  single: user_id field
.. 




:name: Month, date, readonly



.. index::
  single: name field
.. 




:nbr: # of Cases, integer, readonly



.. index::
  single: nbr field
.. 




:section_id: Section, many2one, readonly



.. index::
  single: section_id field
.. 




:state: State, selection, readonly



.. index::
  single: state field
.. 




:amount_revenue: Est.Revenue, float, readonly



.. index::
  single: amount_revenue field
.. 




:category2_id: Type, many2one, readonly



.. index::
  single: category2_id field
.. 




:delay_close: Delay Close, char, readonly



.. index::
  single: delay_close field
.. 



Object: Cases by section and stage
##################################

.. index::
  single: Cases by section and stage object
.. 


:stage_id: Stage, many2one, readonly



.. index::
  single: stage_id field
.. 




:user_id: User, many2one, readonly



.. index::
  single: user_id field
.. 




:name: Month, date, readonly



.. index::
  single: name field
.. 




:nbr: # of Cases, integer, readonly



.. index::
  single: nbr field
.. 




:section_id: Section, many2one, readonly



.. index::
  single: section_id field
.. 




:state: State, selection, readonly



.. index::
  single: state field
.. 




:amount_revenue: Est.Revenue, float, readonly



.. index::
  single: amount_revenue field
.. 




:delay_close: Delay Close, char, readonly



.. index::
  single: delay_close field
.. 




:categ_id: Category, many2one, readonly



.. index::
  single: categ_id field
.. 



Object: Cases by section, Category and stage
############################################

.. index::
  single: Cases by section, Category and stage object
.. 


:stage_id: Stage, many2one, readonly



.. index::
  single: stage_id field
.. 




:user_id: User, many2one, readonly



.. index::
  single: user_id field
.. 




:name: Month, date, readonly



.. index::
  single: name field
.. 




:nbr: # of Cases, integer, readonly



.. index::
  single: nbr field
.. 




:section_id: Section, many2one, readonly



.. index::
  single: section_id field
.. 




:state: State, selection, readonly



.. index::
  single: state field
.. 




:delay_close: Delay Close, char, readonly



.. index::
  single: delay_close field
.. 




:categ_id: Category, many2one, readonly



.. index::
  single: categ_id field
.. 



Object: Cases by section, Category and Category2
################################################

.. index::
  single: Cases by section, Category and Category2 object
.. 


:stage_id: Stage, many2one, readonly



.. index::
  single: stage_id field
.. 




:user_id: User, many2one, readonly



.. index::
  single: user_id field
.. 




:name: Month, date, readonly



.. index::
  single: name field
.. 




:nbr: # of Cases, integer, readonly



.. index::
  single: nbr field
.. 




:section_id: Section, many2one, readonly



.. index::
  single: section_id field
.. 




:state: State, selection, readonly



.. index::
  single: state field
.. 




:category2_id: Type, many2one, readonly



.. index::
  single: category2_id field
.. 




:delay_close: Delay Close, char, readonly



.. index::
  single: delay_close field
.. 




:categ_id: Category, many2one, readonly



.. index::
  single: categ_id field
.. 

