
Module Accounting follow-ups management (*account_followup*)
============================================================
:Module: account_followup
:Name: Accounting follow-ups management
:Version: 5.0.1.0
:Directory: account_followup
:Web: http://www.openerp.com

Description
-----------

::

  Modules to automate letters for unpaid invoices, with multi-level recalls.
  
      You can define your multiple levels of recall through the menu:
          Financial Management/Configuration/Payment Terms/Follow-Ups
  
      Once it's defined, you can automatically prints recall every days
      through simply clicking on the menu:
          Financial_Management/Periodical_Processing/Print_Follow-Ups
  
      It will generate a PDF with all the letters according the the
      different levels of recall defined. You can define different policies
      for different companies.

Dependencies
------------

 * account - installed

Reports
-------

 * Followup Report

Menus
-------

 * Financial Management/Periodical Processing/Send followups
 * Financial Management/Configuration/Follow-Ups
 * Financial Management/Periodical Processing/Send followups/All receivable entries
 * Financial Management/Periodical Processing/Send followups/All payable entries
 * Financial Management/Reporting/Follow-Ups

Views
-----

 * account_followup.followup.line.form (form)
 * account_followup.followup.form (form)
 * account.move.line.partner.tree (tree)
 * \* INHERIT account.move.line.form.followup (form)
 * \* INHERIT account.move.line.tree.followup (form)
 * account_followup.stat.form (form)
 * account_followup.stat.tree (tree)


Objects
-------

Object: Follow-Ups
##################

.. index::
  single: Follow-Ups object
.. 


:followup_line: Follow-Up, one2many



.. index::
  single: followup_line field
.. 




:description: Description, text



.. index::
  single: description field
.. 




:name: Name, char, required



.. index::
  single: name field
.. 




:company_id: Company, many2one



.. index::
  single: company_id field
.. 



Object: Follow-Ups Criteria
###########################

.. index::
  single: Follow-Ups Criteria object
.. 


:description: Printed Message, text



.. index::
  single: description field
.. 




:sequence: Sequence, integer



.. index::
  single: sequence field
.. 




:delay: Days of delay, integer



.. index::
  single: delay field
.. 




:start: Type of Term, selection, required



.. index::
  single: start field
.. 




:followup_id: Follow Ups, many2one, required



.. index::
  single: followup_id field
.. 




:name: Name, char, required



.. index::
  single: name field
.. 



Object: Followup statistics
###########################

.. index::
  single: Followup statistics object
.. 


:balance: Balance, float, readonly



.. index::
  single: balance field
.. 




:account_type: Account Type, selection, readonly



.. index::
  single: account_type field
.. 




:name: Partner, many2one, readonly



.. index::
  single: name field
.. 




:date_move: First move, date, readonly



.. index::
  single: date_move field
.. 




:credit: Credit, float, readonly



.. index::
  single: credit field
.. 




:date_move_last: Last move, date, readonly



.. index::
  single: date_move_last field
.. 




:date_followup: Latest followup, date, readonly



.. index::
  single: date_followup field
.. 




:debit: Debit, float, readonly



.. index::
  single: debit field
.. 




:followup_id: Follow Ups, many2one, readonly



.. index::
  single: followup_id field
.. 

