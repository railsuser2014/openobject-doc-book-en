
.. module:: use_control
    :synopsis: On Demand Open Object - Subscription Control 
    :noindex:
.. 

.. tip:: This module is part of the Open ERP software, the leading Open Source 
  enterprise management system. If you want to discover Open ERP, check our 
  `screencasts <href="http://openerp.tv>`_ or download 
  `Open ERP <href="http://openerp.com>`_ directly.

.. raw:: html

      <br />
    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

On Demand Open Object - Subscription Control (*use_control*)
============================================================
:Module: use_control
:Name: On Demand Open Object - Subscription Control
:Version: 5.0.1.0
:Author: Tiny
:Directory: use_control
:Web: http://www.openerp.com
:Official module: no
:Quality certified: no

Description
-----------

::

  This module provides reports to control your on demand subscription.
  You can not uninstall or delete it.

Download links
--------------

You can download this module as a zip file in the following version:

  * `trunk </download/modules/trunk/use_control.zip>`_


Dependencies
------------

 * :mod:`base`

Reports
-------

None


Menus
-------

 * Administration/On Demand Control
 * Administration/On Demand Control/Hours per User
 * Administration/On Demand Control/Hours per Month

Views
-----

 * use.control.time.month.user.graph (graph)
 * use.control.time.month.user.form (form)
 * use.control.time.month.user.tree (tree)
 * use.control.time.month.graph (graph)
 * use.control.time.month.tree (tree)


Objects
-------

Object: use.control.time (use.control.time)
###########################################



:date: Date, datetime





:duration: Duration, float





:user_id: User, many2one





:uploaded: Uploaded, boolean




Object: Time of Use per Month (use.control.time.month.user)
###########################################################



:date: Month, date





:duration: Duration, float





:user_id: User, many2one




Object: Time of Use per Month (use.control.time.month)
######################################################



:date: Month, date





:duration: Duration, float




Object: Containt the blocking message (use.control.db.block)
############################################################



:name: Block message, text


