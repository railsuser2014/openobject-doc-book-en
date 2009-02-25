
.. index::
   single: Deployment
..

Deployment
==========

As you've seen the complete architecture of Open ERP includes the following elements:

* a database server,

* an Open ERP application server,

* an Open ERP client-web server,

* several clients that access the Open ERP server: they can either be web clients if the client-web
  server is installed, or GTK clients.


.. note:: Deployment

	Deployment is the process of putting a Open ERP database into a production-ready state,
	where it can be used by everyone in your business for their daily work.
	You'd usually configure Open ERP and load data into it on one development system,
	train staff on that or another training system and
	deploy it onto a production system that has better protection against failure, better security and
	more performance.

Deployment Options
------------------

To deploy Open ERP in your company, several options are available to you:

* an SaaS (Software as a Service) or on Demand offer which includes the equipment, the hosting, the
  maintenance and the support on a system configured to your needs in advance,

* an internal installation, that you manage yourselves or have managed by an IT services company
  such as an Open ERP partner,

* hosting by a server supplier on which Open ERP is installed, which enables you to proceed to add
  adaptations on your server.

The first two approaches are the most commonly used.

The SaaS (Software as a Service) offer
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

SaaS is a complete package hosted at a supplier, that includes the following services: server
hardware, hosting of the generic solution, installation and initial configuration, redundancy of the
architecture, backups, system maintenance and support.

It's provided in the form of a monthly subscription with a fixed price per user. You can find the
detail of available SaaS packages at .

SaaS packages don't permit you to develop specific modules to your needs. On the contrary, they
offer a service at a set price based on standard software modules that contain few migration risks.
SaaS suppliers are limited generally to the modules certified and validated by the original author
and project manager, Tiny.

Here are the main advantages of an Open ERP SaaS solution:

* an unbeatable return on investment (cost of implementation: 0, cost of licenses: 0),

* costs that are controlled and without surprises (the offer includes maintenance, frequent
  migrations and support),

* a turnkey solution, installed in less than twenty-four hours,

* packages adapted and preconfigured for different sectors of activity,

* a very robust architecture guaranteed to have constant and permanent access, reachable from
  anywhere.

So this server is recommended for small companies with fewer than about fifteen employees.

Hosting by a supplier
^^^^^^^^^^^^^^^^^^^^^

At first sight a hosted Open ERP system appears similar to SaaS: it provides Open ERP from a
remote installation through a web browser. But in general the similarities stop there.

To compare it with an SaaS package you should check if the hosting offer properly includes the
following elements:

* server hardware,

* hosting,

* maintenance,

* future migrations,

* backups,

* server redundancy,

* telephone and email support,

* frequent updates to the modules.

Also get yourself up to speed on the following points:

* the version of Open ERP proposed,

* the costs of implementation (configuration, data loading, training),

* the cost of configuration (if it's proposed),

* the technology and the procedure used for securing your database,

* the technology and the procedure for preventing system faults,

* the technology and the procedure for restoring a faulty system,

* limitations on the number of users, the number of simultaneous users, and the size of the
  database,

* the level of support and its costs,

* the procedure used to update Open ERP (to fault-fixed versions)

* the procedure adopted for Open ERP upgrades (to versions that have both fault fixes and new
  functionality).

Calling such suppliers can be a good solution if you are willing to entrust all the technical
specifications for the functioning of Open ERP to them, especially if you need to use customized or
extension modules that aren't in the stable version released by Tiny.

Internal Installation
^^^^^^^^^^^^^^^^^^^^^

Large and medium-large companies typically install Open ERP using their own internal company
resources. They usually prefer to have their own IT service in charge of maintenance.

Such companies can do the implementation work themselves internally, or turn to an Open ERP partner
who will do the ERP implementation work or assist them with it. Generally companies prefer to adopt
an intermediate solution which consists of:

	#. Turn the initial implementation over to a partner to limit the risks and delays of integration.
		That enables them to be managed by experts and to obtain a high quality configuration.

	#. Take charge of the simple needs for themselves once the software has been implemented. It's
		quite a lot more convenient for them to be able to modify the database tables, forms, templates and
		workflows internally than routinely depend on a supplier.

An internal installation will probably prove more costly than an SaaS package or hosted service.
Even if you put yourself in charge of it all, you'll take quite a bit of time learning how to manage
the implementation unless the team already has experience of Open ERP. This represents a
significant risk.

However, an internal implementation can be particularly interesting where:

* you want to keep your data within your company,

* you think you want to modify your software,

* you want a specific package of modules,

* you'd like a very fast response time,

* you want the software to be available even if your Internet connection goes down.

These factors, and access to the resources needed to handle an implementation and the subsequent
maintenance, are the reasons that large and medium-large companies usually do it for themselves, at
least partly.

Deployment Procedure
--------------------

The deployment of a version of Open ERP is quite simple when your server has been configured in
your production environment. The security of the data will then be a key element.

When you've installed the server you should create at least two databases:

* a test or development database, in which the users can test the system and familiarize themselves
  with it,

* a production database which will be the one used by the company in daily use.

.. note::  Version numbering

	Open ERP uses a version numbering model that comprises 3 numbers A.B.C (for example 4.2.2 or
	5.0.0) where changes in the number A signify a major functional change, changes to number B signify
	an update that includes a batch of fault fixes and some new functionality, and the number C
	generally refers to some limited updates or fixes to the existing functionality.

	The number B is special: if it's an odd number, (for example 4.3.2 or 5.1.0) it's for a development
	version which isn't designed for a production environment. The even numbers are for stable
	versions.

If you have prepared a data module for Open ERP (that is a module that consists just of data, not
altered functionality), you should test it in your development version and check that it doesn't
require any more manual adjustments. If the import runs correctly, it shows that you're ready to
load your data in the production database.

You can use the Open ERP database backup procedure at different stages of configuration (see
Chapter 1). Then if you've made a false step that you can't recover from you can always return to a
prior state.

Since your data describes much of your company's value, take particular care both when you need to
transfer it (in backups and across your network) and when you're managing the super-administrator
password. Make sure that the connection between a PC client and the two servers is correctly
secured. You can configure Open ERP to use the HTTPS protocol, which provides security for data
transfer

.. index::
   single: HTTPS

.. note:: HTTPS

	The HTTPS protocol (Secured Hyper Text Transfer Protocol) is the standard HTTP protocol secured by
	using the SSL (Secure Socket Layer) or TLS (Transport Layer Security) security protocols.
	It allows a user to verify her identify to the site to which she wants access, using a certificate
	of authentication.
	It also guarantees the integrity and confidentiality of the data sent between the user and the
	server.
	It can, optionally, provide highly secure client authentication by using a numbered certificate.

	The default HTTPS port is 443.

You could also use the PostgreSQL database directly to backup and restore data on the server,
depending on access rights and the availability of passwords for the serve.



.. Copyright © Open Object Press. All rights reserved.

.. You may take electronic copy of this publication and distribute it if you don't
.. change the content. You can also print a copy to be read by yourself only.

.. We have contracts with different publishers in different countries to sell and
.. distribute paper or electronic based versions of this book (translated or not)
.. in bookstores. This helps to distribute and promote the Open ERP product. It
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


