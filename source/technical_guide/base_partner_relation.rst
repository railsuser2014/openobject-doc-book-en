
.. module:: base_partner_relation
    :synopsis: Partners - relation extension 
    :noindex:
.. 

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

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

Description
-----------

::

  Add a tab in the partner form to encode relations between several partners.
      For eg, the partner 'Toubib and Co.' has different contacts.
      When 'Toubib and Co.' orders, you have to deliver to 'Toubib - Belgium'
      and invoice to 'Toubib - Geneva'.

Dependencies
------------

 * :mod:`base`

Reports
-------

None


Menus
-------


None


Views
-----

 * res.partner.relation.form (form)
 * res.partner.relation.tree (tree)
 * \* INHERIT res.partner.form.inherit (form)


Objects
-------

Object: Partner Relation (res.partner.relation)
###############################################



:percent: Ownership, float





:current_partner_id: Partner, many2one, required





:partner_id: Partner, many2one, required





:description: Description, text





:type_id: Type, many2one, required


