
.. i18n: .. module:: account_bob_import
.. i18n:     :synopsis: Import accounting entries from Bob 
.. i18n:     :noindex:
.. i18n: .. 

.. module:: account_bob_import
    :synopsis: Import accounting entries from Bob 
    :noindex:
.. 

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. i18n: Import accounting entries from Bob (*account_bob_import*)
.. i18n: =========================================================
.. i18n: :Module: account_bob_import
.. i18n: :Name: Import accounting entries from Bob
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: account_bob_import
.. i18n: :Web: 
.. i18n: :Official module: no
.. i18n: :Quality certified: no

Import accounting entries from Bob (*account_bob_import*)
=========================================================
:Module: account_bob_import
:Name: Import accounting entries from Bob
:Version: 5.0.1.0
:Author: Tiny
:Directory: account_bob_import
:Web: 
:Official module: no
:Quality certified: no

.. i18n: Description
.. i18n: -----------

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   This module provide an easy way to migrate your financial data from Bob 
.. i18n:   software to OpenERP. It includes the import of
.. i18n:               * chart of accounts,
.. i18n:               * financial journals,
.. i18n:               * customers, suppliers and prospects,
.. i18n:               * contacts,
.. i18n:               * accounting entries
.. i18n:   
.. i18n:           Once the module is installed, all you have to do is run the configuration 
.. i18n:           wizard and provide OpenERP the location of the Bob directory where is your data.

::

  This module provide an easy way to migrate your financial data from Bob 
  software to OpenERP. It includes the import of
              * chart of accounts,
              * financial journals,
              * customers, suppliers and prospects,
              * contacts,
              * accounting entries
  
          Once the module is installed, all you have to do is run the configuration 
          wizard and provide OpenERP the location of the Bob directory where is your data.

.. i18n: Dependencies
.. i18n: ------------

Dependencies
------------

.. i18n:  * :mod:`base_contact`
.. i18n:  * :mod:`account_l10nbe_domiciliation`
.. i18n:  * :mod:`l10n_be`

 * :mod:`base_contact`
 * :mod:`account_l10nbe_domiciliation`
 * :mod:`l10n_be`

.. i18n: Reports
.. i18n: -------

Reports
-------

.. i18n: None

None

.. i18n: Menus
.. i18n: -------

Menus
-------

.. i18n: None

None

.. i18n: Views
.. i18n: -----

Views
-----

.. i18n:  * Configure BOB Import (form)
.. i18n:  * Select Folder for BOB Import (form)

 * Configure BOB Import (form)
 * Select Folder for BOB Import (form)

.. i18n: Objects
.. i18n: -------

Objects
-------

.. i18n: Object: config.bob.import (config.bob.import)
.. i18n: #############################################

Object: config.bob.import (config.bob.import)
#############################################

.. i18n: :path: Path for BOB Folder, char

:path: Path for BOB Folder, char

.. i18n:     *Supply a path that is a Bob Installation Folder.*

    *Supply a path that is a Bob Installation Folder.*

.. i18n: :company_id: Company, many2one, required

:company_id: Company, many2one, required

.. i18n: :zipped_file: Upload a Zip File, binary

:zipped_file: Upload a Zip File, binary

.. i18n:     *Upload a .zip file containing information of BOB Installation'*

    *Upload a .zip file containing information of BOB Installation'*

.. i18n: :location: Location, selection, required

:location: Location, selection, required

.. i18n:     *If this machine is the server, select 'locally' as the location.If this is the client machine, create a zip of the 'Bob' folder placed in Root(Drive Letter)://Program Files/Bob.Upload it and follow the further instructions.*

    *If this machine is the server, select 'locally' as the location.If this is the client machine, create a zip of the 'Bob' folder placed in Root(Drive Letter)://Program Files/Bob.Upload it and follow the further instructions.*

.. i18n: Object: config.path.folder (config.path.folder)
.. i18n: ###############################################

Object: config.path.folder (config.path.folder)
###############################################

.. i18n: :folder: Folder, selection, required

:folder: Folder, selection, required
