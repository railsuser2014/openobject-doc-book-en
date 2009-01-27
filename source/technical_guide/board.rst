
Module Dashboard main module (*board*)
======================================
:Module: board
:Name: Dashboard main module
:Version: 5.0.1.0
:Directory: board
:Web: 

Description
-----------

::

  Base module for all dashboards.

Dependencies
------------

 * base - installed

Reports
-------

None


Menus
-------

 * Dashboards
 * Dashboards/Publish a note
 * Dashboards/Configuration
 * Dashboards/Configuration/Dashboard Definition

Views
-----

 * board.note.tree (tree)
 * board.note.form (form)
 * board.board.tree (tree)
 * board.board.form (form)


Objects
-------

Object: board.board
###################

.. index::
  single: board.board object
.. 


:line_ids: Action Views, one2many



.. index::
  single: line_ids field
.. 




:view_id: Board View, many2one



.. index::
  single: view_id field
.. 




:name: Dashboard, char, required



.. index::
  single: name field
.. 



Object: board.board.line
########################

.. index::
  single: board.board.line object
.. 


:board_id: Dashboard, many2one, required



.. index::
  single: board_id field
.. 




:name: Title, char, required



.. index::
  single: name field
.. 




:sequence: Sequence, integer



.. index::
  single: sequence field
.. 




:height: Height, integer



.. index::
  single: height field
.. 




:width: Width, integer



.. index::
  single: width field
.. 




:position: Position, selection, required



.. index::
  single: position field
.. 




:action_id: Action, many2one, required



.. index::
  single: action_id field
.. 



Object: board.note.type
#######################

.. index::
  single: board.note.type object
.. 


:name: Note Type, char, required



.. index::
  single: name field
.. 



Object: board.note
##################

.. index::
  single: board.note object
.. 


:note: Note, text



.. index::
  single: note field
.. 




:date: Date, date, required



.. index::
  single: date field
.. 




:user_id: Author, many2one



.. index::
  single: user_id field
.. 




:name: Subject, char, required



.. index::
  single: name field
.. 




:type: Note type, selection



.. index::
  single: type field
.. 

