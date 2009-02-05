
.. module:: commission_pricelist
    :synopsis: Sale agent Information 
    :noindex:
.. 

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

Sale agent Information (*commission_pricelist*)
===============================================
:Module: commission_pricelist
:Name: Sale agent Information
:Version: False
:Author: Tiny
:Directory: commission_pricelist
:Web: 
:Official module: no
:Quality certified: no

Description
-----------

::

  Sale agent Info

Dependencies
------------

 * :mod:`base`
 * :mod:`product`

Reports
-------

None


Menus
-------


None


Views
-----


None



Objects
-------

Object: Sale agent sale info (sale.agent)
#########################################



:customer: Customer, one2many, readonly





:active: Active, boolean





:partner_id: Partner, many2one, required





:name: Saleagent Name, char, required





:commission_rate: Commission Rate, float, required


