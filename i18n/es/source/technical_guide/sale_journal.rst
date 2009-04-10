
.. i18n: .. module:: sale_journal
.. i18n:     :synopsis: Managing sales and deliveries by journal (Official, Quality Certified)
.. i18n:     :noindex:
.. i18n: .. 

.. module:: sale_journal
    :synopsis: Managing sales and deliveries by journal (Official, Quality Certified)
    :noindex:
.. 

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. i18n: Managing sales and deliveries by journal (*sale_journal*)
.. i18n: =========================================================
.. i18n: :Module: sale_journal
.. i18n: :Name: Managing sales and deliveries by journal
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: sale_journal
.. i18n: :Web: http://www.openerp.com
.. i18n: :Official module: yes
.. i18n: :Quality certified: yes

Managing sales and deliveries by journal (*sale_journal*)
=========================================================
:Module: sale_journal
:Name: Managing sales and deliveries by journal
:Version: 5.0.1.0
:Author: Tiny
:Directory: sale_journal
:Web: http://www.openerp.com
:Official module: yes
:Quality certified: yes

.. i18n: Description
.. i18n: -----------

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   The sale journal modules allows you to categorise your sales and deliveries (packing lists) 
.. i18n:   between different journals.
.. i18n:   This module is very helpful for bigger companies that works by departments.
.. i18n:   
.. i18n:       You can use journal for different purposes, some examples:
.. i18n:       * isolate sales of different departments
.. i18n:       * journals for deliveries by truck or by UPS
.. i18n:   
.. i18n:       Journals have a responsible and evolves between different status:
.. i18n:       * draft, open, cancel, done.
.. i18n:   
.. i18n:       Batch operations can be processed on the different journals to confirm all sales at once, 
.. i18n:       to validate or invoice packing, ...
.. i18n:   
.. i18n:       It also supports batch invoicing methods that can be configured by partners and sales orders, 
.. i18n:       examples:
.. i18n:       * daily invoicing,
.. i18n:       * monthly invoicing, ...
.. i18n:   
.. i18n:       Some statistics by journals are provided.

::

  The sale journal modules allows you to categorise your sales and deliveries (packing lists) 
  between different journals.
  This module is very helpful for bigger companies that works by departments.
  
      You can use journal for different purposes, some examples:
      * isolate sales of different departments
      * journals for deliveries by truck or by UPS
  
      Journals have a responsible and evolves between different status:
      * draft, open, cancel, done.
  
      Batch operations can be processed on the different journals to confirm all sales at once, 
      to validate or invoice packing, ...
  
      It also supports batch invoicing methods that can be configured by partners and sales orders, 
      examples:
      * daily invoicing,
      * monthly invoicing, ...
  
      Some statistics by journals are provided.

.. i18n: Dependencies
.. i18n: ------------

Dependencies
------------

.. i18n:  * :mod:`stock`
.. i18n:  * :mod:`sale`

 * :mod:`stock`
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

.. i18n:  * Sales Management/Configuration/Invoicing Methods
.. i18n:  * Sales Management/Configuration/Sales Journals
.. i18n:  * Sales Management/Sales by Journal
.. i18n:  * Sales Management/Sales by Journal/My Open Journals
.. i18n:  * Sales Management/Sales by Journal/All Open Journals
.. i18n:  * Sales Management/Reporting
.. i18n:  * Sales Management/Reporting/This Month
.. i18n:  * Sales Management/Reporting/This Month/Sales by Journal
.. i18n:  * Sales Management/Reporting/All Months
.. i18n:  * Sales Management/Reporting/All Months/Sales by Journal
.. i18n:  * Stock Management/Configuration/Packings Journals
.. i18n:  * Stock Management/Packings by Journal
.. i18n:  * Stock Management/Packings by Journal/My Open Journals
.. i18n:  * Stock Management/Packings by Journal/All Open Journals
.. i18n:  * Stock Management/Outgoing Products/Packings to Invoice
.. i18n:  * Stock Management/Outgoing Products/Packings to Invoice/Packings by Invoice Method
.. i18n:  * Stock Management/Reporting/Packings Journal
.. i18n:  * Stock Management/Reporting/Packings Journal/This Month
.. i18n:  * Stock Management/Reporting/Packings Journal/This Month/Packings by Invoice Method
.. i18n:  * Stock Management/Reporting/Packings Journal/All Months
.. i18n:  * Stock Management/Reporting/Packings Journal/All Months/Packings by Invoice Method
.. i18n:  * Stock Management/Reporting/Packings Journal/This Month/Packings by Journal
.. i18n:  * Stock Management/Reporting/Packings Journal/All Months/Packings by Journal

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

.. i18n: Views
.. i18n: -----

Views
-----

.. i18n:  * sale_journal.invoice.type.form (form)
.. i18n:  * sale_journal.invoice.type.tree (tree)
.. i18n:  * sale_journal.sale.journal.form (form)
.. i18n:  * sale_journal.sale.journal.tree (tree)
.. i18n:  * \* INHERIT sale.order.journal.view.form (form)
.. i18n:  * \* INHERIT sale.order.journal.view.tree (tree)
.. i18n:  * \* INHERIT stock.picking.journal.view.form (form)
.. i18n:  * \* INHERIT stock.picking.journal.view.tree (tree)
.. i18n:  * sale_journal.sale.stats.tree (tree)
.. i18n:  * sale_journal.sale.stats.form (form)
.. i18n:  * \* INHERIT res.partner.journal.property.form.inherit (form)
.. i18n:  * sale_journal.picking.journal.form (form)
.. i18n:  * sale_journal.picking.journal.tree (tree)
.. i18n:  * sale_journal.invoice.type.stats.form (form)
.. i18n:  * sale_journal.invoice.type.stats.tree (tree)
.. i18n:  * sale_journal.picking.stats.form (form)
.. i18n:  * sale_journal.picking.stats.tree (tree)

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

.. i18n: Objects
.. i18n: -------

Objects
-------

.. i18n: Object: Invoice Types (sale_journal.invoice.type)
.. i18n: #################################################

Object: Invoice Types (sale_journal.invoice.type)
#################################################

.. i18n: :active: Active, boolean

:active: Active, boolean

.. i18n: :note: Note, text

:note: Note, text

.. i18n: :invoicing_method: Invoicing method, selection, required

:invoicing_method: Invoicing method, selection, required

.. i18n: :name: Invoice Type, char, required

:name: Invoice Type, char, required

.. i18n: Object: Sale Journal (sale_journal.sale.journal)
.. i18n: ################################################

Object: Sale Journal (sale_journal.sale.journal)
################################################

.. i18n: :code: Code, char, required

:code: Code, char, required

.. i18n: :user_id: Responsible, many2one, required

:user_id: Responsible, many2one, required

.. i18n: :name: Journal, char, required

:name: Journal, char, required

.. i18n: :note: Note, text

:note: Note, text

.. i18n: :sale_stats_ids: Sale Stats, one2many, readonly

:sale_stats_ids: Sale Stats, one2many, readonly

.. i18n: :state: State, selection, required

:state: State, selection, required

.. i18n: :date: Journal date, date, required

:date: Journal date, date, required

.. i18n: :date_created: Creation date, date, required, readonly

:date_created: Creation date, date, required, readonly

.. i18n: :date_validation: Validation date, date, readonly

:date_validation: Validation date, date, readonly

.. i18n: Object: Packings Journal (sale_journal.picking.journal)
.. i18n: #######################################################

Object: Packings Journal (sale_journal.picking.journal)
#######################################################

.. i18n: :code: Code, char, required

:code: Code, char, required

.. i18n: :user_id: Responsible, many2one, required

:user_id: Responsible, many2one, required

.. i18n: :name: Journal, char, required

:name: Journal, char, required

.. i18n: :note: Note, text

:note: Note, text

.. i18n: :state: Creation date, selection, required

:state: Creation date, selection, required

.. i18n: :picking_stats_ids: Journal Stats, one2many, readonly

:picking_stats_ids: Journal Stats, one2many, readonly

.. i18n: :date: Journal date, date, required

:date: Journal date, date, required

.. i18n: :date_created: Creation date, date, required, readonly

:date_created: Creation date, date, required, readonly

.. i18n: :date_validation: Validation date, date, readonly

:date_validation: Validation date, date, readonly

.. i18n: Object: Sales Orders by Journal (sale_journal.sale.stats)
.. i18n: #########################################################

Object: Sales Orders by Journal (sale_journal.sale.stats)
#########################################################

.. i18n: :count: # of Lines, integer, readonly

:count: # of Lines, integer, readonly

.. i18n: :price_total: Total Price, float, readonly

:price_total: Total Price, float, readonly

.. i18n: :name: Month, date, readonly

:name: Month, date, readonly

.. i18n: :state: Order State, selection, readonly

:state: Order State, selection, readonly

.. i18n: :journal_id: Journal, many2one, readonly

:journal_id: Journal, many2one, readonly

.. i18n: :price_average: Average Price, float, readonly

:price_average: Average Price, float, readonly

.. i18n: :quantity: Quantities, float, readonly

:quantity: Quantities, float, readonly

.. i18n: Object: Stats on packings by invoice method (sale_journal.invoice.type.stats)
.. i18n: #############################################################################

Object: Stats on packings by invoice method (sale_journal.invoice.type.stats)
#############################################################################

.. i18n: :count: # of Lines, integer, readonly

:count: # of Lines, integer, readonly

.. i18n: :price_total: Total Price, float, readonly

:price_total: Total Price, float, readonly

.. i18n: :name: Month, date, readonly

:name: Month, date, readonly

.. i18n: :price_average: Average Price, float, readonly

:price_average: Average Price, float, readonly

.. i18n: :invoice_state: Invoice state, selection, readonly

:invoice_state: Invoice state, selection, readonly

.. i18n: :state: State, selection, readonly

:state: State, selection, readonly

.. i18n: :invoice_type_id: Invoicing method, many2one, readonly

:invoice_type_id: Invoicing method, many2one, readonly

.. i18n: :quantity: Quantities, float, readonly

:quantity: Quantities, float, readonly

.. i18n: Object: Packing lists by Journal (sale_journal.picking.stats)
.. i18n: #############################################################

Object: Packing lists by Journal (sale_journal.picking.stats)
#############################################################

.. i18n: :count: # of Lines, integer, readonly

:count: # of Lines, integer, readonly

.. i18n: :price_total: Total Price, float, readonly

:price_total: Total Price, float, readonly

.. i18n: :name: Month, date, readonly

:name: Month, date, readonly

.. i18n: :state: State, selection, readonly

:state: State, selection, readonly

.. i18n: :journal_id: Journal, many2one, readonly

:journal_id: Journal, many2one, readonly

.. i18n: :price_average: Average Price, float, readonly

:price_average: Average Price, float, readonly

.. i18n: :quantity: Quantities, float, readonly

:quantity: Quantities, float, readonly
