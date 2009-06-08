
.. i18n: Control of deliveries and invoicing
.. i18n: ===================================

Control of deliveries and invoicing
===================================

.. i18n: Configuration of orders
.. i18n: -----------------------

Configuration of orders
-----------------------

.. i18n: .. index:: 
.. i18n:    pair: control; delivery
.. i18n:    pair: control; invoicing

.. index:: 
   pair: control; delivery
   pair: control; invoicing

.. i18n: Depending on the configuration of the order, several different possible consequences can follow.
.. i18n: Three fields determine the future behaviour of an order:

Depending on the configuration of the order, several different possible consequences can follow.
Three fields determine the future behaviour of an order:

.. i18n: * :guilabel:`Packing Policy` : ``Partial Delivery`` or ``Complete Delivery``,
.. i18n: 
.. i18n: * :guilabel:`Shipping Policy` : ``Shipping & Manual Invoice``, ``Payment Before Delivery``,
.. i18n:   ``Invoice on Order After Delivery``, and ``Invoice from the Packing``,
.. i18n: 
.. i18n: * :guilabel:`Invoice on` : ``Ordered Quantities`` or ``Delivered Quantities``.

* :guilabel:`Packing Policy` : ``Partial Delivery`` or ``Complete Delivery``,

* :guilabel:`Shipping Policy` : ``Shipping & Manual Invoice``, ``Payment Before Delivery``,
  ``Invoice on Order After Delivery``, and ``Invoice from the Packing``,

* :guilabel:`Invoice on` : ``Ordered Quantities`` or ``Delivered Quantities``.

.. i18n:   .. tip::  Simplified view
.. i18n: 
.. i18n:      If you work in the ``Simplified View`` mode, only the :guilabel:`Shipping Policy` field is visible
.. i18n:      in the second tab on the order.
.. i18n:      To get to the ``Extended View`` mode, assign the group :guilabel:`Usability – Extended View` to the current
.. i18n:      user.

  .. tip::  Simplified view

     If you work in the ``Simplified View`` mode, only the :guilabel:`Shipping Policy` field is visible
     in the second tab on the order.
     To get to the ``Extended View`` mode, assign the group :guilabel:`Usability – Extended View` to the current
     user.

.. i18n: Packing mode
.. i18n: ------------

Packing mode
------------

.. i18n: The packing mode determines the way that the storesperson will do the packing. If the order is put
.. i18n: into :guilabel:`Partial Delivery` mode, the packing order will appear in the list of things for the
.. i18n: storesperson to do as soon as any of the products on the order is available. To get the list of
.. i18n: items to be done you can use the menu :menuselection:`Stock Management --> Outgoing Products -->
.. i18n: Available Packing`.

The packing mode determines the way that the storesperson will do the packing. If the order is put
into :guilabel:`Partial Delivery` mode, the packing order will appear in the list of things for the
storesperson to do as soon as any of the products on the order is available. To get the list of
items to be done you can use the menu :menuselection:`Stock Management --> Outgoing Products -->
Available Packing`.

.. i18n: The storesperson will then be able to make a partial delivery of the quantities actually available
.. i18n: and do a second packing operation later when the remaining products are available in stock.

The storesperson will then be able to make a partial delivery of the quantities actually available
and do a second packing operation later when the remaining products are available in stock.

.. i18n: If the packing mode is :guilabel:`Complete Delivery`, the packing list won't appear in the list of
.. i18n: packings to do until all of the products are available in stock. This way there will only be a
.. i18n: single delivery for any given order.

If the packing mode is :guilabel:`Complete Delivery`, the packing list won't appear in the list of
packings to do until all of the products are available in stock. This way there will only be a
single delivery for any given order.

.. i18n: If the storesperson wants, the delivery mode can be modified on each packing list even after the
.. i18n: order has been confirmed.

If the storesperson wants, the delivery mode can be modified on each packing list even after the
order has been confirmed.

.. i18n: In the case of invoicing on the basis of packing, the cost of delivering the products will be
.. i18n: calculated on the basis of multiple deliveries. This risks incurring a higher cost because of
.. i18n: each delivery. If invoicing is on the basis of the orders, the customer will only be invoiced
.. i18n: once for the whole delivery, even if the delivery of several items has already been made.

In the case of invoicing on the basis of packing, the cost of delivering the products will be
calculated on the basis of multiple deliveries. This risks incurring a higher cost because of
each delivery. If invoicing is on the basis of the orders, the customer will only be invoiced
once for the whole delivery, even if the delivery of several items has already been made.

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
