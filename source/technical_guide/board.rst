
.. module:: board
    :synopsis: Dashboard main module (Quality Certified)
    :noindex:
.. 

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

    <style>
      div.body p#module-board {
        display: none;
      }
    </style>

Dashboard main module (*board*)
===============================
:Module: board
:Name: Dashboard main module
:Version: 5.0.1.0
:Author: Tiny
:Directory: board
:Web: 
:Is certified: yes

Description
-----------

::

  Base module for all dashboards.

Dependencies
------------

 * :mod:`base`

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

Object: board.board (board.board)
#################################



:line_ids: Action Views, one2many





:view_id: Board View, many2one





:name: Dashboard, char, required




Object: board.board.line (board.board.line)
###########################################



:board_id: Dashboard, many2one, required





:name: Title, char, required





:sequence: Sequence, integer





:height: Height, integer





:width: Width, integer





:position: Position, selection, required





:action_id: Action, many2one, required




Object: board.note.type (board.note.type)
#########################################



:name: Note Type, char, required




Object: board.note (board.note)
###############################



:note: Note, text





:date: Date, date, required





:user_id: Author, many2one





:name: Subject, char, required





:type: Note type, selection


