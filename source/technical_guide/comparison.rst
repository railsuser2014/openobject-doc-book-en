
Module ERP Comparisons (*comparison*)
=====================================
:Module: comparison
:Name: ERP Comparisons
:Version: 5.0.0.1
:Directory: comparison
:Web: http://www.openerp.com

Description
-----------

::

  This module lets you compare famous ERP systems and lets you vote their respective facilities(e.g. accounting, BOM Support, etc.) provided by them.

Dependencies
------------

 * base - installed

Reports
-------

None


Menus
-------

 * ERP Comparison
 * ERP Comparison/Configuration
 * ERP Comparison/Configuration/Users
 * ERP Comparison/Configuration/Items
 * ERP Comparison/Configuration/Criterions
 * ERP Comparison/Criterions Structure
 * ERP Comparison/Reporting
 * ERP Comparison/Reporting/Results of the Comparisons
 * ERP Comparison/Configuration/Vote Values(Criterias)
 * ERP Comparison/Votes
 * ERP Comparison/Votes/New Vote
 * ERP Comparison/Suggestions
 * ERP Comparison/Suggestions/New Suggestion

Views
-----

 * comparison.user.form (form)
 * comparison.user.tree (tree)
 * comparison.item.form (form)
 * comparison.item.tree (tree)
 * comparison.factor.form (form)
 * comparison.factor.list (tree)
 * comparison.factor.tree (tree)
 * comparison.factor.result.tree (tree)
 * comparison.vote.values.form (form)
 * comparison.vote.values.tree (tree)
 * comparison.vote.form (form)
 * comparison.vote.tree (tree)
 * comparison.ponderation.suggestion.form (form)
 * comparison.ponderation.suggestion.tree (tree)


Objects
-------

Object: comparison.user
#######################

.. index::
  single: comparison.user object
.. 


:active: Active, boolean



.. index::
  single: active field
.. 




:password: Password, char, required



.. index::
  single: password field
.. 




:name: Name, char, required



.. index::
  single: name field
.. 




:email: Email, char, required



.. index::
  single: email field
.. 



Object: comparison.item
#######################

.. index::
  single: comparison.item object
.. 


:user_id: User, many2one



.. index::
  single: user_id field
.. 




:name: Software, char, required



.. index::
  single: name field
.. 




:result_ids: Results, one2many



.. index::
  single: result_ids field
.. 




:note: Description, text



.. index::
  single: note field
.. 




:state: Status, selection, required



.. index::
  single: state field
.. 




:version: Version, char, required



.. index::
  single: version field
.. 



Object: comparison.factor
#########################

.. index::
  single: comparison.factor object
.. 


:user_id: User, many2one



.. index::
  single: user_id field
.. 




:name: Factor Name, char, required



.. index::
  single: name field
.. 




:result_ids: Results, one2many



.. index::
  single: result_ids field
.. 




:sequence: Sequence, integer



.. index::
  single: sequence field
.. 




:child_ids: Child Factors, one2many



.. index::
  single: child_ids field
.. 




:note: Note, text



.. index::
  single: note field
.. 




:parent_id: Parent Factor, many2one



.. index::
  single: parent_id field
.. 




:state: Status, selection, required



.. index::
  single: state field
.. 




:ponderation: Ponderation, float



.. index::
  single: ponderation field
.. 




:pond_computed: Computed Ponderation, float, readonly



.. index::
  single: pond_computed field
.. 




:type: Type, selection



.. index::
  single: type field
.. 



Object: comparison.vote.values
##############################

.. index::
  single: comparison.vote.values object
.. 


:name: Vote Type, char, required



.. index::
  single: name field
.. 




:factor: Factor, float, required



.. index::
  single: factor field
.. 



Object: comparison.vote
#######################

.. index::
  single: comparison.vote object
.. 


:item_id: Item, many2one, required



.. index::
  single: item_id field
.. 




:note: Note, text



.. index::
  single: note field
.. 




:factor_id: Factor, many2one, required



.. index::
  single: factor_id field
.. 




:user_id: User, many2one, required



.. index::
  single: user_id field
.. 




:score_id: Value, many2one, required



.. index::
  single: score_id field
.. 



Object: comparison.factor.result
################################

.. index::
  single: comparison.factor.result object
.. 


:item_id: Item, many2one, required, readonly



.. index::
  single: item_id field
.. 




:factor_id: Factor, many2one, required, readonly



.. index::
  single: factor_id field
.. 




:votes: Votes, float, readonly



.. index::
  single: votes field
.. 




:result: Goodness(%), float, readonly



.. index::
  single: result field
.. 



Object: comparison.ponderation.suggestion
#########################################

.. index::
  single: comparison.ponderation.suggestion object
.. 


:ponderation: Ponderation, float, required



.. index::
  single: ponderation field
.. 




:note: Suggestion, text



.. index::
  single: note field
.. 




:factor_id: Factor, many2one, required



.. index::
  single: factor_id field
.. 




:user_id: User, many2one, required



.. index::
  single: user_id field
.. 




:state: State, selection, readonly



.. index::
  single: state field
.. 

