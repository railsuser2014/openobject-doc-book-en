
.. i18n: .. index::
.. i18n:    pair: configuring; module

.. index::
   pair: configuring; module

.. i18n: Creating a Configuration Module
.. i18n: ===============================

Creating a Configuration Module
===============================

.. i18n: It's very helpful to be able to backup your specific configuration settings in an Open ERP module
.. i18n: dedicated just to that. That enables you to:

It's very helpful to be able to backup your specific configuration settings in an Open ERP module
dedicated just to that. That enables you to:

.. i18n: * automatically duplicate the configuration settings by installing the module in another database,
.. i18n: 
.. i18n: * reinstall a clean database with your own configuration in case you have problems with the initial
.. i18n:   configuration,
.. i18n: 
.. i18n: * publish your specific configuration to benefit other companies in the same industrial sector,
.. i18n: 
.. i18n: * simplify migrations, if you have modified some elements of the basic configuration, there's a risk
.. i18n:   in returning them to their original state after the migration, unless you've saved the modifications
.. i18n:   in a module.

* automatically duplicate the configuration settings by installing the module in another database,

* reinstall a clean database with your own configuration in case you have problems with the initial
  configuration,

* publish your specific configuration to benefit other companies in the same industrial sector,

* simplify migrations, if you have modified some elements of the basic configuration, there's a risk
  in returning them to their original state after the migration, unless you've saved the modifications
  in a module.

.. i18n: .. index::
.. i18n:    single: module; base_module_record

.. index::
   single: module; base_module_record

.. i18n: Start by installing the module :mod:`base_module_record` in the usual way. Then start recording
.. i18n: your actions using the menu :menuselection:`Administration --> Modules Management --> Modules
.. i18n: Recording --> Start Recording`. Manually make all your configuration changes through the user
.. i18n: interface as you would normally (such as menu management, dashboard assignments, screen
.. i18n: configuration, new reports, and access rights management – details of some of these possibilities
.. i18n: are described later in this chapter).

Start by installing the module :mod:`base_module_record` in the usual way. Then start recording
your actions using the menu :menuselection:`Administration --> Modules Management --> Modules
Recording --> Start Recording`. Manually make all your configuration changes through the user
interface as you would normally (such as menu management, dashboard assignments, screen
configuration, new reports, and access rights management – details of some of these possibilities
are described later in this chapter).

.. i18n: Once you've done all this, go to the menu :menuselection:`Administration --> Modules Management -->
.. i18n: Modules Recording --> Save Recorded Module`.

Once you've done all this, go to the menu :menuselection:`Administration --> Modules Management -->
Modules Recording --> Save Recorded Module`.

.. i18n: .. index::
.. i18n:    single: module; base_module_publish

.. index::
   single: module; base_module_publish

.. i18n: .. note:: Contributing to the development of Open ERP
.. i18n: 
.. i18n: 	Once your personal configuration has been saved into a module, install the module
.. i18n: 	:mod:`base_module_publish`.
.. i18n: 	This gives you a new possible action :guilabel:`Publish Module` in the menu :menuselection:`Administration -->
.. i18n: 	Modules Manage --> Modules`.
.. i18n: 
.. i18n: 	Use this function to publish your module on the official Open ERP site.
.. i18n: 	It could then be reused by other companies that have the same needs as yours.
.. i18n: 	You could then yourselves benefit from improvements made by these same companies in future.
.. i18n: 
.. i18n: 	Don't forget to create a user account beforehand on http://openerp.com.

.. note:: Contributing to the development of Open ERP

	Once your personal configuration has been saved into a module, install the module
	:mod:`base_module_publish`.
	This gives you a new possible action :guilabel:`Publish Module` in the menu :menuselection:`Administration -->
	Modules Manage --> Modules`.

	Use this function to publish your module on the official Open ERP site.
	It could then be reused by other companies that have the same needs as yours.
	You could then yourselves benefit from improvements made by these same companies in future.

	Don't forget to create a user account beforehand on http://openerp.com.

.. i18n: Open ERP then creates a ZIP file for you containing all of the modifications you made while you
.. i18n: were carrying out your configuration work. You could reinstall this module on other databases and/or
.. i18n: publish it online to help other companies. This could turn out to be useful if you want to install a
.. i18n: test server for your company's users and give them the same configuration as the production server.

Open ERP then creates a ZIP file for you containing all of the modifications you made while you
were carrying out your configuration work. You could reinstall this module on other databases and/or
publish it online to help other companies. This could turn out to be useful if you want to install a
test server for your company's users and give them the same configuration as the production server.

.. i18n: To install a new module saved in ZIP file form, use the menu :menuselection:`Administration -->
.. i18n: Modules Management --> Import a new module`.

To install a new module saved in ZIP file form, use the menu :menuselection:`Administration -->
Modules Management --> Import a new module`.

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
