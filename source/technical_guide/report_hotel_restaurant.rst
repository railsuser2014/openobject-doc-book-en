
Restaurant Management - Reporting (*report_hotel_restaurant*)
=============================================================
:Module: report_hotel_restaurant
:Name: Restaurant Management - Reporting
:Version: 5.0.1.0
:Directory: report_hotel_restaurant
:Web: 

Description
-----------

::

  A module that adds new reports based on Reservation cases.

Dependencies
------------

 * hotel_restaurant - installed

Reports
-------

None


Menus
-------

 * Hotel Restaurant
 * Hotel Restaurant/Reporting
 * Hotel Restaurant/Reporting/This Month
 * Hotel Restaurant/Reporting/This Month/States By restaurant
 * Hotel Restaurant/Reporting/This Month/States By Restaurant

Views
-----

 * report.hotel.restaurant.status.tree (tree)
 * report.hotel.restaurant.status.form (form)
 * report.hotel.restaurant.status.graph (graph)
 * report.hotel.restaurant.status.graph (graph)


Objects
-------

Object: Reservation By State
############################



:nbr: Reservation, integer, readonly





:state: State, selection, readonly





:reservation_id: Reservation No, char, readonly


