
.. module:: sale_payment
    :synopsis: Sale payment type 
    :noindex:
.. 

.. raw:: html

      <br />
    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. tip:: This module is part of the Open ERP software, the leading Open Source 
  enterprise management system. If you want to discover Open ERP, check our 
  `screencasts <href="http://openerp.tv>`_ or download 
  `Open ERP <href="http://openerp.com>`_ directly.

Sale payment type (*sale_payment*)
==================================
:Module: sale_payment
:Name: Sale payment type
:Version: 5.0.1.0
:Author: Zikzakmedia SL
:Directory: sale_payment
:Web: 
:Official module: no
:Quality certified: no

Description
-----------

::

  Adds payment type and bank account to sale process.
  
  The sale order inherits payment type and bank account (if the payment type is related to bank accounts) from partner as default. Next, the invoice based on this sale order inherits the payment information from it.
  
  Also computes payment type and bank account of invoices created from picking lists (extracted from partner info).
  
  Based on previous work of Readylan (version for 4.2).

Download links
--------------

You can download this module as a zip file in the following version:

  * `trunk </download/modules/trunk/sale_payment.zip>`_


Dependencies
------------

 * :mod:`account_payment`
 * :mod:`account_payment_extension`
 * :mod:`sale`
 * :mod:`stock`

Reports
-------

None


Menus
-------


None


Views
-----

 * \* INHERIT sale.order.form.sale_paytype (form)


Objects
-------

None
