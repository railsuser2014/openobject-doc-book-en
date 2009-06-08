
.. i18n: Import / Export
.. i18n: ===============

Import / Export
===============

.. i18n: .. index::
.. i18n:    single: export; stock management
.. i18n:    single: import; stock management

.. index::
   single: export; stock management
   single: import; stock management

.. i18n: Managing import / export with foreign companies can sometimes be very complex. Between a departure
.. i18n: port and destination company, products can get stopped for several weeks at sea or somewhere in the
.. i18n: numerous transportation stages and customs. To manage such deliveries efficiently it's important to:

Managing import / export with foreign companies can sometimes be very complex. Between a departure
port and destination company, products can get stopped for several weeks at sea or somewhere in the
numerous transportation stages and customs. To manage such deliveries efficiently it's important to:

.. i18n: * know where your products are,
.. i18n: 
.. i18n: * know when they're likely to arrive at their destination,
.. i18n: 
.. i18n: * know your value in transit,
.. i18n: 
.. i18n: * follow the development of the different steps.

* know where your products are,

* know when they're likely to arrive at their destination,

* know your value in transit,

* follow the development of the different steps.

.. i18n: Linked locations in Open ERP enable this all to be managed rather elegantly. You can use a structure
.. i18n: like this:

Linked locations in Open ERP enable this all to be managed rather elegantly. You can use a structure
like this:

.. i18n: * Suppliers
.. i18n: 
.. i18n:   * European Suppliers
.. i18n: 
.. i18n:   * Chinese Suppliers
.. i18n: 
.. i18n: * In transit
.. i18n: 
.. i18n:   * Shanghai Port
.. i18n: 
.. i18n:   * Pacific Ocean
.. i18n: 
.. i18n:   * San Francisco Port
.. i18n: 
.. i18n:   * San Francisco Customs

* Suppliers

  * European Suppliers

  * Chinese Suppliers

* In transit

  * Shanghai Port

  * Pacific Ocean

  * San Francisco Port

  * San Francisco Customs

.. i18n: Stock
.. i18n: -----

Stock
-----

.. i18n: The transit location are linked between themselves with a manual confirmation step. The internal
.. i18n: stock move is validated at each port and customs arrival. Open ERP prepares all the linked moves
.. i18n: automatically.

The transit location are linked between themselves with a manual confirmation step. The internal
stock move is validated at each port and customs arrival. Open ERP prepares all the linked moves
automatically.

.. i18n: .. index::
.. i18n:    single: module; report_instrastat

.. index::
   single: module; report_instrastat

.. i18n: .. note:: Intrastat
.. i18n: 
.. i18n:     Companies that do import / export should install the module :mod:`report_intrastat`.
.. i18n:     This enables them to prepare the reports needed to declare product exports.

.. note:: Intrastat

    Companies that do import / export should install the module :mod:`report_intrastat`.
    This enables them to prepare the reports needed to declare product exports.

.. i18n: You can use the lead times between different locations to account for real delays.
.. i18n: Your lead times and stock forecasts are calculated by Open ERP to estimate the arrival of
.. i18n: incoming products so that you can respond to a customer's needs as precisely as possible.

You can use the lead times between different locations to account for real delays.
Your lead times and stock forecasts are calculated by Open ERP to estimate the arrival of
incoming products so that you can respond to a customer's needs as precisely as possible.

.. i18n: You can also value the products in transit in your account depending on the chosen stock location
.. i18n: configuration.

You can also value the products in transit in your account depending on the chosen stock location
configuration.

.. i18n: .. index:: rent

.. index:: rent

.. i18n: Rental locations
.. i18n: ----------------

Rental locations
----------------

.. i18n: .. index::
.. i18n:    single: module; stock_location

.. index::
   single: module; stock_location

.. i18n: You can manage rental locations in Open ERP very simply using the same system of linked locations.
.. i18n: Using the module :mod:`stock_location` you can set a return date for rental items sent to customer
.. i18n: location after a certain rental period.

You can manage rental locations in Open ERP very simply using the same system of linked locations.
Using the module :mod:`stock_location` you can set a return date for rental items sent to customer
location after a certain rental period.

.. i18n: Then the set of real and virtual stocks is maintained daily in real time. The different operations
.. i18n: such as delivery and receipt after a few days are automatically suggested by Open ERP which
.. i18n: simplifies the work of data entry.

Then the set of real and virtual stocks is maintained daily in real time. The different operations
such as delivery and receipt after a few days are automatically suggested by Open ERP which
simplifies the work of data entry.

.. i18n: You then have the product list found in the customer locations and your own stock in your stock
.. i18n: location. The list of goods receipts waiting is automatically generated by Open ERP using the
.. i18n: location links.

You then have the product list found in the customer locations and your own stock in your stock
location. The list of goods receipts waiting is automatically generated by Open ERP using the
location links.

.. i18n: The same principle is used for internal stock to generate the quality control for certain products.

The same principle is used for internal stock to generate the quality control for certain products.

.. i18n: Consigned Products
.. i18n: ------------------

Consigned Products
------------------

.. i18n: The principle of linked locations is used to manage consigned products. You can specify that
.. i18n: certain products should be returned to you a certain number of days after they have been
.. i18n: delivered to customers.

The principle of linked locations is used to manage consigned products. You can specify that
certain products should be returned to you a certain number of days after they have been
delivered to customers.

.. i18n: When the products have been delivered Open ERP automatically creates goods receipts for the
.. i18n: consigned product. The specified date is obviously approximate but enables you to forecast returns.

When the products have been delivered Open ERP automatically creates goods receipts for the
consigned product. The specified date is obviously approximate but enables you to forecast returns.

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
