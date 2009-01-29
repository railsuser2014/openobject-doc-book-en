
EDI (*edi*)
===========
:Module: edi
:Name: EDI
:Version: 5.0.1.0
:Directory: edi
:Web: 

Description
-----------

::

  Used for the communication with others proprietary ERP's. Has been tested in the food industries process, communicating with SAP. This module is able to import order and export delivery notes.

Dependencies
------------

 * sale - installed

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

Object: EDI log
###############



:name: Log name, char, required





:log_line: Log Lines, one2many, readonly




Object: EDI Log Line
####################



:sender: Partner, many2one, readonly





:log_id: Log Ref, many2one





:timestamp: Order date, char





:logdesc: Description, text





:order_num: Edi Order Id, char





:name: Name, char, required


