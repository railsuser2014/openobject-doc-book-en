
.. i18n: .. module:: report_crm
.. i18n:     :synopsis: CRM Management - Reporting (Official, Quality Certified)
.. i18n:     :noindex:
.. i18n: .. 

.. module:: report_crm
    :synopsis: CRM Management - Reporting (Official, Quality Certified)
    :noindex:
.. 

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. i18n: CRM Management - Reporting (*report_crm*)
.. i18n: =========================================
.. i18n: :Module: report_crm
.. i18n: :Name: CRM Management - Reporting
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: report_crm
.. i18n: :Web: http://www.openerp.com
.. i18n: :Official module: yes
.. i18n: :Quality certified: yes

CRM Management - Reporting (*report_crm*)
=========================================
:Module: report_crm
:Name: CRM Management - Reporting
:Version: 5.0.1.0
:Author: Tiny
:Directory: report_crm
:Web: http://www.openerp.com
:Official module: yes
:Quality certified: yes

.. i18n: Description
.. i18n: -----------

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   A module that adds new reports based on CRM cases.
.. i18n:       Case By section, Case By category

::

  A module that adds new reports based on CRM cases.
      Case By section, Case By category

.. i18n: Dependencies
.. i18n: ------------

Dependencies
------------

.. i18n:  * :mod:`crm`

 * :mod:`crm`

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

.. i18n:  * CRM & SRM/Reporting
.. i18n:  * CRM & SRM/Reporting/This Month
.. i18n:  * CRM & SRM/Reporting/This Month/Cases by user and section (this month)
.. i18n:  * CRM & SRM/Reporting/All Months
.. i18n:  * CRM & SRM/Reporting/All Months/Cases by User and Section
.. i18n:  * CRM & SRM/Reporting/This Month/My cases by section (this month)
.. i18n:  * CRM & SRM/Reporting/All Months/My cases by section
.. i18n:  * CRM & SRM/Reporting/This Month/Cases by categories and section (this month)
.. i18n:  * CRM & SRM/Reporting/All Months/Cases by Categories and Section

 * CRM & SRM/Reporting
 * CRM & SRM/Reporting/This Month
 * CRM & SRM/Reporting/This Month/Cases by user and section (this month)
 * CRM & SRM/Reporting/All Months
 * CRM & SRM/Reporting/All Months/Cases by User and Section
 * CRM & SRM/Reporting/This Month/My cases by section (this month)
 * CRM & SRM/Reporting/All Months/My cases by section
 * CRM & SRM/Reporting/This Month/Cases by categories and section (this month)
 * CRM & SRM/Reporting/All Months/Cases by Categories and Section

.. i18n: Views
.. i18n: -----

Views
-----

.. i18n:  * report.crm.case.user.tree (tree)
.. i18n:  * report.crm.case.user.form (form)
.. i18n:  * report.crm.case.user.graph (graph)
.. i18n:  * report.crm.case.categ.tree (tree)
.. i18n:  * report.crm.case.categ.form (form)

 * report.crm.case.user.tree (tree)
 * report.crm.case.user.form (form)
 * report.crm.case.user.graph (graph)
 * report.crm.case.categ.tree (tree)
 * report.crm.case.categ.form (form)

.. i18n: Objects
.. i18n: -------

Objects
-------

.. i18n: Object: Cases by user and section (report.crm.case.user)
.. i18n: ########################################################

Object: Cases by user and section (report.crm.case.user)
########################################################

.. i18n: :amount_revenue_prob: Est. Rev*Prob., float, readonly

:amount_revenue_prob: Est. Rev*Prob., float, readonly

.. i18n: :amount_costs: Est.Cost, float, readonly

:amount_costs: Est.Cost, float, readonly

.. i18n: :user_id: User, many2one, readonly

:user_id: User, many2one, readonly

.. i18n: :name: Month, date, readonly

:name: Month, date, readonly

.. i18n: :probability: Avg. Probability, float, readonly

:probability: Avg. Probability, float, readonly

.. i18n: :nbr: # of Cases, integer, readonly

:nbr: # of Cases, integer, readonly

.. i18n: :section_id: Section, many2one, readonly

:section_id: Section, many2one, readonly

.. i18n: :state: Status, selection, readonly

:state: Status, selection, readonly

.. i18n: :amount_revenue: Est.Revenue, float, readonly

:amount_revenue: Est.Revenue, float, readonly

.. i18n: :delay_close: Delay to close, char, readonly

:delay_close: Delay to close, char, readonly

.. i18n: Object: Cases by section and category (report.crm.case.categ)
.. i18n: #############################################################

Object: Cases by section and category (report.crm.case.categ)
#############################################################

.. i18n: :amount_revenue_prob: Est. Rev*Prob., float, readonly

:amount_revenue_prob: Est. Rev*Prob., float, readonly

.. i18n: :amount_costs: Est.Cost, float, readonly

:amount_costs: Est.Cost, float, readonly

.. i18n: :name: Month, date, readonly

:name: Month, date, readonly

.. i18n: :probability: Avg. Probability, float, readonly

:probability: Avg. Probability, float, readonly

.. i18n: :nbr: # of Cases, integer, readonly

:nbr: # of Cases, integer, readonly

.. i18n: :section_id: Section, many2one, readonly

:section_id: Section, many2one, readonly

.. i18n: :state: Status, selection, readonly

:state: Status, selection, readonly

.. i18n: :amount_revenue: Est.Revenue, float, readonly

:amount_revenue: Est.Revenue, float, readonly

.. i18n: :delay_close: Delay Close, char, readonly

:delay_close: Delay Close, char, readonly

.. i18n: :categ_id: Category, many2one, readonly

:categ_id: Category, many2one, readonly
