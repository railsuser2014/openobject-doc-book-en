
Module Performance Review (*hr_performance*)
============================================
:Module: hr_performance
:Name: Performance Review
:Version: 5.0.1.0
:Directory: hr_performance
:Web: http://tinyerp.com

Description
-----------

::

  A module that Check Performance For the Company Employees.

Dependencies
------------

 * base - installed
 * hr - installed

Reports
-------

 * Performance report

Menus
-------

 * Human Resources/Performance Review/Performance HR
 * Human Resources/Performance Review/Review Attributes HR

Views
-----

 * hr.performance.form (form)
 * hr.performance.tree (tree)
 * hr.attribute.line.form (form)
 * hr.attribute.line.tree (tree)
 * hr.performance.line.attribute.form (form)
 * hr.performance.line.attribute.tree (tree)


Objects
-------

Object: Employee Performance 
#############################

.. index::
  single: Employee Performance  object
.. 


:name: Description, char



.. index::
  single: name field
.. 




:reviewer_id: Employee, many2one, readonly



.. index::
  single: reviewer_id field
.. 




:date_from: Date From, date, required



.. index::
  single: date_from field
.. 




:state: State, selection, readonly



.. index::
  single: state field
.. 




:date_to: Date To, date, required



.. index::
  single: date_to field
.. 




:performance_id: Performance, one2many



.. index::
  single: performance_id field
.. 



Object: Performance Review Points
#################################

.. index::
  single: Performance Review Points object
.. 


:employee_id: Employee, many2one, required, readonly



.. index::
  single: employee_id field
.. 




:name: Description, char



.. index::
  single: name field
.. 




:attribute_line: Attributes, one2many



.. index::
  single: attribute_line field
.. 




:performance: Performance in (%), float, readonly



.. index::
  single: performance field
.. 




:total: Total, float, readonly



.. index::
  single: total field
.. 




:performance_id: Review Point, many2one



.. index::
  single: performance_id field
.. 



Object: Review Attributes
#########################

.. index::
  single: Review Attributes object
.. 


:note: Description, text



.. index::
  single: note field
.. 




:name: Attribute Name, char, required



.. index::
  single: name field
.. 




:total_point: Total Point, integer, required



.. index::
  single: total_point field
.. 



Object: Attributes Lines
########################

.. index::
  single: Attributes Lines object
.. 


:total_marks: Total Marks, float, readonly



.. index::
  single: total_marks field
.. 




:name: Description, char



.. index::
  single: name field
.. 




:obtained_marks: Obtained Marks, float, required



.. index::
  single: obtained_marks field
.. 




:attribute_id: Attribute, many2one, required, readonly



.. index::
  single: attribute_id field
.. 




:performance_line_id: Performance Line, many2one, readonly



.. index::
  single: performance_line_id field
.. 




:description: Description, text



.. index::
  single: description field
.. 

