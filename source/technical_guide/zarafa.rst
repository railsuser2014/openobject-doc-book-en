
.. module:: zarafa
    :synopsis: Zarafa Integration 
    :noindex:
.. 

.. tip:: This module is part of the Open ERP software, the leading Open Source 
  enterprise management system. If you want to discover Open ERP, check our 
  `screencasts <href="http://openerp.tv>`_ or download 
  `Open ERP <href="http://openerp.com>`_ directly.

.. raw:: html

      <br />
    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

Zarafa Integration (*zarafa*)
=============================
:Module: zarafa
:Name: Zarafa Integration
:Version: 5.0.1.0
:Author: Sednacom
:Directory: zarafa
:Web: http://www.sednacom.fr
:Official module: no
:Quality certified: no

Description
-----------

::

  New objetcs and views to improve use of OpenERP:
   * shortcuts view
   * module view
   * email object
   * Zarafa tools

Download links
--------------

You can download this module as a zip file in the following version:

  * `trunk </download/modules/trunk/zarafa.zip>`_


Dependencies
------------

 * :mod:`base`
 * :mod:`crm`

Reports
-------

None


Menus
-------

 * Administration/Modules Management/Modules by Sednacom
 * Tools/Shortcuts
 * Tools/Import contact from Zarafa
 * Tools/Emails

Views
-----

 * \* INHERIT res.users.form.zarafa (form)
 * \* INHERIT res.partner.address.tree.email (tree)
 * sednacom.email.form (form)
 * sednacom.email.tree (tree)


Objects
-------

Object: sednacom.email (sednacom.email)
#######################################



:body: Message, text, readonly





:name: Title, char, required, readonly





:recipients: Contacts, many2many, readonly





:datetime: Date, datetime, readonly





:to: To, char, readonly





:state: State, selection, readonly





:exp: From, char, required, readonly





:crm_case: Case, many2one, readonly




Object: Contacts, with features to import from Zarafa server (zarafa.contact)
#############################################################################



:fax: Fax, char





:name: Name, char, required





:mobile: Mobile, char





:company: Company, char





:state: State, selection, readonly





:phone: Phone, char





:zid: Z-Id, char, required





:email: Email, char, required


