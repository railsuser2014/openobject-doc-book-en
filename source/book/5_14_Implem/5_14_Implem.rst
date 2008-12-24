

Implementation Methodology
###########################

Summary

* Planning Open ERP's implementation

* Deployment options

* User training

* Maintenance and support

Keywords

* implementation

* integration

* deployment

* SaaS

* training

* migration

 *You may have mastered the technical aspects of administering and using your enterprise management system, but you still have a great deal of work to do integrating Open ERP into your company. This work is more business-related and social in nature than technical. The Open ERP implementation process encompasses several different phases: evaluation, planning, configuration, data migration, deployment, and user training, and impacts both support and maintenance* 



The management of ERP projects, and IT project management in general, are the subject of very many other books that you might want to investigate for yourself. The elements of the methodology presented here aren't intended to be an exhaustive review, just a brief overview of the different phases necessary to implement Open ERP in your company

.. tip::   **Definition**  *Implementation* 

	Implementation encompasses the whole process of integrating and deploying Open ERP, including evaluating it, establishing specifications, planning the deployment, the configuration of the software, loading data, installation and training the users. It doesn't really extend to software customization, nor support and maintenance.

Requirements Analysis and Planning
===================================

Requirements analysis and planning are the keys to the success of an implementation. At this stage you should set up a management team to define the costs and benefits of the project, select a project team, and set out the detailed stages that will have to be carried out.

Open ERP is so easy to start using that it's not always obvious, particularly to IT staff, that a clear requirements plan is necessary for implementing the system successfully. The difficulty isn't particularly in installing the software nor in configuring it, but rather more about:

* knowing what to configure,

* deciding if you should adapt the software or perhaps change your method of working, for some of your specialized processes,

* forming teams that can specify and work on some of the changes,

* ensuring that your users are committed to the change.

ERP system implementation is a project carried out using information technology but it's a business project rather than an IT project in itself. The challenge of this type of project is in changing the behaviour of those involved at all levels of the enterprise. 

People in the IT department will certainly be an integral part of the project but they should be managed by someone in a senior position who both understands the business impact across the organization and has experience of technical projects. Ideally the project manager should know the company well, both its specific quirks and its different standard cross-company processes.

If the enterprise doesn't have its own IT group, you're probably better off opting for an SaaS offer. This means that you subcontract all the difficult technology, from the installation of the server to its maintenance, all the while being assured of the installation of a robust architecture with its redundancy, backed-up servers, and separation of authentication and data.

.. tip::   **Reminder**  *The SaaS offer* 

	SaaS (Software as a Service) offers are hosted by a supplier in the form of a monthly subscription which includes all the IT material (servers), system maintenance, hosting and support.

	You can obtain a month's free trial from http://ondemand.openerp.com/, which lets you start rapidly without any integration cost or material to buy, or you can ask one of Tiny's partners for access to this or their own services.

	This service can be particularly useful to small companies who want to grow their integrated management system rapidly, at low cost, based on the same robust general system architecture as that used by large banks.

Planning methods
-----------------

Planning methods vary in their degree of complexity, formality and level of automation. It's not the intention of this chapter to steer you towards one method or the other.

Open ERP's menus are organized to lead you through an implementation in a sensible order, so that information that has to be entered first is encountered first in the menu system. Forms are also organized so that if you enter data in the natural order you'll get later fields completed automatically by the earlier ones where possible. And demonstration data illustrates how Open ERP's functional areas are linked from one to the other

The menus themselves hint at several helpful implementation suggestions, for example the submenus of *Administration > Configuration* are useful for the configuration of the software. New functions such as the Module Recorder enable you to significantly accelerate the configuration of data.

External modules, such as the Implementation Planner module \ ``implem``\   which helps you develop high level implementation plans are also being produced by third-party developers. These plans, designed for managing or investigating Open ERP, detail the software structure and the different steps required by your implementation.

Deployment
===========

As you've seen the complete architecture of Open ERP includes the following elements:

* a database server,

* an Open ERP application server,

* an eTiny web server,

* several clients that access the Open ERP server: they can either be web clients if the eTiny web server is installed, or GTK clients.

.. tip::   **Definition**  *Deployment* 

	Deployment is the process of putting a Open ERP database into a production-ready state, where it can be used by everyone in your business for their daily work. You'd usually configure Open ERP and load data into it on one development system, train staff on that or another training system and deploy it onto a production system that has better protection against failure, better security and more performance.

Deployment Options
-------------------

To deploy Open ERP in your company, several options are available to you:

* an SaaS (Software as a Service) or on Demand offer which includes the equipment, the hosting, the maintenance and the support on a system configured to your needs in advance,

* an internal installation, that you manage yourselves or have managed by an IT services company such as an Open ERP partner,

* hosting by a server supplier on which Open ERP is installed, which enables you to proceed to add adaptations on your server.

The first two approaches are the most commonly used.

The SaaS (Software as a Service) offer
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

SaaS is a complete package hosted at a supplier, that includes the following services: server hardware, hosting of the generic solution, installation and initial configuration, redundancy of the architecture, backups, system maintenance and support.

It's provided in the form of a monthly subscription with a fixed price per user. You can find the detail of available SaaS packages at .

SaaS packages don't permit you to develop specific modules to your needs. On the contrary, they offer a service at a set price based on standard software modules that contain few migration risks. SaaS suppliers are limited generally to the modules certified and validated by the original author and project manager, Tiny.

Here are the main advantages of an Open ERP SaaS solution:

* an unbeatable return on investment (cost of implementation: 0, cost of licenses: 0),

* costs that are controlled and without surprises (the offer includes maintenance, frequent migrations and support),

* a turnkey solution, installed in less than twenty-four hours,

* packages adapted and preconfigured for different sectors of activity,

* a very robust architecture guaranteed to have constant and permanent access, reachable from anywhere.

So this servr is recommended for small companies with fewer than about fifteen employees.

Hosting by a supplier
^^^^^^^^^^^^^^^^^^^^^^^

At first sight a hosted Open ERP system appears similar to SaaS: it provides Open ERP from a remote installation through a web browser. But in general the similarities stop there.

To compare it with an SaaS package you should check if the hosting offer properly includes the following elements:

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

* the cost of personalization (if it's proposed),

* the technology and the procedure used for securing your database,

* the technology and the procedure for preventing system faults,

* the technology and the procedure for restoring a faulty system,

* limitations on the number of users, the number of simultaneous users, and the size of the database,

* the level of support and its costs,

* the procedure used to update Open ERP (to fault-fixed versions)

* the procedure adopted for Open ERP upgrades (to versions that have both fault fixes and new functionality).

Calling such suppliers can be a good solution if you are willing to entrust all the technical specifications for the functioning of Open ERP to them, especially if you need to use customized or extension modules that aren't in the stable version released by Tiny.

Internal Installation
^^^^^^^^^^^^^^^^^^^^^^^

Large and medium-large companies typically install Open ERP using their own internal company resources. They usually prefer to have their own IT service in charge of maintenance.

Such companies can do the implementation work themselves internally, or turn to an Open ERP partner who will do the ERP implementation work or assist them with it. Generally companies prefer to adopt an intermediate solution which consists of:

	#. Turn the initial implementation over to a partner to limit the risks and delays of integration. That enables them to be managed by experts and to obtain a high quality configuration.

	#. Take charge of the simple needs for themselves once the software has been implemented. It's quite a lot more convenient for them to be able to modify the database tables, forms, templates and workflows internally than routinely depend on a supplier.

An internal installation will probably prove more costly than an SaaS package or hosted service. Even if you put yourself in charge of it all, you'll take quite a bit of time learning how to manage the implementation unless the team already has experience of Open ERP. This represents a significant risk.

However, an internal implementation can be particularly interesting where:

* you want to keep your data within your company,

* you think you want to modify your software,

* you want a specific package of modules,

* you'd like a very fast response time,

* you want the software to be available even if your Internet connection goes down.

These factors, and access to the resources needed to handle an implementation and the subsequent maintenance, are the reasons that large and medium-large companies usually do it for themselves, at least partly.

Deployment Procedure
---------------------

The deployment of a version of Open ERP is quite simple when your server has been configured in your production environment. The security of the data will then be a key element.

When you've installed the server you should create at least two databases:

* a test or development database, in which the users can test the system and familiarize themselves with it,

* a production database which will be the one used by the company in daily use.

.. tip::   **Note**  *Version numbering* 

	Open ERP uses a version numbering model that comprises 3 numbers A.B.C (for example 4.2.2) where changes in the number A signify a major functional change, changes to number B signify an update that includes a batch of fault fixes and some new functionality, and the number C generally refers to some limited updates or fixes to the existing functionality.

	The number B is notable: if it's an odd number, (for example 4.3.0) it's for a development version which isn't designed for a production environment. The even numbers are for stable versions.

If you have prepared a data module for Open ERP (that is a module that consists just of data, not altered functionality), you should test it in your development version and check that it doesn't require any more manual adjustments. If the import runs correctly, it shows that you're ready to load your data in the production database.

You can use the Open ERP database backup procedure at different stages of configuration (see Chapter 1). Then if you've made a false step that you can't recover from you can always return to a prior state.

Since your data describes much of your company's value, take particular care both when you need to transfer it (in backups and across your network) and when you're managing the super-administrator password. Make sure that the connection between a PC client and the two servers is correctly secured. You can configure Open ERP to use the HTTPS protocol, which provides security for data transfer

.. tip::   **Definition**  *HTTPS* 

	The HTTPS protocol (Secured Hyper Text Transfer Protocol) is the standard HTTP protocol secured by using the SSL (Secure Socket Layer) or TLS (Transport Layer Security) security protocols. It allows a user to verify her identify to the site to which she wants access, using a certificate of authentication. It also guarantees the integrity and confidentiality of the data sent between the user and the server. It can, optionally, provide highly secure client authentication by using a numbered certificate.

	The default HTTPS port is 443.

You could also use the PostgreSQL database directly to backup and restore data on the server, depending on access rights and the availability of passwords for the serve.

User training
===============

Two types of training are provided by the Tiny company and its partners:

* Technical training in Open ERP: the objective of this intensive training is to enable you to develop your own modules by modifying and adapting the existing ones. It covers the creation of new objects, menus, reports and workflows, and also of interfaces with external software. It lasts for five days and is designed for IT people

* User training: this enables you to be productive as rapidly as possible in the use of Open ERP. All of the modules there are detailed with concrete examples and different exercises. For the sake of realism the training uses data for a fictitious company. This training also lasts for five days. It is designed for those responsible for an ERP project, who will then be capable of training employees internally.

Tiny's training calendar is available on the official Open ERP site  by clicking the menu  *Services > Trainin* g. The training is delivered in either French or English depending on the course.

Both Tiny, the creators of Open ERP, and the Open ERP partners can also provide customized training. This, although more expensive, is focused on your own needs.

Your training needs depend on the type of deployment you've chosen. If you have opted for an SaaS development, technical training isn't very useful.

In summary, you should arrange both user training and self-paced training (perhaps based on this book) if you can. Technical training is strongly advised if you see yourselves developing your own modules. Although it's not obligatory it gives you quite a time advantage in any serious Open ERP engagement.

Support and maintenance
=========================

It's when you actually use your ERP that you will obtain value from your investment. For that reason maintenance and support are critical for your long term success.

* Support aims to ensure that end users get the maximum productivity from their use of Open ERP by responding to their questions on the use of the system. Support can be technical or functional.

* Maintenance aims to ensure that the system itself continues to function as required. It includes system upgrades, which give you access to the latest functionality available.

Some partners offer preventative maintenance. This makes sure that all the specific developments for your system are revised and tested for each new version so that they remain compatible with the base Open ERP.

If you haven't anticipated your needs with a preventive maintenance contract, the costs of migration after a few years can become significant. If special modules that you developed have been allowed to become too old you may eventually need a new development to your specifications.

Updates and Upgrades
---------------------

There are four sources of code change for Open ERP:

* patches supplied by Tiny to correct faults: after validation these patches won't cause any secondary effects,

* minor updates, which gather the fault corrections together in one package, and are generally announced with a modification of the version number, such as from 4.2.0 to 4.2.1,

* upgrades, which bundle both the fault corrections and the improvements to the functionality in a major release such as from 4.0.3 to 4.2.0.

* new functions generally released in the form of new modules.

You should establish a procedure with your supplier to define how to respond to changes in the Open ERP code.

For simple updates your maintenance team will evaluate the patches to determine if they are beneficial to the use of your Open ERP. These patches should be tested on an offline instance of Open ERP before being installed in your live production version.

The maintenance team would also take charge of regular updates to the software.

Patches and updates can only be installed if you have the necessary access to the Open ERP server. You must first install the patch or update and then restart the server using the command line: \ ``–update=all``\  .

Once Tiny has released a new upgraded version your response should be a cautious one. If you're perfectly satisfied with the existing system it would be best to not touch the new version. If you want to have access to the new functionality supplied by an upgraded version, you have a delicate operation to carry out. Most upgrades require your data to be migrated because the databases before and after the upgrade can be a little different.

Version Migration
-------------------

Open ERP has a system to manage migrations automatically. To update specific modules, or the whole database, you only need to start the server with the argument:–\ ``update=NAME_OF_MODULE``\   or \ ``–update=all``\  ..

New stable versions of Open ERP sometimes require operations that aren't provided in the automated migration. Tiny, the creator and maintainer of Open ERP, has a policy of supporting migration from all official stable releases to the latest. Scripts are provided for each new release of a stable version. These carry out the upgrade from the previous major version to the new major version.

The managers responsible for the migration between two versions of Open ERP will find the documentation and the necessary scripts in the directory \ ``doc/migrate``\   of the Open ERP server.

The procedure for migrating runs like this:

	#. Make a backup of the database from the old version of Open ERP

	#. Stop the server running the old version

	#. Start the script called \ ``pre.py``\  for the versions you're moving between.

	#. Start the new version of the server using the option –\ ``update=all``\  

	#. Stop the server running the new version.

	#. Start the script called post.py for the versions you're moving between.

	#. Start the new version of the server and test it.

A migration is never an easy process. It may be that your system doesn't function as it did before or that something requires new developments in the functionality of the modules that have already been installed. So you should only move to a new version if you have a real need and should engage a competent partner to help if the version that you use differs greatly from the basic version of Open ERP.

Similarly you should take care that this migration does not correct any setting that was done incorrectly. It's can be the case, for example, that the main menu structure has been modified without recording it. You may find that you're making the wrong assumptions about that structure when loading data in that was recorded with the Module Recorder.



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

