
.. module:: sale_crm
    :synopsis: Sale CRM Stuff (Official, Quality Certified)
    :noindex:
.. 

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

Sale CRM Stuff (*sale_crm*)
===========================
:Module: sale_crm
:Name: Sale CRM Stuff
:Version: 5.0.1.0
:Author: Tiny
:Directory: sale_crm
:Web: http://www.openerp.com
:Official module: yes
:Quality certified: yes

Description
-----------

::

  This module adds a shortcut on one or several cases in the CRM.
  This shortcut allows you to generate a sale order based the selected case.
  If different cases are open (a list), it generates one sale order by
  case.
  The case is then closed and linked to the generated sale order.
  
  It also add a shortcut on one or several partners.
  This shortcut allows you to generate a CRM case for the partners.
  
  We suggest you to install this module if you installed both the sale and the
  crm_configuration modules.

Dependencies
------------

 * :mod:`sale`
 * :mod:`crm_configuration`

Reports
-------

None


Menus
-------


None


Views
-----

 * \* INHERIT CRM - Opportunities - Quote Inherit (form)


Objects
-------

None
