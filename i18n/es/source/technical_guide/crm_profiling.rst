
.. i18n: .. module:: crm_profiling
.. i18n:     :synopsis: crm_profiling management (Official, Quality Certified)
.. i18n:     :noindex:
.. i18n: .. 

.. module:: crm_profiling
    :synopsis: crm_profiling management (Official, Quality Certified)
    :noindex:
.. 

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. i18n: crm_profiling management (*crm_profiling*)
.. i18n: ==========================================
.. i18n: :Module: crm_profiling
.. i18n: :Name: crm_profiling management
.. i18n: :Version: 5.0.1.3
.. i18n: :Author: Tiny
.. i18n: :Directory: crm_profiling
.. i18n: :Web: http://www.openerp.com
.. i18n: :Official module: yes
.. i18n: :Quality certified: yes

crm_profiling management (*crm_profiling*)
==========================================
:Module: crm_profiling
:Name: crm_profiling management
:Version: 5.0.1.3
:Author: Tiny
:Directory: crm_profiling
:Web: http://www.openerp.com
:Official module: yes
:Quality certified: yes

.. i18n: Description
.. i18n: -----------

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   This module allow users to perform segmentation within partners.
.. i18n:   It use the profiles criteria from the earlier segmentation module and improve it thanks to the new 
.. i18n:   concept of questionnaire. 
.. i18n:   You can now regroup questions into a questionnaire and directly use it on a partner.
.. i18n:   
.. i18n:   It also has been merged with the earlier CRM & SRM segmentation tool because they were overlapping.
.. i18n:   The menu items related are in "CRM & SRM\Configuration\Segmentations"
.. i18n:       * Note: this module is not compatible with the module segmentation, since it's the same which 
.. i18n:               has been renamed.

::

  This module allow users to perform segmentation within partners.
  It use the profiles criteria from the earlier segmentation module and improve it thanks to the new 
  concept of questionnaire. 
  You can now regroup questions into a questionnaire and directly use it on a partner.
  
  It also has been merged with the earlier CRM & SRM segmentation tool because they were overlapping.
  The menu items related are in "CRM & SRM\Configuration\Segmentations"
      * Note: this module is not compatible with the module segmentation, since it's the same which 
              has been renamed.

.. i18n: Dependencies
.. i18n: ------------

Dependencies
------------

.. i18n:  * :mod:`base`
.. i18n:  * :mod:`crm`

 * :mod:`base`
 * :mod:`crm`

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

.. i18n:  * CRM & SRM/Configuration/Segmentations/Questionnaires
.. i18n:  * CRM & SRM/Configuration/Segmentations/Questions

 * CRM & SRM/Configuration/Segmentations/Questionnaires
 * CRM & SRM/Configuration/Segmentations/Questions

.. i18n: Views
.. i18n: -----

Views
-----

.. i18n:  * Questionnaires (tree)
.. i18n:  * Questionnaires (form)
.. i18n:  * Answers (tree)
.. i18n:  * Answers (form)
.. i18n:  * Questions (tree)
.. i18n:  * Questions (form)
.. i18n:  * \* INHERIT res.partner.profile.form (form)
.. i18n:  * crm.segmentation.tree (tree)

 * Questionnaires (tree)
 * Questionnaires (form)
 * Answers (tree)
 * Answers (form)
 * Questions (tree)
 * Questions (form)
 * \* INHERIT res.partner.profile.form (form)
 * crm.segmentation.tree (tree)

.. i18n: Objects
.. i18n: -------

Objects
-------

.. i18n: Object: Question (crm_profiling.question)
.. i18n: #########################################

Object: Question (crm_profiling.question)
#########################################

.. i18n: :answers_ids: Avalaible answers, one2many

:answers_ids: Avalaible answers, one2many

.. i18n: :open_question: Open Question, boolean

:open_question: Open Question, boolean

.. i18n: :name: Question, char, required

:name: Question, char, required

.. i18n: :target: Target, selection, required

:target: Target, selection, required

.. i18n: Object: Questionnaire (crm_profiling.questionnaire)
.. i18n: ###################################################

Object: Questionnaire (crm_profiling.questionnaire)
###################################################

.. i18n: :questions_ids: Questions, many2many

:questions_ids: Questions, many2many

.. i18n: :name: Questionnaire, char, required

:name: Questionnaire, char, required

.. i18n: :description: Description, text, required

:description: Description, text, required

.. i18n: Object: Answer (crm_profiling.answer)
.. i18n: #####################################

Object: Answer (crm_profiling.answer)
#####################################

.. i18n: :text: Open Answer, text

:text: Open Answer, text

.. i18n: :name: Answer, char, required

:name: Answer, char, required

.. i18n: :question_id: Question, many2one

:question_id: Question, many2one
