
Module Import accounting entries from Bob (*account_bob_import*)
================================================================
:Module: account_bob_import
:Name: Import accounting entries from Bob
:Version: 5.0.1.0
:Directory: account_bob_import
:Web: 

Description
-----------

::

  This module provide an easy way to migrate your financial data from Bob software to OpenERP. It includes the import of
              * chart of accounts,
              * financial journals,
              * customers, suppliers and prospects,
              * contacts,
              * accounting entries
  
          Once the module is installed, all you have to do is run the configuration wizard and provide OpenERP the location of the Bob directory where is your data.

Dependencies
------------

 * base_contact - installed
 * account_l10nbe_domiciliation - installed
 * l10n_be - installed

Reports
-------

None


Menus
-------


None


Views
-----

 * Configure BOB Import (form)
 * Select Folder for BOB Import (form)


Objects
-------

Object: config.bob.import
#########################

.. index::
  single: config.bob.import object
.. 


:path: Path for BOB Folder, char

    *Supply a path that is a Bob Installation Folder.*

.. index::
  single: path field
.. 




:company_id: Company, many2one, required



.. index::
  single: company_id field
.. 




:zipped_file: Upload a Zip File, binary

    *Upload a .zip file containing information of BOB Installation'*

.. index::
  single: zipped_file field
.. 




:location: Location, selection, required

    *If this machine is the server, select 'locally' as the location.If this is the client machine, create a zip of the 'Bob' folder placed in Root(Drive Letter)://Program Files/Bob.Upload it and follow the further instructions.*

.. index::
  single: location field
.. 



Object: config.path.folder
##########################

.. index::
  single: config.path.folder object
.. 


:folder: Folder, selection, required



.. index::
  single: folder field
.. 

