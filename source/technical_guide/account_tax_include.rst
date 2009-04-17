
.. module:: account_tax_include
    :synopsis: Invoices and prices with taxes included (Official, Quality Certified)
    :noindex:
.. 

.. raw:: html

      <br />
    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. tip:: This module is part of the Open ERP software, the leading Open Source 
  enterprise management system. If you want to discover Open ERP, check our 
  `screencasts <href="http://openerp.tv>`_ or download 
  `Open ERP <href="http://openerp.com>`_ directly.

Invoices and prices with taxes included (*account_tax_include*)
===============================================================
:Module: account_tax_include
:Name: Invoices and prices with taxes included
:Version: 5.0.1.0
:Author: Tiny
:Directory: account_tax_include
:Web: http://www.openerp.com
:Official module: yes
:Quality certified: yes

Description
-----------

::

  Allow the user to work tax included prices.
  Especially useful for b2c businesses.
      
  This module implement the modification on the invoice form.

Download links
--------------

You can download this module as a zip file in the following version:

  * `4.2 </download/modules/4.2/account_tax_include.zip>`_
  * `5.0 </download/modules/5.0/account_tax_include.zip>`_
  * `trunk </download/modules/trunk/account_tax_include.zip>`_


Dependencies
------------

 * :mod:`account`

Reports
-------

None


Menus
-------


None


Views
-----

 * \* INHERIT account.tax.exlcuded.view.form (form)
 * \* INHERIT account.invoice.vat.exlcuded.view.form (form)
 * \* INHERIT account.invoice.supplier.tax_include (form)
 * \* INHERIT account.invoice.supplier.tax_include2 (form)
 * \* INHERIT account.invoice.supplier.tax_include3 (form)
 * \* INHERIT account.invoice.line.tree (tree)


Objects
-------

None
