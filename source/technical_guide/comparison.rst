
ERP Comparisons (*comparison*)
==============================
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



:active: Active, boolean





:password: Password, char, required





:name: Name, char, required





:email: Email, char, required




Object: comparison.item
#######################



:user_id: User, many2one





:name: Software, char, required





:result_ids: Results, one2many





:note: Description, text





:state: Status, selection, required





:version: Version, char, required




Object: comparison.factor
#########################



:user_id: User, many2one





:name: Factor Name, char, required





:result_ids: Results, one2many





:sequence: Sequence, integer





:child_ids: Child Factors, one2many





:note: Note, text





:parent_id: Parent Factor, many2one





:state: Status, selection, required





:ponderation: Ponderation, float





:pond_computed: Computed Ponderation, float, readonly





:type: Type, selection




Object: comparison.vote.values
##############################



:name: Vote Type, char, required





:factor: Factor, float, required




Object: comparison.vote
#######################



:item_id: Item, many2one, required





:note: Note, text





:factor_id: Factor, many2one, required





:user_id: User, many2one, required





:score_id: Value, many2one, required




Object: comparison.factor.result
################################



:item_id: Item, many2one, required, readonly





:factor_id: Factor, many2one, required, readonly





:votes: Votes, float, readonly





:result: Goodness(%), float, readonly




Object: comparison.ponderation.suggestion
#########################################



:ponderation: Ponderation, float, required





:note: Suggestion, text





:factor_id: Factor, many2one, required





:user_id: User, many2one, required





:state: State, selection, readonly


