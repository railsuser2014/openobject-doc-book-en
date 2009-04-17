
.. module:: bookstore
    :synopsis: Bookstore Verticalisation 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/bookstore"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Bookstore Verticalisation (*bookstore*)
=======================================
:Module: bookstore
:Name: Bookstore Verticalisation
:Version: 5.0.1.0
:Author: Tiny
:Directory: bookstore
:Web: 
:Official module: no
:Quality certified: no

Description
-----------

::

  Module to manage book store.
      Add book Information, 
      Author Information, 
      Books Category,
      Related books,
      Available Languages,

Download links
--------------

You can download this module as a zip file in the following version:

  * `trunk </download/modules/trunk/bookstore.zip>`_


Dependencies
------------

 * :mod:`library`
 * :mod:`delivery`
 * :mod:`sale`

Reports
-------

None


Menus
-------


None


Views
-----

 * \* INHERIT Company (form)
 * \* INHERIT Partner (form)
 * \* INHERIT Partner (form)
 * \* INHERIT Partner Address (form)
 * Partners (tree)
 * \* INHERIT Sale lines replace uom by mode (form)
 * \* INHERIT  (form)


Objects
-------

None
