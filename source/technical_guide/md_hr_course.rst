
Module Pilot Human Resources (*md_hr_course*)
=============================================
:Module: md_hr_course
:Name: Pilot Human Resources
:Version: 5.0.1.0
:Directory: md_hr_course
:Web: http://tinyerp.com/module_hr.html

Description
-----------

::

  None

Dependencies
------------

 * hr - installed

Reports
-------

None


Menus
-------

 * Human Resources
 * Human Resources/Courses
 * Human Resources/Courses/Courses
 * Human Resources/Courses/Courses by Employee

Views
-----

 * md.hr.course.form (form)
 * md.hr.course.tree (tree)
 * md.hr.course.student.form (form)
 * md.hr.course.student.tree (tree)


Objects
-------

Object: Course
##############

.. index::
  single: Course object
.. 


:code: Code, char, required



.. index::
  single: code field
.. 




:name: Course title, char, required



.. index::
  single: name field
.. 



Object: Course Student
######################

.. index::
  single: Course Student object
.. 


:payback_clause_ends: Pay back clause ends, date



.. index::
  single: payback_clause_ends field
.. 




:employee_id: Employee, many2one



.. index::
  single: employee_id field
.. 




:amount: Amount, float



.. index::
  single: amount field
.. 




:personal_contribution: Personal Contribution, boolean



.. index::
  single: personal_contribution field
.. 




:state: State, selection



.. index::
  single: state field
.. 




:payback_clause: Pay back clause (in %), float



.. index::
  single: payback_clause field
.. 




:date: Date followed, date



.. index::
  single: date field
.. 




:course_id: Course, many2one



.. index::
  single: course_id field
.. 

