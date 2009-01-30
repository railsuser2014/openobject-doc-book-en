
.. module:: account_analytic_default
    :synopsis: Account Analytic Default
    :noindex:
.. 

Account Analytic Default (*account_analytic_default*)
=====================================================
:Module: account_analytic_default
:Name: Account Analytic Default
:Version: 5.0.1.0
:Directory: account_analytic_default
:Web: http://www.openerp.com
:Is certified: yes

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


