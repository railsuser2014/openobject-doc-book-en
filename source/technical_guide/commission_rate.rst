
Module Sale Agent Information (*commission_rate*)
=================================================
:Module: commission_rate
:Name: Sale Agent Information
:Version: 5.0.0.1
:Directory: commission_rate
:Web: 

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

Object: Commission of month
###########################

.. index::
  single: Commission of month object
.. 


:inv_total: Invoice Amount, float, readonly



.. index::
  single: inv_total field
.. 




:name: Sales Agent Name, char, readonly



.. index::
  single: name field
.. 




:pdate: Invoice Paid Date, date, readonly



.. index::
  single: pdate field
.. 




:state: Invoice State, selection



.. index::
  single: state field
.. 




:productname: Product Name, char, readonly



.. index::
  single: productname field
.. 




:commission: Commissions Amount, float, readonly



.. index::
  single: commission field
.. 




:comrate: Commission Rate (%), float, readonly



.. index::
  single: comrate field
.. 




:in_date: Invoice Date, date, readonly



.. index::
  single: in_date field
.. 




:invno: Invoice Number, char, readonly



.. index::
  single: invno field
.. 




:product_quantity: Product Quantity, integer, readonly



.. index::
  single: product_quantity field
.. 




:sono: Sales Order No, char, readonly



.. index::
  single: sono field
.. 

