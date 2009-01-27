
Module Enterprise Process (*process*)
=====================================
:Module: process
:Name: Enterprise Process
:Version: 5.0.1.0
:Directory: process
:Web: http://www.openerp.com

Description
-----------

::

  This module allows you to manage your process for the end-users.

Dependencies
------------

 * base - installed

Reports
-------

None


Menus
-------

 * Administration/Customization/Enterprise Processes
 * Administration/Customization/Enterprise Processes/Process
 * Administration/Customization/Enterprise Processes/Process Nodes
 * Administration/Customization/Enterprise Processes/Process Transitions

Views
-----

 * process.process.form (form)
 * process.process.tree (tree)
 * process.node.tree (tree)
 * process.node.form (form)
 * process.transition.tree (tree)
 * process.transition.form (form)


Objects
-------

Object: Process
###############

.. index::
  single: Process object
.. 


:active: Active, boolean



.. index::
  single: active field
.. 




:model_id: Object, many2one



.. index::
  single: model_id field
.. 




:note: Notes, text



.. index::
  single: note field
.. 




:name: Name, char, required



.. index::
  single: name field
.. 




:node_ids: Nodes, one2many



.. index::
  single: node_ids field
.. 



Object: Process Nodes
#####################

.. index::
  single: Process Nodes object
.. 


:menu_id: Related Menu, many2one



.. index::
  single: menu_id field
.. 




:model_id: Object, many2one



.. index::
  single: model_id field
.. 




:kind: Kind of Node, selection, required



.. index::
  single: kind field
.. 




:name: Name, char, required



.. index::
  single: name field
.. 




:subflow_id: Subflow, many2one



.. index::
  single: subflow_id field
.. 




:condition_ids: Conditions, one2many



.. index::
  single: condition_ids field
.. 




:directory_id: Document directory, many2one



.. index::
  single: directory_id field
.. 




:note: Notes, text



.. index::
  single: note field
.. 




:process_id: Process, many2one, required



.. index::
  single: process_id field
.. 




:model_states: States Expression, char



.. index::
  single: model_states field
.. 




:transition_out: Ending Transitions, one2many



.. index::
  single: transition_out field
.. 




:help_url: Help URL, char



.. index::
  single: help_url field
.. 




:transition_in: Starting Transitions, one2many



.. index::
  single: transition_in field
.. 




:flow_start: Starting Flow, boolean



.. index::
  single: flow_start field
.. 



Object: Condition
#################

.. index::
  single: Condition object
.. 


:model_id: Object, many2one



.. index::
  single: model_id field
.. 




:node_id: Node, many2one, required



.. index::
  single: node_id field
.. 




:model_states: Expression, char, required



.. index::
  single: model_states field
.. 




:name: Name, char, required



.. index::
  single: name field
.. 



Object: Process Transitions
###########################

.. index::
  single: Process Transitions object
.. 


:role_ids: Roles, many2many



.. index::
  single: role_ids field
.. 




:transition_ids: Workflow Transitions, many2many



.. index::
  single: transition_ids field
.. 




:name: Name, char, required



.. index::
  single: name field
.. 




:note: Description, text



.. index::
  single: note field
.. 




:target_node_id: Target Node, many2one, required



.. index::
  single: target_node_id field
.. 




:source_node_id: Source Node, many2one, required



.. index::
  single: source_node_id field
.. 




:action_ids: Buttons, one2many



.. index::
  single: action_ids field
.. 



Object: Process Transitions Actions
###################################

.. index::
  single: Process Transitions Actions object
.. 


:action: Action ID, char



.. index::
  single: action field
.. 




:state: Type, selection, required



.. index::
  single: state field
.. 




:name: Name, char, required



.. index::
  single: name field
.. 




:transition_id: Transition, many2one, required



.. index::
  single: transition_id field
.. 

