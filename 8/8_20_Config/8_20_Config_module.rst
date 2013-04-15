.. index::
   pair: configuring; module

Creating a Configuration Module
===============================

It is very helpful to be able to backup your specific configuration settings in an OpenERP module
dedicated just to that. This enables you to:

* automatically duplicate the configuration settings by installing the module in another database,

* reinstall a clean database with your own configuration, in case you have problems with the initial
  configuration,

* simplify migrations. If you have modified some elements of the basic configuration, there is a risk
  in returning them to their original state after the migration, unless you have saved the modifications
  in a module.

.. index::
   single: module; base_module_record

base_module_record:  this was a developer tool we removed as almost no developer was using it. It was not clean enough to respect new OpenERP quality standards;

To install a new module saved in ZIP file form, use the menu :menuselection:`Settings -->
Modules --> Import Module`.

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

