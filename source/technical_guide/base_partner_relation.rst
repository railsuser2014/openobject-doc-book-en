
Module Partners - relation extension (*base_partner_relation*)
==============================================================
:Module: base_partner_relation
:Name: Partners - relation extension
:Version: 5.0.1.0
:Directory: base_partner_relation
:Web: 

Description
-----------

::

  Add a tab in the partner form to encode relations between several partners.
      For eg, the partner 'Toubib and Co.' has different contacts.
      When 'Toubib and Co.' orders, you have to deliver to 'Toubib - Belgium'
      and invoice to 'Toubib - Geneva'.

Dependencies
------------

 * base - installed

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

Object: Partner Relation
########################

.. index::
  single: Partner Relation object
.. 


:percent: Ownership, float



.. index::
  single: percent field
.. 




:current_partner_id: Partner, many2one, required



.. index::
  single: current_partner_id field
.. 




:partner_id: Partner, many2one, required



.. index::
  single: partner_id field
.. 




:description: Description, text



.. index::
  single: description field
.. 




:type_id: Type, many2one, required



.. index::
  single: type_id field
.. 

