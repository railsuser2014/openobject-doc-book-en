
.. module:: account_simulation
    :synopsis: Accounting simulation journal 
    :noindex:
.. 

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

    <style>
      div.body p#module-account_simulation {
        display: none;
      }
    </style>

Accounting simulation journal (*account_simulation*)
====================================================
:Module: account_simulation
:Name: Accounting simulation journal
:Version: 5.0.1.0
:Author: Tiny
:Directory: account_simulation
:Web: http://tinyerp.com/module_account.html
:Is certified: no

Description
-----------

::

  Accounting simulation plan.

Dependencies
------------

 * :mod:`account`

Reports
-------

None


Menus
-------

 * Financial Management/Configuration/Financial Accounting/Financial Journals/Journal Simulations
 * Financial Management/Configuration/Financial Accounting/Financial Journals/Account Journal

Views
-----

 * account.journal.simulation.tree (tree)
 * account.journal.simulation.form (form)
 * \* INHERIT account.journal.simulation.form.inherit (form)
 * account.journal.tree (tree)


Objects
-------

Object: Simulation level (account.journal.simulation)
#####################################################



:code: Simulation code, char, required





:name: Simulation name, char, required


