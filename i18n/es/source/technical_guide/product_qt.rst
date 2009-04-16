
.. i18n: .. module:: product_qt
.. i18n:     :synopsis: Products & Pricelists 
.. i18n:     :noindex:
.. i18n: .. 

.. module:: product_qt
    :synopsis: Products & Pricelists 
    :noindex:
.. 

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. i18n: Products & Pricelists (*product_qt*)
.. i18n: ====================================
.. i18n: :Module: product_qt
.. i18n: :Name: Products & Pricelists
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: product_qt
.. i18n: :Web: 
.. i18n: :Official module: no
.. i18n: :Quality certified: no

Products & Pricelists (*product_qt*)
====================================
:Module: product_qt
:Name: Products & Pricelists
:Version: 5.0.1.0
:Author: Tiny
:Directory: product_qt
:Web: 
:Official module: no
:Quality certified: no

.. i18n: Description
.. i18n: -----------

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   This module add quality control and testing parameters in product
.. i18n:       1> configure QC parameters for particular product.
.. i18n:       2> QC testing on purchased raw material.
.. i18n:       3> QC testing during production.
.. i18n:       3> QC testing on finished goods.

::

  This module add quality control and testing parameters in product
      1> configure QC parameters for particular product.
      2> QC testing on purchased raw material.
      3> QC testing during production.
      3> QC testing on finished goods.

.. i18n: Dependencies
.. i18n: ------------

Dependencies
------------

.. i18n:  * :mod:`base`
.. i18n:  * :mod:`process`
.. i18n:  * :mod:`product`
.. i18n:  * :mod:`stock`
.. i18n:  * :mod:`mrp`

 * :mod:`base`
 * :mod:`process`
 * :mod:`product`
 * :mod:`stock`
 * :mod:`mrp`

.. i18n: Reports
.. i18n: -------

Reports
-------

.. i18n: None

None

.. i18n: Menus
.. i18n: -------

Menus
-------

.. i18n:  * Stock Management/Testing Result
.. i18n:  * Stock Management/Testing Result/Testing Result

 * Stock Management/Testing Result
 * Stock Management/Testing Result/Testing Result

.. i18n: Views
.. i18n: -----

Views
-----

.. i18n:  * quality.testing.form (form)
.. i18n:  * quality.testing.tree (tree)
.. i18n:  * quality.testing.config.tree (tree)
.. i18n:  * quality.testing.config.form (form)
.. i18n:  * \* INHERIT product.testing.form (form)
.. i18n:  * \* INHERIT quality.testing.form (form)
.. i18n:  * \* INHERIT quality.testing.move.form (form)
.. i18n:  * testing_result.tree (tree)
.. i18n:  * testing_result.form (form)
.. i18n:  * \* INHERIT quality.testing.mrp.production.form (form)
.. i18n:  * \* INHERIT quality.testing.mrp.production.tree (tree)
.. i18n:  * \* INHERIT quality.testing.mrp.form (form)

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

.. i18n: Objects
.. i18n: -------

Objects
-------

.. i18n: Object: quality testings (quality.test)
.. i18n: #######################################

Object: quality testings (quality.test)
#######################################

.. i18n: :name: Test Case, char

:name: Test Case, char

.. i18n: :description: Description, text

:description: Description, text

.. i18n: Object: testing.result (testing.result)
.. i18n: #######################################

Object: testing.result (testing.result)
#######################################

.. i18n: :product: Product, many2one, readonly

:product: Product, many2one, readonly

.. i18n: :type: Testing Type, selection, readonly

:type: Testing Type, selection, readonly

.. i18n: :test_date: Testing Date, date

:test_date: Testing Date, date

.. i18n: :test_case: Cases, one2many

:test_case: Cases, one2many

.. i18n: :tester: Tested By, many2one

:tester: Tested By, many2one

.. i18n: Object: quality test configuration (quality.test.config)
.. i18n: ########################################################

Object: quality test configuration (quality.test.config)
########################################################

.. i18n: :product_idf: Product, many2one

:product_idf: Product, many2one

.. i18n: :max_limit: Max Limit, float

:max_limit: Max Limit, float

.. i18n:     *Maximum Limit of measure*

    *Maximum Limit of measure*

.. i18n: :actual_val: Actual Value, float

:actual_val: Actual Value, float

.. i18n: :name: Test Case, many2one

:name: Test Case, many2one

.. i18n: :min_limit: Min Limit, float

:min_limit: Min Limit, float

.. i18n:     *Minimum Limit of measure*

    *Minimum Limit of measure*

.. i18n: :state: Status, selection, readonly

:state: Status, selection, readonly

.. i18n: :product_idr: Product, many2one

:product_idr: Product, many2one

.. i18n: :product_idp: Product, many2one

:product_idp: Product, many2one

.. i18n: :test_id: Test Result, many2one

:test_id: Test Result, many2one

.. i18n: :uom: UOM, many2one

:uom: UOM, many2one
