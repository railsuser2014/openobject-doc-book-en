
.. module:: membership
    :synopsis: Membership
    :noindex:
.. 

Membership (*membership*)
=========================
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

Object: Member line (membership.membership_line)
################################################



:date_from: From, date





:state: State, selection, readonly





:account_invoice_line: Account Invoice line, many2one





:date_to: To, date





:partner: Partner, many2one





:date_cancel: Cancel date, date




Object: Membership by Years (report.partner_member.year)
########################################################



:waiting_number: Waiting, integer, readonly





:paid_amount: Paid, float, readonly





:invoiced_amount: Invoiced, float, readonly





:paid_number: Paid, integer, readonly





:canceled_number: Canceled, integer, readonly





:currency: Currency, many2one, readonly





:invoiced_number: Invoiced, integer, readonly





:year: Year, char, readonly





:waiting_amount: Waiting, float, readonly





:canceled_amount: Canceled, float, readonly




Object: New Membership by Years (report.partner_member.year_new)
################################################################



:waiting_number: Waiting, integer, readonly





:paid_amount: Paid, float, readonly





:invoiced_amount: Invoiced, float, readonly





:paid_number: Paid, integer, readonly





:canceled_number: Canceled, integer, readonly





:currency: Currency, many2one, readonly





:invoiced_number: Invoiced, integer, readonly





:year: Year, char, readonly





:waiting_amount: Waiting, float, readonly





:canceled_amount: Canceled, float, readonly


