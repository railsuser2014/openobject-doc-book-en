
.. module:: account_date_check
    :synopsis: Account Date check (Official, Quality Certified)
    :noindex:
.. 

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

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
