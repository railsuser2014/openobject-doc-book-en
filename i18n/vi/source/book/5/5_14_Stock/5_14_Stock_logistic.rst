
.. i18n: Logistics Configuration
.. i18n: =======================

Logistics Configuration
=======================

.. i18n: In this section you'll see how to configure stock management to match your company's needs. Open ERP
.. i18n: can handle many different situations by configuring it to behave as required.

In this section you'll see how to configure stock management to match your company's needs. Open ERP
can handle many different situations by configuring it to behave as required.

.. i18n: .. index:: 
.. i18n:    single: stock; location

.. index:: 
   single: stock; location

.. i18n: Stock locations
.. i18n: ---------------

Stock locations
---------------

.. i18n: You've seen in the preceding sections that the whole of stock management is built on a concept of
.. i18n: stock locations. Locations are structured hierarchically to account for the subdivision of a
.. i18n: warehouse into sections, aisles, and/or cupboards. The hierarchical view also enables you to
.. i18n: structure virtual locations such as production counterparts. That gives you a finer level of
.. i18n: analysis.

You've seen in the preceding sections that the whole of stock management is built on a concept of
stock locations. Locations are structured hierarchically to account for the subdivision of a
warehouse into sections, aisles, and/or cupboards. The hierarchical view also enables you to
structure virtual locations such as production counterparts. That gives you a finer level of
analysis.

.. i18n: Use the menu :menuselection:`Stock Management --> Configuration --> Locations` then click
.. i18n: :guilabel:`New` to define new locations.

Use the menu :menuselection:`Stock Management --> Configuration --> Locations` then click
:guilabel:`New` to define new locations.

.. i18n: .. figure:: images/stock_location_form.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Definition of a stock location*

.. figure:: images/stock_location_form.png
   :scale: 75
   :align: center

   *Definition of a stock location*

.. i18n: You should then give a name to your stock location. Now look at location types and localization.

You should then give a name to your stock location. Now look at location types and localization.

.. i18n: .. index:: 
.. i18n:    single: stock; location type

.. index:: 
   single: stock; location type

.. i18n: Location types
.. i18n: --------------

Location types
--------------

.. i18n: The location must have one of the following types:

The location must have one of the following types:

.. i18n: * View: shows that the location is only an organizational node for the hierarchical structure, and
.. i18n:   can't be involved in stock moves itself. The view type is not usually made into a leaf node in a
.. i18n:   structure – it usually has children.
.. i18n: 
.. i18n: * Customer: destination for products sent to customers,
.. i18n: 
.. i18n: * Supplier: source of products received from suppliers,
.. i18n: 
.. i18n: * Internal: locations for your own stock,
.. i18n: 
.. i18n: * Inventory: the counterpart for inventory operations used to correct stock levels,
.. i18n: 
.. i18n: * Production: the counterpart for production operations; receipt of raw material and sending
.. i18n:   finished products,
.. i18n: 
.. i18n: * Procurement: the counterpart for procurement operations when you don't yet know the source
.. i18n:   (supplier or production). Products in this location should be zero after the scheduler run
.. i18n:   completes.

* View: shows that the location is only an organizational node for the hierarchical structure, and
  can't be involved in stock moves itself. The view type is not usually made into a leaf node in a
  structure – it usually has children.

* Customer: destination for products sent to customers,

* Supplier: source of products received from suppliers,

* Internal: locations for your own stock,

* Inventory: the counterpart for inventory operations used to correct stock levels,

* Production: the counterpart for production operations; receipt of raw material and sending
  finished products,

* Procurement: the counterpart for procurement operations when you don't yet know the source
  (supplier or production). Products in this location should be zero after the scheduler run
  completes.

.. i18n: You can have several locations of the same type. In that case your product, supplier and warehouse
.. i18n: configurations determine the location that's to be used for any given operation.

You can have several locations of the same type. In that case your product, supplier and warehouse
configurations determine the location that's to be used for any given operation.

.. i18n: The counterparts for procurement, inventory and production operations are given by the locations
.. i18n: shown on the product form. The counterparts of reception and delivery operations are given by the
.. i18n: locations shown on the partner form. The choice of stock location is given by the configuration of
.. i18n: the warehouse, linked to a Shop.

The counterparts for procurement, inventory and production operations are given by the locations
shown on the product form. The counterparts of reception and delivery operations are given by the
locations shown on the partner form. The choice of stock location is given by the configuration of
the warehouse, linked to a Shop.

.. i18n: .. figure:: images/stock_product_location_form.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Definition of stock locations on the product form*

.. figure:: images/stock_product_location_form.png
   :scale: 75
   :align: center

   *Definition of stock locations on the product form*

.. i18n: .. figure:: images/stock_partner_location_form.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Definition of stock locations on the partner form*

.. figure:: images/stock_partner_location_form.png
   :scale: 75
   :align: center

   *Definition of stock locations on the partner form*

.. i18n: .. index:: 
.. i18n:    single: stock; localization

.. index:: 
   single: stock; localization

.. i18n: Localization
.. i18n: ------------

Localization
------------

.. i18n: Each location can be given an address. That enables you to create a location for a customer or a
.. i18n: supplier, for example. You can then give it the address of that customer or supplier. You should
.. i18n: indicate to Open ERP on the partner form that it should use this location rather than the default
.. i18n: location given to partner deliveries.

Each location can be given an address. That enables you to create a location for a customer or a
supplier, for example. You can then give it the address of that customer or supplier. You should
indicate to Open ERP on the partner form that it should use this location rather than the default
location given to partner deliveries.

.. i18n: .. tip:: Subcontracting production
.. i18n: 
.. i18n:     You'll see in the chapter, :ref:`ch-mnf`, that it is possible to assign a location to a
.. i18n:     manufacturing workcenter.
.. i18n:     If this location is at a supplier's you must give it an address so that Open ERP can prepare a
.. i18n:     delivery order
.. i18n:     for the supplier and a receive operation for the manufactured goods.
.. i18n: 
.. i18n:     Creating a location specifically for a partner is also a simple solution for handled consigned
.. i18n:     stocks in Open ERP.

.. tip:: Subcontracting production

    You'll see in the chapter, :ref:`ch-mnf`, that it is possible to assign a location to a
    manufacturing workcenter.
    If this location is at a supplier's you must give it an address so that Open ERP can prepare a
    delivery order
    for the supplier and a receive operation for the manufactured goods.

    Creating a location specifically for a partner is also a simple solution for handled consigned
    stocks in Open ERP.

.. i18n: .. note:: Consigned Stock
.. i18n: 
.. i18n:     Consigned stock is stock that is owned by you (valued in your accounts) but is physically
.. i18n:     stocked by your supplier.
.. i18n:     Or, conversely, it could be stock owned by your customer (not valued by you) but stocked in your
.. i18n:     company.

.. note:: Consigned Stock

    Consigned stock is stock that is owned by you (valued in your accounts) but is physically
    stocked by your supplier.
    Or, conversely, it could be stock owned by your customer (not valued by you) but stocked in your
    company.

.. i18n: To enable you to consolidate easily at a higher level, the location definition is hierarchical. This
.. i18n: structure is given by the field :guilabel:`Parent location`. That also enables you to manage complex
.. i18n: cases of product localization. For example, you could imagine the following scenario.

To enable you to consolidate easily at a higher level, the location definition is hierarchical. This
structure is given by the field :guilabel:`Parent location`. That also enables you to manage complex
cases of product localization. For example, you could imagine the following scenario.

.. i18n: Example Structure for two warehouses
.. i18n: ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Example Structure for two warehouses
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. i18n: A company has a warehouse in Paris and in Bordeaux. For some orders you must deliver the products
.. i18n: from Paris, and for others from Bordeaux. But you should also specify a fictitious warehouse that
.. i18n: Open ERP uses to calculate if it should deliver products from Paris or from Bordeaux.

A company has a warehouse in Paris and in Bordeaux. For some orders you must deliver the products
from Paris, and for others from Bordeaux. But you should also specify a fictitious warehouse that
Open ERP uses to calculate if it should deliver products from Paris or from Bordeaux.

.. i18n: To do this in Open ERP, you'd create a third warehouse 'France' which consolidates the warehouses in
.. i18n: Paris and Bordeaux. You create the following physical locations:

To do this in Open ERP, you'd create a third warehouse 'France' which consolidates the warehouses in
Paris and Bordeaux. You create the following physical locations:

.. i18n: * Company
.. i18n: 
.. i18n:   * Output
.. i18n: 
.. i18n:     * Warehouses France
.. i18n: 
.. i18n:       * Warehouse Paris
.. i18n: 
.. i18n:       * Warehouse Bordeaux

* Company

  * Output

    * Warehouses France

      * Warehouse Paris

      * Warehouse Bordeaux

.. i18n: Open ERP will then deliver the goods from the warehouse that has the ordered product in stock. When
.. i18n: products are available in several warehouses, Open ERP will select the nearest warehouse. To
.. i18n: formalize the notion of distance between warehouses you should use the geographic co-ordinates (X,
.. i18n: Y, Z) of the different stores to enable Open ERP to search for the nearest goods.

Open ERP will then deliver the goods from the warehouse that has the ordered product in stock. When
products are available in several warehouses, Open ERP will select the nearest warehouse. To
formalize the notion of distance between warehouses you should use the geographic co-ordinates (X,
Y, Z) of the different stores to enable Open ERP to search for the nearest goods.

.. i18n: The same co-ordinates could also be used to structure the shelves, aisles and interior rooms in a
.. i18n: warehouse.

The same co-ordinates could also be used to structure the shelves, aisles and interior rooms in a
warehouse.

.. i18n: .. index:: 
.. i18n:    single: stock; real time valutation

.. index:: 
   single: stock; real time valutation

.. i18n: Accounting valuation in real time
.. i18n: ---------------------------------

Accounting valuation in real time
---------------------------------

.. i18n: .. index::
.. i18n:    single: accountant

.. index::
   single: accountant

.. i18n: If you have experience of managing with traditional software you'll know the problem of getting
.. i18n: useful indicators. If you ask your accountant for a stock valuation or the value added by production
.. i18n: he'll give you a figure. If you ask for the same figure from your stores manager you'll get an
.. i18n: entirely different amount. You have no idea who's right!

If you have experience of managing with traditional software you'll know the problem of getting
useful indicators. If you ask your accountant for a stock valuation or the value added by production
he'll give you a figure. If you ask for the same figure from your stores manager you'll get an
entirely different amount. You have no idea who's right!

.. i18n: In Open ERP the management of stock is completely integrated with the accounts, to give strong
.. i18n: coherence between the two systems. The double-entry structure of locations enables a very precise
.. i18n: correspondence between stocks and accounts.

In Open ERP the management of stock is completely integrated with the accounts, to give strong
coherence between the two systems. The double-entry structure of locations enables a very precise
correspondence between stocks and accounts.

.. i18n: Each stock movement also generates a corresponding accounting entry in an accounting journal to
.. i18n: ensure that the two systems can stay in permanent synchronization.

Each stock movement also generates a corresponding accounting entry in an accounting journal to
ensure that the two systems can stay in permanent synchronization.

.. i18n: To do that, set up a general account for each location that should be valued in your accounts. If a
.. i18n: product goes to one location or another and the accounts are different in the two locations, Open
.. i18n: ERP automatically generates the corresponding accounting entries in the accounts, in the stock
.. i18n: journal.

To do that, set up a general account for each location that should be valued in your accounts. If a
product goes to one location or another and the accounts are different in the two locations, Open
ERP automatically generates the corresponding accounting entries in the accounts, in the stock
journal.

.. i18n: If a stock move will go from a location without an account to a location where an account has been
.. i18n: assigned (for example goods receipt from a supplier order), Open ERP generates an accounting entry
.. i18n: using the properties defined in the product form for the counterpart. You can use different accounts
.. i18n: per location or link several location to the same account, depending on the level of analysis
.. i18n: needed.

If a stock move will go from a location without an account to a location where an account has been
assigned (for example goods receipt from a supplier order), Open ERP generates an accounting entry
using the properties defined in the product form for the counterpart. You can use different accounts
per location or link several location to the same account, depending on the level of analysis
needed.

.. i18n: You use this system for managing consigned stocks:

You use this system for managing consigned stocks:

.. i18n: * a supplier location that is valued in your own accounts or,
.. i18n: 
.. i18n: * a location in your own company that isn't valued in your accounts.

* a supplier location that is valued in your own accounts or,

* a location in your own company that isn't valued in your accounts.

.. i18n: .. index:: 
.. i18n:    single: chained location
.. i18n:    single: location; chained

.. index:: 
   single: chained location
   single: location; chained

.. i18n: Linked locations
.. i18n: ----------------

Linked locations
----------------

.. i18n: Locations in Open ERP can be linked between each other to define paths followed by products. So you
.. i18n: can then define rules such as: all products that enter the warehouse must automatically be sent to
.. i18n: quality control. The warehouse and quality control are represented by two different locations.

Locations in Open ERP can be linked between each other to define paths followed by products. So you
can then define rules such as: all products that enter the warehouse must automatically be sent to
quality control. The warehouse and quality control are represented by two different locations.

.. i18n: Then when a product arrives in a location, Open ERP can automatically suggest that you send the
.. i18n: product to another linked location. Three link modes are available:

Then when a product arrives in a location, Open ERP can automatically suggest that you send the
product to another linked location. Three link modes are available:

.. i18n: * Manual,
.. i18n: 
.. i18n: * Automatic,
.. i18n: 
.. i18n: * Automatic without steps.

* Manual,

* Automatic,

* Automatic without steps.

.. i18n: The manual mode will create an internal move order to the linked location once products arrive in
.. i18n: the source locations. This order will wait for a confirmation of the move by a user. This enables
.. i18n: you to have a list of moves to do, proposed by the system and confirmed by the storesperson.

The manual mode will create an internal move order to the linked location once products arrive in
the source locations. This order will wait for a confirmation of the move by a user. This enables
you to have a list of moves to do, proposed by the system and confirmed by the storesperson.

.. i18n: .. index::
.. i18n:    single: module; stock_location

.. index::
   single: module; stock_location

.. i18n: .. tip:: Product Logistics
.. i18n: 
.. i18n:     The module :mod:`stock_location` lets you generate paths to follow, not just at the level of
.. i18n:     locations but also at the level of products.
.. i18n:     It then enables you to manage default locations for a given product or to refer to the products
.. i18n:     as a function of
.. i18n:     operations such as quality control, supplier receipt, and after-sales service.
.. i18n: 
.. i18n:     A more detailed explanation of this module, with examples, is given at the end of this chapter.

.. tip:: Product Logistics

    The module :mod:`stock_location` lets you generate paths to follow, not just at the level of
    locations but also at the level of products.
    It then enables you to manage default locations for a given product or to refer to the products
    as a function of
    operations such as quality control, supplier receipt, and after-sales service.

    A more detailed explanation of this module, with examples, is given at the end of this chapter.

.. i18n: The automatic mode will do the same but won't wait for a confirmation from the user. Products will
.. i18n: automatically be sent to the linked location without any intervening manual operation to do. This
.. i18n: corresponds to the case where, for simplicity, you delete a step in the process so the end user can
.. i18n: set off the process automatically.

The automatic mode will do the same but won't wait for a confirmation from the user. Products will
automatically be sent to the linked location without any intervening manual operation to do. This
corresponds to the case where, for simplicity, you delete a step in the process so the end user can
set off the process automatically.

.. i18n: The ``automatic without steps`` mode won't include the additional stock move but will change the
.. i18n: destination move transparently to assign the linked the location. You could then assign a
.. i18n: destination location to which you send all the products that arrive in your warehouse. The
.. i18n: storesperson will modify the goods receipt note.

The ``automatic without steps`` mode won't include the additional stock move but will change the
destination move transparently to assign the linked the location. You could then assign a
destination location to which you send all the products that arrive in your warehouse. The
storesperson will modify the goods receipt note.

.. i18n: If there is a linkage to do, the field :guilabel:`Type of linked location` lets the destination
.. i18n: location be determined. If the field is set to 'customer', the location is given by the properties
.. i18n: of the partner form. If the field is set to ``fixed`` , the destination location is given by the field
.. i18n: :guilabel:`Location if link is fixed`.

If there is a linkage to do, the field :guilabel:`Type of linked location` lets the destination
location be determined. If the field is set to 'customer', the location is given by the properties
of the partner form. If the field is set to ``fixed`` , the destination location is given by the field
:guilabel:`Location if link is fixed`.

.. i18n: Some operations take a certain time between order and execution. To account for this lead time, you
.. i18n: can set a value in days in the field :guilabel:`Link lead time`. Then the extra move (automatic or
.. i18n: not) will be carried out several days after the original move. If you use the mode ``automatic
.. i18n: without steps``, the lead time is inserted directly into the initial order. In this way you can add
.. i18n: security lead times at certain control points in the warehouse.

Some operations take a certain time between order and execution. To account for this lead time, you
can set a value in days in the field :guilabel:`Link lead time`. Then the extra move (automatic or
not) will be carried out several days after the original move. If you use the mode ``automatic
without steps``, the lead time is inserted directly into the initial order. In this way you can add
security lead times at certain control points in the warehouse.

.. i18n: Case of structuring locations
.. i18n: -----------------------------

Case of structuring locations
-----------------------------

.. i18n: You'll see in the next part that linking locations lets you manage a whole series of complex cases
.. i18n: in managing production efficiently:

You'll see in the next part that linking locations lets you manage a whole series of complex cases
in managing production efficiently:

.. i18n: * handling multiple operations for a customer order,
.. i18n: 
.. i18n: * tracking import and export by sea transport,
.. i18n: 
.. i18n: * managing a production chain in detail,
.. i18n: 
.. i18n: * managing rented products,
.. i18n: 
.. i18n: * managing consigned products.

* handling multiple operations for a customer order,

* tracking import and export by sea transport,

* managing a production chain in detail,

* managing rented products,

* managing consigned products.

.. i18n: To show these concepts, five cases of structuring and configuring these locations are given below.
.. i18n: Many other configurations are possible depending on needs.

To show these concepts, five cases of structuring and configuring these locations are given below.
Many other configurations are possible depending on needs.

.. i18n: Handling customer orders
.. i18n: ------------------------

Handling customer orders
------------------------

.. i18n: Customer orders are usually handled in one of two ways:

Customer orders are usually handled in one of two ways:

.. i18n: * item note (or preparation order), confirmed when the item is ready to send,
.. i18n: 
.. i18n: * delivery order (or freight note), confirmed when the transporter has delivered the item to a
.. i18n:   customer.

* item note (or preparation order), confirmed when the item is ready to send,

* delivery order (or freight note), confirmed when the transporter has delivered the item to a
  customer.

.. i18n: You use the following stock move in Open ERP to simulate these operations:

You use the following stock move in Open ERP to simulate these operations:

.. i18n: * Packing Note: Stock > Output,
.. i18n: 
.. i18n: * Delivery Order: Output > Customer.

* Packing Note: Stock > Output,

* Delivery Order: Output > Customer.

.. i18n: The first operation is automatically generated by the customer order. The second is then generated
.. i18n: by the stock management by showing that the ``Output`` location is linked to the ``Customer`` location.
.. i18n: That then gives the two operations waiting. If the ``Output`` location isn't situated beneath the
.. i18n: stock location you then have to move the item from stock to the place that the item is prepared.

The first operation is automatically generated by the customer order. The second is then generated
by the stock management by showing that the ``Output`` location is linked to the ``Customer`` location.
That then gives the two operations waiting. If the ``Output`` location isn't situated beneath the
stock location you then have to move the item from stock to the place that the item is prepared.

.. i18n: Some companies don't want to work in two steps, because it just seems like extra work to have to
.. i18n: confirm a delivery note in the system. You can then set the link mode to 'Automatic' to make Open
.. i18n: ERP automatically confirm the second step. It's then assumed the all the items have automatically
.. i18n: been delivered to the customer.

Some companies don't want to work in two steps, because it just seems like extra work to have to
confirm a delivery note in the system. You can then set the link mode to 'Automatic' to make Open
ERP automatically confirm the second step. It's then assumed the all the items have automatically
been delivered to the customer.

.. i18n: .. index:: 
.. i18n:    single: linked production

.. index:: 
   single: linked production

.. i18n: Linked Production
.. i18n: -----------------

Linked Production
-----------------

.. i18n: The :mod:`stock_location` module enables you to manage the linkages by product in addition to doing
.. i18n: that by location. You can then create a location structure that represents your production chain by
.. i18n: product.

The :mod:`stock_location` module enables you to manage the linkages by product in addition to doing
that by location. You can then create a location structure that represents your production chain by
product.

.. i18n: The location structure looks like this:

The location structure looks like this:

.. i18n: * Stock
.. i18n: 
.. i18n:   * Level 1
.. i18n: 
.. i18n:   * Level 2
.. i18n: 
.. i18n:     * Link 1
.. i18n: 
.. i18n:       * Operation 1
.. i18n: 
.. i18n:       * Operation 2
.. i18n: 
.. i18n:       * Operation 3
.. i18n: 
.. i18n:       * Operation 4

* Stock

  * Level 1

  * Level 2

    * Link 1

      * Operation 1

      * Operation 2

      * Operation 3

      * Operation 4

.. i18n: You can then set the locations a product or a routing must go through on the relevant form. All
.. i18n: products that enter the production chain will automatically follow the predetermined path.

You can then set the locations a product or a routing must go through on the relevant form. All
products that enter the production chain will automatically follow the predetermined path.

.. i18n: .. figure:: images/stock_product_path.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Logistics for a given product*

.. figure:: images/stock_product_path.png
   :scale: 75
   :align: center

   *Logistics for a given product*

.. i18n: To improve your logistics, you'll see further on in this chapter how you can put minimum stock rules
.. i18n: onto different locations to guarantee security stocks for assembly operators. Reports on the state
.. i18n: of stocks in different locations will rapidly show you the bottlenecks in your production chain.

To improve your logistics, you'll see further on in this chapter how you can put minimum stock rules
onto different locations to guarantee security stocks for assembly operators. Reports on the state
of stocks in different locations will rapidly show you the bottlenecks in your production chain.

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
