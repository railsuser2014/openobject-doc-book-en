
Module CCI CRM (*cci_crm*)
==========================
:Module: cci_crm
:Name: CCI CRM
:Version: 5.0.1.0
:Directory: cci_crm
:Web: http://www.openerp.com

Description
-----------

::

  - define some groups with access rules
          - so using above rules , new object which will be confidential (can only be accessed by some users of group)

Dependencies
------------

 * base - installed
 * crm_configuration - installed
 * event - installed
 * cci_partner - installed

Reports
-------

None


Menus
-------

 * CRM & SRM/Meeting Confidential Info

Views
-----

 * \* INHERIT crm.case.form.confidential (form)
 * \* INHERIT crm.case.form.inherit (form)
 * \* INHERIT event.event.form.inherit (form)
 * meeting.confidential.info.form (form)
 * meeting.confidential.info.tree (tree)
 * meeting.confidential.info.form (form)
 * meeting.confidential.info.tree (tree)


Objects
-------

Object: Meeting Confidential Info
#################################

.. index::
  single: Meeting Confidential Info object
.. 


:group: Group, selection, required



.. index::
  single: group field
.. 




:name: Table, char



.. index::
  single: name field
.. 




:description: Description, text, required



.. index::
  single: description field
.. 

