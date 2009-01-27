
Module Auction module (*auction*)
=================================
:Module: auction
:Name: Auction module
:Version: 5.0.1.0
:Directory: auction
:Web: 

Description
-----------

::

  This module provides functionality to 
       manage artists, articles, sellers, buyers and auction.
       Manage bids, track of sold, paid and unpaid objects.
       Delivery Management.

Dependencies
------------

 * base - installed
 * account - installed
 * hr_attendance - installed

Reports
-------

 * Listing Huissiers

 * Artists Biography

 * Bids phones

 * Bids

 * Code barres du lot

 * Lots List - Landscape

 * Auction Totals with lists

 * Buyer Form

 * Deposits

 * Seller Form

 * Seller List

 * Buyer List

 * Bids per lot (phone)

 * Results with buyer

Menus
-------

 * Auction Management
 * Auction Management/Configuration
 * Auction Management/Configuration/Define Artists
 * Auction Management/Configuration/Object Categories
 * Auction Management/Auction Dates
 * Auction Management/Auction Dates/Next Auction Dates
 * Auction Management/Auction Dates/Old Auction Dates
 * Auction Management/Auction Dates/New Auction Dates
 * Auction Management/Objects
 * Auction Management/Objects/All objects
 * Auction Management/Objects/All objects/Sold Objects
 * Auction Management/Objects/All objects/Objects to sell
 * Auction Management/Objects/All objects/Unplanned objects
 * Auction Management/Objects/All objects/Unsold Objects
 * Auction Management/Objects/All objects/Unclassified objects
 * Auction Management/Sellers
 * Auction Management/Sellers/Deposit border
 * Auction Management/Buyers
 * Auction Management/Buyers/Bids
 * Auction Management/Buyers/Bids/Bids line
 * Auction Management/Reporting
 * Auction Management/Reporting/Auction
 * Auction Management/Reporting/Auction/Auction's Summary
 * Auction Management/Reporting/Auction/Auction's Revenues
 * Auction Management/Reporting/Sellers
 * Auction Management/Reporting/Sellers/Seller's Summary
 * Auction Management/Reporting/Sellers/Seller's Revenues
 * Auction Management/Reporting/Buyer
 * Auction Management/Reporting/Buyer/Buyer's Summary
 * Auction Management/Reporting/Buyer/Buyer's Revenues
 * Auction Management/Reporting/Employees
 * Auction Management/Reporting/Employees/Comparison of estimations
 * Auction Management/Reporting/Manager
 * Auction Management/Reporting/Manager/Comparison of estimations
 * Auction Management/Reporting/Employees/Attendance
 * Auction Management/Reporting/Manager/Attendance
 * Auction Management/Reporting/Employees/My Latest Deposits
 * Auction Management/Reporting/Manager/Latest Deposits
 * Auction Management/Reporting/Manager/Encoded Objects Per Day
 * Auction Management/Reporting/Employees/My Encoded Objects Per Day
 * Auction Management/Objects/Objects by Auction
 * Auction Management/Reporting/Manager/Adjudication by Auction
 * Auction Management/Reporting/Manager/Depositer's Statistics
 * Auction Management/Reporting/Employees/Depositer's Statistics
 * Auction Management/Tools Bar Codes
 * Auction Management/Tools Bar Codes/Deliveries Management

Views
-----

 * auction.artists.tree (tree)
 * auction.artists.form (form)
 * auction.lot.category.tree (tree)
 * auction.lot.category.form (form)
 * Auction dates (tree)
 * Auction dates (form)
 * Auction lots (tree)
 * Auction lots (form)
 * Auction lots (graph)
 * Auction lots (tree)
 * Auction lots (form)
 * auction.lots.form3 (form)
 * Auction.deposit.tree (tree)
 * auction.deposit.form (form)
 * Deposit border (tree)
 * auction.bid_line.tree1 (tree)
 * auction.bid_line.form1 (form)
 * auction.bid.form (form)
 * auction.bid.tree (tree)
 * auction.reports.tree (tree)
 * auction.reports.form (form)
 * auction.reports.tree2 (tree)
 * Auction report (form)
 * Seller's auction (form)
 * Seller's auction (tree)
 * Seller's auction (graph)
 * Seller's auction (form)
 * Seller's auction (tree)
 * Seller's auction (graph)
 * Buyer's auction (form)
 * Buyer's auction (tree)
 * Buyer's auction (form)
 * Buyer's auction (tree)
 * Unplanned objects (tree)
 * Unplanned objects (form)
 * report.auction.estimation.adj.category.form (form)
 * report.auction.estimation.adj.category.tree (tree)
 * report.auction.estimation.adj.category.graph (graph)
 * report attendance (tree)
 * Graph attendance (graph)
 * Objects by date (tree)
 * Object date (form)
 * report.auction.object.date.graph (graph)
 * report.auction.adjudication.tree (tree)
 * report.auction.adjudication.graph (graph)
 * Depositer's statistics (tree)
 * report.object.encoded.form (form)
 * report.object.encoded.tree (tree)
 * report.object.encoded.graph (graph)
 * report.object.encoded.tree (tree)
 * report.object.encoded.graph (graph)
 * report.unclassified.objects (tree)


Objects
-------

Object: auction.artists
#######################

.. index::
  single: auction.artists object
.. 


:birth_death_dates: Birth / Death dates, char



.. index::
  single: birth_death_dates field
.. 




:pseudo: Pseudo, char



.. index::
  single: pseudo field
.. 




:name: Artist/Author Name, char, required



.. index::
  single: name field
.. 




:biography: Biography, text



.. index::
  single: biography field
.. 



Object: auction.dates
#####################

.. index::
  single: auction.dates object
.. 


:journal_seller_id: Seller Journal, many2one, required



.. index::
  single: journal_seller_id field
.. 




:expo1: First Exposition Day, date, required



.. index::
  single: expo1 field
.. 




:name: Auction date, char, required



.. index::
  single: name field
.. 




:expo2: Last Exposition Day, date, required



.. index::
  single: expo2 field
.. 




:acc_income: Income Account, many2one, required



.. index::
  single: acc_income field
.. 




:journal_id: Buyer Journal, many2one, required



.. index::
  single: journal_id field
.. 




:adj_total: Total Adjudication, float, readonly



.. index::
  single: adj_total field
.. 




:state: Status, selection, readonly



.. index::
  single: state field
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




:account_analytic_id: Analytic Account, many2one, required



.. index::
  single: account_analytic_id field
.. 




:seller_costs: Seller Costs, many2many



.. index::
  single: seller_costs field
.. 




:acc_expense: Expense Account, many2one, required



.. index::
  single: acc_expense field
.. 



Object: Deposit Border
######################

.. index::
  single: Deposit Border object
.. 


:info: Description, char



.. index::
  single: info field
.. 




:create_uid: Created by, many2one, readonly



.. index::
  single: create_uid field
.. 




:specific_cost_ids: Specific Costs, one2many



.. index::
  single: specific_cost_ids field
.. 




:name: Depositer Inventory, char, required



.. index::
  single: name field
.. 




:date_dep: Deposit date, date, required



.. index::
  single: date_dep field
.. 




:transfer: Transfer, boolean



.. index::
  single: transfer field
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



Object: auction.deposit.cost
############################

.. index::
  single: auction.deposit.cost object
.. 


:deposit_id: Deposit, many2one



.. index::
  single: deposit_id field
.. 




:account: Destination Account, many2one, required



.. index::
  single: account field
.. 




:amount: Amount, float



.. index::
  single: amount field
.. 




:name: Cost Name, char, required



.. index::
  single: name field
.. 



Object: auction.lot.category
############################

.. index::
  single: auction.lot.category object
.. 


:priority: Priority, float



.. index::
  single: priority field
.. 




:active: Active, boolean



.. index::
  single: active field
.. 




:name: Category Name, char, required



.. index::
  single: name field
.. 




:aie_categ: Aie Category, selection



.. index::
  single: aie_categ field
.. 



Object: Object
##############

.. index::
  single: Object object
.. 


:is_ok: Buyer's payment, boolean



.. index::
  single: is_ok field
.. 




:vnd_lim: Seller limit, float



.. index::
  single: vnd_lim field
.. 




:statement_id: Payment, many2many



.. index::
  single: statement_id field
.. 




:image: Image, binary



.. index::
  single: image field
.. 




:obj_num: Catalog Number, integer



.. index::
  single: obj_num field
.. 




:lot_num: List Number, integer, required



.. index::
  single: lot_num field
.. 




:ach_uid: Buyer, many2one



.. index::
  single: ach_uid field
.. 




:sel_inv_id: Seller Invoice, many2one, readonly



.. index::
  single: sel_inv_id field
.. 




:vnd_lim_net: Net limit ?, boolean, readonly



.. index::
  single: vnd_lim_net field
.. 




:bord_vnd_id: Depositer Inventory, many2one, required



.. index::
  single: bord_vnd_id field
.. 




:ach_emp: Taken Away, boolean



.. index::
  single: ach_emp field
.. 




:create_uid: Created by, many2one, readonly



.. index::
  single: create_uid field
.. 




:net_revenue: Net revenue, float, readonly



.. index::
  single: net_revenue field
.. 




:artist2_id: Artist/Author 2, many2one



.. index::
  single: artist2_id field
.. 




:obj_comm: Commission, boolean



.. index::
  single: obj_comm field
.. 




:paid_ach: Buyer invoice reconciled, boolean, readonly



.. index::
  single: paid_ach field
.. 




:lot_local: Location, char



.. index::
  single: lot_local field
.. 




:state: Status, selection, required, readonly



.. index::
  single: state field
.. 




:costs: Indirect costs, float, readonly



.. index::
  single: costs field
.. 




:history_ids: Auction history, one2many



.. index::
  single: history_ids field
.. 




:artist_id: Artist/Author, many2one



.. index::
  single: artist_id field
.. 




:ach_login: Buyer Username, char



.. index::
  single: ach_login field
.. 




:gross_revenue: Gross revenue, float, readonly



.. index::
  single: gross_revenue field
.. 




:lot_type: Object category, selection



.. index::
  single: lot_type field
.. 




:author_right: Author rights, many2one



.. index::
  single: author_right field
.. 




:ach_avance: Buyer Advance, float



.. index::
  single: ach_avance field
.. 




:gross_margin: Gross Margin (%), float, readonly



.. index::
  single: gross_margin field
.. 




:important: To be Emphatized, boolean



.. index::
  single: important field
.. 




:name2: Short Description (2), char



.. index::
  single: name2 field
.. 




:lot_est1: Minimum Estimation, float



.. index::
  single: lot_est1 field
.. 




:lot_est2: Maximum Estimation, float



.. index::
  single: lot_est2 field
.. 




:name: Short Description, char, required



.. index::
  single: name field
.. 




:product_id: Product, many2one, required



.. index::
  single: product_id field
.. 




:net_margin: Net Margin (%), float, readonly



.. index::
  single: net_margin field
.. 




:ach_inv_id: Buyer Invoice, many2one, readonly



.. index::
  single: ach_inv_id field
.. 




:obj_price: Adjudication price, float



.. index::
  single: obj_price field
.. 




:obj_ret: Price retired, float



.. index::
  single: obj_ret field
.. 




:auction_id: Auction Date, many2one



.. index::
  single: auction_id field
.. 




:bid_lines: Bids, one2many



.. index::
  single: bid_lines field
.. 




:paid_vnd: Seller Paid, boolean



.. index::
  single: paid_vnd field
.. 




:buyer_price: Buyer price, float, readonly



.. index::
  single: buyer_price field
.. 




:obj_desc: Object Description, text



.. index::
  single: obj_desc field
.. 




:seller_price: Seller price, float, readonly



.. index::
  single: seller_price field
.. 



Object: Bid auctions
####################

.. index::
  single: Bid auctions object
.. 


:bid_lines: Bid, one2many



.. index::
  single: bid_lines field
.. 




:contact_tel: Contact, char



.. index::
  single: contact_tel field
.. 




:auction_id: Auction Date, many2one, required



.. index::
  single: auction_id field
.. 




:partner_id: Buyer Name, many2one, required



.. index::
  single: partner_id field
.. 




:name: Bid ID, char, required



.. index::
  single: name field
.. 



Object: Lot history
###################

.. index::
  single: Lot history object
.. 


:lot_id: Object, many2one, required



.. index::
  single: lot_id field
.. 




:price: Withdrawn price, float



.. index::
  single: price field
.. 




:auction_id: Auction date, many2one, required



.. index::
  single: auction_id field
.. 




:name: Date, date



.. index::
  single: name field
.. 



Object: Bid
###########

.. index::
  single: Bid object
.. 


:name: Bid date, char



.. index::
  single: name field
.. 




:auction: Auction Name, char



.. index::
  single: auction field
.. 




:price: Maximum Price, float



.. index::
  single: price field
.. 




:bid_id: Bid ID, many2one, required



.. index::
  single: bid_id field
.. 




:call: To be Called, boolean



.. index::
  single: call field
.. 




:lot_id: Object, many2one, required



.. index::
  single: lot_id field
.. 



Object: Auction Reporting on buyer view
#######################################

.. index::
  single: Auction Reporting on buyer view object
.. 


:total_price: Total Adj., float, readonly



.. index::
  single: total_price field
.. 




:auction: Auction date, many2one, readonly



.. index::
  single: auction field
.. 




:object: No of objects, integer, readonly



.. index::
  single: object field
.. 




:buyer: Buyer, many2one, readonly



.. index::
  single: buyer field
.. 




:avg_price: Avg Adj., float, readonly



.. index::
  single: avg_price field
.. 




:date: Create Date, date



.. index::
  single: date field
.. 




:buyer_login: Buyer Login, char, readonly



.. index::
  single: buyer_login field
.. 



Object: Auction Reporting on buyer view
#######################################

.. index::
  single: Auction Reporting on buyer view object
.. 


:gross_revenue: Gross Revenue, float, readonly



.. index::
  single: gross_revenue field
.. 




:net_revenue: Net Revenue, float, readonly



.. index::
  single: net_revenue field
.. 




:auction: Auction date, many2one, readonly



.. index::
  single: auction field
.. 




:net_margin: Net Margin, float, readonly



.. index::
  single: net_margin field
.. 




:date: Create Date, date, required



.. index::
  single: date field
.. 




:sumadj: Sum of adjustication, float, readonly



.. index::
  single: sumadj field
.. 




:buyer: Buyer, many2one, readonly



.. index::
  single: buyer field
.. 




:buyer_login: Buyer Login, char, readonly



.. index::
  single: buyer_login field
.. 



Object: Auction Reporting on seller view
########################################

.. index::
  single: Auction Reporting on seller view object
.. 


:total_price: Total adjudication, float, readonly



.. index::
  single: total_price field
.. 




:auction: Auction date, many2one, readonly



.. index::
  single: auction field
.. 




:object_number: No of Objects, integer, readonly



.. index::
  single: object_number field
.. 




:seller: Seller, many2one, readonly



.. index::
  single: seller field
.. 




:state: Status, selection, readonly



.. index::
  single: state field
.. 




:avg_estimation: Avg estimation, float, readonly



.. index::
  single: avg_estimation field
.. 




:avg_price: Avg adjudication, float, readonly



.. index::
  single: avg_price field
.. 




:date: Create Date, date, required



.. index::
  single: date field
.. 



Object: Auction Reporting on seller view2
#########################################

.. index::
  single: Auction Reporting on seller view2 object
.. 


:gross_revenue: Gross revenue, float, readonly



.. index::
  single: gross_revenue field
.. 




:sum_adj: Sum Adjustication, float, readonly



.. index::
  single: sum_adj field
.. 




:net_revenue: Net revenue, float, readonly



.. index::
  single: net_revenue field
.. 




:auction: Auction date, many2one, readonly



.. index::
  single: auction field
.. 




:seller: Seller, many2one, readonly



.. index::
  single: seller field
.. 




:date: Auction date, date, required



.. index::
  single: date field
.. 




:net_margin: Net margin, float, readonly



.. index::
  single: net_margin field
.. 



Object: Auction Reporting on  view2
###################################

.. index::
  single: Auction Reporting on  view2 object
.. 


:gross_revenue: Gross revenue, float, readonly



.. index::
  single: gross_revenue field
.. 




:obj_number: # of Objects, integer, readonly



.. index::
  single: obj_number field
.. 




:sum_adj: Sum of adjudication, float, readonly



.. index::
  single: sum_adj field
.. 




:net_revenue: Net revenue, float, readonly



.. index::
  single: net_revenue field
.. 




:auction: Auction date, many2one, readonly



.. index::
  single: auction field
.. 




:obj_margin_procent: Net margin (%), float, readonly



.. index::
  single: obj_margin_procent field
.. 




:obj_margin: Avg margin, float, readonly



.. index::
  single: obj_margin field
.. 




:date: Auction date, date, required



.. index::
  single: date field
.. 



Object: Auction Reporting on view1
##################################

.. index::
  single: Auction Reporting on view1 object
.. 


:obj_ret: # obj ret, integer, readonly



.. index::
  single: obj_ret field
.. 




:min_est: Minimum Estimation, float, readonly



.. index::
  single: min_est field
.. 




:nseller: No of sellers, float, readonly



.. index::
  single: nseller field
.. 




:nbuyer: No of buyers, float, readonly



.. index::
  single: nbuyer field
.. 




:nobjects: No of objects, float, readonly



.. index::
  single: nobjects field
.. 




:max_est: Maximum Estimation, float, readonly



.. index::
  single: max_est field
.. 




:auction_id: Auction date, many2one, readonly



.. index::
  single: auction_id field
.. 




:adj_price: Adjudication price, float, readonly



.. index::
  single: adj_price field
.. 



Object: Objects per day
#######################

.. index::
  single: Objects per day object
.. 


:month: Month, date



.. index::
  single: month field
.. 




:user_id: User, many2one



.. index::
  single: user_id field
.. 




:obj_num: # of Objects, integer



.. index::
  single: obj_num field
.. 




:name: Created date, date



.. index::
  single: name field
.. 



Object: comparaison estimate/adjudication 
##########################################

.. index::
  single: comparaison estimate/adjudication  object
.. 


:user_id: User, many2one



.. index::
  single: user_id field
.. 




:obj_price: Adjudication price, float



.. index::
  single: obj_price field
.. 




:lot_type: Object Type, selection



.. index::
  single: lot_type field
.. 




:adj_total: Total Adjudication, float



.. index::
  single: adj_total field
.. 




:date: Date, date, readonly



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



Object: report_auction_adjudication
###################################

.. index::
  single: report_auction_adjudication object
.. 


:date: Date, date, readonly



.. index::
  single: date field
.. 




:adj_total: Total Adjudication, float



.. index::
  single: adj_total field
.. 




:state: Status, selection



.. index::
  single: state field
.. 




:user_id: User, many2one



.. index::
  single: user_id field
.. 




:name: Auction date, many2one, readonly



.. index::
  single: name field
.. 



Object: Report Sign In/Out
##########################

.. index::
  single: Report Sign In/Out object
.. 


:total_attendance: Total, float, readonly



.. index::
  single: total_attendance field
.. 




:employee_id: Employee, many2one, readonly



.. index::
  single: employee_id field
.. 




:name: Date, date, readonly



.. index::
  single: name field
.. 



Object: Report deposit border
#############################

.. index::
  single: Report deposit border object
.. 


:total_marge: Total margin, float, readonly



.. index::
  single: total_marge field
.. 




:nb_obj: # of objects, float, readonly



.. index::
  single: nb_obj field
.. 




:bord: Depositer Inventory, char, required



.. index::
  single: bord field
.. 




:moy_est: Avg. Est, float, readonly



.. index::
  single: moy_est field
.. 




:seller: Seller, many2one



.. index::
  single: seller field
.. 



Object: Object encoded
######################

.. index::
  single: Object encoded object
.. 


:gross_revenue: Gross revenue, float, readonly



.. index::
  single: gross_revenue field
.. 




:user_id: User, many2one



.. index::
  single: user_id field
.. 




:obj_num: # of Encoded obj., integer, readonly



.. index::
  single: obj_num field
.. 




:net_revenue: Net revenue, float, readonly



.. index::
  single: net_revenue field
.. 




:obj_margin: Net margin, float, readonly



.. index::
  single: obj_margin field
.. 




:obj_ret: # obj ret, integer, readonly



.. index::
  single: obj_ret field
.. 




:state: Status, selection, required



.. index::
  single: state field
.. 




:date: Create Date, date, required



.. index::
  single: date field
.. 




:estimation: Estimation, float



.. index::
  single: estimation field
.. 




:adj: Adj., integer, readonly



.. index::
  single: adj field
.. 



Object: Object encoded
######################

.. index::
  single: Object encoded object
.. 


:gross_revenue: Gross revenue, float, readonly



.. index::
  single: gross_revenue field
.. 




:user_id: User, many2one



.. index::
  single: user_id field
.. 




:obj_num: # of Encoded obj., integer, readonly



.. index::
  single: obj_num field
.. 




:net_revenue: Net revenue, float, readonly



.. index::
  single: net_revenue field
.. 




:obj_ret: # obj ret, integer, readonly



.. index::
  single: obj_ret field
.. 




:obj_margin: Net margin, float, readonly



.. index::
  single: obj_margin field
.. 




:date: Create Date, date, required



.. index::
  single: date field
.. 




:estimation: Estimation, float



.. index::
  single: estimation field
.. 




:adj: Adj., integer, readonly



.. index::
  single: adj field
.. 



Object: Unclassified objects 
#############################

.. index::
  single: Unclassified objects  object
.. 


:name: Short Description, char, required



.. index::
  single: name field
.. 




:auction: Auction date, many2one, readonly



.. index::
  single: auction field
.. 




:obj_comm: Commission, boolean



.. index::
  single: obj_comm field
.. 




:obj_price: Adjudication price, float



.. index::
  single: obj_price field
.. 




:lot_type: Object category, selection



.. index::
  single: lot_type field
.. 




:state: Status, selection, required, readonly



.. index::
  single: state field
.. 




:lot_num: List Number, integer, required



.. index::
  single: lot_num field
.. 




:lot_est1: Minimum Estimation, float



.. index::
  single: lot_est1 field
.. 




:lot_est2: Maximum Estimation, float



.. index::
  single: lot_est2 field
.. 




:ach_login: Buyer Username, char



.. index::
  single: ach_login field
.. 




:bord_vnd_id: Depositer Inventory, many2one, required



.. index::
  single: bord_vnd_id field
.. 




:obj_num: Catalog Number, integer



.. index::
  single: obj_num field
.. 

