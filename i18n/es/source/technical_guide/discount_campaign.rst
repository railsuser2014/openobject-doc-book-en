
.. i18n: .. module:: discount_campaign
.. i18n:     :synopsis: Discount on Marketing Campaigns 
.. i18n:     :noindex:
.. i18n: .. 

.. module:: discount_campaign
    :synopsis: Discount on Marketing Campaigns 
    :noindex:
.. 

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. i18n: Discount on Marketing Campaigns (*discount_campaign*)
.. i18n: =====================================================
.. i18n: :Module: discount_campaign
.. i18n: :Name: Discount on Marketing Campaigns
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: discount_campaign
.. i18n: :Web: http://www.openerp.com/
.. i18n: :Official module: no
.. i18n: :Quality certified: no

Discount on Marketing Campaigns (*discount_campaign*)
=====================================================
:Module: discount_campaign
:Name: Discount on Marketing Campaigns
:Version: 5.0.1.0
:Author: Tiny
:Directory: discount_campaign
:Web: http://www.openerp.com/
:Official module: no
:Quality certified: no

.. i18n: Description
.. i18n: -----------

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   Marketing management module

::

  Marketing management module

.. i18n: Dependencies
.. i18n: ------------

Dependencies
------------

.. i18n:  * :mod:`base`
.. i18n:  * :mod:`sale`

 * :mod:`base`
 * :mod:`sale`

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

.. i18n:  * Sales Management/Configuration/Discount Campaign

 * Sales Management/Configuration/Discount Campaign

.. i18n: Views
.. i18n: -----

Views
-----

.. i18n:  * \* INHERIT discountcampaign.sale.order.form.view (form)
.. i18n:  * \* INHERIT discount.campaign.partner.form.view (form)
.. i18n:  * discount.campaign.form (form)
.. i18n:  * discount.campaign.tree (tree)
.. i18n:  * discount.campaign.line.form (form)
.. i18n:  * discount.campaign.line.tree (tree)

 * \* INHERIT discountcampaign.sale.order.form.view (form)
 * \* INHERIT discount.campaign.partner.form.view (form)
 * discount.campaign.form (form)
 * discount.campaign.tree (tree)
 * discount.campaign.line.form (form)
 * discount.campaign.line.tree (tree)

.. i18n: Objects
.. i18n: -------

Objects
-------

.. i18n: Object: discount.campaign (discount.campaign)
.. i18n: #############################################

Object: discount.campaign (discount.campaign)
#############################################

.. i18n: :line_ids: Discount Lines, one2many

:line_ids: Discount Lines, one2many

.. i18n: :date_stop: Stop Date, date, required

:date_stop: Stop Date, date, required

.. i18n: :date_start: Start Date, date, required

:date_start: Start Date, date, required

.. i18n: :name: Name, char

:name: Name, char

.. i18n: :state: State, selection, readonly

:state: State, selection, readonly

.. i18n: Object: discount.campaign.line (discount.campaign.line)
.. i18n: #######################################################

Object: discount.campaign.line (discount.campaign.line)
#######################################################

.. i18n: :condition_sale: Sale Condition, char

:condition_sale: Sale Condition, char

.. i18n: :condition_product_id: Product, many2one

:condition_product_id: Product, many2one

.. i18n: :sequence: Sequence, integer, required

:sequence: Sequence, integer, required

.. i18n: :name: Name, char

:name: Name, char

.. i18n: :discount_id: Discount Lines, many2one

:discount_id: Discount Lines, many2one

.. i18n: :discount: Discount, float

:discount: Discount, float

.. i18n: :condition_category_id: Category, many2one

:condition_category_id: Category, many2one

.. i18n: :condition_quantity: Min. Quantity, float

:condition_quantity: Min. Quantity, float
