
CRM Management - Reporting (*report_crm*)
=========================================
:Module: report_crm
:Name: CRM Management - Reporting
:Version: 5.0.1.0
:Directory: report_crm
:Web: http://www.openerp.com

Description
-----------

::

  A module that adds new reports based on CRM cases.
      Case By section, Case By category

Dependencies
------------

 * crm - installed

Reports
-------

None


Menus
-------

 * CRM & SRM/Reporting
 * CRM & SRM/Reporting/This Month
 * CRM & SRM/Reporting/This Month/Cases by user and section (this month)
 * CRM & SRM/Reporting/All Months
 * CRM & SRM/Reporting/All Months/Cases by User and Section
 * CRM & SRM/Reporting/This Month/My cases by section (this month)
 * CRM & SRM/Reporting/All Months/My cases by section
 * CRM & SRM/Reporting/This Month/Cases by categories and section (this month)
 * CRM & SRM/Reporting/All Months/Cases by Categories and Section

Views
-----

 * report.crm.case.user.tree (tree)
 * report.crm.case.user.form (form)
 * report.crm.case.user.graph (graph)
 * report.crm.case.categ.tree (tree)
 * report.crm.case.categ.form (form)


Objects
-------

Object: Cases by user and section
#################################



:amount_revenue_prob: Est. Rev*Prob., float, readonly





:amount_costs: Est.Cost, float, readonly





:user_id: User, many2one, readonly





:name: Month, date, readonly





:probability: Avg. Probability, float, readonly





:nbr: # of Cases, integer, readonly





:section_id: Section, many2one, readonly





:state: Status, selection, readonly





:amount_revenue: Est.Revenue, float, readonly





:delay_close: Delay to close, char, readonly




Object: Cases by section and category
#####################################



:amount_revenue_prob: Est. Rev*Prob., float, readonly





:amount_costs: Est.Cost, float, readonly





:name: Month, date, readonly





:probability: Avg. Probability, float, readonly





:nbr: # of Cases, integer, readonly





:section_id: Section, many2one, readonly





:state: Status, selection, readonly





:amount_revenue: Est.Revenue, float, readonly





:delay_close: Delay Close, char, readonly





:categ_id: Category, many2one, readonly


