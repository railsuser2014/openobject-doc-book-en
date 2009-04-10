
.. i18n: .. module:: city
.. i18n:     :synopsis: City 
.. i18n:     :noindex:
.. i18n: .. 

.. module:: city
    :synopsis: City 
    :noindex:
.. 

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. i18n: City (*city*)
.. i18n: =============
.. i18n: :Module: city
.. i18n: :Name: City
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Pablo Rocandio
.. i18n: :Directory: city
.. i18n: :Web: 
.. i18n: :Official module: no
.. i18n: :Quality certified: no

City (*city*)
=============
:Module: city
:Name: City
:Version: 5.0.1.0
:Author: Pablo Rocandio
:Directory: city
:Web: 
:Official module: no
:Quality certified: no

.. i18n: Description
.. i18n: -----------

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   Creates a model for storing cities Zip code, city, state and country fields are replaced with 
.. i18n:   a location field in partner and partner contact forms.
.. i18n:   This module helps to keep homogenous address data in the database.

::

  Creates a model for storing cities Zip code, city, state and country fields are replaced with 
  a location field in partner and partner contact forms.
  This module helps to keep homogenous address data in the database.

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

.. i18n:  * Partners/Configuration/Localisation/Cities

 * Partners/Configuration/Localisation/Cities

.. i18n: Views
.. i18n: -----

Views
-----

.. i18n:  * \* INHERIT partners_form_add_location (form)
.. i18n:  * \* INHERIT partners_form_del_city (form)
.. i18n:  * \* INHERIT partners_form_del_citycity (form)
.. i18n:  * \* INHERIT partners_form_del_zip (form)
.. i18n:  * \* INHERIT partners_form_del_state (form)
.. i18n:  * \* INHERIT partners_form_add_location1 (form)
.. i18n:  * \* INHERIT partners_form_del_city1 (form)
.. i18n:  * \* INHERIT partners_form_del_zip1 (form)
.. i18n:  * \* INHERIT partners_form_del_country1 (form)
.. i18n:  * \* INHERIT partners_form_add_location2 (form)
.. i18n:  * \* INHERIT partners_form_del_city2 (form)
.. i18n:  * \* INHERIT partners_form_del_zip2 (form)
.. i18n:  * \* INHERIT partners_form_del_country2 (form)
.. i18n:  * \* INHERIT view_country_state_form2 (form)
.. i18n:  * city.city.tree (tree)
.. i18n:  * city.city.form (form)

 * \* INHERIT partners_form_add_location (form)
 * \* INHERIT partners_form_del_city (form)
 * \* INHERIT partners_form_del_citycity (form)
 * \* INHERIT partners_form_del_zip (form)
 * \* INHERIT partners_form_del_state (form)
 * \* INHERIT partners_form_add_location1 (form)
 * \* INHERIT partners_form_del_city1 (form)
 * \* INHERIT partners_form_del_zip1 (form)
 * \* INHERIT partners_form_del_country1 (form)
 * \* INHERIT partners_form_add_location2 (form)
 * \* INHERIT partners_form_del_city2 (form)
 * \* INHERIT partners_form_del_zip2 (form)
 * \* INHERIT partners_form_del_country2 (form)
 * \* INHERIT view_country_state_form2 (form)
 * city.city.tree (tree)
 * city.city.form (form)

.. i18n: Objects
.. i18n: -------

Objects
-------

.. i18n: Object: City (city.city)
.. i18n: ########################

Object: City (city.city)
########################

.. i18n: :state_id: State, many2one, required

:state_id: State, many2one, required

.. i18n: :name: City, char, required

:name: City, char, required

.. i18n: :zipcode: ZIP, char, required

:zipcode: ZIP, char, required
