
.. i18n: .. index::
.. i18n:    single: Logistics
.. i18n:    single: Stock Management

.. index::
   single: Logistics
   single: Stock Management

.. i18n: .. _ch-stocks:
.. i18n: 
.. i18n: ******************************
.. i18n: Logistics and Stock Management
.. i18n: ******************************

.. _ch-stocks:

******************************
Logistics and Stock Management
******************************

.. i18n:  *Open ERP's stock management is at once very simple, flexible and complete.
.. i18n:  It's based on the concept of double entry that revolutionized accounting.
.. i18n:  The system can be described by Lavoisier's maxim “nothing lost, everything changed” or, better,
.. i18n:  “everything moved”. In Open ERP you don't talk of disappearance, consumption or loss of products:
.. i18n:  instead you speak only of stock moves from one place to another.*

 *Open ERP's stock management is at once very simple, flexible and complete.
 It's based on the concept of double entry that revolutionized accounting.
 The system can be described by Lavoisier's maxim “nothing lost, everything changed” or, better,
 “everything moved”. In Open ERP you don't talk of disappearance, consumption or loss of products:
 instead you speak only of stock moves from one place to another.*

.. i18n: Just as in accounting, the Open ERP system manages counterparts to each of its main operations such as
.. i18n: receipts from suppliers, deliveries to customers, profits and losses from inventory, and consumption
.. i18n: of raw materials. Stock movements are always made from one location to another. To satisfy the need
.. i18n: for a counterpart to each stock movement, the software supports different types of stock location:

Just as in accounting, the Open ERP system manages counterparts to each of its main operations such as
receipts from suppliers, deliveries to customers, profits and losses from inventory, and consumption
of raw materials. Stock movements are always made from one location to another. To satisfy the need
for a counterpart to each stock movement, the software supports different types of stock location:

.. i18n: * Physical stock locations,
.. i18n: 
.. i18n: * Partner locations,
.. i18n: 
.. i18n: * Virtual counterparts such as production and inventory.

* Physical stock locations,

* Partner locations,

* Virtual counterparts such as production and inventory.

.. i18n: Physical locations represent warehouses and their hierarchical structure. These are generally the
.. i18n: locations that are managed by traditional stock management systems.

Physical locations represent warehouses and their hierarchical structure. These are generally the
locations that are managed by traditional stock management systems.

.. i18n: Partner locations represent your customers' and suppliers' stocks. To reconcile them with your
.. i18n: accounts, these stores play the role of third-party accounts. Reception from a supplier can be shown
.. i18n: by the movement of goods from a partner location to a physical location in your own company. As you
.. i18n: see, supplier locations usually show negative stocks and customer locations usually show positive
.. i18n: stocks.

Partner locations represent your customers' and suppliers' stocks. To reconcile them with your
accounts, these stores play the role of third-party accounts. Reception from a supplier can be shown
by the movement of goods from a partner location to a physical location in your own company. As you
see, supplier locations usually show negative stocks and customer locations usually show positive
stocks.

.. i18n: Virtual counterparts for production are used in manufacturing operations. Manufacturing is
.. i18n: characterized by the consumption of raw materials and the production of finished products. Virtual
.. i18n: locations are used for the counterparts of these two operations.

Virtual counterparts for production are used in manufacturing operations. Manufacturing is
characterized by the consumption of raw materials and the production of finished products. Virtual
locations are used for the counterparts of these two operations.

.. i18n: Inventory locations are counterparts of the stock operations that represent your company's profits
.. i18n: and losses in terms of your stocks.

Inventory locations are counterparts of the stock operations that represent your company's profits
and losses in terms of your stocks.

.. i18n: The figure :ref:`fig-stloctree` shows the initial configuration of the stores locations when the software is
.. i18n: installed.

The figure :ref:`fig-stloctree` shows the initial configuration of the stores locations when the software is
installed.

.. i18n: .. _fig-stloctree:
.. i18n: 
.. i18n: .. figure:: images/stock_location_tree.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Stores location structure when Open ERP has just been installed*

.. _fig-stloctree:

.. figure:: images/stock_location_tree.png
   :scale: 75
   :align: center

   *Stores location structure when Open ERP has just been installed*

.. i18n: .. note::  Hierarchical stock locations
.. i18n: 
.. i18n:     In Open ERP locations are structured hierarchically.
.. i18n:     You can structure your locations as a tree, dependent on a parent-child relationship.
.. i18n:     This gives you more detailed levels of analysis of your stock operations and the organization of
.. i18n:     your warehouses.

.. note::  Hierarchical stock locations

    In Open ERP locations are structured hierarchically.
    You can structure your locations as a tree, dependent on a parent-child relationship.
    This gives you more detailed levels of analysis of your stock operations and the organization of
    your warehouses.

.. i18n: .. tip:: Locations and Warehouses
.. i18n: 
.. i18n:     In Open ERP **warehouses** represent your places of physical stock.
.. i18n:     A warehouse can be structured into several locations at multiple levels.
.. i18n:     Locations are used to manage all types of storage place, such as at the customer and production
.. i18n:     counterparts.

.. tip:: Locations and Warehouses

    In Open ERP **warehouses** represent your places of physical stock.
    A warehouse can be structured into several locations at multiple levels.
    Locations are used to manage all types of storage place, such as at the customer and production
    counterparts.

.. i18n: For this chapter you should start with a fresh database that includes demo data,
.. i18n: with :mod:`stock` and its dependencies installed and no particular chart of accounts configured. 

For this chapter you should start with a fresh database that includes demo data,
with :mod:`stock` and its dependencies installed and no particular chart of accounts configured. 

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <div class="all-toctree">

.. raw:: html

    <div class="all-toctree">

.. i18n: .. toctree::
.. i18n: 
.. i18n:     5_14_Stock_illustration
.. i18n:     5_14_Stock_wf
.. i18n:     5_14_Stock_stocks
.. i18n:     5_14_Stock_logistic
.. i18n:     5_14_Stock_import
.. i18n:     5_14_Stock_warehouses
.. i18n:     5_14_Stock_production.rst
.. i18n:     5_14_Stock_lots.rst
.. i18n:     5_14_Stock_journals.rst
.. i18n:     5_14_Stock_advanced.rst

.. toctree::

    5_14_Stock_illustration
    5_14_Stock_wf
    5_14_Stock_stocks
    5_14_Stock_logistic
    5_14_Stock_import
    5_14_Stock_warehouses
    5_14_Stock_production.rst
    5_14_Stock_lots.rst
    5_14_Stock_journals.rst
    5_14_Stock_advanced.rst

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     </div>

.. raw:: html

    </div>

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
