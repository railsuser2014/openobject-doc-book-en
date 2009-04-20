
.. module:: base_module_quality
    :synopsis: Base module quality (Quality Certified)
    :noindex:
.. 

.. raw:: html

      <br />
    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. tip:: This module is part of the Open ERP software, the leading Open Source 
  enterprise management system. If you want to discover Open ERP, check our 
  `screencasts <href="http://openerp.tv>`_ or download 
  `Open ERP <href="http://openerp.com>`_ directly.

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/base_module_quality"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Base module quality (*base_module_quality*)
===========================================
:Module: base_module_quality
:Name: Base module quality
:Version: 5.0.1.0
:Author: Tiny
:Directory: base_module_quality
:Web: http://www.openerp.com
:Official module: no
:Quality certified: yes

Description
-----------

::

  This module's aim is to check the quality of other modules.
  
  It defines a wizard on the list of modules in OpenERP, which allow you to
  evaluate them on different criteria such as: the respect of OpenERP coding
  standards, the speed efficiency...
  
  This module also provides generic framework to define your own quality test.
  For further info, coders may take a look into base_module_quality\README.txt
  
  WARNING: This module can not work as a ZIP file, you must unzip it before
  using it, otherwise it may crash.

Download links
--------------

You can download this module as a zip file in the following version:

  * `trunk <http://www.openerp.com/download/modules/trunk/base_module_quality.zip>`_


Dependencies
------------

 * :mod:`base`

Reports
-------

None


Menus
-------


None


Views
-----

 * Results of Quality Checks (tree)
 * Results of Quality Checks (form)
 * Results of Quality Checks with detail (form)
 * Results of Quality Checks with detail (tree)


Objects
-------

Object: wizard.quality.check (wizard.quality.check)
###################################################



:final_score: Final Score (%), char





:name: Rated Module, char





:test_ids: Tests, one2many




Object: quality.check.detail (quality.check.detail)
###################################################



:name: Name, char





:detail: Details, text





:summary: Summary, text





:note: Note, text





:state: State, selection

    *The test will be completed only if the module is installed or if the test may be processed on uninstalled module.*



:score: Score (%), float





:quality_check_id: Quality, many2one





:ponderation: Ponderation, float

    *Some tests are more critical than others, so they have a bigger weight in the computation of final rating*
