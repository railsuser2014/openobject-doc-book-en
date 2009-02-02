
.. module:: cci_crm
    :synopsis: CCI CRM
    :noindex:
.. 

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

CCI CRM (*cci_crm*)
===================
:Module: cci_crm
:Name: CCI CRM
:Version: 5.0.1.0
:Directory: cci_crm
:Web: http://www.openerp.com
:Is certified: no

Description
-----------

::

  - define some groups with access rules
          - so using above rules , new object which will be confidential (can only be accessed by some users of group)

Dependencies
------------

 * :mod:`base`
 * :mod:`crm_configuration`
 * :mod:`event`
 * :mod:`cci_partner`

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

Object: Meeting Confidential Info (meeting.confidential.info)
#############################################################



:group: Group, selection, required





:name: Table, char





:description: Description, text, required


