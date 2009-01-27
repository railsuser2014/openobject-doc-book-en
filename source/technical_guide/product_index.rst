
Module Manage indexes on products prices (*product_index*)
==========================================================
:Module: product_index
:Name: Manage indexes on products prices
:Version: 5.0.1.0
:Directory: product_index
:Web: http://www.tinyerp.com

Description
-----------

::

  None

Dependencies
------------

 * product - installed

Reports
-------

None


Menus
-------

 * Products/Configuration/Indexes
 * Products/Configuration/Indexes/New index

Views
-----

 * product.index.tree (tree)
 * product.index.form (form)
 * \* INHERIT product.normal.form (form)


Objects
-------

Object: Index
#############

.. index::
  single: Index object
.. 


:rate_ids: Rates, one2many



.. index::
  single: rate_ids field
.. 




:code: Index code, char



.. index::
  single: code field
.. 




:name: Index name, char, required



.. index::
  single: name field
.. 




:rounding: Rounding factor, float



.. index::
  single: rounding field
.. 




:rate: Current rate, float, readonly



.. index::
  single: rate field
.. 




:active: Active, boolean



.. index::
  single: active field
.. 



Object: Index Rate
##################

.. index::
  single: Index Rate object
.. 


:rate: Rate, float, required



.. index::
  single: rate field
.. 




:index_id: index, many2one, readonly



.. index::
  single: index_id field
.. 




:name: Date, date, required



.. index::
  single: name field
.. 

