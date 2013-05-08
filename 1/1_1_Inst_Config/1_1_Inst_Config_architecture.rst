
.. index::
   single: architecture; OpenERP

The Architecture of OpenERP
===========================

To access OpenERP V7 you can:

* use only a web browser pointed at the OpenERP client-web server.

It is best to use the web browser if the OpenERP server is some distance away 
(such as on another continent) because it is more tolerant of time delays.
The web client is also easier to maintain, because it is generally already installed on users' computers.

.. index::
   single: client; web (thin) and GTK (thick)
   single: client; caching

An OpenERP system is formed from three main components:

* the PostgreSQL database server, which contains all of the databases, each of which contains all
  data and most elements of the OpenERP system configuration,

* the OpenERP application server, which contains all of the enterprise logic and ensures that
  OpenERP runs optimally,

* the web server, a separate application called the Open Object client-web, which enables you to
  connect to OpenERP from standard web browsers.

.. figure:: images/terp_arch_1.png
   :align: center
   :scale: 90
   
   *The architecture of OpenERP*

.. note::   Terminology: Client-web – Server or Client?

    The client-web component can be thought of as a server or a client depending on
    your viewpoint.

    It acts as a web server to an end user connecting from a web browser, but
    it also acts as a client to the OpenERP application server.

    So in this book its context will determine whether the client-web component is referred to as
    a server or a client.

.. index::
   pair: eTiny; client-web

.. index::
   single: PostgreSQL

.. note::   PostgreSQL, the relational and object database management system.

    It is a free and open-source high-performance system that compares well with other database
    management systems such as MySQL and FirebirdSQL (both free), Sybase, DB2
    and Microsoft SQL Server (all proprietary). It runs on all types of
    Operating System, from Unix/Linux to the various releases of Windows, via
    Mac OS X, Solaris, SunOS and BSD.

These three components can be installed on the same server or can be
distributed onto separate computer servers, if performance considerations
require it.

.. Copyright © Open Object Press. All rights reserved.

.. You may take electronic copy of this publication and distribute it if you don't
.. change the content. You can also print a copy to be read by yourself only.

.. We have contracts with different publishers in different countries to sell and
.. distribute paper or electronic based versions of this book (translated or not)
.. in bookstores. This helps to distribute and promote the OpenERP product. It
.. also helps us to create incentives to pay contributors and authors using author
.. rights of these sales.

.. Due to this, grants to translate, modify or sell this book are strictly
.. forbidden, unless Tiny SPRL (representing Open Object Press) gives you a
.. written authorisation for this.

.. Many of the designations used by manufacturers and suppliers to distinguish their
.. products are claimed as trademarks. Where those designations appear in this book,
.. and Open Object Press was aware of a trademark claim, the designations have been
.. printed in initial capitals.

.. While every precaution has been taken in the preparation of this book, the publisher
.. and the authors assume no responsibility for errors or omissions, or for damages
.. resulting from the use of the information contained herein.

.. Published by Open Object Press, Grand Rosière, Belgium

