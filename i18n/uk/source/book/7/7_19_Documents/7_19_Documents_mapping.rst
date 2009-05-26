
.. i18n: Mapping between Open ERP resources and directories
.. i18n: ==================================================

Mapping between Open ERP resources and directories
==================================================

.. i18n: Each directory can either have the type ``Static`` or be linked to another resource. A static directory, as
.. i18n: with Operating Systems, is the classic directory that can contain a set of files. The directories
.. i18n: linked to systems resources automatically possess sub-directories for each of resource types defined in
.. i18n: the parent directory.

Each directory can either have the type ``Static`` or be linked to another resource. A static directory, as
with Operating Systems, is the classic directory that can contain a set of files. The directories
linked to systems resources automatically possess sub-directories for each of resource types defined in
the parent directory.

.. i18n: .. tip:: Directories in English
.. i18n: 
.. i18n:     To keep them synchronized to the working language, directory names are not translatable.
.. i18n:     But Open ERP's demonstration data automatically creates directories in English.
.. i18n:     You can rename them through the menu :menuselection:`Document Management --> Configuration -->
.. i18n:     Directories`.

.. tip:: Directories in English

    To keep them synchronized to the working language, directory names are not translatable.
    But Open ERP's demonstration data automatically creates directories in English.
    You can rename them through the menu :menuselection:`Document Management --> Configuration -->
    Directories`.

.. i18n: For example you can look at the directory shown in :menuselection:`Main Repository --> Sales Orders
.. i18n: --> All Sales Orders`. You'll see the directory for all the orders present in Open ERP that was
.. i18n: created automatically by the system.

For example you can look at the directory shown in :menuselection:`Main Repository --> Sales Orders
--> All Sales Orders`. You'll see the directory for all the orders present in Open ERP that was
created automatically by the system.

.. i18n: .. figure::  images/document_sale.png
.. i18n:    :scale: 50
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Orders in Open ERP*

.. figure::  images/document_sale.png
   :scale: 50
   :align: center

   *Orders in Open ERP*

.. i18n: .. figure::  images/document_ftp_sale.png
.. i18n:    :scale: 50
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Directories representing all the orders in the document management system*

.. figure::  images/document_ftp_sale.png
   :scale: 50
   :align: center

   *Directories representing all the orders in the document management system*

.. i18n: Directories can follow a tree like the tree of resources in Open ERP. For example if you go to the
.. i18n: directory :menuselection:`Main Repository --> Projects` you'll see the structure of the analytic
.. i18n: accounts.

Directories can follow a tree like the tree of resources in Open ERP. For example if you go to the
directory :menuselection:`Main Repository --> Projects` you'll see the structure of the analytic
accounts.

.. i18n: To define a directory containing a specific type of resource you have to define parameters when you
.. i18n: define the directory itself:

To define a directory containing a specific type of resource you have to define parameters when you
define the directory itself:

.. i18n: * :guilabel:`Type` : Other Resources
.. i18n: 
.. i18n: * :guilabel:`Child Models` : Choose one of the system objects
.. i18n: 
.. i18n: * :guilabel:`Domain` :  an event filtered so that it sees only a subset of the resources
.. i18n: 
.. i18n: * :guilabel:`Tree structure` : to show the resources hierarchically

* :guilabel:`Type` : Other Resources

* :guilabel:`Child Models` : Choose one of the system objects

* :guilabel:`Domain` :  an event filtered so that it sees only a subset of the resources

* :guilabel:`Tree structure` : to show the resources hierarchically

.. i18n: .. figure::  images/document_dir_form.png
.. i18n:    :scale: 50
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Configuration of the directory containing quotations (draft orders)*

.. figure::  images/document_dir_form.png
   :scale: 50
   :align: center

   *Configuration of the directory containing quotations (draft orders)*

.. i18n: This is a very flexible approach because any modification of the resource in Open ERP is
.. i18n: automatically reflected in the document management system. So when the quotation gets confirmed in
.. i18n: Open ERP the directory no longer appears as a quotation through FTP access.

This is a very flexible approach because any modification of the resource in Open ERP is
automatically reflected in the document management system. So when the quotation gets confirmed in
Open ERP the directory no longer appears as a quotation through FTP access.

.. i18n: Here are some examples of directories linked to Open ERP resources that could be helpful when
.. i18n: configured in the document management system:

Here are some examples of directories linked to Open ERP resources that could be helpful when
configured in the document management system:

.. i18n: * Quotations and Order: storing documents that relate to orders,
.. i18n: 
.. i18n: * Products: for storing products' technical datasheets,
.. i18n: 
.. i18n: * Users: to automatically define a directory owned by each user of the system,
.. i18n: 
.. i18n: * Employees: to store documents about employees, such as their CVs, your interview notes, contract
.. i18n:   details, and their annual assessments,
.. i18n: 
.. i18n: * Support Requests: storing items about requests or about technical support responses,
.. i18n: 
.. i18n: * Analytic accounts or project: to store project management and tracking documents.

* Quotations and Order: storing documents that relate to orders,

* Products: for storing products' technical datasheets,

* Users: to automatically define a directory owned by each user of the system,

* Employees: to store documents about employees, such as their CVs, your interview notes, contract
  details, and their annual assessments,

* Support Requests: storing items about requests or about technical support responses,

* Analytic accounts or project: to store project management and tracking documents.

.. i18n: .. Copyright © Open Object Press. All rights reserved.

.. Copyright © Open Object Press. All rights reserved.

.. i18n: .. You may take electronic copy of this publication and distribute it if you don't
.. i18n: .. change the content. You can also print a copy to be read by yourself only.

.. You may take electronic copy of this publication and distribute it if you don't
.. change the content. You can also print a copy to be read by yourself only.

.. i18n: .. We have contracts with different publishers in different countries to sell and
.. i18n: .. distribute paper or electronic based versions of this book (translated or not)
.. i18n: .. in bookstores. This helps to distribute and promote the Open ERP product. It
.. i18n: .. also helps us to create incentives to pay contributors and authors using author
.. i18n: .. rights of these sales.

.. We have contracts with different publishers in different countries to sell and
.. distribute paper or electronic based versions of this book (translated or not)
.. in bookstores. This helps to distribute and promote the Open ERP product. It
.. also helps us to create incentives to pay contributors and authors using author
.. rights of these sales.

.. i18n: .. Due to this, grants to translate, modify or sell this book are strictly
.. i18n: .. forbidden, unless Tiny SPRL (representing Open Object Press) gives you a
.. i18n: .. written authorisation for this.

.. Due to this, grants to translate, modify or sell this book are strictly
.. forbidden, unless Tiny SPRL (representing Open Object Press) gives you a
.. written authorisation for this.

.. i18n: .. Many of the designations used by manufacturers and suppliers to distinguish their
.. i18n: .. products are claimed as trademarks. Where those designations appear in this book,
.. i18n: .. and Open Object Press was aware of a trademark claim, the designations have been
.. i18n: .. printed in initial capitals.

.. Many of the designations used by manufacturers and suppliers to distinguish their
.. products are claimed as trademarks. Where those designations appear in this book,
.. and Open Object Press was aware of a trademark claim, the designations have been
.. printed in initial capitals.

.. i18n: .. While every precaution has been taken in the preparation of this book, the publisher
.. i18n: .. and the authors assume no responsibility for errors or omissions, or for damages
.. i18n: .. resulting from the use of the information contained herein.

.. While every precaution has been taken in the preparation of this book, the publisher
.. and the authors assume no responsibility for errors or omissions, or for damages
.. resulting from the use of the information contained herein.

.. i18n: .. Published by Open Object Press, Grand Rosière, Belgium

.. Published by Open Object Press, Grand Rosière, Belgium
