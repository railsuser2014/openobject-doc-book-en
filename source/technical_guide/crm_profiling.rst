
crm_profiling management (*crm_profiling*)
==========================================
:Module: crm_profiling
:Name: crm_profiling management
:Version: 5.0.1.3
:Directory: crm_profiling
:Web: http://www.openerp.com

Description
-----------

::

  This module allow users to perform segmentation within partners.
      It use the profiles criteria from the earlier segmentation module and improve it thanks to the new concept of questionnaire. You can now regroup questions into a questionnaire and directly use it on a partner.
  
      It also has been merged with the earlier CRM & SRM segmentation tool because they were overlapping.
  
  
      The menu items related are in "CRM & SRM\Configuration\Segmentations"
  
  
      * Note: this module is not compatible with the module segmentation, since it's the same which has been renamed.

Dependencies
------------

 * base - installed
 * crm - installed

Reports
-------

None


Menus
-------

 * CRM & SRM/Configuration/Segmentations/Questionnaires
 * CRM & SRM/Configuration/Segmentations/Questions

Views
-----

 * Questionnaires (tree)
 * Questionnaires (form)
 * Answers (tree)
 * Answers (form)
 * Questions (tree)
 * Questions (form)
 * \* INHERIT res.partner.profile.form (form)
 * crm.segmentation.tree (tree)


Objects
-------

Object: Question
################



:answers_ids: Avalaible answers, one2many





:open_question: Open Question, boolean





:name: Question, char, required





:target: Target, selection, required




Object: Questionnaire
#####################



:questions_ids: Questions, many2many





:name: Questionnaire, char, required





:description: Description, text, required




Object: Answer
##############



:text: Open Answer, text





:name: Answer, char, required





:question_id: Question, many2one


