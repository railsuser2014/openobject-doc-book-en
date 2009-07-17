
.. i18n: .. module:: hotel_housekeeping
.. i18n:     :synopsis: Hotel Housekeeping 
.. i18n:     :noindex:
.. i18n: .. 

.. module:: hotel_housekeeping
    :synopsis: Hotel Housekeeping 
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/hotel_housekeeping"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/hotel_housekeeping"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Hotel Housekeeping (*hotel_housekeeping*)
.. i18n: =========================================
.. i18n: :Module: hotel_housekeeping
.. i18n: :Name: Hotel Housekeeping
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: hotel_housekeeping
.. i18n: :Web: 
.. i18n: :Official module: no
.. i18n: :Quality certified: no

Hotel Housekeeping (*hotel_housekeeping*)
=========================================
:Module: hotel_housekeeping
:Name: Hotel Housekeeping
:Version: 5.0.1.0
:Author: Tiny
:Directory: hotel_housekeeping
:Web: 
:Official module: no
:Quality certified: no

.. i18n: Description
.. i18n: -----------

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   Module for Hotel/Hotel Housekeeping. You can manage:
.. i18n:       * Housekeeping process
.. i18n:       * Housekeeping history room wise
.. i18n:   
.. i18n:         Different reports are also provided, mainly for hotel statistics.

::

  Module for Hotel/Hotel Housekeeping. You can manage:
      * Housekeeping process
      * Housekeeping history room wise
  
        Different reports are also provided, mainly for hotel statistics.

.. i18n: Download links
.. i18n: --------------

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:

You can download this module as a zip file in the following version:

.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/hotel_housekeeping.zip>`_

  * `trunk <http://www.openerp.com/download/modules/trunk/hotel_housekeeping.zip>`_

.. i18n: Dependencies
.. i18n: ------------

Dependencies
------------

.. i18n:  * :mod:`hotel`

 * :mod:`hotel`

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

.. i18n:  * Hotel Housekeeping
.. i18n:  * Hotel Housekeeping/Housekeeping
.. i18n:  * Hotel Housekeeping/Activity List
.. i18n:  * Hotel Housekeeping/Activity Types

 * Hotel Housekeeping
 * Hotel Housekeeping/Housekeeping
 * Hotel Housekeeping/Activity List
 * Hotel Housekeeping/Activity Types

.. i18n: Views
.. i18n: -----

Views
-----

.. i18n:  * hotel.housekeeping.form (form)
.. i18n:  * hotel.housekeeping.tree (tree)
.. i18n:  * housekeeping.activity.form (form)
.. i18n:  * housekeeping.activity.tree (tree)
.. i18n:  * hotel_housekeeping_activity_type_form (form)
.. i18n:  * hotel_housekeeping_activity_type_list (tree)

 * hotel.housekeeping.form (form)
 * hotel.housekeeping.tree (tree)
 * housekeeping.activity.form (form)
 * housekeeping.activity.tree (tree)
 * hotel_housekeeping_activity_type_form (form)
 * hotel_housekeeping_activity_type_list (tree)

.. i18n: Objects
.. i18n: -------

Objects
-------

.. i18n: Object: Reservation (hotel.housekeeping)
.. i18n: ########################################

Object: Reservation (hotel.housekeeping)
########################################

.. i18n: :room_no: Room No, many2one, required

:room_no: Room No, many2one, required

.. i18n: :quality: Quality, selection, required

:quality: Quality, selection, required

.. i18n: :state: state, selection, required, readonly

:state: state, selection, required, readonly

.. i18n: :activity_lines: Activities, one2many

:activity_lines: Activities, one2many

.. i18n: :current_date: Today's Date, date, required

:current_date: Today's Date, date, required

.. i18n: :inspect_date_time: Inspect Date Time, datetime, required

:inspect_date_time: Inspect Date Time, datetime, required

.. i18n: :inspector: Inspector, many2one, required

:inspector: Inspector, many2one, required

.. i18n: :clean_type: Clean Type, selection, required

:clean_type: Clean Type, selection, required

.. i18n: Object: Activity Type (hotel.housekeeping.activity.type)
.. i18n: ########################################################

Object: Activity Type (hotel.housekeeping.activity.type)
########################################################

.. i18n: :property_account_expense_categ: Expense Account, many2one

:property_account_expense_categ: Expense Account, many2one

.. i18n:     *This account will be used to value outgoing stock for the current product category*

    *This account will be used to value outgoing stock for the current product category*

.. i18n: :updated: Category updated on Magento, boolean

:updated: Category updated on Magento, boolean

.. i18n: :activity_id: category, many2one, required

:activity_id: category, many2one, required

.. i18n: :magento_product_attribute_set_id: Magento product attribute set id, integer

:magento_product_attribute_set_id: Magento product attribute set id, integer

.. i18n: :sequence: Sequence, integer

:sequence: Sequence, integer

.. i18n: :property_account_expense_europe: Expense Account for Europe, many2one

:property_account_expense_europe: Expense Account for Europe, many2one

.. i18n:     *This account will be used, instead of the default one, to value outgoing stock for the current product*

    *This account will be used, instead of the default one, to value outgoing stock for the current product*

.. i18n: :property_stock_journal: Stock journal, many2one

:property_stock_journal: Stock journal, many2one

.. i18n:     *This journal will be used for the accounting move generated by stock move*

    *This journal will be used for the accounting move generated by stock move*

.. i18n: :property_stock_account_input_categ: Stock Input Account, many2one

:property_stock_account_input_categ: Stock Input Account, many2one

.. i18n:     *This account will be used to value the input stock*

    *This account will be used to value the input stock*

.. i18n: :property_account_income_categ: Income Account, many2one

:property_account_income_categ: Income Account, many2one

.. i18n:     *This account will be used to value incoming stock for the current product category*

    *This account will be used to value incoming stock for the current product category*

.. i18n: :child_id: Child Categories, one2many

:child_id: Child Categories, one2many

.. i18n: :property_stock_account_output_categ: Stock Output Account, many2one

:property_stock_account_output_categ: Stock Output Account, many2one

.. i18n:     *This account will be used to value the output stock*

    *This account will be used to value the output stock*

.. i18n: :name: Name, char, required

:name: Name, char, required

.. i18n: :isactivitytype: Is Activity Type, boolean

:isactivitytype: Is Activity Type, boolean

.. i18n: :isroomtype: Is Room Type, boolean

:isroomtype: Is Room Type, boolean

.. i18n: :exportable: Export to website, boolean

:exportable: Export to website, boolean

.. i18n: :property_account_expense_world: Outside Europe Expense Account, many2one

:property_account_expense_world: Outside Europe Expense Account, many2one

.. i18n:     *This account will be used, instead of the default one, to value outgoing stock for the current product*

    *This account will be used, instead of the default one, to value outgoing stock for the current product*

.. i18n: :ismenutype: Is Menu Type, boolean

:ismenutype: Is Menu Type, boolean

.. i18n: :isservicetype: Is Service Type, boolean

:isservicetype: Is Service Type, boolean

.. i18n: :parent_id: Parent Category, many2one

:parent_id: Parent Category, many2one

.. i18n: :property_account_income_world: Outside Europe Income Account, many2one

:property_account_income_world: Outside Europe Income Account, many2one

.. i18n:     *This account will be used, instead of the default one, to value incoming stock for the current product*

    *This account will be used, instead of the default one, to value incoming stock for the current product*

.. i18n: :complete_name: Name, char, readonly

:complete_name: Name, char, readonly

.. i18n: :magento_product_type: Magento product type, integer

:magento_product_type: Magento product type, integer

.. i18n: :isamenitype: Is amenities Type, boolean

:isamenitype: Is amenities Type, boolean

.. i18n: :property_account_income_europe: Income Account for Europe, many2one

:property_account_income_europe: Income Account for Europe, many2one

.. i18n:     *This account will be used, instead of the default one, to value incoming stock for the current product*

    *This account will be used, instead of the default one, to value incoming stock for the current product*

.. i18n: :magento_id: Magento category id, integer

:magento_id: Magento category id, integer

.. i18n: Object: Housekeeping Activity List (housekeeping.activity)
.. i18n: ##########################################################

Object: Housekeeping Activity List (housekeeping.activity)
##########################################################

.. i18n: :categ_id: Category, many2one, required

:categ_id: Category, many2one, required

.. i18n: :name: Activity Name, char, required

:name: Activity Name, char, required

.. i18n: Object: Housekeeping Activities  (hotel.housekeeping.activities)
.. i18n: ################################################################

Object: Housekeeping Activities  (hotel.housekeeping.activities)
################################################################

.. i18n: :a_list: unknown, many2one

:a_list: unknown, many2one

.. i18n: :housekeeper: Housekeeper, many2one

:housekeeper: Housekeeper, many2one

.. i18n: :clean_start_time: Clean Start Time, datetime, required

:clean_start_time: Clean Start Time, datetime, required

.. i18n: :clean_end_time: Clean End Time, datetime, required

:clean_end_time: Clean End Time, datetime, required

.. i18n: :dirty: Dirty, boolean

:dirty: Dirty, boolean

.. i18n: :clean: Clean, boolean

:clean: Clean, boolean

.. i18n: :activity_name: Housekeeping Activity, many2one

:activity_name: Housekeeping Activity, many2one
