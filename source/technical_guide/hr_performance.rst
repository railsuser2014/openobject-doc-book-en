
Performance Review (*hr_performance*)
=====================================
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



:name: Description, char





:reviewer_id: Employee, many2one, readonly





:date_from: Date From, date, required





:state: State, selection, readonly





:date_to: Date To, date, required





:performance_id: Performance, one2many




Object: Performance Review Points
#################################



:employee_id: Employee, many2one, required, readonly





:name: Description, char





:attribute_line: Attributes, one2many





:performance: Performance in (%), float, readonly





:total: Total, float, readonly





:performance_id: Review Point, many2one




Object: Review Attributes
#########################



:note: Description, text





:name: Attribute Name, char, required





:total_point: Total Point, integer, required




Object: Attributes Lines
########################



:total_marks: Total Marks, float, readonly





:name: Description, char





:obtained_marks: Obtained Marks, float, required





:attribute_id: Attribute, many2one, required, readonly





:performance_line_id: Performance Line, many2one, readonly





:description: Description, text


