
.. i18n: .. module:: account_base
.. i18n:     :synopsis: Voucher-setup 
.. i18n:     :noindex:
.. i18n: .. 

.. module:: account_base
    :synopsis: Voucher-setup 
    :noindex:
.. 

.. i18n: .. raw:: html
.. i18n: 
.. i18n:       <br />
.. i18n:     <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. raw:: html

      <br />
    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. i18n: .. tip:: This module is part of the Open ERP software, the leading Open Source 
.. i18n:   enterprise management system. If you want to discover Open ERP, check our 
.. i18n:   `screencasts <http://openerp.tv>`_ or download 
.. i18n:   `Open ERP <http://openerp.com>`_ directly.

.. tip:: This module is part of the Open ERP software, the leading Open Source 
  enterprise management system. If you want to discover Open ERP, check our 
  `screencasts <http://openerp.tv>`_ or download 
  `Open ERP <http://openerp.com>`_ directly.

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/account_base"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/account_base"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Voucher-setup (*account_base*)
.. i18n: ==============================
.. i18n: :Module: account_base
.. i18n: :Name: Voucher-setup
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Axelor
.. i18n: :Directory: account_base
.. i18n: :Web: 
.. i18n: :Official module: no
.. i18n: :Quality certified: no

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

.. i18n: Description
.. i18n: -----------

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   None

::

  None

.. i18n: Download links
.. i18n: --------------

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:

You can download this module as a zip file in the following version:

.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/account_base.zip>`_

  * `trunk <http://www.openerp.com/download/modules/trunk/account_base.zip>`_

.. i18n: Dependencies
.. i18n: ------------

Dependencies
------------

.. i18n:  * :mod:`base`
.. i18n:  * :mod:`base_setup`

 * :mod:`base`
 * :mod:`base_setup`

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

.. i18n: None

None

.. i18n: Views
.. i18n: -----

Views
-----

.. i18n:  * \* INHERIT voucher.partner.form (form)
.. i18n:  * wizard.account.base.setup.form (form)

 * \* INHERIT voucher.partner.form (form)
 * wizard.account.base.setup.form (form)

.. i18n: Objects
.. i18n: -------

Objects
-------

.. i18n: Object: wizard.account.base.setup (wizard.account.base.setup)
.. i18n: #############################################################

Object: wizard.account.base.setup (wizard.account.base.setup)
#############################################################

.. i18n: :vat_no: VAT Number, char

:vat_no: VAT Number, char

.. i18n: :excise: Exices Number, char

:excise: Exices Number, char

.. i18n: :pan_no: PAN Number, char

:pan_no: PAN Number, char

.. i18n: :company_id: Company, many2one, required

:company_id: Company, many2one, required

.. i18n: :range: Range, char

:range: Range, char

.. i18n: :ser_tax: Service Tax Number, char

:ser_tax: Service Tax Number, char

.. i18n: :div: Division, char

:div: Division, char

.. i18n: :partner_id: Partner, many2one

:partner_id: Partner, many2one

.. i18n: :cst_no: CST Number, char

:cst_no: CST Number, char
