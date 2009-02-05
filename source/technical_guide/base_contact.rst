
.. module:: base_contact
    :synopsis: Base Contact (Official, Quality Certified)
    :noindex:
.. 

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

Base Contact (*base_contact*)
=============================
:Module: base_contact
:Name: Base Contact
:Version: 5.0.1.0
:Author: Tiny
:Directory: base_contact
:Web: http://www.openerp.com
:Official module: yes
:Quality certified: yes

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

 * :mod:`base`
 * :mod:`process`

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

Object: res.partner.contact (res.partner.contact)
#################################################



:origin: Origin, char

    *The DB from which the info is coming from*



:fse_work_status: FSE Work Status, char





:canal_id: Favourite Channel, many2one





:data_private: Private data, boolean





:self_sufficent: Keep contact, boolean

    *This contact will not be removed even if all his addresses are deleted*



:partner_id: Main Employer, many2one





:first_name: First Name, char





:title: Title, selection





:country_id: Nationality, many2one





:who_presence: In WsW, boolean





:lang_id: Language, many2one





:who_date_publication: Publication, date





:fse_work_experience: FSE Work Exp., char





:magazine_subscription: Magazine subscription, selection





:country_ids: Expertize's Countries, many2many





:website: Website, char





:old_id: Old Datman ID, integer





:fse_studies: FSE Studies, char





:who_description: WsW Description, text





:active: Active, boolean





:answers_ids: Answers, many2many





:function_id: Main Job, many2one





:job_ids: Functions and Addresses, one2many





:link_ids: Contact Link, one2many





:name: Last Name, char, required





:magazine_subscription_source: Mag. Subscription Source, char





:mobile: Mobile, char





:who_date_accept: Accept Date, date





:birthdate: Birth Date, date





:who_date_last: Last Modification, date





:national_number: National Number, char





:article_ids: Articles, many2many




Object: Contact Partner Function (res.partner.job)
##################################################



:date_stop: Date Stop, date





:dir_presence: In Directory, boolean





:canal_id: Canal, many2one

    *favorite chanel for communication*



:date_end: Date end, date





:address_id: Address, many2one





:contact_id: Contact, many2one, required





:function_label: Function Label, char, required





:team_id: Team, many2one





:password: Password, char





:date_start: Date start, date





:who_presence: In Whos Who, boolean





:state: State, selection, required





:department: Department, char





:email: E-Mail, char





:phone: Phone, char





:active: Active, boolean





:answers_ids: Answers, many2many





:function_id: Partner Function, many2one





:sequence_partner: Partner Seq., integer

    *Order of importance of this job title in the list of job title of the linked partner*



:sequence_contact: Contact Seq., integer

    *Order of importance of this address in the list of addresses of the linked contact*



:name: Partner, many2one





:function_code_label: Codes, char





:token: Token, char





:login_name: Login Name, char


