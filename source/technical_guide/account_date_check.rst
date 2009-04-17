
.. module:: account_date_check
    :synopsis: Account Date check (Official, Quality Certified)
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/account_date_check"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Account Date check (*account_date_check*)
=========================================
:Module: account_date_check
:Name: Account Date check
:Version: 5.0.1.0
:Author: Tiny
:Directory: account_date_check
:Web: http://www.openerp.com
:Official module: yes
:Quality certified: yes

Description
-----------

::

  * Adds a field on journals: "Allows date not in the period"
      * By default, this field is checked.
  
  If this field is not checked, the system control that the date is in the
  period when you create an account entry. Otherwise, it generates an
  error message: "The date of your account move is not in the defined
  period !"

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 </download/modules/5.0/account_date_check.zip>`_
  * `trunk </download/modules/trunk/account_date_check.zip>`_


Dependencies
------------

 * :mod:`account`

Reports
-------

None


Menus
-------


None


Views
-----

 * \* INHERIT account.journal.form.inherit2 (form)


Objects
-------

None
