
Module CCI Base Contact (*cci_base_contact*)
============================================
:Module: cci_base_contact
:Name: CCI Base Contact
:Version: 5.0.1.0
:Directory: cci_base_contact
:Web: http://www.openerp.com

Description
-----------

::

  specific module for cci project which will inherit
          base_contact module..

Dependencies
------------

 * base - installed
 * base_contact - installed
 * project - installed

Reports
-------

None


Menus
-------

 * Partners/Configuration/Link Type
 * Partners/Configuration/Link Type/Contact Link Type

Views
-----

 * res.partner.country.relation.tree (tree)
 * res.partner.country.relation.form (form)
 * \* INHERIT res.partner.contact.tree2 (tree)
 * \* INHERIT res.partner.contact.form (form)
 * \* INHERIT res.partner.contact.form (form)
 * \* INHERIT res.partner.contact.form (form)
 * \* INHERIT res.partner.contact.form (form)
 * res.partner.contact.link.type.tree (tree)
 * res.partner.contact.link.type.form (form)
 * \* INHERIT project.project.form.inherit (form)
 * \* INHERIT res.partner.job.form.inherit (form)


Objects
-------

Object: res.partner.contact.link.type
#####################################

.. index::
  single: res.partner.contact.link.type object
.. 


:name: Name, char, required



.. index::
  single: name field
.. 



Object: res.partner.contact.link
################################

.. index::
  single: res.partner.contact.link object
.. 


:current_contact_id: Current contact, many2one, required



.. index::
  single: current_contact_id field
.. 




:name: Name, char, required



.. index::
  single: name field
.. 




:contact_id: Contact, many2one, required



.. index::
  single: contact_id field
.. 




:type_id: Type, many2one, required



.. index::
  single: type_id field
.. 

