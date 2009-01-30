
.. module:: sale_supplier_direct_delivery
    :synopsis: Automates direct delivery between a supplier and a customer
    :noindex:
.. 

Automates direct delivery between a supplier and a customer (*sale_supplier_direct_delivery*)
=============================================================================================
:Module: sale_supplier_direct_delivery
:Name: Automates direct delivery between a supplier and a customer
:Version: 5.0.0.9
:Directory: sale_supplier_direct_delivery
:Web: 
:Is certified: no

Description
-----------

::

  Enable to send goods directly form supplier to customer taking special care of:
  - making only one picking from supplier location to customer location and using that picking in the sale_order workflow
  - copying the sale order shipping address to the generate purchase order line (so merging purchase orders later on will still work)
  
  Also take note of the following points:
  1) We set automatically a Sale Order line to direct delivery if there isn't enough product in the stock.
  2) We don't try to split such a line, but we set it entirely to direct delivery even if some products are available
  3) In a sale order, some lines can be set to direct while some others are on stock at the same time
  4) When we look if there is enough product on virtual stock for a line, we look at the time the sale order is confirmed,
  we don't try to anticipate if there will be enough virtual stock is the future if the sale order is planned for later.

Dependencies
------------

 * base - installed
 * product - installed
 * sale - installed
 * purchase - installed

Reports
-------

None


Menus
-------

 * Stock Management/Supplier Direct Delivery

Views
-----

 * \* INHERIT product.supplierinfo.tree.direct_delivery.inherit (tree)
 * \* INHERIT product.supplierinfo.form.direct_delivery.inherit (form)
 * \* INHERIT sale.order.tree.direct_delivery (tree)
 * \* INHERIT sale.order.line.form.direct_delivery (form)
 * \* INHERIT sale.order.line.tree.direct_delivery (form)
 * \* INHERIT purchase.order.tree.direct_delivery (tree)
 * \* INHERIT purchase.order.line.form.direct_delivery (form)
 * \* INHERIT purchase.order.line.tree.direct_delivery (tree)


Objects
-------

None
