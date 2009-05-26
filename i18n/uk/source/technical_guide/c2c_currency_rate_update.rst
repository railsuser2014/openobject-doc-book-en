
.. i18n: .. module:: c2c_currency_rate_update
.. i18n:     :synopsis: Currency Rate Update 
.. i18n:     :noindex:
.. i18n: .. 

.. module:: c2c_currency_rate_update
    :synopsis: Currency Rate Update 
    :noindex:
.. 

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. i18n: Currency Rate Update (*c2c_currency_rate_update*)
.. i18n: =================================================
.. i18n: :Module: c2c_currency_rate_update
.. i18n: :Name: Currency Rate Update
.. i18n: :Version: 0.5
.. i18n: :Author: Camptocamp SA
.. i18n: :Directory: c2c_currency_rate_update
.. i18n: :Web: http://camptocamp.com
.. i18n: :Official module: no
.. i18n: :Quality certified: no

Currency Rate Update (*c2c_currency_rate_update*)
=================================================
:Module: c2c_currency_rate_update
:Name: Currency Rate Update
:Version: 0.5
:Author: Camptocamp SA
:Directory: c2c_currency_rate_update
:Web: http://camptocamp.com
:Official module: no
:Quality certified: no

.. i18n: Description
.. i18n: -----------

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   
.. i18n:   Import exchange rates from three different sources on the internet :
.. i18n:   
.. i18n:   1. Admin.ch
.. i18n:      Updated daily, source in CHF. Source type is XML based.
.. i18n:   
.. i18n:   2. Federal Reserve Bank of New York
.. i18n:      Daily 12 noon buying rates in New York are certified by the
.. i18n:      New York Federal Reserve Bank for customs purposes.
.. i18n:      Source in USD.
.. i18n:      http://www.newyorkfed.org/markets/pilotfx.html
.. i18n:   
.. i18n:   3. European Central Bank
.. i18n:      The reference rates are based on the regular daily concertation procedure between
.. i18n:      central banks within and outside the European System of Central Banks,
.. i18n:      which normally takes place at 2.15 p.m. (14:15) ECB time. Source in EUR.
.. i18n:      http://www.ecb.europa.eu/stats/exchange/eurofxref/html/index.en.html
.. i18n:   
.. i18n:   4. Google Finance
.. i18n:      Updated daily from Citibank N.A., source in EUR. Information may be delayed.
.. i18n:      This is parsed from an HTML page, so it may be broken at anytime.
.. i18n:   
.. i18n:   5. Bank of Canada
.. i18n:      Updated daily at 12:30 am, source in CAD, nominal rate. Source type is CSV based.
.. i18n:   
.. i18n:   You can set time cycle for getting updates, 'first execute date' define when to start
.. i18n:   the import and you can add a comment that describe why you use that particular service.
.. i18n:   
.. i18n:   The module uses internal ir_cron feature from OpenERP, so the job is launched once
.. i18n:   the server starts if the 'first execute date' is before the current day.
.. i18n:   
.. i18n:   If in multi-company mode, the base currency will be the first company's currency
.. i18n:   found in database.
.. i18n:   

::

  
  Import exchange rates from three different sources on the internet :
  
  1. Admin.ch
     Updated daily, source in CHF. Source type is XML based.
  
  2. Federal Reserve Bank of New York
     Daily 12 noon buying rates in New York are certified by the
     New York Federal Reserve Bank for customs purposes.
     Source in USD.
     http://www.newyorkfed.org/markets/pilotfx.html
  
  3. European Central Bank
     The reference rates are based on the regular daily concertation procedure between
     central banks within and outside the European System of Central Banks,
     which normally takes place at 2.15 p.m. (14:15) ECB time. Source in EUR.
     http://www.ecb.europa.eu/stats/exchange/eurofxref/html/index.en.html
  
  4. Google Finance
     Updated daily from Citibank N.A., source in EUR. Information may be delayed.
     This is parsed from an HTML page, so it may be broken at anytime.
  
  5. Bank of Canada
     Updated daily at 12:30 am, source in CAD, nominal rate. Source type is CSV based.
  
  You can set time cycle for getting updates, 'first execute date' define when to start
  the import and you can add a comment that describe why you use that particular service.
  
  The module uses internal ir_cron feature from OpenERP, so the job is launched once
  the server starts if the 'first execute date' is before the current day.
  
  If in multi-company mode, the base currency will be the first company's currency
  found in database.
  

.. i18n: Dependencies
.. i18n: ------------

Dependencies
------------

.. i18n:  * :mod:`base`

 * :mod:`base`

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

.. i18n: None

None

.. i18n: Views
.. i18n: -----

Views
-----

.. i18n: None

None

.. i18n: Objects
.. i18n: -------

Objects
-------

.. i18n: None

None
