
Sale agent Information (*commission_pricelist*)
===============================================
:Module: commission_pricelist
:Name: Sale agent Information
:Version: False
:Directory: commission_pricelist
:Web: 

Description
-----------

::

  Sale agent Info

Dependencies
------------

 * base - installed
 * product - installed

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

Object: Sale agent sale info
############################



:customer: Customer, one2many, readonly





:active: Active, boolean





:partner_id: Partner, many2one, required





:name: Saleagent Name, char, required





:commission_rate: Commission Rate, float, required


