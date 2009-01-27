
Module CCI Country (*cci_country*)
==================================
:Module: cci_country
:Name: CCI Country
:Version: 5.0.1.0
:Directory: cci_country
:Web: http://www.ccilv.be

Description
-----------

::

  For some applications in the OpenERP software used by some Belgian Chamber of Commerce,
          we need a table regrouping countries and areas (group of countries). The table used by
          default in OpenERP doesn't answer to this need, because it's used in other and we need to
          specify if this code can be used in some cases or others
          This table is by evidence very specific to the Chamber of Commerce dedicated modules.

Dependencies
------------

 * base - installed

Reports
-------

None


Menus
-------

 * Partners/Configuration/Country and Area

Views
-----

 * cci_country.form (form)
 * cci_country.tree (tree)


Objects
-------

Object: Country or Area for CCI
###############################

.. index::
  single: Country or Area for CCI object
.. 


:cci_country_ids: Linked Countries-Areas, many2many



.. index::
  single: cci_country_ids field
.. 




:phoneprefix: Phone Prefix, integer



.. index::
  single: phoneprefix field
.. 




:name: Name, char, required



.. index::
  single: name field
.. 




:valid4embassy: Embassy, boolean

    *Indicates if this code can be used for Embassies*

.. index::
  single: valid4embassy field
.. 




:description: Description, text



.. index::
  single: description field
.. 




:official_name: Official Name, char



.. index::
  single: official_name field
.. 




:postalabbrev: Postal Abbreviation, char



.. index::
  single: postalabbrev field
.. 




:code: Code, char, required



.. index::
  single: code field
.. 




:valid4certificate: Certificates, boolean

    *Indicates if this code can be used for certificates*

.. index::
  single: valid4certificate field
.. 




:active: Active, boolean

    *Indicates if we can still use this country-area code*

.. index::
  single: active field
.. 




:valid4ata: ATA, boolean

    *Indicates if this code can be used for carnets ATA*

.. index::
  single: valid4ata field
.. 




:iscountry: Country, boolean

    *Indicates if this code designates a country; if False, designates an area*

.. index::
  single: iscountry field
.. 

