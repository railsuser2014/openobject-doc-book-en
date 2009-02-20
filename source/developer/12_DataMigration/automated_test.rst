===============
Automated tests
===============

This document describes all tests that are made each time someone install Open ERP on a computer. You can then assume that all these tests are valid as we must launch them before publishing a new module or a release of Open ERP.
Integrity tests on migrations

* Sum credit = Sum debit
* Balanced account chart 

---------

For automated testing, we used to do this:

* Demonstration data for each module and each object. Do demo data that goes to each branch of each workflow, by validating workflow operations in the .xml file of the demo data. If you do this, every line of every	function should be run at installation of a new db.

* To perform tests on demo data or on consistancy, use asserts tags. Then, at the end of big processes, put assert in your .XML file. If you do this, tests are processed at each installation of the database.

* To automate others kind of tests, we developed the base_quality module which is available in addons_extra. It performs tests like: all read operations on all your objects are all in O(1) and not O(n²), all fields_view_get works efficiently, etc. It also checks for respect of the guidelines: space instead of tabs, ... 

... Describe all integrity tests here


**Workflow tests**

... Describe all processus tested here.


Record creation

More than 300 records are created, describe them here. 