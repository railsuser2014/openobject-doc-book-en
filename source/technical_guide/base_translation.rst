
.. module:: base_translation
    :synopsis: Translation 
    :noindex:
.. 

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

    <style>
      div.body p#module-base_translation {
        display: none;
      }
    </style>

Translation (*base_translation*)
================================
:Module: base_translation
:Name: Translation
:Version: 5.0.1.0
:Author: Tiny
:Directory: base_translation
:Web: 
:Is certified: no

Description
-----------

::

  For better translation process

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


