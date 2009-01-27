
Module Test New Features (*test_44*)
====================================
:Module: test_44
:Name: Test New Features
:Version: 5.0.1.0
:Directory: test_44
:Web: http://tinyerp.com

Description
-----------

::

  The module adds google map field in partner address
  so that we can directly open google map from the
  url widget.

Dependencies
------------

 * base - installed
 * sale - installed

Reports
-------

None


Menus
-------

 * Testing
 * Testing/Testing

Views
-----

 * Testing Temporal Data (form)


Objects
-------

Object: test.temporal
#####################

.. index::
  single: test.temporal object
.. 


:line_ids: Lines, one2many



.. index::
  single: line_ids field
.. 




:state: State, selection



.. index::
  single: state field
.. 




:partner_id: Partner, many2one



.. index::
  single: partner_id field
.. 




:partner_ids: Partners, many2many



.. index::
  single: partner_ids field
.. 




:name: Name, char, required



.. index::
  single: name field
.. 



Object: test.temporal.line
##########################

.. index::
  single: test.temporal.line object
.. 


:temporal_id: Temporal, many2one



.. index::
  single: temporal_id field
.. 




:length: Size, integer



.. index::
  single: length field
.. 




:name: Name, char, required



.. index::
  single: name field
.. 

