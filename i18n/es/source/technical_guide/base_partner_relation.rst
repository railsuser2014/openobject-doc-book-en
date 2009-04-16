
.. i18n: .. module:: base_partner_relation
.. i18n:     :synopsis: Partners - relation extension 
.. i18n:     :noindex:
.. i18n: .. 

.. module:: base_partner_relation
    :synopsis: Partners - relation extension 
    :noindex:
.. 

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. i18n: Partners - relation extension (*base_partner_relation*)
.. i18n: =======================================================
.. i18n: :Module: base_partner_relation
.. i18n: :Name: Partners - relation extension
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: base_partner_relation
.. i18n: :Web: 
.. i18n: :Official module: no
.. i18n: :Quality certified: no

Partners - relation extension (*base_partner_relation*)
=======================================================
:Module: base_partner_relation
:Name: Partners - relation extension
:Version: 5.0.1.0
:Author: Tiny
:Directory: base_partner_relation
:Web: 
:Official module: no
:Quality certified: no

.. i18n: Description
.. i18n: -----------

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   Add a tab in the partner form to encode relations between several partners.
.. i18n:       For eg, the partner 'Toubib and Co.' has different contacts.
.. i18n:       When 'Toubib and Co.' orders, you have to deliver to 'Toubib - Belgium' and invoice to 
.. i18n:       'Toubib - Geneva'.

::

  Add a tab in the partner form to encode relations between several partners.
      For eg, the partner 'Toubib and Co.' has different contacts.
      When 'Toubib and Co.' orders, you have to deliver to 'Toubib - Belgium' and invoice to 
      'Toubib - Geneva'.

.. i18n: Dependencies
.. i18n: ------------

Dependencies
------------

.. i18n:  * :mod:`base`

 * :mod:`base`

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

.. i18n: None

None

.. i18n: Views
.. i18n: -----

Views
-----

.. i18n:  * res.partner.relation.form (form)
.. i18n:  * res.partner.relation.tree (tree)
.. i18n:  * \* INHERIT res.partner.form.inherit (form)

 * res.partner.relation.form (form)
 * res.partner.relation.tree (tree)
 * \* INHERIT res.partner.form.inherit (form)

.. i18n: Objects
.. i18n: -------

Objects
-------

.. i18n: Object: Partner Relation (res.partner.relation)
.. i18n: ###############################################

Object: Partner Relation (res.partner.relation)
###############################################

.. i18n: :percent: Ownership, float

:percent: Ownership, float

.. i18n: :current_partner_id: Partner, many2one, required

:current_partner_id: Partner, many2one, required

.. i18n: :partner_id: Partner, many2one, required

:partner_id: Partner, many2one, required

.. i18n: :description: Description, text

:description: Description, text

.. i18n: :type_id: Type, many2one, required

:type_id: Type, many2one, required
