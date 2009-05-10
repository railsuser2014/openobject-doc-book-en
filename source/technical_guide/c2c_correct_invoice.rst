
.. module:: c2c_correct_invoice
    :synopsis: Invoice Correcting 
    :noindex:
.. 

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

Invoice Correcting (*c2c_correct_invoice*)
==========================================
:Module: c2c_correct_invoice
:Name: Invoice Correcting
:Version: 1.1
:Author: Camptocamp
:Directory: c2c_correct_invoice
:Web: http://www.camptocamp.com
:Official module: no
:Quality certified: no

Description
-----------

::

  
  	This modules allows  in one action correcte a paid invoice. 
  	-This will create a refund, 
  	-Unreconcile the invoice and reconcile it with the refund 
  	-If needed recreate an invoice
  	This wizard override the invoice  Refund wizard
  	It add two more action :
  	-The cancel invoice that will create an refund and unreconcile/reconcile it.
  	-The modify invoice that does the same as before but also create open an new invoice
  	that is the copy of the original invoice.
  	 
  

Dependencies
------------

 * :mod:`base`
 * :mod:`c2c_partner_address`
 * :mod:`account`

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
