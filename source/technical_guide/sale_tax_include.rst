
.. module:: sale_tax_include
    :synopsis: Invoices and prices with taxes included 
    :noindex:
.. 

.. raw:: html

      <br />
    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. tip:: This module is part of the Open ERP software, the leading Open Source 
  enterprise management system. If you want to discover Open ERP, check our 
  `screencasts <href="http://openerp.tv>`_ or download 
  `Open ERP <href="http://openerp.com>`_ directly.

Invoices and prices with taxes included (*sale_tax_include*)
============================================================
:Module: sale_tax_include
:Name: Invoices and prices with taxes included
:Version: 5.0.1.0
:Author: Tiny
:Directory: sale_tax_include
:Web: http://www.openerp.com
:Official module: no
:Quality certified: no

Description
-----------

::

  Allow the user to work tax included prices.
  Especially useful for b2c businesses.
      
  This module implement the modification on the sale order form.

Download links
--------------

You can download this module as a zip file in the following version:

  * `4.2 </download/modules/4.2/sale_tax_include.zip>`_
  * `trunk </download/modules/trunk/sale_tax_include.zip>`_


Dependencies
------------

 * :mod:`sale`
 * :mod:`account_tax_include`

Reports
-------

None


Menus
-------


None


Views
-----

 * \* INHERIT sale.order.exlcuded.view.form (form)
 * \* INHERIT sale.order.exlcuded.view.form (form)


Objects
-------

None
