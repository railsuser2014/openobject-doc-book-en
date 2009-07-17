
.. i18n: OpenObject Server and Modules
.. i18n: =============================

OpenObject Server and Modules
=============================

.. i18n: * **OpenERP** is a `Client/Server <http://en.wikipedia.org/wiki/Client_server>`_ system that works over a IP Network.
.. i18n: * **OpenERP** programming language is Python.
.. i18n: * **OpenERP** uses Object-Oriented technologies.
.. i18n: * **OpenERP** records its data with a PostgreSQL relational database.
.. i18n: * **OpenERP** business objects are modeled with an Object Relational Mapping (ORM) system.
.. i18n: * **OpenERP** offers three Human Machine Interfaces (HMI) a GTK client, a QT client and a web client (eTiny).
.. i18n: * **OpenERP** uses ReportLab for report generation in (PDF).
.. i18n: * **OpenERP** uses XML for several purpose: describing data, view, reports, data transport (XML-RPC) 

* **OpenERP** is a `Client/Server <http://en.wikipedia.org/wiki/Client_server>`_ system that works over a IP Network.
* **OpenERP** programming language is Python.
* **OpenERP** uses Object-Oriented technologies.
* **OpenERP** records its data with a PostgreSQL relational database.
* **OpenERP** business objects are modeled with an Object Relational Mapping (ORM) system.
* **OpenERP** offers three Human Machine Interfaces (HMI) a GTK client, a QT client and a web client (eTiny).
* **OpenERP** uses ReportLab for report generation in (PDF).
* **OpenERP** uses XML for several purpose: describing data, view, reports, data transport (XML-RPC) 

.. i18n: Technical Architecture
.. i18n: ----------------------

Technical Architecture
----------------------

.. i18n: Server/client, XML-RPC
.. i18n: ++++++++++++++++++++++

Server/client, XML-RPC
++++++++++++++++++++++

.. i18n: Open ERP is a based on a client/server architecture. The server and the client communicate using the XML-RPC protocol. XML-RPC is a very simple protocol which allows the client to do remote procedure calls. The function called, its arguments, and the result are sent HTTP and encoded using XML.

Open ERP is a based on a client/server architecture. The server and the client communicate using the XML-RPC protocol. XML-RPC is a very simple protocol which allows the client to do remote procedure calls. The function called, its arguments, and the result are sent HTTP and encoded using XML.

.. i18n: For more information on XML-RPC, please see: http://www.xml-rpc.com/

For more information on XML-RPC, please see: http://www.xml-rpc.com/

.. i18n: Since version 4.2, there is a new protocol between client/server that have been called net-rpc. It is based on the python cPickle function, it is faster than the xml-rpc.

Since version 4.2, there is a new protocol between client/server that have been called net-rpc. It is based on the python cPickle function, it is faster than the xml-rpc.

.. i18n: Client
.. i18n: ++++++

Client
++++++

.. i18n: The logic of Open ERP is entirely on the server side. The client is very simple; his work is to ask data (forms, lists, trees) from the server and to send them back. With this approach, nearly all developments are made on the server side. This makes Open ERP easier to develop and to maintain.

The logic of Open ERP is entirely on the server side. The client is very simple; his work is to ask data (forms, lists, trees) from the server and to send them back. With this approach, nearly all developments are made on the server side. This makes Open ERP easier to develop and to maintain.

.. i18n: The client doesn't understand what it posts. Even actions like 'Click on the print icon' are sent to the server to ask how to react.

The client doesn't understand what it posts. Even actions like 'Click on the print icon' are sent to the server to ask how to react.

.. i18n: The client operation is very simple; when a user makes an action (save a form, open a menu, print, ...) it sends this action to the server. The server then sends the new action to execute to the client.

The client operation is very simple; when a user makes an action (save a form, open a menu, print, ...) it sends this action to the server. The server then sends the new action to execute to the client.

.. i18n: There are three types of action;

There are three types of action;

.. i18n: * Open a window (form or tree)
.. i18n: * Print a document
.. i18n: * Execute a wizard 

* Open a window (form or tree)
* Print a document
* Execute a wizard 

.. i18n: Architecture

Architecture

.. i18n: .. figure::  images/client_server.png
.. i18n:    :scale: 85
.. i18n:    :align: center

.. figure::  images/client_server.png
   :scale: 85
   :align: center

.. i18n: Explanation of modules:

Explanation of modules:

.. i18n: **Server - Base distribution**

**Server - Base distribution**

.. i18n: We use a distributed communication mechanism inside the Open ERP server. Our engine support most commonly distributed patterns: request/reply, publish/subscribe, monitoring, triggers/callback, ...

We use a distributed communication mechanism inside the Open ERP server. Our engine support most commonly distributed patterns: request/reply, publish/subscribe, monitoring, triggers/callback, ...

.. i18n: Different business objects can be in different computers or the same objects can be on multiple computers to perform load-balancing on multiple computers.
.. i18n: Server - Object Relational Mapping (ORM)

Different business objects can be in different computers or the same objects can be on multiple computers to perform load-balancing on multiple computers.
Server - Object Relational Mapping (ORM)

.. i18n: This layer provides additional object functionality on top of postgresql:

This layer provides additional object functionality on top of postgresql:

.. i18n:     * Consistency: powerful validity checks,
.. i18n:     * Work with objects (methods, references, ...)
.. i18n:     * Row-level security (per user/group/role)
.. i18n:     * Complex actions on a group of resources
.. i18n:     * Inheritance 

    * Consistency: powerful validity checks,
    * Work with objects (methods, references, ...)
    * Row-level security (per user/group/role)
    * Complex actions on a group of resources
    * Inheritance 

.. i18n: **Server - Web-Services**

**Server - Web-Services**

.. i18n: The web-service module offer a common interface for all web-services

The web-service module offer a common interface for all web-services

.. i18n:     * SOAP
.. i18n:     * XML-RPC
.. i18n:     * NET-RPC 

    * SOAP
    * XML-RPC
    * NET-RPC 

.. i18n: Business objects can also be accessed via the distributed object mechanism. They can all be modified via the client interface with contextual views.

Business objects can also be accessed via the distributed object mechanism. They can all be modified via the client interface with contextual views.

.. i18n: **Server - Workflow Engine**

**Server - Workflow Engine**

.. i18n: Workflows are graphs represented by business objects that describe the dynamics of the company. Workflows are also used to track processes that evolve over time.

Workflows are graphs represented by business objects that describe the dynamics of the company. Workflows are also used to track processes that evolve over time.

.. i18n: An example of workflow used in Open ERP:

An example of workflow used in Open ERP:

.. i18n: A sales order generates an invoice and a shipping order

A sales order generates an invoice and a shipping order

.. i18n: **Server - Report Engine**

**Server - Report Engine**

.. i18n: Reports in Open ERP can be rendered in different ways:

Reports in Open ERP can be rendered in different ways:

.. i18n:     * Custom reports: those reports can be directly created via the client interface, no programming required. Those reports are represented by business objects (ir.report.custom)
.. i18n:     * High quality personalized reports using openreport: no programming required but you have to write 2 small XML files:
.. i18n: 
.. i18n:           - a template which indicates the data you plan to report
.. i18n:           - an XSL:RML stylesheet 
.. i18n:     * Hard coded reports
.. i18n:     * OpenOffice Writer templates 

    * Custom reports: those reports can be directly created via the client interface, no programming required. Those reports are represented by business objects (ir.report.custom)
    * High quality personalized reports using openreport: no programming required but you have to write 2 small XML files:

          - a template which indicates the data you plan to report
          - an XSL:RML stylesheet 
    * Hard coded reports
    * OpenOffice Writer templates 

.. i18n: Nearly all reports are produced in PDF.

Nearly all reports are produced in PDF.

.. i18n: **Server - Business Objects**

**Server - Business Objects**

.. i18n: Almost everything is a business object in Open ERP, they described all data of the program (workflows, invoices, users, customized reports, ...). Business objects are described using the ORM module. They are persistent and can have multiple views (described by the user or automatically calculated).

Almost everything is a business object in Open ERP, they described all data of the program (workflows, invoices, users, customized reports, ...). Business objects are described using the ORM module. They are persistent and can have multiple views (described by the user or automatically calculated).

.. i18n: Business objects are structured in the /module directory.

Business objects are structured in the /module directory.

.. i18n: **Client - Wizards**

**Client - Wizards**

.. i18n: Wizards are graphs of actions/windows that the user can perform during a session.

Wizards are graphs of actions/windows that the user can perform during a session.

.. i18n: **Client - Widgets**

**Client - Widgets**

.. i18n: Widgets are probably, although the origin of the term seems to be very difficult to trace, "WIndow gaDGETS" in the IT world, which mean they are gadgets before anything, which implement elementary features through a portable visual tool.

Widgets are probably, although the origin of the term seems to be very difficult to trace, "WIndow gaDGETS" in the IT world, which mean they are gadgets before anything, which implement elementary features through a portable visual tool.

.. i18n: All common widgets are supported:

All common widgets are supported:

.. i18n:     * entries
.. i18n:     * textboxes
.. i18n:     * floating point numbers
.. i18n:     * dates (with calendar)
.. i18n:     * checkboxes
.. i18n:     * ... 

    * entries
    * textboxes
    * floating point numbers
    * dates (with calendar)
    * checkboxes
    * ... 

.. i18n: And also all special widgets:

And also all special widgets:

.. i18n:     * buttons that call actions
.. i18n:     * references widgets
.. i18n: 
.. i18n:           - one2one
.. i18n: 
.. i18n:           - many2one
.. i18n: 
.. i18n:           - many2many
.. i18n: 
.. i18n:           - one2many in list
.. i18n: 
.. i18n:           - ... 

    * buttons that call actions
    * references widgets

          - one2one

          - many2one

          - many2many

          - one2many in list

          - ... 

.. i18n: Widget have different appearances in different views. For example, the date widget in the search dialog represents two normal dates for a range of date (from...to...).

Widget have different appearances in different views. For example, the date widget in the search dialog represents two normal dates for a range of date (from...to...).

.. i18n: Some widgets may have different representations depending on the context. For example, the one2many widget can be represented as a form with multiple pages or a multi-columns list.

Some widgets may have different representations depending on the context. For example, the one2many widget can be represented as a form with multiple pages or a multi-columns list.

.. i18n: Events on the widgets module are processed with a callback mechanism. A callback mechanism is a process whereby an element defines the type of events he can handle and which methods should be called when this event is triggered. Once the event is triggered, the system knows that the event is bound to a specific method, and calls that method back. Hence callback. 

Events on the widgets module are processed with a callback mechanism. A callback mechanism is a process whereby an element defines the type of events he can handle and which methods should be called when this event is triggered. Once the event is triggered, the system knows that the event is bound to a specific method, and calls that method back. Hence callback. 
