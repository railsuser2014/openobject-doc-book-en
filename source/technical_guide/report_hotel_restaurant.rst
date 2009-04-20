
.. module:: report_hotel_restaurant
    :synopsis: Restaurant Management - Reporting 
    :noindex:
.. 

.. raw:: html

      <br />
    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. tip:: This module is part of the Open ERP software, the leading Open Source 
  enterprise management system. If you want to discover Open ERP, check our 
  `screencasts <href="http://openerp.tv>`_ or download 
  `Open ERP <href="http://openerp.com>`_ directly.

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/report_hotel_restaurant"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Restaurant Management - Reporting (*report_hotel_restaurant*)
=============================================================
:Module: report_hotel_restaurant
:Name: Restaurant Management - Reporting
:Version: 5.0.1.0
:Author: Tiny
:Directory: report_hotel_restaurant
:Web: 
:Official module: no
:Quality certified: no

Description
-----------

::

  A module that adds new reports based on Reservation cases.

Download links
--------------

You can download this module as a zip file in the following version:

  * `trunk <http://www.openerp.com/download/modules/trunk/report_hotel_restaurant.zip>`_


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


