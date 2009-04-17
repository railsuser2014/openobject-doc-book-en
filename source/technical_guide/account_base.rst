
.. module:: account_base
    :synopsis: Voucher-setup 
    :noindex:
.. 

.. raw:: html

      <br />
    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. tip:: This module is part of the Open ERP software, the leading Open Source 
  enterprise management system. If you want to discover Open ERP, check our 
  `screencasts <href="http://openerp.tv>`_ or download 
  `Open ERP <href="http://openerp.com>`_ directly.

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="account_base"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Voucher-setup (*account_base*)
==============================
:Module: account_base
:Name: Voucher-setup
:Version: 5.0.1.0
:Author: Axelor
:Directory: account_base
:Web: 
:Official module: no
:Quality certified: no

Description
-----------

::

  None

Download links
--------------

You can download this module as a zip file in the following version:

  * `trunk </download/modules/trunk/account_base.zip>`_


Dependencies
------------

 * :mod:`base`
 * :mod:`base_setup`

Reports
-------

None


Menus
-------


None


Views
-----

 * \* INHERIT voucher.partner.form (form)
 * wizard.account.base.setup.form (form)


Objects
-------

Object: wizard.account.base.setup (wizard.account.base.setup)
#############################################################



:vat_no: VAT Number, char





:excise: Exices Number, char





:pan_no: PAN Number, char





:company_id: Company, many2one, required





:range: Range, char





:ser_tax: Service Tax Number, char





:div: Division, char





:partner_id: Partner, many2one





:cst_no: CST Number, char


