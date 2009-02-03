
.. module:: base_report_model
    :synopsis: Base Report Model 
    :noindex:
.. 

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

    <style>
      div.body p#module-base_report_model {
        display: none;
      }
    </style>

Base Report Model (*base_report_model*)
=======================================
:Module: base_report_model
:Name: Base Report Model
:Version: 5.0.0.1
:Author: Tiny
:Directory: base_report_model
:Web: http://openerp.com
:Is certified: no

Description
-----------

::

  This module allows you to specify the models which can have an attachment from OpenOffice Report

Dependencies
------------

 * :mod:`base`

Reports
-------

None


Menus
-------

 * Administration/Low Level Objects/Base
 * Administration/Low Level Objects/Base/OpenOffice Attachment Available Models

Views
-----

 * base.report.model.view.form (form)
 * base.report.model.view.tree (tree)


Objects
-------

Object: Visible models for a tool (base.report.model)
#####################################################



:model_id: Model, many2one, required





:name: Visible Name, char, required


