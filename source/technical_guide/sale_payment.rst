
.. module:: sale_payment
    :synopsis: Sale payment type
    :noindex:
.. 

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

Sale payment type (*sale_payment*)
==================================
:Module: sale_payment
:Name: Sale payment type
:Version: 5.0.1.0
:Directory: sale_payment
:Web: 
:Is certified: no

Description
-----------

::

  Adds payment type and bank account to sale process.
  
  The sale order inherits payment type and bank account (if the payment type is related to bank accounts) from partner as default. Next, the invoice based on this sale order inherits the payment information from it.
  
  Based on previous work of Readylan (version for 4.2).

Dependencies
------------

 * :mod:`account_payment`
 * :mod:`account_payment_extension`
 * :mod:`sale`
 * :mod:`stock`

Reports
-------

None


Menus
-------


None


Views
-----

 * \* INHERIT sale.order.form.sale_paytype (form)


Objects
-------

None
