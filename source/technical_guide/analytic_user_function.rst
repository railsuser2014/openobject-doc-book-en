
.. module:: analytic_user_function
    :synopsis: Analytic User Function (Official, Quality Certified)
    :noindex:
.. 

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

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

Description
-----------

::

  This module allows you to define what is the default function of a specific user on a given account. 
  This is mostly used when a user encode his timesheet: the values are  retrieved and the fields are 
  auto-filled... but the possibility to change these values is still available.
  
      Obviously if no data has been recorded for the current account, the default value 
  is given as usual by the employee data so that this module is perfectly compatible with older configurations.

Dependencies
------------

 * :mod:`hr_timesheet_sheet`

Reports
-------

None


Menus
-------


None


Views
-----

 * analytic_user_funct_grid.tree (tree)
 * analytic_user_funct_grid.form (form)
 * \* INHERIT account.analytic.account.form (form)
 * \* INHERIT hr.timesheet.sheet.form (form)
 * \* INHERIT hr.analytic.timesheet.form (form)
 * \* INHERIT hr.analytic.timesheet.form (form)
 * \* INHERIT hr.analytic.timesheet.tree (tree)
 * \* INHERIT hr.analytic.timesheet.tree (tree)


Objects
-------

Object: Relation table between users and products on a analytic account (analytic_user_funct_grid)
##################################################################################################



:user_id: User, many2one, required





:product_id: Product, many2one, required





:account_id: Analytic Account, many2one, required


