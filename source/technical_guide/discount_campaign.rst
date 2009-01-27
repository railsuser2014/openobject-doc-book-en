
Module Discount on Marketing Campaigns (*discount_campaign*)
============================================================
:Module: discount_campaign
:Name: Discount on Marketing Campaigns
:Version: 5.0.1.0
:Directory: discount_campaign
:Web: http://tinyerp.com/module_crm_marketing.html

Description
-----------

::

  Marketing management module

Dependencies
------------

 * base - installed
 * sale - installed

Reports
-------

None


Menus
-------

 * Sales Management/Configuration/Discount Campaign

Views
-----

 * \* INHERIT discountcampaign.sale.order.form.view (form)
 * \* INHERIT discount.campaign.partner.form.view (form)
 * discount.campaign.form (form)
 * discount.campaign.tree (tree)
 * discount.campaign.line.form (form)
 * discount.campaign.line.tree (tree)


Objects
-------

Object: discount.campaign
#########################

.. index::
  single: discount.campaign object
.. 


:line_ids: Discount Lines, one2many



.. index::
  single: line_ids field
.. 




:date_stop: Stop Date, date, required



.. index::
  single: date_stop field
.. 




:date_start: Start Date, date, required



.. index::
  single: date_start field
.. 




:name: Name, char



.. index::
  single: name field
.. 




:state: State, selection, readonly



.. index::
  single: state field
.. 



Object: discount.campaign.line
##############################

.. index::
  single: discount.campaign.line object
.. 


:condition_sale: Sale Condition, char



.. index::
  single: condition_sale field
.. 




:condition_product_id: Product, many2one



.. index::
  single: condition_product_id field
.. 




:sequence: Sequence, integer, required



.. index::
  single: sequence field
.. 




:name: Name, char



.. index::
  single: name field
.. 




:discount_id: Discount Lines, many2one



.. index::
  single: discount_id field
.. 




:discount: Discount, float



.. index::
  single: discount field
.. 




:condition_category_id: Category, many2one



.. index::
  single: condition_category_id field
.. 




:condition_quantity: Min. Quantity, float



.. index::
  single: condition_quantity field
.. 

