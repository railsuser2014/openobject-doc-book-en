
Module Human Resources Evaluation (*hr_evaluation*)
===================================================
:Module: hr_evaluation
:Name: Human Resources Evaluation
:Version: 5.0.0.1
:Directory: hr_evaluation
:Web: http://tinyerp.com/module_hr.html

Description
-----------

::

  Ability to create employees evaluation.

Dependencies
------------

 * hr - installed

Reports
-------

None


Menus
-------

 * Human Resources/Evaluations
 * Human Resources/Evaluations/HR Responsible
 * Human Resources/Evaluations/HR Responsible/Evaluations
 * Human Resources/Evaluations/HR Responsible/Next Evaluations
 * Human Resources/Evaluations/HR Responsible/My Next Evaluations
 * Human Resources/Evaluations/My Preceeding Evaluations
 * Human Resources/Evaluations/Configuration
 * Human Resources/Evaluations/Configuration/Evaluation Criterions

Views
-----

 * hr_evaluation.quote.form (form)
 * hr_evaluation.quote.tree (tree)
 * hr_evaluation.evaluation.form (form)
 * hr_evaluation.evaluation.tree (tree)
 * hr_evaluation.evaluation.form.ro (form)
 * hr_evaluation.type.tree (tree)
 * hr_evaluation.type.form (form)


Objects
-------

Object: Employee Evaluation
###########################

.. index::
  single: Employee Evaluation object
.. 


:info_improve: To Improve, text



.. index::
  single: info_improve field
.. 




:employee_id: Employee, many2one, required



.. index::
  single: employee_id field
.. 




:user_id: Evaluation User, many2one, required



.. index::
  single: user_id field
.. 




:name: Summary, char, required



.. index::
  single: name field
.. 




:info_employee: Employee Response, text



.. index::
  single: info_employee field
.. 




:state: State, selection



.. index::
  single: state field
.. 




:score: Score, float



.. index::
  single: score field
.. 




:date: Date, date, required



.. index::
  single: date field
.. 




:info_bad: Bad Points, text



.. index::
  single: info_bad field
.. 




:info_good: Good Points, text



.. index::
  single: info_good field
.. 




:quote_ids: Quotes, one2many



.. index::
  single: quote_ids field
.. 



Object: Employee Evaluation Type
################################

.. index::
  single: Employee Evaluation Type object
.. 


:info: Information, text



.. index::
  single: info field
.. 




:name: Evaluation Criterion, char, required



.. index::
  single: name field
.. 




:value_ids: Values, one2many



.. index::
  single: value_ids field
.. 




:category_ids: Appliable Role, many2many



.. index::
  single: category_ids field
.. 




:score: Score, float



.. index::
  single: score field
.. 




:active: Active, boolean



.. index::
  single: active field
.. 



Object: Evaluation Type Value
#############################

.. index::
  single: Evaluation Type Value object
.. 


:score: Score, float



.. index::
  single: score field
.. 




:name: Value, char, required



.. index::
  single: name field
.. 




:type_id: Evaluation Type, many2one, required



.. index::
  single: type_id field
.. 



Object: Employee Evaluation Quote
#################################

.. index::
  single: Employee Evaluation Quote object
.. 


:evaluation_id: Evaluation, many2one, required



.. index::
  single: evaluation_id field
.. 




:value_id: Value, many2one



.. index::
  single: value_id field
.. 




:score: Score, float



.. index::
  single: score field
.. 




:name: Quote, char



.. index::
  single: name field
.. 




:type_id: Type, many2one



.. index::
  single: type_id field
.. 

