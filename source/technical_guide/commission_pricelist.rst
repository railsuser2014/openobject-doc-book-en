
Module Sale agent Information (*commission_pricelist*)
======================================================
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

.. index::
  single: Sale agent sale info object
.. 


:customer: Customer, one2many, readonly



.. index::
  single: customer field
.. 




:active: Active, boolean



.. index::
  single: active field
.. 




:partner_id: Partner, many2one, required



.. index::
  single: partner_id field
.. 




:name: Saleagent Name, char, required



.. index::
  single: name field
.. 




:commission_rate: Commission Rate, float, required



.. index::
  single: commission_rate field
.. 

