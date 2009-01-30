
.. module:: hr_evaluation
    :synopsis: Human Resources Evaluation
    :noindex:
.. 

Human Resources Evaluation (*hr_evaluation*)
============================================
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

Object: Employee Evaluation (hr_evaluation.evaluation)
######################################################



:info_improve: To Improve, text





:employee_id: Employee, many2one, required





:user_id: Evaluation User, many2one, required





:name: Summary, char, required





:info_employee: Employee Response, text





:state: State, selection





:score: Score, float





:date: Date, date, required





:info_bad: Bad Points, text





:info_good: Good Points, text





:quote_ids: Quotes, one2many




Object: Employee Evaluation Type (hr_evaluation.type)
#####################################################



:info: Information, text





:name: Evaluation Criterion, char, required





:value_ids: Values, one2many





:category_ids: Appliable Role, many2many





:score: Score, float





:active: Active, boolean




Object: Evaluation Type Value (hr_evaluation.type.value)
########################################################



:score: Score, float





:name: Value, char, required





:type_id: Evaluation Type, many2one, required




Object: Employee Evaluation Quote (hr_evaluation.quote)
#######################################################



:evaluation_id: Evaluation, many2one, required





:value_id: Value, many2one





:score: Score, float





:name: Quote, char





:type_id: Type, many2one


