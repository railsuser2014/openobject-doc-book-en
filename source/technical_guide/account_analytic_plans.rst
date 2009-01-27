
Module Multiple-plans management in Analytic Accounting (*account_analytic_plans*)
==================================================================================
:Module: account_analytic_plans
:Name: Multiple-plans management in Analytic Accounting
:Version: 5.0.1.0
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

Dependencies
------------

 * account - installed
 * account_analytic_default - installed

Reports
-------

 * Crossovered Analytic

Menus
-------

 * Financial Management/Configuration/Analytic Accounting/Analytic Journal Definition/Analytic Distribution's models
 * Financial Management/Configuration/Analytic Accounting/Analytic Accounts/Analytic Plan

Views
-----

 * \* INHERIT account.journal.form.inherit (form)
 * \* INHERIT account.move.form.inherit (form)
 * \* INHERIT account.move.line.form.inherit (form)
 * \* INHERIT account.invoice.line.form.inherit (form)
 * \* INHERIT account.invoice.supplier.form.inherit (form)
 * account.analytic.plan.instance.form (form)
 * account.analytic.plan.instance.tree (tree)
 * account.analytic.plan.instance.line.form (form)
 * account.analytic.plan.instance.line.tree (tree)
 * account.analytic.plan.form (form)
 * account.analytic.plan.tree (tree)
 * account.analytic.plan.line.form (form)
 * account.analytic.plan.line.tree (tree)
 * \* INHERIT account.analytic.default.form.plans (form)
 * \* INHERIT account.analytic.default.tree.plans (tree)


Objects
-------

Object: Analytic Plans
######################

.. index::
  single: Analytic Plans object
.. 


:plan_ids: Analytic Plans, one2many



.. index::
  single: plan_ids field
.. 




:name: Analytic Plan, char, required



.. index::
  single: name field
.. 




:default_instance_id: Default Entries, many2one



.. index::
  single: default_instance_id field
.. 



Object: Analytic Plan Lines
###########################

.. index::
  single: Analytic Plan Lines object
.. 


:min_required: Minimum Allowed (%), float



.. index::
  single: min_required field
.. 




:plan_id: Analytic Plan, many2one



.. index::
  single: plan_id field
.. 




:name: Plan Name, char, required



.. index::
  single: name field
.. 




:max_required: Maximum Allowed (%), float



.. index::
  single: max_required field
.. 




:sequence: Sequence, integer



.. index::
  single: sequence field
.. 




:root_analytic_id: Root Account, many2one, required

    *Root account of this plan.*

.. index::
  single: root_analytic_id field
.. 



Object: Analytic Plan Instance
##############################

.. index::
  single: Analytic Plan Instance object
.. 


:account5_ids: Account5 Id, one2many



.. index::
  single: account5_ids field
.. 




:code: Distribution Code, char



.. index::
  single: code field
.. 




:plan_id: Model's Plan, many2one



.. index::
  single: plan_id field
.. 




:name: Analytic Distribution, char



.. index::
  single: name field
.. 




:account3_ids: Account3 Id, one2many



.. index::
  single: account3_ids field
.. 




:journal_id: Analytic Journal, many2one, required



.. index::
  single: journal_id field
.. 




:account6_ids: Account6 Id, one2many



.. index::
  single: account6_ids field
.. 




:account_ids: Account Id, one2many



.. index::
  single: account_ids field
.. 




:account4_ids: Account4 Id, one2many



.. index::
  single: account4_ids field
.. 




:account2_ids: Account2 Id, one2many



.. index::
  single: account2_ids field
.. 




:account1_ids: Account1 Id, one2many



.. index::
  single: account1_ids field
.. 



Object: Analytic Instance Line
##############################

.. index::
  single: Analytic Instance Line object
.. 


:analytic_account_id: Analytic Account, many2one, required



.. index::
  single: analytic_account_id field
.. 




:rate: Rate (%), float, required



.. index::
  single: rate field
.. 




:plan_id: Plan Id, many2one



.. index::
  single: plan_id field
.. 

