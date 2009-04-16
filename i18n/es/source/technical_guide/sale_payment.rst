
.. i18n: .. module:: sale_payment
.. i18n:     :synopsis: Sale payment type 
.. i18n:     :noindex:
.. i18n: .. 

.. module:: sale_payment
    :synopsis: Sale payment type 
    :noindex:
.. 

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. i18n: Sale payment type (*sale_payment*)
.. i18n: ==================================
.. i18n: :Module: sale_payment
.. i18n: :Name: Sale payment type
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Zikzakmedia SL
.. i18n: :Directory: sale_payment
.. i18n: :Web: 
.. i18n: :Official module: no
.. i18n: :Quality certified: no

Sale payment type (*sale_payment*)
==================================
:Module: sale_payment
:Name: Sale payment type
:Version: 5.0.1.0
:Author: Zikzakmedia SL
:Directory: sale_payment
:Web: 
:Official module: no
:Quality certified: no

.. i18n: Description
.. i18n: -----------

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   Adds payment type and bank account to sale process.
.. i18n:   
.. i18n:   The sale order inherits payment type and bank account (if the payment type is related to bank accounts) 
.. i18n:   from partner as default. Next, the invoice based on this sale order inherits the payment information 
.. i18n:   from it.
.. i18n:   
.. i18n:   Based on previous work of Readylan (version for 4.2).

::

  Adds payment type and bank account to sale process.
  
  The sale order inherits payment type and bank account (if the payment type is related to bank accounts) 
  from partner as default. Next, the invoice based on this sale order inherits the payment information 
  from it.
  
  Based on previous work of Readylan (version for 4.2).

.. i18n: Dependencies
.. i18n: ------------

Dependencies
------------

.. i18n:  * :mod:`account_payment`
.. i18n:  * :mod:`account_payment_extension`
.. i18n:  * :mod:`sale`
.. i18n:  * :mod:`stock`

 * :mod:`account_payment`
 * :mod:`account_payment_extension`
 * :mod:`sale`
 * :mod:`stock`

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

.. i18n: None

None

.. i18n: Views
.. i18n: -----

Views
-----

.. i18n:  * \* INHERIT sale.order.form.sale_paytype (form)

 * \* INHERIT sale.order.form.sale_paytype (form)

.. i18n: Objects
.. i18n: -------

Objects
-------

.. i18n: None

None
