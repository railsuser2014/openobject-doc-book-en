
.. module:: product_series
    :synopsis: Partner Product Series (Official, Quality Certified)
    :noindex:
.. 

.. raw:: html

      <br />
    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. tip:: This module is part of the Open ERP software, the leading Open Source 
  enterprise management system. If you want to discover Open ERP, check our 
  `screencasts <href="http://openerp.tv>`_ or download 
  `Open ERP <href="http://openerp.com>`_ directly.

Partner Product Series (*product_series*)
=========================================
:Module: product_series
:Name: Partner Product Series
:Version: 5.0.0.1
:Author: Thymbra - Torre de Hanoi
:Directory: product_series
:Web: 
:Official module: yes
:Quality certified: yes

Description
-----------

::

  It relates partners to product series.
  
  This module adds a new object and a field on the product view.

Download links
--------------

You can download this module as a zip file in the following version:

  * `trunk </download/modules/trunk/product_series.zip>`_


Dependencies
------------

 * :mod:`base`
 * :mod:`product`

Reports
-------

None


Menus
-------

 * Products/Configuration/Products Series

Views
-----

 * product.series.form (form)
 * product.series.tree (tree)
 * \* INHERIT product.normal.form (form)


Objects
-------

Object: Partner Product Series (product.series)
###############################################



:code: Code, char





:partner_id: Manufacturer, many2one, required





:name: Name, char





:description: Description, char


