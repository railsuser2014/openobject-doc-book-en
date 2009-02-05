
.. module:: board_project
    :synopsis: Board for project users (Official, Quality Certified)
    :noindex:
.. 

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

Board for project users (*board_project*)
=========================================
:Module: board_project
:Name: Board for project users
:Version: 5.0.1.0
:Author: Tiny
:Directory: board_project
:Web: 
:Official module: yes
:Quality certified: yes

Description
-----------

::

  This module implements a dashboard for project member that includes:
      * List of my open tasks
      * List of my next deadlines
      * List of public notes
      * Graph of my timesheet
      * Graph of my work analysis

Dependencies
------------

 * :mod:`project`
 * :mod:`report_timesheet`
 * :mod:`board`
 * :mod:`report_analytic_planning`
 * :mod:`report_analytic_line`
 * :mod:`report_task`
 * :mod:`hr_timesheet_sheet`

Reports
-------

None


Menus
-------

 * Dashboards/Project
 * Dashboards/Project/Project Dashboard
 * Dashboards/Project/Project Manager Dashboard

Views
-----

 * project.task.tree (tree)
 * board.project.form (form)
 * hr.timesheet.sheet.tree.simplified.board (tree)
 * board.project.manager.form (form)


Objects
-------

None
