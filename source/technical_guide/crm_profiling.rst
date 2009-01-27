
Module crm_profiling management (*crm_profiling*)
=================================================
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

.. index::
  single: Question object
.. 


:answers_ids: Avalaible answers, one2many



.. index::
  single: answers_ids field
.. 




:open_question: Open Question, boolean



.. index::
  single: open_question field
.. 




:name: Question, char, required



.. index::
  single: name field
.. 




:target: Target, selection, required



.. index::
  single: target field
.. 



Object: Questionnaire
#####################

.. index::
  single: Questionnaire object
.. 


:questions_ids: Questions, many2many



.. index::
  single: questions_ids field
.. 




:name: Questionnaire, char, required



.. index::
  single: name field
.. 




:description: Description, text, required



.. index::
  single: description field
.. 



Object: Answer
##############

.. index::
  single: Answer object
.. 


:text: Open Answer, text



.. index::
  single: text field
.. 




:name: Answer, char, required



.. index::
  single: name field
.. 




:question_id: Question, many2one



.. index::
  single: question_id field
.. 

