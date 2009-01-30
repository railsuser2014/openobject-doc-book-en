
.. module:: account_followup
    :synopsis: Accounting follow-ups management
    :noindex:
.. 

Accounting follow-ups management (*account_followup*)
=====================================================
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

Object: Follow-Ups (account_followup.followup)
##############################################



:followup_line: Follow-Up, one2many





:description: Description, text





:name: Name, char, required





:company_id: Company, many2one




Object: Follow-Ups Criteria (account_followup.followup.line)
############################################################



:description: Printed Message, text





:sequence: Sequence, integer





:delay: Days of delay, integer





:start: Type of Term, selection, required





:followup_id: Follow Ups, many2one, required





:name: Name, char, required




Object: Followup statistics (account_followup.stat)
###################################################



:balance: Balance, float, readonly





:account_type: Account Type, selection, readonly





:name: Partner, many2one, readonly





:date_move: First move, date, readonly





:credit: Credit, float, readonly





:date_move_last: Last move, date, readonly





:date_followup: Latest followup, date, readonly





:debit: Debit, float, readonly





:followup_id: Follow Ups, many2one, readonly


