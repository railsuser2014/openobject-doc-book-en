
.. module:: crm_profiling
    :synopsis: crm_profiling management (Official, Quality Certified)
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="crm_profiling"></div>
    <script src="http://js-kit.com/ratings.js"></script>

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

Description
-----------

::

  This module allow users to perform segmentation within partners.
      It use the profiles criteria from the earlier segmentation module and improve it thanks to the new concept of questionnaire. You can now regroup questions into a questionnaire and directly use it on a partner.
  
      It also has been merged with the earlier CRM & SRM segmentation tool because they were overlapping.
  
  
      The menu items related are in "CRM & SRM\Configuration\Segmentations"
  
  
      * Note: this module is not compatible with the module segmentation, since it's the same which has been renamed.

Download links
--------------

You can download this module as a zip file in the following version:

  * `4.2 </download/modules/4.2/crm_profiling.zip>`_
  * `5.0 </download/modules/5.0/crm_profiling.zip>`_
  * `trunk </download/modules/trunk/crm_profiling.zip>`_


Dependencies
------------

 * :mod:`base`
 * :mod:`crm`

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

Object: Question (crm_profiling.question)
#########################################



:answers_ids: Avalaible answers, one2many





:name: Question, char, required




Object: Questionnaire (crm_profiling.questionnaire)
###################################################



:first: First question, many2one





:questions_ids: Questions, many2many





:name: Questionnaire, char, required





:description: Description, text, required




Object: Answer (crm_profiling.answer)
#####################################



:next: Next question, many2one





:name: Answer, char, required





:question_id: Question, many2one


