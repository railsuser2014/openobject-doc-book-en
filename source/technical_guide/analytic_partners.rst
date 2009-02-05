
.. module:: analytic_partners
    :synopsis: Analytic accounts with multiple partners
    :noindex:
.. 

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

Analytic accounts with multiple partners (*analytic_partners*)
==============================================================
:Module: analytic_partners
:Name: Analytic accounts with multiple partners
:Version: 5.0.1.0
:Directory: analytic_partners
:Web: 
:Is certified: no

Description
-----------

::

  This module adds the possibility to assign multiple partners on
      the same analytic account. It's usefull when you do a management
      by affairs, where you can attach all suppliers and customers to
      a project.
  
      A report for the project manager is added to print the analytic
      account and all associated partners with their contacts.
  
      It's usefull to give to all members of a project, so that they
      get the contacts of all suppliers in this project.

Dependencies
------------

 * :mod:`account`

Reports
-------

 * Analytic Account with Partners

Menus
-------


None


Views
-----

 * \* INHERIT analytic_partners.analytic.account.form (form)


Objects
-------

None
