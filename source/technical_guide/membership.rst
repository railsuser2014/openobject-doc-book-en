
Module Membership (*membership*)
================================
:Module: membership
:Name: Membership
:Version: 5.0.0.1
:Directory: membership
:Web: 

Description
-----------

::

  This module allows you to manage all operations for managing memberships.
  It supports different kind of members:
  * Free member
  * Associated member (ex: a group subscribe for a membership for all
    subsidiaries)
  * Paid members,
  * Special member prices, ...
  
  It is integrated with sales and accounting to allow you to automatically
  invoice and send propositions for membership renewal.

Dependencies
------------

 * base - installed
 * product - installed
 * account - installed
 * process - installed

Reports
-------

None


Menus
-------

 * Membership
 * Membership/Configuration
 * Membership/Configuration/Membership products
 * Membership/Current members
 * Membership/Current members/Paid members
 * Membership/Current members/Free members
 * Membership/Current members/Associated members
 * Membership/Current members/Invoiced members
 * Membership/Future members (invoice not confirmed)
 * Membership/Old members
 * Membership/Reporting
 * Membership/Reporting/Membership by Years
 * Membership/Reporting/New Membership by Years

Views
-----

 * Membership products (tree)
 * Membership products (form)
 * \* INHERIT Membership product (form)
 * Current members (tree)
 * \* INHERIT res.partner.tree.form.inherit (form)
 * \* INHERIT res.partner.form.inherit (form)
 * report.partner_member.year.tree (tree)
 * report.partner_member.year.tree (tree)
 * report.partner_member.year.graph1 (graph)
 * report.partner_member.year.graph2 (graph)
 * report.partner_member.year_new.tree (tree)
 * report.partner_member.year_new.tree (tree)
 * report.partner_member.year_new.graph1 (graph)
 * report.partner_member.year_new.graph2 (graph)
 * \* INHERIT product.normal.form (form)


Objects
-------

Object: Member line
###################

.. index::
  single: Member line object
.. 


:date_from: From, date



.. index::
  single: date_from field
.. 




:state: State, selection, readonly



.. index::
  single: state field
.. 




:account_invoice_line: Account Invoice line, many2one



.. index::
  single: account_invoice_line field
.. 




:date_to: To, date



.. index::
  single: date_to field
.. 




:partner: Partner, many2one



.. index::
  single: partner field
.. 




:date_cancel: Cancel date, date



.. index::
  single: date_cancel field
.. 



Object: Membership by Years
###########################

.. index::
  single: Membership by Years object
.. 


:waiting_number: Waiting, integer, readonly



.. index::
  single: waiting_number field
.. 




:paid_amount: Paid, float, readonly



.. index::
  single: paid_amount field
.. 




:invoiced_amount: Invoiced, float, readonly



.. index::
  single: invoiced_amount field
.. 




:paid_number: Paid, integer, readonly



.. index::
  single: paid_number field
.. 




:canceled_number: Canceled, integer, readonly



.. index::
  single: canceled_number field
.. 




:currency: Currency, many2one, readonly



.. index::
  single: currency field
.. 




:invoiced_number: Invoiced, integer, readonly



.. index::
  single: invoiced_number field
.. 




:year: Year, char, readonly



.. index::
  single: year field
.. 




:waiting_amount: Waiting, float, readonly



.. index::
  single: waiting_amount field
.. 




:canceled_amount: Canceled, float, readonly



.. index::
  single: canceled_amount field
.. 



Object: New Membership by Years
###############################

.. index::
  single: New Membership by Years object
.. 


:waiting_number: Waiting, integer, readonly



.. index::
  single: waiting_number field
.. 




:paid_amount: Paid, float, readonly



.. index::
  single: paid_amount field
.. 




:invoiced_amount: Invoiced, float, readonly



.. index::
  single: invoiced_amount field
.. 




:paid_number: Paid, integer, readonly



.. index::
  single: paid_number field
.. 




:canceled_number: Canceled, integer, readonly



.. index::
  single: canceled_number field
.. 




:currency: Currency, many2one, readonly



.. index::
  single: currency field
.. 




:invoiced_number: Invoiced, integer, readonly



.. index::
  single: invoiced_number field
.. 




:year: Year, char, readonly



.. index::
  single: year field
.. 




:waiting_amount: Waiting, float, readonly



.. index::
  single: waiting_amount field
.. 




:canceled_amount: Canceled, float, readonly



.. index::
  single: canceled_amount field
.. 

