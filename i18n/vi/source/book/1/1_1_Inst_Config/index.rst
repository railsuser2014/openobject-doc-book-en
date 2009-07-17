
.. i18n: .. index::
.. i18n:    single: Installation
.. i18n:    single: Initial Setup
.. i18n:    pair: configuration; setup

.. index::
   single: Installation
   single: Initial Setup
   pair: configuration; setup

.. i18n: .. _ch-inst:
.. i18n: 
.. i18n: ******************************
.. i18n: Installation and Initial Setup
.. i18n: ******************************

.. _ch-inst:

******************************
Installation and Initial Setup
******************************

.. i18n:  *Installing Open ERP under Windows or Linux for familiarization use should take you only half an
.. i18n:  hour or so and needs only a couple of operations.*
.. i18n:  
.. i18n:  *The first operation is installation of the application and database server on a server PC (that's
.. i18n:  a Windows or Linux or Macintosh computer).*

 *Installing Open ERP under Windows or Linux for familiarization use should take you only half an
 hour or so and needs only a couple of operations.*
 
 *The first operation is installation of the application and database server on a server PC (that's
 a Windows or Linux or Macintosh computer).*

.. i18n:  *You've a choice of approaches for the second operation:
.. i18n:  either install a web server (most probably on the original server PC) to use with standard web
.. i18n:  clients that can be found on anybody's PC, or install application clients on each intended user's PC.*
.. i18n:  
.. i18n: When you first install Open ERP you'll set up a database containing a little functionality and
.. i18n: some demonstration data to test the installation.
.. i18n:  
.. i18n: .. index::
.. i18n:    single: Tiny ERP

 *You've a choice of approaches for the second operation:
 either install a web server (most probably on the original server PC) to use with standard web
 clients that can be found on anybody's PC, or install application clients on each intended user's PC.*
 
When you first install Open ERP you'll set up a database containing a little functionality and
some demonstration data to test the installation.
 
.. index::
   single: Tiny ERP

.. i18n: .. note:: Renaming from Tiny ERP to Open ERP
.. i18n: 
.. i18n:    Tiny ERP was renamed to Open ERP early in 2008 so somebody who's already used Tiny ERP should be
.. i18n:    equally at home with Open ERP. The two names refer to the same software, so there's no
.. i18n:    functional difference between versions 4.2.X of Open ERP and 4.2.X of Tiny ERP. This book
.. i18n:    applies to versions of Open ERP from 5.0.0 onwards, with references to earlier versions from
.. i18n:    time to time.

.. note:: Renaming from Tiny ERP to Open ERP

   Tiny ERP was renamed to Open ERP early in 2008 so somebody who's already used Tiny ERP should be
   equally at home with Open ERP. The two names refer to the same software, so there's no
   functional difference between versions 4.2.X of Open ERP and 4.2.X of Tiny ERP. This book
   applies to versions of Open ERP from 5.0.0 onwards, with references to earlier versions from
   time to time.

.. i18n: .. index::
.. i18n:    single:SaaS

.. index::
   single:SaaS

.. i18n: .. note:: The SaaS, or “on-demand”, offer
.. i18n: 
.. i18n:    SaaS (Software as a Service) is delivered by a hosting supplier and paid in the form of a monthly
.. i18n:    subscription that
.. i18n:    includes hardware (servers), system maintenance, provision of hosting services, and support.
.. i18n: 
.. i18n:    You can get a month's free trial on Tiny's http://ondemand.openerp.com, which enables you to get
.. i18n:    started quickly
.. i18n:    without incurring costs for integration or for buying computer systems.
.. i18n:    Many of Tiny's partner companies will access this, and some may offer their own similar service.
.. i18n: 
.. i18n:    This service should be particularly useful to small companies that just want to get going quickly
.. i18n:    and at low cost.
.. i18n:    It gives them immediate access to an integrated management system that's been built on the type
.. i18n:    of enterprise architecture
.. i18n:    used in banks and other large organizations.
.. i18n:    Open ERP is that system, and is described in detail throughout this book.

.. note:: The SaaS, or “on-demand”, offer

   SaaS (Software as a Service) is delivered by a hosting supplier and paid in the form of a monthly
   subscription that
   includes hardware (servers), system maintenance, provision of hosting services, and support.

   You can get a month's free trial on Tiny's http://ondemand.openerp.com, which enables you to get
   started quickly
   without incurring costs for integration or for buying computer systems.
   Many of Tiny's partner companies will access this, and some may offer their own similar service.

   This service should be particularly useful to small companies that just want to get going quickly
   and at low cost.
   It gives them immediate access to an integrated management system that's been built on the type
   of enterprise architecture
   used in banks and other large organizations.
   Open ERP is that system, and is described in detail throughout this book.

.. i18n: Whether you want to test Open ERP or to put it into full production, you have at least two starting
.. i18n: points:

Whether you want to test Open ERP or to put it into full production, you have at least two starting
points:

.. i18n: * evaluate it on line at http://www.openerp.com and ask Tiny for an SaaS trial hosted at
.. i18n:   http://ondemand.openerp.com, or the equivalent service at any of Tiny's partner companies,
.. i18n: 
.. i18n: * install it on your own computers to test it in your company's systems environment.

* evaluate it on line at http://www.openerp.com and ask Tiny for an SaaS trial hosted at
  http://ondemand.openerp.com, or the equivalent service at any of Tiny's partner companies,

* install it on your own computers to test it in your company's systems environment.

.. i18n: There are some differences between installing Open ERP on Windows and on Linux systems, but once
.. i18n: installed, it gives the same functions from both so you won't generally be able to tell which type
.. i18n: of server you're using.

There are some differences between installing Open ERP on Windows and on Linux systems, but once
installed, it gives the same functions from both so you won't generally be able to tell which type
of server you're using.

.. i18n: .. note:: Linux, Windows, Mac
.. i18n: 
.. i18n:    Although this book deals only with installation on Windows and Linux systems, the same versions
.. i18n:    are also available for the Macintosh on the official website of Open ERP.

.. note:: Linux, Windows, Mac

   Although this book deals only with installation on Windows and Linux systems, the same versions
   are also available for the Macintosh on the official website of Open ERP.

.. i18n: .. note:: Web sites for Open ERP
.. i18n: 
.. i18n:    * Main Site: http://www.openerp.com,
.. i18n: 
.. i18n:    * SaaS or “on-demand” Site: http://ondemand.openerp.com,
.. i18n: 
.. i18n:    * Documentation Site: http://doc.openerp.com/,
.. i18n: 
.. i18n:    * Community discussion forum where you can often receive informed assistance:
.. i18n:      http://www.openobject.com/forum.

.. note:: Web sites for Open ERP

   * Main Site: http://www.openerp.com,

   * SaaS or “on-demand” Site: http://ondemand.openerp.com,

   * Documentation Site: http://doc.openerp.com/,

   * Community discussion forum where you can often receive informed assistance:
     http://www.openobject.com/forum.

.. i18n: .. tip:: Current documentation
.. i18n: 
.. i18n:    The procedure for installing Open ERP and its web server are sure to change and improve with
.. i18n:    each new version, so you should always check each release's documentation – both packaged with
.. i18n:    the release and on the website – for exact installation procedures.

.. tip:: Current documentation

   The procedure for installing Open ERP and its web server are sure to change and improve with
   each new version, so you should always check each release's documentation – both packaged with
   the release and on the website – for exact installation procedures.

.. i18n: Once you've completed this installation, create and set up a database to confirm that your
.. i18n: Open ERP installation is working. You can follow these early chapters in this part of the book to achieve this.

Once you've completed this installation, create and set up a database to confirm that your
Open ERP installation is working. You can follow these early chapters in this part of the book to achieve this.

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <div class="all-toctree">

.. raw:: html

    <div class="all-toctree">

.. i18n: .. toctree::
.. i18n: 
.. i18n:    1_1_Inst_Config_architecture
.. i18n:    1_1_Inst_Config_install
.. i18n:    1_1_Inst_Config_db_create

.. toctree::

   1_1_Inst_Config_architecture
   1_1_Inst_Config_install
   1_1_Inst_Config_db_create

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     </div>

.. raw:: html

    </div>

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
