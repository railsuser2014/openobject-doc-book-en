
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



:name: Test Case, char





:description: Description, text




Object: testing.result
######################



:product: Product, many2one, readonly





:type: Testing Type, selection, readonly





:test_date: Testing Date, date





:test_case: Cases, one2many





:tester: Tested By, many2one




Object: quality test configuration
##################################



:product_idf: Product, many2one





:max_limit: Max Limit, float

    *Maximum Limit of measure*



:actual_val: Actual Value, float





:name: Test Case, many2one





:min_limit: Min Limit, float

    *Minimum Limit of measure*



:state: Status, selection, readonly





:product_idr: Product, many2one





:product_idp: Product, many2one





:test_id: Test Result, many2one





:uom: UOM, many2one


