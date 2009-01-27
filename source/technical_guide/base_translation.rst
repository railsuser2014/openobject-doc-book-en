
Module Translation (*base_translation*)
=======================================
:Module: base_translation
:Name: Translation
:Version: 5.0.1.0
:Directory: base_translation
:Web: 

Description
-----------

::

  For better translation process

Dependencies
------------

 * base - installed

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

Object: Translation Contribution
################################

.. index::
  single: Translation Contribution object
.. 


:lang: Language, selection



.. index::
  single: lang field
.. 




:src: Source, text



.. index::
  single: src field
.. 




:name: Field Name, char, required



.. index::
  single: name field
.. 




:res_id: Resource ID, integer



.. index::
  single: res_id field
.. 




:upload: upload, boolean



.. index::
  single: upload field
.. 




:value: Translation Value, text



.. index::
  single: value field
.. 




:state: Translation State, selection, readonly



.. index::
  single: state field
.. 




:contributor_email: Email Id of Contibutor, char



.. index::
  single: contributor_email field
.. 




:type: Type, selection



.. index::
  single: type field
.. 

