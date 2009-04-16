
.. i18n: .. module:: board
.. i18n:     :synopsis: Dashboard main module (Official, Quality Certified)
.. i18n:     :noindex:
.. i18n: .. 

.. module:: board
    :synopsis: Dashboard main module (Official, Quality Certified)
    :noindex:
.. 

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. i18n: Dashboard main module (*board*)
.. i18n: ===============================
.. i18n: :Module: board
.. i18n: :Name: Dashboard main module
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: board
.. i18n: :Web: 
.. i18n: :Official module: yes
.. i18n: :Quality certified: yes

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

.. i18n: Description
.. i18n: -----------

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   Base module for all dashboards.

::

  Base module for all dashboards.

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

.. i18n:  * Dashboards
.. i18n:  * Dashboards/Publish a note
.. i18n:  * Dashboards/Configuration
.. i18n:  * Dashboards/Configuration/Dashboard Definition

 * Dashboards
 * Dashboards/Publish a note
 * Dashboards/Configuration
 * Dashboards/Configuration/Dashboard Definition

.. i18n: Views
.. i18n: -----

Views
-----

.. i18n:  * board.note.tree (tree)
.. i18n:  * board.note.form (form)
.. i18n:  * board.board.tree (tree)
.. i18n:  * board.board.form (form)

 * board.note.tree (tree)
 * board.note.form (form)
 * board.board.tree (tree)
 * board.board.form (form)

.. i18n: Objects
.. i18n: -------

Objects
-------

.. i18n: Object: board.board (board.board)
.. i18n: #################################

Object: board.board (board.board)
#################################

.. i18n: :line_ids: Action Views, one2many

:line_ids: Action Views, one2many

.. i18n: :view_id: Board View, many2one

:view_id: Board View, many2one

.. i18n: :name: Dashboard, char, required

:name: Dashboard, char, required

.. i18n: Object: board.board.line (board.board.line)
.. i18n: ###########################################

Object: board.board.line (board.board.line)
###########################################

.. i18n: :board_id: Dashboard, many2one, required

:board_id: Dashboard, many2one, required

.. i18n: :name: Title, char, required

:name: Title, char, required

.. i18n: :sequence: Sequence, integer

:sequence: Sequence, integer

.. i18n: :height: Height, integer

:height: Height, integer

.. i18n: :width: Width, integer

:width: Width, integer

.. i18n: :position: Position, selection, required

:position: Position, selection, required

.. i18n: :action_id: Action, many2one, required

:action_id: Action, many2one, required

.. i18n: Object: board.note.type (board.note.type)
.. i18n: #########################################

Object: board.note.type (board.note.type)
#########################################

.. i18n: :name: Note Type, char, required

:name: Note Type, char, required

.. i18n: Object: board.note (board.note)
.. i18n: ###############################

Object: board.note (board.note)
###############################

.. i18n: :note: Note, text

:note: Note, text

.. i18n: :date: Date, date, required

:date: Date, date, required

.. i18n: :user_id: Author, many2one

:user_id: Author, many2one

.. i18n: :name: Subject, char, required

:name: Subject, char, required

.. i18n: :type: Note type, selection

:type: Note type, selection
