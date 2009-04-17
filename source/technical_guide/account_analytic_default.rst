
.. module:: account_analytic_default
    :synopsis: Account Analytic Default (Official, Quality Certified)
    :noindex:
.. 

.. raw:: html

      <br />
    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. tip:: This module is part of the Open ERP software, the leading Open Source 
  enterprise management system. If you want to discover Open ERP, check our 
  `screencasts <href="http://openerp.tv>`_ or download 
  `Open ERP <href="http://openerp.com>`_ directly.

Account Analytic Default (*account_analytic_default*)
=====================================================
:Module: account_analytic_default
:Name: Account Analytic Default
:Version: 5.0.1.0
:Author: Tiny
:Directory: account_analytic_default
:Web: http://www.openerp.com
:Official module: yes
:Quality certified: yes

Description
-----------

::

  Allows to automatically select analytic accounts based on criterions:
  * Product
  * Partner
  * User
  * Company
  * Date

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 </download/modules/5.0/account_analytic_default.zip>`_
  * `trunk </download/modules/trunk/account_analytic_default.zip>`_


Dependencies
------------

 * :mod:`account`

Reports
-------

None


Menus
-------

 * Financial Management/Configuration/Analytic Accounting/Analytic Defaults

Views
-----

 * account.analytic.default.tree (tree)
 * account.analytic.default.form (form)


Objects
-------

Object: Analytic Distributions (account.analytic.default)
#########################################################



:date_stop: End Date, date





:user_id: User, many2one





:product_id: Product, many2one





:sequence: Sequence, integer





:date_start: Start Date, date





:analytics_id: Analytic Distribution, many2one





:company_id: Company, many2one





:analytic_id: Analytic Account, many2one





:partner_id: Partner, many2one


