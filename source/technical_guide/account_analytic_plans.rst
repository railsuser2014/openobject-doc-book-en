
Module Multiple-plans management in Analytic Accounting (*account_analytic_plans*)
==================================================================================
:Module: account_analytic_plans
:Name: Multiple-plans management in Analytic Accounting
:Version: False
:Directory: account_analytic_plans
:Web: http://www.openerp.com

Description
-----------

::
  
    This module allows to use several analytic plans, according to the general journal,
  so that multiple analytic lines are created when the invoice or the entries
  are confirmed.
  
  For example, you can define the following analytic structure:
    Projects
        Project 1
            SubProj 1.1
            SubProj 1.2
        Project 2
    Salesman
        Eric
        Fabien
  
  Here, we have two plans: Projects and Salesman. An invoice line must
  be able to write analytic entries in the 2 plans: SubProj 1.1 and
  Fabien. The amount can also be splitted. The following example is for
  an invoice that touches the two subproject and assigned to one salesman:
  
  Plan1:
      SubProject 1.1 : 50%
      SubProject 1.2 : 50%
  Plan2:
      Eric: 100%
  
  So when this line of invoice will be confirmed, it will generate 3 analytic lines,
  for one account entry.
          

Reports
-------

Menus
-------

Views
-----

Dependencies
------------

 * account - installed

 * account_analytic_default - uninstalled

Objects
-------