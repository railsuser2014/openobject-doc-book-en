
.. module:: account_coda_2_1_d
    :synopsis: Account CODA Version 2.1 D 
    :noindex:
.. 

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

Account CODA Version 2.1 D (*account_coda_2_1_d*)
=================================================
:Module: account_coda_2_1_d
:Name: Account CODA Version 2.1 D
:Version: 5.0.1.0.1
:Author: Open ERP
:Directory: account_coda_2_1_d
:Web: 
:Official module: no
:Quality certified: no

Description
-----------

::

  Module provides functionality to import bank statements from .csv file.
  Import coda file wizard is used to import bank statements.

Dependencies
------------

 * :mod:`base`
 * :mod:`account`
 * :mod:`account_report`
 * :mod:`base_iban`

Reports
-------

None


Menus
-------

 * Financial Management/Reporting/Coda Statements
 * Financial Management/Periodical Processing/Import Coda Statements

Views
-----

 * account.coda.form (form)
 * account.coda.tree (tree)


Objects
-------

Object: CODA Format For Account (account.coda)
##############################################



:user_id: User, many2one, readonly





:name: Coda file, binary, readonly





:journal_id: Bank Journal, many2one, readonly





:note: Import log, text, readonly





:date: Import Date, date, readonly





:statement_id: Generated Bank Statement, many2one, readonly


