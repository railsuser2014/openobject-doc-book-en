
.. i18n: .. index:: MPS
.. i18n: .. index:: Master Production Schedule
.. i18n: .. index:: Master Procurement Schedule

.. index:: MPS
.. index:: Master Production Schedule
.. index:: Master Procurement Schedule

.. i18n: Scheduling
.. i18n: ==========

Scheduling
==========

.. i18n: The master production plan, sometimes called the MPS (Master Production Schedule), enables you to
.. i18n: generate forecasts for incoming and outgoing material. It's based on forecasts of inputs and outputs
.. i18n: by the logistics manager.

The master production plan, sometimes called the MPS (Master Production Schedule), enables you to
generate forecasts for incoming and outgoing material. It's based on forecasts of inputs and outputs
by the logistics manager.

.. i18n: .. note:: MPS, Procurement and Production
.. i18n:    
.. i18n:    Open ERP distinguishes between Production, Purchase and Production.
.. i18n:    
.. i18n:    Production is manufacture, Purchase is the acquisition of goods from another party,
.. i18n:    and Procurement is either or both of those. So it would be better to call the
.. i18n:    MPS the Master Procurement Schedule. Which Open ERP does!

.. note:: MPS, Procurement and Production
   
   Open ERP distinguishes between Production, Purchase and Production.
   
   Production is manufacture, Purchase is the acquisition of goods from another party,
   and Procurement is either or both of those. So it would be better to call the
   MPS the Master Procurement Schedule. Which Open ERP does!

.. i18n: .. tip:: Product trading
.. i18n: 
.. i18n:     Also called the Production Plan, this tool is also very useful for traded products which aren't
.. i18n:     manufactured.
.. i18n:     You can then use it for stock management with purchased and manufactured products.

.. tip:: Product trading

    Also called the Production Plan, this tool is also very useful for traded products which aren't
    manufactured.
    You can then use it for stock management with purchased and manufactured products.

.. i18n: .. index::
.. i18n:    single: module; stock_planning

.. index::
   single: module; stock_planning

.. i18n: To be able to use the production plan, you must install the :mod:`stock_planning` module.
.. i18n: This can be found amongst Open ERP's ``addons-extra`` rather in the main set of ``addons``.
.. i18n: (Beware! One reason it is not in the core of Open ERP at the time of writing
.. i18n: could be because some screens have no navigation 
.. i18n: controls, so you can't always easily get back to the main Open ERP system).

To be able to use the production plan, you must install the :mod:`stock_planning` module.
This can be found amongst Open ERP's ``addons-extra`` rather in the main set of ``addons``.
(Beware! One reason it is not in the core of Open ERP at the time of writing
could be because some screens have no navigation 
controls, so you can't always easily get back to the main Open ERP system).

.. i18n: .. index:: forecasts

.. index:: forecasts

.. i18n: Sales Forecasts
.. i18n: ---------------

Sales Forecasts
---------------

.. i18n: The first thing to do to work with a production plan is to define the periods for stock management.
.. i18n: Some companies plan daily, others weekly or monthly.

The first thing to do to work with a production plan is to define the periods for stock management.
Some companies plan daily, others weekly or monthly.

.. i18n: .. tip:: Stock Management interval
.. i18n: 
.. i18n:    The interval chosen for managing stock in the production plan will depend on the length of your
.. i18n:    production cycle. You generally work daily, weekly or monthly.
.. i18n: 
.. i18n:    If your products take several days to assemble it's preferable to have a weekly plan. If your
.. i18n:    manufacturing cycles are several months you can work with a monthly plan.

.. tip:: Stock Management interval

   The interval chosen for managing stock in the production plan will depend on the length of your
   production cycle. You generally work daily, weekly or monthly.

   If your products take several days to assemble it's preferable to have a weekly plan. If your
   manufacturing cycles are several months you can work with a monthly plan.

.. i18n: To do this use the menu :menuselection:`Sales Management --> Configuration --> Create Sales
.. i18n: Periods`. A window appears enabling you to automatically define the next periods that will be
.. i18n: provided for stock management.

To do this use the menu :menuselection:`Sales Management --> Configuration --> Create Sales
Periods`. A window appears enabling you to automatically define the next periods that will be
provided for stock management.

.. i18n: .. figure:: images/sale_period.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Defining periods for stock management*

.. figure:: images/sale_period.png
   :scale: 75
   :align: center

   *Defining periods for stock management*

.. i18n: Salespeople can then enter their sales forecasts by product and by period using the menu
.. i18n: :menuselection:`Sales Management --> Sales Forecasts --> My Sales Forecasts`. The forecasts can be
.. i18n: made by quantity or by value. For a forecast by amount Open ERP automatically calculates for you the
.. i18n: quantity equivalent to the estimated amount. This can be modified manually as needed before
.. i18n: completion.

Salespeople can then enter their sales forecasts by product and by period using the menu
:menuselection:`Sales Management --> Sales Forecasts --> My Sales Forecasts`. The forecasts can be
made by quantity or by value. For a forecast by amount Open ERP automatically calculates for you the
quantity equivalent to the estimated amount. This can be modified manually as needed before
completion.

.. i18n: .. figure:: images/stock_sale_forecast.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Sales Forecast to help create a master production plan*

.. figure:: images/stock_sale_forecast.png
   :scale: 75
   :align: center

   *Sales Forecast to help create a master production plan*

.. i18n: .. index::
.. i18n:    single: plan; production

.. index::
   single: plan; production

.. i18n: Production Plan
.. i18n: ---------------

Production Plan
---------------

.. i18n: The manager responsible for logistics then plans receipts (manufacturing or purchases) and outgoings
.. i18n: (consumption or customer deliveries) by period. To do this use the menu :menuselection:`Stock
.. i18n: Management --> Planning --> Master Procurement Schedule`.

The manager responsible for logistics then plans receipts (manufacturing or purchases) and outgoings
(consumption or customer deliveries) by period. To do this use the menu :menuselection:`Stock
Management --> Planning --> Master Procurement Schedule`.

.. i18n: For each period and product Open ERP gives you the following information:

For each period and product Open ERP gives you the following information:

.. i18n: * stock estimated at the end of the period, calculated as stock in the following period less total
.. i18n:   estimated outgoings plus total estimated inputs,
.. i18n: 
.. i18n: * closed entries, coming from production or confirmed purchases,
.. i18n: 
.. i18n: * forecast inputs for the period, calculated using the incoming entries less the closing amounts,
.. i18n: 
.. i18n: * planned inputs entered manually by the logistics manager,
.. i18n: 
.. i18n: * closed outgoings which are the consumption of manufacturing waiting and deliveries to be made to
.. i18n:   customers,
.. i18n: 
.. i18n: * forecast outgoings, calculated from the planned outgoings, less the closing amounts,
.. i18n: 
.. i18n: * planned outgoings, manually entered by the logistics manager,
.. i18n: 
.. i18n: * sales forecasts, which represent the sum of forecasts made by the salespeople.

* stock estimated at the end of the period, calculated as stock in the following period less total
  estimated outgoings plus total estimated inputs,

* closed entries, coming from production or confirmed purchases,

* forecast inputs for the period, calculated using the incoming entries less the closing amounts,

* planned inputs entered manually by the logistics manager,

* closed outgoings which are the consumption of manufacturing waiting and deliveries to be made to
  customers,

* forecast outgoings, calculated from the planned outgoings, less the closing amounts,

* planned outgoings, manually entered by the logistics manager,

* sales forecasts, which represent the sum of forecasts made by the salespeople.

.. i18n: .. figure:: images/stock_forecast.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *The master production schedule (MPS)*

.. figure:: images/stock_forecast.png
   :scale: 75
   :align: center

   *The master production schedule (MPS)*

.. i18n: The production plan then enables the logistics manager to play with the forecast income and
.. i18n: outgoings and test the impact on the future stock for the product under consideration. It enables
.. i18n: you for example to check that the stock doesn't fall below a certain level for the product under
.. i18n: consideration.

The production plan then enables the logistics manager to play with the forecast income and
outgoings and test the impact on the future stock for the product under consideration. It enables
you for example to check that the stock doesn't fall below a certain level for the product under
consideration.

.. i18n: You can also open the production plan for past periods. In this case Open ERP shows you the real
.. i18n: stock moves, by period for forecast reports.

You can also open the production plan for past periods. In this case Open ERP shows you the real
stock moves, by period for forecast reports.

.. i18n: If you don't have automated procurement rules for a product you can start procurement at any time
.. i18n: based on the estimates of the production plan. 
.. i18n: To do this press the button :guilabel:`Procure Incoming Left` (i.e. remaining) on 
.. i18n: the :guilabel:`Master Procurement Schedule`. 
.. i18n: Open ERP plans procurement for an amount equal to the entries forecast.

If you don't have automated procurement rules for a product you can start procurement at any time
based on the estimates of the production plan. 
To do this press the button :guilabel:`Procure Incoming Left` (i.e. remaining) on 
the :guilabel:`Master Procurement Schedule`. 
Open ERP plans procurement for an amount equal to the entries forecast.

.. i18n: .. Copyright © Open Object Press. All rights reserved.

.. Copyright © Open Object Press. All rights reserved.

.. i18n: .. You may take electronic copy of this publication and distribute it if you don't
.. i18n: .. change the content. You can also print a copy to be read by yourself only.

.. You may take electronic copy of this publication and distribute it if you don't
.. change the content. You can also print a copy to be read by yourself only.

.. i18n: .. We have contracts with different publishers in different countries to sell and
.. i18n: .. distribute paper or electronic based versions of this book (translated or not)
.. i18n: .. in bookstores. This helps to distribute and promote the Open ERP product. It
.. i18n: .. also helps us to create incentives to pay contributors and authors using author
.. i18n: .. rights of these sales.

.. We have contracts with different publishers in different countries to sell and
.. distribute paper or electronic based versions of this book (translated or not)
.. in bookstores. This helps to distribute and promote the Open ERP product. It
.. also helps us to create incentives to pay contributors and authors using author
.. rights of these sales.

.. i18n: .. Due to this, grants to translate, modify or sell this book are strictly
.. i18n: .. forbidden, unless Tiny SPRL (representing Open Object Press) gives you a
.. i18n: .. written authorisation for this.

.. Due to this, grants to translate, modify or sell this book are strictly
.. forbidden, unless Tiny SPRL (representing Open Object Press) gives you a
.. written authorisation for this.

.. i18n: .. Many of the designations used by manufacturers and suppliers to distinguish their
.. i18n: .. products are claimed as trademarks. Where those designations appear in this book,
.. i18n: .. and Open Object Press was aware of a trademark claim, the designations have been
.. i18n: .. printed in initial capitals.

.. Many of the designations used by manufacturers and suppliers to distinguish their
.. products are claimed as trademarks. Where those designations appear in this book,
.. and Open Object Press was aware of a trademark claim, the designations have been
.. printed in initial capitals.

.. i18n: .. While every precaution has been taken in the preparation of this book, the publisher
.. i18n: .. and the authors assume no responsibility for errors or omissions, or for damages
.. i18n: .. resulting from the use of the information contained herein.

.. While every precaution has been taken in the preparation of this book, the publisher
.. and the authors assume no responsibility for errors or omissions, or for damages
.. resulting from the use of the information contained herein.

.. i18n: .. Published by Open Object Press, Grand Rosière, Belgium

.. Published by Open Object Press, Grand Rosière, Belgium
