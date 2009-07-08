**************************
Document Management System
**************************

Configure the DMS
=================

As the NotSoTiny company is growing faster, it requires a way to efficiently
store, track, index and route all documents of the company. They need...

So you decided to install the document management system of Open ERP to get
a centralized storing and processing mechanism for all documents.

.. note:: Exercice 1 - Install the dms

    Install and configure the module for document management.

You will first start to create the DMS structure using the FTP access. So, you
should connect to the FTP server of Open ERP and create the following structure.

* Documents

  * Sales
  * Projects
  * Employees

.. note:: Exercice 2 - Connect to the FTP

    Create the directories structure from the FTP interface.


NotSoTiny decided to classify all documents into their relative projects or
relative sales orders. They need an automaticly generated directory structure
that reflects their current sales order.

.. note:: Exercice 3 - Configure DMS for sales orders

    Configure the DMS so that you see automatically one directory per sale
    order in the "Sales" directory.

Now, the employees can upload to the FTP each time they get a document related
to a sale order. ... describe why it's good ...

.. note:: Exercice 4 - Upload a document on SO/001

    From the FTP access, copy a document in the SO/001 directory. Then, connect
    to Open ERP interface and check that there is an available attachement on
    the SO/001. Then, do the invert: attach a document from the Open ERP interface
    to the SO/001 sales order and download this document from the FTP access.

You noticed that the salesman lost a lot of time of sending the different quotations
by email or by fax to the customers. What you need is a way to efficiently store
and make available the prints of the sales orders. As to improve the efficiency
of the DMS, you want to put automatically a .PDF file, which is the result of the
print of the sale order in each sales directory.


.. note:: Exercice 5 - Virtual printed files

    Configure the DMS to see a "SO001_print.pdf" file under each sale order
    directory. This file should be the result of the print of the sale order.


Todo:

* Fixed Templates of Directories
* Search for a file

  * Using meta data (partner)
  * Using indexed content

* Each time someone read a virtual file, it should save a copy in attachemnt
