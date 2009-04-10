
.. i18n: .. module:: commission_rate
.. i18n:     :synopsis: Sale Agent Information 
.. i18n:     :noindex:
.. i18n: .. 

.. module:: commission_rate
    :synopsis: Sale Agent Information 
    :noindex:
.. 

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. i18n: Sale Agent Information (*commission_rate*)
.. i18n: ==========================================
.. i18n: :Module: commission_rate
.. i18n: :Name: Sale Agent Information
.. i18n: :Version: 5.0.0.1
.. i18n: :Author: Tiny
.. i18n: :Directory: commission_rate
.. i18n: :Web: 
.. i18n: :Official module: no
.. i18n: :Quality certified: no

Sale Agent Information (*commission_rate*)
==========================================
:Module: commission_rate
:Name: Sale Agent Information
:Version: 5.0.0.1
:Author: Tiny
:Directory: commission_rate
:Web: 
:Official module: no
:Quality certified: no

.. i18n: Description
.. i18n: -----------

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   Sale agent Info

::

  Sale agent Info

.. i18n: Dependencies
.. i18n: ------------

Dependencies
------------

.. i18n:  * :mod:`base`
.. i18n:  * :mod:`product`
.. i18n:  * :mod:`sale`

 * :mod:`base`
 * :mod:`product`
 * :mod:`sale`

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

.. i18n:  * Sales Management
.. i18n:  * Sales Management/Commissions
.. i18n:  * Sales Management/Commissions/Sales agent
.. i18n:  * Sales Management/Commissions/Reporting
.. i18n:  * Sales Management/Commissions/Reporting/This Month
.. i18n:  * Sales Management/Commissions/Reporting/This Month/All Commissions
.. i18n:  * Sales Management/Commissions/Reporting/This Month/Commissions with Opened Invoices
.. i18n:  * Sales Management/Commissions/Reporting/This Month/Commissions with Paid Invoices
.. i18n:  * Sales Management/Commissions/Reporting/All Months
.. i18n:  * Sales Management/Commissions/Reporting/All Months/All Commissions
.. i18n:  * Sales Management/Commissions/Reporting/All Months/Commissions with Opened Invoices
.. i18n:  * Sales Management/Commissions/Reporting/All Months/Commissions with Paid Invoices

 * Sales Management
 * Sales Management/Commissions
 * Sales Management/Commissions/Sales agent
 * Sales Management/Commissions/Reporting
 * Sales Management/Commissions/Reporting/This Month
 * Sales Management/Commissions/Reporting/This Month/All Commissions
 * Sales Management/Commissions/Reporting/This Month/Commissions with Opened Invoices
 * Sales Management/Commissions/Reporting/This Month/Commissions with Paid Invoices
 * Sales Management/Commissions/Reporting/All Months
 * Sales Management/Commissions/Reporting/All Months/All Commissions
 * Sales Management/Commissions/Reporting/All Months/Commissions with Opened Invoices
 * Sales Management/Commissions/Reporting/All Months/Commissions with Paid Invoices

.. i18n: Views
.. i18n: -----

Views
-----

.. i18n:  * saleagent.info.tree (tree)
.. i18n:  * saleagent.info.form (form)
.. i18n:  * \* INHERIT res.partner.form.inherit (form)
.. i18n:  * commission.month.form (form)
.. i18n:  * commission.month.form.tree (tree)
.. i18n:  * commission.all.form (form)
.. i18n:  * commission.all.form.tree (tree)

 * saleagent.info.tree (tree)
 * saleagent.info.form (form)
 * \* INHERIT res.partner.form.inherit (form)
 * commission.month.form (form)
 * commission.month.form.tree (tree)
 * commission.all.form (form)
 * commission.all.form.tree (tree)

.. i18n: Objects
.. i18n: -------

Objects
-------

.. i18n: Object: Commission of month (report.commission.month)
.. i18n: #####################################################

Object: Commission of month (report.commission.month)
#####################################################

.. i18n: :inv_total: Invoice Amount, float, readonly

:inv_total: Invoice Amount, float, readonly

.. i18n: :name: Sales Agent Name, char, readonly

:name: Sales Agent Name, char, readonly

.. i18n: :pdate: Invoice Paid Date, date, readonly

:pdate: Invoice Paid Date, date, readonly

.. i18n: :state: Invoice State, selection

:state: Invoice State, selection

.. i18n: :productname: Product Name, char, readonly

:productname: Product Name, char, readonly

.. i18n: :commission: Commissions Amount, float, readonly

:commission: Commissions Amount, float, readonly

.. i18n: :comrate: Commission Rate (%), float, readonly

:comrate: Commission Rate (%), float, readonly

.. i18n: :in_date: Invoice Date, date, readonly

:in_date: Invoice Date, date, readonly

.. i18n: :invno: Invoice Number, char, readonly

:invno: Invoice Number, char, readonly

.. i18n: :product_quantity: Product Quantity, integer, readonly

:product_quantity: Product Quantity, integer, readonly

.. i18n: :sono: Sales Order No, char, readonly

:sono: Sales Order No, char, readonly
