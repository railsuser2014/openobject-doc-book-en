
.. module:: product_index
    :synopsis: Manage indexes on products prices
    :noindex:
.. 

Manage indexes on products prices (*product_index*)
===================================================
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

 * Books/Configuration/Indexes
 * Books/Configuration/Indexes/New index

Views
-----

 * product.index.tree (tree)
 * product.index.form (form)
 * \* INHERIT product.normal.form (form)


Objects
-------

Object: Index (product.index)
#############################



:rate_ids: Rates, one2many





:code: Index code, char





:name: Index name, char, required





:rounding: Rounding factor, float





:rate: Current rate, float, readonly





:active: Active, boolean




Object: Index Rate (product.index.rate)
#######################################



:rate: Rate, float, required





:index_id: index, many2one, readonly





:name: Date, date, required


