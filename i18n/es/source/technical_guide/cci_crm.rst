
.. i18n: .. module:: cci_crm
.. i18n:     :synopsis: CCI CRM 
.. i18n:     :noindex:
.. i18n: .. 

.. module:: cci_crm
    :synopsis: CCI CRM 
    :noindex:
.. 

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. i18n: CCI CRM (*cci_crm*)
.. i18n: ===================
.. i18n: :Module: cci_crm
.. i18n: :Name: CCI CRM
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: cci_crm
.. i18n: :Web: http://www.openerp.com
.. i18n: :Official module: no
.. i18n: :Quality certified: no

CCI CRM (*cci_crm*)
===================
:Module: cci_crm
:Name: CCI CRM
:Version: 5.0.1.0
:Author: Tiny
:Directory: cci_crm
:Web: http://www.openerp.com
:Official module: no
:Quality certified: no

.. i18n: Description
.. i18n: -----------

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   - define some groups with access rules
.. i18n:           - so using above rules , new object which will be confidential 
.. i18n:             (can only be accessed by some users of group)

::

  - define some groups with access rules
          - so using above rules , new object which will be confidential 
            (can only be accessed by some users of group)

.. i18n: Dependencies
.. i18n: ------------

Dependencies
------------

.. i18n:  * :mod:`base`
.. i18n:  * :mod:`crm_configuration`
.. i18n:  * :mod:`event`
.. i18n:  * :mod:`cci_partner`

 * :mod:`base`
 * :mod:`crm_configuration`
 * :mod:`event`
 * :mod:`cci_partner`

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

.. i18n:  * CRM & SRM/Meeting Confidential Info

 * CRM & SRM/Meeting Confidential Info

.. i18n: Views
.. i18n: -----

Views
-----

.. i18n:  * \* INHERIT crm.case.form.confidential (form)
.. i18n:  * \* INHERIT crm.case.form.inherit (form)
.. i18n:  * \* INHERIT event.event.form.inherit (form)
.. i18n:  * meeting.confidential.info.form (form)
.. i18n:  * meeting.confidential.info.tree (tree)
.. i18n:  * meeting.confidential.info.form (form)
.. i18n:  * meeting.confidential.info.tree (tree)

 * \* INHERIT crm.case.form.confidential (form)
 * \* INHERIT crm.case.form.inherit (form)
 * \* INHERIT event.event.form.inherit (form)
 * meeting.confidential.info.form (form)
 * meeting.confidential.info.tree (tree)
 * meeting.confidential.info.form (form)
 * meeting.confidential.info.tree (tree)

.. i18n: Objects
.. i18n: -------

Objects
-------

.. i18n: Object: Meeting Confidential Info (meeting.confidential.info)
.. i18n: #############################################################

Object: Meeting Confidential Info (meeting.confidential.info)
#############################################################

.. i18n: :group: Group, selection, required

:group: Group, selection, required

.. i18n: :name: Table, char

:name: Table, char

.. i18n: :description: Description, text, required

:description: Description, text, required
