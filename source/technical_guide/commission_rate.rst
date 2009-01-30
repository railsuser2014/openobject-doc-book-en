
.. module:: commission_rate
    :synopsis: Sale Agent Information
    :noindex:
.. 

Sale Agent Information (*commission_rate*)
==========================================
:Module: commission_rate
:Name: Sale Agent Information
:Version: 5.0.0.1
:Directory: commission_rate
:Web: 
:Is certified: no

Description
-----------

::

  Sale agent Info

Dependencies
------------

 * base - installed
 * product - installed
 * sale - installed

Reports
-------

None


Menus
-------

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

Views
-----

 * saleagent.info.tree (tree)
 * saleagent.info.form (form)
 * \* INHERIT res.partner.form.inherit (form)
 * commission.month.form (form)
 * commission.month.form.tree (tree)
 * commission.all.form (form)
 * commission.all.form.tree (tree)


Objects
-------

Object: Commission of month (report.commission.month)
#####################################################



:inv_total: Invoice Amount, float, readonly





:name: Sales Agent Name, char, readonly





:pdate: Invoice Paid Date, date, readonly





:state: Invoice State, selection





:productname: Product Name, char, readonly





:commission: Commissions Amount, float, readonly





:comrate: Commission Rate (%), float, readonly





:in_date: Invoice Date, date, readonly





:invno: Invoice Number, char, readonly





:product_quantity: Product Quantity, integer, readonly





:sono: Sales Order No, char, readonly


