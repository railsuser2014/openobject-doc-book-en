
.. i18n: .. module:: base_contact
.. i18n:     :synopsis: Base Contact (Official, Quality Certified)
.. i18n:     :noindex:
.. i18n: .. 

.. module:: base_contact
    :synopsis: Base Contact (Official, Quality Certified)
    :noindex:
.. 

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. i18n: Base Contact (*base_contact*)
.. i18n: =============================
.. i18n: :Module: base_contact
.. i18n: :Name: Base Contact
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: base_contact
.. i18n: :Web: http://www.openerp.com
.. i18n: :Official module: yes
.. i18n: :Quality certified: yes

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

.. i18n: Description
.. i18n: -----------

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   This module allows you to manage entirely your contacts.
.. i18n:   
.. i18n:       It lets you define
.. i18n:           *contacts unrelated to a partner,
.. i18n:           *contacts working at several addresses (possibly for different partners),
.. i18n:           *contacts with possibly different functions for each of its job's addresses
.. i18n:   
.. i18n:       It also add new menu items located in
.. i18n:           Partners \ Contacts
.. i18n:           Partners \ Functions
.. i18n:   
.. i18n:       Pay attention that this module converts the existing addresses into "addresses + contacts".
.. i18n:  It means that some fields of the addresses will be missing (like the contact name), since 
.. i18n: these are supposed to be defined in an other object.

::

  This module allows you to manage entirely your contacts.
  
      It lets you define
          *contacts unrelated to a partner,
          *contacts working at several addresses (possibly for different partners),
          *contacts with possibly different functions for each of its job's addresses
  
      It also add new menu items located in
          Partners \ Contacts
          Partners \ Functions
  
      Pay attention that this module converts the existing addresses into "addresses + contacts".
 It means that some fields of the addresses will be missing (like the contact name), since 
these are supposed to be defined in an other object.

.. i18n: Dependencies
.. i18n: ------------

Dependencies
------------

.. i18n:  * :mod:`base`
.. i18n:  * :mod:`process`

 * :mod:`base`
 * :mod:`process`

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

.. i18n:  * Partners/Contacts
.. i18n:  * Partners/Contact's Jobs

 * Partners/Contacts
 * Partners/Contact's Jobs

.. i18n: Views
.. i18n: -----

Views
-----

.. i18n:  * res.partner.contact.tree (tree)
.. i18n:  * res.partner.contact.form (form)
.. i18n:  * \* INHERIT Partner form inherited (form)
.. i18n:  * \* INHERIT res.partner.form (form)
.. i18n:  * \* INHERIT res.partner.form (form)
.. i18n:  * \* INHERIT res.partner.form (form)
.. i18n:  * \* INHERIT Partner addresses inherited (tree)
.. i18n:  * \* INHERIT res.partner.address.form.inherited0 (form)
.. i18n:  * \* INHERIT res.partner.address.form.inherited1 (form)
.. i18n:  * \* INHERIT res.partner.address.form.inherited2 (form)
.. i18n:  * \* INHERIT res.partner.address.form.inherited3 (form)
.. i18n:  * \* INHERIT res.partner.address.form.inherited4 (form)
.. i18n:  * \* INHERIT res.partner.address.form.inherited6 (form)
.. i18n:  * \* INHERIT res.partner.address.form.inherited5 (form)
.. i18n:  * res.partner.job.tree (tree)
.. i18n:  * res.partner.job.form (form)

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

.. i18n: Objects
.. i18n: -------

Objects
-------

.. i18n: Object: res.partner.contact (res.partner.contact)
.. i18n: #################################################

Object: res.partner.contact (res.partner.contact)
#################################################

.. i18n: :origin: Origin, char

:origin: Origin, char

.. i18n:     *The DB from which the info is coming from*

    *The DB from which the info is coming from*

.. i18n: :fse_work_status: FSE Work Status, char

:fse_work_status: FSE Work Status, char

.. i18n: :canal_id: Favourite Channel, many2one

:canal_id: Favourite Channel, many2one

.. i18n: :data_private: Private data, boolean

:data_private: Private data, boolean

.. i18n: :self_sufficent: Keep contact, boolean

:self_sufficent: Keep contact, boolean

.. i18n:     *This contact will not be removed even if all his addresses are deleted*

    *This contact will not be removed even if all his addresses are deleted*

.. i18n: :partner_id: Main Employer, many2one

:partner_id: Main Employer, many2one

.. i18n: :first_name: First Name, char

:first_name: First Name, char

.. i18n: :title: Title, selection

:title: Title, selection

.. i18n: :country_id: Nationality, many2one

:country_id: Nationality, many2one

.. i18n: :who_presence: In WsW, boolean

:who_presence: In WsW, boolean

.. i18n: :lang_id: Language, many2one

:lang_id: Language, many2one

.. i18n: :who_date_publication: Publication, date

:who_date_publication: Publication, date

.. i18n: :fse_work_experience: FSE Work Exp., char

:fse_work_experience: FSE Work Exp., char

.. i18n: :magazine_subscription: Magazine subscription, selection

:magazine_subscription: Magazine subscription, selection

.. i18n: :country_ids: Expertize's Countries, many2many

:country_ids: Expertize's Countries, many2many

.. i18n: :website: Website, char

:website: Website, char

.. i18n: :old_id: Old Datman ID, integer

:old_id: Old Datman ID, integer

.. i18n: :fse_studies: FSE Studies, char

:fse_studies: FSE Studies, char

.. i18n: :who_description: WsW Description, text

:who_description: WsW Description, text

.. i18n: :active: Active, boolean

:active: Active, boolean

.. i18n: :answers_ids: Answers, many2many

:answers_ids: Answers, many2many

.. i18n: :function_id: Main Job, many2one

:function_id: Main Job, many2one

.. i18n: :job_ids: Functions and Addresses, one2many

:job_ids: Functions and Addresses, one2many

.. i18n: :link_ids: Contact Link, one2many

:link_ids: Contact Link, one2many

.. i18n: :name: Last Name, char, required

:name: Last Name, char, required

.. i18n: :magazine_subscription_source: Mag. Subscription Source, char

:magazine_subscription_source: Mag. Subscription Source, char

.. i18n: :mobile: Mobile, char

:mobile: Mobile, char

.. i18n: :who_date_accept: Accept Date, date

:who_date_accept: Accept Date, date

.. i18n: :birthdate: Birth Date, date

:birthdate: Birth Date, date

.. i18n: :who_date_last: Last Modification, date

:who_date_last: Last Modification, date

.. i18n: :national_number: National Number, char

:national_number: National Number, char

.. i18n: :article_ids: Articles, many2many

:article_ids: Articles, many2many

.. i18n: Object: Contact Partner Function (res.partner.job)
.. i18n: ##################################################

Object: Contact Partner Function (res.partner.job)
##################################################

.. i18n: :date_stop: Date Stop, date

:date_stop: Date Stop, date

.. i18n: :dir_presence: In Directory, boolean

:dir_presence: In Directory, boolean

.. i18n: :canal_id: Canal, many2one

:canal_id: Canal, many2one

.. i18n:     *favorite chanel for communication*

    *favorite chanel for communication*

.. i18n: :date_end: Date end, date

:date_end: Date end, date

.. i18n: :address_id: Address, many2one

:address_id: Address, many2one

.. i18n: :contact_id: Contact, many2one, required

:contact_id: Contact, many2one, required

.. i18n: :function_label: Function Label, char, required

:function_label: Function Label, char, required

.. i18n: :team_id: Team, many2one

:team_id: Team, many2one

.. i18n: :password: Password, char

:password: Password, char

.. i18n: :date_start: Date start, date

:date_start: Date start, date

.. i18n: :who_presence: In Whos Who, boolean

:who_presence: In Whos Who, boolean

.. i18n: :state: State, selection, required

:state: State, selection, required

.. i18n: :department: Department, char

:department: Department, char

.. i18n: :email: E-Mail, char

:email: E-Mail, char

.. i18n: :phone: Phone, char

:phone: Phone, char

.. i18n: :active: Active, boolean

:active: Active, boolean

.. i18n: :answers_ids: Answers, many2many

:answers_ids: Answers, many2many

.. i18n: :function_id: Partner Function, many2one

:function_id: Partner Function, many2one

.. i18n: :sequence_partner: Partner Seq., integer

:sequence_partner: Partner Seq., integer

.. i18n:     *Order of importance of this job title in the list of job title of the linked partner*

    *Order of importance of this job title in the list of job title of the linked partner*

.. i18n: :sequence_contact: Contact Seq., integer

:sequence_contact: Contact Seq., integer

.. i18n:     *Order of importance of this address in the list of addresses of the linked contact*

    *Order of importance of this address in the list of addresses of the linked contact*

.. i18n: :name: Partner, many2one

:name: Partner, many2one

.. i18n: :function_code_label: Codes, char

:function_code_label: Codes, char

.. i18n: :token: Token, char

:token: Token, char

.. i18n: :login_name: Login Name, char

:login_name: Login Name, char
