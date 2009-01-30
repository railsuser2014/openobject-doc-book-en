
.. module:: discount_campaign
    :synopsis: Discount on Marketing Campaigns
    :noindex:
.. 

Discount on Marketing Campaigns (*discount_campaign*)
=====================================================
:Module: discount_campaign
:Name: Discount on Marketing Campaigns
:Version: 5.0.1.0
:Directory: discount_campaign
:Web: http://tinyerp.com/module_crm_marketing.html
:Is certified: no

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

Object: discount.campaign (discount.campaign)
#############################################



:line_ids: Discount Lines, one2many





:date_stop: Stop Date, date, required





:date_start: Start Date, date, required





:name: Name, char





:state: State, selection, readonly




Object: discount.campaign.line (discount.campaign.line)
#######################################################



:condition_sale: Sale Condition, char





:condition_product_id: Product, many2one





:sequence: Sequence, integer, required





:name: Name, char





:discount_id: Discount Lines, many2one





:discount: Discount, float





:condition_category_id: Category, many2one





:condition_quantity: Min. Quantity, float


