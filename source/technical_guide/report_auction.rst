
Module Auction Management - Reporting (*report_auction*)
========================================================
:Module: report_auction
:Name: Auction Management - Reporting
:Version: 5.0.1.0
:Directory: report_auction
:Web: http://tinyerp.com/module_auction.html

Description
-----------

::

  A module that adds new reports based on Auction.

Dependencies
------------

 * auction - installed
 * hr_timesheet_sheet - installed

Reports
-------

None


Menus
-------

 * Auction Management/Reporting/Manager
 * Auction Management/Reporting/Manager/Auction Adjudication
 * Auction Management/Reporting/Member
 * Auction Management/Reporting/Member/Auction Adjudication
 * Auction Management/Reporting/Member/Auction Adjudication
 * Auction Management/Reporting/Manager/Customer Per Seller
 * Auction Management/Reporting/Member/My Latest 10 Deposit
 * Auction Management/Reporting/Member/My Latest 10 Objects
 * Auction Management/Reporting/Member/Object Per Day
 * Auction Management/Reporting/Manager/Object Per Day
 * Auction Management/Reporting/Member/This Month
 * Auction Management/Reporting/Member/This Month/Estimation
 * Auction Management/Reporting/Member/This Month/Estimation/Adjudication
 * Auction Management/Reporting/Manager/This Month
 * Auction Management/Reporting/Manager/This Month/Estimation
 * Auction Management/Reporting/Manager/This Month/Estimation/Adjudication
 * Auction Management/Reporting/Member/Summury of Sign_in Sign_out
 * Auction Management/Reporting/Manager/Summury of Sign_in Sign_out

Views
-----

 * Auction adjudication (tree)
 * Auction adjudication (form)
 * report.auction.adjudication.graph1 (graph)
 * report.per.seller.customer.tree (tree)
 * Seller/customer (form)
 * report.per.seller.customer.graph (graph)
 * Latest deposit  (form)
 * Latest deposit (tree)
 * report.latest.objects.tree (tree)
 * Latest objects (form)
 * Object date (tree)
 * Object date (form)
 * report.auction.object.date.graph1 (graph)
 * report.auction.estimation.adj.category.tree1 (tree)
 * report.auction.estimation.adj.category.graph1 (graph)
 * report.auction.user.pointing.tree (tree)
 * report.auction.user.pointing.graph (graph)


Objects
-------

Object: report_auction_adjudication
###################################

.. index::
  single: report_auction_adjudication object
.. 


:name: Auction date, char, required



.. index::
  single: name field
.. 




:adj_total: Total Adjudication, float



.. index::
  single: adj_total field
.. 




:auction1: First Auction Day, date, required



.. index::
  single: auction1 field
.. 




:buyer_costs: Buyer Costs, many2many



.. index::
  single: buyer_costs field
.. 




:auction2: Last Auction Day, date, required



.. index::
  single: auction2 field
.. 




:seller_costs: Seller Costs, many2many



.. index::
  single: seller_costs field
.. 



Object: Customer per seller
###########################

.. index::
  single: Customer per seller object
.. 


:partner_id: Partner, many2one



.. index::
  single: partner_id field
.. 




:no_of_buyer: Buyer, integer



.. index::
  single: no_of_buyer field
.. 




:name: Seller, char, required



.. index::
  single: name field
.. 



Object: Latest 10 Deposits
##########################

.. index::
  single: Latest 10 Deposits object
.. 


:info: Description, char



.. index::
  single: info field
.. 




:specific_cost_ids: Specific Costs, one2many



.. index::
  single: specific_cost_ids field
.. 




:user_id: User, many2one



.. index::
  single: user_id field
.. 




:name: Depositer Inventory, char, required



.. index::
  single: name field
.. 




:date_dep: Deposit date, date, required



.. index::
  single: date_dep field
.. 




:total_neg: Allow Negative Amount, boolean



.. index::
  single: total_neg field
.. 




:lot_id: Objects, one2many



.. index::
  single: lot_id field
.. 




:partner_id: Seller, many2one, required



.. index::
  single: partner_id field
.. 




:method: Withdrawned method, selection, required



.. index::
  single: method field
.. 




:tax_id: Expenses, many2one



.. index::
  single: tax_id field
.. 



Object: Latest 10 Objects
#########################

.. index::
  single: Latest 10 Objects object
.. 


:user_id: User, many2one



.. index::
  single: user_id field
.. 




:obj_num: Catalog Number, integer



.. index::
  single: obj_num field
.. 




:obj_comm: Commission, boolean



.. index::
  single: obj_comm field
.. 




:obj_price: Adjudication price, float



.. index::
  single: obj_price field
.. 




:obj_desc: Object Description, text



.. index::
  single: obj_desc field
.. 




:obj_ret: Price retired, float



.. index::
  single: obj_ret field
.. 




:auction_id: Auction Date, many2one



.. index::
  single: auction_id field
.. 




:partner_id: Seller, many2one, required



.. index::
  single: partner_id field
.. 




:bord_vnd_id: Depositer Inventory, many2one, required



.. index::
  single: bord_vnd_id field
.. 



Object: Objects per day
#######################

.. index::
  single: Objects per day object
.. 


:obj_ret: Price retired, float



.. index::
  single: obj_ret field
.. 




:obj_num: Catalog Number, integer



.. index::
  single: obj_num field
.. 




:obj_comm: Commission, boolean



.. index::
  single: obj_comm field
.. 




:obj_price: Adjudication price, float



.. index::
  single: obj_price field
.. 




:bord_vnd_id: Depositer Inventory, many2one, required



.. index::
  single: bord_vnd_id field
.. 




:lot_type: Object Type, selection



.. index::
  single: lot_type field
.. 




:state: State, selection, required



.. index::
  single: state field
.. 




:auction_id: Auction Date, many2one



.. index::
  single: auction_id field
.. 




:lot_num: Quantity, integer, required



.. index::
  single: lot_num field
.. 




:date: Name, char, required



.. index::
  single: date field
.. 




:obj_desc: Object Description, text



.. index::
  single: obj_desc field
.. 




:name: Short Description, char, required



.. index::
  single: name field
.. 



Object: comparison estimate/adjudication 
#########################################

.. index::
  single: comparison estimate/adjudication  object
.. 


:obj_ret: Price retired, float



.. index::
  single: obj_ret field
.. 




:name: Short Description, char, required



.. index::
  single: name field
.. 




:obj_comm: Commission, boolean



.. index::
  single: obj_comm field
.. 




:obj_price: Adjudication price, float



.. index::
  single: obj_price field
.. 




:obj_desc: Object Description, text



.. index::
  single: obj_desc field
.. 




:lot_type: Object Type, selection



.. index::
  single: lot_type field
.. 




:adj_total: Total Adjudication, float



.. index::
  single: adj_total field
.. 




:state: State, selection, required



.. index::
  single: state field
.. 




:auction_id: Auction Date, many2one



.. index::
  single: auction_id field
.. 




:lot_num: Quantity, integer, required



.. index::
  single: lot_num field
.. 




:date: Name, char, required



.. index::
  single: date field
.. 




:lot_est1: Minimum Estimation, float



.. index::
  single: lot_est1 field
.. 




:lot_est2: Maximum Estimation, float



.. index::
  single: lot_est2 field
.. 




:bord_vnd_id: Depositer Inventory, many2one, required



.. index::
  single: bord_vnd_id field
.. 




:obj_num: Catalog Number, integer



.. index::
  single: obj_num field
.. 



Object: user pointing 
######################

.. index::
  single: user pointing  object
.. 


:total_timesheet: Project Timesheet, float



.. index::
  single: total_timesheet field
.. 




:sheet_id: Sheet, many2one



.. index::
  single: sheet_id field
.. 




:user_id: User, char, required



.. index::
  single: user_id field
.. 




:name: Date, date



.. index::
  single: name field
.. 

