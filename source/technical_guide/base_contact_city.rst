
.. module:: base_contact_city
    :synopsis: City for base_contat 
    :noindex:
.. 

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

    <style>
      div.body p#module-base_contact_city {
        display: none;
      }
    </style>

City for base_contat (*base_contact_city*)
==========================================
:Module: base_contact_city
:Name: City for base_contat
:Version: 5.0.1.0
:Author: Pablo Rocandio
:Directory: base_contact_city
:Web: 
:Is certified: no

Description
-----------

::

  Zip code, city, state and country fields are replaced with a location field in partner form when base_contact module is installed.
  This module helps to keep homogenous address data in our database.

Dependencies
------------

 * :mod:`base`
 * :mod:`base_contact`
 * :mod:`city`

Reports
-------

None


Menus
-------


None


Views
-----

 * \* INHERIT partners_form_inherit_add_location (form)
 * \* INHERIT partners_form_inherit_del_city (form)
 * \* INHERIT partners_form_inherit_del_zip (form)
 * \* INHERIT partners_form_inherit_del_state (form)


Objects
-------

None
