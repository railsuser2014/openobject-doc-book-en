
Module Skill Management (*hr_skill*)
====================================
:Module: hr_skill
:Name: Skill Management
:Version: 5.0.0.1
:Directory: hr_skill
:Web: http://www.tinyerp.com

Description
-----------

::

  Generic and powerfull skill management system. This module allows you to manage your company and employees skills, interviews, ...

Dependencies
------------

 * hr - installed

Reports
-------

 * Evaluation report

Menus
-------

 * Human Resources/Configuration/Skills Management
 * Human Resources/Configuration/Skills Management/Skills
 * Human Resources/Configuration/Skills Management/Skills Structure
 * Human Resources/Configuration/Skills Management/Positions
 * Human Resources/Configuration/Skills Management/Profiles
 * Human Resources/Configuration/Skills Management/Weight Categories
 * Human Resources/Configuration/Skills Management/Weights
 * Human Resources/Configuration/Skills Management/Experience Categories
 * Human Resources/Configuration/Skills Management/Experiences
 * Human Resources/Configuration/Skills Management/Evaluations
 * Human Resources/Configuration/Skills Management/Languages
 * Human Resources/Configuration/Skills Management/Scale Grade 
 * Human Resources/Configuration/Skills Management/Employees Status

Views
-----

 * hr_skill.skill.form (form)
 * hr_skill.skill.tree (tree)
 * hr_skill.position.form (form)
 * hr_skill.profile.form (form)
 * hr_skill.weight.category.form (form)
 * hr_skill.weight.form (form)
 * hr_skill.experience.category.form (form)
 * hr_skill.experience.form (form)
 * hr_skill.evaluation.form (form)
 * hr_skill.evaluation.tree (tree)
 * \* INHERIT hr.employee.form (form)
 * Languages (form)
 * Languages (tree)
 * Languages (form)
 * Languages (tree)
 * \* INHERIT employee.grade.form1.inherit (form)
 * Pay Scales (form)
 * Pay Scales (tree)
 * employee.status.form (form)


Objects
-------

Object: hr_skill.weight.category
################################

.. index::
  single: hr_skill.weight.category object
.. 


:name: Name, char, required



.. index::
  single: name field
.. 



Object: hr_skill.weight
#######################

.. index::
  single: hr_skill.weight object
.. 


:category_id: Category, many2one, required



.. index::
  single: category_id field
.. 




:name: Name, char, required



.. index::
  single: name field
.. 




:value: Numerical value, float, required



.. index::
  single: value field
.. 



Object: hr_skill.skill
######################

.. index::
  single: hr_skill.skill object
.. 


:name: Name, char, required



.. index::
  single: name field
.. 




:weight: Weight, float, required



.. index::
  single: weight field
.. 




:child_ids: Childs, one2many



.. index::
  single: child_ids field
.. 




:parent_id: Parent, many2one



.. index::
  single: parent_id field
.. 




:weight_category_id: Weight Category, many2one



.. index::
  single: weight_category_id field
.. 




:active: Active, boolean



.. index::
  single: active field
.. 




:view: Skill, selection, required



.. index::
  single: view field
.. 



Object: hr_skill.experience.category
####################################

.. index::
  single: hr_skill.experience.category object
.. 


:name: Name, char, required



.. index::
  single: name field
.. 



Object: hr_skill.experience
###########################

.. index::
  single: hr_skill.experience object
.. 


:skill_ids: Skills, one2many



.. index::
  single: skill_ids field
.. 




:category_id: Category, many2one



.. index::
  single: category_id field
.. 




:name: Name, char, required



.. index::
  single: name field
.. 




:sequence: Sequence, integer



.. index::
  single: sequence field
.. 



Object: hr_skill.evaluation.category
####################################

.. index::
  single: hr_skill.evaluation.category object
.. 


:name: Name, char, required



.. index::
  single: name field
.. 



Object: hr_skill.evaluation
###########################

.. index::
  single: hr_skill.evaluation object
.. 


:experience_ids: Experience, one2many



.. index::
  single: experience_ids field
.. 




:employee_id: Evaluated Employee, many2one



.. index::
  single: employee_id field
.. 




:name: Evaluation name, char, required



.. index::
  single: name field
.. 




:reference: Reference, char



.. index::
  single: reference field
.. 




:skill_ids: Skill, one2many



.. index::
  single: skill_ids field
.. 




:interviewer_name: Evaluator, char, required



.. index::
  single: interviewer_name field
.. 




:interviewee_name: Evaluated People, char, required



.. index::
  single: interviewee_name field
.. 




:note: Notes, text



.. index::
  single: note field
.. 




:date: Date, date, required



.. index::
  single: date field
.. 




:category_id: Category, many2one



.. index::
  single: category_id field
.. 



Object: hr_skill.profile
########################

.. index::
  single: hr_skill.profile object
.. 


:skill_ids: Skills, one2many



.. index::
  single: skill_ids field
.. 




:name: Name, char, required



.. index::
  single: name field
.. 



Object: hr_skill.position
#########################

.. index::
  single: hr_skill.position object
.. 


:status: Status, selection



.. index::
  single: status field
.. 




:profile_ids: Profiles, one2many



.. index::
  single: profile_ids field
.. 




:employee_id: Assigned Employee, many2one



.. index::
  single: employee_id field
.. 




:name: Name, char, required



.. index::
  single: name field
.. 



Object: hr_skill.position.profile
#################################

.. index::
  single: hr_skill.position.profile object
.. 


:position_id: Position, many2one, required



.. index::
  single: position_id field
.. 




:weight_id: Weight, many2one, required



.. index::
  single: weight_id field
.. 




:profile_id: Profile, many2one, required



.. index::
  single: profile_id field
.. 




:name: Name, char



.. index::
  single: name field
.. 



Object: hr_skill.experience.skill
#################################

.. index::
  single: hr_skill.experience.skill object
.. 


:weight_id: Weight, many2one, required



.. index::
  single: weight_id field
.. 




:experience_id: Experience, many2one, required



.. index::
  single: experience_id field
.. 




:name: Name, char, required



.. index::
  single: name field
.. 




:skill_id: Skill, many2one, required



.. index::
  single: skill_id field
.. 



Object: hr_skill.profile.skill
##############################

.. index::
  single: hr_skill.profile.skill object
.. 


:weight_id: Weight, many2one, required



.. index::
  single: weight_id field
.. 




:profile_id: Profile, many2one, required



.. index::
  single: profile_id field
.. 




:name: Name, char



.. index::
  single: name field
.. 




:skill_id: Skill, many2one, required



.. index::
  single: skill_id field
.. 



Object: hr_skill.evaluation.experience
######################################

.. index::
  single: hr_skill.evaluation.experience object
.. 


:weight_id: Weight, many2one, required



.. index::
  single: weight_id field
.. 




:evaluation_id: Evaluation, many2one, required



.. index::
  single: evaluation_id field
.. 




:name: Name, char, required



.. index::
  single: name field
.. 




:experience_id: Experience, many2one, required



.. index::
  single: experience_id field
.. 



Object: hr_skill.evaluation.skill
#################################

.. index::
  single: hr_skill.evaluation.skill object
.. 


:weight_id: Weight, many2one, required



.. index::
  single: weight_id field
.. 




:evaluation_id: Evaluation, many2one, required



.. index::
  single: evaluation_id field
.. 




:name: Name, char



.. index::
  single: name field
.. 




:skill_id: Skill, many2one, required



.. index::
  single: skill_id field
.. 



Object: Languages
#################

.. index::
  single: Languages object
.. 


:name: Language, char



.. index::
  single: name field
.. 



Object: Languages
#################

.. index::
  single: Languages object
.. 


:read: Read, boolean



.. index::
  single: read field
.. 




:write: Write, boolean



.. index::
  single: write field
.. 




:speak: Speak, boolean



.. index::
  single: speak field
.. 




:name: Language, many2one



.. index::
  single: name field
.. 




:ii_id: languages known, many2one



.. index::
  single: ii_id field
.. 



Object: Pay Scales
##################

.. index::
  single: Pay Scales object
.. 


:code: Code, char



.. index::
  single: code field
.. 




:name: Name, char



.. index::
  single: name field
.. 




:increase: Step Increase, integer



.. index::
  single: increase field
.. 




:min_sal: Minimum Salary, integer



.. index::
  single: min_sal field
.. 




:max_sal: Maximum Salary, integer



.. index::
  single: max_sal field
.. 




:cur: Currency, selection



.. index::
  single: cur field
.. 



Object: employee.status
#######################

.. index::
  single: employee.status object
.. 


:name: Status Name, char, required



.. index::
  single: name field
.. 

