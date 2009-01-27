
Module City (*city*)
====================
:Module: city
:Name: City
:Version: 5.0.1.0
:Directory: city
:Web: 

Description
-----------

::

  Creates a model for storing cities
  Zip code, city, state and country fields are replaced with a location field in partner and partner contact forms.
  This module helps to keep homogenous address data in the database.

Dependencies
------------

 * base - installed

Reports
-------

None


Menus
-------

 * Partners/Configuration/Localisation/Cities

Views
-----

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


Objects
-------

Object: City
############



:state_id: State, many2one, required





:name: City, char, required





:zipcode: ZIP, char, required


