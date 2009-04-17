
.. module:: board
    :synopsis: Dashboard main module (Official, Quality Certified)
    :noindex:
.. 

.. raw:: html

      <br />
    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. tip:: This module is part of the Open ERP software, the leading Open Source 
  enterprise management system. If you want to discover Open ERP, check our 
  `screencasts <href="http://openerp.tv>`_ or download 
  `Open ERP <href="http://openerp.com>`_ directly.

Dashboard main module (*board*)
===============================
:Module: board
:Name: Dashboard main module
:Version: 5.0.1.0
:Author: Tiny
:Directory: board
:Web: 
:Official module: yes
:Quality certified: yes

Description
-----------

::

  Base module for all dashboards.

Download links
--------------

You can download this module as a zip file in the following version:

  * `4.2 </download/modules/4.2/board.zip>`_
  * `5.0 </download/modules/5.0/board.zip>`_
  * `trunk </download/modules/trunk/board.zip>`_


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


