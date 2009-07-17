
.. i18n: **************************
.. i18n: Document Management System
.. i18n: **************************

**************************
Document Management System
**************************

.. i18n: Configure the DMS
.. i18n: =================

Configure the DMS
=================

.. i18n: As the NotSoTiny company is growing faster, it requires a way to efficiently
.. i18n: store, track, index and route all documents of the company. They need...

As the NotSoTiny company is growing faster, it requires a way to efficiently
store, track, index and route all documents of the company. They need...

.. i18n: So you decided to install the document management system of Open ERP to get
.. i18n: a centralized storing and processing mechanism for all documents.

So you decided to install the document management system of Open ERP to get
a centralized storing and processing mechanism for all documents.

.. i18n: .. note:: Exercice 1 - Install the dms
.. i18n: 
.. i18n:     Install and configure the module for document management.

.. note:: Exercice 1 - Install the dms

    Install and configure the module for document management.

.. i18n: You will first start to create the DMS structure using the FTP access. So, you
.. i18n: should connect to the FTP server of Open ERP and create the following structure.

You will first start to create the DMS structure using the FTP access. So, you
should connect to the FTP server of Open ERP and create the following structure.

.. i18n: * Documents
.. i18n: 
.. i18n:   * Sales
.. i18n:   * Projects
.. i18n:   * Employees

* Documents

  * Sales
  * Projects
  * Employees

.. i18n: .. note:: Exercice 2 - Connect to the FTP
.. i18n: 
.. i18n:     Create the directories structure from the FTP interface.

.. note:: Exercice 2 - Connect to the FTP

    Create the directories structure from the FTP interface.

.. i18n: NotSoTiny decided to classify all documents into their relative projects or
.. i18n: relative sales orders. They need an automaticly generated directory structure
.. i18n: that reflects their current sales order.

NotSoTiny decided to classify all documents into their relative projects or
relative sales orders. They need an automaticly generated directory structure
that reflects their current sales order.

.. i18n: .. note:: Exercice 3 - Configure DMS for sales orders
.. i18n: 
.. i18n:     Configure the DMS so that you see automatically one directory per sale
.. i18n:     order in the "Sales" directory.

.. note:: Exercice 3 - Configure DMS for sales orders

    Configure the DMS so that you see automatically one directory per sale
    order in the "Sales" directory.

.. i18n: Now, the employees can upload to the FTP each time they get a document related
.. i18n: to a sale order. ... describe why it's good ...

Now, the employees can upload to the FTP each time they get a document related
to a sale order. ... describe why it's good ...

.. i18n: .. note:: Exercice 4 - Upload a document on SO/001
.. i18n: 
.. i18n:     From the FTP access, copy a document in the SO/001 directory. Then, connect
.. i18n:     to Open ERP interface and check that there is an available attachement on
.. i18n:     the SO/001. Then, do the invert: attach a document from the Open ERP interface
.. i18n:     to the SO/001 sales order and download this document from the FTP access.

.. note:: Exercice 4 - Upload a document on SO/001

    From the FTP access, copy a document in the SO/001 directory. Then, connect
    to Open ERP interface and check that there is an available attachement on
    the SO/001. Then, do the invert: attach a document from the Open ERP interface
    to the SO/001 sales order and download this document from the FTP access.

.. i18n: You noticed that the salesman lost a lot of time of sending the different quotations
.. i18n: by email or by fax to the customers. What you need is a way to efficiently store
.. i18n: and make available the prints of the sales orders. As to improve the efficiency
.. i18n: of the DMS, you want to put automatically a .PDF file, which is the result of the
.. i18n: print of the sale order in each sales directory.

You noticed that the salesman lost a lot of time of sending the different quotations
by email or by fax to the customers. What you need is a way to efficiently store
and make available the prints of the sales orders. As to improve the efficiency
of the DMS, you want to put automatically a .PDF file, which is the result of the
print of the sale order in each sales directory.

.. i18n: .. note:: Exercice 5 - Virtual printed files
.. i18n: 
.. i18n:     Configure the DMS to see a "SO001_print.pdf" file under each sale order
.. i18n:     directory. This file should be the result of the print of the sale order.

.. note:: Exercice 5 - Virtual printed files

    Configure the DMS to see a "SO001_print.pdf" file under each sale order
    directory. This file should be the result of the print of the sale order.

.. i18n: Todo:

Todo:

.. i18n: * Fixed Templates of Directories
.. i18n: * Search for a file
.. i18n: 
.. i18n:   * Using meta data (partner)
.. i18n:   * Using indexed content
.. i18n: 
.. i18n: * Each time someone read a virtual file, it should save a copy in attachemnt

* Fixed Templates of Directories
* Search for a file

  * Using meta data (partner)
  * Using indexed content

* Each time someone read a virtual file, it should save a copy in attachemnt
