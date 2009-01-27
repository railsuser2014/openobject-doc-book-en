
Module Base module quality (*base_module_quality*)
==================================================
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

.. index::
  single: wizard.quality.check object
.. 


:final_score: Final Score (%), char



.. index::
  single: final_score field
.. 




:name: Rated Module, char



.. index::
  single: name field
.. 




:test_ids: Tests, one2many



.. index::
  single: test_ids field
.. 



Object: quality.check.detail
############################

.. index::
  single: quality.check.detail object
.. 


:name: Name, char



.. index::
  single: name field
.. 




:detail: Details, text



.. index::
  single: detail field
.. 




:summary: Summary, text



.. index::
  single: summary field
.. 




:note: Note, text



.. index::
  single: note field
.. 




:state: State, selection

    *The test will be completed only if the module is installed or if the test may be processed on uninstalled module.*

.. index::
  single: state field
.. 




:score: Score (%), float



.. index::
  single: score field
.. 




:quality_check_id: Quality, many2one



.. index::
  single: quality_check_id field
.. 




:ponderation: Ponderation, float

    *Some tests are more critical than others, so they have a bigger weight in the computation of final rating*

.. index::
  single: ponderation field
.. 

