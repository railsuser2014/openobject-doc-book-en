
Base module quality (*base_module_quality*)
===========================================
:Module: base_module_quality
:Name: Base module quality
:Version: 5.0.1.0
:Directory: base_module_quality
:Web: 

Description
-----------

::

  This module's aim is to check the quality of other modules.
  
      It defines a wizard on the list of modules in OpenERP, which allow you to evaluate them on different criteria such as: the respect of OpenERP coding standards, the speed efficiency...
  
      This module also provides generic framework to define your own quality test. For further info, coders may take a look into base_module_quality\README.txt

Dependencies
------------

 * base - installed

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

Object: wizard.quality.check
############################



:final_score: Final Score (%), char





:name: Rated Module, char





:test_ids: Tests, one2many




Object: quality.check.detail
############################



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
