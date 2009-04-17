
.. module:: edi
    :synopsis: EDI 
    :noindex:
.. 

.. raw:: html

      <br />
    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. tip:: This module is part of the Open ERP software, the leading Open Source 
  enterprise management system. If you want to discover Open ERP, check our 
  `screencasts <href="http://openerp.tv>`_ or download 
  `Open ERP <href="http://openerp.com>`_ directly.

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/edi"></div>
    <script src="http://js-kit.com/ratings.js"></script>

EDI (*edi*)
===========
:Module: edi
:Name: EDI
:Version: 5.0.1.0
:Author: Tiny
:Directory: edi
:Web: 
:Official module: no
:Quality certified: no

Description
-----------

::

  Used for the communication with others proprietary ERP's. Has been tested in the food industries process, communicating with SAP. This module is able to import order and export delivery notes.

Download links
--------------

You can download this module as a zip file in the following version:

  * `trunk </download/modules/trunk/edi.zip>`_


Dependencies
------------

 * :mod:`sale`

Reports
-------

None


Menus
-------

 * Sales Management/Edi
 * Sales Management/Edi/View Logs

Views
-----

 * edi.log.line.tree (tree)
 * edi.log.tree (tree)
 * edi.log.form (form)
 * \* INHERIT sale.order.form.pvc (form)
 * \* INHERIT sale.order.line.form.pvc (form)


Objects
-------

Object: EDI log (edi.log)
#########################



:name: Log name, char, required





:log_line: Log Lines, one2many, readonly




Object: EDI Log Line (edi.log.line)
###################################



:sender: Partner, many2one, readonly





:log_id: Log Ref, many2one





:timestamp: Order date, char





:logdesc: Description, text





:order_num: Edi Order Id, char





:name: Name, char, required


