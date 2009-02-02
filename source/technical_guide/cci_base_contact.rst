
.. module:: cci_base_contact
    :synopsis: CCI Base Contact
    :noindex:
.. 

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

CCI Base Contact (*cci_base_contact*)
=====================================
:Module: cci_base_contact
:Name: CCI Base Contact
:Version: 5.0.1.0
:Directory: cci_base_contact
:Web: http://www.openerp.com
:Is certified: no

Description
-----------

::

  specific module for cci project which will inherit
          base_contact module..

Dependencies
------------

 * :mod:`base`
 * :mod:`base_contact`
 * :mod:`project`

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

Object: res.partner.contact.link.type (res.partner.contact.link.type)
#####################################################################



:name: Name, char, required




Object: res.partner.contact.link (res.partner.contact.link)
###########################################################



:current_contact_id: Current contact, many2one, required





:name: Name, char, required





:contact_id: Contact, many2one, required





:type_id: Type, many2one, required


