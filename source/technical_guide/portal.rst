
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



:menu_id: Main Menu, many2one, required





:menu_action_id: User Menu Action, many2one, readonly

    *Default main menu for the users of the portal. This field is auto-completed at creation.*



:name: Portal Name, char, required





:company_id: Company, many2one, required





:home_action_id: User Home Action, many2one

    *Complete this field to provide a Home menu different from the Main menu.*



:group_id: Associated Group, many2one, required




Object: Portal Model
####################



:model_id: Model, many2one, required





:rule_group_id: Rule group, many2one





:view_ids: Views, many2many





:name: Name, char




Object: portal.config.install_modules_wizard
############################################



:portal_service: Portal for Service Module, boolean





:portal_sale: Portal for Sale Module, boolean





:portal_account: Portal for Account Module, boolean





:portal_analytic: Portal for Analytic Account Module, boolean


