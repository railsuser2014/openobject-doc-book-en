
Module Portal Management (*portal*)
===================================
:Module: portal
:Name: Portal Management
:Version: 5.0.0.1
:Directory: portal
:Web: http://tinyerp.com/

Description
-----------

::

  Base module to manage portal:
      - define new menu entry with associated actions.
      - add/delete menu entry easily.
      - on-the-fly rules and access control creation.

Dependencies
------------

 * base - installed

Reports
-------

None


Menus
-------

 * Portal
 * Portal/Configuration
 * Portal/Customer Portal
 * Portal/Configuration/Portals
 * Portal/Configuration/Available Models
 * Portal/Configuration/Create Menu

Views
-----

 * Portal (form)
 * Portal (tree)
 * Portal Model (form)
 * \* INHERIT ir.actions.report.custom.form.inherit (form)
 * \* INHERIT ir.actions.report_xml.form.inherit (form)
 * \* INHERIT ir.actions.wizards.form.inherit (form)
 * \* INHERIT ir.actions.windows.form.inherit (form)
 * Portal : Install extra modules (form)


Objects
-------

Object: Portal
##############

.. index::
  single: Portal object
.. 


:menu_id: Main Menu, many2one, required



.. index::
  single: menu_id field
.. 




:menu_action_id: User Menu Action, many2one, readonly

    *Default main menu for the users of the portal. This field is auto-completed at creation.*

.. index::
  single: menu_action_id field
.. 




:name: Portal Name, char, required



.. index::
  single: name field
.. 




:company_id: Company, many2one, required



.. index::
  single: company_id field
.. 




:home_action_id: User Home Action, many2one

    *Complete this field to provide a Home menu different from the Main menu.*

.. index::
  single: home_action_id field
.. 




:group_id: Associated Group, many2one, required



.. index::
  single: group_id field
.. 



Object: Portal Model
####################

.. index::
  single: Portal Model object
.. 


:model_id: Model, many2one, required



.. index::
  single: model_id field
.. 




:rule_group_id: Rule group, many2one



.. index::
  single: rule_group_id field
.. 




:view_ids: Views, many2many



.. index::
  single: view_ids field
.. 




:name: Name, char



.. index::
  single: name field
.. 



Object: portal.config.install_modules_wizard
############################################

.. index::
  single: portal.config.install_modules_wizard object
.. 


:portal_service: Portal for Service Module, boolean



.. index::
  single: portal_service field
.. 




:portal_sale: Portal for Sale Module, boolean



.. index::
  single: portal_sale field
.. 




:portal_account: Portal for Account Module, boolean



.. index::
  single: portal_account field
.. 




:portal_analytic: Portal for Analytic Account Module, boolean



.. index::
  single: portal_analytic field
.. 

