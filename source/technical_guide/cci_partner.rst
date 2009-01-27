
Module CCI Partner (*cci_partner*)
==================================
:Module: cci_partner
:Name: CCI Partner
:Version: 5.0.1.0
:Directory: cci_partner
:Web: http://www.openerp.com

Description
-----------

::

  Specific module for cci project which will inherit partner module

Dependencies
------------

 * base - installed
 * base_vat - installed
 * cci_base_contact - installed
 * account_l10nbe_domiciliation - installed
 * cci_country - installed

Reports
-------

 * Count invoices

Menus
-------

 * Partners/Configuration/States
 * Partners/Configuration/States/Activity State
 * Partners/Configuration/States/Customer State
 * Partners/Configuration/Partner Activity
 * Partners/Configuration/Partner Activity/Activity
 * Partners/Configuration/Partner Activity/Activity Relation
 * Partners/Configuration/Partner Activity/Activity List
 * Partners/Configuration/Zip
 * Partners/Configuration/Zip/Zip
 * Partners/Configuration/Zip/Zip Group
 * Partners/Configuration/Zip/Group Type
 * Partners/Configuration/Article
 * Partners/Configuration/Article/Article
 * Partners/Configuration/Article/Article Keyword
 * Partners/Configuration/Article/Article Reviews
 * Partners/Configuration/Link Type/Partner Link Type

Views
-----

 * \* INHERIT res.company.form (form)
 * res.partner.state.form (form)
 * res.partner.state2.form (form)
 * res.partner.activity.form (form)
 * res.partner.activity.tree (tree)
 * res.partner.activity.relation.form (form)
 * res.partner.activity.relation.tree (tree)
 * res.partner.activity.list.form (form)
 * res.partner.activity.list.tree (tree)
 * res.partner.zip.form (form)
 * res.partner.zip.tree (tree)
 * res.partner.zip.group.form (form)
 * res.partner.zip.group.tree (tree)
 * res.partner.zip.group.type.form (form)
 * res.partner.zip.group.type.tree (tree)
 * res.partner.article.form (form)
 * res.partner.article.tree (tree)
 * res.partner.article.keywords.form (form)
 * res.partner.article.keywords.tree (tree)
 * res.partner.article.review.form (form)
 * res.partner.article.review.tree (tree)
 * res.partner.relation.type.form (form)
 * res.partner.relation.tree (tree)
 * res.partner.relation.form (form)
 * \* INHERIT res.partner.contact.form (form)
 * \* INHERIT res.partner.contact.form (form)
 * \* INHERIT res.partner.contact.form (form)
 * \* INHERIT res.partner.job.form.inherit1 (form)
 * \* INHERIT Partner addresses inherited (form)
 * \* INHERIT res.partner.form (form)
 * \* INHERIT res.partner.form (form)
 * \* INHERIT res.partner.form (form)
 * \* INHERIT res.partner.form (form)
 * \* INHERIT res.partner.form (form)
 * \* INHERIT res.partner.form (form)
 * \* INHERIT Partner form inherited (form)


Objects
-------

Object: res.partner.state
#########################

.. index::
  single: res.partner.state object
.. 


:name: Partner Status, char, required



.. index::
  single: name field
.. 



Object: res.partner.state2
##########################

.. index::
  single: res.partner.state2 object
.. 


:name: Customer Status, char, required



.. index::
  single: name field
.. 



Object: res.partner.article.review
##################################

.. index::
  single: res.partner.article.review object
.. 


:date: Date, date, required



.. index::
  single: date field
.. 




:article_ids: Articles, one2many



.. index::
  single: article_ids field
.. 




:name: Name, char, required



.. index::
  single: name field
.. 



Object: res.partner.article
###########################

.. index::
  single: res.partner.article object
.. 


:picture: Picture, boolean



.. index::
  single: picture field
.. 




:subtitle: Subtitle, text



.. index::
  single: subtitle field
.. 




:review_id: Review, many2one



.. index::
  single: review_id field
.. 




:canal_id: Reference, char

    *A text with or without a link incorporated*

.. index::
  single: canal_id field
.. 




:press_review: In the next press review, boolean

    *Must be inserted on the next press review*

.. index::
  single: press_review field
.. 




:data: Data, boolean



.. index::
  single: data field
.. 




:title: Title, char, required



.. index::
  single: title field
.. 




:summary: Summary, text



.. index::
  single: summary field
.. 




:source_id: Source, char



.. index::
  single: source_id field
.. 




:contact_ids: Contacts, many2many



.. index::
  single: contact_ids field
.. 




:keywords_ids: Keywords, many2many



.. index::
  single: keywords_ids field
.. 




:graph: Graph, boolean



.. index::
  single: graph field
.. 




:date: Date, date, required



.. index::
  single: date field
.. 




:partner_ids: Partners, many2many



.. index::
  single: partner_ids field
.. 




:article_length: Length, float



.. index::
  single: article_length field
.. 




:article_id: Article, char



.. index::
  single: article_id field
.. 




:page: Page, integer



.. index::
  single: page field
.. 



Object: res.partner.article.keywords
####################################

.. index::
  single: res.partner.article.keywords object
.. 


:article_ids: Articles, many2many



.. index::
  single: article_ids field
.. 




:name: Name, char, required



.. index::
  single: name field
.. 



Object: res.partner.zip.group.type
##################################

.. index::
  single: res.partner.zip.group.type object
.. 


:name: Name, char, required



.. index::
  single: name field
.. 



Object: res.partner.zip.group
#############################

.. index::
  single: res.partner.zip.group object
.. 


:name: Name, char, required



.. index::
  single: name field
.. 




:type_id: Type, many2one



.. index::
  single: type_id field
.. 



Object: res.partner.zip
#######################

.. index::
  single: res.partner.zip object
.. 


:post_center_id: Post Center, char



.. index::
  single: post_center_id field
.. 




:city: City, char



.. index::
  single: city field
.. 




:user_id: Salesman Responsible, many2one



.. index::
  single: user_id field
.. 




:name: Zip Code, char, required



.. index::
  single: name field
.. 




:groups_id: Areas, many2many



.. index::
  single: groups_id field
.. 




:post_center_special: Post Center Special, boolean



.. index::
  single: post_center_special field
.. 




:partner_id: Master Cci, many2one



.. index::
  single: partner_id field
.. 




:distance: Distance, integer

    *Distance (km) between zip location and the cci.*

.. index::
  single: distance field
.. 



Object: res.partner.activity.list
#################################

.. index::
  single: res.partner.activity.list object
.. 


:abbreviation: Abbreviation, char



.. index::
  single: abbreviation field
.. 




:name: Code list, char, required



.. index::
  single: name field
.. 



Object: res.partner.activity
############################

.. index::
  single: res.partner.activity object
.. 


:code_relations: Related codes, many2many



.. index::
  single: code_relations field
.. 




:code: Code, char, required



.. index::
  single: code field
.. 




:list_id: List, many2one, required



.. index::
  single: list_id field
.. 




:description: Description, text



.. index::
  single: description field
.. 




:label: Label, char, required



.. index::
  single: label field
.. 



Object: res.partner.activity.relation
#####################################

.. index::
  single: res.partner.activity.relation object
.. 


:importance: Importance, selection, required



.. index::
  single: importance field
.. 




:activity_id: Activity, many2one



.. index::
  single: activity_id field
.. 




:partner_id: Partner, many2one



.. index::
  single: partner_id field
.. 



Object: res.partner.relation.type
#################################

.. index::
  single: res.partner.relation.type object
.. 


:name: Contact, char, required



.. index::
  single: name field
.. 



Object: res.partner.country.relation
####################################

.. index::
  single: res.partner.country.relation object
.. 


:country_id: Country, many2one



.. index::
  single: country_id field
.. 




:frequency: Frequency, selection



.. index::
  single: frequency field
.. 




:partner_id: Partner, many2one



.. index::
  single: partner_id field
.. 




:type: Types, selection



.. index::
  single: type field
.. 

