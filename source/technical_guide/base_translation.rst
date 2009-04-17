
.. module:: base_translation
    :synopsis: Translation 
    :noindex:
.. 

.. raw:: html

      <br />
    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. tip:: This module is part of the Open ERP software, the leading Open Source 
  enterprise management system. If you want to discover Open ERP, check our 
  `screencasts <href="http://openerp.tv>`_ or download 
  `Open ERP <href="http://openerp.com>`_ directly.

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="base_translation"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Translation (*base_translation*)
================================
:Module: base_translation
:Name: Translation
:Version: 5.0.1.0
:Author: Tiny
:Directory: base_translation
:Web: 
:Official module: no
:Quality certified: no

Description
-----------

::

  For better translation process

Download links
--------------

You can download this module as a zip file in the following version:

  * `trunk </download/modules/trunk/base_translation.zip>`_


Dependencies
------------

 * :mod:`base`

Reports
-------

None


Menus
-------

 * Administration/Translations/Translations Management
 * Administration/Translations/Translations Management/All Contribution
 * Administration/Translations/Translations Management/Maintainer
 * Administration/Translations/Translations Management/Maintainer/Review Proposed Contribution
 * Administration/Translations/Translations Management/Contributors
 * Administration/Translations/Translations Management/Contributors/Download New Version
 * Administration/Translations/Translations Management/Maintainer/Download Contributor's Proposition
 * Administration/Translations/Translations Management/Contributors/Review Proposed Contributions
 * Administration/Translations/Translations Management/Contributors/Upload Contributions
 * Administration/Translations/Translations Management/Maintainer/Publish New Version

Views
-----

 * Translations Contrib (form)
 * Translations Contrib (tree)


Objects
-------

Object: Translation Contribution (ir.translation.contribution)
##############################################################



:lang: Language, selection





:src: Source, text





:name: Field Name, char, required





:res_id: Resource ID, integer





:upload: upload, boolean





:value: Translation Value, text





:state: Translation State, selection, readonly





:contributor_email: Email Id of Contibutor, char





:type: Type, selection


