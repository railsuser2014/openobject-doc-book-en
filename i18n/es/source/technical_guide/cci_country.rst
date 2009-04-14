
.. i18n: .. module:: cci_country
.. i18n:     :synopsis: CCI Country 
.. i18n:     :noindex:
.. i18n: .. 

.. module:: cci_country
    :synopsis: CCI Country 
    :noindex:
.. 

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. i18n: CCI Country (*cci_country*)
.. i18n: ===========================
.. i18n: :Module: cci_country
.. i18n: :Name: CCI Country
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: CCILV
.. i18n: :Directory: cci_country
.. i18n: :Web: http://www.ccilv.be
.. i18n: :Official module: no
.. i18n: :Quality certified: no

CCI Country (*cci_country*)
===========================
:Module: cci_country
:Name: CCI Country
:Version: 5.0.1.0
:Author: CCILV
:Directory: cci_country
:Web: http://www.ccilv.be
:Official module: no
:Quality certified: no

.. i18n: Description
.. i18n: -----------

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   For some applications in the OpenERP software used by some Belgian Chamber of Commerce,we need a 
.. i18n:   table regrouping countries and areas (group of countries). 
.. i18n:   The table used by default in OpenERP doesn't answer to this need, because it's used in other and 
.. i18n:   we need to specify if this code can be used in some cases or others
.. i18n:   This table is by evidence very specific to the Chamber of Commerce dedicated modules.

::

  For some applications in the OpenERP software used by some Belgian Chamber of Commerce,we need a 
  table regrouping countries and areas (group of countries). 
  The table used by default in OpenERP doesn't answer to this need, because it's used in other and 
  we need to specify if this code can be used in some cases or others
  This table is by evidence very specific to the Chamber of Commerce dedicated modules.

.. i18n: Dependencies
.. i18n: ------------

Dependencies
------------

.. i18n:  * :mod:`base`

 * :mod:`base`

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

.. i18n:  * Partners/Configuration/Country and Area

 * Partners/Configuration/Country and Area

.. i18n: Views
.. i18n: -----

Views
-----

.. i18n:  * cci_country.form (form)
.. i18n:  * cci_country.tree (tree)

 * cci_country.form (form)
 * cci_country.tree (tree)

.. i18n: Objects
.. i18n: -------

Objects
-------

.. i18n: Object: Country or Area for CCI (cci.country)
.. i18n: #############################################

Object: Country or Area for CCI (cci.country)
#############################################

.. i18n: :cci_country_ids: Linked Countries-Areas, many2many

:cci_country_ids: Linked Countries-Areas, many2many

.. i18n: :phoneprefix: Phone Prefix, integer

:phoneprefix: Phone Prefix, integer

.. i18n: :name: Name, char, required

:name: Name, char, required

.. i18n: :valid4embassy: Embassy, boolean

:valid4embassy: Embassy, boolean

.. i18n:     *Indicates if this code can be used for Embassies*

    *Indicates if this code can be used for Embassies*

.. i18n: :description: Description, text

:description: Description, text

.. i18n: :official_name: Official Name, char

:official_name: Official Name, char

.. i18n: :postalabbrev: Postal Abbreviation, char

:postalabbrev: Postal Abbreviation, char

.. i18n: :code: Code, char, required

:code: Code, char, required

.. i18n: :valid4certificate: Certificates, boolean

:valid4certificate: Certificates, boolean

.. i18n:     *Indicates if this code can be used for certificates*

    *Indicates if this code can be used for certificates*

.. i18n: :active: Active, boolean

:active: Active, boolean

.. i18n:     *Indicates if we can still use this country-area code*

    *Indicates if we can still use this country-area code*

.. i18n: :valid4ata: ATA, boolean

:valid4ata: ATA, boolean

.. i18n:     *Indicates if this code can be used for carnets ATA*

    *Indicates if this code can be used for carnets ATA*

.. i18n: :iscountry: Country, boolean

:iscountry: Country, boolean

.. i18n:     *Indicates if this code designates a country; if False, designates an area*

    *Indicates if this code designates a country; if False, designates an area*
