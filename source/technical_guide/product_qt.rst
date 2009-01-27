
Module Products & Pricelists (*product_qt*)
===========================================
:Module: product_qt
:Name: Products & Pricelists
:Version: 5.0.1.0
:Directory: product_qt
:Web: 

Description
-----------

::

  This module add quality control and testing parameters in product
      1> configure QC parameters for particular product.
      2> QC testing on purchased raw material.
      3> QC testing during production.
      3> QC testing on finished goods.

Dependencies
------------

 * base - installed
 * process - installed
 * product - installed
 * stock - installed
 * mrp - installed

Reports
-------

None


Menus
-------

 * Stock Management/Testing Result
 * Stock Management/Testing Result/Testing Result

Views
-----

 * quality.testing.form (form)
 * quality.testing.tree (tree)
 * quality.testing.config.tree (tree)
 * quality.testing.config.form (form)
 * \* INHERIT product.testing.form (form)
 * \* INHERIT quality.testing.form (form)
 * \* INHERIT quality.testing.move.form (form)
 * testing_result.tree (tree)
 * testing_result.form (form)
 * \* INHERIT quality.testing.mrp.production.form (form)
 * \* INHERIT quality.testing.mrp.production.tree (tree)
 * \* INHERIT quality.testing.mrp.form (form)


Objects
-------

Object: quality testings
########################

.. index::
  single: quality testings object
.. 


:name: Test Case, char



.. index::
  single: name field
.. 




:description: Description, text



.. index::
  single: description field
.. 



Object: testing.result
######################

.. index::
  single: testing.result object
.. 


:product: Product, many2one, readonly



.. index::
  single: product field
.. 




:type: Testing Type, selection, readonly



.. index::
  single: type field
.. 




:test_date: Testing Date, date



.. index::
  single: test_date field
.. 




:test_case: Cases, one2many



.. index::
  single: test_case field
.. 




:tester: Tested By, many2one



.. index::
  single: tester field
.. 



Object: quality test configuration
##################################

.. index::
  single: quality test configuration object
.. 


:product_idf: Product, many2one



.. index::
  single: product_idf field
.. 




:max_limit: Max Limit, float

    *Maximum Limit of measure*

.. index::
  single: max_limit field
.. 




:actual_val: Actual Value, float



.. index::
  single: actual_val field
.. 




:name: Test Case, many2one



.. index::
  single: name field
.. 




:min_limit: Min Limit, float

    *Minimum Limit of measure*

.. index::
  single: min_limit field
.. 




:state: Status, selection, readonly



.. index::
  single: state field
.. 




:product_idr: Product, many2one



.. index::
  single: product_idr field
.. 




:product_idp: Product, many2one



.. index::
  single: product_idp field
.. 




:test_id: Test Result, many2one



.. index::
  single: test_id field
.. 




:uom: UOM, many2one



.. index::
  single: uom field
.. 

