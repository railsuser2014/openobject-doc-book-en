
Account Date check (*account_date_check*)
=========================================
:Module: account_date_check
:Name: Account Date check
:Version: 5.0.1.0
:Directory: account_date_check
:Web: http://www.openerp.com

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

 * account - installed

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
