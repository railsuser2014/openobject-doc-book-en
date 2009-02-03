
.. module:: report_hotel_restaurant
    :synopsis: Restaurant Management - Reporting 
    :noindex:
.. 

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

    <style>
      div.body p#module-report_hotel_restaurant {
        display: none;
      }
    </style>

Restaurant Management - Reporting (*report_hotel_restaurant*)
=============================================================
:Module: report_hotel_restaurant
:Name: Restaurant Management - Reporting
:Version: 5.0.1.0
:Author: Tiny
:Directory: report_hotel_restaurant
:Web: 
:Is certified: no

Description
-----------

::

  A module that adds new reports based on Reservation cases.

Dependencies
------------

 * :mod:`hotel_restaurant`

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

Object: Reservation By State (report.hotel.restaurant.status)
#############################################################



:nbr: Reservation, integer, readonly





:state: State, selection, readonly





:reservation_id: Reservation No, char, readonly


