
Module Account Analytic Default (*account_analytic_default*)
============================================================
:Module: account_analytic_default
:Name: Account Analytic Default
:Version: 5.0.1.0
:Directory: account_analytic_default
:Web: http://www.openerp.com

Description
-----------

::

  Allows to automatically select analytic accounts based on criterions:
  * Product
  * Partner
  * User
  * Company
  * Date

Dependencies
------------

 * account - installed

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

Object: Analytic Distributions
##############################

.. index::
  single: Analytic Distributions object
.. 


:date_stop: End Date, date



.. index::
  single: date_stop field
.. 




:user_id: User, many2one



.. index::
  single: user_id field
.. 




:product_id: Product, many2one



.. index::
  single: product_id field
.. 




:sequence: Sequence, integer



.. index::
  single: sequence field
.. 




:date_start: Start Date, date



.. index::
  single: date_start field
.. 




:analytics_id: Analytic Distribution, many2one



.. index::
  single: analytics_id field
.. 




:company_id: Company, many2one



.. index::
  single: company_id field
.. 




:analytic_id: Analytic Account, many2one



.. index::
  single: analytic_id field
.. 




:partner_id: Partner, many2one



.. index::
  single: partner_id field
.. 

