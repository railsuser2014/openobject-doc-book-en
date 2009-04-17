
.. module:: l10n_fr_account_generation
    :synopsis: France - Generation de compte comptable tiers 
    :noindex:
.. 

.. raw:: html

      <br />
    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. tip:: This module is part of the Open ERP software, the leading Open Source 
  enterprise management system. If you want to discover Open ERP, check our 
  `screencasts <href="http://openerp.tv>`_ or download 
  `Open ERP <href="http://openerp.com>`_ directly.

France - Generation de compte comptable tiers (*l10n_fr_account_generation*)
============================================================================
:Module: l10n_fr_account_generation
:Name: France - Generation de compte comptable tiers
:Version: 5.0.1.0
:Author: SISTHEO
:Directory: l10n_fr_account_generation
:Web: http://www.openerp.com
:Official module: no
:Quality certified: no

Description
-----------

::

  Add a button in partners form for creating the payable and receive accounts in general account.
  
  Credits: Sistheo Zeekom

Download links
--------------

You can download this module as a zip file in the following version:

  * `trunk </download/modules/trunk/l10n_fr_account_generation.zip>`_


Dependencies
------------

 * :mod:`base`
 * :mod:`account`
 * :mod:`account_chart`

Reports
-------

None


Menus
-------

 * Financial Management/Configuration/Account generation config

Views
-----

 * \* INHERIT res.partner.form (form)
 * account.generation.config.form (form)


Objects
-------

Object: Account Generation Configuration (account.generation.config)
####################################################################



:customer: Global Customer, many2one





:supplier: Global Supplier, many2one





:name: Configuration Name, char, required





:nbcar: Char size, integer

    *Number of character for the creation of accounts*
