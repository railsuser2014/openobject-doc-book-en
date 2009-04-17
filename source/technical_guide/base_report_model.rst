
.. module:: base_report_model
    :synopsis: Base Report Model 
    :noindex:
.. 

.. tip:: This module is part of the Open ERP software, the leading Open Source 
  enterprise management system. If you want to discover Open ERP, check our 
  `screencasts <href="http://openerp.tv>`_ or download 
  `Open ERP <href="http://openerp.com>`_ directly.

.. raw:: html

      <br />
    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

Base Report Model (*base_report_model*)
=======================================
:Module: base_report_model
:Name: Base Report Model
:Version: 5.0.0.1
:Author: Tiny
:Directory: base_report_model
:Web: http://www.openerp.com
:Official module: no
:Quality certified: no

Description
-----------

::

  This module allows you to specify the models which can have an attachment from OpenOffice Report

Download links
--------------

You can download this module as a zip file in the following version:

  * `trunk </download/modules/trunk/base_report_model.zip>`_


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


