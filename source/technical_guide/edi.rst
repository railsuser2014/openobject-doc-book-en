
Module EDI (*edi*)
==================
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

.. index::
  single: EDI log object
.. 


:name: Log name, char, required



.. index::
  single: name field
.. 




:log_line: Log Lines, one2many, readonly



.. index::
  single: log_line field
.. 



Object: EDI Log Line
####################

.. index::
  single: EDI Log Line object
.. 


:sender: Partner, many2one, readonly



.. index::
  single: sender field
.. 




:log_id: Log Ref, many2one



.. index::
  single: log_id field
.. 




:timestamp: Order date, char



.. index::
  single: timestamp field
.. 




:logdesc: Description, text



.. index::
  single: logdesc field
.. 




:order_num: Edi Order Id, char



.. index::
  single: order_num field
.. 




:name: Name, char, required



.. index::
  single: name field
.. 

