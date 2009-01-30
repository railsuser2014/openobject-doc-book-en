
.. module:: stock_location
    :synopsis: Stock Location Paths
    :noindex:
.. 

Stock Location Paths (*stock_location*)
=======================================
:Module: stock_location
:Name: Stock Location Paths
:Version: 5.0.1.0
:Directory: stock_location
:Web: 

Description
-----------

::

  Manages product's path in locations.
  
  This module may be useful for different purposes:
  * Manages the product in his whole manufacturing chain
  * Manages different default locations by products
  * Define paths within the warehouse to route products based on operations:
     - Quality Control
     - After Sales Services
     - Supplier Return
  * Manage products to be rent.

Dependencies
------------

 * stock - installed

Reports
-------

None


Menus
-------


None


Views
-----

 * stock.location.path.tree (tree)
 * stock.location.path.form (form)
 * \* INHERIT product.product.form (form)


Objects
-------

Object: stock.location.path (stock.location.path)
#################################################



:location_from_id: Source Location, many2one





:product_id: Products, many2one





:auto: Automatic Move, selection, required

    *This is used to define paths the product has to follow within the location tree.
    The 'Automatic Move' value will create a stock move after the current one that will be validated automatically. With 'Manual Operation', the stock move has to be validated by a worker. With 'Automatic No Step Added', the location is replaced in the original move.*



:delay: Delay (days), integer

    *Number of days to do this transition*



:location_dest_id: Destination Location, many2one





:name: Operation, char


