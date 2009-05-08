
.. module:: c2c_multicurrency_journal
    :synopsis: Auto currency computation in journal 
    :noindex:
.. 

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

Auto currency computation in journal (*c2c_multicurrency_journal*)
==================================================================
:Module: c2c_multicurrency_journal
:Name: Auto currency computation in journal
:Version: 1.0
:Author: Camptocamp
:Directory: c2c_multicurrency_journal
:Web: http://www.camptocamp.com
:Official module: no
:Quality certified: no

Description
-----------

::

  
  	Modifiy the journal view in order to fill automatically the fiel currency_amount, or amount. It will add
  	amount_currency and currency columns in your journal view. You can remove this columns ot the views without any		trouble by editing your journal view. But if there are no ammount currency and currency column the mdoule wille		be innefective.  
  	The journal will check if there is a currency, amout-currency or an amount data enter and complete the others.
  	The date taken for computation will be maturity date if there is one, else it will use today date.
  	If you enter currency amount it sign will decide if it is a debit or credit writing
  	

Dependencies
------------

 * :mod:`base`
 * :mod:`account`
 * :mod:`product`

Reports
-------

None


Menus
-------


None


Views
-----


None



Objects
-------

None
