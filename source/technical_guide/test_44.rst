
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



:line_ids: Lines, one2many





:state: State, selection





:partner_id: Partner, many2one





:partner_ids: Partners, many2many





:name: Name, char, required




Object: test.temporal.line
##########################



:temporal_id: Temporal, many2one





:length: Size, integer





:name: Name, char, required


