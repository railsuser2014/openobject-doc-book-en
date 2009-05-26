
.. i18n: OpenERP Objects
.. i18n: ===============

OpenERP Objects
===============

.. i18n: Introduction
.. i18n: ----------------

Introduction
----------------

.. i18n: .. This chapter is dedicated to detailed objects definition:
.. i18n:     all fields
.. i18n:     all objects
.. i18n:     inheritancies

.. This chapter is dedicated to detailed objects definition:
    all fields
    all objects
    inheritancies

.. i18n: All the ERP's pieces of data are accessible through "objects". As an example, there is a res.partner object to access the data concerning the partners, an account.invoice object for the data concerning the invoices, etc...

All the ERP's pieces of data are accessible through "objects". As an example, there is a res.partner object to access the data concerning the partners, an account.invoice object for the data concerning the invoices, etc...

.. i18n: Please note that there is an object for every type of resource, and not an object per resource. We have thus a res.partner object to manage all the partners and not a @@res.partner@@ object per partner. If we talk in "object oriented" terms, we could also say that there is an object per level.

Please note that there is an object for every type of resource, and not an object per resource. We have thus a res.partner object to manage all the partners and not a @@res.partner@@ object per partner. If we talk in "object oriented" terms, we could also say that there is an object per level.

.. i18n: The direct consequences is that all the methods of objects have a common parameter: the "ids" parameter. This specifies on which resources (for example, on which partner) the method must be applied. Precisely, this parameter contains a list of resource ids on which the method must be applied.

The direct consequences is that all the methods of objects have a common parameter: the "ids" parameter. This specifies on which resources (for example, on which partner) the method must be applied. Precisely, this parameter contains a list of resource ids on which the method must be applied.

.. i18n: For example, if we have two partners with the identifiers 1 and 5, and we want to call the res_partner method "send_email", we will write something like::
.. i18n: 
.. i18n:         res_partner.send_email(... , [1, 5], ...)

For example, if we have two partners with the identifiers 1 and 5, and we want to call the res_partner method "send_email", we will write something like::

        res_partner.send_email(... , [1, 5], ...)

.. i18n: We will see the exact syntax of object method calls further in this document.

We will see the exact syntax of object method calls further in this document.

.. i18n: In the following section, we will see how to define a new object. Then, we will check out the different methods of doing this.

In the following section, we will see how to define a new object. Then, we will check out the different methods of doing this.

.. i18n: For developers:

For developers:

.. i18n: * Open ERP "objects" are usually called classes in object oriented programming.
.. i18n: * A Open ERP "resource" is usually called an object in OO programming, instance of a class. 

* Open ERP "objects" are usually called classes in object oriented programming.
* A Open ERP "resource" is usually called an object in OO programming, instance of a class. 

.. i18n: It's a bit confusing when you try to program inside Open ERP, because the language used is Python, and Python is a fully object oriented language, and has objects and instances ...

It's a bit confusing when you try to program inside Open ERP, because the language used is Python, and Python is a fully object oriented language, and has objects and instances ...

.. i18n: Luckily, an Open ERP "resource" can be converted magically into a nice Python object using the "browse" class method (Open ERP object method). 

Luckily, an Open ERP "resource" can be converted magically into a nice Python object using the "browse" class method (Open ERP object method). 
