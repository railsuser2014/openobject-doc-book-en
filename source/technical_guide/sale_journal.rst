
Module Managing sales and deliveries by journal (*sale_journal*)
================================================================
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

.. index::
  single: Invoice Types object
.. 


:active: Active, boolean



.. index::
  single: active field
.. 




:note: Note, text



.. index::
  single: note field
.. 




:invoicing_method: Invoicing method, selection, required



.. index::
  single: invoicing_method field
.. 




:name: Invoice Type, char, required



.. index::
  single: name field
.. 



Object: Sale Journal
####################

.. index::
  single: Sale Journal object
.. 


:code: Code, char, required



.. index::
  single: code field
.. 




:user_id: Responsible, many2one, required



.. index::
  single: user_id field
.. 




:name: Journal, char, required



.. index::
  single: name field
.. 




:note: Note, text



.. index::
  single: note field
.. 




:sale_stats_ids: Sale Stats, one2many, readonly



.. index::
  single: sale_stats_ids field
.. 




:state: State, selection, required



.. index::
  single: state field
.. 




:date: Journal date, date, required



.. index::
  single: date field
.. 




:date_created: Creation date, date, required, readonly



.. index::
  single: date_created field
.. 




:date_validation: Validation date, date, readonly



.. index::
  single: date_validation field
.. 



Object: Packings Journal
########################

.. index::
  single: Packings Journal object
.. 


:code: Code, char, required



.. index::
  single: code field
.. 




:user_id: Responsible, many2one, required



.. index::
  single: user_id field
.. 




:name: Journal, char, required



.. index::
  single: name field
.. 




:note: Note, text



.. index::
  single: note field
.. 




:state: Creation date, selection, required



.. index::
  single: state field
.. 




:picking_stats_ids: Journal Stats, one2many, readonly



.. index::
  single: picking_stats_ids field
.. 




:date: Journal date, date, required



.. index::
  single: date field
.. 




:date_created: Creation date, date, required, readonly



.. index::
  single: date_created field
.. 




:date_validation: Validation date, date, readonly



.. index::
  single: date_validation field
.. 



Object: Sales Orders by Journal
###############################

.. index::
  single: Sales Orders by Journal object
.. 


:count: # of Lines, integer, readonly



.. index::
  single: count field
.. 




:price_total: Total Price, float, readonly



.. index::
  single: price_total field
.. 




:name: Month, date, readonly



.. index::
  single: name field
.. 




:state: Order State, selection, readonly



.. index::
  single: state field
.. 




:journal_id: Journal, many2one, readonly



.. index::
  single: journal_id field
.. 




:price_average: Average Price, float, readonly



.. index::
  single: price_average field
.. 




:quantity: Quantities, float, readonly



.. index::
  single: quantity field
.. 



Object: Stats on packings by invoice method
###########################################

.. index::
  single: Stats on packings by invoice method object
.. 


:count: # of Lines, integer, readonly



.. index::
  single: count field
.. 




:price_total: Total Price, float, readonly



.. index::
  single: price_total field
.. 




:name: Month, date, readonly



.. index::
  single: name field
.. 




:price_average: Average Price, float, readonly



.. index::
  single: price_average field
.. 




:invoice_state: Invoice state, selection, readonly



.. index::
  single: invoice_state field
.. 




:state: State, selection, readonly



.. index::
  single: state field
.. 




:invoice_type_id: Invoicing method, many2one, readonly



.. index::
  single: invoice_type_id field
.. 




:quantity: Quantities, float, readonly



.. index::
  single: quantity field
.. 



Object: Packing lists by Journal
################################

.. index::
  single: Packing lists by Journal object
.. 


:count: # of Lines, integer, readonly



.. index::
  single: count field
.. 




:price_total: Total Price, float, readonly



.. index::
  single: price_total field
.. 




:name: Month, date, readonly



.. index::
  single: name field
.. 




:state: State, selection, readonly



.. index::
  single: state field
.. 




:journal_id: Journal, many2one, readonly



.. index::
  single: journal_id field
.. 




:price_average: Average Price, float, readonly



.. index::
  single: price_average field
.. 




:quantity: Quantities, float, readonly



.. index::
  single: quantity field
.. 

