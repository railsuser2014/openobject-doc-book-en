
.. i18n: .. module:: report_intrastat
.. i18n:     :synopsis: Intrastat Reporting - Reporting (Official, Quality Certified)
.. i18n:     :noindex:
.. i18n: .. 

.. module:: report_intrastat
    :synopsis: Intrastat Reporting - Reporting (Official, Quality Certified)
    :noindex:
.. 

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. i18n: Intrastat Reporting - Reporting (*report_intrastat*)
.. i18n: ====================================================
.. i18n: :Module: report_intrastat
.. i18n: :Name: Intrastat Reporting - Reporting
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: report_intrastat
.. i18n: :Web: http://www.openerp.com
.. i18n: :Official module: yes
.. i18n: :Quality certified: yes

Intrastat Reporting - Reporting (*report_intrastat*)
====================================================
:Module: report_intrastat
:Name: Intrastat Reporting - Reporting
:Version: 5.0.1.0
:Author: Tiny
:Directory: report_intrastat
:Web: http://www.openerp.com
:Official module: yes
:Quality certified: yes

.. i18n: Description
.. i18n: -----------

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   A module that adds intrastat reports.

::

  A module that adds intrastat reports.

.. i18n: Dependencies
.. i18n: ------------

Dependencies
------------

.. i18n:  * :mod:`base`
.. i18n:  * :mod:`product`
.. i18n:  * :mod:`stock`
.. i18n:  * :mod:`sale`
.. i18n:  * :mod:`purchase`

 * :mod:`base`
 * :mod:`product`
 * :mod:`stock`
 * :mod:`sale`
 * :mod:`purchase`

.. i18n: Reports
.. i18n: -------

Reports
-------

.. i18n:  * Invoice Intrastat

 * Invoice Intrastat

.. i18n: Menus
.. i18n: -------

Menus
-------

.. i18n:  * Books/Configuration/Intrastat Code
.. i18n:  * Stock Management/Reporting/This Month
.. i18n:  * Stock Management/Reporting/This Month/Intrastat (this month)
.. i18n:  * Stock Management/Reporting/All Months
.. i18n:  * Stock Management/Reporting/All Months/Intrastat

 * Books/Configuration/Intrastat Code
 * Stock Management/Reporting/This Month
 * Stock Management/Reporting/This Month/Intrastat (this month)
 * Stock Management/Reporting/All Months
 * Stock Management/Reporting/All Months/Intrastat

.. i18n: Views
.. i18n: -----

Views
-----

.. i18n:  * \* INHERIT res.country.tree (form)
.. i18n:  * \* INHERIT res.country.form (form)
.. i18n:  * \* INHERIT product.normal.form (form)
.. i18n:  * report.intrastat.code.tree (tree)
.. i18n:  * report.intrastat.code.form (form)
.. i18n:  * report.intrastat.view (tree)

 * \* INHERIT res.country.tree (form)
 * \* INHERIT res.country.form (form)
 * \* INHERIT product.normal.form (form)
 * report.intrastat.code.tree (tree)
 * report.intrastat.code.form (form)
 * report.intrastat.view (tree)

.. i18n: Objects
.. i18n: -------

Objects
-------

.. i18n: Object: Intrastat code (report.intrastat.code)
.. i18n: ##############################################

Object: Intrastat code (report.intrastat.code)
##############################################

.. i18n: :name: Intrastat Code, char

:name: Intrastat Code, char

.. i18n: :description: Description, char

:description: Description, char

.. i18n: Object: Intrastat report (report.intrastat)
.. i18n: ###########################################

Object: Intrastat report (report.intrastat)
###########################################

.. i18n: :code: Country code, char, readonly

:code: Country code, char, readonly

.. i18n: :name: Month, date, readonly

:name: Month, date, readonly

.. i18n: :weight: Weight, float, readonly

:weight: Weight, float, readonly

.. i18n: :value: Value, float, readonly

:value: Value, float, readonly

.. i18n: :currency_id: Currency, many2one, readonly

:currency_id: Currency, many2one, readonly

.. i18n: :intrastat_id: Intrastat code, many2one, readonly

:intrastat_id: Intrastat code, many2one, readonly

.. i18n: :type: Type, selection

:type: Type, selection
