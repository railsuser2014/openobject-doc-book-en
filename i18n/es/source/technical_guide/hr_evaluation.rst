
.. i18n: .. module:: hr_evaluation
.. i18n:     :synopsis: Human Resources Evaluation 
.. i18n:     :noindex:
.. i18n: .. 

.. module:: hr_evaluation
    :synopsis: Human Resources Evaluation 
    :noindex:
.. 

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. i18n: Human Resources Evaluation (*hr_evaluation*)
.. i18n: ============================================
.. i18n: :Module: hr_evaluation
.. i18n: :Name: Human Resources Evaluation
.. i18n: :Version: 5.0.0.1
.. i18n: :Author: Tiny
.. i18n: :Directory: hr_evaluation
.. i18n: :Web: http://www.openerp.com/
.. i18n: :Official module: no
.. i18n: :Quality certified: no

Human Resources Evaluation (*hr_evaluation*)
============================================
:Module: hr_evaluation
:Name: Human Resources Evaluation
:Version: 5.0.0.1
:Author: Tiny
:Directory: hr_evaluation
:Web: http://www.openerp.com/
:Official module: no
:Quality certified: no

.. i18n: Description
.. i18n: -----------

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   Ability to create employees evaluation.

::

  Ability to create employees evaluation.

.. i18n: Dependencies
.. i18n: ------------

Dependencies
------------

.. i18n:  * :mod:`hr`

 * :mod:`hr`

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

.. i18n:  * Human Resources/Evaluations
.. i18n:  * Human Resources/Evaluations/HR Responsible
.. i18n:  * Human Resources/Evaluations/HR Responsible/Evaluations
.. i18n:  * Human Resources/Evaluations/HR Responsible/Next Evaluations
.. i18n:  * Human Resources/Evaluations/HR Responsible/My Next Evaluations
.. i18n:  * Human Resources/Evaluations/My Preceeding Evaluations
.. i18n:  * Human Resources/Evaluations/Configuration
.. i18n:  * Human Resources/Evaluations/Configuration/Evaluation Criterions

 * Human Resources/Evaluations
 * Human Resources/Evaluations/HR Responsible
 * Human Resources/Evaluations/HR Responsible/Evaluations
 * Human Resources/Evaluations/HR Responsible/Next Evaluations
 * Human Resources/Evaluations/HR Responsible/My Next Evaluations
 * Human Resources/Evaluations/My Preceeding Evaluations
 * Human Resources/Evaluations/Configuration
 * Human Resources/Evaluations/Configuration/Evaluation Criterions

.. i18n: Views
.. i18n: -----

Views
-----

.. i18n:  * hr_evaluation.quote.form (form)
.. i18n:  * hr_evaluation.quote.tree (tree)
.. i18n:  * hr_evaluation.evaluation.form (form)
.. i18n:  * hr_evaluation.evaluation.tree (tree)
.. i18n:  * hr_evaluation.evaluation.form.ro (form)
.. i18n:  * hr_evaluation.type.tree (tree)
.. i18n:  * hr_evaluation.type.form (form)

 * hr_evaluation.quote.form (form)
 * hr_evaluation.quote.tree (tree)
 * hr_evaluation.evaluation.form (form)
 * hr_evaluation.evaluation.tree (tree)
 * hr_evaluation.evaluation.form.ro (form)
 * hr_evaluation.type.tree (tree)
 * hr_evaluation.type.form (form)

.. i18n: Objects
.. i18n: -------

Objects
-------

.. i18n: Object: Employee Evaluation (hr_evaluation.evaluation)
.. i18n: ######################################################

Object: Employee Evaluation (hr_evaluation.evaluation)
######################################################

.. i18n: :info_improve: To Improve, text

:info_improve: To Improve, text

.. i18n: :employee_id: Employee, many2one, required

:employee_id: Employee, many2one, required

.. i18n: :user_id: Evaluation User, many2one, required

:user_id: Evaluation User, many2one, required

.. i18n: :name: Summary, char, required

:name: Summary, char, required

.. i18n: :info_employee: Employee Response, text

:info_employee: Employee Response, text

.. i18n: :state: State, selection

:state: State, selection

.. i18n: :score: Score, float

:score: Score, float

.. i18n: :date: Date, date, required

:date: Date, date, required

.. i18n: :info_bad: Bad Points, text

:info_bad: Bad Points, text

.. i18n: :info_good: Good Points, text

:info_good: Good Points, text

.. i18n: :quote_ids: Quotes, one2many

:quote_ids: Quotes, one2many

.. i18n: Object: Employee Evaluation Type (hr_evaluation.type)
.. i18n: #####################################################

Object: Employee Evaluation Type (hr_evaluation.type)
#####################################################

.. i18n: :info: Information, text

:info: Information, text

.. i18n: :name: Evaluation Criterion, char, required

:name: Evaluation Criterion, char, required

.. i18n: :value_ids: Values, one2many

:value_ids: Values, one2many

.. i18n: :category_ids: Appliable Role, many2many

:category_ids: Appliable Role, many2many

.. i18n: :score: Score, float

:score: Score, float

.. i18n: :active: Active, boolean

:active: Active, boolean

.. i18n: Object: Evaluation Type Value (hr_evaluation.type.value)
.. i18n: ########################################################

Object: Evaluation Type Value (hr_evaluation.type.value)
########################################################

.. i18n: :score: Score, float

:score: Score, float

.. i18n: :name: Value, char, required

:name: Value, char, required

.. i18n: :type_id: Evaluation Type, many2one, required

:type_id: Evaluation Type, many2one, required

.. i18n: Object: Employee Evaluation Quote (hr_evaluation.quote)
.. i18n: #######################################################

Object: Employee Evaluation Quote (hr_evaluation.quote)
#######################################################

.. i18n: :evaluation_id: Evaluation, many2one, required

:evaluation_id: Evaluation, many2one, required

.. i18n: :value_id: Value, many2one

:value_id: Value, many2one

.. i18n: :score: Score, float

:score: Score, float

.. i18n: :name: Quote, char

:name: Quote, char

.. i18n: :type_id: Type, many2one

:type_id: Type, many2one
