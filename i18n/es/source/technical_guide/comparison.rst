
.. i18n: .. module:: comparison
.. i18n:     :synopsis: ERP Comparisons 
.. i18n:     :noindex:
.. i18n: .. 

.. module:: comparison
    :synopsis: ERP Comparisons 
    :noindex:
.. 

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. i18n: ERP Comparisons (*comparison*)
.. i18n: ==============================
.. i18n: :Module: comparison
.. i18n: :Name: ERP Comparisons
.. i18n: :Version: 5.0.0.1
.. i18n: :Author: Tiny
.. i18n: :Directory: comparison
.. i18n: :Web: http://www.openerp.com
.. i18n: :Official module: no
.. i18n: :Quality certified: no

ERP Comparisons (*comparison*)
==============================
:Module: comparison
:Name: ERP Comparisons
:Version: 5.0.0.1
:Author: Tiny
:Directory: comparison
:Web: http://www.openerp.com
:Official module: no
:Quality certified: no

.. i18n: Description
.. i18n: -----------

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   This module lets you compare famous ERP systems and lets you vote their respective facilities
.. i18n:   (e.g. accounting, BOM Support, etc.) provided by them.

::

  This module lets you compare famous ERP systems and lets you vote their respective facilities
  (e.g. accounting, BOM Support, etc.) provided by them.

.. i18n: Dependencies
.. i18n: ------------

Dependencies
------------

.. i18n:  * :mod:`base`

 * :mod:`base`

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

.. i18n:  * ERP Comparison
.. i18n:  * ERP Comparison/Configuration
.. i18n:  * ERP Comparison/Configuration/Users
.. i18n:  * ERP Comparison/Configuration/Items
.. i18n:  * ERP Comparison/Configuration/Criterions
.. i18n:  * ERP Comparison/Criterions Structure
.. i18n:  * ERP Comparison/Reporting
.. i18n:  * ERP Comparison/Reporting/Results of the Comparisons
.. i18n:  * ERP Comparison/Configuration/Vote Values(Criterias)
.. i18n:  * ERP Comparison/Votes
.. i18n:  * ERP Comparison/Votes/New Vote
.. i18n:  * ERP Comparison/Suggestions
.. i18n:  * ERP Comparison/Suggestions/New Suggestion

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

.. i18n: Views
.. i18n: -----

Views
-----

.. i18n:  * comparison.user.form (form)
.. i18n:  * comparison.user.tree (tree)
.. i18n:  * comparison.item.form (form)
.. i18n:  * comparison.item.tree (tree)
.. i18n:  * comparison.factor.form (form)
.. i18n:  * comparison.factor.list (tree)
.. i18n:  * comparison.factor.tree (tree)
.. i18n:  * comparison.factor.result.tree (tree)
.. i18n:  * comparison.vote.values.form (form)
.. i18n:  * comparison.vote.values.tree (tree)
.. i18n:  * comparison.vote.form (form)
.. i18n:  * comparison.vote.tree (tree)
.. i18n:  * comparison.ponderation.suggestion.form (form)
.. i18n:  * comparison.ponderation.suggestion.tree (tree)

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

.. i18n: Objects
.. i18n: -------

Objects
-------

.. i18n: Object: comparison.user (comparison.user)
.. i18n: #########################################

Object: comparison.user (comparison.user)
#########################################

.. i18n: :active: Active, boolean

:active: Active, boolean

.. i18n: :password: Password, char, required

:password: Password, char, required

.. i18n: :name: Name, char, required

:name: Name, char, required

.. i18n: :email: Email, char, required

:email: Email, char, required

.. i18n: Object: comparison.item (comparison.item)
.. i18n: #########################################

Object: comparison.item (comparison.item)
#########################################

.. i18n: :user_id: User, many2one

:user_id: User, many2one

.. i18n: :name: Software, char, required

:name: Software, char, required

.. i18n: :result_ids: Results, one2many

:result_ids: Results, one2many

.. i18n: :note: Description, text

:note: Description, text

.. i18n: :state: Status, selection, required

:state: Status, selection, required

.. i18n: :version: Version, char, required

:version: Version, char, required

.. i18n: Object: comparison.factor (comparison.factor)
.. i18n: #############################################

Object: comparison.factor (comparison.factor)
#############################################

.. i18n: :user_id: User, many2one

:user_id: User, many2one

.. i18n: :name: Factor Name, char, required

:name: Factor Name, char, required

.. i18n: :result_ids: Results, one2many

:result_ids: Results, one2many

.. i18n: :sequence: Sequence, integer

:sequence: Sequence, integer

.. i18n: :child_ids: Child Factors, one2many

:child_ids: Child Factors, one2many

.. i18n: :note: Note, text

:note: Note, text

.. i18n: :parent_id: Parent Factor, many2one

:parent_id: Parent Factor, many2one

.. i18n: :state: Status, selection, required

:state: Status, selection, required

.. i18n: :ponderation: Ponderation, float

:ponderation: Ponderation, float

.. i18n: :pond_computed: Computed Ponderation, float, readonly

:pond_computed: Computed Ponderation, float, readonly

.. i18n: :type: Type, selection

:type: Type, selection

.. i18n: Object: comparison.vote.values (comparison.vote.values)
.. i18n: #######################################################

Object: comparison.vote.values (comparison.vote.values)
#######################################################

.. i18n: :name: Vote Type, char, required

:name: Vote Type, char, required

.. i18n: :factor: Factor, float, required

:factor: Factor, float, required

.. i18n: Object: comparison.vote (comparison.vote)
.. i18n: #########################################

Object: comparison.vote (comparison.vote)
#########################################

.. i18n: :item_id: Item, many2one, required

:item_id: Item, many2one, required

.. i18n: :note: Note, text

:note: Note, text

.. i18n: :factor_id: Factor, many2one, required

:factor_id: Factor, many2one, required

.. i18n: :user_id: User, many2one, required

:user_id: User, many2one, required

.. i18n: :score_id: Value, many2one, required

:score_id: Value, many2one, required

.. i18n: Object: comparison.factor.result (comparison.factor.result)
.. i18n: ###########################################################

Object: comparison.factor.result (comparison.factor.result)
###########################################################

.. i18n: :item_id: Item, many2one, required, readonly

:item_id: Item, many2one, required, readonly

.. i18n: :factor_id: Factor, many2one, required, readonly

:factor_id: Factor, many2one, required, readonly

.. i18n: :votes: Votes, float, readonly

:votes: Votes, float, readonly

.. i18n: :result: Goodness(%), float, readonly

:result: Goodness(%), float, readonly

.. i18n: Object: comparison.ponderation.suggestion (comparison.ponderation.suggestion)
.. i18n: #############################################################################

Object: comparison.ponderation.suggestion (comparison.ponderation.suggestion)
#############################################################################

.. i18n: :ponderation: Ponderation, float, required

:ponderation: Ponderation, float, required

.. i18n: :note: Suggestion, text

:note: Suggestion, text

.. i18n: :factor_id: Factor, many2one, required

:factor_id: Factor, many2one, required

.. i18n: :user_id: User, many2one, required

:user_id: User, many2one, required

.. i18n: :state: State, selection, readonly

:state: State, selection, readonly
