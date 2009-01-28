
account_invoice_layout (*account_invoice_layout*)
=================================================
:Module: account_invoice_layout
:Name: account_invoice_layout
:Version: 5.0.1.0
:Directory: account_invoice_layout
:Web: http://www.openerp.com

Description
-----------

::

  This module provides some features to improve the layout of the invoices.
  
      It gives you the possibility to
          * order all the lines of an invoice
          * add titles, comment lines, sub total lines
          * draw horizontal lines and put page breaks
  
      Moreover, there is one option which allow you to print all the selected invoices with a given special message at the bottom of it. This feature can be very useful for printing your invoices with end-of-year wishes, special punctual conditions...

Dependencies
------------

 * base - installed
 * account - installed

Reports
-------

 * Invoices with Layout

Menus
-------

 * Financial Management/Configuration/Notification Message
 * Financial Management/Configuration/Notification Message/All Notification Messages

Views
-----

 * \* INHERIT account.invoice.line.form.inherit_1 (form)
 * \* INHERIT account.invoice.line.tree.inherit_1 (tree)
 * \* INHERIT account.invoice.line.tree.inherit_2 (tree)
 * \* INHERIT account.invoice.form.inherit_1 (form)
 * notify.message.tree (tree)
 * notify.message.form (form)


Objects
-------

Object: Notify By Messages
##########################



:msg: Special Message, text, required

    *This notification will appear at the bottom of the Invoices when printed.*



:name: Title, char, required


