
.. i18n: .. index::
.. i18n:    single: maintenance
.. i18n:    single: support

.. index::
   single: maintenance
   single: support

.. i18n: Support and maintenance
.. i18n: =======================

Support and maintenance
=======================

.. i18n: It's when you actually use your ERP that you will obtain value from your investment. For that reason
.. i18n: maintenance and support are critical for your long term success.

It's when you actually use your ERP that you will obtain value from your investment. For that reason
maintenance and support are critical for your long term success.

.. i18n: * Support aims to ensure that end users get the maximum productivity from their use of Open ERP by
.. i18n:   responding to their questions on the use of the system. Support can be technical or functional.
.. i18n: 
.. i18n: * Maintenance aims to ensure that the system itself continues to function as required. It includes
.. i18n:   system upgrades, which give you access to the latest functionality available.

* Support aims to ensure that end users get the maximum productivity from their use of Open ERP by
  responding to their questions on the use of the system. Support can be technical or functional.

* Maintenance aims to ensure that the system itself continues to function as required. It includes
  system upgrades, which give you access to the latest functionality available.

.. i18n: Some partners offer preventative maintenance. This makes sure that all the specific developments for
.. i18n: your system are revised and tested for each new version so that they remain compatible with the base
.. i18n: Open ERP.

Some partners offer preventative maintenance. This makes sure that all the specific developments for
your system are revised and tested for each new version so that they remain compatible with the base
Open ERP.

.. i18n: Tiny themselves have changed their support strategy from time to time. At the time of writing
.. i18n: they propose a maintenance contract supplied either direct to the end user or through partners
.. i18n: that guarantees a quick fix to any faults discovered in the covered code. Although you can 
.. i18n: expect these fixes to become available to all users of the code in time, maintenance
.. i18n: guarantees quick attention. And you're likely to get quicker migration support to new upgrades.

Tiny themselves have changed their support strategy from time to time. At the time of writing
they propose a maintenance contract supplied either direct to the end user or through partners
that guarantees a quick fix to any faults discovered in the covered code. Although you can 
expect these fixes to become available to all users of the code in time, maintenance
guarantees quick attention. And you're likely to get quicker migration support to new upgrades.

.. i18n: If you haven't anticipated your needs with a preventive maintenance contract, the costs of migration
.. i18n: after a few years can become significant. If special modules that you developed have been allowed to
.. i18n: become too old you may eventually need a new development to your specifications.

If you haven't anticipated your needs with a preventive maintenance contract, the costs of migration
after a few years can become significant. If special modules that you developed have been allowed to
become too old you may eventually need a new development to your specifications.

.. i18n: .. index:: 
.. i18n:    single: update
.. i18n:    single: upgrade
.. i18n:    
.. i18n: Updates and Upgrades
.. i18n: --------------------

.. index:: 
   single: update
   single: upgrade
   
Updates and Upgrades
--------------------

.. i18n: There are four sources of code change for Open ERP:

There are four sources of code change for Open ERP:

.. i18n: * patches supplied by Tiny to correct faults: after validation these patches shouldn't cause any
.. i18n:   secondary effects,
.. i18n: 
.. i18n: * minor updates, which gather the fault corrections together in one package, and are generally
.. i18n:   announced with a modification of the version number, such as from 5.0.0 to 5.0.1,
.. i18n: 
.. i18n: * upgrades, which bundle both the fault corrections and the improvements to the functionality in a
.. i18n:   major release such as from 5.0.3 to 5.2.0.
.. i18n: 
.. i18n: * new functions generally released in the form of new modules.

* patches supplied by Tiny to correct faults: after validation these patches shouldn't cause any
  secondary effects,

* minor updates, which gather the fault corrections together in one package, and are generally
  announced with a modification of the version number, such as from 5.0.0 to 5.0.1,

* upgrades, which bundle both the fault corrections and the improvements to the functionality in a
  major release such as from 5.0.3 to 5.2.0.

* new functions generally released in the form of new modules.

.. i18n: You should establish a procedure with your supplier to define how to respond to changes in the
.. i18n: Open ERP code.

You should establish a procedure with your supplier to define how to respond to changes in the
Open ERP code.

.. i18n: For simple updates your maintenance team will evaluate the patches to determine if they are
.. i18n: beneficial to the use of your Open ERP. These patches should be tested on an offline instance of
.. i18n: Open ERP before being installed in your live production version.

For simple updates your maintenance team will evaluate the patches to determine if they are
beneficial to the use of your Open ERP. These patches should be tested on an offline instance of
Open ERP before being installed in your live production version.

.. i18n: The maintenance team would also take charge of regular updates to the software.

The maintenance team would also take charge of regular updates to the software.

.. i18n: Patches and updates can only be installed if you have the necessary access to the Open ERP server.
.. i18n: You must first install the patch or update and then restart the server using the command line: \
.. i18n: ``–update=all``\  .

Patches and updates can only be installed if you have the necessary access to the Open ERP server.
You must first install the patch or update and then restart the server using the command line: \
``–update=all``\  .

.. i18n: Once Tiny has released a new upgraded version your response should be a cautious one. If you're
.. i18n: perfectly satisfied with the existing system it would be best to not touch the new version. If you
.. i18n: want to have access to the new functionality supplied by an upgraded version, you have a delicate
.. i18n: operation to carry out. Most upgrades require your data to be migrated because the databases before
.. i18n: and after the upgrade can be a little different.

Once Tiny has released a new upgraded version your response should be a cautious one. If you're
perfectly satisfied with the existing system it would be best to not touch the new version. If you
want to have access to the new functionality supplied by an upgraded version, you have a delicate
operation to carry out. Most upgrades require your data to be migrated because the databases before
and after the upgrade can be a little different.

.. i18n: .. index:: 
.. i18n:    single: migration

.. index:: 
   single: migration

.. i18n: Version Migration
.. i18n: -----------------

Version Migration
-----------------

.. i18n: Open ERP has a system to manage migrations semi-automatically. To update specific modules, or the whole
.. i18n: database, you only need to start the server with the argument:–\ ``update=NAME_OF_MODULE``\   or \
.. i18n: ``–update=all``\ (that's minor module changes).

Open ERP has a system to manage migrations semi-automatically. To update specific modules, or the whole
database, you only need to start the server with the argument:–\ ``update=NAME_OF_MODULE``\   or \
``–update=all``\ (that's minor module changes).

.. i18n: New stable versions of Open ERP sometimes require operations that aren't provided in the automated
.. i18n: migration. Tiny, the creator and maintainer of Open ERP, has a policy of supporting migration from
.. i18n: all official stable releases to the latest. Scripts are provided for each new release of a stable
.. i18n: version. These carry out the upgrade from the previous major version to the new major version.

New stable versions of Open ERP sometimes require operations that aren't provided in the automated
migration. Tiny, the creator and maintainer of Open ERP, has a policy of supporting migration from
all official stable releases to the latest. Scripts are provided for each new release of a stable
version. These carry out the upgrade from the previous major version to the new major version.

.. i18n: Managers responsible for the migration between two versions of Open ERP will find the
.. i18n: documentation and the necessary scripts in the directory \ ``doc/migrate``\   of the Open ERP
.. i18n: server.

Managers responsible for the migration between two versions of Open ERP will find the
documentation and the necessary scripts in the directory \ ``doc/migrate``\   of the Open ERP
server.

.. i18n: The changes between version 4 and 5 made the migration process more difficult than in the past
.. i18n: so there was a greater delay in the provision of migration assistance and more manual work
.. i18n: than usual.

The changes between version 4 and 5 made the migration process more difficult than in the past
so there was a greater delay in the provision of migration assistance and more manual work
than usual.

.. i18n: The procedure for migrating runs like this:

The procedure for migrating runs like this:

.. i18n: 	#. Make a backup of the database from the old version of Open ERP
.. i18n: 
.. i18n: 	#. Stop the server running the old version
.. i18n: 
.. i18n: 	#. Start the script called \ ``pre.py``\  for the versions you're moving between.
.. i18n: 
.. i18n: 	#. Start the new version of the server using the option –\ ``update=all``\
.. i18n: 
.. i18n: 	#. Stop the server running the new version.
.. i18n: 
.. i18n: 	#. Start the script called post.py for the versions you're moving between.
.. i18n: 
.. i18n: 	#. Start the new version of the server and test it.

	#. Make a backup of the database from the old version of Open ERP

	#. Stop the server running the old version

	#. Start the script called \ ``pre.py``\  for the versions you're moving between.

	#. Start the new version of the server using the option –\ ``update=all``\

	#. Stop the server running the new version.

	#. Start the script called post.py for the versions you're moving between.

	#. Start the new version of the server and test it.

.. i18n: A migration is never an easy process. It may be that your system doesn't function as it did before
.. i18n: or that something requires new developments in the functionality of the modules that have already
.. i18n: been installed. So you should only move to a new version if you have a real need and should engage a
.. i18n: competent partner to help if the version that you use differs greatly from the basic version of
.. i18n: Open ERP.

A migration is never an easy process. It may be that your system doesn't function as it did before
or that something requires new developments in the functionality of the modules that have already
been installed. So you should only move to a new version if you have a real need and should engage a
competent partner to help if the version that you use differs greatly from the basic version of
Open ERP.

.. i18n: Similarly you should take care that this migration does not incorrectly change any setting
.. i18n: that has already been made. The main menu structure might have been modified in place
.. i18n: without proper recording of the changes. 
.. i18n: So you could find that you're making the wrong assumptions about that structure
.. i18n: when later loading data in that was recorded with the Module Recorder.

Similarly you should take care that this migration does not incorrectly change any setting
that has already been made. The main menu structure might have been modified in place
without proper recording of the changes. 
So you could find that you're making the wrong assumptions about that structure
when later loading data in that was recorded with the Module Recorder.

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
