
.. i18n: .. module:: account_coda_2_1_d
.. i18n:     :synopsis: Account CODA Version 2.1 D 
.. i18n:     :noindex:
.. i18n: .. 

.. module:: account_coda_2_1_d
    :synopsis: Account CODA Version 2.1 D 
    :noindex:
.. 

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. i18n: Account CODA Version 2.1 D (*account_coda_2_1_d*)
.. i18n: =================================================
.. i18n: :Module: account_coda_2_1_d
.. i18n: :Name: Account CODA Version 2.1 D
.. i18n: :Version: 5.0.1.0.1
.. i18n: :Author: Open ERP
.. i18n: :Directory: account_coda_2_1_d
.. i18n: :Web: 
.. i18n: :Official module: no
.. i18n: :Quality certified: no

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

.. i18n: Description
.. i18n: -----------

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   Module provides functionality to import bank statements from .csv file.
.. i18n:   Import coda file wizard is used to import bank statements.

::

  Module provides functionality to import bank statements from .csv file.
  Import coda file wizard is used to import bank statements.

.. i18n: Dependencies
.. i18n: ------------

Dependencies
------------

.. i18n:  * :mod:`base`
.. i18n:  * :mod:`account`
.. i18n:  * :mod:`account_report`
.. i18n:  * :mod:`base_iban`

 * :mod:`base`
 * :mod:`account`
 * :mod:`account_report`
 * :mod:`base_iban`

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

.. i18n:  * Financial Management/Reporting/Coda Statements
.. i18n:  * Financial Management/Periodical Processing/Import Coda Statements

 * Financial Management/Reporting/Coda Statements
 * Financial Management/Periodical Processing/Import Coda Statements

.. i18n: Views
.. i18n: -----

Views
-----

.. i18n:  * account.coda.form (form)
.. i18n:  * account.coda.tree (tree)

 * account.coda.form (form)
 * account.coda.tree (tree)

.. i18n: Objects
.. i18n: -------

Objects
-------

.. i18n: Object: CODA Format For Account (account.coda)
.. i18n: ##############################################

Object: CODA Format For Account (account.coda)
##############################################

.. i18n: :user_id: User, many2one, readonly

:user_id: User, many2one, readonly

.. i18n: :name: Coda file, binary, readonly

:name: Coda file, binary, readonly

.. i18n: :journal_id: Bank Journal, many2one, readonly

:journal_id: Bank Journal, many2one, readonly

.. i18n: :note: Import log, text, readonly

:note: Import log, text, readonly

.. i18n: :date: Import Date, date, readonly

:date: Import Date, date, readonly

.. i18n: :statement_id: Generated Bank Statement, many2one, readonly

:statement_id: Generated Bank Statement, many2one, readonly
