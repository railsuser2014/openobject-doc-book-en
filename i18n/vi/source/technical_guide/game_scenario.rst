
.. i18n: .. module:: game_scenario
.. i18n:     :synopsis: Scenario of games 
.. i18n:     :noindex:
.. i18n: .. 

.. module:: game_scenario
    :synopsis: Scenario of games 
    :noindex:
.. 

.. i18n: .. raw:: html
.. i18n: 
.. i18n:       <br />
.. i18n:     <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. raw:: html

      <br />
    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. i18n: .. tip:: This module is part of the Open ERP software, the leading Open Source 
.. i18n:   enterprise management system. If you want to discover Open ERP, check our 
.. i18n:   `screencasts <http://openerp.tv>`_ or download 
.. i18n:   `Open ERP <http://openerp.com>`_ directly.

.. tip:: This module is part of the Open ERP software, the leading Open Source 
  enterprise management system. If you want to discover Open ERP, check our 
  `screencasts <http://openerp.tv>`_ or download 
  `Open ERP <http://openerp.com>`_ directly.

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/game_scenario"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/game_scenario"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Scenario of games (*game_scenario*)
.. i18n: ===================================
.. i18n: :Module: game_scenario
.. i18n: :Name: Scenario of games
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: game_scenario
.. i18n: :Web: 
.. i18n: :Official module: no
.. i18n: :Quality certified: no

Scenario of games (*game_scenario*)
===================================
:Module: game_scenario
:Name: Scenario of games
:Version: 5.0.1.0
:Author: Tiny
:Directory: game_scenario
:Web: 
:Official module: no
:Quality certified: no

.. i18n: Description
.. i18n: -----------

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   Allows to check the scenario of games

::

  Allows to check the scenario of games

.. i18n: Download links
.. i18n: --------------

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:

You can download this module as a zip file in the following version:

.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/game_scenario.zip>`_

  * `trunk <http://www.openerp.com/download/modules/trunk/game_scenario.zip>`_

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

.. i18n:  * Administration/Game Scenario
.. i18n:  * Administration/Game Scenario/Configuration
.. i18n:  * Administration/Game Scenario/Configuration/Scenario Steps
.. i18n:  * Administration/Game Scenario/Configuration/Scenario

 * Administration/Game Scenario
 * Administration/Game Scenario/Configuration
 * Administration/Game Scenario/Configuration/Scenario Steps
 * Administration/Game Scenario/Configuration/Scenario

.. i18n: Views
.. i18n: -----

Views
-----

.. i18n:  * game.scenario.step.tree (tree)
.. i18n:  * game.scenario.step.form (form)
.. i18n:  * game.scenario.tree (tree)
.. i18n:  * game.scenario.form (form)

 * game.scenario.step.tree (tree)
 * game.scenario.step.form (form)
 * game.scenario.tree (tree)
 * game.scenario.form (form)

.. i18n: Objects
.. i18n: -------

Objects
-------

.. i18n: Object: game.scenario (game.scenario)
.. i18n: #####################################

Object: game.scenario (game.scenario)
#####################################

.. i18n: :note: Note, text

:note: Note, text

.. i18n: :state: State, selection, required

:state: State, selection, required

.. i18n: :name: Name, char, required

:name: Name, char, required

.. i18n: Object: game.scenario.step (game.scenario.step)
.. i18n: ###############################################

Object: game.scenario.step (game.scenario.step)
###############################################

.. i18n: :menu_id: Menu, many2one, required

:menu_id: Menu, many2one, required

.. i18n: :post_process_object: Postprocess Object, char

:post_process_object: Postprocess Object, char

.. i18n: :name: Name, char, required

:name: Name, char, required

.. i18n: :pre_process_method: Preprocess Method, char

:pre_process_method: Preprocess Method, char

.. i18n: :description: Description, text

:description: Description, text

.. i18n: :post_process_method: Postprocess Method, char

:post_process_method: Postprocess Method, char

.. i18n: :tip: Tip, text

:tip: Tip, text

.. i18n: :scenario_id: Scenario, many2one, required

:scenario_id: Scenario, many2one, required

.. i18n: :state: State, selection, required

:state: State, selection, required

.. i18n: :error: Error, text

:error: Error, text

.. i18n: :step_next_ids: Next Steps, many2many

:step_next_ids: Next Steps, many2many

.. i18n: :pre_process_object: Preprocess Object, char

:pre_process_object: Preprocess Object, char
