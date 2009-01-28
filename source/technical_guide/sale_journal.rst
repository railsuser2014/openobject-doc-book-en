
Managing sales and deliveries by journal (*sale_journal*)
=========================================================
:Module: sale_journal
:Name: Managing sales and deliveries by journal
:Version: 5.0.1.0
:Directory: sale_journal
:Web: http://www.openerp.com

Description
-----------

::

  The sale journal modules allows you to categorise your
      sales and deliveries (packing lists) between different journals.
      This module is very helpful for bigger companies that
      works by departments.
  
      You can use journal for different purposes, some examples:
      * isolate sales of different departments
      * journals for deliveries by truck or by UPS
  
      Journals have a responsible and evolves between different status:
      * draft, open, cancel, done.
  
      Batch operations can be processed on the different journals to
      confirm all sales at once, to validate or invoice packing, ...
  
      It also supports batch invoicing methods that can be configured by
      partners and sales orders, examples:
      * daily invoicing,
      * monthly invoicing, ...
  
      Some statistics by journals are provided.

Dependencies
------------

 * stock - installed
 * sale - installed

Reports
-------

None


Menus
-------

 * Sales Management/Configuration/Invoicing Methods
 * Sales Management/Configuration/Sales Journals
 * Sales Management/Sales by Journal
 * Sales Management/Sales by Journal/My Open Journals
 * Sales Management/Sales by Journal/All Open Journals
 * Sales Management/Reporting
 * Sales Management/Reporting/This Month
 * Sales Management/Reporting/This Month/Sales by Journal
 * Sales Management/Reporting/All Months
 * Sales Management/Reporting/All Months/Sales by Journal
 * Stock Management/Configuration/Packings Journals
 * Stock Management/Packings by Journal
 * Stock Management/Packings by Journal/My Open Journals
 * Stock Management/Packings by Journal/All Open Journals
 * Stock Management/Outgoing Products/Packings to Invoice
 * Stock Management/Outgoing Products/Packings to Invoice/Packings by Invoice Method
 * Stock Management/Reporting/Packings Journal
 * Stock Management/Reporting/Packings Journal/This Month
 * Stock Management/Reporting/Packings Journal/This Month/Packings by Invoice Method
 * Stock Management/Reporting/Packings Journal/All Months
 * Stock Management/Reporting/Packings Journal/All Months/Packings by Invoice Method
 * Stock Management/Reporting/Packings Journal/This Month/Packings by Journal
 * Stock Management/Reporting/Packings Journal/All Months/Packings by Journal

Views
-----

 * sale_journal.invoice.type.form (form)
 * sale_journal.invoice.type.tree (tree)
 * sale_journal.sale.journal.form (form)
 * sale_journal.sale.journal.tree (tree)
 * \* INHERIT sale.order.journal.view.form (form)
 * \* INHERIT sale.order.journal.view.tree (tree)
 * \* INHERIT stock.picking.journal.view.form (form)
 * \* INHERIT stock.picking.journal.view.tree (tree)
 * sale_journal.sale.stats.tree (tree)
 * sale_journal.sale.stats.form (form)
 * \* INHERIT res.partner.journal.property.form.inherit (form)
 * sale_journal.picking.journal.form (form)
 * sale_journal.picking.journal.tree (tree)
 * sale_journal.invoice.type.stats.form (form)
 * sale_journal.invoice.type.stats.tree (tree)
 * sale_journal.picking.stats.form (form)
 * sale_journal.picking.stats.tree (tree)


Objects
-------

Object: Invoice Types
#####################



:active: Active, boolean





:note: Note, text





:invoicing_method: Invoicing method, selection, required





:name: Invoice Type, char, required




Object: Sale Journal
####################



:code: Code, char, required





:user_id: Responsible, many2one, required





:name: Journal, char, required





:note: Note, text





:sale_stats_ids: Sale Stats, one2many, readonly





:state: State, selection, required





:date: Journal date, date, required





:date_created: Creation date, date, required, readonly





:date_validation: Validation date, date, readonly




Object: Packings Journal
########################



:code: Code, char, required





:user_id: Responsible, many2one, required





:name: Journal, char, required





:note: Note, text





:state: Creation date, selection, required





:picking_stats_ids: Journal Stats, one2many, readonly





:date: Journal date, date, required





:date_created: Creation date, date, required, readonly





:date_validation: Validation date, date, readonly




Object: Sales Orders by Journal
###############################



:count: # of Lines, integer, readonly





:price_total: Total Price, float, readonly





:name: Month, date, readonly





:state: Order State, selection, readonly





:journal_id: Journal, many2one, readonly





:price_average: Average Price, float, readonly





:quantity: Quantities, float, readonly




Object: Stats on packings by invoice method
###########################################



:count: # of Lines, integer, readonly





:price_total: Total Price, float, readonly





:name: Month, date, readonly





:price_average: Average Price, float, readonly





:invoice_state: Invoice state, selection, readonly





:state: State, selection, readonly





:invoice_type_id: Invoicing method, many2one, readonly





:quantity: Quantities, float, readonly




Object: Packing lists by Journal
################################



:count: # of Lines, integer, readonly





:price_total: Total Price, float, readonly





:name: Month, date, readonly





:state: State, selection, readonly





:journal_id: Journal, many2one, readonly





:price_average: Average Price, float, readonly





:quantity: Quantities, float, readonly


