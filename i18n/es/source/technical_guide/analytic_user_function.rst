
.. i18n: .. module:: analytic_user_function
.. i18n:     :synopsis: Analytic User Function (Official, Quality Certified)
.. i18n:     :noindex:
.. i18n: .. 

.. module:: analytic_user_function
    :synopsis: Analytic User Function (Official, Quality Certified)
    :noindex:
.. 

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. i18n: Analytic User Function (*analytic_user_function*)
.. i18n: =================================================
.. i18n: :Module: analytic_user_function
.. i18n: :Name: Analytic User Function
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: analytic_user_function
.. i18n: :Web: http://www.openerp.com
.. i18n: :Official module: yes
.. i18n: :Quality certified: yes

Analytic User Function (*analytic_user_function*)
=================================================
:Module: analytic_user_function
:Name: Analytic User Function
:Version: 5.0.1.0
:Author: Tiny
:Directory: analytic_user_function
:Web: http://www.openerp.com
:Official module: yes
:Quality certified: yes

.. i18n: Description
.. i18n: -----------

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   This module allows you to define what is the default function of a specific user on a given account. 
.. i18n:   This is mostly used when a user encode his timesheet: the values are  retrieved and the fields are 
.. i18n:   auto-filled... but the possibility to change these values is still available.
.. i18n:   
.. i18n:       Obviously if no data has been recorded for the current account, the default value 
.. i18n:   is given as usual by the employee data so that this module is perfectly compatible with older configurations.

::

  This module allows you to define what is the default function of a specific user on a given account. 
  This is mostly used when a user encode his timesheet: the values are  retrieved and the fields are 
  auto-filled... but the possibility to change these values is still available.
  
      Obviously if no data has been recorded for the current account, the default value 
  is given as usual by the employee data so that this module is perfectly compatible with older configurations.

.. i18n: Dependencies
.. i18n: ------------

Dependencies
------------

.. i18n:  * :mod:`hr_timesheet_sheet`

 * :mod:`hr_timesheet_sheet`

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

.. i18n: None

None

.. i18n: Views
.. i18n: -----

Views
-----

.. i18n:  * analytic_user_funct_grid.tree (tree)
.. i18n:  * analytic_user_funct_grid.form (form)
.. i18n:  * \* INHERIT account.analytic.account.form (form)
.. i18n:  * \* INHERIT hr.timesheet.sheet.form (form)
.. i18n:  * \* INHERIT hr.analytic.timesheet.form (form)
.. i18n:  * \* INHERIT hr.analytic.timesheet.form (form)
.. i18n:  * \* INHERIT hr.analytic.timesheet.tree (tree)
.. i18n:  * \* INHERIT hr.analytic.timesheet.tree (tree)

 * analytic_user_funct_grid.tree (tree)
 * analytic_user_funct_grid.form (form)
 * \* INHERIT account.analytic.account.form (form)
 * \* INHERIT hr.timesheet.sheet.form (form)
 * \* INHERIT hr.analytic.timesheet.form (form)
 * \* INHERIT hr.analytic.timesheet.form (form)
 * \* INHERIT hr.analytic.timesheet.tree (tree)
 * \* INHERIT hr.analytic.timesheet.tree (tree)

.. i18n: Objects
.. i18n: -------

Objects
-------

.. i18n: Object: Relation table between users and products on a analytic account (analytic_user_funct_grid)
.. i18n: ##################################################################################################

Object: Relation table between users and products on a analytic account (analytic_user_funct_grid)
##################################################################################################

.. i18n: :user_id: User, many2one, required

:user_id: User, many2one, required

.. i18n: :product_id: Product, many2one, required

:product_id: Product, many2one, required

.. i18n: :account_id: Analytic Account, many2one, required

:account_id: Analytic Account, many2one, required
