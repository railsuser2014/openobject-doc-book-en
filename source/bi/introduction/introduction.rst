
Introduction
============

The Open Object Business Intelligence system aims to be a full featured open source Business Intelligence system written in Python. It implements a HOLAP (Hybride OLAP = ROLAP + MOLAP) cube and a MDX query engine based on SQLAlchemy.

Comparing to most current business intelligence software in the market, our goal is to produce a BI for the mid market. It has to be:

For the end-user:
-----------------

* Is easy and fast to use: a simple web-interface that does not require any dependencies and can be integrated in proprietary softwares, and an OpenOffice interface for complex dashboards creation.
* Is easy to install: auto-installation on Windows and Linux, a few dependencies
* Integrated and independent from Tiny ERP. 

For the administrator user:
---------------------------

* A cube designer within Tiny ERP (application and web-client)
* Easy to configure: Automatic cube definition (5 clicks, using introspection on database),
* Easy to maintain: the application must be smart enough that do not require any fine tuning in the cube definition: run well on bad indexes, no need to explicitly define aggregated table, no need to define axes.
* No intervention at all from developers: everything through interfaces for end-user. 

For the developer:
------------------

* Everything (dimensions, ) must be object oriented with a module system to allow to add your own code to extend the software, like in Tiny ERP.
* It must support main database engine and aggregation of multiple database: PostgreSQL, MySQL, Oracle, MSSQL etc... to do reporting for any application.


.. Copyright © Open Object Press. All rights reserved.

.. You may take electronic copy of this publication and distribute it if you don't
.. change the content. You can also print a copy to be read by yourself only.

.. We have contracts with different publishers in different countries to sell and
.. distribute paper or electronic based versions of this book (translated or not)
.. in bookstores. This helps to distribute and promote the Open ERP product. It
.. also helps us to create incentives to pay contributors and authors using author
.. rights of these sales.

.. Due to this, grants to translate, modify or sell this book are strictly
.. forbidden, unless Tiny SPRL (representing Open Object Presses) gives you a
.. written authorisation for this.

.. Many of the designations used by manufacturers and suppliers to distinguish their
.. products are claimed as trademarks. Where those designations appear in this book,
.. and Open ERP Press was aware of a trademark claim, the designations have been
.. printed in initial capitals.

.. While every precaution has been taken in the preparation of this book, the publisher
.. and the authors assume no responsibility for errors or omissions, or for damages
.. resulting from the use of the information contained herein.

.. Published by Open ERP Press, Grand Rosière, Belgium


