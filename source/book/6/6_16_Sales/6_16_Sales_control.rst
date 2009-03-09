
Control of deliveries and invoicing
===================================

Configuration of orders
-----------------------

.. index:: 
   pair: control; delivery
   pair: control; invoicing

Depending on the configuration of the order, several different possible consequences can follow.
Three fields determine the future behaviour of an order:

* :guilabel:`Packing Policy` : ``Partial Delivery`` or ``Complete Delivery``,

* :guilabel:`Shipping Policy` : ``Shipping & Manual Invoice``, ``Payment Before Delivery``,
  ``Invoice on Order After Delivery``, and ``Invoice from the Packing``,

* :guilabel:`Invoice on` : ``Ordered Quantities`` or ``Delivered Quantities``.

  .. tip::  Simplified view

     If you work in the ``Simplified View`` mode, only the :guilabel:`Shipping Policy` field is visible
     in the second tab on the order.
     To get to the ``Extended View`` mode, assign the group :guilabel:`Usability – Extended View` to the current
     user.

Packing mode
------------

The packing mode determines the way that the storesperson will do the packing. If the order is put
into :guilabel:`Partial Delivery` mode, the packing order will appear in the list of things for the
storesperson to do as soon as any of the products on the order is available. To get the list of
items to be done you can use the menu :menuselection:`Stock Management --> Outgoing Products -->
Available Packing`.

The storesperson will then be able to make a partial delivery of the quantities actually available
and do a second packing operation later when the remaining products are available in stock.

If the packing mode is :guilabel:`Complete Delivery`, the packing list won't appear in the list of
packings to do until all of the products are available in stock. This way there will only be a
single delivery for any given order.

If the storesperson wants, the delivery mode can be modified on each packing list even after the
order has been confirmed.

In the case of invoicing on the basis of packing, the cost of delivering the products will be
calculated on the basis of multiple deliveries. This risks incurring a higher cost because of
each delivery. If invoicing is on the basis of the orders, the customer will only be invoiced
once for the whole delivery, even if the delivery of several items has already been made.

.. Copyright © Open Object Press. All rights reserved.

.. You may take electronic copy of this publication and distribute it if you don't
.. change the content. You can also print a copy to be read by yourself only.

.. We have contracts with different publishers in different countries to sell and
.. distribute paper or electronic based versions of this book (translated or not)
.. in bookstores. This helps to distribute and promote the Open ERP product. It
.. also helps us to create incentives to pay contributors and authors using author
.. rights of these sales.

.. Due to this, grants to translate, modify or sell this book are strictly
.. forbidden, unless Tiny SPRL (representing Open Object Press) gives you a
.. written authorisation for this.

.. Many of the designations used by manufacturers and suppliers to distinguish their
.. products are claimed as trademarks. Where those designations appear in this book,
.. and Open Object Press was aware of a trademark claim, the designations have been
.. printed in initial capitals.

.. While every precaution has been taken in the preparation of this book, the publisher
.. and the authors assume no responsibility for errors or omissions, or for damages
.. resulting from the use of the information contained herein.

.. Published by Open Object Press, Grand Rosière, Belgium
