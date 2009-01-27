
Module Base Contact (*base_contact*)
====================================
:Module: base_contact
:Name: Base Contact
:Version: 5.0.1.0
:Directory: base_contact
:Web: http://www.openerp.com

Description
-----------

::

  This module allows you to manage entirely your contacts.
  
      It lets you define
          *contacts unrelated to a partner,
          *contacts working at several addresses (possibly for different partners),
          *contacts with possibly different functions for each of its job's addresses
  
      It also add new menu items located in
          Partners \ Contacts
          Partners \ Functions
  
      Pay attention that this module converts the existing addresses into "addresses + contacts". It means that some fields of the addresses will be missing (like the contact name), since these are supposed to be defined in an other object.

Dependencies
------------

 * base - installed
 * process - installed

Reports
-------

None


Menus
-------

 * Partners/Contacts
 * Partners/Contact's Jobs

Views
-----

 * res.partner.contact.tree (tree)
 * res.partner.contact.form (form)
 * \* INHERIT Partner form inherited (form)
 * \* INHERIT res.partner.form (form)
 * \* INHERIT res.partner.form (form)
 * \* INHERIT res.partner.form (form)
 * \* INHERIT Partner addresses inherited (tree)
 * \* INHERIT res.partner.address.form.inherited0 (form)
 * \* INHERIT res.partner.address.form.inherited1 (form)
 * \* INHERIT res.partner.address.form.inherited2 (form)
 * \* INHERIT res.partner.address.form.inherited3 (form)
 * \* INHERIT res.partner.address.form.inherited4 (form)
 * \* INHERIT res.partner.address.form.inherited6 (form)
 * \* INHERIT res.partner.address.form.inherited5 (form)
 * res.partner.job.tree (tree)
 * res.partner.job.form (form)


Objects
-------

Object: res.partner.contact
###########################

.. index::
  single: res.partner.contact object
.. 


:origin: Origin, char

    *The DB from which the info is coming from*

.. index::
  single: origin field
.. 




:fse_work_status: FSE Work Status, char



.. index::
  single: fse_work_status field
.. 




:canal_id: Favourite Channel, many2one



.. index::
  single: canal_id field
.. 




:data_private: Private data, boolean



.. index::
  single: data_private field
.. 




:self_sufficent: Keep contact, boolean

    *This contact will not be removed even if all his addresses are deleted*

.. index::
  single: self_sufficent field
.. 




:partner_id: Main Employer, many2one



.. index::
  single: partner_id field
.. 




:first_name: First Name, char



.. index::
  single: first_name field
.. 




:title: Title, selection



.. index::
  single: title field
.. 




:country_id: Nationality, many2one



.. index::
  single: country_id field
.. 




:who_presence: In WsW, boolean



.. index::
  single: who_presence field
.. 




:lang_id: Language, many2one



.. index::
  single: lang_id field
.. 




:who_date_publication: Publication, date



.. index::
  single: who_date_publication field
.. 




:fse_work_experience: FSE Work Exp., char



.. index::
  single: fse_work_experience field
.. 




:magazine_subscription: Magazine subscription, selection



.. index::
  single: magazine_subscription field
.. 




:country_ids: Expertize's Countries, many2many



.. index::
  single: country_ids field
.. 




:website: Website, char



.. index::
  single: website field
.. 




:old_id: Old Datman ID, integer



.. index::
  single: old_id field
.. 




:fse_studies: FSE Studies, char



.. index::
  single: fse_studies field
.. 




:who_description: WsW Description, text



.. index::
  single: who_description field
.. 




:active: Active, boolean



.. index::
  single: active field
.. 




:answers_ids: Answers, many2many



.. index::
  single: answers_ids field
.. 




:function_id: Main Job, many2one



.. index::
  single: function_id field
.. 




:job_ids: Functions and Addresses, one2many



.. index::
  single: job_ids field
.. 




:link_ids: Contact Link, one2many



.. index::
  single: link_ids field
.. 




:name: Last Name, char, required



.. index::
  single: name field
.. 




:magazine_subscription_source: Mag. Subscription Source, char



.. index::
  single: magazine_subscription_source field
.. 




:mobile: Mobile, char



.. index::
  single: mobile field
.. 




:who_date_accept: Accept Date, date



.. index::
  single: who_date_accept field
.. 




:birthdate: Birth Date, date



.. index::
  single: birthdate field
.. 




:who_date_last: Last Modification, date



.. index::
  single: who_date_last field
.. 




:national_number: National Number, char



.. index::
  single: national_number field
.. 




:article_ids: Articles, many2many



.. index::
  single: article_ids field
.. 



Object: Contact Partner Function
################################

.. index::
  single: Contact Partner Function object
.. 


:date_stop: Date Stop, date



.. index::
  single: date_stop field
.. 




:dir_presence: In Directory, boolean



.. index::
  single: dir_presence field
.. 




:canal_id: Canal, many2one

    *favorite chanel for communication*

.. index::
  single: canal_id field
.. 




:date_end: Date end, date



.. index::
  single: date_end field
.. 




:address_id: Address, many2one



.. index::
  single: address_id field
.. 




:contact_id: Contact, many2one, required



.. index::
  single: contact_id field
.. 




:function_label: Function Label, char, required



.. index::
  single: function_label field
.. 




:team_id: Team, many2one



.. index::
  single: team_id field
.. 




:password: Password, char



.. index::
  single: password field
.. 




:date_start: Date start, date



.. index::
  single: date_start field
.. 




:who_presence: In Whos Who, boolean



.. index::
  single: who_presence field
.. 




:state: State, selection, required



.. index::
  single: state field
.. 




:department: Department, char



.. index::
  single: department field
.. 




:email: E-Mail, char



.. index::
  single: email field
.. 




:phone: Phone, char



.. index::
  single: phone field
.. 




:active: Active, boolean



.. index::
  single: active field
.. 




:answers_ids: Answers, many2many



.. index::
  single: answers_ids field
.. 




:function_id: Partner Function, many2one



.. index::
  single: function_id field
.. 




:sequence_partner: Partner Seq., integer

    *Order of importance of this job title in the list of job title of the linked partner*

.. index::
  single: sequence_partner field
.. 




:sequence_contact: Contact Seq., integer

    *Order of importance of this address in the list of addresses of the linked contact*

.. index::
  single: sequence_contact field
.. 




:name: Partner, many2one



.. index::
  single: name field
.. 




:function_code_label: Codes, char



.. index::
  single: function_code_label field
.. 




:token: Token, char



.. index::
  single: token field
.. 




:login_name: Login Name, char



.. index::
  single: login_name field
.. 

