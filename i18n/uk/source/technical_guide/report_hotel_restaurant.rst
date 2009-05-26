
.. i18n: .. module:: report_hotel_restaurant
.. i18n:     :synopsis: Restaurant Management - Reporting 
.. i18n:     :noindex:
.. i18n: .. 

.. module:: report_hotel_restaurant
    :synopsis: Restaurant Management - Reporting 
    :noindex:
.. 

.. i18n: .. raw:: html
.. i18n: 
.. i18n:       <br />
.. i18n:     <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. raw:: html

      <br />
    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. i18n: .. tip:: This module is part of the Open ERP software, the leading Open Source 
.. i18n:   enterprise management system. If you want to discover Open ERP, check our 
.. i18n:   `screencasts <http://openerp.tv>`_ or download 
.. i18n:   `Open ERP <http://openerp.com>`_ directly.

.. tip:: This module is part of the Open ERP software, the leading Open Source 
  enterprise management system. If you want to discover Open ERP, check our 
  `screencasts <http://openerp.tv>`_ or download 
  `Open ERP <http://openerp.com>`_ directly.

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/report_hotel_restaurant"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/report_hotel_restaurant"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Restaurant Management - Reporting (*report_hotel_restaurant*)
.. i18n: =============================================================
.. i18n: :Module: report_hotel_restaurant
.. i18n: :Name: Restaurant Management - Reporting
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: report_hotel_restaurant
.. i18n: :Web: 
.. i18n: :Official module: no
.. i18n: :Quality certified: no

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

.. i18n: Description
.. i18n: -----------

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   A module that adds new reports based on Reservation cases.

::

  A module that adds new reports based on Reservation cases.

.. i18n: Download links
.. i18n: --------------

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:

You can download this module as a zip file in the following version:

.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/report_hotel_restaurant.zip>`_

  * `trunk <http://www.openerp.com/download/modules/trunk/report_hotel_restaurant.zip>`_

.. i18n: Dependencies
.. i18n: ------------

Dependencies
------------

.. i18n:  * :mod:`hotel_restaurant`

 * :mod:`hotel_restaurant`

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

.. i18n:  * Hotel Restaurant
.. i18n:  * Hotel Restaurant/Reporting
.. i18n:  * Hotel Restaurant/Reporting/This Month
.. i18n:  * Hotel Restaurant/Reporting/This Month/States By restaurant
.. i18n:  * Hotel Restaurant/Reporting/This Month/States By Restaurant

 * Hotel Restaurant
 * Hotel Restaurant/Reporting
 * Hotel Restaurant/Reporting/This Month
 * Hotel Restaurant/Reporting/This Month/States By restaurant
 * Hotel Restaurant/Reporting/This Month/States By Restaurant

.. i18n: Views
.. i18n: -----

Views
-----

.. i18n:  * report.hotel.restaurant.status.tree (tree)
.. i18n:  * report.hotel.restaurant.status.form (form)
.. i18n:  * report.hotel.restaurant.status.graph (graph)
.. i18n:  * report.hotel.restaurant.status.graph (graph)

 * report.hotel.restaurant.status.tree (tree)
 * report.hotel.restaurant.status.form (form)
 * report.hotel.restaurant.status.graph (graph)
 * report.hotel.restaurant.status.graph (graph)

.. i18n: Objects
.. i18n: -------

Objects
-------

.. i18n: Object: Reservation By State (report.hotel.restaurant.status)
.. i18n: #############################################################

Object: Reservation By State (report.hotel.restaurant.status)
#############################################################

.. i18n: :nbr: Reservation, integer, readonly

:nbr: Reservation, integer, readonly

.. i18n: :state: State, selection, readonly

:state: State, selection, readonly

.. i18n: :reservation_id: Reservation No, char, readonly

:reservation_id: Reservation No, char, readonly
