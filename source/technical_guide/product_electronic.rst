
.. module:: product_electronic
    :synopsis: Products Attributes & Manufacturers 
    :noindex:
.. 

.. raw:: html

      <br />
    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. tip:: This module is part of the Open ERP software, the leading Open Source 
  enterprise management system. If you want to discover Open ERP, check our 
  `screencasts <href="http://openerp.tv>`_ or download 
  `Open ERP <href="http://openerp.com>`_ directly.

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/product_electronic"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Products Attributes & Manufacturers (*product_electronic*)
==========================================================
:Module: product_electronic
:Name: Products Attributes & Manufacturers
:Version: 5.0.1.0
:Author: Tiny
:Directory: product_electronic
:Web: 
:Official module: no
:Quality certified: no

Description
-----------

::

  A module that add manufacturers and attributes on the product form

Download links
--------------

You can download this module as a zip file in the following version:

  * `4.2 <http://www.openerp.com/download/modules/4.2/product_electronic.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/product_electronic.zip>`_


Dependencies
------------

 * :mod:`base`
 * :mod:`account`
 * :mod:`product`
 * :mod:`stock`

Reports
-------

None


Menus
-------


None


Views
-----

 * \* INHERIT product.normal.form (form)
 * product.electronic.attribute.tree (tree)
 * product.electronic.attribute.form (form)


Objects
-------

Object: Product attributes (product.electronic.attribute)
#########################################################



:name: Attribute, char, required





:value: Value, char





:product_id: Product, many2one


